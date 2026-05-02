---
id: critique:<slug>
kind: critique
status: draft
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
review_target: <record ref | code change target>
links: {}
external_refs: {}
---

# Summary

What this critique reviewed.

# Review Target

Name the specific target and why it was reviewed. For code review, name the
branch, commit, diff range, pull request, or changed file set.

# Verdict

Use one verdict value and explain it:

- `pass`
- `pass_with_findings`
- `changes_required`
- `inconclusive`

Set `status: final` only when evidence reviewed, findings, residual risks, and
acceptance recommendation are complete enough for the ticket to consume.

# Findings

List concrete findings with stable finding IDs. Remove the example finding or
write `None - no findings` when no finding applies.

## FIND-<nnn>: Short finding title

Severity: low | medium | high
Confidence: low | medium | high
Disposition: open | resolved | accepted_risk | superseded | converted_to_follow_up

Observation:

Why it matters:

Follow-up:

Use linked ticket references when a finding is converted to follow-up work, for
example `ticket:<token>`. Tickets consume this as a ticket-owned disposition such
as `critique:example-review#FIND-001` — converted to follow-up ticket
`ticket:<token>`.

For claim-specific findings, include:

Challenges:

List real qualified claim IDs, or write `None - not claim-specific`.

# Evidence Reviewed

What records, files, diffs, tests, outputs, or evidence were inspected.

# Residual Risks

What still looks risky after the review.

# Required Follow-up

What should happen before acceptance or closure.

# Acceptance Recommendation

Use a concrete recommendation: close-ready, complete pending acceptance,
review required, active follow-up required, blocked, or accepted risk needed.
