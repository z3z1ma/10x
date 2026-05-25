from __future__ import annotations

import asyncio
import json
import os
import re
import shutil
import signal
import time
from dataclasses import asdict
from pathlib import Path

from loom_mill.processes import summarize_iteration
from loom_mill.processes.backpressure import IterationRecord, detect_backpressure

from .config import HarnessConfig
from .models import OutputEvent, WorkstationState, WorkstationStatus


class WorkstationEngine:
    def __init__(
        self,
        workspace_root: Path,
        ticket_path: Path,
        harness: HarnessConfig,
        *,
        stop_timeout: float = 5.0,
    ) -> None:
        self.workspace_root = workspace_root.resolve()
        self.ticket_path = ticket_path.resolve()
        self.harness = harness
        self.stop_timeout = stop_timeout
        self.state = WorkstationState()
        self.output_queue: asyncio.Queue[OutputEvent] = asyncio.Queue()
        self._process: asyncio.subprocess.Process | None = None
        self._capture_tasks: list[asyncio.Task[None]] = []
        self._wait_task: asyncio.Task[int] | None = None
        self._iteration = 0
        self._iteration_started_at: float | None = None

    async def start(self) -> WorkstationState:
        if self.state.status != WorkstationStatus.IDLE:
            raise RuntimeError(f"cannot start workstation from {self.state.status}")

        worktree_path = self.workspace_root / ".mill" / "worktrees" / self._ticket_slug()
        worktree_path.parent.mkdir(parents=True, exist_ok=True)
        await self._run_git("worktree", "add", "--detach", str(worktree_path), "HEAD")
        return await self._launch(worktree_path)

    async def resume(self) -> WorkstationState:
        if self.state.status != WorkstationStatus.PAUSED:
            raise RuntimeError(f"cannot resume workstation from {self.state.status}")
        if self.state.worktree_path is None:
            raise RuntimeError("cannot resume workstation without a worktree")
        if self._wait_task is not None:
            await self._wait_task

        self.state.andon.active = False
        self.state.andon.signals = []
        return await self._launch(self.state.worktree_path)

    def acknowledge_andon(self) -> WorkstationState:
        self.state.andon.active = False
        self.state.andon.signals = []
        return self.state

    async def _launch(self, worktree_path: Path) -> WorkstationState:
        if not worktree_path.exists():
            raise RuntimeError("cannot launch workstation without an existing worktree")

        env = os.environ.copy()
        if self.harness.env:
            env.update(self.harness.env)

        process = await asyncio.create_subprocess_exec(
            *self.harness.command_line(self.ticket_path),
            cwd=self._process_cwd(worktree_path),
            env=env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        self._process = process
        self._iteration += 1
        self._iteration_started_at = time.monotonic()
        self.state.status = WorkstationStatus.RUNNING
        self.state.worktree_path = worktree_path
        self.state.process_id = process.pid
        self.state.exit_code = None
        self.state.iteration_summary = None
        self.state.backpressure_signals = []
        self._capture_tasks = [
            asyncio.create_task(self._capture_stream("stdout", process.stdout)),
            asyncio.create_task(self._capture_stream("stderr", process.stderr)),
        ]
        self._wait_task = asyncio.create_task(self._wait_for_exit())
        return self.state

    async def wait(self) -> WorkstationState:
        if self._wait_task is None:
            return self.state
        await self._wait_task
        return self.state

    async def stop(self) -> WorkstationState:
        return await self._terminate(WorkstationStatus.STOPPED)

    async def pause(self) -> WorkstationState:
        return await self._terminate(WorkstationStatus.PAUSED)

    async def teardown(self) -> None:
        if self.state.status == WorkstationStatus.RUNNING:
            raise RuntimeError("cannot teardown a running workstation")
        if self.state.worktree_path is None:
            return

        worktree_path = self.state.worktree_path
        await self._run_git("worktree", "remove", "--force", str(worktree_path))
        if worktree_path.exists():
            shutil.rmtree(worktree_path)

    async def _terminate(self, status: WorkstationStatus) -> WorkstationState:
        process = self._process
        if process is None or process.returncode is not None:
            self.state.status = status
            return self.state

        self.state.status = status
        process.send_signal(signal.SIGTERM)
        try:
            await asyncio.wait_for(process.wait(), timeout=self.stop_timeout)
        except TimeoutError:
            process.kill()
            await process.wait()

        await asyncio.gather(*self._capture_tasks)
        self.state.exit_code = process.returncode
        await self._summarize_exit()
        return self.state

    async def _wait_for_exit(self) -> int:
        if self._process is None:
            raise RuntimeError("workstation process was not started")
        exit_code = await self._process.wait()
        await asyncio.gather(*self._capture_tasks)
        self.state.exit_code = exit_code
        if self.state.status == WorkstationStatus.RUNNING:
            self.state.status = WorkstationStatus.COMPLETED
            await self._check_backpressure(exit_code)
        await self._summarize_exit()
        return exit_code

    async def _capture_stream(
        self,
        stream: str,
        reader: asyncio.StreamReader | None,
    ) -> None:
        if reader is None:
            return
        while chunk := await reader.read(4096):
            event = OutputEvent(stream=stream, data=chunk.decode(errors="replace"))
            self.state.output.append(event)
            await self.output_queue.put(event)

    async def _run_git(self, *args: str) -> None:
        process = await asyncio.create_subprocess_exec(
            "git",
            *args,
            cwd=self.workspace_root,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await process.communicate()
        if process.returncode != 0:
            message = stderr.decode(errors="replace").strip()
            raise RuntimeError(f"git {' '.join(args)} failed: {message}")

    async def _git_output(self, cwd: Path, *args: str) -> str:
        process = await asyncio.create_subprocess_exec(
            "git",
            *args,
            cwd=cwd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            message = stderr.decode(errors="replace").strip()
            raise RuntimeError(f"git {' '.join(args)} failed: {message}")
        return stdout.decode(errors="replace")

    async def _check_backpressure(self, exit_code: int) -> None:
        if self.state.worktree_path is None:
            return

        started_at = self._iteration_started_at or time.monotonic()
        duration_seconds = time.monotonic() - started_at
        history = self._load_iteration_history()
        output_tail = "".join(event.data for event in self.state.output)[-4000:]
        loom_changed = bool((await self._git_output(self.state.worktree_path, "status", "--porcelain", "--", ".loom")).strip())
        history.append(
            IterationRecord(
                exit_code=exit_code,
                duration_seconds=duration_seconds,
                loom_changed=loom_changed,
                output_tail=output_tail,
            )
        )
        self._save_iteration_history(history)
        signals = detect_backpressure(history)
        self.state.backpressure_signals = signals
        alerts = [signal for signal in signals if signal.severity == "alert"]
        if alerts:
            self.state.andon.active = True
            self.state.andon.signals = alerts
            self.state.status = WorkstationStatus.PAUSED

    async def _summarize_exit(self) -> None:
        if self.state.iteration_summary is not None:
            return
        if self.state.worktree_path is None or self._iteration_started_at is None:
            return
        duration = time.monotonic() - self._iteration_started_at
        self.state.iteration_summary = await summarize_iteration(
            workspace_root=self.workspace_root,
            worktree_path=self.state.worktree_path,
            ticket_slug=self._ticket_slug(),
            iteration=self._iteration,
            exit_code=self.state.exit_code,
            duration_seconds=duration,
        )

    def _pattern_path(self) -> Path:
        return self.workspace_root / ".mill" / "patterns" / f"{self._ticket_slug()}.json"

    def _load_iteration_history(self) -> list[IterationRecord]:
        path = self._pattern_path()
        if not path.exists():
            return []
        data = json.loads(path.read_text(encoding="utf-8"))
        return [IterationRecord(**item) for item in data]

    def _save_iteration_history(self, history: list[IterationRecord]) -> None:
        path = self._pattern_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps([asdict(record) for record in history], indent=2) + "\n", encoding="utf-8")

    def _process_cwd(self, worktree_path: Path) -> Path:
        if self.harness.cwd is None:
            return worktree_path
        cwd = Path(self.harness.cwd)
        return cwd if cwd.is_absolute() else worktree_path / cwd

    def _ticket_slug(self) -> str:
        stem = self.ticket_path.stem.lower()
        slug = re.sub(r"[^a-z0-9._-]+", "-", stem).strip("-._")
        return slug or "workstation"
