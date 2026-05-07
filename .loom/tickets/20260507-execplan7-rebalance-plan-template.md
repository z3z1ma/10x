---
id: ticket:execplan7
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T17:15:48Z
updated_at: 2026-05-07T17:20:27Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:execplan-plan-template-validation
  critique:
    - critique:execplan-plan-template-review
external_refs:
  openai_codex_exec_plans: https://developers.openai.com/cookbook/articles/codex_exec_plans
depends_on: []
---

# Summary

Rebalance the Loom plan template and guidance against OpenAI's Codex ExecPlan
article, incorporating Loom's owner layers deeply instead of copying ExecPlan's
progress-log shape into plans.

# Context

The user asked whether all current plan sections hold their weight and noted the
original template was supposed to be based on the Codex ExecPlan article. Direct
comparison shows the current template over-emphasizes Loom-specific review tables
and omits or weakens several ExecPlan ideas that matter for long-running work:
purpose/big picture, context/orientation, narrative milestones, validation and
acceptance, idempotence/recovery, interfaces/dependencies, and concise artifacts.

# Scope

In:

- Update `skills/loom-plans/templates/plan.md` so each section is weight-bearing.
- Update `skills/loom-plans/references/plan-shape.md` to explain the ExecPlan to
  Loom mapping.
- Update `skills/loom-plans/SKILL.md` if top-level plan questions need alignment.
- Keep tickets as the live progress ledger; do not import ExecPlan `Progress` as a
  plan-owned live state section.
- Validate structurally and run critique before closure.

Out:

- Do not add a `PLANS.md` product surface.
- Do not add hidden runtimes, command wrappers, commit requirements, or a second
  execution ledger.
- Do not modify unrelated todo-app example files.

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:execplan7#ACC-001
- ticket:execplan7#ACC-002
- ticket:execplan7#ACC-003
- ticket:execplan7#ACC-004
- ticket:execplan7#ACC-005

Ticket-local criteria:

- ACC-001: Plan template sections each carry a distinct job tied to either ExecPlan intent or Loom ownership, without redundant confidence/review sections.
- ACC-002: Plan template includes purpose/big picture, context/orientation, execution units, narrative milestones, validation/acceptance strategy, idempotence/recovery, interfaces/dependencies, decision rationale, artifacts/notes, risks/loopbacks, readiness, exit criteria, and completion basis.
- ACC-003: Plan guidance maps ExecPlan living-document concepts into Loom owners: tickets own live progress, evidence owns observations/artifacts, research owns discoveries/tradeoffs, and plan owns strategy/decomposition decisions.
- ACC-004: Plan guidance preserves decomposition into ticket-ready units as the center of gravity and avoids turning plans into implementation progress logs or command choreography.
- ACC-005: Structural validation and critique find no unresolved high/medium blockers or owner-layer boundary regression.

# Current State

Status rationale:

`closed` because plan guidance/template edits, validation evidence, mandatory
critique, follow-up wording, finding disposition, and acceptance reconciliation are
recorded.

Blockers:

None.

Execution notes:

- Product write boundary is `skills/loom-plans` plus this ticket, validation
  evidence, and critique.
- The OpenAI article is an external reference, not Loom authority.

Continuation note:

No immediate continuation is required for this ticket.

# Evidence

Disposition: sufficient for closure

Records:

- `evidence:execplan-plan-template-validation`

Gaps / limits:

- Evidence is structural and content-anchor based; it does not prove future plan
  authoring quality.
- Validation is scoped to `skills/loom-plans` and this ticket's records; unrelated
  worktree changes were outside scope.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority change to plan structure and execution-strategy ownership.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency

Findings:

- `critique:execplan-plan-template-review#FIND-001`: resolved by removing residual
  `strategy snapshots` wording from `loom-plans/SKILL.md` and confirming no
  strategy-snapshot terms remain.
- `critique:execplan-plan-template-review#FIND-002`: accepted as residual risk;
  structural evidence does not prove future operator authoring quality.

Promotion disposition: completed
Promotion / deferral rationale: accepted guidance landed in existing plan skill,
reference, and template surfaces rather than a `PLANS.md` product surface or a
second execution ledger.

Promoted / deferred:

- Promoted into `skills/loom-plans/SKILL.md`,
  `skills/loom-plans/references/plan-shape.md`, and
  `skills/loom-plans/templates/plan.md`.

Wiki disposition: not_required - the product skill corpus and validation/critique
records carry the accepted correction; no separate wiki page is needed.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent under user-delegated Loom operation
Accepted at: 2026-05-07T17:20:27Z
Basis: `ticket:execplan7#ACC-001` through `ticket:execplan7#ACC-005` are supported
by scoped plan skill edits, `evidence:execplan-plan-template-validation`, and
mandatory critique `critique:execplan-plan-template-review`; no high/medium
blockers remain.
Residual risks: Markdown guidance cannot prove future plan authoring quality; the
heavier template may need pressure-scenario evidence after use; the OpenAI article
is an external reference and not Loom authority.

# Dependencies

None.

# Journal

- 2026-05-07T17:15:48Z: Created ticket after comparing the current plan template with OpenAI's Codex ExecPlan article and finding several sections underpowered or redundant.
- 2026-05-07T17:17:53Z: Rebalanced plan template and guidance around ExecPlan
  concepts mapped into Loom owners; recorded structural validation evidence.
- 2026-05-07T17:20:27Z: Mandatory critique found no high/medium blockers; removed
  residual strategy-snapshot wording.
- 2026-05-07T17:20:27Z: Linked evidence and critique, dispositioned findings,
  recorded acceptance, and closed the ticket.
