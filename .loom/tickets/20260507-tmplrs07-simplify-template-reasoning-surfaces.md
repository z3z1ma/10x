---
id: ticket:tmplrs07
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T06:17:26Z
updated_at: 2026-05-07T06:35:34Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  constitution:
    - constitution:main
  research:
    - research:skill-template-benchmark-synthesis
  evidence:
    - evidence:skill-template-surface-validation
  critique:
    - critique:skill-template-surface-review
external_refs:
  mattpocock_skills_engineering: https://github.com/mattpocock/skills/tree/main/skills/engineering
  addyosmani_agent_skills: https://github.com/addyosmani/agent-skills
depends_on: []
---

# Summary

Simplify overbuilt Loom templates while sharpening the skill corpus around
reasoning, assumptions, quality, anti-rationalization, and evidence-backed
verification.

# Context

The user compared the `with-loom` and `without-loom` todo apps and concluded
that Loom produced more auditability and robustness but not an obviously better
UI per time spent. They asked to use that blue/green run plus external
high-quality skill examples to improve Loom proper.

# Scope

In:

- Simplify the ticket template into fewer, higher-signal sections while preserving closure gates.
- Simplify packet and support templates by moving repeated doctrine out of copy surfaces.
- Strengthen weak reasoning templates, especially specs, skill-authoring templates, research/spike, evidence, and critique.
- Add anti-rationalization, red-flag, and verification guidance to core owner, workflow, support, and coordinator skills where it changes agent behavior.
- Add product/UX/visual quality, assumptions, quality delta, examples/non-examples, and variant/exploration guidance where appropriate.
- Preserve Markdown-native, script-free, no-hidden-runtime Loom boundaries.

Out:

- Do not add scripts, validators, CLIs, daemons, MCP requirements, command wrappers, hidden runtimes, or new canonical owner layers.
- Do not import external skill text wholesale or make external repositories authoritative.
- Do not weaken ticket-owned acceptance, evidence, critique, promotion, or parent reconciliation boundaries.
- Do not rewrite package docs unless a changed skill/template would otherwise contradict them.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| External skill repositories are advisory examples, not authority. | yes | no | Accepted and recorded in `research:skill-template-benchmark-synthesis`. |
| The product surface should remain `skills/` only. | no | yes if contradicted | Inherited from `constitution:main`; no hidden runtime or new layer added. |
| Active ticket should be reconciled into the new compact ticket shape. | yes | no | Completed during acceptance reconciliation. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:tmplrs07#ACC-001
- ticket:tmplrs07#ACC-002
- ticket:tmplrs07#ACC-003
- ticket:tmplrs07#ACC-004
- ticket:tmplrs07#ACC-005
- ticket:tmplrs07#ACC-006
- ticket:tmplrs07#ACC-007
- ticket:tmplrs07#ACC-008

Ticket-local criteria:

- ACC-001: `skills/loom-tickets/templates/ticket.md` is materially shorter and lower-noise while preserving acceptance, evidence, critique, follow-through, acceptance decision, dependencies, and journal truth.
- ACC-002: Claim matrices are no longer default ticket ceremony and are documented as optional when claim coverage complexity warrants them.
- ACC-003: `skills/loom-specs/templates/spec.md` and spec guidance force stronger reasoning around assumptions, quality bars, examples/non-examples, decision points, and evidence plans.
- ACC-004: Ralph, critique, wiki, drive handoff, plan, research, and evidence templates are tightened or strengthened according to their role without weakening safety fields.
- ACC-005: Core skills include targeted common rationalizations, red flags, and verification guidance where that guidance changes agent behavior.
- ACC-006: Product/UX/visual review, UI/product evidence, spike/sketch variant exploration, debugging hypotheses, and external skill benchmark lessons are reflected in the appropriate product-surface skills or references.
- ACC-007: Skill-authoring guidance and templates teach future skill authors the improved structure: process over knowledge, anti-rationalization, red flags, and evidence-backed verification.
- ACC-008: Structural validation and adversarial critique find no unresolved high/medium blockers for the changed product surface.

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:tmplrs07#ACC-001 | evidence:skill-template-surface-validation | critique:skill-template-surface-review#FIND-001 resolved | supported |
| ticket:tmplrs07#ACC-002 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-003 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-004 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-005 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-006 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-007 | evidence:skill-template-surface-validation | critique:skill-template-surface-review no blocker | supported |
| ticket:tmplrs07#ACC-008 | evidence:skill-template-surface-validation | critique:skill-template-surface-review#FIND-001 resolved; #FIND-002 resolved | supported |

