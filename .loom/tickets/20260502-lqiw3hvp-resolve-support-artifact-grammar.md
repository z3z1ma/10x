---
id: ticket:lqiw3hvp
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T16:35:43Z
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
    - packet:ralph-ticket-lqiw3hvp-20260502T161552Z
    - packet:ralph-ticket-lqiw3hvp-20260502T162727Z
  evidence:
    - evidence:support-artifact-grammar-validation
  critique:
    - critique:support-artifact-grammar-review
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
| `initiative:skills-corpus-perfection-council-followup#OBJ-003` | `evidence:support-artifact-grammar-validation` | `critique:support-artifact-grammar-review` with all findings resolved | supported |

# Execution Notes

Council affected surfaces include `skills/loom-drive/templates/outer-loop-handoff.md`,
`skills/loom-drive/SKILL.md`, `skills/loom-records/references/frontmatter.md`,
`skills/loom-records/references/status-lifecycle.md`,
`skills/loom-workspace/templates/harness.md`, and
`skills/loom-records/references/naming-and-ids.md`.

Implementation decision: drive outer-loop handoffs are prompt-only by default.
When saved, they are durable support artifacts under
`.loom/support/drive-handoffs/` with support-local ID/kind/status grammar, not a
packet family and not canonical truth owners. Workspace harness records use
`kind: workspace-support` with support-local `active | superseded | retired`
status for transport documentation only.

First oracle critique found two required repairs: separate canonical owner-record
ID grammar from packet/support-local ID grammar, and explicitly include objective
state in the workspace harness non-owner warning.

Second repair iteration separated canonical owner-record ID families from stable
support and packet ID families, removed the misleading frontmatter canonical-owner
table reference, and normalized workspace harness non-owner wording to include
objective state and the full support boundary.

# Blockers

None. Dependency `ticket:4ilnwsnl` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:yk89awl5`.

# Ralph Readiness

Bounded iteration: resolve drive handoff and workspace support artifact grammar.

Write boundary: `skills/loom-drive/**`, `skills/loom-workspace/**`,
`skills/loom-records/**`, this ticket, one evidence record, one critique record,
and the Ralph packet.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, and retrospective disposition.

# Evidence

Recorded:

- `evidence:support-artifact-grammar-validation` records `git diff --check`,
  targeted searches for support artifact grammar and oracle-repair terms, and
  manual comparison of drive handoff and workspace harness templates against
  naming/frontmatter/status references.

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

Recorded in `critique:support-artifact-grammar-review`:

- `critique:support-artifact-grammar-review#ORACLE-LQIW3HVP-001` - resolved.
- `critique:support-artifact-grammar-review#ORACLE-LQIW3HVP-002` - resolved.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no remaining findings.

# Wiki Disposition

Retrospective disposition complete. Durable lessons were promoted directly into
the owner product surfaces: support/packet ID taxonomy,
support-artifact frontmatter guidance, support-local status lifecycle boundaries,
workspace harness template wording, and drive handoff support grammar. No separate
wiki page, research record, spec, constitution decision, or memory entry is needed
for this ticket.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T16:35:43Z
Basis: Ralph packets `packet:ralph-ticket-lqiw3hvp-20260502T161552Z` and
`packet:ralph-ticket-lqiw3hvp-20260502T162727Z`; evidence
`evidence:support-artifact-grammar-validation`; final oracle critique
`critique:support-artifact-grammar-review` with no remaining findings.
Residual risks: validation and critique were structural/textual; future operator
application is not proven beyond corpus consistency.

# Dependencies

- `ticket:4ilnwsnl`

# Journal

- 2026-05-02T15:25:50Z: Created from council findings `COUNCIL-FIND-004` and
  `COUNCIL-FIND-006`.
- 2026-05-02T16:15:52Z: Dependency `ticket:4ilnwsnl` closed. Moved to active
  and compiled Ralph packet `packet:ralph-ticket-lqiw3hvp-20260502T161552Z` from
  commit `6f7be0b053ccc73bcbc3de9b8dee7776b3dabb38`.
- 2026-05-02T16:19:42Z: Implemented support artifact grammar alignment, recorded
  `evidence:support-artifact-grammar-validation`, and moved to `review_required`
  for mandatory oracle critique.
- 2026-05-02T16:27:27Z: Oracle critique found two blocking issues. Recorded
  `critique:support-artifact-grammar-review`, moved back to active, and compiled
  repair packet `packet:ralph-ticket-lqiw3hvp-20260502T162727Z`.
- 2026-05-02T16:31:46Z: Applied second-iteration repair for both oracle findings,
  refreshed `evidence:support-artifact-grammar-validation`, and returned ticket to
  `review_required` for oracle re-check.
- 2026-05-02T16:35:43Z: Oracle re-check passed with both findings resolved and no
  new findings. Recorded final critique, retrospective disposition, and acceptance;
  closed ticket.
