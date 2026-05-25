from __future__ import annotations

import asyncio
from pathlib import Path

from watchfiles import Change, awatch

from loom_mill.parser import parse_record, parse_records
from loom_mill.state import GitState, GitStateChanged, MillStateStore, RecordAdded, RecordChanged, RecordRemoved


class LoomWatcher:
    def __init__(self, workspace_root: str | Path, *, store: MillStateStore | None = None) -> None:
        self.workspace_root = Path(workspace_root).resolve()
        self.loom_path = self.workspace_root / ".loom"
        self.git_path = self.workspace_root / ".git"
        self.store = store or MillStateStore()
        self._tasks: list[asyncio.Task[None]] = []

    async def __aenter__(self) -> LoomWatcher:
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.stop()

    async def start(self) -> None:
        if self._tasks:
            return
        await self.refresh_all()
        if self.loom_path.exists():
            self._tasks.append(asyncio.create_task(self._watch_loom()))
        if self.git_path.exists():
            self._tasks.append(asyncio.create_task(self._watch_git()))
            self._tasks.append(asyncio.create_task(self._poll_git()))
        if self._tasks:
            await asyncio.sleep(0.1)

    async def stop(self) -> None:
        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks = []

    async def refresh_all(self) -> None:
        graph = parse_records(self.loom_path)
        await self.store.replace_all_records(graph.records)
        await self.refresh_git_state()

    async def refresh_git_state(self) -> None:
        git = await read_git_state(self.workspace_root)
        previous = await self.store.replace_git_state(git)
        if git != previous:
            await self.store.publish(GitStateChanged(git=git, previous=previous))

    async def apply_record_path(self, path: str | Path, change: Change | None = None) -> None:
        record_path = Path(path)
        if record_path.suffix != ".md":
            return
        try:
            display_path = str(record_path.resolve().relative_to(self.loom_path))
        except ValueError:
            return

        if change == Change.deleted or not record_path.exists():
            previous = await self.store.remove_record(display_path)
            if previous is not None:
                await self.store.publish(RecordRemoved(path=display_path, previous=previous))
            return

        record = parse_record(record_path, root=self.loom_path)
        if record is None:
            previous = await self.store.remove_record(display_path)
            if previous is not None:
                await self.store.publish(RecordRemoved(path=display_path, previous=previous))
            return

        previous = await self.store.replace_record(record)
        if previous is None:
            await self.store.publish(RecordAdded(path=record.path, record=record))
        elif previous != record:
            await self.store.publish(RecordChanged(path=record.path, record=record, previous=previous))

    async def _watch_loom(self) -> None:
        async for changes in awatch(self.loom_path, debounce=100, step=50):
            for change, path in changes:
                await self.apply_record_path(path, change)

    async def _watch_git(self) -> None:
        async for _changes in awatch(self.git_path, debounce=100, step=50):
            await self.refresh_git_state()

    async def _poll_git(self) -> None:
        while True:
            await asyncio.sleep(0.25)
            await self.refresh_git_state()


async def read_git_state(workspace_root: str | Path) -> GitState:
    root = Path(workspace_root)
    branch = await _git_output(root, "rev-parse", "--abbrev-ref", "HEAD")
    commits = await _git_output(root, "log", "--oneline", "-10")
    status = await _git_output(root, "status", "--porcelain")
    return GitState(
        current_branch=branch.strip() or None,
        recent_commits=tuple(line for line in commits.splitlines() if line),
        dirty=bool(status.strip()),
    )


async def _git_output(root: Path, *args: str) -> str:
    process = await asyncio.create_subprocess_exec(
        "git",
        *args,
        cwd=root,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, _stderr = await process.communicate()
    if process.returncode != 0:
        return ""
    return stdout.decode(errors="replace")
