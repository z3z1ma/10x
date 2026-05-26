from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import pytest_asyncio

from loom_mill.api.workstation import delete_workstation, get_workstation, list_workstations, start_workstation
from loom_mill.api.ws import _event_payload
from loom_mill.state import MillStateStore, WorkstationStateChanged
from loom_mill.workstation import FactoryConfig, HarnessConfig, WorkstationStatus
from loom_mill.workstation.manager import WorkstationManager


class FakeRequest:
    def __init__(self, app, data: dict | None = None, path_params: dict | None = None) -> None:
        self.app = app
        self.path_params = path_params or {}
        self._data = data or {}

    async def json(self) -> dict:
        return self._data


async def _run(command: list[str], cwd: Path) -> str:
    process = await asyncio.create_subprocess_exec(
        *command,
        cwd=cwd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    assert process.returncode == 0, stderr.decode(errors="replace")
    return stdout.decode(errors="replace")


@pytest_asyncio.fixture
async def git_workspace(tmp_path: Path) -> Path:
    await _run(["git", "init"], tmp_path)
    await _run(["git", "config", "user.email", "mill@example.invalid"], tmp_path)
    await _run(["git", "config", "user.name", "Mill Test"], tmp_path)
    ticket_dir = tmp_path / ".loom" / "tickets"
    ticket_dir.mkdir(parents=True)
    for name in ["ticket-a", "ticket-b", "ticket-c"]:
        (ticket_dir / f"{name}.md").write_text(f"# {name}\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("test repo\n", encoding="utf-8")
    await _run(["git", "add", "."], tmp_path)
    await _run(["git", "commit", "-m", "initial"], tmp_path)
    return tmp_path


@pytest.mark.asyncio
async def test_manager_starts_three_independent_workstations(git_workspace: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(
        git_workspace,
        store,
        FactoryConfig(
            max_workstations=3,
            harness=HarnessConfig(command=sys.executable, args=["-c", "import time; time.sleep(1)"]),
        ),
    )

    engines = []
    for ticket_id in ["ticket-a", "ticket-b", "ticket-c"]:
        engines.append(await manager.start(git_workspace / ".loom" / "tickets" / f"{ticket_id}.md", ticket_id))

    assert len({engine.workstation_id for engine in engines}) == 3
    assert len({engine.state.worktree_path for engine in engines}) == 3
    assert {engine.ticket_id for engine in engines} == {"ticket-a", "ticket-b", "ticket-c"}
    assert all(engine.state.status == WorkstationStatus.RUNNING for engine in engines)
    assert all(engine.state.process_id is not None for engine in engines)

    await manager.shutdown()


@pytest.mark.asyncio
async def test_manager_enforces_wip_limit(git_workspace: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(
        git_workspace,
        store,
        FactoryConfig(
            max_workstations=2,
            harness=HarnessConfig(command=sys.executable, args=["-c", "import time; time.sleep(1)"]),
        ),
    )

    await manager.start(git_workspace / ".loom" / "tickets" / "ticket-a.md", "ticket-a")
    await manager.start(git_workspace / ".loom" / "tickets" / "ticket-b.md", "ticket-b")

    with pytest.raises(RuntimeError, match="WIP limit reached"):
        await manager.start(git_workspace / ".loom" / "tickets" / "ticket-c.md", "ticket-c")

    await manager.shutdown()


@pytest.mark.asyncio
async def test_pause_one_workstation_leaves_other_running(git_workspace: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(
        git_workspace,
        store,
        FactoryConfig(
            max_workstations=2,
            harness=HarnessConfig(command=sys.executable, args=["-c", "import time; time.sleep(10)"]),
        ),
    )
    first = await manager.start(git_workspace / ".loom" / "tickets" / "ticket-a.md", "ticket-a")
    second = await manager.start(git_workspace / ".loom" / "tickets" / "ticket-b.md", "ticket-b")

    await manager.pause(first.workstation_id)

    assert first.state.status == WorkstationStatus.PAUSED
    assert second.state.status == WorkstationStatus.RUNNING

    await manager.shutdown()


@pytest.mark.asyncio
async def test_websocket_workstation_event_payload_includes_workstation_id(git_workspace: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(
        git_workspace,
        store,
        FactoryConfig(harness=HarnessConfig(command=sys.executable, args=["-c", "print('done')"])),
    )
    engine = await manager.start(git_workspace / ".loom" / "tickets" / "ticket-a.md", "ticket-a")

    payload = _event_payload(WorkstationStateChanged(workstation_id=engine.workstation_id, workstation=engine.state))

    assert payload["workstation_id"] == engine.workstation_id
    assert payload["event"] == "state_change"
    assert payload["payload"]["ticket_id"] == "ticket-a"

    await manager.shutdown()


@pytest.mark.asyncio
async def test_rest_endpoints_start_list_get_and_enforce_wip(git_workspace: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(
        git_workspace,
        store,
        FactoryConfig(
            max_workstations=1,
            harness=HarnessConfig(command=sys.executable, args=["-c", "import time; time.sleep(1)"]),
        ),
    )
    app = SimpleNamespace(
        state=SimpleNamespace(
            workspace_root=str(git_workspace),
            workstation_manager=manager,
        )
    )

    created = await start_workstation(FakeRequest(app, {"ticket_id": "ticket-a"}))
    assert created.status_code == 200
    workstation_id = json.loads(created.body)["id"]

    listed = await list_workstations(FakeRequest(app))
    assert listed.status_code == 200
    assert [item["id"] for item in json.loads(listed.body)] == [workstation_id]

    fetched = await get_workstation(FakeRequest(app, path_params={"workstation_id": workstation_id}))
    assert fetched.status_code == 200
    assert json.loads(fetched.body)["ticket_id"] == "ticket-a"

    blocked = await start_workstation(FakeRequest(app, {"ticket_id": "ticket-b"}))
    assert blocked.status_code == 409
    assert "WIP limit reached" in json.loads(blocked.body)["error"]

    deleted = await delete_workstation(FakeRequest(app, path_params={"workstation_id": workstation_id}))
    assert deleted.status_code == 200
