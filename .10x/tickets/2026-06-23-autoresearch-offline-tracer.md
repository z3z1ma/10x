Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-contract-validator.md

# Build Offline Scoring Tracer

## Scope

Create the first offline scorer path against saved transcript/file-output
fixtures. This is the tracer bullet before broad scenario coverage or live model
execution.

Likely write scope:

- `autoresearch/offline_score.py`
- `autoresearch/fixtures/offline/`
- `autoresearch/README.md`

Included:

- Define a minimal fixture format for saved transcript and produced-file state.
- Add representative passing and failing fixtures for SCN-001, SCN-004, SCN-008,
  and SCN-009.
- Produce a score artifact compatible with `score-artifact.schema.json`.
- Implement first-pass scoring for at least S001, S002, S004, and S006 on those
  fixtures.
- Mark all scorer outputs as Trust Level 1 unless calibration evidence justifies
  otherwise.

Excluded:

- Live API or harness calls.
- Complete coverage for every score/scenario.
- Promotion claims.

## Acceptance Criteria

- AC-001: Offline scoring command reads saved fixtures and writes score artifacts.
- AC-002: Passing and failing fixtures produce different numeric scores for the
  targeted scores.
- AC-003: The generated score artifacts validate with the contract validator or a
  documented equivalent.
- AC-004: Evidence records command output and at least one inspected score
  rationale.
- AC-005: The ticket records scorer limitations and false-positive risks.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until validator and static contracts exist.

