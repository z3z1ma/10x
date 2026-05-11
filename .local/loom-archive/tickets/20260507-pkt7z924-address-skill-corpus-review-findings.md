---
id: ticket:pkt7z924
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-07T18:31:54Z
updated_at: 2026-05-07T18:45:01Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:skill-corpus-fix-structural-checks
  critique:
    - critique:skill-corpus-fix-review
external_refs: {}
depends_on: []
---

# Summary

Resolve the skill-corpus review findings across skill frontmatter guidance, shared record grammar, packet templates, ticket disposition vocabulary, and workflow read-order/reconciliation guidance.

# Context

The operator requested a full `skills/` review, then asked for all findings to be addressed directly and adversarially reviewed by an oracle. The findings are protocol-authority edits because they affect how future agents route, validate, packetize, and reconcile Loom work.

# Scope

In:

- Align packet `change_class` vocabulary with the canonical shared change-class list.
- Align packet source fingerprint placeholders with machine-readable `git_status_summary` grammar.
- Reconcile ticket evidence disposition vocabulary between the ticket template and acceptance-gate guidance.
- Clarify status lifecycle transition wording so generic transitions do not imply invalid statuses for record kinds.
- Tighten spike, debugging, skill-authoring, critique-packet, drive-handoff, and plan guidance identified by review.
- Preserve structural evidence and oracle critique disposition for the fix.

Out:

- No runtime validators, helper scripts, command wrappers, or non-Markdown protocol dependencies.
- No changes to unrelated untracked `examples/00-todo-app` worktree content.
- No broad rewrite of skill architecture beyond the reviewed inconsistencies.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| The reviewed findings can be fixed with local skill/reference/template edits rather than new owner-layer architecture. | yes | no | accepted for this ticket; oracle review will challenge scope. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:pkt7z924#ACC-001 — every finding from the operator-requested review is addressed in the relevant skill, reference, or template.
- ticket:pkt7z924#ACC-002 — structural checks verify the changed vocabulary and placeholders no longer contradict the owning references.
- ticket:pkt7z924#ACC-003 — oracle adversarial review is preserved in a final `critique:<slug>` record with verdict, evidence reviewed, residual risks, acceptance recommendation, and ticket-owned dispositions for valid findings.

# Finding Disposition

Original review findings:

| ID | Finding | Disposition |
| --- | --- | --- |
| F-001 | `packet-frontmatter.md` omitted canonical `change_class` values. | Fixed in `skills/loom-records/references/packet-frontmatter.md`. |
| F-002 | Packet templates allowed `git_status_summary` to carry “unknown with rationale” instead of the machine-readable enum. | Fixed in Ralph, critique, and wiki packet templates; rationale belongs in `git_status_detail`. |
| F-003 | Generic status transitions implied invalid lifecycle statuses for some record kinds. | Fixed in `status-lifecycle.md`; oracle follow-up O-001 further tightened source and target validity. |
| F-004 | Ticket evidence disposition vocabulary differed between the ticket template and acceptance-gate guidance. | Fixed in ticket template, acceptance gate, ticket skill verification, and status lifecycle disposition vocabulary. |
| F-005 | Write-bearing spike guidance required ticket/Ralph but Done Means lacked ticket reconciliation. | Fixed and narrowed so only throwaway code, source-tree changes, generated prototype artifacts, or other non-record mutations require this branch. |
| F-006 | Debugging read order omitted retrospective despite routing prevention lessons there. | Fixed in `skills/loom-debugging/SKILL.md`. |
| F-007 | Critique packet `parent_merge_scope.records` combined critique and ticket refs in one list item. | Fixed by splitting critique and optional ticket refs; oracle follow-up O-005 made critique record reconciliation explicit. |
| F-008 | Critique packet `review_target.paths` allowed a no-path sentinel that shared grammar did not document. | Fixed in shared packet frontmatter grammar. |
| F-009 | Drive handoff frontmatter docs omitted `handoff_kind`. | Fixed in `skills/loom-records/references/frontmatter.md`. |
| F-010 | Plan rationalizations duplicated the progress-tracking warning. | Fixed by removing the duplicate row. |
| F-011 | Skill-authoring skill lacked its own rationalizations, red flags, and verification sections. | Fixed in `skills/loom-skill-authoring/SKILL.md`. |
| F-012 | Skill-authoring read order said “the relevant template” without naming simple versus router template use. | Fixed in `skills/loom-skill-authoring/SKILL.md`. |
| F-013 | Bootstrap read order and self-audit posture were bare compared with the skill-authoring standard. | Fixed by annotating ordered references and adding rationalizations, red flags, verification, and Done Means. |

Oracle review findings:

