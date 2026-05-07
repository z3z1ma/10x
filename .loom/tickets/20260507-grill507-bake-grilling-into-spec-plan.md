---
id: ticket:grill507
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T14:57:22Z
updated_at: 2026-05-07T15:05:12Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:engdisc7
  research:
    - research:grill-diagnose-gap-analysis
  evidence:
    - evidence:grill-spec-plan-validation
  critique:
    - critique:grill-spec-plan-review
external_refs:
  matt_grill_with_docs: https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md
  matt_diagnose: https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md
depends_on: []
---

# Summary

Bake Matt Pocock's grilling discipline into Loom spec and plan creation, and
correct plan guidance so plans primarily decompose high-level work into detailed
ticket-ready execution units rather than only owning sequencing and waves.

# Context

The prior engineering-discipline tranche added pressure checks and vertical-slice
language, but the user identified a remaining gap: `grill-with-docs` is an active
interview and codebase/domain-model challenge loop, not just a table in a spec;
plans are primarily where high-level work is teased apart into executable slices
for tickets, not merely an ordering document.

# Scope

In:

- Re-read Matt's `grill-with-docs` and `diagnose` source.
- Strengthen `loom-specs` so spec creation includes a grilling pass over language,
  codebase truth, concrete scenarios, recommended answers, and decision capture.
- Strengthen `loom-plans` so plan creation centers decomposition into vertical or
  otherwise ticket-ready execution units, with sequencing and waves as secondary
  strategy concerns.
- Tighten `loom-debugging` where Matt's diagnose loop still exposes gaps.
- Validate structurally and run critique before closure.

Out:

- Do not add Matt's `CONTEXT.md` or ADR file layout as Loom ontology.
- Do not add command wrappers, hidden runtime, required scripts, or external issue
  tracker ownership.
- Do not modify unrelated todo-app example files.

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:grill507#ACC-001
- ticket:grill507#ACC-002
- ticket:grill507#ACC-003
- ticket:grill507#ACC-004
- ticket:grill507#ACC-005

Ticket-local criteria:

- ACC-001: Gap analysis records how Matt's `grill-with-docs` and `diagnose` differ from current Loom spec, plan, and debugging guidance.
- ACC-002: Spec guidance and template make the grilling pass part of spec creation: codebase-first questions, one material question at a time, recommended answers, terminology conflict handling, concrete scenarios, and sparse durable decision capture.
- ACC-003: Plan guidance and template make decomposition into detailed ticket-ready execution units the primary plan job, with sequencing/waves secondary and each unit carrying outcome, source claim, write scope, verification, non-goals, and loopback conditions.
- ACC-004: Debugging guidance reflects the remaining diagnose gap around domain orientation, aggressive feedback-loop construction, and stopping when no credible loop exists.
- ACC-005: Structural validation and critique find no unresolved high/medium blockers, hidden-runtime drift, or owner-layer boundary regression.

# Current State

Status rationale:

`closed` because gap analysis, skill edits, validation evidence, mandatory critique,
follow-up fixes, and acceptance reconciliation are recorded in the owning layers.

Blockers:

None.

Execution notes:

- Product write boundary was `skills/` plus this ticket, gap research, validation
  evidence, and critique.
- External source files are evidence. Loom skill files remain the product surface.
- The unrelated `package.json` modification observed by critique is outside this
  ticket's scope and is not part of this ticket's acceptance claim.

Continuation note:

No immediate continuation is required for this ticket. Later pressure-scenario
evidence may be useful if future operators need proof that the grilling guidance
changes behavior in practice.

# Evidence

Disposition: sufficient for closure

Records:

- `evidence:grill-spec-plan-validation`

Gaps / limits:

- Evidence is structural and content-anchor based; it does not prove future
  operator compliance.
- This repository has no automated test suite for Markdown skill behavior.
- Unrelated `package.json` and todo-app example changes were outside this ticket's
  validation scope.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority changes to spec creation, plan creation, debugging, and ticket-decomposition behavior.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency

Findings:

- `critique:grill-spec-plan-review#FIND-001`: low, non-blocking source-provenance
  finding addressed by recording Matt's clone commit in
  `research:grill-diagnose-gap-analysis`.
- `critique:grill-spec-plan-review#FIND-002`: low, non-blocking template wording
  finding addressed by changing the spec and plan template rows to `Material ...
  question, one row at a time`.
- `critique:grill-spec-plan-review#FIND-003`: low, non-blocking debugging-order
  finding addressed by changing `loom-debugging/SKILL.md` to start with
  `orient -> feedback loop`.

Promotion disposition: completed
Promotion / deferral rationale: accepted changes landed in existing spec, plan, and
debugging skill surfaces rather than a new grill skill, runtime, command wrapper,
or external ontology.

Promoted / deferred:

- Promoted into `skills/loom-specs/SKILL.md`,
  `skills/loom-specs/references/spec-shape.md`,
  `skills/loom-specs/templates/spec.md`, `skills/loom-plans/SKILL.md`,
  `skills/loom-plans/references/plan-shape.md`,
  `skills/loom-plans/references/slicing.md`,
  `skills/loom-plans/templates/plan.md`, `skills/loom-debugging/SKILL.md`, and
  `skills/loom-debugging/references/systematic-debugging.md`.
- Deferred behavioral proof of future operator compliance until later usage or
  pressure-scenario evidence exists.

Wiki disposition: not_required - the accepted guidance is now in the product skill
corpus and concluded research; no separate wiki page is needed for closure.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent under user-delegated Loom operation
Accepted at: 2026-05-07T15:05:12Z
Basis: `ticket:grill507#ACC-001` through `ticket:grill507#ACC-005` are supported
by `research:grill-diagnose-gap-analysis`, changed spec/plan/debugging skill
surfaces, `evidence:grill-spec-plan-validation`, and final mandatory critique
`critique:grill-spec-plan-review`; no high/medium blockers remain.
Residual risks: Markdown guidance cannot prove future operators will perform
grilling correctly without later pressure-scenario evidence; template additions
depend on future record authors replacing placeholders truthfully; unrelated
`package.json` remains outside this ticket's scope.

# Dependencies

None.

# Journal

- 2026-05-07T14:57:22Z: Created ticket after user identified the remaining gap in grilling/spec/plan guidance and asked for closer comparison against Matt's source skills.
- 2026-05-07T14:59:56Z: Recorded validation evidence for the scoped spec, plan,
  debugging, ticket, and research changes.
- 2026-05-07T15:04:23Z: Mandatory critique found no high/medium product-surface
  blockers and raised low findings around source provenance, template question
  wording, debugging top-level order, and unrelated `package.json` scope.
- 2026-05-07T15:04:23Z: Addressed low findings by pinning Matt's clone commit,
  clarifying template question wording, and moving debugging domain orientation
  before feedback-loop construction in the top-level route.
- 2026-05-07T15:05:12Z: Linked evidence and critique, recorded dispositions,
  excluded unrelated `package.json` from acceptance scope, and closed the ticket.
