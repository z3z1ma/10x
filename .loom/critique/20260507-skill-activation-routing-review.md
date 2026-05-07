---
id: critique:skill-activation-routing-review
kind: critique
status: final
created_at: 2026-05-07T07:53:53Z
updated_at: 2026-05-07T07:53:53Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:actvskill README.md and skills activation/routing diff"
links:
  ticket:
    - ticket:actvskill
  research:
    - research:external-skill-activation-deep-dive
  evidence:
    - evidence:skill-activation-routing-validation
external_refs: {}
---

# Summary

Adversarial review of the high-risk activation/routing product-surface changes
for `ticket:actvskill`.

# Review Target

Target: `ticket:actvskill` and the current dirty diff affecting `README.md`,
`skills/`, and linked root Loom records.

Review profiles applied:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface

# Verdict

`pass_with_findings`

The first review found one medium issue and one low issue. Both were fixed and
verified by follow-up review. No unresolved high or medium product-surface
blockers remain.

# Findings

## FIND-001: Change-class defaults missed new matching critique profiles

Severity: medium
Confidence: high
State: open

Challenges:

- ticket:actvskill#ACC-004
- ticket:actvskill#ACC-006

Observation:

`code-structure` and `dependency-tooling` critique profiles existed, but the
change-class default critique table initially routed those change classes to the
generic `code-change` profile instead of the new matching profiles.

Why it matters:

Refactors and tooling/dependency changes need tailored lenses: behavior
preservation, coupling, lockfile risk, generated-file drift, compatibility, and
feedback-loop effects. Generic defaults made the new profiles easy to miss.

Follow-up:

Resolved. `skills/loom-records/references/change-class.md` now routes
`code-structure` to `code-structure`, plus `code-change` when behavior risk is
plausible, and routes `dependency-tooling` to `dependency-tooling`, plus
`security` when dependency risk matters.

## FIND-002: Local execution still had token-like residue

Severity: low
Confidence: high
State: open

Challenges:

- ticket:actvskill#ACC-003

Observation:

The new local execution boundary was mostly clear, but old terms such as
`local_edit`, `local-edit-ready`, `ticket-local fix`, and `local edit` remained in
several skills/references.

Why it matters:

The main guidance says local execution is not a workflow token or ticket bypass.
Leftover token-like language could revive route-token thinking.

Follow-up:

Resolved. The language was normalized to local execution. Follow-up validation
confirmed `rg -n 'local_edit|local-edit-ready|ticket-local fix|local edit' skills`
returns no output.

# Evidence Reviewed

- `git status --short`
- scoped dirty diff/stat for `README.md`, `skills/`, and linked root Loom records
- `git diff --check` with no output
- `.loom/tickets/20260507-actvskill-broaden-skill-activation.md`
- `.loom/research/20260507-external-skill-activation-deep-dive.md`
- `.loom/evidence/20260507-skill-activation-routing-validation.md`
- all `skills/*/SKILL.md` descriptions
- `skills/loom-workspace/references/task-routing-catalog.md`
- `skills/loom-tickets/references/local-execution.md`
- `skills/loom-records/references/change-class.md`
- `skills/loom-critique/references/critique-lens.md`
- `skills/loom-evidence/references/evidence-quality.md`
- `skills/loom-wiki/references/shared-language.md`
- `skills/loom-skill-authoring/references/principles.md`
- README routing and skill-map changes
- Follow-up verification of `change-class.md:33-47`, local execution language,
  `git diff --check`, and supplemental evidence lines.

# Residual Risks

- Structural review cannot prove future harness autoactivation quality.
- No package/install distribution check was performed.
- The unrelated untracked example-app surface was not reviewed.

# Required Follow-up

- Reconcile `ticket:actvskill` with `evidence:skill-activation-routing-validation`
  and this critique.
- Record ticket-owned dispositions for both findings as `resolved` before closure.
- Record promotion/acceptance disposition before closure.

# Acceptance Recommendation

`no-critique-blockers`

Accept the product-surface changes for `ticket:actvskill` after ticket ledger
reconciliation. No high or medium critique blockers remain.
