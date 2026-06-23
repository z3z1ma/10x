Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-score-coverage.md

# Implement MICRO Runner

## Scope

Implement the first live MICRO experiment runner for controlled, repeated
subject-agent samples.

Likely write scope:

- `autoresearch/run_micro.py`
- `autoresearch/templates/`
- `autoresearch/README.md`
- `.10x/research/.storage/` or `.10x/evidence/.storage/` only for run artifacts
  produced during validation.

Included:

- Read a registered experiment record or equivalent local experiment definition.
- Run no-10x, current-10x, and candidate arms when configured.
- Enforce the accepted MICRO budget: 300 subject-agent samples or 10 wall-clock
  hours per campaign.
- Cache per scenario, variant, repetition, model, and instruction digest.
- Write raw outputs and score artifacts.
- Preserve no-10x control isolation requirements in runner design.
- Support dry-run mode that resolves planned calls without invoking a live model.

Excluded:

- Codex FULL harness integration.
- Claude/OpenCode/oh-my-pi integration.
- Automatic promotion decisions.
- Trust Level 3 scorer approval.

## Acceptance Criteria

- AC-001: Dry-run mode shows planned arms, scenarios, repetitions, cache keys,
  and budget limits without live calls.
- AC-002: Runner refuses a non-exploratory MICRO run without a registered
  experiment definition.
- AC-003: Runner writes raw outputs and score artifacts to documented locations.
- AC-004: Runner enforces sample and wall-clock limits.
- AC-005: Evidence records a small safe MICRO run or dry-run plus offline-scored
  sample artifacts.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until offline score and scenario coverage is credible.

