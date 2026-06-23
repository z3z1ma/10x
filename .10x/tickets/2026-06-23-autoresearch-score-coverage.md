Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-offline-tracer.md

# Expand Offline Score And Scenario Coverage

## Scope

Expand the offline scoring layer from tracer coverage to the full initial score
and scenario battery required by the active spec.

Likely write scope:

- `autoresearch/offline_score.py`
- `autoresearch/fixtures/offline/`
- `autoresearch/catalogs/`
- Supporting documentation under `autoresearch/README.md`

Included:

- Add offline fixtures for SCN-001 through SCN-015 or documented successor
  fixtures.
- Add first-pass scoring coverage for S001 through S009 where offline scoring can
  honestly inspect the behavior.
- Mark scores that require live execution, cost telemetry, or human judgment as
  partial instead of faking certainty.
- Preserve known scorer limitations in machine-readable or documented form.

Excluded:

- Live MICRO runner.
- FULL harness integration.
- Trust Level 2/3 calibration claims unless separately evidenced.

## Acceptance Criteria

- AC-001: Every initial scenario has at least one saved fixture or a documented
  reason it cannot be offline-scored yet.
- AC-002: Every score S001-S009 has a first-pass scoring path or a documented
  unsupported status with reason.
- AC-003: The scorer emits confidence and limits for every per-sample score.
- AC-004: Evidence records full offline scoring output.
- AC-005: Manual inspection notes cover at least one positive and one negative
  scorer match for each core behavioral score S001-S006.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until offline tracer ticket is complete.

