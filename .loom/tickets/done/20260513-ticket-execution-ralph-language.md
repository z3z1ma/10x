# Ticket Execution Ralph Language

Status: done
Created: 2026-05-13
Updated: 2026-05-13

Legacy note: Risk — medium - changes Core ticket execution doctrine and related loop wording.

## Summary

Align ticket execution language with the Ralph-centered worker model. Tickets should own scope, state, acceptance, evidence posture, and closure; Ralph packets should own bounded execution and review slices for ticket work.

The closure claim is that `loom-tickets` no longer presents Ralph as merely optional delegation, and related loop/docs say ticket work executes through Ralph packets.

## Related Records

- `.loom/tickets/done/20260513-ralph-language-consolidation.md` - prior terminology consolidation around Ralph-backed worker and audit language.
- `.loom/evidence/20260513-ralph-language-consolidation-checks.md` - prior validation evidence for the Ralph language pass.
- `.loom/evidence/20260513-ticket-execution-ralph-language-checks.md` - validation evidence for this ticket execution language pass.

## Scope

May change:

- `loom-core/skills/loom-tickets/**`
- `loom-core/skills/using-loom/**` when loop wording mentions ticket execution
- `loom-core/skills/loom-plans/references/slicing-work.md` when child-ticket
  readiness mentions execution
- `loom-playbooks/skills/loom-incremental-implementation/SKILL.md` when implementation slice wording mentions Ralph execution
- human-facing docs that restate ticket execution semantics
- this ticket and related evidence

Must not change:

- historical `.loom` records except this ticket and new evidence
- adapter manifests, package mechanics, hooks, or runtime behavior
- unrelated spec-slicing or package-surface edits already present in the worktree

## Acceptance

- ACC-001: `loom-tickets` states that tickets own live execution state and acceptance, while Ralph packets own bounded execution/review slices for ticket work.
  - Evidence: source inspection of `loom-core/skills/loom-tickets/**` after edits.
  - Audit: separate audit is not required for this terminology-only slice if grep and diff inspection show the ticket/Ralph ownership split clearly.

- ACC-002: Ticket acting guidance tells agents to compile/use a Ralph packet for ticket implementation or review slices instead of treating Ralph as only delegated-worker optionality.
  - Evidence: source inspection of `loom-core/skills/loom-tickets/references/acting-on-tickets.md` after edits.
  - Audit: separate audit is not required for this terminology-only slice if package checks and diff inspection pass.

- ACC-003: Related loop and implementation-playbook wording no longer implies ticket execution can bypass Ralph as a normal path.
  - Evidence: targeted grep/source inspection of affected Core/playbook/docs wording after edits.
  - Audit: separate audit is not required for this terminology-only slice if the wording preserves ticket state ownership and Ralph packet boundaries.

## Current State

Closed. `loom-tickets` now says tickets own state, acceptance, progress, review posture, and closure, while Ralph packets own bounded execution and review slices. Acting guidance now says ticket execution uses Ralph packets, including when the current session performs the work. Related loop, plan-slicing, incremental implementation, and current doc restatements now describe ticket execution through Ralph packets. Evidence is recorded in `.loom/evidence/20260513-ticket-execution-ralph-language-checks.md`; separate audit was not performed per the terminology-only audit waiver.

## Journal

- 2026-05-13: Created follow-up ticket from operator request to make `loom-tickets` use the same Ralph-centered execution language.
- 2026-05-13: Updated ticket skill, ticket references/template, loop wording, plan slicing, incremental implementation, and current docs so ticket execution is described as Ralph packet execution. Recorded validation evidence and closed.
