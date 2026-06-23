Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/reviews/2026-06-23-records-first-retrieval-promotion.md

# Promote Records-First Retrieval

## Scope

Promote the narrow records-first retrieval behavior into canonical `SKILL.md`.

Included:

- Add concise instruction under Outer Loop investigation.
- Mark candidate record as promoted.
- Preserve the promotion review and experiment evidence links.

Excluded:

- Scorer changes.
- Harness changes.
- Broad rewrites of the Outer Loop section.

## Acceptance Criteria

- `SKILL.md` tells the agent to answer from existing `.10x` records before
  asking the user to restate known context.
- The instruction requires citing paths used, separating settled facts from
  gaps, and avoiding duplicate records.
- Promotion review exists and references the supporting experiments.
- Validation passes.

## Progress And Notes

- 2026-06-23: Promoted compact rule after EXP-826, EXP-827, EXP-828, and
  EXP-829 aggregate review.

## Blockers

None.
