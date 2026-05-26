# Mill Process Control (SPC + Jidoka)

ID: spec:mill-process-control
Type: Spec
Status: active
Created: 2026-05-25
Updated: 2026-05-25

## Summary

This spec defines the inter-iteration process control system: an LLM-backed statistical process control (SPC) pass that runs between iterations on each workstation, detects patterns indicating drift or defects, and triggers jidoka (automatic stop) when thresholds are crossed.

## Product Slice

This spec owns the "quality built in at every step" behavior: what happens between iterations to detect problems before they compound. It does NOT own workstation lifecycle, scheduling, merge, or the andon board UI (those display SPC signals but don't generate them).

## Spec Set Coverage

Completes the "how does the factory stop itself" question. Without this, the operator must watch manually for drift. With it, the factory has autonomation: machines that stop themselves when they detect defects.

## Problem

LLMs are good at single-turn judgment but fail cumulatively: drift, repetition, scope creep, placeholder cheating, looping on the same file. These failure modes are invisible per-iteration but obvious when viewed across iterations. A human watching would say "it's been trying the same thing for 3 iterations" but a fresh worker context doesn't carry that awareness. SPC fills this gap.

## Desired Behavior

After each iteration boundary on each workstation, the SPC process:

1. Collects iteration data: diff, test results, duration, files touched, exit code, comparison with previous iterations.
2. Sends a structured summary to the configured SPC model (configurable per-factory, defaults to fast/cheap).
3. The model evaluates: is the workstation making meaningful progress, or is it showing a failure pattern?
4. Returns a signal: `continue`, `alert` (surface to operator but don't stop), or `stop` (jidoka - halt the workstation).
5. The signal is recorded in iteration history and surfaced in the control room.

Jidoka means: when `stop` is signaled, the workstation halts automatically. The andon board shows why. The operator addresses the issue (reshape, add constraint, add knowledge) and resumes.

## Not Doing

- Semantic interpretation of ticket acceptance or closure
- Making product decisions about what "good" means (that's the spec/ticket's job)
- Running the workstation or managing its subprocess
- Evidence gathering (SPC signals are observations, not evidence records unless promoted)
- Audit (SPC is mechanical detection, not adversarial review)

## Requirements

- REQ-001: The SPC process MUST run after every iteration boundary on every active workstation.

- REQ-002: The SPC model MUST be configurable per-factory. The operator selects which model handles SPC analysis. Default should be a fast/cheap model suitable for pattern detection over structured data.

- REQ-003: The SPC process MUST receive structured iteration data, not raw logs. Input includes: current iteration number, diff stat (files changed, lines added/removed), files touched (list), test results if observable (pass/fail counts), iteration duration, exit code, and a rolling window of previous iterations' same data.

- REQ-004: The SPC model MUST return one of three signals: `continue` (no issues detected), `alert` (potential issue, surface to operator, don't stop), `stop` (jidoka - halt workstation immediately).

- REQ-005: When signal is `stop`, the workstation MUST halt automatically (jidoka). No further iterations run until operator intervention.

- REQ-006: Every SPC signal MUST include a brief reasoning string explaining what pattern was detected or why continuation is safe.

- REQ-007: SPC signals MUST be recorded in the iteration history (`.mill/`) and surfaced to the frontend via the workstation's event stream.

- REQ-008: The SPC process MUST detect at minimum these patterns:
  - Same test(s) failing across 3+ iterations
  - Same file(s) being modified in 3+ consecutive iterations without tests passing
  - Iteration duration increasing monotonically (3+ iterations)
  - No meaningful diff (empty or trivial changes)
  - Scope drift: files outside the ticket's declared write scope being modified

- REQ-009: Pattern detection thresholds MUST be configurable. The defaults (3 iterations for repetition patterns) should be overridable per-factory.

- REQ-010: If the SPC model is unavailable or times out, the system MUST fall back to deterministic rule-based checks for the patterns in REQ-008. The fallback does not produce `alert` signals, only `continue` or `stop`.

- REQ-011: The SPC process MUST NOT add meaningful latency to the iteration cycle. Target: < 5 seconds for the SPC pass. If the model is slow, proceed with fallback rules and log the timeout.

## Scenarios

### SCN-001: Normal Progress

Exercises: REQ-001, REQ-003, REQ-004

GIVEN workstation W completes iteration 4
AND iterations 1-4 each touched different files, tests went from 5/10 to 8/10 to 9/10 to 10/10
WHEN SPC runs
THEN signal is `continue` with reasoning "steady test improvement, no repetition patterns"

### SCN-002: Repetition Detection (Jidoka Stop)

Exercises: REQ-005, REQ-008

GIVEN workstation W is on iteration 5
AND iterations 3, 4, and 5 all show `test_parser_edge` failing
AND the same 2 files were modified in all 3 iterations
WHEN SPC runs after iteration 5
THEN signal is `stop` with reasoning "same test failing 3 consecutive iterations, same files modified"
AND workstation W halts automatically
AND andon board shows the stop with the reasoning

### SCN-003: Alert Without Stop

Exercises: REQ-004, REQ-006

GIVEN workstation W completes iteration 3
AND iteration duration increased: 5min, 8min, 12min
BUT tests are still progressing (new tests passing each iteration)
WHEN SPC runs
THEN signal is `alert` with reasoning "iteration duration increasing monotonically, but test progress continues"
AND workstation continues running
AND operator sees the alert in the control room

### SCN-004: Model Timeout Fallback

Exercises: REQ-010, REQ-011

GIVEN SPC model is configured but responding slowly (> 5 second timeout)
WHEN iteration boundary triggers SPC
THEN system falls back to deterministic rule checks
AND iteration proceeds without waiting for model response
AND timeout is logged

### SCN-005: Scope Drift Detection

Exercises: REQ-008

GIVEN ticket declares write scope as `src/parser/` and `tests/parser/`
AND iteration 3 modifies `src/api/routes.py` (outside declared scope)
WHEN SPC runs
THEN signal is `alert` or `stop` (based on severity) with reasoning "files outside declared write scope modified"

## Evidence Plan

- REQ-001: Integration test showing SPC fires after every iteration boundary across multiple workstations.
- REQ-004-005 / SCN-002: Test with fixture iteration history showing repetition pattern triggers `stop` and workstation halts.
- REQ-008: Unit tests for each pattern type with fixture data showing correct detection.
- REQ-010 / SCN-004: Test that timeout triggers fallback to rule-based detection.
- REQ-011: Performance test showing SPC completes within 5 seconds with a mocked model.

## Interface Contract

### SPC Input

```python
@dataclass
class SPCInput:
    workstation_id: str
    ticket_id: str
    ticket_write_scope: list[str]        # declared write paths
    current_iteration: int
    iterations_window: list[IterationSnapshot]  # last N iterations
    
@dataclass
class IterationSnapshot:
    iteration: int
    duration_seconds: float
    files_changed: list[str]
    lines_added: int
    lines_removed: int
    test_results: TestResults | None     # pass_count, fail_count, failing_tests
    exit_code: int
    commit_sha: str
```

### SPC Output

```python
@dataclass
class SPCSignal:
    signal: Literal["continue", "alert", "stop"]
    reasoning: str
    patterns_detected: list[str]         # e.g., ["repetition", "scope_drift"]
    confidence: float                     # 0.0-1.0
```

### SPC Model Prompt Shape

The SPC model receives structured data (not prose). The prompt asks: "Given this iteration history for a workstation executing ticket X, is the workstation making meaningful progress or showing failure patterns? Return: continue, alert, or stop with reasoning."

## Constraints

- SPC is an observer. It MUST NOT modify `.loom/` records, workstation files, or ticket state.
- SPC signals are ephemeral observations stored in `.mill/`, not evidence records unless explicitly promoted.
- The SPC model does not see full logs or full diffs. It sees structured summaries to keep token cost low.
- Scope drift detection requires the ticket to declare write scope. If not declared, scope drift detection is skipped.
- Jidoka stops are reversible. The operator can always resume after addressing the issue.

## Related Records

- `spec:mill-factory-floor` - displays SPC signals and andon board, handles jidoka stop
- `spec:mill-scheduling-agent` - may re-queue tickets that were stopped by jidoka
- `constitution:main` - jidoka and autonomation as factory principles
- `research:20260524-loom-mill-software-factory` - SPC and pattern detection research
