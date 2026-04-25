---
id: spec:shipping-workflow
kind: spec
status: accepted
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:05:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:abcd1234
external_refs: {}
---

# Summary

Define how Loom packages completed work for external handoff.

# Requirements

- REQ-001: Shipping may summarize Loom work for PR, release, or handoff.
- REQ-002: Shipping must not close tickets.

# Acceptance

- ACC-001: Given a completed ticket with evidence, the workflow produces a
  summary grounded in Loom records.
- ACC-002: Given an open ticket, the workflow leaves closure to the ticket
  acceptance gate.
