Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-retrospective-extraction-type-gate-scn012-live-micro.md, .10x/evidence/2026-06-23-scn012-skill-record-scoring-validation.md, .10x/reviews/2026-06-23-scn012-skill-record-scoring.md

# Improve SCN-012 Skill Record Scoring

## Scope

Update the SCN-012 retrospective scoring path so `.10x/skills/` records with
valid skill frontmatter count as first-class retrospective procedure capture.

Included:

- Adjust Trust Level 1 S002 retrospective scoring to recognize skill records.
- Add or update tests covering a retrospective that correctly routes a procedure
  to `.10x/skills/<slug>/SKILL.md`.

Excluded:

- Changing candidate promotion rules.
- Replacing manual inspection.

## Acceptance Criteria

- AC-001: A valid skill record can satisfy the "repeatable operational
  procedure captured" part of SCN-012.
- AC-002: Skill records are not required to have common record headers because
  `SKILL.md` specifies YAML frontmatter for skills.
- AC-003: Tests prevent the regression seen in
  `EXP-20260623-850-retrospective-extraction-type-gate-scn012-live-micro`, where
  the candidate got a lower S002 score despite creating the correct skill.

## Progress And Notes

- 2026-06-23: Opened from EXP-850 manual inspection. Candidate's correct skill
  record was manually promotable but scored `S002=70` because the scorer did not
  model skill records in SCN-012.
- 2026-06-23: Updated SCN-012 S002 retrospective scoring to treat valid
  `.10x/skills/<slug>/SKILL.md` records as repeatable procedure capture.
- 2026-06-23: Added tests for valid skill frontmatter and invalid path-only
  skill records.
- 2026-06-23: Validation passed. Direct rescore of the EXP-850 candidate raw
  artifact now reports `S002=85` with no floor trigger.

## Blockers

- None.
