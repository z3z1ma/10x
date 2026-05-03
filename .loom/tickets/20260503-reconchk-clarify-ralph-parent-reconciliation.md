---
id: ticket:reconchk
kind: ticket
status: ready
change_class: workflow-boundary
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
external_refs: {}
depends_on:
  - ticket:evhard05
---

# Summary

Make Ralph parent reconciliation and stale compiled packet recovery explicit.

# Context

Council identified parent reconciliation as the fragile point where child output
can fail to become ticket/evidence/critique truth.

# Why Now

Ralph is central to bounded fresh-worker execution. The parent checklist should be
copyable and recovery queries should find stale packets.

# Scope

- Add or sharpen parent reconciliation checklist in Ralph guidance.
- Add stale `compiled` packet recovery/search guidance in Ralph or records query
  references.
- Keep packets as support artifacts, not truth owners.

# Out Of Scope

- Do not create a reconciliation record kind.
- Do not add automated merge scripts or hidden runtimes.

# Acceptance Criteria

- ACC-001: Ralph guidance gives a concrete parent reconciliation checklist after
  child output.
- ACC-002: Guidance includes stale `compiled` packet discovery and disposition.
- ACC-003: The text preserves ticket-owned execution/acceptance and packet support
  boundaries.
- ACC-004: Evidence records targeted reconciliation/stale packet searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-007`
- `ticket:reconchk#ACC-001`
- `ticket:reconchk#ACC-002`
- `ticket:reconchk#ACC-003`
- `ticket:reconchk#ACC-004`
- `ticket:reconchk#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-007` | pending | pending | open |
| `ticket:reconchk#ACC-001` | pending | pending | open |
| `ticket:reconchk#ACC-002` | pending | pending | open |
| `ticket:reconchk#ACC-003` | pending | pending | open |
| `ticket:reconchk#ACC-004` | pending | pending | open |
| `ticket:reconchk#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-ralph/references/work-driver.md`,
`skills/loom-ralph/references/packet-contract.md`, and query/status references if
needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: parent reconciliation checklist and stale packet recovery.
Write boundary: Ralph references and directly related query/status references.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, reconciliation query observations, and
critique recommendation.

# Evidence

Expected: targeted searches for reconciliation checklist, stale `compiled` packet
query, packet terminal statuses, ticket truth boundary, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: parent reconciliation controls whether child work becomes
truthful Loom state.

Required critique profiles:

- workflow-boundary
- packet-safety
- operator-clarity

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Pending after critique.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

- `ticket:evhard05`

# Journal

- 2026-05-03T04:09:51Z: Created from council parent reconciliation finding.
