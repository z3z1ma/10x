---
id: ticket:329erym3
kind: ticket
status: complete_pending_acceptance
change_class: protocol-authority
risk_class: medium
created_at: 2026-04-30T08:22:13Z
updated_at: 2026-04-30T08:31:09Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:sharpen-memory-support-layer
  specs:
    - spec:memory-support-layer-contract
  evidence:
    - evidence:memory-support-layer-validation
  critique:
    - critique:memory-support-layer-review
external_refs: {}
depends_on: []
---

# Summary

Sharpen Loom's memory support layer so agents can tell why memory exists, when to
use it, how it differs from canonical owner layers, and when to promote or prune
memory content.

# Context

The user identified that `loom-memory` is much vaguer than Loom's canonical
layers. The current skill protects against shadow truth but does not sufficiently
teach memory's positive role or practical routing boundaries.

# Why Now

As `loom-drive` and other owner-layer workflows become more concrete, memory's
weak definition creates a usability gap: agents can avoid memory, misuse it as a
scratchpad, or accidentally let it duplicate ticket/wiki/evidence truth.

# Scope

- Update `skills/loom-memory/SKILL.md`.
- Update `skills/loom-memory/references/memory-model.md`.
- Update `skills/loom-memory/references/retrieval.md`.
- Update `skills/loom-memory/references/housekeeping.md`.
- Update `skills/loom-memory/templates/*.md` where small template notes keep the
  memory shapes aligned with the new contract.
- Make targeted alignment edits to product summary surfaces that define memory's
  layer role.
- Record structural validation evidence and critique disposition.

# Non-goals

- Do not add a memory runtime, hidden index, embeddings, database, CLI, or daemon.
- Do not make memory canonical project truth.
- Do not create broad examples unless the first tranche proves they are needed.
- Do not rewrite historical dogfood memory records beyond direct support for this
  ticket.

# Acceptance Criteria

- `spec:memory-support-layer-contract#ACC-001`
- `spec:memory-support-layer-contract#ACC-002`
- `spec:memory-support-layer-contract#ACC-003`
- `spec:memory-support-layer-contract#ACC-004`
- `spec:memory-support-layer-contract#ACC-005`
- `spec:memory-support-layer-contract#ACC-006`

# Coverage

Covers:

- `spec:memory-support-layer-contract#ACC-001`
- `spec:memory-support-layer-contract#ACC-002`
- `spec:memory-support-layer-contract#ACC-003`
- `spec:memory-support-layer-contract#ACC-004`
- `spec:memory-support-layer-contract#ACC-005`
- `spec:memory-support-layer-contract#ACC-006`
- `initiative:sharpen-memory-support-layer` OBJ-001
- `initiative:sharpen-memory-support-layer` OBJ-002
- `initiative:sharpen-memory-support-layer` OBJ-003
- `initiative:sharpen-memory-support-layer` OBJ-004

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `spec:memory-support-layer-contract#ACC-001` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review` | supported |
| `spec:memory-support-layer-contract#ACC-002` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review` | supported |
| `spec:memory-support-layer-contract#ACC-003` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review` | supported |
| `spec:memory-support-layer-contract#ACC-004` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review` | supported |
| `spec:memory-support-layer-contract#ACC-005` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review#FIND-001 resolved` | supported |
| `spec:memory-support-layer-contract#ACC-006` | `evidence:memory-support-layer-validation` | `critique:memory-support-layer-review#FIND-001 resolved` | supported |

# Execution Notes

Use a local edit rather than Ralph for the first tranche. The scope is a bounded
Markdown protocol edit, the write boundary is explicit, and the current parent
has already read the governing records and memory surface.

# Blockers

None.

# Next Move / Next Route

Ticket acceptance review.

# Ralph Readiness

None - local edit is the selected route for this bounded tranche.

# Evidence

Recorded:

- `evidence:memory-support-layer-validation` records `git diff --check`, targeted
  grep checks, and diff-shape validation for this tranche.

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

This changes protocol guidance and layer-boundary interpretation, but the first
tranche stays within the existing memory support layer and does not alter
canonical truth ownership.

Required critique profiles:

- protocol-change
- operator-clarity

Findings:

`critique:memory-support-layer-review#FIND-001` was medium severity and resolved.

Disposition status: completed

Deferral / not-required rationale:

None.

# Wiki Disposition

Deferred for this tranche. The product source owns the memory behavior contract;
a later wiki page or example may be useful if operators repeatedly need a longer
explanation.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

Depends on `spec:memory-support-layer-contract`, created with this ticket to own
the intended behavior.

# Journal

- 2026-04-30T08:22:13Z: Created by `loom-drive` from the user's high-level
  objective to sharpen memory's interpretation, usefulness, and boundaries.
- 2026-04-30T08:26:34Z: Completed the local edit pass and recorded
  `evidence:memory-support-layer-validation`; recommended critique is the next
  route before acceptance.
- 2026-04-30T08:31:09Z: Ran recommended critique. Resolved
  `critique:memory-support-layer-review#FIND-001` by correcting
  `skills/loom-drive/SKILL.md` so memory is support recall rather than project
  truth. Moved ticket to `complete_pending_acceptance`.
