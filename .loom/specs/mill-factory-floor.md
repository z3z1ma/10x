# Mill Factory Floor

ID: spec:mill-factory-floor
Type: Spec
Status: active
Created: 2026-05-25
Updated: 2026-05-25

Supersedes: spec:loom-mill-factory-floor-mvp

## Summary

This spec defines the production Factory Floor: the execution control room of Loom Mill. It covers what the operator sees, controls, and reads during autonomous execution across N concurrent workstations.

Downstream tickets should cite this spec when building multi-workstation management, pipeline visualization, log streaming, diff viewing, playback, takt indicators, WIP enforcement, quality metrics, changelog, andon board, and operator controls.

## Product Slice

This spec owns the Factory Floor as a product surface: the backend engine that manages N workstations and the frontend control room that renders their state.

This spec does NOT own:
- How work is selected for execution (see `spec:mill-scheduling-agent`)
- How inter-iteration intelligence works (see `spec:mill-process-control`)
- How finished work merges (see `spec:mill-shipping-dock`)
- The Design Office shaping experience

Those are connected systems with their own lifecycle and interface contracts.

## Spec Set Coverage

Together with `spec:mill-scheduling-agent`, `spec:mill-process-control`, and `spec:mill-shipping-dock`, this forms the complete production Factory Floor behavior contract. This spec is the primary one; the satellites define subsystems that plug into the workstation lifecycle.

## Problem

The MVP proved the architecture: single workstation, basic pipeline, pause/resume, backpressure signals. But production autonomous execution needs N concurrent workstations, full observability (logs, diffs, iteration history), playback for post-hoc review, takt tracking, WIP enforcement, quality metrics, and aggregate output summaries. Without these, the operator cannot trust or steer multi-ticket parallel execution.

## Desired Behavior

The Factory Floor runs N workstations concurrently. Each workstation is a worktree + harness subprocess + log stream + iteration history. The operator sees all workstations simultaneously in a control room layout: pipeline overview showing all tickets flowing through stages, active workstation panels with live state, a log panel per workstation, diff views per iteration, takt indicators, an andon board for stops/alerts, quality metrics over time, and a changelog of what shipped.

The operator can: start workstations (manually or via scheduling agent), pause/stop any workstation, steer (edit record + resume), view full iteration history and playback, configure WIP limits, and read aggregate metrics.

The backend multiplexes all workstation state over WebSocket. The frontend renders N panels with live updates. Iteration history persists in `.mill/` for playback and metrics.

## Not Doing

- Semantic interpretation of record prose (Mill is mechanical, not reasoning)
- Scheduling logic (owned by `spec:mill-scheduling-agent`)
- Inter-iteration LLM analysis (owned by `spec:mill-process-control`)
- Merge/shipping workflow (owned by `spec:mill-shipping-dock`)
- Design Office shaping UI
- Remote/hosted operation
- TUI (separate future product slice)

## Requirements

- REQ-001: Mill MUST support N concurrent workstations, each with its own worktree, harness subprocess, log stream, and iteration history. N is limited only by system resources and configured WIP limits.

- REQ-002: Each workstation MUST be identified by a stable ID and associated with exactly one ticket during its lifetime. The association is immutable once started.

- REQ-003: Mill MUST stream full stdout and stderr from each harness subprocess to the frontend in real-time, multiplexed by workstation ID.

- REQ-004: Mill MUST track iteration boundaries per workstation. An iteration boundary is detected by: subprocess exit, git commit on the worktree branch, or configurable signal. Each iteration records: start time, end time, git diff, test/command results when observable, and subprocess exit code.

- REQ-005: Mill MUST persist iteration history per workstation in `.mill/` (gitignored). History includes: iteration diffs, durations, exit codes, log excerpts, and SPC signals received.

- REQ-006: Mill MUST provide per-iteration and aggregate diff views in the frontend. Per-iteration shows what changed in one iteration. Aggregate shows total change for the ticket so far.

- REQ-007: Mill MUST provide playback: the operator can step through completed iterations of any workstation (active or finished), viewing the diff, duration, logs, and any SPC signals at each step.