# Current State

Status rationale:

`closed` because the product-surface edits landed, structural validation passed,
mandatory critique is final, the one medium finding was fixed and verified, and
ticket-owned evidence, critique, promotion, and acceptance dispositions are now
closure-compatible.

Blockers:

None.

Execution notes:

- Simplified high-noise templates and strengthened spec/research/evidence/critique/Ralph guidance.
- Added product/UX/visual review and evidence routes without creating a new owner layer.
- Added common rationalizations, red flags, and verification sections across core owner, workflow, support, and coordinator skills.
- Reconciled stale ticket section references from old headings to `# Acceptance` and `# Review And Follow-Through`.
- Fixed critique-requested ticket-template rationale prompts and conditional risk-restatement wording.

Continuation note:

No continuation required for this ticket. Future package/release work, if needed,
belongs in separate ship or release-packaging work.

# Evidence

Disposition: sufficient

Records:

- evidence:skill-template-surface-validation — supports ticket:tmplrs07#ACC-001 through ticket:tmplrs07#ACC-008 with structural scans, targeted reference checks, behavior-guard coverage, no-hidden-runtime lexical check, and follow-up validation after critique fixes.

Gaps / limits:

- Structural evidence cannot prove future agents will follow the guidance.
- No package/install distribution check was run because this ticket changed source product-surface Markdown, not a release package.
- The large unrelated untracked `examples/` surface was not reviewed as part of this ticket.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk `protocol-authority` changes touched operator behavior, template copy surfaces, ticket closure posture, critique/evidence expectations, and skill activation/verification behavior.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- product-ux

Findings:

- critique:skill-template-surface-review#FIND-001 — resolved by adding `Critique rationale:` and `Promotion / deferral rationale:` prompts to `skills/loom-tickets/templates/ticket.md`; follow-up review verified the fix.
- critique:skill-template-surface-review#FIND-002 — resolved by this ticket reconciliation of evidence, critique, promotion disposition, claim matrix, and acceptance basis.
- critique:skill-template-surface-review#FIND-003 — resolved by making `skills/loom-records/references/change-class.md` conditional when `# Review And Follow-Through` restates `risk_class`; follow-up review verified the fix.

Promotion disposition: completed
Promotion / deferral rationale: the durable lessons from the todo comparison and external skill benchmark were promoted into the product surface that owns this protocol behavior: templates, SKILL files, and references. No separate wiki page is required because this ticket updates the governing skill corpus directly, and the investigation remains citable in `research:skill-template-benchmark-synthesis`.

Promoted / deferred:

- Promoted into `skills/loom-tickets/templates/ticket.md`, ticket readiness and acceptance references, and claim coverage references.
- Promoted into spec, evidence, research, plan, Ralph, critique, wiki, drive, debugging, spike, and skill-authoring templates/references where they own the behavior.
- Promoted anti-rationalization/red-flag/verification scaffolds into core SKILL files where they change operator behavior.

Wiki disposition: not_required — accepted explanation did not need a separate wiki page for this bounded product-surface mutation.

# Acceptance Decision

Accepted by: OpenCode agent under current user-delegated task
Accepted at: 2026-05-07T06:35:34Z
Basis: all ticket-local acceptance criteria are supported by `evidence:skill-template-surface-validation`; mandatory `critique:skill-template-surface-review` is final with no unresolved high/medium blockers; the one medium finding has ticket-owned disposition `resolved`.
Residual risks: structural review cannot prove future agent compliance; package/install distribution was not checked; unrelated example-app untracked work was not reviewed for this ticket.

# Dependencies

None.

# Journal

- 2026-05-07T06:17:26Z: Created ticket and benchmark research after user requested full implementation of template simplification and skill-quality changes.
- 2026-05-07T06:27:32Z: Recorded structural validation evidence for the product-surface edits.
- 2026-05-07T06:34:27Z: Recorded mandatory critique after adversarial review and follow-up verification.
- 2026-05-07T06:35:34Z: Reconciled evidence, critique findings, promotion disposition, claim matrix, and acceptance basis; closed the ticket.
