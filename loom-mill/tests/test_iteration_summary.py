from __future__ import annotations

import asyncio
import json
from pathlib import Path

import pytest
import pytest_asyncio

from loom_mill.processes import summarize_iteration
from loom_mill.workstation import HarnessConfig, WorkstationEngine, WorkstationStatus


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
    ticket_path = tmp_path / ".loom" / "tickets" / "example-ticket.md"
    ticket_path.parent.mkdir(parents=True)
    ticket_path.write_text(
        "# Example Ticket\n\nID: ticket:example-ticket\nType: Ticket\nStatus: active\nUpdated: 2026-05-25\n",
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text("test repo\n", encoding="utf-8")
    await _run(["git", "add", "."], tmp_path)
    await _run(["git", "commit", "-m", "initial"], tmp_path)
    return tmp_path


@pytest.mark.asyncio
async def test_summarize_iteration_records_files_records_and_exit_status(git_workspace: Path) -> None:
    worktree_path = git_workspace / ".mill" / "worktrees" / "example-ticket"
    worktree_path.parent.mkdir(parents=True)
    await _run(["git", "worktree", "add", "--detach", str(worktree_path), "HEAD"], git_workspace)
    (worktree_path / "README.md").write_text("test repo\nchanged\n", encoding="utf-8")
    (worktree_path / ".loom" / "tickets" / "example-ticket.md").write_text(
        "# Example Ticket\n\nID: ticket:example-ticket\nType: Ticket\nStatus: review\nUpdated: 2026-05-26\n",
        encoding="utf-8",
    )

    summary = await summarize_iteration(
        workspace_root=git_workspace,
        worktree_path=worktree_path,
        ticket_slug="example-ticket",
        iteration=1,
        exit_code=7,
        duration_seconds=1.23456,
    )

    assert summary.label.startswith("iteration summary")
    assert summary.exit_code == 7
    assert summary.files_changed.count == 2
    assert summary.files_changed.paths == [".loom/tickets/example-ticket.md", "README.md"]
    assert summary.records_changed[0].record_id == "ticket:example-ticket"
    assert summary.records_changed[0].changed_fields == ["status", "updated"]
    stored = json.loads(Path(summary.storage_path).read_text(encoding="utf-8"))
    assert stored["label"] == "iteration summary (visibility output, not evidence, audit, or acceptance)"


@pytest.mark.asyncio
async def test_workstation_writes_iteration_summary_after_process_exit(git_workspace: Path) -> None:
    ticket_path = git_workspace / ".loom" / "tickets" / "example-ticket.md"
    engine = WorkstationEngine(
        git_workspace,
        ticket_path,
        HarnessConfig(
            command="python",
            args=[
                "-c",
                "from pathlib import Path; Path('README.md').write_text('changed\\n'); Path('.loom/tickets/example-ticket.md').write_text('# Example Ticket\\n\\nID: ticket:example-ticket\\nType: Ticket\\nStatus: review\\nUpdated: 2026-05-26\\n')",
            ],
        ),
    )

    await engine.start()
    await engine.wait()

    assert engine.state.status == WorkstationStatus.COMPLETED
    assert engine.state.iteration_summary is not None
    assert engine.state.iteration_summary.files_changed.paths == [".loom/tickets/example-ticket.md", "README.md"]
    assert engine.state.iteration_summary.records_changed[0].changed_fields == ["status", "updated"]
    assert (git_workspace / ".mill" / "summaries" / "example-ticket" / "iteration-1.json").exists()
