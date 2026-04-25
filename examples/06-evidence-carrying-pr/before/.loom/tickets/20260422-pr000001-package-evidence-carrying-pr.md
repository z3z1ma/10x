---
id: ticket:pr000001
kind: ticket
status: ready
change_class: release-packaging
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:00:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  spec:
    - spec:evidence-carrying-pr
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
| spec:evidence-carrying-pr#ACC-001 | pending | pending | open |
| spec:evidence-carrying-pr#ACC-002 | pending | pending | open |

# Evidence

Expected from PR package inspection.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: External PR packages can mislead reviewers if they omit
evidence limits, critique findings, or ticket closure boundaries.

Required critique profiles:
- operator-clarity

Findings:
- none yet

Disposition status: pending

# Wiki Disposition

No wiki page required unless the PR packaging route becomes recurring.
