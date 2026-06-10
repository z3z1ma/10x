# Playbook And Public Doc Alignment

Status: done
Created: 2026-05-10
Updated: 2026-05-10

Legacy note: Risk — medium - playbooks and docs are secondary surfaces that must reinforce Core without becoming a competing protocol.

## Summary

Align execution-triggering playbooks and public docs with the strengthened Core loop semantics: shape before build, split before ticket, packet before worker launch, and evidence/audit before closure.

## Related Records

- `.loom/tickets/20260510-core-loop-hardening.md` - owns the broader hardening sequence.
- `.loom/research/20260510-loom-loop-failure-analysis.md` - explains why playbook/core composition needs clearer language.

## Scope

May change:

- `loom-playbooks/skills/loom-frontend-ui-engineering/SKILL.md`
- `loom-playbooks/skills/loom-source-driven-development/SKILL.md`
- `loom-playbooks/skills/loom-incremental-implementation/SKILL.md`
- `loom-playbooks/skills/loom-code-review-and-quality/SKILL.md`
- `loom-playbooks/skills/loom-idea-refine/SKILL.md`
- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `loom-core/README.md`
- `loom-playbooks/README.md`

Must not change:

- package entrypoints, manifests, hooks, or adapter catalogs unless verification reveals direct drift

## Acceptance

- ACC-001: Relevant playbooks make Core ownership visible at the point they can trigger execution or worker handoff.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge whether playbooks can still be read as bypassing Core shaping or Ralph.

- ACC-002: Public docs restate the strengthened protocol without creating new surfaces or source-repo-only assumptions.
  - Evidence: source diff inspection and final audit.
  - Audit: fresh review should challenge doc consistency with Core.

## Current State

Closed. Relevant playbooks and public docs now reinforce Core loop order, Core
surface ownership, ticket-ready slicing, and packetized worker handoff without
creating a second protocol surface. Fresh-context audit
`.loom/reviews/20260510-loop-hardening-review.md` found no material issues within scope.

## Journal

- 2026-05-10: Created from `.loom/tickets/20260510-core-loop-hardening.md`.
- 2026-05-10: Updated relevant execution/review playbooks and public docs to
  reinforce Core shaping, slicing, and packet handoff semantics; moved to review
  pending packetized fresh-context audit.
- 2026-05-10: Closed after `.loom/reviews/20260510-loop-hardening-review.md` returned a
  clear verdict for playbook and public doc alignment.
