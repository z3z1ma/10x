---
id: critique:skills-only-example-reconciliation-review
kind: critique
status: final
created_at: 2026-04-30T16:43:49Z
updated_at: 2026-04-30T16:43:49Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:9bgilfwy
links:
  ticket:
    - ticket:9bgilfwy
  evidence:
    - evidence:skills-only-example-reconciliation
external_refs: {}
---

# Summary

Operator-surface critique for reconciling stale examples with the skills-only
product boundary.

# Review Target

Reviewed the example reconciliation changes for `ticket:9bgilfwy`, including the
deleted example 03 command-wrapper fixture, updated core example prose, and
supporting ticket/evidence records.

# Verdict

`pass`

The first critique pass found one low-severity consistency issue. The parent
fixed it, and re-review confirmed no new medium/high findings.

# Findings

## FIND-001: Example 03 common wrong behavior used old command wording

Severity: low
Confidence: high
Disposition: resolved

Observation:

`examples/03-feature-with-spec-plan-ticket-ralph/common-wrong-behavior.md` still
said "adding a command without a spec or ticket" while the reconciled README now
frames the stale behavior as adding a command wrapper as the product surface.

Why it matters:

The older wording was not a direct command-route instruction, but it left one
example surface less aligned with the current skills-only product boundary.

Follow-up:

Resolved by changing the common wrong behavior to: "adding a command wrapper as
the product surface when behavior belongs in a skill".

Challenges:

None - not claim-specific after resolution.

# Evidence Reviewed

- `ticket:9bgilfwy`
- `evidence:skills-only-example-reconciliation`
- `examples/README.md`
- `examples/02-bugfix-with-reproduction/README.md`
- `examples/03-feature-with-spec-plan-ticket-ralph/**`
- `examples/06-evidence-carrying-pr/expected-route.md`
- `examples/06-evidence-carrying-pr/after/pr-body.md`
- `git diff --check`
- targeted greps for `/loom-*`, `after/commands`, `commands/loom`, and stale
  command wording
- Oracle read-only critique and re-review output in the parent session

# Residual Risks

- Adapter examples still use "command" terminology for harness-native operations;
  current uses appear transport-specific or negative rather than Loom product
  surface instructions.
- Structural evidence cannot prove future operators will not infer command-wrapper
  workflows from outside the examples.

# Required Follow-up

None for this tranche.

# Acceptance Recommendation

complete pending acceptance
