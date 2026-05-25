from __future__ import annotations

import asyncio
from collections.abc import Callable
from pathlib import Path

import pytest
import pytest_asyncio

from loom_mill.state import GitStateChanged, MillEvent, RecordAdded, RecordChanged, RecordRemoved
from loom_mill.watcher import LoomWatcher


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


async def _next_event(
    stream,
    predicate: Callable[[MillEvent], bool],
    *,
    timeout: float = 1.0,
) -> MillEvent:
    deadline = asyncio.get_running_loop().time() + timeout
    while True:
        remaining = deadline - asyncio.get_running_loop().time()
        assert remaining > 0, "timed out waiting for watcher event"
        event = await asyncio.wait_for(anext(stream), remaining)
        if predicate(event):
            return event


@pytest_asyncio.fixture
async def git_workspace(tmp_path: Path) -> Path:
    await _run(["git", "init"], tmp_path)
    await _run(["git", "config", "user.email", "mill@example.invalid"], tmp_path)
    await _run(["git", "config", "user.name", "Mill Test"], tmp_path)
    (tmp_path / ".loom" / "tickets").mkdir(parents=True)
    (tmp_path / "README.md").write_text("test repo\n", encoding="utf-8")
    await _run(["git", "add", "."], tmp_path)
    await _run(["git", "commit", "-m", "initial"], tmp_path)
    return tmp_path


@pytest.mark.asyncio
async def test_loom_file_changes_emit_record_events_within_one_second(git_workspace: Path) -> None:
    watcher = LoomWatcher(git_workspace)
    async with watcher:
        stream = watcher.store.subscribe()
        try:
            ticket_path = git_workspace / ".loom" / "tickets" / "example.md"
            ticket_path.write_text(
                """# Example

ID: ticket:20260525-example
Type: Ticket
Status: open
Created: 2026-05-25
Updated: 2026-05-25

## Acceptance

- ACC-001: Initial.
""",
                encoding="utf-8",
            )

            added = await _next_event(stream, lambda event: isinstance(event, RecordAdded))
            assert isinstance(added, RecordAdded)
            assert added.path == "tickets/example.md"
            assert added.record.metadata.id == "ticket:20260525-example"

            ticket_path.write_text(
                ticket_path.read_text(encoding="utf-8").replace("Status: open", "Status: active"),
                encoding="utf-8",
            )

            changed = await _next_event(stream, lambda event: isinstance(event, RecordChanged))
            assert isinstance(changed, RecordChanged)
            assert changed.record.metadata.status == "active"
            assert changed.previous.metadata.status == "open"

            ticket_path.unlink()

            removed = await _next_event(stream, lambda event: isinstance(event, RecordRemoved))
            assert isinstance(removed, RecordRemoved)
            assert removed.previous.metadata.id == "ticket:20260525-example"
        finally:
            await stream.aclose()


@pytest.mark.asyncio
async def test_git_state_updates_from_git_operations(git_workspace: Path) -> None:
    watcher = LoomWatcher(git_workspace)
    async with watcher:
        stream = watcher.store.subscribe()
        try:
            snapshot = await watcher.store.snapshot()
            assert snapshot.git.current_branch in {"main", "master"}
            assert snapshot.git.recent_commits
            assert snapshot.git.dirty is False

            (git_workspace / "README.md").write_text("test repo\nchanged\n", encoding="utf-8")
            await _run(["git", "add", "README.md"], git_workspace)
            await _run(["git", "commit", "-m", "second"], git_workspace)

            event = await _next_event(
                stream,
                lambda item: isinstance(item, GitStateChanged)
                and any("second" in commit for commit in item.git.recent_commits),
                timeout=3.0,
            )
            assert isinstance(event, GitStateChanged)
            assert event.git.dirty is False
            assert "second" in event.git.recent_commits[0]
        finally:
            await stream.aclose()


@pytest.mark.asyncio
async def test_state_snapshot_and_subscription_api(git_workspace: Path) -> None:
    watcher = LoomWatcher(git_workspace)
    await watcher.refresh_all()
    stream = watcher.store.subscribe()
    try:
        ticket_path = git_workspace / ".loom" / "tickets" / "manual.md"
        ticket_path.write_text(
            """# Manual

ID: ticket:20260525-manual
Type: Ticket
Status: review
Created: 2026-05-25
Updated: 2026-05-25
""",
            encoding="utf-8",
        )

        await watcher.apply_record_path(ticket_path)
        event = await _next_event(stream, lambda item: isinstance(item, RecordAdded))
        snapshot = await watcher.store.snapshot()

        assert isinstance(event, RecordAdded)
        assert [record.metadata.id for record in snapshot.records] == ["ticket:20260525-manual"]
        assert snapshot.git.current_branch in {"main", "master"}
    finally:
        await stream.aclose()