| ID | Finding | Disposition |
| --- | --- | --- |
| O-001 | Status transition clarification needed both source and target statuses to be valid for the record kind. | Fixed in `status-lifecycle.md`. |
| O-002 | Spike reconciliation wording accidentally treated ordinary Loom record updates as write-bearing prototype mutations. | Fixed in `skills/loom-spike/SKILL.md`. |
| O-003 | Ticket acceptance was not recoverable because original findings were not listed. | Fixed by this finding disposition table. |
| O-004 | Shared lifecycle grammar did not define ticket-owned evidence disposition values. | Fixed in `status-lifecycle.md`; ticket skill prose now uses the `not_required` token. |
| O-005 | Critique packet parent merge grammar was ambiguous about output-only review versus critique record reconciliation. | Fixed by requiring a critique record parent merge target and making ticket reconciliation optional only when no ticket owns execution. |
| O-006 | Spike read-order wording still treated any repository file mutation as ticket/Ralph-triggering. | Fixed in `skills/loom-spike/SKILL.md` by reusing the narrowed non-record mutation condition. |
| O-007 | Mandatory critique acceptance could be satisfied by chat-only oracle output. | Fixed by requiring and creating a final critique record. |
| O-008 | Ticket lacked standard dependencies and journal sections. | Fixed by adding `# Dependencies` and `# Journal`. |

# Current State

Status rationale:

Closed; all acceptance criteria are satisfied by the scoped diff, structural evidence, and final critique record.

Blockers:

None.

Execution notes:

- Initial review findings were gathered from direct inspection plus oracle/explorer review of the skill corpus.
- Existing untracked `examples/00-todo-app` files are unrelated and will not be modified by this ticket.

Continuation note:

None - ticket is closed. Reopen only if the edited skill-corpus surfaces change again or review identifies a new blocker.

# Evidence

Disposition: sufficient

Records:

- evidence:skill-corpus-fix-structural-checks — supports ticket:pkt7z924#ACC-002 and ticket:pkt7z924#ACC-003.

Gaps / limits:

- Evidence is structural and does not prove future operator behavior.
- Evidence does not validate unrelated untracked `examples/00-todo-app` files.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: The change touches skill-corpus protocol authority and the operator explicitly requested oracle adversarial review.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-clarity

Findings:

- critique:skill-corpus-fix-review#FIND-001 — resolved by status-lifecycle source/target status guard.
- critique:skill-corpus-fix-review#FIND-002 — resolved by narrowed spike main flow, verification, Done Means, and read-order wording.
- critique:skill-corpus-fix-review#FIND-003 — resolved by this ticket's `# Finding Disposition` table.
- critique:skill-corpus-fix-review#FIND-004 — resolved by adding ticket-owned evidence disposition grammar to status lifecycle and tokenizing ticket skill prose.
- critique:skill-corpus-fix-review#FIND-005 — resolved by requiring a critique record in critique packet parent merge scope and making ticket reconciliation optional only when no ticket owns execution.
- critique:skill-corpus-fix-review#FIND-006 — resolved by requiring final critique record preservation for oracle review.
- critique:skill-corpus-fix-review#FIND-007 — resolved by adding dependencies and journal sections.

Promotion disposition: not_required
Promotion / deferral rationale: The reusable learning was incorporated directly into the owning skill/reference/template surfaces touched by this ticket; no separate wiki, research, spec, plan, initiative, constitution, or memory promotion is needed.

Promoted / deferred:

- None - direct owner-surface edits are the promotion.

Wiki disposition: not_required with reason - this ticket repairs existing skill-corpus guidance rather than introducing a reusable explanation that needs a new wiki page.

# Acceptance Decision

Accepted and closed at 2026-05-07T18:45:01Z.

Basis:

- ticket:pkt7z924#ACC-001 satisfied by the `# Finding Disposition` table and changed skill/reference/template files.
- ticket:pkt7z924#ACC-002 supported by evidence:skill-corpus-fix-structural-checks.
- ticket:pkt7z924#ACC-003 satisfied by critique:skill-corpus-fix-review and the ticket-owned resolved dispositions listed above.

Residual risk:

- Markdown guidance cannot mechanically guarantee future operator behavior.
- Unrelated untracked `examples/00-todo-app` files remain outside this ticket's scope.

# Dependencies

Hard prerequisites:

- None - this ticket directly addresses the completed skill-corpus review findings.

Soft links / related work:

- None - related prior protocol-hardening tickets informed the corpus but do not block this bounded fix.

# Journal

- 2026-05-07T18:31:54Z — Created active ticket `ticket:pkt7z924` for the skill-corpus review fixes.
- 2026-05-07T18:36:00Z — Applied initial fixes across packet grammar, status lifecycle, ticket evidence disposition, spike/debugging guidance, critique packet template, drive handoff docs, plan rationalizations, skill-authoring, and bootstrap.
- 2026-05-07T18:39:00Z — Ran structural checks: diff whitespace check passed; frontmatter parsed after allowing YAML timestamps; packet change-class list matched canonical change-class values; targeted contradiction searches passed.
- 2026-05-07T18:41:00Z — Oracle adversarial review found five issues; addressed status transition source/target validity, spike mutation scope, ticket finding recoverability, evidence disposition lifecycle grammar, and critique packet parent merge ambiguity.
- 2026-05-07T18:43:00Z — Second oracle review found three remaining issues; addressed spike read-order wording, mandatory final critique record requirement, and missing ticket dependencies/journal sections.
- 2026-05-07T18:44:00Z — Created evidence:skill-corpus-fix-structural-checks and critique:skill-corpus-fix-review.
- 2026-05-07T18:45:01Z — Reran final scoped checks, updated evidence/critique/ticket reconciliation, and closed the ticket.
