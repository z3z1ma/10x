---
id: spec:acceptance-hardening
kind: spec
status: accepted
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:00:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:bug00001
external_refs: {}
---

# Requirements

- REQ-001: Acceptance must fail closed when required critique has unresolved
  high-severity findings.

# Acceptance

- ACC-001: Given unresolved high-severity critique, acceptance leaves the
  ticket open and reports the blocking finding.
