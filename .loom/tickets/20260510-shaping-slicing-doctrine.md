# Shaping And Slicing Doctrine

ID: ticket:20260510-shaping-slicing-doctrine
Type: Ticket
Status: closed
Created: 2026-05-10
Updated: 2026-05-10
Risk: medium - changes Core guidance that future agents use to decide whether work is shaped enough to execute.

## Summary

Strengthen the Core outer-loop and slicing language so broad requests move through operator-shaped intent, quality, evidence, and ticket boundaries before implementation. The outcome is clearer Core guidance in `using-loom`, ticket creation, and plan slicing surfaces.

## Related Records

- `plan:20260510-core-loop-hardening` - owns the broader hardening sequence.
- `research:20260510-loom-loop-failure-analysis` - explains the observed failure modes.

## Scope

May change:

- `loom-core/skills/using-loom/SKILL.md`
- `loom-core/skills/using-loom/references/shaping-with-humans.md`
- `loom-core/skills/loom-tickets/SKILL.md`
- `loom-core/skills/loom-tickets/references/creating-tickets.md`
- `loom-core/skills/loom-tickets/references/ticket-shape.md`
- `loom-core/skills/loom-plans/SKILL.md`
- `loom-core/skills/loom-plans/references/creating-plans.md`
- `loom-core/skills/loom-plans/references/slicing-work.md`
- related templates only if the template shape needs the new discipline

Must not change:

- adapter manifests or package entrypoints
- eval app source files
- unrelated skill playbooks except through separate tickets

## Acceptance

- ACC-001: Core shaping guidance explicitly treats vague or quality-heavy product requests as outer-loop work until operator direction, quality bar, non-goals, evidence posture, and execution boundary are clear.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge whether the wording prevents premature execution without overfitting to the eval.

- ACC-002: Ticket and plan guidance includes a practical single-work-unit or single-closure-claim slicing test.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge whether a stack/data/UI/verification bundle would still pass as one ticket.

## Current State

Closed. Core shaping and slicing doctrine now makes vague product requests an
outer-loop input until operator direction, quality bar, evidence posture, and
execution boundary are clear. Ticket and plan guidance now carries the
single-closure-claim slicing test. Fresh-context audit
`audit:20260510-loop-hardening-review` found no material issues within scope.

## Journal

- 2026-05-10: Created and set active from `plan:20260510-core-loop-hardening`.
- 2026-05-10: Updated `using-loom`, shaping, ticket, plan, and template guidance;
  moved to review pending packetized fresh-context audit.
- 2026-05-10: Closed after `audit:20260510-loop-hardening-review` returned a
  clear verdict for the shaping and slicing changes.
