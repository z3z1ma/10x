# Ralph And Audit Handoff Doctrine

ID: ticket:20260510-ralph-audit-handoff-doctrine
Type: Ticket
Status: closed
Created: 2026-05-10
Updated: 2026-05-10
Risk: medium - changes inner-loop worker and audit guidance that controls recoverability of delegated work.

## Summary

Strengthen Core worker handoff language so Loom worker runs are compiled as on-disk Ralph packets before launch, and substantive fresh-context audits are prepared through those packets before audit records are written.

## Related Records

- `plan:20260510-core-loop-hardening` - owns the broader hardening sequence.
- `research:20260510-loom-loop-failure-analysis` - identifies missing packet adherence in the eval.

## Scope

May change:

- `loom-core/skills/using-loom/references/delegating-to-workers.md`
- `loom-core/skills/loom-ralph/SKILL.md`
- `loom-core/skills/loom-ralph/references/running-packets.md`
- `loom-core/skills/loom-ralph/references/packet-shape.md`
- `loom-core/skills/loom-audit/SKILL.md`
- `loom-core/skills/loom-audit/references/audit-shape.md`
- `loom-core/skills/loom-audit/templates/audit.md`
- `loom-core/skills/loom-tickets/references/acting-on-tickets.md`

Must not change:

- adapter implementation mechanics
- subagent tool behavior
- eval workspace records

## Acceptance

- ACC-001: Ralph guidance states that a Loom worker run is packet file plus launch, with wrapper prompts pointing at the packet instead of carrying the work contract.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge whether direct `task` prompts still read as an acceptable Loom worker handoff.

- ACC-002: Audit guidance makes the fresh-context review request a Ralph packet and keeps audit records as the durable review result after the worker returns.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge audit/Ralph surface separation.

## Current State

Closed. Ralph, delegation, audit, and ticket-acting guidance now state that a Loom
worker run is an on-disk `.loom/packets/ralph/` packet plus a launch that points to
the packet. Fresh-context audit `audit:20260510-loop-hardening-review` found no
material issues within scope.

## Journal

- 2026-05-10: Created from `plan:20260510-core-loop-hardening`.
- 2026-05-10: Updated `using-loom` delegation, Ralph, audit, ticket acting, and
  packet/audit templates to make on-disk packets the worker handoff contract;
  moved to review pending packetized fresh-context audit.
- 2026-05-10: Closed after `audit:20260510-loop-hardening-review` returned a
  clear verdict for packet-before-worker and audit handoff semantics.
