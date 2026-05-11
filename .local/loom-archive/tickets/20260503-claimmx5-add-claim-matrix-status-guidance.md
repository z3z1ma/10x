---
id: ticket:claimmx5
kind: ticket
status: closed
change_class: protocol-authority
risk_class: low
created_at: 2026-05-03T00:56:36Z
updated_at: 2026-05-03T02:17:18Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  plan:
    - plan:skills-corpus-residual-protocol-sharpening-pass
  research:
    - research:skills-corpus-residual-audit-synthesis
  packet:
    - packet:ralph-ticket-claimmx5-20260503T021312Z
  evidence:
    - evidence:claim-matrix-status-guidance-validation
  critique:
    - critique:claim-matrix-status-guidance-review
external_refs: {}
depends_on: []
---

# Summary

Add local claim matrix status guidance to ticket template copy surfaces.

# Context

Council finding `NC2-005` found that the ticket template's claim matrix leaves the
`Status` column unconstrained locally, inviting invented values such as `done` or
`passed`.

# Why Now

The canonical claim matrix vocabulary exists in claim coverage, but agents copying
the ticket template should see the allowed values at the point of edit.

# Scope

- Add a concise pointer in the ticket template to canonical claim matrix status
  values.
- Keep the canonical vocabulary owned by `skills/loom-records/references/claim-coverage.md`.
- Avoid duplicating long claim-coverage doctrine in the ticket template.

# Out Of Scope

- Do not change claim coverage status meanings.
- Do not add runtime validation.

# Acceptance Criteria

- ACC-001: Ticket template names or points to allowed claim matrix statuses:
  `open`, `supported`, `supported_pending_review`, `challenged`,
  `accepted_risk`, and `superseded`.
- ACC-002: Template still allows removing the matrix or writing `None - reason`
  when no matrix applies.
- ACC-003: Claim coverage remains the canonical vocabulary owner.
- ACC-004: Evidence records before/after claim matrix searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-007`
- `ticket:claimmx5#ACC-001`
- `ticket:claimmx5#ACC-002`
- `ticket:claimmx5#ACC-003`
- `ticket:claimmx5#ACC-004`
- `ticket:claimmx5#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-007` | `evidence:claim-matrix-status-guidance-validation` | `critique:claim-matrix-status-guidance-review` | supported |
| `ticket:claimmx5#ACC-001` through `ticket:claimmx5#ACC-005` | `evidence:claim-matrix-status-guidance-validation` | `critique:claim-matrix-status-guidance-review` | supported |

# Execution Notes

Likely touched surfaces are `skills/loom-tickets/templates/ticket.md` and,
possibly, a short backlink in claim coverage if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:wsalias6`.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:claim-matrix-status-guidance-validation` and oracle critique
`critique:claim-matrix-status-guidance-review` support closure with no findings.

# Evidence

Recorded: `evidence:claim-matrix-status-guidance-validation`.

# Critique Disposition

Risk class: low

Critique policy: mandatory

Policy rationale: user instruction requires oracle critique for every ticket;
template status vocabulary affects future acceptance consistency.

Required critique profiles:

- template-safety
- records-grammar
- operator-clarity

Findings:

`critique:claim-matrix-status-guidance-review` - no findings; mandatory oracle
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Claim matrix status copy guidance was promoted directly into the ticket
  template while leaving claim coverage as canonical vocabulary owner.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
ticket template and claim coverage reference.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T02:17:18Z
Basis: Ralph packet `packet:ralph-ticket-claimmx5-20260503T021312Z`; evidence
`evidence:claim-matrix-status-guidance-validation`; oracle critique
`critique:claim-matrix-status-guidance-review` with no findings.
Residual risks: validation is structural/manual; there is no automated
protocol-template test suite. Status tokens are repeated in the template for copy
safety, so future vocabulary changes must reconcile the pointer/list.

# Dependencies

None.

# Journal

- 2026-05-03T00:56:36Z: Created from council finding `NC2-005`.
- 2026-05-03T02:14:37Z: Ralph iteration
  `packet:ralph-ticket-claimmx5-20260503T021312Z` completed in scope. Evidence
  recorded in `evidence:claim-matrix-status-guidance-validation`; next route is
  mandatory oracle critique.
- 2026-05-03T02:17:18Z: Mandatory oracle critique
  `critique:claim-matrix-status-guidance-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
