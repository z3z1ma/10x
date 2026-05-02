---
id: ticket:lqiw3hvp
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
  - ticket:4ilnwsnl
---

# Summary

Resolve support artifact grammar for drive outer-loop handoffs and workspace
harness support records so they cannot be mistaken for canonical project truth.

# Context

Council findings `COUNCIL-FIND-004` and `COUNCIL-FIND-006` identified support
artifacts with frontmatter/status but unclear path, ID, kind, and lifecycle
grammar.

# Why Now

Support artifacts are useful only if their boundaries are crisp. If drive
handoffs or workspace harness records look like new ledgers, they undermine
Loom's owner-layer model.

# Scope

- Decide and document whether drive outer-loop handoffs are transient prompt
  material or durable support artifacts.
- Align any durable support artifact path/kind/status grammar with
  `loom-records`.
- Fix workspace harness support record naming/kind grammar or template shape.
- Preserve non-canonical support status: no support artifact may own objective,
  ticket, acceptance, evidence, critique, or packet lifecycle truth.

# Non-goals

- Do not add a new canonical owner layer.
- Do not add runtime support records beyond documented support grammar.
- Do not simplify all `loom-drive` vocabulary; ticket `9c2delu8` owns that pass.

# Acceptance Criteria

- ACC-001: Drive outer-loop handoff grammar explicitly states transient vs
  durable support behavior and path/kind/status expectations if saved.
- ACC-002: Workspace harness support record template and naming/status grammar
  agree.
- ACC-003: Support artifacts are explicitly non-canonical and cannot own live
  execution, acceptance, objective, evidence, critique, or packet lifecycle truth.
- ACC-004: Evidence records targeted searches for support artifact kinds/statuses
  and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-003`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-003` | pending | pending | open |

# Execution Notes

Council affected surfaces include `skills/loom-drive/templates/outer-loop-handoff.md`,
`skills/loom-drive/SKILL.md`, `skills/loom-records/references/frontmatter.md`,
`skills/loom-records/references/status-lifecycle.md`,
`skills/loom-workspace/templates/harness.md`, and
`skills/loom-records/references/naming-and-ids.md`.

# Blockers

Depends on `ticket:4ilnwsnl` so packet/support grammar boundaries are settled.

# Next Move / Next Route

Ralph implementation packet after dependency closes.

# Ralph Readiness

Bounded iteration: resolve drive handoff and workspace support artifact grammar.

Write boundary: `skills/loom-drive/**`, `skills/loom-workspace/**`,
`skills/loom-records/**`, this ticket, one evidence record, one critique record,
and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Expected:

- `git diff --check`
- targeted searches for `workspace-support`, `outer-loop-handoff`, handoff
  status fields, and support artifact path/kind references
- manual comparison of templates against naming/frontmatter/status references

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: support artifact grammar can create shadow-ledger confusion.

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

- `ticket:4ilnwsnl`

# Journal

- 2026-05-02T15:25:50Z: Created from council findings `COUNCIL-FIND-004` and
  `COUNCIL-FIND-006`.
