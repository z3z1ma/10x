---
id: ticket:pr000001
kind: ticket
status: complete_pending_acceptance
change_class: release-packaging
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:05:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  spec:
    - spec:evidence-carrying-pr
  evidence:
    - evidence:evidence-carrying-pr-package
  critique:
    - critique:evidence-carrying-pr-review
  wiki:
    - wiki:evidence-carrying-pr
external_refs: {}
depends_on: []
---

# Summary

Package an evidence-carrying PR body from Loom records.

# Acceptance Criteria

- PR body cites ticket, claims, evidence, critique, residual risks, and
  follow-ups.
- Ticket closure remains with acceptance.

# Coverage

Covers:
- spec:evidence-carrying-pr#ACC-001
- spec:evidence-carrying-pr#ACC-002

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| spec:evidence-carrying-pr#ACC-001 | evidence:evidence-carrying-pr-package | critique:evidence-carrying-pr-review no blocking findings | supported_pending_review |
| spec:evidence-carrying-pr#ACC-002 | evidence:evidence-carrying-pr-package | critique:evidence-carrying-pr-review no blocking findings | supported_pending_review |

# Evidence

- evidence:evidence-carrying-pr-package

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: External PR packages can mislead reviewers if they omit
evidence limits, critique findings, or ticket closure boundaries.

Required critique profiles:
- operator-clarity

Findings:
- none

Disposition status: completed

# Wiki Disposition

Promoted to `wiki:evidence-carrying-pr` because the packaging route is reusable.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:
