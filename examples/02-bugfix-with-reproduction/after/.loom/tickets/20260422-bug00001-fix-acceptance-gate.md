---
id: ticket:bug00001
kind: ticket
status: review_required
change_class: code-behavior
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:05:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  spec:
    - spec:acceptance-hardening
  evidence:
    - evidence:acceptance-red-green
external_refs: {}
depends_on: []
---

# Summary

Fix acceptance closure when high-severity critique is unresolved.

# Coverage

Covers:
- spec:acceptance-hardening#ACC-001

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| spec:acceptance-hardening#ACC-001 | evidence:acceptance-red-green | mandatory critique pending | supported_pending_review |

# Evidence

- evidence:acceptance-red-green

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: Acceptance-gate behavior can close work incorrectly when
high-severity findings remain unresolved.

Required critique profiles:
- code-change
- operator-clarity

Findings: []

Disposition status: pending

# Journal

- 2026-04-22T00:00:00Z: Fix landed with red/green evidence; critique is next.
