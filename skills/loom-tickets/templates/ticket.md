---
id: ticket:<token>
kind: ticket
status: proposed
change_class: "<TBD: choose one change class before saving>"
risk_class: "<TBD: choose low, medium, or high before saving>"
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
links: {}
external_refs: {}
depends_on: []
---

# Summary

What this bounded work item is.

Save-ready rule: replace every placeholder before saving. Remove the unused
acceptance owner branch; do not remove evidence, critique, retrospective /
promotion, acceptance, or closure gates just because they are pending.

# Context

Relevant upstream context and why this exists.

# Why Now

Why this deserves attention in the current phase.

# Scope

What belongs inside this ticket.

# Out Of Scope

What should not happen inside this ticket.

# Acceptance Criteria

What must be true for this ticket to be accepted.

Choose exactly one acceptance owner branch before saving. Remove the branch that
does not apply.

Spec-owned acceptance branch:

Use this branch when a spec owns the reusable acceptance contract. Do not create
ticket-local `ACC-*` criteria here. Summarize only the ticket-scoped work here
and cite the spec-owned acceptance IDs under `# Coverage`.

Ticket-local acceptance branch:

If no spec owns the acceptance contract, this ticket may own ticket-local
acceptance criteria. Write stable local IDs so evidence and critique can cite
them. Replace these example criteria before saving:

- ACC-001: <TBD: write the first ticket-local acceptance criterion>
- ACC-002: <TBD: write the second ticket-local acceptance criterion, or remove>

# Coverage

Covers:

List qualified claim or acceptance IDs. If none apply, write `None - reason`.

- Use `spec:<slug>#ACC-001` for spec-owned acceptance.
- Use `ticket:<token>#ACC-001` for ticket-local acceptance criteria owned in
  this ticket.
- Use `initiative:<slug>#OBJ-001` for initiative objectives this ticket advances.

# Claim Matrix

Use only real claim, evidence, and critique references. Remove this table or
write `None - reason` when no claim matrix applies yet.
Use the canonical status vocabulary from
`skills/loom-records/references/claim-coverage.md`: `open`, `supported`,
`supported_pending_review`, `challenged`, `accepted_risk`, or `superseded`.

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |

# Execution Notes

Useful implementation notes, but not a transcript dump.

# Blockers

Named blockers only. If none exist, write `None`.

# Evidence

What evidence exists or is expected.

- Link evidence records by stable ID.
- State which acceptance or claim IDs each record supports or challenges.
- Note whether evidence is fresh enough for the current source, record,
  dependency, and environment state.
- Summarize material limitations without turning the ticket into the raw evidence
  store.
- Remember: evidence feeds the ticket-owned acceptance gate; evidence does not
  close the ticket by itself.

# Critique Disposition

Risk class: <TBD: repeat frontmatter risk_class>

Must match frontmatter `risk_class`. The frontmatter field is the ticket's
canonical risk classification; this section restates that risk only to explain
the critique policy and acceptance disposition. If the two differ, reconcile the
ticket before readiness, critique planning, or closure.

Critique policy: <TBD: choose optional, recommended, or mandatory>

Policy rationale:

Required critique profiles:

List profile names, or write `None - reason`.

Findings:

List real finding references and ticket-owned finding dispositions, or write
`None - no critique yet`.

Example:

- `critique:example-review#FIND-001` — `resolved` by <evidence or change ref>
- `critique:example-review#FIND-002` — `accepted_risk`; rationale and acceptance
  provenance recorded in `# Acceptance Decision`
- `critique:example-review#FIND-003` — `superseded` by <evidence ref>
- `critique:example-review#FIND-004` — `converted_to_follow_up` as
  `ticket:<token>`

Open medium/high findings must have ticket-owned dispositions of `resolved`,
`accepted_risk`, `superseded`, or `converted_to_follow_up` before closure, with
evidence, acceptance provenance, or linked follow-up tickets as appropriate.
Withdrawn findings require critique rationale and may be cited for audit history
without ticket-owned finding disposition.

Disposition status: <TBD: choose pending, blocking, completed, deferred, or not_required>

Use `blocking` only when unresolved required critique currently blocks acceptance
or dependent continuation. This status is a ticket-owned gate summary, not a
critique verdict.

Mandatory critique fail-closed rule:

- If critique policy is `mandatory`, keep this disposition `pending` until a
  final, non-draft/stub required critique exists.
- If mandatory critique exists but has unresolved blocking issues, use
  `blocking`.
- If open medium/high findings are missing ticket-owned dispositions, use
  `blocking` until the ticket records `resolved`, `accepted_risk`, `superseded`,
  or `converted_to_follow_up` with the needed evidence, acceptance provenance,
  or linked follow-up ticket.
- `deferred` and `not_required` are closure-compatible only for recommended or
  optional critique with rationale; do not use them to satisfy mandatory
  critique.
- Critique owns finding state and verdict. The ticket owns how findings affect
  closure.

Deferral / not-required rationale:

# Retrospective / Promotion Disposition

Ticket-owned closure summary for durable learning and follow-through across all
promotion paths. This section does not create a retrospective record kind or
make retrospective replace acceptance; it tells acceptance review whether
compounding work is resolved for this ticket.

Disposition status: <TBD: choose pending, blocking, completed, deferred, or not_required>

- Use `pending` while implementation, critique, or acceptance review has not yet
  determined the retrospective need.
- Use `blocking` when closure would be unsafe because required promotion or
  prevention follow-through is incomplete.
- Use `completed` when durable lessons were promoted into their existing owner
  layers, or the retrospective pass completed and found no open follow-through.
- Use `deferred` when promotion or prevention is intentionally moved to linked
  follow-up work before closure.
- Use `not_required` when the ticket has no durable lesson to promote.

Promoted:

List owner-record updates, or write `None - reason`.

Deferred / not-required rationale:

# Wiki Disposition

Wiki outcome when accepted explanation is one selected promotion path. Write
`N/A - no wiki promotion needed` when the broader retrospective / promotion
disposition sends learning elsewhere or finds no durable wiki-worthy explanation.

# Acceptance Decision

Required when the workspace, team, accepted risk, or operator asks for explicit
acceptance provenance.

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

Human-readable notes for important dependencies beyond `depends_on`.

# Journal

Chronological updates that matter later.