- REQ-008: Mill MUST track takt time per iteration and surface it as a visible indicator. When an iteration exceeds a configurable duration threshold, the indicator should escalate visually (not stop automatically; jidoka handles stopping via `spec:mill-process-control`).

- REQ-009: Mill MUST enforce configurable WIP limits. When the number of active workstations equals the WIP limit, no new workstation can start until one finishes or is stopped. The scheduling agent respects this; manual start is also blocked with a clear message.

- REQ-010: The frontend MUST render a pipeline overview showing all tickets flowing through lifecycle stages (shaped/queued, executing, evidence, audit, shipping, closed). Tickets move through stages based on their `.loom/` record status.

- REQ-011: The frontend MUST render N workstation panels simultaneously. Each panel shows: ticket ID, current iteration number, last commit time, takt indicator, status (running/paused/stopped/finished), and controls (pause/stop/view-logs/view-diff).

- REQ-012: The frontend MUST include an andon board that aggregates all active alerts, stops, and escalations across workstations. Each entry links to the source workstation and relevant record.

- REQ-013: Mill MUST provide quality metrics per session: iterations per ticket, average iteration duration, number of SPC stops, rework count (tickets that resumed after steering), and completion rate.

- REQ-014: Mill MUST provide a changelog view: an aggregate summary of tickets that reached shipping/closed status during the current session, with their diffs and evidence state.

- REQ-015: The backend MUST multiplex all workstation events over a single WebSocket connection using a message format that includes workstation ID, event type, and payload.

- REQ-016: Operator controls MUST include: start workstation (for a given ticket), pause, stop, resume (from updated graph), open record (for steering), and configure WIP/takt thresholds.

- REQ-017: Mill MUST treat `.loom/` as the only durable truth. All Mill runtime state (iteration history, logs, metrics, session state) lives in gitignored `.mill/`.

- REQ-018: The harness command, model, and flags MUST remain operator-configurable. The same subprocess lifecycle applies regardless of harness.

## Scenarios

### SCN-001: N Concurrent Workstations

Exercises: REQ-001, REQ-002, REQ-011, REQ-015

GIVEN WIP limit is set to 3
WHEN the operator starts 3 workstations on tickets A, B, C
THEN 3 worktrees exist, 3 subprocesses are running, 3 log streams are active
AND the frontend shows 3 workstation panels with live state
AND all events arrive multiplexed over one WebSocket connection

### SCN-002: WIP Limit Enforcement

Exercises: REQ-009

GIVEN WIP limit is 2 and 2 workstations are active
WHEN the operator or scheduling agent attempts to start a 3rd workstation
THEN the start is blocked with a clear message indicating WIP limit reached
AND the ticket remains in queued state

### SCN-003: Live Log Streaming

Exercises: REQ-003, REQ-015

GIVEN workstation W is running ticket A
WHEN the harness subprocess writes to stdout or stderr
THEN the output appears in workstation W's log panel in the frontend within 1 second
AND logs from other workstations do not intermix

### SCN-004: Iteration Tracking and Diff View

Exercises: REQ-004, REQ-005, REQ-006

GIVEN workstation W completes iteration 3 (commit detected)
THEN Mill records: iteration 3 start/end time, git diff, exit code
AND the frontend shows the per-iteration diff for iteration 3
AND the aggregate diff shows all changes across iterations 1-3

### SCN-005: Playback

Exercises: REQ-007, REQ-005

GIVEN workstation W has completed 5 iterations
WHEN the operator opens playback for workstation W
THEN they can step through iterations 1-5
AND at each step they see: the diff, duration, log excerpt, and any SPC signals

### SCN-006: Takt Time Escalation

Exercises: REQ-008

GIVEN takt threshold is configured at 15 minutes
WHEN workstation W's current iteration has been running for 20 minutes
THEN the takt indicator for W escalates visually (color change, warning icon)
AND no automatic stop occurs (that's jidoka's job via SPC)

### SCN-007: Pipeline Overview

Exercises: REQ-010

GIVEN 8 tickets exist: 2 queued, 3 executing, 1 in evidence, 1 in audit, 1 closed
WHEN the operator views the pipeline
THEN all 8 tickets appear in their correct lifecycle stage
AND stage assignment reflects the ticket's status in `.loom/`

