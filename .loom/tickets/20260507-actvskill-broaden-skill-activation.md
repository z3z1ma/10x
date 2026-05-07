---
id: ticket:actvskill
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T07:39:36Z
updated_at: 2026-05-07T07:54:12Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  constitution:
    - constitution:main
  research:
    - research:external-skill-activation-deep-dive
  evidence:
    - evidence:skill-activation-routing-validation
  critique:
    - critique:skill-activation-routing-review
external_refs:
  mattpocock_skills: https://github.com/mattpocock/skills
  addyosmani_agent_skills: https://github.com/addyosmani/agent-skills
depends_on: []
---

# Summary

Broaden Loom skill activation and common coding-task routing so ordinary coding
prompts reliably enter the right Loom paper process without weakening owner-layer
truth.

# Context

The user observed that Loom's core premise is stronger than the external skill
repos because every engineering thought/process has an owner artifact. The gap is
that Loom skills and paper processes may not activate richly enough across normal
coding tasks. The deeper external benchmark found that Addy and Matt style skills
use broad natural-language triggers and concrete workflow shapes that Loom can
adapt while preserving owner truth.

# Scope

In:

- Broaden core skill frontmatter descriptions using common coding-task triggers.
- Add a task-routing catalog that maps ordinary user requests to Loom owner routes.
- Add a ticket-local execution process for single bounded implementation/local execution.
- Enrich change-class guidance for common coding work such as refactors, tests, dependencies, performance, and UI/product changes.
- Update skill-authoring guidance/templates so future skills optimize descriptions for activation.
- Add accepted shared-language guidance to the wiki paper process.
- Preserve script-free, Markdown-native, owner-layer truth boundaries.

Out:

- Do not add a new implementation owner layer.
- Do not add canonical command wrappers, daemons, validators, MCP assumptions, hidden runtimes, or issue-tracker dependencies.
- Do not copy external skills wholesale.
- Do not modify the unrelated example app surface.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Activation should improve through descriptions and routing references before adding skills. | yes | no | Accepted for this tranche. |
| Ticket-local execution can cover small implementation without a new owner layer. | yes | no | Accepted; critique did not find a Ralph/ticket boundary blocker after token-language cleanup. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:actvskill#ACC-001
- ticket:actvskill#ACC-002
- ticket:actvskill#ACC-003
- ticket:actvskill#ACC-004
- ticket:actvskill#ACC-005
- ticket:actvskill#ACC-006

Ticket-local criteria:

- ACC-001: Core skill descriptions include broad ordinary coding-task triggers while still naming the owner-layer boundary.
- ACC-002: Workspace routing includes a common-task catalog for bug fixes, features, refactors, tests, dependencies, performance, security, UI, API/interface, architecture, docs, PR/release, and acceptance/done checks.
- ACC-003: Ticket guidance includes a local execution loop for single bounded implementation work with write boundary, evidence, critique, journal, and closure reconciliation.
- ACC-004: Change-class guidance covers common coding work beyond generic code behavior, including code structure, validation instrumentation, dependency/tooling, performance-sensitive, and UI/product work.
- ACC-005: Skill-authoring guidance and templates require activation-rich descriptions with aliases/common triggers instead of owner nouns only.
- ACC-006: Structural validation and mandatory critique find no unresolved high/medium blockers for the activation/routing product surface.

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:actvskill#ACC-001 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review no blocker | supported |
| ticket:actvskill#ACC-002 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review no blocker | supported |
| ticket:actvskill#ACC-003 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review#FIND-002 resolved | supported |
| ticket:actvskill#ACC-004 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review#FIND-001 resolved | supported |
| ticket:actvskill#ACC-005 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review no blocker | supported |
| ticket:actvskill#ACC-006 | evidence:skill-activation-routing-validation | critique:skill-activation-routing-review#FIND-001 resolved; #FIND-002 resolved | supported |

# Current State

Status rationale:

`closed` because the activation/routing product-surface edits landed, structural
validation passed, mandatory critique is final, both critique findings were fixed
and verified, and evidence, critique, promotion, and acceptance dispositions are
closure-compatible.

