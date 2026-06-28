Status: done
Created: 2026-06-28
Updated: 2026-06-28
Depends-On: .10x/specs/10x-autoresearch-loop.md, autoresearch/catalogs/scores.json, autoresearch/catalogs/scenarios.json, autoresearch/trial-seeds/index.json

# Add Record Richness Grading

## Scope

Add an autoresearch grading criterion for the quality and richness of records
created by 10x, so experiments can judge whether a fresh agent can read the
ticket/spec/research/evidence/decision/knowledge graph and continue without
guessing.

Included:

- Add a stable score catalog entry for record richness / regeneration quality.
- Update the active autoresearch spec's rubric list.
- Map existing record-creation scenarios and seed inventory metadata to the new
  score where appropriate.
- Update validation and documentation so the new score is part of the official
  rubric surface.
- Prefer reusing existing seeds; create no new seed unless the existing catalog
  cannot exercise the criterion.

Excluded:

- Changing canonical `SKILL.md`.
- Adding fixture-backed grading or automatic promotion.
- Adding broad new runner behavior.
- Creating a large new scenario suite if existing record-producing seeds cover
  the behavior.

## Acceptance Criteria

- AC-001: The new score explicitly grades cold-start richness, completeness,
  edge cases, provenance, and ambiguity/blocker preservation across record
  types.
- AC-002: The score has hard floors for under-specified executable records and
  record bloat that still leaves a cold reader guessing.
- AC-003: Existing scenarios that create tickets, specs, research, evidence, or
  durable context reference the new score where it is a relevant target.
- AC-004: `autoresearch/trial-seeds/index.json` is regenerated so seed selection
  can find record-richness experiments.
- AC-005: Validation and tests pass.
- AC-006: Evidence and review record the result before closure.

## Progress And Notes

- 2026-06-28: Opened from the user's request to grade the quality/richness of
  `.10x` records, especially under-specified tickets, specs, and research that
  leave future agents guessing.
- 2026-06-28: Added `S010` / Record Regeneration Quality, mapped it to existing
  record-producing scenarios, regenerated the seed index, and validated the
  autoresearch contracts and test suite.

## Blockers

None.

## References

- `.10x/specs/10x-autoresearch-loop.md`
- `autoresearch/catalogs/scores.json`
- `autoresearch/catalogs/scenarios.json`
- `autoresearch/trial-seeds/index.json`
- `autoresearch/validate.py`
- `.10x/evidence/2026-06-28-record-richness-grading.md`
- `.10x/reviews/2026-06-28-record-richness-grading-review.md`
