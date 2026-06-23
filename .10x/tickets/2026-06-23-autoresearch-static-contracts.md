Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/specs/10x-autoresearch-loop.md, .10x/decisions/autoresearch-initial-implementation-defaults.md

# Create Autoresearch Static Contracts

## Scope

Create the static contract artifacts that future validators, scorers, runners,
and reports consume.

Likely write scope:

- `autoresearch/README.md`
- `autoresearch/catalogs/scores.json`
- `autoresearch/catalogs/scenarios.json`
- `autoresearch/templates/experiment.md`
- `autoresearch/templates/manual-inspection.md`
- `autoresearch/schemas/score-artifact.schema.json`

Included:

- Represent scores S001 through S009 from `.10x/specs/10x-autoresearch-loop.md`.
- Represent scenarios SCN-001 through SCN-015.
- Represent required experiment-record fields from REQ-002.
- Represent scorer trust levels and required scorer metadata from REQ-009.
- Represent budget defaults and no-10x control isolation notes from
  `.10x/decisions/autoresearch-initial-implementation-defaults.md`.
- Use plain Markdown and JSON; no runtime dependencies.

Excluded:

- Validation code.
- Scoring code.
- Harness execution.
- Reports beyond README-level orientation.

## Acceptance Criteria

- AC-001: `scores.json` contains stable IDs S001-S009, names, ranges, summary
  rubrics, hard floors, and related requirement IDs.
- AC-002: `scenarios.json` contains stable IDs SCN-001-SCN-015, target scores,
  expected high-quality behavior, expected failure behavior, allowed/disallowed
  writes, and fixture/reset placeholders.
- AC-003: `experiment.md` includes every field required for registered
  experiments in the spec.
- AC-004: `manual-inspection.md` covers the required inspection checks from the
  spec.
- AC-005: `score-artifact.schema.json` can describe per-sample score output,
  cost, evidence refs, confidence, floor triggers, and limits.
- AC-006: `autoresearch/README.md` clearly states that `.10x/` remains the
  durable record graph and `autoresearch/` is implementation tooling.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

None.

