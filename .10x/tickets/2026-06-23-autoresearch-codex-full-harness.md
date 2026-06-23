Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-micro-runner.md

# Integrate Codex FULL Harness

## Scope

Implement the first FULL harness integration using Codex after MICRO scoring is
credible.

Likely write scope:

- `autoresearch/run_full_codex.py` or a similarly narrow Codex harness module.
- `autoresearch/fixtures/full/`
- `autoresearch/README.md`
- `.10x/evidence/.storage/` for validation run artifacts.

Included:

- Run reproducible FULL fixtures under Codex.
- Record model, harness, instruction digest, fixture digest, tools, and artifact
  paths per run.
- Enforce accepted FULL budget: 20 harness runs or 36 wall-clock hours per
  campaign, with 3-hour suggested per-run stop.
- Support no-10x control isolation so project-level 10x instruction files do not
  contaminate the control arm.
- Capture enough transcript/file state for offline scoring.
- Avoid canonical 10x instruction changes.

Excluded:

- Claude Code, OpenCode, and oh-my-pi FULL harnesses.
- Automatic PR creation or release.
- Automatic promotion from one FULL run.

## Acceptance Criteria

- AC-001: Harness can perform a dry-run or safe smoke run that proves fixture
  setup and artifact paths.
- AC-002: No-10x control isolation is demonstrated or the ticket blocks with a
  precise reason.
- AC-003: Harness records required model/harness/instruction/fixture metadata.
- AC-004: Harness output can be consumed by offline scoring.
- AC-005: Evidence records the smoke run and any residual harness limitations.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until MICRO runner and scoring flow are credible.

