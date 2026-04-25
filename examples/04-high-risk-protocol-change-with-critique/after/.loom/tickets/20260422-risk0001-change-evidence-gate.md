---
id: ticket:risk0001
kind: ticket
status: review_required
change_class: protocol-authority
created_at: 2026-04-22T00:00:00Z
updated_at: 2026-04-22T00:05:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  critique:
    - critique:evidence-gate-review
  evidence:
    - evidence:evidence-gate-structural-check
external_refs: {}
depends_on: []
---

# Summary

Change evidence requirements before closure.

# Acceptance Criteria

- Evidence minimums are clear enough that future agents do not close work with
  unsupported claims.

# Local Claims

- CLAIM-001: The evidence gate protocol change is structurally routed through
  ticket, evidence, and critique before acceptance.

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:risk0001#CLAIM-001 | evidence:evidence-gate-structural-check | critique:evidence-gate-review#FIND-001 open | challenged |

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: Protocol-authority changes can alter closure semantics for
future agents.

Required critique profiles:
- protocol-change
- operator-clarity

Findings:
- critique:evidence-gate-review#FIND-001 — open

Disposition status: pending

# Constitutional Decision Disposition

The constitutional decision is deferred. The rule fixture is not accepted as
durable policy until critique:evidence-gate-review#FIND-001 is resolved or
explicitly accepted as risk.
