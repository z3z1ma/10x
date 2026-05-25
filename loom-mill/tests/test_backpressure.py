from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
import pytest_asyncio

from loom_mill.processes.backpressure import IterationRecord, detect_backpressure
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
    ticket_path.write_text("# Example Ticket\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("test repo\n", encoding="utf-8")
    await _run(["git", "add", "."], tmp_path)
    await _run(["git", "commit", "-m", "initial"], tmp_path)
    return tmp_path


def test_repeated_failure_signal_after_same_exit_code_three_times() -> None:
    history = [
        IterationRecord(exit_code=7, duration_seconds=12, loom_changed=False),
        IterationRecord(exit_code=7, duration_seconds=10, loom_changed=False),
        IterationRecord(exit_code=7, duration_seconds=11, loom_changed=False),
    ]

    signals = detect_backpressure(history)

    assert any(signal.kind == "repeated_failure" and signal.severity == "alert" for signal in signals)


def test_long_iteration_signal_uses_previous_median() -> None:
    history = [
        IterationRecord(exit_code=0, duration_seconds=10, loom_changed=True),
        IterationRecord(exit_code=0, duration_seconds=12, loom_changed=True),
        IterationRecord(exit_code=0, duration_seconds=25, loom_changed=True),
    ]

    signals = detect_backpressure(history)

    assert any(signal.kind == "long_iteration" and signal.severity == "warning" for signal in signals)


@pytest.mark.asyncio
async def test_no_record_change_after_successful_iteration_warns(git_workspace: Path) -> None:
    ticket_path = git_workspace / ".loom" / "tickets" / "example-ticket.md"
    engine = WorkstationEngine(
        git_workspace,
        ticket_path,
        HarnessConfig(command="python", args=["-c", "print('no-op')"]),
    )

    await engine.start()
    await engine.wait()

    assert engine.state.status == WorkstationStatus.COMPLETED
    assert any(signal.kind == "no_record_change" for signal in engine.state.backpressure_signals)


@pytest.mark.asyncio
async def test_repeated_failure_raises_andon_and_holds_workstation(git_workspace: Path) -> None:
    ticket_path = git_workspace / ".loom" / "tickets" / "example-ticket.md"

    for _ in range(3):
        engine = WorkstationEngine(
            git_workspace,
            ticket_path,
            HarnessConfig(command="python", args=["-c", "import sys; print('bad'); raise SystemExit(3)"]),
        )
        await engine.start()
        await engine.wait()
        if not engine.state.andon.active:
            await engine.teardown()

    assert engine.state.status == WorkstationStatus.PAUSED
    assert engine.state.andon.active
    assert any(signal.kind == "repeated_failure" for signal in engine.state.andon.signals)
    with pytest.raises(RuntimeError, match="cannot start workstation"):
        await engine.start()

    engine.acknowledge_andon()
    assert not engine.state.andon.active
