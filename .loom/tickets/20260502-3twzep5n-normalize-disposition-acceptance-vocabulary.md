---
id: ticket:3twzep5n
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T15:56:59Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
  packet:
    - packet:ralph-ticket-3twzep5n-20260502T153040Z
    - packet:ralph-ticket-3twzep5n-20260502T154425Z
    - packet:ralph-ticket-3twzep5n-20260502T155314Z
  evidence:
    - evidence:disposition-acceptance-vocabulary-validation
  critique:
    - critique:disposition-acceptance-vocabulary-review
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
| `initiative:skills-corpus-perfection-council-followup#OBJ-001` | `evidence:disposition-acceptance-vocabulary-validation` | `critique:disposition-acceptance-vocabulary-review` with all findings resolved | supported |

# Execution Notes

Council affected surfaces include `skills/loom-tickets/templates/ticket.md`,
`skills/loom-tickets/references/acceptance-gate.md`,
`skills/loom-critique/templates/critique.md`,
`skills/loom-critique/references/finding-format.md`, and
`skills/loom-drive/references/continuity-contract.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Continue to `ticket:4ilnwsnl`.

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

- `evidence:disposition-acceptance-vocabulary-validation` records structural
  validation, targeted disposition vocabulary searches, manual comparison against
  bootstrap closure doctrine and ticket acceptance gate, and `git diff --check`.

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

Recorded in `critique:disposition-acceptance-vocabulary-review`:

- `critique:disposition-acceptance-vocabulary-review#ORACLE-3TWZEP5N-001` - resolved.
- `critique:disposition-acceptance-vocabulary-review#ORACLE-3TWZEP5N-002` - resolved.
- `critique:disposition-acceptance-vocabulary-review#ORACLE-3TWZEP5N-003` - resolved.
- `critique:disposition-acceptance-vocabulary-review#ORACLE-3TWZEP5N-004` - resolved.
- `critique:disposition-acceptance-vocabulary-review#ORACLE-3TWZEP5N-RC-001` - resolved.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no remaining findings.

# Wiki Disposition

Retrospective disposition complete. Durable lessons were promoted directly into
the owner product surfaces: shared lifecycle grammar, ticket acceptance gate,
critique finding format/template, drive stop/checkpoint wording, semantic link
usage, and bootstrap closure doctrine. No separate wiki page, research record,
spec, constitution decision, or memory entry is needed for this ticket.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T15:56:59Z
Basis: Ralph packets `packet:ralph-ticket-3twzep5n-20260502T153040Z`,
`packet:ralph-ticket-3twzep5n-20260502T154425Z`, and
`packet:ralph-ticket-3twzep5n-20260502T155314Z`; evidence
`evidence:disposition-acceptance-vocabulary-validation`; final oracle critique
`critique:disposition-acceptance-vocabulary-review` with no remaining findings.
Residual risks: validation and critique were structural/textual; future operator
application is not proven beyond corpus consistency.

# Dependencies

None.

# Journal

- 2026-05-02T15:25:50Z: Created from council finding `COUNCIL-FIND-001`.
- 2026-05-02T15:30:39Z: Moved to active and compiled Ralph packet
  `packet:ralph-ticket-3twzep5n-20260502T153040Z` from commit
  `4e17691f7cacf2792a61ee2ed5aff6159effcf93`.
- 2026-05-02T15:36:04Z: Ralph child implementation normalized the shared,
  ticket, critique, drive, and bootstrap vocabulary surfaces; recorded structural
  evidence in `evidence:disposition-acceptance-vocabulary-validation`; moved to
  `review_required` because mandatory oracle critique remains pending.
- 2026-05-02T15:44:25Z: Oracle critique found medium issues in withdrawn-finding
  closure semantics, stale semantic-link wording, and packet lifecycle
  reconciliation. Parent consumed the first packet and moved ticket back to
  active for Ralph repair packet `packet:ralph-ticket-3twzep5n-20260502T154425Z`.
- 2026-05-02T15:45:34Z: Ralph child repair made the withdrawn-finding closure
  rule explicit, replaced stale semantic-link wording, added `blocking` to the
  ticket template disposition status grammar, refreshed validation evidence, and
  moved the ticket to `review_required` for mandatory oracle re-check.
- 2026-05-02T15:53:13Z: Oracle re-check passed all medium/high findings but
  reported one low drive wording issue. Moved back to active for narrow Ralph
  repair packet `packet:ralph-ticket-3twzep5n-20260502T155314Z`.
- 2026-05-02T15:54:03Z: Narrow Ralph repair updated the drive stop condition so
  only open or unresolved medium/high critique findings lacking ticket-owned
  dispositions stop the drive, refreshed validation evidence, and moved the
  ticket back to `review_required` for mandatory oracle re-check.
- 2026-05-02T15:56:59Z: Final oracle re-check passed with no remaining findings;
  ticket accepted and closed after retrospective disposition was recorded.
