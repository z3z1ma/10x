Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-static-contracts.md

# Implement Autoresearch Contract Validator

## Scope

Implement standard-library validation for the static autoresearch contracts.

Likely write scope:

- `autoresearch/validate.py`
- `autoresearch/tests/` or a minimal fixture directory if the repo has no test
  convention yet.
- Small updates to `autoresearch/README.md` documenting validation commands.

Included:

- Validate score catalog shape and ID coverage.
- Validate scenario catalog shape and ID coverage.
- Validate experiment template required fields.
- Validate score artifact schema sanity.
- Validate cross-references between requirements, scores, and scenarios where the
  static files expose those relationships.
- Return non-zero exit status on validation failure.

Excluded:

- Running subject-agent experiments.
- Scoring transcripts.
- JSON Schema dependency installation.
- Full CI integration unless it can be done with existing project conventions.

## Acceptance Criteria

- AC-001: A documented command validates all static contracts and exits zero on
  the checked-in valid state.
- AC-002: At least one intentionally invalid fixture or local test path proves the
  validator catches a missing score/scenario ID.
- AC-003: The validator uses only Python standard library or another existing
  runtime already present in the repo.
- AC-004: Evidence records the validation command and output.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until `.10x/tickets/2026-06-23-autoresearch-static-contracts.md` is
closed or has usable static artifacts.

