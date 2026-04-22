---
id: ticket:0od11m0z
kind: ticket
status: closed
created_at: 2026-04-22T09:10:31Z
updated_at: 2026-04-22T16:09:59Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  critique:
    - critique:protocol-hardening-review
external_refs: {}
depends_on: []
---

# Summary

Expand the remaining protocol examples into before/after fixture form.

# Context

The feature-with-Ralph example now includes a concrete fixture slice. The other
examples remain narrative traces.

# Why Now

Fixtures make protocol changes easier to review across harnesses without
building a runtime.

# Scope

- add `before/`, `operator-request.md`, `expected-route.md`, `after/`, and
  `common-wrong-behavior.md` surfaces where useful
- keep fixtures small and readable
- preserve examples as non-authoritative protocol traces

# Non-goals

- do not create a runtime test harness
- do not make examples canonical project truth

# Acceptance Criteria

- at least the remaining high-value examples have concrete before/after slices
- each fixture demonstrates owner-layer routing and common wrong behavior

# Coverage

Covers:
- critique:protocol-hardening-review#FIND-002

# Critique Disposition

Risk class: low

Required critique profiles:
- operator-clarity

Findings:
- critique:protocol-hardening-review#FIND-002 — resolved

Status: completed

# Wiki Disposition

Not required.

# Journal

- 2026-04-22T09:10:31Z: Created from critique follow-up.
- 2026-04-22T16:09:59Z: Added fixture structure for all five examples,
  including operator request, expected route, common wrong behavior, and
  before/after slices.
