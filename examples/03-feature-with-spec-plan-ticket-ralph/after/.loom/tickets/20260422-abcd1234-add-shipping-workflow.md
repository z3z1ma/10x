---
id: ticket:abcd1234
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
    - spec:shipping-workflow
  evidence:
    - evidence:shipping-workflow-smoke
external_refs: {}
depends_on: []
---

# Summary

Add the first shipping workflow surface.

# Coverage

Covers:
- spec:shipping-workflow#ACC-001
- spec:shipping-workflow#ACC-002

# Critique Disposition

Risk class: medium

Required critique profiles:
- code-change
- operator-clarity

Findings: []

Status: required

# Journal

- 2026-04-22T00:00:00Z: Ralph iteration consumed; parent routed to critique.