### SCN-008: Quality Metrics and Changelog

Exercises: REQ-013, REQ-014

GIVEN a session where 3 tickets completed and 1 required steering/rework
WHEN the operator views metrics
THEN they see: 3 completed, 1 reworked, average iteration duration, total iterations
WHEN the operator views changelog
THEN they see the 3 completed tickets with summary diffs and evidence state

## Evidence Plan

- REQ-001 / SCN-001: Integration test with 3 concurrent workstations using mock harness commands. All 3 run, produce output, and are tracked independently.
- REQ-003 / SCN-003: Test that subprocess stdout/stderr arrives at WebSocket client within latency bound, correctly tagged by workstation ID.
- REQ-004-005 / SCN-004: Test that commit detection creates iteration records in `.mill/` with correct metadata.
- REQ-006 / SCN-004: Frontend test or screenshot showing per-iteration and aggregate diff views.
- REQ-007 / SCN-005: Integration test that iteration history supports random-access playback after completion.
- REQ-008 / SCN-006: Test that takt threshold crossing triggers UI escalation event without stopping the workstation.
- REQ-009 / SCN-002: Test that WIP limit blocks new workstation creation and returns appropriate error.
- REQ-010 / SCN-007: Frontend test showing correct pipeline stage assignment from fixture `.loom/` records.
- REQ-013-014 / SCN-008: Test that session metrics accumulate correctly and changelog renders completed tickets.
- REQ-015: WebSocket protocol test showing multiplexed messages with workstation ID discrimination.

## Quality Bar

The control room should let an operator assess the state of N concurrent workstations within 5 seconds of looking at the screen. They should know: what's running, what's stuck, what shipped, and where to intervene. The UI should feel like a manufacturing control room: dense, calm, professional, information-rich without noise.

Playback should feel like scrubbing through a video timeline: instant, oriented, and revealing of the build sequence.

## Interface Contract

### WebSocket Message Format

```
{
  "workstation_id": "ws-001",
  "event": "log" | "iteration" | "state" | "takt" | "andon" | "metrics",
  "payload": { ... }
}
```

### Backend API

- `POST /workstations` - start a new workstation for a ticket
- `DELETE /workstations/{id}` - stop a workstation
- `POST /workstations/{id}/pause` - pause
- `POST /workstations/{id}/resume` - resume from updated graph
- `GET /workstations/{id}/iterations` - iteration history
- `GET /workstations/{id}/iterations/{n}/diff` - specific iteration diff
- `GET /workstations/{id}/diff` - aggregate diff
- `GET /workstations/{id}/logs` - historical logs
- `GET /metrics` - session quality metrics
- `GET /changelog` - completed tickets this session
- `GET /config` - current WIP limit, takt threshold, harness config
- `PUT /config` - update config

### Iteration Record (`.mill/workstations/{id}/iterations/{n}.json`)

```json
{
  "iteration": 3,
  "started_at": "2026-05-25T14:00:00Z",
  "ended_at": "2026-05-25T14:08:22Z",
  "duration_seconds": 502,
  "exit_code": 0,
  "commit_sha": "abc1234",
  "diff_stat": "+45 -12 across 3 files",
  "spc_signals": [],
  "log_excerpt": "..."
}
```

## Constraints

- All iteration persistence in `.mill/` (gitignored). Never in `.loom/`.
- WebSocket must handle N workstations without degrading frontend responsiveness.
- Log streaming must not buffer entire subprocess output in memory; stream and truncate older entries.
- Worktree creation/cleanup must be safe around concurrent git operations.
- Frontend must remain a static Svelte build compatible with Tauri wrapping.

## Related Records

- `spec:loom-mill-factory-floor-mvp` - superseded predecessor
- `spec:mill-scheduling-agent` - decides what enters workstations
- `spec:mill-process-control` - decides when workstations stop (jidoka)
- `spec:mill-shipping-dock` - decides how finished work merges
- `constitution:main` - Loom/Mill identity and factory principles
- `roadmap:loom-mill` - strategic sequence
- `research:20260524-loom-mill-software-factory` - factory architecture research
