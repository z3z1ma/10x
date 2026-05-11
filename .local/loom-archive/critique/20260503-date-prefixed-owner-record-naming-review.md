---
id: critique:date-prefixed-owner-record-naming-review
kind: critique
status: final
created_at: 2026-05-03T20:16:21Z
updated_at: 2026-05-03T20:16:21Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:namefmt54 date-prefixed owner-record naming diff"
links:
  tickets:
    - ticket:namefmt54
  evidence:
    - evidence:date-prefixed-owner-record-naming-validation
external_refs: {}
---

# Summary

Reviewed the date-prefixed naming convention change for owner-record boundaries,
ID stability, validation behavior, and migration risk.

# Review Target

Target: `ticket:namefmt54`, the naming convention diff across `skills/`, and the
rename of `.loom/critique/20260503-route-token-simplification-review.md`.

# Verdict

`pass_with_findings`

The initial review found missing evidence naming guidance, over-broad validation
wording, and overly strong age-pruning wording. Those findings were repaired, and
the follow-up review reported no remaining findings.

# Findings

## FIND-001: Evidence creation surface lacked the new naming rule

Severity: medium
Confidence: high
State: open

Observation:

The initial review found that `skills/loom-records/references/naming-and-ids.md`
documented date-prefixed evidence filenames, but `skills/loom-evidence/SKILL.md`
had no corresponding creation guidance.

Why it matters:

Evidence authors could continue creating semantic-only evidence filenames despite
the shared naming table.

Follow-up:

Resolved in `ticket:namefmt54` by adding a `## Naming` section to
`skills/loom-evidence/SKILL.md`.

Challenges:

- ticket:namefmt54#ACC-003

## FIND-002: Validation wording over-applied date+slug matching

Severity: medium
Confidence: high
State: open

Observation:

The initial validation wording referred to date-prefixed owner records generally,
which could be misread to include ticket filenames even though tickets use
date+token+short-slug and `id: ticket:<token>`.

Why it matters:

The naming convention must not create false validation failures for ticket files,
and it should check the filename date against `created_at` for the date+slug
record families.

Follow-up:

Resolved in `ticket:namefmt54` by narrowing the validation check to initiative,
plan, critique, and evidence date+slug records and adding the `created_at` date
check.

Challenges:

- ticket:namefmt54#ACC-004

## FIND-003: Age-only pruning wording was too strong for canonical records

Severity: low
Confidence: high
State: open

Observation:

The initial owner-skill naming sections said records could eventually be retained
or pruned by age.

Why it matters:

Canonical owner records should not imply deletion by age alone; any cleanup still
needs lifecycle, status, evidence, and reference reconciliation policy.

Follow-up:

Resolved in `ticket:namefmt54` by replacing that wording with temporal discovery
and future retention or cleanup decisions.

Challenges:

- ticket:namefmt54#ACC-002

# Evidence Reviewed

- `evidence:date-prefixed-owner-record-naming-validation`
- `skills/loom-records/references/naming-and-ids.md`
- `skills/loom-records/references/validation.md`
- `skills/loom-initiatives/SKILL.md`
- `skills/loom-plans/SKILL.md`
- `skills/loom-critique/SKILL.md`
- `skills/loom-evidence/SKILL.md`
- `skills/loom-critique/templates/critique-packet.md`
- Oracle review task `ses_21088ef08ffeQ4NqpWuZg2QjPI`, including initial findings
  and follow-up no-findings review

# Residual Risks

- Existing historical `.loom` records still contain legacy non-date filenames;
  this is accepted as legacy-compatible, not a current product-surface blocker.
- The route-token simplification critique rename must be staged as a delete plus
  new path together if committed later.
- This review did not define the future retention policy.

# Required Follow-up

None before acceptance. The ticket owns the resolved dispositions for all open
findings above.

# Acceptance Recommendation

`no-critique-blockers`
