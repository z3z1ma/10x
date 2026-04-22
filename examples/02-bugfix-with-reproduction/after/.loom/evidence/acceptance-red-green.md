---
id: evidence:acceptance-red-green
kind: evidence
status: recorded
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

# Summary

Red/green proof for high-severity critique blocking acceptance.

# Supports Claims

- spec:acceptance-hardening#ACC-001

# Challenges Claims

None.

# Environment

Commit: abcdef0
Branch: bugfix/acceptance-gate
Runtime: fixture
OS: unknown
Relevant config: none

# Result

Before: ticket closed despite unresolved high-severity critique.
After: ticket remained open and reported the blocking finding.

# Limitations

Fixture evidence illustrates the route, not a real executable test harness.
