---
id: ticket:u02z7o9j
kind: ticket
status: ready
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T15:25:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
external_refs: {}
depends_on:
  - ticket:3twzep5n
---

# Summary

Clarify ticket-local `ACC-*` acceptance IDs and make ticket readiness route-neutral
instead of Ralph-biased.

# Context

Council findings `COUNCIL-FIND-007` and `COUNCIL-FIND-008` found that ticket-local
acceptance criteria are allowed but not clearly ID-shaped, and the ticket template
uses `# Ralph Readiness` even when critique/wiki packet handoffs are sibling
routes.

# Why Now

Ticket templates are copied frequently. Ambiguous acceptance IDs and Ralph-biased
readiness headings train fresh agents to guess or misroute bounded work.

# Scope

- Clarify whether and how ticket-local `ACC-*` IDs should be written and cited.
- Align claim coverage references for `ticket:<token>#ACC-001` if selected.
- Rename or reshape ticket readiness heading to cover local edit, Ralph,
  critique, wiki, evidence, and acceptance routes without blurring Ralph.
- Update relevant ticket readiness guidance and examples.

# Non-goals

- Do not change spec-owned acceptance contract grammar except to distinguish it
  from ticket-local criteria.
- Do not remove Ralph-specific requirements from Ralph packet guidance.

# Acceptance Criteria

- ACC-001: Ticket-local acceptance criteria have explicit ID/reference guidance.
- ACC-002: Ticket template readiness is route-neutral and does not imply all
  packetized work is Ralph.
- ACC-003: Claim coverage references and ticket guidance agree.
- ACC-004: Evidence records before/after searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-005` | pending | pending | open |

# Execution Notes

Council affected surfaces include `skills/loom-tickets/templates/ticket.md`,
`skills/loom-records/references/claim-coverage.md`, `skills/loom-tickets/SKILL.md`,
and `skills/loom-tickets/references/readiness.md`.

# Blockers

Depends on `ticket:3twzep5n` so critique disposition wording is settled.

# Next Move / Next Route

Ralph implementation packet after dependency closes.

# Ralph Readiness

Bounded iteration: clarify ticket-local acceptance IDs and route-neutral ticket
readiness.

Write boundary: `skills/loom-tickets/**`, `skills/loom-records/**`, this ticket,
one evidence record, one critique record, and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Expected:

- `git diff --check`
- targeted searches for `Ralph Readiness`, `Handoff Readiness`, `ACC-*`, and
  `ticket:<token>#ACC-001`
- manual comparison against claim coverage and ticket readiness guidance

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique for every ticket; ticket template
changes affect operator routing.

Required critique profiles:

- records-grammar
- operator-clarity
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is required by user instruction.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

- `ticket:3twzep5n`

# Journal

- 2026-05-02T15:25:50Z: Created from council findings `COUNCIL-FIND-007` and
  `COUNCIL-FIND-008`.
