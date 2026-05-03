---
id: ticket:pktfam04
kind: ticket
status: ready
change_class: packet-safety
risk_class: high
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
  - ticket:tplsave3
---

# Summary

Separate shared packet grammar from Ralph-only requirements without weakening
Ralph packet discipline.

# Context

Council found critique/wiki packets may be forced into Ralph-shaped precision or
fake `unknown` fields if shared packet requirements are too broad.

# Why Now

Packet support surfaces are central to fresh workers and packetized sibling work.
Their required fields should be accurate by family.

# Scope

- Clarify shared packet fields versus Ralph-specific fields.
- Preserve strict Ralph `source_fingerprint`, `execution_context`,
  `child_write_scope`, and `verification_posture` expectations.
- Adjust critique/wiki packet templates or references if current wording implies
  Ralph-only requirements everywhere.

# Out Of Scope

- Do not add new packet families or canonical owner layers.
- Do not weaken Ralph packet launch safety.

# Acceptance Criteria

- ACC-001: Shared packet grammar distinguishes common support fields from
  family-specific required fields.
- ACC-002: Ralph requirements remain strict and explicit.
- ACC-003: Critique/wiki packet guidance avoids fake precision while preserving
  enough review/synthesis contract metadata.
- ACC-004: Evidence records targeted packet-family searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-005`
- `ticket:pktfam04#ACC-001`
- `ticket:pktfam04#ACC-002`
- `ticket:pktfam04#ACC-003`
- `ticket:pktfam04#ACC-004`
- `ticket:pktfam04#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-005` | pending | pending | open |
| `ticket:pktfam04#ACC-001` | pending | pending | open |
| `ticket:pktfam04#ACC-002` | pending | pending | open |
| `ticket:pktfam04#ACC-003` | pending | pending | open |
| `ticket:pktfam04#ACC-004` | pending | pending | open |
| `ticket:pktfam04#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-records/references/packet-frontmatter.md`, Ralph
packet contract/template, critique packet template, and wiki packet template.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: packet-family requirement separation.
Write boundary: packet frontmatter reference and packet templates/references.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, packet field observations, and critique
recommendation.

# Evidence

Expected: targeted searches for required shared fields, Ralph-only fields,
`verification_posture`, critique/wiki packet fields, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: packet grammar controls bounded worker contracts.

Required critique profiles:

- packet-safety
- protocol-change
- workflow-boundary

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

- `ticket:tplsave3`

# Journal

- 2026-05-03T04:09:51Z: Created from council packet-family requirement finding.
