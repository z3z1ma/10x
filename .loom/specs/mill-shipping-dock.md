# Mill Shipping Dock

ID: spec:mill-shipping-dock
Type: Spec
Status: active
Created: 2026-05-25
Updated: 2026-05-25

## Summary

This spec defines how finished work leaves the factory: merging completed ticket worktrees into a target branch. It supports both auto-merge (after audit passes) and operator-approved merge, with configurable target branch per-factory or per-ticket.

## Product Slice

This spec owns the merge workflow: when and how a workstation's worktree gets merged, what happens on conflict, and how the worktree is cleaned up. It does NOT own audit (that's upstream), scheduling (that's triggered by completion), or the pipeline visualization (that's the control room).

## Spec Set Coverage

Completes the "finished goods" story. Without this, the operator must manually merge worktrees. With it, the factory has a shipping dock: completed work flows out automatically (or with one click) to the configured branch.

## Problem

With N workstations running in parallel on separate worktrees, each producing commits against their own branch, the operator needs a clear merge path. Questions: which branch to merge into (not always main), whether to auto-merge or wait for approval, what to do about conflicts between parallel tickets, and when to clean up the worktree.

## Desired Behavior

When a ticket passes through its quality gate (audit pass, evidence gathered, or operator marks ready), it enters the shipping dock. The shipping dock either:

- **Auto-merge mode**: immediately attempts merge to the configured target branch. On success, cleans up the worktree and marks the workstation as finished. On conflict, triggers jidoka (stops, surfaces conflict, waits for operator).
- **Operator-approved mode**: queues the ticket at the shipping dock. The operator reviews and clicks "ship" (merge). Same conflict handling.

The target branch is configurable: per-factory default (e.g., `dev`) with per-ticket override (e.g., ticket says "merge to `feature/auth-rewrite`"). This supports the real workflow where changes accumulate on feature branches before reaching main.

## Not Doing

- Deciding whether audit passed (that's audit's job; shipping dock reacts to the result)
- Running CI/CD pipelines (shipping dock merges; downstream CI is external)
- Deploying or releasing (shipping is the code merge, not the release)
- Squash vs merge commit strategy (use merge commit for traceability; can be configured later)
- PR creation against remote (local merge only; push is separate operator action)

## Requirements

- REQ-001: Mill MUST support two shipping modes: `auto-merge` and `operator-approved`. Mode is configurable per-factory.

- REQ-002: The target branch MUST be configurable. Per-factory default (e.g., `main`, `dev`, `develop`). Per-ticket override via a `Target Branch:` field in the ticket record or operator setting at start time.

- REQ-003: In auto-merge mode, merge MUST be attempted automatically when the ticket reaches a configured "ready to ship" status (default: after audit passes or operator marks ready).

- REQ-004: In operator-approved mode, completed tickets MUST queue at the shipping dock. The operator sees them in the pipeline and explicitly triggers merge.

- REQ-005: Merge MUST use `git merge --no-ff` from the workstation branch into the target branch, preserving the commit history for traceability.

- REQ-006: On merge conflict, the system MUST halt (jidoka). The conflict is surfaced in the andon board with: which files conflict, which workstation, and the target branch. The workstation enters a `conflict` state.

- REQ-007: After successful merge, the worktree MUST be cleaned up (deleted) and the workstation marked as `finished`. The local branch may be deleted or preserved based on configuration.

- REQ-008: After successful merge, the scheduling agent MUST be notified that capacity is freed (triggering potential next pull).

- REQ-009: The shipping dock MUST handle sequential merges safely. If tickets A and B both target `dev`, and A merges first, B's merge attempt must include A's changes (rebase or merge from target before merging B).