Blockers:

None.

Execution notes:

- Broadened all core skill descriptions with ordinary coding-task trigger language while preserving owner boundaries.
- Added `skills/loom-workspace/references/task-routing-catalog.md` for common prompt-language routing.
- Added `skills/loom-tickets/references/local-execution.md` and normalized old local-edit token language.
- Added change-class coverage for `code-structure`, `validation-instrumentation`, `dependency-tooling`, `performance-sensitive`, and `ui-product`.
- Added critique/evidence guidance for the new change classes.
- Added `skills/loom-wiki/references/shared-language.md` for accepted terminology and avoided synonyms.
- Updated skill-authoring guidance/templates so future descriptions optimize for activation.
- Updated README routing and skill map to reflect common-task routing and shared language.

Continuation note:

No continuation required for this ticket. Future work could further enrich
language/glossary workflows or package docs, but this ticket's activation/routing
scope is accepted.

# Evidence

Disposition: sufficient

Records:

- evidence:skill-activation-routing-validation - supports ticket:actvskill#ACC-001 through ticket:actvskill#ACC-006 with description scans, routing/reference scans, stale-heading scan, placeholder scan, hidden-runtime lexical scan, and supplemental validation after critique fixes.

Gaps / limits:

- Structural scans cannot prove future harness autoactivation quality.
- No package/install distribution check was run because this ticket changed source product-surface Markdown and README framing.
- The unrelated untracked example-app surface was not reviewed for this ticket.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority change to skill activation, routing, common task classification, and ticket execution behavior.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface

Findings:

- critique:skill-activation-routing-review#FIND-001 - resolved by aligning `code-structure` and `dependency-tooling` change classes with matching critique profiles in `skills/loom-records/references/change-class.md`; follow-up review verified the fix.
- critique:skill-activation-routing-review#FIND-002 - resolved by normalizing old `local_edit` / local-edit language to local execution; follow-up scan and review verified the cleanup.

Promotion disposition: completed
Promotion / deferral rationale: the durable lessons from the deeper external skill inspection were promoted into the product surfaces that own them: skill descriptions, workspace routing, ticket execution guidance, change-class grammar, wiki shared-language guidance, skill-authoring guidance, and README framing.

Promoted / deferred:

- Promoted common coding-task triggers into all core `skills/*/SKILL.md` descriptions.
- Promoted common prompt routing into `skills/loom-workspace/references/task-routing-catalog.md`.
- Promoted local execution paper process into `skills/loom-tickets/references/local-execution.md`.
- Promoted change-class/evidence/critique guidance for common coding work into records/evidence/critique references.
- Promoted shared-language handling into `skills/loom-wiki/references/shared-language.md`.
- Promoted future-skill activation standards into `loom-skill-authoring` references and templates.

Wiki disposition: not_required - this ticket changed the governing wiki skill and reference directly; no separate project wiki page is needed for the product-surface lesson.

# Acceptance Decision

Accepted by: OpenCode agent under current user-delegated task
Accepted at: 2026-05-07T07:54:12Z
Basis: all ticket-local acceptance criteria are supported by `evidence:skill-activation-routing-validation`; mandatory `critique:skill-activation-routing-review` is final with no unresolved high/medium blockers; both findings have ticket-owned disposition `resolved`.
Residual risks: structural review cannot prove future harness autoactivation quality; package/install distribution was not checked; unrelated example-app untracked work was not reviewed for this ticket.

# Dependencies

None.

# Journal

- 2026-05-07T07:39:36Z: Created ticket and research after deeper external skill activation review.
- 2026-05-07T07:46:15Z: Recorded structural validation evidence for activation/routing edits.
- 2026-05-07T07:52:52Z: Added supplemental validation after critique-requested fixes.
- 2026-05-07T07:53:53Z: Recorded final mandatory critique with no unresolved high/medium blockers.
- 2026-05-07T07:54:12Z: Reconciled evidence, critique findings, promotion disposition, claim matrix, and acceptance basis; closed the ticket.
