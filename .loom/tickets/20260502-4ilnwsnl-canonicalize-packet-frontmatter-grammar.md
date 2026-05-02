---
id: ticket:4ilnwsnl
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
depends_on:
  - ticket:3twzep5n
---

# Summary

Create one canonical shared packet-frontmatter grammar and align Ralph,
critique, and wiki packet templates/references to it.

# Context

Council finding `COUNCIL-FIND-002` found packet grammar spread across
`loom-records`, `loom-ralph`, `loom-critique`, and `loom-wiki`. Packet drift is
high leverage because packets are copied into fresh-context work.

# Why Now

Every implementation ticket in this pass uses Ralph. Future fresh workers need a
single reliable place to understand packet-family fields, valid values, write
scope, parent merge scope, source fingerprint, and verification posture.

# Scope

- Add or update a canonical `loom-records` packet frontmatter reference.
- Align `loom-ralph` packet-contract guidance to cite the shared grammar without
  duplicating ownership.
- Align Ralph, critique, and wiki packet templates with the canonical field set.
- Clarify packet-family differences and valid values where practical.

# Non-goals

- Do not turn packets into canonical truth owners.
- Do not add runtime validation tooling.
- Do not rewrite all packet prose outside the frontmatter contract boundary.

# Acceptance Criteria

- ACC-001: A shared packet-frontmatter reference exists in `loom-records` or an
  equally appropriate shared grammar surface.
- ACC-002: Ralph, critique, and wiki packet templates align with the shared
  grammar.
- ACC-003: References explain packet-family differences without making critique
  or wiki packets Ralph-governed.
- ACC-004: Evidence records template/reference comparison and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-002`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-002` | pending | pending | open |

# Execution Notes

Council affected surfaces include `skills/loom-records/references/frontmatter.md`,
`skills/loom-ralph/references/packet-contract.md`,
`skills/loom-ralph/templates/ralph-packet.md`,
`skills/loom-critique/templates/critique-packet.md`, and
`skills/loom-wiki/templates/wiki-packet.md`.

# Blockers

Depends on `ticket:3twzep5n` so disposition vocabulary is stable first.

# Next Move / Next Route

Ralph implementation packet after dependency closes.

# Ralph Readiness

Bounded iteration: canonicalize packet frontmatter grammar and align packet
templates/references.

Write boundary: `skills/loom-records/**`, `skills/loom-ralph/**`,
`skills/loom-critique/**`, `skills/loom-wiki/**`, this ticket, one evidence
record, one critique record, and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Expected:

- `git diff --check`
- targeted searches for packet frontmatter fields and packet templates
- manual comparison of templates against shared grammar

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: packet grammar affects fresh-context authority and write-scope
safety.

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

- `ticket:3twzep5n`

# Journal

- 2026-05-02T15:25:50Z: Created from council finding `COUNCIL-FIND-002`.