- REQ-010: The operator MUST be able to: skip shipping (close a ticket without merging), change the target branch before merge, force merge (override conflict by accepting their resolution), or abort (discard the workstation's changes).

- REQ-011: Merge events (success, conflict, skip, abort) MUST be logged and surfaced in the changelog and quality metrics.

## Scenarios

### SCN-001: Auto-Merge Success

Exercises: REQ-001, REQ-002, REQ-003, REQ-005, REQ-007, REQ-008

GIVEN auto-merge mode, target branch is `dev`
AND workstation W finishes ticket A, audit passes
WHEN ticket A reaches "ready to ship" status
THEN Mill merges workstation branch into `dev` with `--no-ff`
AND worktree is cleaned up
AND workstation W is marked `finished`
AND scheduling agent is notified of freed capacity

### SCN-002: Merge Conflict (Jidoka)

Exercises: REQ-006, REQ-009

GIVEN tickets A and B both target `dev`
AND ticket A merged successfully, changing `src/parser.py`
WHEN ticket B attempts to merge and also modified `src/parser.py`
THEN merge conflict is detected
AND workstation B enters `conflict` state
AND andon board shows: conflicting files, workstation B, target `dev`
AND no further action until operator resolves

### SCN-003: Operator-Approved Merge

Exercises: REQ-004, REQ-010

GIVEN operator-approved mode
AND ticket C finishes execution and audit
WHEN ticket C reaches shipping dock
THEN it queues visibly in the pipeline's "shipping" stage
AND no merge occurs until operator clicks "ship"
WHEN operator clicks "ship"
THEN merge proceeds as in SCN-001

### SCN-004: Per-Ticket Target Branch

Exercises: REQ-002

GIVEN factory default target is `dev`
AND ticket D has `Target Branch: feature/auth-rewrite` in its record
WHEN ticket D reaches shipping dock
THEN merge targets `feature/auth-rewrite`, not `dev`

### SCN-005: Skip Shipping

Exercises: REQ-010, REQ-011

GIVEN ticket E is at shipping dock
WHEN operator selects "skip" (close without merge)
THEN ticket is marked closed, worktree is cleaned up
AND changelog records it was closed without merge
AND no merge occurs

## Evidence Plan

- REQ-001-003 / SCN-001: Integration test with mock git repo showing auto-merge creates merge commit on target branch.
- REQ-006 / SCN-002: Test with conflicting changes showing merge failure triggers conflict state and andon.
- REQ-009: Test showing sequential merges where second merge includes first's changes.
- REQ-005: Test that merge commits use `--no-ff` and preserve history.
- REQ-007: Test that worktree cleanup occurs after successful merge.
- REQ-010 / SCN-005: Test that skip closes ticket without merge attempt.

## Interface Contract

### Shipping Dock API

- `POST /shipping/{workstation_id}/ship` - trigger merge (used by auto-merge or operator click)
- `POST /shipping/{workstation_id}/skip` - close without merge
- `POST /shipping/{workstation_id}/abort` - discard workstation changes
- `POST /shipping/{workstation_id}/resolve` - operator resolved conflict, retry merge
- `GET /shipping/queue` - list tickets waiting for operator approval

### Shipping Event

```python
@dataclass
class ShippingEvent:
    workstation_id: str
    ticket_id: str
    action: Literal["merged", "conflict", "skipped", "aborted"]
    target_branch: str
    merge_sha: str | None
    conflict_files: list[str] | None
    timestamp: str
```

### Configuration

```python
@dataclass
class ShippingConfig:
    mode: Literal["auto-merge", "operator-approved"]
    default_target_branch: str              # e.g., "main", "dev"
    cleanup_branch_after_merge: bool        # delete workstation branch
    ready_to_ship_statuses: list[str]       # ticket statuses that trigger shipping
```

## Constraints

- Shipping dock operates on the LOCAL repository only. Push to remote is a separate operator action.
- Merge uses `--no-ff` for traceability. Squash may be added later as a config option.
- Conflict resolution is manual. Mill does not attempt automatic conflict resolution.
- Worktree cleanup must verify no uncommitted changes before deletion.
- The shipping dock MUST NOT modify `.loom/` records. Ticket status updates happen through the model/operator path.

## Related Records

- `spec:mill-factory-floor` - pipeline visualization shows shipping dock state
- `spec:mill-scheduling-agent` - notified when merge completes (capacity freed)
- `spec:mill-process-control` - upstream; SPC/audit must pass before shipping
- `constitution:main` - shipping dock = finished goods leave the factory
