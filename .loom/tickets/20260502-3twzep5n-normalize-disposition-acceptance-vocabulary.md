---
id: ticket:3twzep5n
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
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
depends_on: []
---

# Summary

Normalize the vocabulary split between critique-owned finding state,
ticket-owned critique disposition, and drive continuity summaries.

# Context

Council finding `COUNCIL-FIND-001` identified overlapping disposition terms in
`loom-tickets`, `loom-critique`, and `loom-drive`. The risk is that critique or
drive support snapshots can appear to own acceptance state that belongs only to
tickets.

# Why Now

Every later ticket in this plan depends on clear acceptance and critique
vocabulary. Closure grammar must fail closed before packet, support artifact,
README, ticket, and drive surfaces are refined.

# Scope

- Define a clear shared vocabulary for critique finding states and ticket critique
  disposition.
- Align `skills/loom-tickets` acceptance gate, ticket template, and examples.
- Align `skills/loom-critique` finding format/template wording.
- Align `skills/loom-drive` continuity/checkpoint wording so it reports ticket
  truth rather than owning acceptance.
- Preserve bootstrap consistency if downstream wording would otherwise conflict.

# Non-goals

- Do not create a new record kind or canonical layer.
- Do not change ticket state-machine statuses except where wording references
  critique disposition.
- Do not rewrite unrelated drive vocabulary; ticket `9c2delu8` owns the drive
  simplification pass.

# Acceptance Criteria

- ACC-001: `loom-records` or the owning shared grammar surface defines the split
  between finding state and ticket critique disposition.
- ACC-002: `loom-tickets` and `loom-critique` use compatible terms and examples.
- ACC-003: `loom-drive` describes critique/acceptance status as a cited ticket
  summary, not as drive-owned closure truth.
- ACC-004: Bootstrap closure doctrine remains consistent with the normalized
  vocabulary.
- ACC-005: Evidence records before/after terminology checks and `git diff --check`.
- ACC-006: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-001`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-001` | pending | pending | open |

# Execution Notes

Council affected surfaces include `skills/loom-tickets/templates/ticket.md`,
`skills/loom-tickets/references/acceptance-gate.md`,
`skills/loom-critique/templates/critique.md`,
`skills/loom-critique/references/finding-format.md`, and
`skills/loom-drive/references/continuity-contract.md`.

# Blockers

None.

# Next Move / Next Route

Ralph implementation packet.

# Ralph Readiness

Bounded iteration: normalize disposition vocabulary across the named shared
grammar, ticket, critique, and drive surfaces.

Write boundary: `skills/loom-records/**`, `skills/loom-tickets/**`,
`skills/loom-critique/**`, `skills/loom-drive/**`, this ticket, one evidence
record, one critique record, and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and any required retrospective promotion.

# Evidence

Expected:

- `git diff --check`
- targeted searches for disposition terms before/after
- manual comparison against bootstrap closure doctrine and ticket acceptance gate

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: disposition vocabulary affects closure safety and protocol
authority.

Required critique profiles:

- protocol-change
- records-grammar
- routing-safety
- operator-clarity

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is mandatory.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

None.

# Journal

- 2026-05-02T15:25:50Z: Created from council finding `COUNCIL-FIND-001`.
