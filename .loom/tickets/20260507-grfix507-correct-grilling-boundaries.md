---
id: ticket:grfix507
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T15:15:00Z
updated_at: 2026-05-07T15:36:24Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:grill507
  evidence:
    - evidence:grilling-boundary-correction-validation
  critique:
    - critique:grilling-boundary-correction-review
external_refs:
  matt_grill_with_docs: https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md
depends_on: []
---

# Summary

Correct the grilling changes so grilling is procedural skill behavior, not record
template surface, and so spec grilling hardens behavior contracts without coupling
the spec to current implementation reality.

# Context

The prior `ticket:grill507` edits added grilling rows to spec and plan templates and
let spec grilling inspect current code. The user rejected both choices. The correct
shape is: plans use grilling as a skill procedure that relentlessly hunts ambiguity
with one-question-at-a-time interrogation and recommended answers; specs use
grilling to make intended behavior and acceptance rock solid as a standalone
behavior contract.

# Scope

In:

- Remove grilling sections from spec and plan templates.
- Move plan grilling into `loom-plans` procedure guidance.
- Rewrite spec grilling as behavior-contract hardening with no current-code/source
  coupling.
- Remove spec guidance that treats current implementation behavior as a source of
  intended behavior.
- Validate structurally and run critique before closure.

Out:

- Do not add a new grill skill.
- Do not add command wrappers, hidden runtime, or external ontology.
- Do not modify unrelated todo-app example files.

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:grfix507#ACC-001
- ticket:grfix507#ACC-002
- ticket:grfix507#ACC-003
- ticket:grfix507#ACC-004
- ticket:grfix507#ACC-005

Ticket-local criteria:

- ACC-001: Spec and plan templates no longer contain grilling-pass sections or rows.
- ACC-002: Plan skill guidance includes the grilling procedure as operator behavior: relentlessly walk ambiguity, ask one material question at a time, provide recommended answers, challenge terminology, use concrete scenarios, and route resolved decisions.
- ACC-003: Plan guidance still centers decomposition into ticket-ready execution units.
- ACC-004: Spec skill guidance keeps grilling as behavior-contract hardening while avoiding current implementation/source coupling.
- ACC-005: Structural validation and critique find no unresolved high/medium blockers or owner-layer boundary regression.

# Current State

Status rationale:

`closed` because corrective edits, validation evidence, mandatory critique,
follow-up wording, finding disposition, and acceptance reconciliation are recorded.

Blockers:

None.

Execution notes:

- Product write boundary is `skills/loom-specs` and `skills/loom-plans` plus this
  ticket, validation evidence, and critique.
- The correction removes template grilling sections and removes current-code/current
  implementation coupling from spec surfaces.

Continuation note:

No immediate continuation is required for this ticket.

# Evidence

Disposition: sufficient for closure

Records:

- `evidence:grilling-boundary-correction-validation`

Gaps / limits:

- Evidence is structural and content-anchor based; it does not prove future agents
  will apply grilling well.
- Validation was scoped to `skills/loom-specs`, `skills/loom-plans`, and this
  ticket's records; unrelated worktree changes were outside scope.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk correction to spec/plan operator behavior and owner-layer boundaries.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency

Findings:

- `critique:grilling-boundary-correction-review#FIND-001`: resolved by this ticket
  reconciliation linking evidence and critique, recording dispositions, and filling
  acceptance provenance.
- `critique:grilling-boundary-correction-review#FIND-002`: resolved by updating
  `evidence:grilling-boundary-correction-validation` with observed HEAD commit
  `d75d3a418936613dcfc8a7741953292589981d66` and rerunning scoped checks.
- `critique:grilling-boundary-correction-review#FIND-003`: resolved by changing
  `loom-specs/SKILL.md` so specs preserve resolved/routed/blocking decisions, not
  grilling process metadata.

Promotion disposition: completed
Promotion / deferral rationale: accepted corrections landed in existing spec and
plan skill/reference/template surfaces rather than a new grill skill or template
ledger.

Promoted / deferred:

- Promoted into `skills/loom-specs/SKILL.md`,
  `skills/loom-specs/references/spec-shape.md`,
  `skills/loom-specs/templates/spec.md`, `skills/loom-plans/SKILL.md`,
  `skills/loom-plans/references/plan-shape.md`, and
  `skills/loom-plans/templates/plan.md`.

Wiki disposition: not_required - the product skill corpus and critique/evidence
records carry the accepted correction; no separate wiki page is needed.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent under user-delegated Loom operation
Accepted at: 2026-05-07T15:36:24Z
Basis: `ticket:grfix507#ACC-001` through `ticket:grfix507#ACC-005` are supported
by scoped skill edits, `evidence:grilling-boundary-correction-validation`, and
mandatory critique `critique:grilling-boundary-correction-review`; no high/medium
blockers remain.
Residual risks: Markdown guidance cannot prove future agents will grill well;
evidence is scoped to spec/plan skill surfaces; unrelated worktree changes remain
outside this ticket's acceptance scope.

# Dependencies

None.

# Journal

- 2026-05-07T15:15:00Z: Created corrective ticket after user rejected grilling as template content and current-code-coupled spec grilling.
- 2026-05-07T15:32:57Z: Removed grilling sections from spec and plan templates,
  moved plan grilling into skill procedure, rewrote spec grilling as behavior
  contract hardening, and recorded validation evidence.
- 2026-05-07T15:36:24Z: Mandatory critique found no high/medium blockers; addressed
  low findings by adding source fingerprint evidence and removing spec wording that
  could preserve grilling process metadata.
- 2026-05-07T15:36:24Z: Linked evidence and critique, dispositioned findings,
  recorded acceptance, and closed the ticket.
