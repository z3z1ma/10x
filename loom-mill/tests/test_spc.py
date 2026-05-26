from __future__ import annotations

import asyncio
from dataclasses import asdict
from pathlib import Path

import pytest

from loom_mill.api.ws import _event_payload
from loom_mill.iterations import IterationRecord, IterationStore
from loom_mill.processes import SPCEngine
from loom_mill.state import MillStateStore, WorkstationAndon, WorkstationIterationCompleted
from loom_mill.workstation import FactoryConfig, WorkstationState, WorkstationStatus
from loom_mill.workstation.manager import WorkstationManager


def iteration(
    number: int,
    *,
    duration_seconds: float = 10,
    exit_code: int | None = 0,
    files_changed: list[str] | None = None,
    lines_added: int = 1,
    lines_removed: int = 0,
    failing_tests: list[str] | None = None,
) -> dict:
    data = asdict(
        IterationRecord(
            iteration=number,
            started_at="2026-05-25T00:00:00Z",
            ended_at="2026-05-25T00:01:00Z",
            duration_seconds=duration_seconds,
            exit_code=exit_code,
            commit_sha=f"sha-{number}",
            files_changed=files_changed or [],
            lines_added=lines_added,
            lines_removed=lines_removed,
            diff_stat=f"+{lines_added} -{lines_removed} across {len(files_changed or [])} files",
        )
    )
    if failing_tests is not None:
        data["failing_tests"] = failing_tests
    return data


def record(number: int, *, lines_added: int = 0, lines_removed: int = 0) -> IterationRecord:
    return IterationRecord(
        iteration=number,
        started_at="2026-05-25T00:00:00Z",
        ended_at="2026-05-25T00:01:00Z",
        duration_seconds=10,
        exit_code=0,
        commit_sha=f"sha-{number}",
        files_changed=[],
        lines_added=lines_added,
        lines_removed=lines_removed,
        diff_stat=f"+{lines_added} -{lines_removed} across 0 files",
    )


@pytest.mark.asyncio
async def test_spc_advisory_receives_structured_input_and_parses_signal() -> None:
    calls = []

    async def advisory(payload: dict) -> dict:
        calls.append(payload)
        return {"signal": "alert", "reasoning": "watch duration", "patterns": ["duration_escalation"]}

    signal = await SPCEngine(FactoryConfig(spc_model="spc-test"), advisory_fn=advisory).analyze(
        "ws-abc",
        [iteration(1, duration_seconds=5, files_changed=["a.py"], lines_added=3, lines_removed=1, exit_code=0)],
    )

    assert signal.signal == "alert"
    assert signal.reasoning == "watch duration"
    assert signal.patterns_detected == ["duration_escalation"]
    assert calls[0] == {
        "workstation_id": "ws-abc",
        "model": "spc-test",
        "iterations": [
            {
                "iteration": 1,
                "duration_seconds": 5,
                "files_changed": ["a.py"],
                "lines_added": 3,
                "lines_removed": 1,
                "exit_code": 0,
            }
        ],
    }


@pytest.mark.asyncio
async def test_spc_timeout_falls_back_to_deterministic_rules() -> None:
    async def slow_advisory(payload: dict) -> dict:
        await asyncio.sleep(0.05)
        return {"signal": "continue", "reasoning": "late", "patterns": []}

    signal = await SPCEngine(
        FactoryConfig(spc_model="spc-test", spc_timeout_seconds=0.01),
        advisory_fn=slow_advisory,
    ).analyze("ws-abc", [iteration(1, lines_added=0), iteration(2, lines_added=0)])

    assert signal.signal == "stop"
    assert signal.patterns_detected == ["stall"]


@pytest.mark.asyncio
async def test_deterministic_rules_detect_required_patterns_and_thresholds() -> None:
    engine = SPCEngine(FactoryConfig())

    repetition = await engine.analyze("ws", [iteration(1, failing_tests=["test_a"]), iteration(2, failing_tests=["test_a"]), iteration(3, failing_tests=["test_a"])])
    churn = await engine.analyze("ws", [iteration(1, files_changed=["a.py"]), iteration(2, files_changed=["a.py"]), iteration(3, files_changed=["a.py"])])
    escalation = await engine.analyze("ws", [iteration(1, duration_seconds=1), iteration(2, duration_seconds=2), iteration(3, duration_seconds=3)])
    stall = await engine.analyze("ws", [iteration(1, lines_added=0), iteration(2, lines_added=0)])
    custom = await SPCEngine(FactoryConfig(spc_thresholds={"churn_count": 2})).analyze(
        "ws",
        [iteration(1, files_changed=["b.py"]), iteration(2, files_changed=["b.py"])],
    )

    assert repetition.signal == "stop"
    assert "repetition" in repetition.patterns_detected
    assert churn.signal == "alert"
    assert churn.patterns_detected == ["file_churn"]
    assert escalation.signal == "alert"
    assert escalation.patterns_detected == ["duration_escalation"]
    assert stall.signal == "stop"
    assert stall.patterns_detected == ["stall"]
    assert custom.signal == "alert"


class FakeEngine:
    def __init__(self, workstation_id: str) -> None:
        self.workstation_id = workstation_id
        self.state = WorkstationState(id=workstation_id, ticket_id="example", status=WorkstationStatus.RUNNING)
        self.iteration_queue: asyncio.Queue[IterationRecord] = asyncio.Queue()

    async def pause(self) -> WorkstationState:
        self.state.status = WorkstationStatus.PAUSED
        return self.state

    def wait_done(self) -> bool:
        return True


@pytest.mark.asyncio
async def test_manager_runs_spc_after_iteration_stores_signal_and_emits_andon(tmp_path: Path) -> None:
    store = MillStateStore()
    manager = WorkstationManager(tmp_path, store, FactoryConfig())
    engine = FakeEngine("ws-abc")
    manager.workstations[engine.workstation_id] = engine  # type: ignore[assignment]
    iteration_store = IterationStore(tmp_path, engine.workstation_id)
    first = record(1)
    second = record(2)
    iteration_store.save(first, "")
    iteration_store.save(second, "")
    await engine.iteration_queue.put(second)
    subscription = store.subscribe()

    try:
        await manager._pump_iterations(engine)  # type: ignore[arg-type]
        events = [await asyncio.wait_for(subscription.__anext__(), timeout=1) for _ in range(4)]
    finally:
        await subscription.aclose()

    reloaded = iteration_store.get(2)
    assert reloaded.spc_signal == {"signal": "stop", "reasoning": "no changed lines for 2 iterations", "patterns_detected": ["stall"]}
    assert engine.state.status == WorkstationStatus.PAUSED
    assert any(isinstance(event, WorkstationIterationCompleted) and event.iteration.spc_signal for event in events)
    andon = next(event for event in events if isinstance(event, WorkstationAndon))
    assert _event_payload(andon) == {
        "workstation_id": "ws-abc",
        "event": "andon",
        "payload": {"signal": "stop", "reasoning": "no changed lines for 2 iterations", "patterns": ["stall"]},
    }
