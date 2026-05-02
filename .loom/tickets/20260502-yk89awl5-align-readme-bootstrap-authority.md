---
id: ticket:yk89awl5
kind: ticket
status: ready
change_class: documentation-explanation
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
  - ticket:4ilnwsnl
  - ticket:lqiw3hvp
---

# Summary

Align README public framing with bootstrap authority around workflow skills,
packets, ledgers, and bounded implementation routing.

# Context

Council finding `COUNCIL-FIND-003` found README wording looser than bootstrap.
The README should not imply workflow skills can casually create ledgers or that a
packet itself is the route owner for bounded implementation.

# Why Now

README is the public entry point. If it is less strict than bootstrap, fresh
operators can learn the wrong mental model before the mandatory doctrine loads.

# Scope

- Replace README wording that says workflow skills do not create ledgers unless a
  new kind of work needs a durable place.
- Route bounded implementation through `loom-ralph` with a Ralph packet rather
  than `packet` as if packet were a route owner.
- Keep the README readable and compelling while matching bootstrap authority.

# Non-goals

- Do not rewrite README wholesale.
- Do not change bootstrap unless the prior tickets reveal a necessary exact
  wording alignment.
- Do not change product architecture or install guidance.

# Acceptance Criteria

- ACC-001: README states workflow skills coordinate routes through existing owner
  layers and do not create ledgers.
- ACC-002: README route table sends bounded implementation to Ralph with a Ralph
  packet.
- ACC-003: README remains consistent with bootstrap authority and packet sibling
  grammar.
- ACC-004: Evidence records README/bootstrap comparison and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-004`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-004` | pending | pending | open |

# Execution Notes

Council affected README lines were around the route table and workflow section.
Use current line numbers, not stale council line numbers, during implementation.

# Blockers

Depends on `ticket:3twzep5n`, `ticket:4ilnwsnl`, and `ticket:lqiw3hvp` so public
framing inherits settled grammar.

# Next Move / Next Route

Ralph implementation packet after dependencies close.

# Ralph Readiness

Bounded iteration: align README public framing with bootstrap authority.

Write boundary: `README.md`, possibly targeted bootstrap references only if
needed for exact alignment, this ticket, one evidence record, one critique
record, and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Expected:

- `git diff --check`
- targeted search for route table row and workflow-ledger wording
- manual comparison against bootstrap `truth-and-authority` and Ralph packet
  sibling doctrine

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique for every ticket; README public
framing shapes operator behavior.

Required critique profiles:

- operator-clarity
- routing-safety
- protocol-change

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
- `ticket:4ilnwsnl`
- `ticket:lqiw3hvp`

# Journal

- 2026-05-02T15:25:50Z: Created from council finding `COUNCIL-FIND-003`.
