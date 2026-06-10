# Docs Validation No Packets

Status: done
Created: 2026-05-15
Updated: 2026-05-15

Legacy note: Risk — medium - updates public explanations and final validation for a core workflow semantics change.

Priority: medium - final alignment should run after source-facing doctrine, agents, and Playbooks change.
Depends-On: .loom/tickets/done/20260515-agent-surfaces-ticket-worker-model.md, .loom/tickets/done/20260515-playbook-ticket-worker-language.md

## Summary

Align human-facing docs and final validation with the no-packet active product model. The single closure claim is that current docs and validation no longer present packets as a Loom surface, while historical `.loom` packet records remain untouched.

## Related Records

- `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md` - durable decision removing packets while preserving Ralph.
- `.loom/specs/ticket-owned-worker-handoffs.md` - target worker handoff behavior.
- `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` - parent plan.
- `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md` - Core prerequisite.
- `.loom/tickets/done/20260515-agent-surfaces-ticket-worker-model.md` - agent-surface prerequisite.
- `.loom/tickets/done/20260515-playbook-ticket-worker-language.md` - Playbook language prerequisite.
- `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md` - validation dossier supporting closure.
- `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` - Ralph-backed audit covering this ticket and the parent migration.

## Scope

May change:

- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `INSTALL.md`
- package READMEs under `loom-core/` and `loom-playbooks/`
- tests, smoke expectations, or documentation checks that mention packets as an active surface
- this ticket and new evidence/audit records as needed

Must not change:

- source-facing Core skills, agent prompts, or Playbook bodies except narrow stale-reference fixes discovered during final grep
- historical `.loom/packets/**` records or historical tickets/audits that cite packets
- unrelated package architecture, adapter install flow, or Playbook invocation behavior

## Acceptance

- ACC-001: Current human-facing docs no longer list packets as a Loom surface, describe `.loom/packets/ralph/` as an active directory, or teach users to compile Ralph packets for future work.
  - Evidence: targeted grep/source inspection over docs after edits, excluding historical `.loom` records.
  - Audit: separate audit is expected because docs must faithfully restate the changed Core model without becoming product doctrine.

- ACC-002: Docs explain the replacement model concisely: tickets hold durable worker/audit context, Ralph remains bounded worker/review discipline, transient launch prompts are not durable truth, and evidence/audit still own proof and review.
  - Evidence: source inspection of updated docs.
  - Audit: challenge whether docs over-explain repository dogfood or under-specify worker boundaries.

- ACC-003: Final active-surface grep shows no future packet-creation instructions remain in shipped product surfaces, generated command surfaces, agent prompts, docs, package entrypoints, or tests, except explicitly historical `.loom` records or deprecation notes.
  - Evidence: recorded grep commands and outputs.
  - Audit: audit reviews exclusions and false positives.

- ACC-004: Relevant package and Markdown checks pass after the full migration.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, and `git diff --check`, unless a command is skipped with a recorded reason.
  - Audit: audit reviews command evidence and skipped-command reasons.

## Current State

Closed. Updated current human-facing docs, package docs, the activation eval, and the explicit-skill test setup so active product-facing explanations no longer list packets as a Loom surface, describe `.loom/packets/ralph/` as an active directory, or teach compiling Ralph packets for future work.

Changed files in this slice:

- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `INSTALL.md`
- `loom-core/README.md`
- `loom-playbooks/README.md`
- `evals/activation/loom-activation-scenarios.md`
- `tests/explicit-skill-requests/run-test.sh`
- `.loom/tickets/done/20260515-docs-validation-no-packets.md`

Validation run:

- `npm --prefix loom-core run smoke` passed.
- `npm --prefix loom-core run pack:check` passed.
- `npm --prefix loom-playbooks run smoke` passed.
- `npm --prefix loom-playbooks run pack:check` passed.
- `git diff --check` passed.
- Targeted active-surface grep outside `.loom` passed with no matches: `rg -n "packet|packets|\.loom/packets|packet:" --glob '!.loom/**' --glob '!node_modules/**' .`.

Remaining packet matches/exclusions: none outside `.loom` after this slice. Historical `.loom` packet records and historical `.loom` references were intentionally not edited. The worktree still contains existing unrelated/prerequisite changes from other tickets, including historical `.loom/packets` records; this ticket did not modify or create `.loom/packets` records.

Audit: `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` returned clear after follow-up. The grep result proves active non-`.loom` packet wording is absent. Unrelated historical `.loom/packets/ralph` worktree records are explicitly excluded from this ticket and were not created or modified for this migration.

## Journal

- 2026-05-15: Created from `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` as the docs and final validation slice.
- 2026-05-15: Began implementation from this ticket and linked records. Preflight grep outside `.loom` found active packet instructions in `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, `loom-core/README.md`, `loom-playbooks/README.md`, `evals/activation/loom-activation-scenarios.md`, and `tests/explicit-skill-requests/run-test.sh`; updating those surfaces to ticket-owned Ralph language.
- 2026-05-15: Replaced active packet-surface and packet-compilation docs with ticket-owned Ralph worker/review language. Validation passed: Core smoke, Core pack dry-run, Playbooks smoke, Playbooks pack dry-run, `git diff --check`, and targeted grep outside `.loom` for packet terms. Moved ticket to `Status: review`; separate audit remains the next honest move before closure.
- 2026-05-15: Cited `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md` and `.loom/reviews/20260515-ticket-owned-worker-handoffs.md`; audit returned clear after follow-up. Closed with unrelated historical `.loom/packets/ralph` worktree records excluded from this migration.
