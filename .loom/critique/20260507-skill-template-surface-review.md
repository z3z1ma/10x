---
id: critique:skill-template-surface-review
kind: critique
status: final
created_at: 2026-05-07T06:34:27Z
updated_at: 2026-05-07T06:34:27Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:tmplrs07 skills/ product-surface diff"
links:
  ticket:
    - ticket:tmplrs07
  research:
    - research:skill-template-benchmark-synthesis
  evidence:
    - evidence:skill-template-surface-validation
external_refs: {}
---

# Summary

Adversarial review of the high-risk skill/template reasoning-surface overhaul for
`ticket:tmplrs07`. The review inspected the dirty `skills/` diff, the active
ticket, benchmark research, and structural validation evidence.

# Review Target

Target: `ticket:tmplrs07` and the current dirty product-surface diff affecting
`skills/`, plus root Loom records linked to the ticket.

Review profiles applied:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- product-ux

# Verdict

`pass_with_findings`

The initial review found one medium blocker in the compact ticket template and
two low findings. The medium blocker and one low wording drift were addressed and
verified in a follow-up read-only review. No unresolved high or medium
product-surface blockers remain. The ticket ledger still needs final
reconciliation before closure.

# Findings

## FIND-001: Compact ticket review gate lacked rationale prompts

Severity: medium
Confidence: high
State: open

Challenges:

- ticket:tmplrs07#ACC-001
- ticket:tmplrs07#ACC-008

Observation:

The first reviewed version of `skills/loom-tickets/templates/ticket.md` preserved
critique policy, disposition, profiles, findings, promotion disposition, and wiki
disposition, but did not explicitly prompt for critique policy rationale or
promotion deferral/not-required rationale. This conflicted with
`skills/loom-tickets/references/acceptance-gate.md`, which requires those
rationales for closure decisions.

Why it matters:

Without compact rationale prompts, future tickets could appear closure-compatible
by filling statuses while omitting the ticket-owned rationale needed to defer or
reject critique and promotion follow-through.

Follow-up:

Addressed in `skills/loom-tickets/templates/ticket.md` by adding `Critique
rationale:` and `Promotion / deferral rationale:` prompts. Follow-up review
verified the finding as resolved. The ticket should consume this finding with a
ticket-owned disposition of `resolved`.

## FIND-002: Active ticket still needs parent reconciliation before acceptance

Severity: low
Confidence: high
State: open

Challenges:

- ticket:tmplrs07#ACC-008

Observation:

At review time, `.loom/tickets/20260507-tmplrs07-simplify-template-reasoning-surfaces.md`
still recorded evidence, critique, and promotion disposition as pending, while
`evidence:skill-template-surface-validation` and this critique now provide the
records the ticket should consume.

Why it matters:

Tickets are the live execution ledger. Acceptance review should not depend on
evidence or critique records alone; the ticket must record evidence disposition,
critique disposition, finding disposition, promotion disposition, and acceptance
basis.

Follow-up:

Reconcile the ticket before closure.

## FIND-003: Risk restatement wording was slightly inconsistent

Severity: low
Confidence: medium
State: open

Challenges:

None - not claim-specific.

Observation:

`skills/loom-records/references/change-class.md` initially said the risk class
restated in `# Review And Follow-Through` must match frontmatter, but the new
ticket template does not restate risk class. `acceptance-gate.md` correctly says
body sections may restate risk.

Why it matters:

The wording could create minor operator-clarity drift.

Follow-up:

Addressed by making the rule conditional: if `# Review And Follow-Through`
restates `risk_class`, it must match frontmatter. Follow-up review verified the
finding as resolved.

# Evidence Reviewed

- `git status`, scoped dirty diff, and diff stat for `skills/` plus root Loom records.
- `skills/loom-tickets/templates/ticket.md`
- `skills/loom-specs/templates/spec.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`
- `skills/loom-drive/templates/outer-loop-handoff.md`
- `skills/loom-plans/templates/plan.md`
- `skills/loom-research/templates/research.md`
- `skills/loom-evidence/templates/evidence.md`
- `skills/loom-records/references/change-class.md`
- `skills/loom-records/references/claim-coverage.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-tickets/references/acceptance-gate.md`
- `skills/loom-critique/references/critique-lens.md`
- `.loom/tickets/20260507-tmplrs07-simplify-template-reasoning-surfaces.md`
- `.loom/research/20260507-skill-template-benchmark-synthesis.md`
- `.loom/evidence/20260507-skill-template-surface-validation.md`
- Follow-up verification of `skills/loom-tickets/templates/ticket.md:86-105` and
  `skills/loom-records/references/change-class.md:56-60` after fixes.

# Residual Risks

- Structural review cannot prove future agents will follow the new guidance.
- The large unrelated untracked `examples/` surface was not reviewed in depth.
- No package/install distribution check was performed.
- The ticket ledger needs final reconciliation before closure.

# Required Follow-up

- Reconcile `ticket:tmplrs07` with `evidence:skill-template-surface-validation`
  and this critique.
- Record ticket-owned disposition for `critique:skill-template-surface-review#FIND-001`
  as `resolved` before closure.
- Record promotion/retrospective disposition as completed, deferred, or not
  required before closure.

# Acceptance Recommendation

`ticket-acceptance-review-needed`

No further product-surface changes are required by this critique. The ticket can
proceed to acceptance once the ticket ledger consumes the evidence and critique
findings and records a closure-compatible promotion disposition.
