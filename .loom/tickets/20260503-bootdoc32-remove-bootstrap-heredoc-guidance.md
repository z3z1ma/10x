---
id: ticket:bootdoc32
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T18:34:35Z
updated_at: 2026-05-03T18:36:49Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:bootstrap-file-creation-guidance-validation
  critique:
    - critique:bootstrap-file-creation-guidance-review
external_refs: {}
depends_on: []
---

# Summary

Remove the bootstrap here-doc file-creation recipe and make the creation guidance
template-first and method-neutral.

# Context

The user observed that bootstrap guidance was overly prescriptive when it taught a
specific here-doc flow for creating records. The bootstrap should give the model
the owning template and validation expectations, then let the operator choose the
safest creation method for the current harness.

# Why Now

Bootstrap doctrine is the first product-facing operating surface agents read. It
should teach judgment, owner boundaries, and structural expectations without
turning one shell idiom into protocol behavior.

# Scope

- Remove the here-doc record-creation section from
  `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`.
- Replace prescriptive creation options with template-first, method-neutral
  guidance.
- Preserve structural expectations: real frontmatter values, naming/ID rules,
  placeholder removal, owner-layer links, and smallest honest checks.

# Out Of Scope

- Do not change record templates.
- Do not add a file-creation runtime, validator, or command wrapper.
- Do not rewrite historical tickets, evidence, critique, or packets that discuss
  prior here-doc copy-safety work.

# Acceptance Criteria

- ACC-001: Bootstrap filesystem guidance no longer suggests or includes a
  here-doc recipe for creating records.
- ACC-002: Bootstrap record-creation guidance is template-first and leaves the
  concrete file-creation method to operator/model judgment.
- ACC-003: The guidance still requires saved records to be truthful,
  placeholder-free, correctly named, linked to the owner layer, and structurally
  checked before being treated as truth.
- ACC-004: Validation and critique support acceptance.
- ACC-005: The broader authoring lesson is preserved as support recall without
  making memory the product-truth owner.

# Coverage

Covers:

- ticket:bootdoc32#ACC-001
- ticket:bootdoc32#ACC-002
- ticket:bootdoc32#ACC-003
- ticket:bootdoc32#ACC-004
- ticket:bootdoc32#ACC-005

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:bootdoc32#ACC-001 | evidence:bootstrap-file-creation-guidance-validation | critique:bootstrap-file-creation-guidance-review | satisfied |
| ticket:bootdoc32#ACC-002 | evidence:bootstrap-file-creation-guidance-validation | critique:bootstrap-file-creation-guidance-review | satisfied |
| ticket:bootdoc32#ACC-003 | evidence:bootstrap-file-creation-guidance-validation | critique:bootstrap-file-creation-guidance-review | satisfied |
| ticket:bootdoc32#ACC-004 | evidence:bootstrap-file-creation-guidance-validation | critique:bootstrap-file-creation-guidance-review | satisfied |
| ticket:bootdoc32#ACC-005 | evidence:bootstrap-file-creation-guidance-validation | critique:bootstrap-file-creation-guidance-review | satisfied |

# Execution Notes

Implemented as a small local edit to the bootstrap filesystem/tooling reference.
The change removed method-specific record creation mechanics and kept the product
guidance focused on templates, ownership, and validation expectations.

# Blockers

None.

# Next Move / Next Route

Next route: stop

# Route Readiness

Stop readiness:

stop_kind: satisfied

stop_reason: Bootstrap file-creation guidance is template-first,
method-neutral, support recall is updated, validation and critique passed, and
the scoped change is accepted.

owner_record: ticket:bootdoc32

resume_condition: None - work is accepted and closed; reopen only if a new audit
finding or failed validation challenges this acceptance decision.

closure_claim: yes

# Evidence

Evidence status: sufficient for structural acceptance.

Evidence record:

- evidence:bootstrap-file-creation-guidance-validation

# Critique Disposition

Risk class: medium

Critique policy: completed

Policy rationale: the change affects bootstrap operator behavior, but the edit is
small, localized, and removes overly prescriptive mechanics rather than adding a
new protocol gate.

Findings:

None - `critique:bootstrap-file-creation-guidance-review` found no blockers.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- The durable lesson was promoted directly into the owning bootstrap reference:
  `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`.
- A support-only memory cue was added to `.loom/memory/system/patterns.md` so
  future authoring work remembers the broader judgment pattern without making
  memory the product-truth owner.

Deferred / not-required rationale:

No separate wiki, research, spec, plan, initiative, or constitution promotion is
required because the accepted guidance now lives in the product surface that owns
it. Memory was updated only as support recall.

# Wiki Disposition

N/A - no wiki route selected.

# Acceptance Decision

Accepted by: OpenCode
Accepted at: 2026-05-03T18:36:49Z
Basis: `evidence:bootstrap-file-creation-guidance-validation` and
`critique:bootstrap-file-creation-guidance-review` support all acceptance
criteria, and no blockers remain.
Residual risks: Historical Loom records still discuss prior here-doc work as
history. They were intentionally left unchanged because this ticket changes the
product bootstrap surface, not historical provenance.

# Dependencies

None.

# Journal

- 2026-05-03T18:34:35Z: Removed the bootstrap here-doc record creation recipe
  and recorded evidence and critique.
- 2026-05-03T18:35:52Z: Validated the changed reference and new records.
- 2026-05-03T18:36:49Z: Added support recall for the broader authoring pattern,
  reconciled acceptance, and closed the ticket.
