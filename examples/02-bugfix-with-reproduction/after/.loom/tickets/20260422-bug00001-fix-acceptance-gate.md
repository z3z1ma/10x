---
id: ticket:bug00001
kind: ticket
status: review_required
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:00:00Z
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

# Critique Disposition

Risk class: high

Required critique profiles:
- code-change
- operator-clarity

Findings: []

Status: required

# Journal

- 2026-04-22T00:00:00Z: Fix landed with red/green evidence; critique is next.
