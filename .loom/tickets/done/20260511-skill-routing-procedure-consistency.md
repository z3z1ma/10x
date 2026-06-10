# Skill Routing Procedure Consistency

Status: done
Created: 2026-05-11
Updated: 2026-05-11

Legacy note: Risk — medium - changes shipped instruction wording across core doctrine and playbook skills.

## Summary

Clarify how workflow-specific skills differ from record skills, require routed Loom skills to be followed completely, and make Ralph packet launch guidance transport-neutral.

Single closure claim: shipped skill and public-doc prose consistently treats workflow-specific skills as process routes over record skills, requires target skill procedures to be followed when routing, and says any worker transport should point at the packet path rather than carrying the work contract in the launch wrapper.

## Related Records

- `.loom/tickets/done/20260510-product-surface-language-cleanup.md` - prior product-surface cleanup this follow-up refines.
- `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md` - command and search evidence for this ticket.
- `former packet 20260511T074110Z-skill-routing-procedure-review` - fresh-context review packet.
- `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md` - audit record for the fresh-context review.

## Scope

May change:

- `loom-core/skills/using-loom/**`
- `loom-core/skills/loom-ralph/**`
- `loom-core/skills/loom-tickets/**` when ticket handoff wording needs alignment
- `loom-playbooks/skills/*/SKILL.md`
- public docs that define package, record-skill, workflow-skill, or Ralph launch semantics
- this ticket and supporting evidence, packets, and audit records

Must not change:

- eval app implementation files
- adapter entrypoints or manifests unless verification reveals direct drift
- historical dogfood records solely to make product-facing grep cleaner

## Acceptance

- ACC-001: Product-facing prose defines the distinction between record skills and workflow-specific skills without relying on package-layer workflow precedence.
  - Evidence: source diff inspection and targeted searches.
  - Audit: fresh review should challenge terminology consistency.
  - Result: satisfied by `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md` and `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md`.

- ACC-002: Every playbook skill's `## Loom Surfaces` section says routed Loom skills must be followed with their own procedure and guidance, not treated as shortcuts.
  - Evidence: grep/count over `loom-playbooks/skills/*/SKILL.md`.
  - Audit: fresh review should inspect whether the wording is strong and consistent.
  - Result: satisfied by `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md` and `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md`.

- ACC-003: Ralph launch guidance is transport-neutral: subagents, headless harness commands, manual handoffs, or other transports should receive the packet path and leave the work contract in the packet.
  - Evidence: source diff inspection and targeted searches.
  - Audit: fresh review should challenge whether any wording still narrows the rule to harness-native subagents only.
  - Result: satisfied by `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md` and `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md`.

- ACC-004: Package smoke, package pack checks, and Markdown diff checks pass after the wording changes.
  - Evidence: command outputs recorded in evidence.
  - Result: satisfied by `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md`.

## Current State

Closed. Implementation changes are complete; package checks, pack checks, Markdown diff checks, and targeted searches passed. Fresh-context review found no shipped-prose issues and raised one low-severity ticket-state finding, `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md#FIND-001`, which this update resolves before closure.

## Journal

- 2026-05-11: Created follow-up for skill routing procedure consistency and transport-neutral Ralph launch wording.
- 2026-05-11: Updated core doctrine and public docs to define record skills as owning Loom surfaces and workflow-specific skills as task-shaped routes over those surfaces.
- 2026-05-11: Added the routed-skill procedure requirement to all 25 playbook `SKILL.md` files.
- 2026-05-11: Updated Ralph launch guidance so every worker transport points at the packet path and keeps the work contract in the packet.
- 2026-05-11: Ran package smoke, pack checks, `git diff --check`, and targeted searches; results recorded in `.loom/evidence/20260511-skill-routing-procedure-consistency-checks.md`.
- 2026-05-11: Consumed `former packet 20260511T074110Z-skill-routing-procedure-review`; fresh review returned `concerns` only for stale ticket current-state wording, with shipped prose clear within scope.
- 2026-05-11: Resolved `.loom/reviews/20260511-skill-routing-procedure-consistency-review.md#FIND-001` by updating this ticket's related records, acceptance results, current state, and journal, then closed the ticket. Residual risk: targeted searches and sampled review cannot prove every semantically equivalent stale wording is absent, and live agent behavior was not verified.
