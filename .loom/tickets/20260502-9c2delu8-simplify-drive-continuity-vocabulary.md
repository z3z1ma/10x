---
id: ticket:9c2delu8
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
  - ticket:lqiw3hvp
---

# Summary

Simplify `loom-drive` continuity/checkpoint/tranche vocabulary while preserving
parent-loop autonomy, restart safety, and owner-layer boundaries.

# Context

Council finding `COUNCIL-FIND-011` found overlapping drive terms: continuity
contract, checkpoint, snapshot, tranche contract, gap matrix, route exit, and
resume instruction. Drive is powerful but risks feeling bureaucratic.

# Why Now

After disposition and support artifact grammar are settled, drive can be made
lighter and more operational without weakening safety gates.

# Scope

- Consolidate drive vocabulary around a small canonical continuity/checkpoint
  shape.
- Make advanced tranche/gap guidance conditional rather than always-on.
- Preserve explicit owner-record checkpoint requirements before child launch,
  compaction, or handoff.
- Keep drive coordination from owning project truth.

# Non-goals

- Do not remove drive safety gates.
- Do not create a new drive record kind or ledger.
- Do not rewrite unrelated skills.

# Acceptance Criteria

- ACC-001: Drive references use a smaller, coherent continuity vocabulary.
- ACC-002: Checkpoint/resume safety remains explicit and fail-closed.
- ACC-003: Advanced tranche/gap guidance is clearly conditional.
- ACC-004: Drive still routes durable truth to owner layers and tickets.
- ACC-005: Evidence records term searches, pressure-scenario spot checks, and
  `git diff --check`.
- ACC-006: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-006`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-006` | pending | pending | open |

# Execution Notes

Council affected surfaces include `skills/loom-drive/references/checkpoint-resume-protocol.md`,
`skills/loom-drive/references/continuity-contract.md`, and
`skills/loom-drive/references/tranche-decision-protocol.md`.

# Blockers

Depends on `ticket:3twzep5n` and `ticket:lqiw3hvp` so disposition and support
artifact grammar are settled.

# Next Move / Next Route

Ralph implementation packet after dependencies close.

# Ralph Readiness

Bounded iteration: simplify drive continuity vocabulary without weakening safety.

Write boundary: `skills/loom-drive/**`, this ticket, one evidence record, one
critique record, and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Expected:

- `git diff --check`
- targeted searches for drive vocabulary before/after
- pressure-scenario spot checks for cold resume, blocked critique, next-route
  selection, and child handoff

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: drive coordinates broad autonomous work and checkpoint safety.

Required critique profiles:

- protocol-change
- operator-clarity
- routing-safety

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
- `ticket:lqiw3hvp`

# Journal

- 2026-05-02T15:25:50Z: Created from council finding `COUNCIL-FIND-011`.
