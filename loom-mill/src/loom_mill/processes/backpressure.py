from __future__ import annotations

from dataclasses import dataclass
from statistics import median


REPEATED_FAILURE_THRESHOLD = 3
LONG_ITERATION_MULTIPLIER = 2
LONG_ITERATION_ABSOLUTE_CAP_SECONDS = 600
CRASH_LOOP_SECONDS = 5


@dataclass(frozen=True)
class IterationRecord:
    exit_code: int | None
    duration_seconds: float
    loom_changed: bool
    output_tail: str = ""


@dataclass(frozen=True)
class BackpressureSignal:
    kind: str
    severity: str
    message: str
    iteration_index: int
    exit_code: int | None = None
    duration_seconds: float | None = None
    output_tail: str = ""


def detect_backpressure(history: list[IterationRecord]) -> list[BackpressureSignal]:
    if not history:
        return []

    latest = history[-1]
    iteration_index = len(history) - 1
    signals: list[BackpressureSignal] = []

    if latest.exit_code not in (None, 0):
        repeated = history[-REPEATED_FAILURE_THRESHOLD:]
        if len(repeated) == REPEATED_FAILURE_THRESHOLD and all(record.exit_code == latest.exit_code for record in repeated):
            signals.append(
                BackpressureSignal(
                    kind="repeated_failure",
                    severity="alert",
                    message=f"Exit code {latest.exit_code} repeated {REPEATED_FAILURE_THRESHOLD} times in a row.",
                    iteration_index=iteration_index,
                    exit_code=latest.exit_code,
                    duration_seconds=latest.duration_seconds,
                    output_tail=latest.output_tail,
                )
            )
        if latest.duration_seconds < CRASH_LOOP_SECONDS:
            signals.append(
                BackpressureSignal(
                    kind="crash_loop",
                    severity="warning",
                    message=f"Process exited in {latest.duration_seconds:.1f}s with code {latest.exit_code}.",
                    iteration_index=iteration_index,
                    exit_code=latest.exit_code,
                    duration_seconds=latest.duration_seconds,
                    output_tail=latest.output_tail,
                )
            )

    previous_durations = [record.duration_seconds for record in history[:-1] if record.duration_seconds > 0]
    duration_limit = LONG_ITERATION_ABSOLUTE_CAP_SECONDS
    if previous_durations:
        duration_limit = max(median(previous_durations) * LONG_ITERATION_MULTIPLIER, CRASH_LOOP_SECONDS)
    if latest.duration_seconds > duration_limit:
        signals.append(
            BackpressureSignal(
                kind="long_iteration",
                severity="warning",
                message=f"Iteration took {latest.duration_seconds:.1f}s, above the {duration_limit:.1f}s backpressure limit.",
                iteration_index=iteration_index,
                exit_code=latest.exit_code,
                duration_seconds=latest.duration_seconds,
                output_tail=latest.output_tail,
            )
        )

    if latest.exit_code == 0 and not latest.loom_changed:
        signals.append(
            BackpressureSignal(
                kind="no_record_change",
                severity="warning",
                message="Iteration exited successfully without changing .loom records.",
                iteration_index=iteration_index,
                exit_code=latest.exit_code,
                duration_seconds=latest.duration_seconds,
                output_tail=latest.output_tail,
            )
        )

    return signals
