from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import TYPE_CHECKING, Awaitable, Callable

if TYPE_CHECKING:
    from loom_mill.workstation.config import FactoryConfig


VALID_SIGNALS = {"continue", "alert", "stop"}


@dataclass(frozen=True)
class SPCSignal:
    signal: str
    reasoning: str
    patterns_detected: list[str]


AdvisoryFn = Callable[[dict], Awaitable[dict | None]]


class SPCEngine:
    def __init__(self, config: FactoryConfig, advisory_fn: AdvisoryFn | None = None) -> None:
        self.config = config
        self.advisory_fn = advisory_fn

    async def analyze(self, workstation_id: str, iterations: list[dict]) -> SPCSignal:
        if not self.config.spc_enabled:
            return SPCSignal("continue", "SPC disabled", [])

        if self.config.spc_model and self.advisory_fn is not None:
            advisory = await self._advisory(workstation_id, iterations)
            if advisory is not None:
                return advisory

        return self._deterministic(iterations)

    async def _advisory(self, workstation_id: str, iterations: list[dict]) -> SPCSignal | None:
        payload = {
            "workstation_id": workstation_id,
            "model": self.config.spc_model,
            "iterations": [self._summary(iteration) for iteration in iterations],
        }
        try:
            response = await asyncio.wait_for(self.advisory_fn(payload), timeout=self.config.spc_timeout_seconds)  # type: ignore[misc]
        except (TimeoutError, OSError, RuntimeError, ValueError):
            return None
        if not isinstance(response, dict):
            return None

        signal = str(response.get("signal", "")).strip().lower()
        if signal not in VALID_SIGNALS:
            return None
        patterns = response.get("patterns", [])
        if not isinstance(patterns, list):
            patterns = []
        return SPCSignal(
            signal=signal,
            reasoning=str(response.get("reasoning") or f"SPC model returned {signal}"),
            patterns_detected=[str(pattern) for pattern in patterns],
        )

    def _deterministic(self, iterations: list[dict]) -> SPCSignal:
        patterns: list[str] = []
        reasons: list[str] = []
        repetition_count = self._threshold("repetition_count", 3)
        churn_count = self._threshold("churn_count", 3)
        escalation_count = self._threshold("escalation_count", 3)
        stall_count = self._threshold("stall_count", 2)

        repeated_tests = self._repeated_failing_tests(iterations, repetition_count)
        repeated_exit_code = self._repeated_exit_code(iterations, repetition_count)
        if repeated_tests:
            patterns.append("repetition")
            reasons.append(f"same failing tests repeated: {', '.join(repeated_tests)}")
        elif repeated_exit_code is not None:
            patterns.append("repetition")
            reasons.append(f"exit code {repeated_exit_code} repeated for {repetition_count} iterations")

        churn_files = self._churn_files(iterations, churn_count)
        if churn_files:
            patterns.append("file_churn")
            reasons.append(f"same files changed for {churn_count} iterations: {', '.join(churn_files)}")

        if self._duration_escalating(iterations, escalation_count):
            patterns.append("duration_escalation")
            reasons.append(f"duration increased monotonically for {escalation_count} iterations")

        if self._stalled(iterations, stall_count):
            patterns.append("stall")
            reasons.append(f"no changed lines for {stall_count} iterations")

        if "repetition" in patterns or "stall" in patterns:
            return SPCSignal("stop", "; ".join(reasons), patterns)
        if patterns:
            return SPCSignal("alert", "; ".join(reasons), patterns)
        return SPCSignal("continue", "no SPC patterns detected", [])

    def _threshold(self, name: str, default: int) -> int:
        value = self.config.spc_thresholds.get(name, default)
        try:
            return max(1, int(value))
        except (TypeError, ValueError):
            return default

    def _summary(self, iteration: dict) -> dict:
        return {
            "iteration": iteration.get("iteration"),
            "duration_seconds": iteration.get("duration_seconds"),
            "files_changed": iteration.get("files_changed", []),
            "lines_added": iteration.get("lines_added", 0),
            "lines_removed": iteration.get("lines_removed", 0),
            "exit_code": iteration.get("exit_code"),
        }

    def _window(self, iterations: list[dict], count: int) -> list[dict]:
        return iterations[-count:] if len(iterations) >= count else []

    def _repeated_failing_tests(self, iterations: list[dict], count: int) -> list[str]:
        window = self._window(iterations, count)
        if not window:
            return []
        failing_sets = []
        for iteration in window:
            tests = iteration.get("failing_tests") or iteration.get("test_results", {}).get("failing_tests", [])
            failing_sets.append({str(test) for test in tests})
        return sorted(set.intersection(*failing_sets)) if all(failing_sets) else []

    def _repeated_exit_code(self, iterations: list[dict], count: int) -> int | None:
        window = self._window(iterations, count)
        if not window:
            return None
        exit_codes = [iteration.get("exit_code") for iteration in window]
        latest = exit_codes[-1]
        if latest not in (None, 0) and all(exit_code == latest for exit_code in exit_codes):
            return int(latest)
        return None

    def _churn_files(self, iterations: list[dict], count: int) -> list[str]:
        window = self._window(iterations, count)
        if not window:
            return []
        file_sets = [{str(path) for path in iteration.get("files_changed", [])} for iteration in window]
        return sorted(set.intersection(*file_sets)) if all(file_sets) else []

    def _duration_escalating(self, iterations: list[dict], count: int) -> bool:
        window = self._window(iterations, count)
        if not window:
            return False
        durations = [float(iteration.get("duration_seconds") or 0) for iteration in window]
        return all(previous < current for previous, current in zip(durations, durations[1:]))

    def _stalled(self, iterations: list[dict], count: int) -> bool:
        window = self._window(iterations, count)
        if not window:
            return False
        return all((int(iteration.get("lines_added") or 0) + int(iteration.get("lines_removed") or 0)) == 0 for iteration in window)
