# Playbook Ticket Worker Language

ID: ticket:20260515-playbook-ticket-worker-language
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - changes optional workflow macro language and generated command surfaces, but should preserve existing Playbook invocation behavior.
Priority: medium - should follow Core and agent vocabulary updates to avoid divergent wording.
Depends On: ticket:20260515-core-ticket-owned-worker-doctrine

## Summary

Update Playbook macro bodies and generated command surfaces so optional workflow lenses preserve ticket-owned worker/audit discipline instead of packet compilation or packet coordination. The single closure claim is that active Playbook product surfaces no longer instruct agents to create Ralph packets or coordinate by packet IDs.

## Related Records

- `decision:0002` - durable decision removing packets while preserving Ralph.
- `spec:ticket-owned-worker-handoffs` - target worker handoff behavior.
- `spec:playbook-explicit-macros` - Playbook invocation and workflow-lens behavior.
- `plan:20260515-ticket-owned-worker-handoffs` - parent plan.
- `ticket:20260515-core-ticket-owned-worker-doctrine` - prerequisite Core vocabulary migration.
- `evidence:20260515-ticket-owned-worker-handoffs-validation` - validation dossier supporting closure.
- `audit:20260515-ticket-owned-worker-handoffs` - Ralph-backed audit covering this ticket and the parent migration.

## Scope

May change:

- `loom-playbooks/playbooks/**/SKILL.md`
- `loom-playbooks/commands/*.toml`
- `loom-playbooks/loom-playbooks.mjs` shared macro preamble if it contains packet wording
- Playbooks package smoke or generation checks directly needed to keep commands aligned
- this ticket and new evidence/audit records as needed

Must not change:

- Core skills, Driver/Weaver agents, or human docs except to record blockers
- Playbook invocation mechanics from `spec:playbook-explicit-macros`
- unrelated Playbook workflow redesigns beyond replacing packet handoff semantics
- historical `.loom/packets/**` records

## Acceptance

- ACC-001: Playbook source macro bodies no longer instruct agents to compile Ralph packets, write `.loom/packets`, use packet IDs as coordination handles, or compare work against packet missions as the active model.
  - Evidence: targeted grep/source inspection over `loom-playbooks/playbooks/**` after edits.
  - Audit: separate audit is expected if many Playbooks change or if wording risks weakening worker boundaries.

- ACC-002: Playbook guidance that delegates worker or review work uses ticket-owned Ralph runs, child tickets, ticket-defined write scopes, evidence, and audit as the durable path.
  - Evidence: source inspection of Playbooks that previously mentioned packets, especially incremental implementation, parallel worker coordination, source-driven development, code review, frontend UI, TDD, git workspace isolation, and architecture/deprecation/security playbooks.
  - Audit: challenge whether the new wording allows unbounded prompt-only work.

- ACC-003: Generated or adapter command surfaces are aligned with the Playbook source language and do not retain stale packet wording.
  - Evidence: targeted grep/source inspection over `loom-playbooks/commands/*.toml` and any generation path used.
  - Audit: included in the Playbook audit pass.

- ACC-004: Playbook explicit invocation behavior from `spec:playbook-explicit-macros` is preserved; this ticket does not reintroduce implicit Playbook activation.
  - Evidence: Playbooks smoke/pack checks and source inspection of explicit macro surfaces.
  - Audit: included in the Playbook audit pass.

- ACC-005: Relevant checks pass.
  - Evidence: `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, and `git diff --check`, unless a command is skipped with a recorded reason.
  - Audit: audit reviews command evidence and skipped-command reasons.

## Current State

Closed. Updated the shared Playbook macro preamble, targeted Playbook source bodies, and regenerated all 25 command TOML files so optional workflow lenses preserve ticket-owned Ralph worker/review discipline instead of packet compilation, `.loom/packets` writes, packet IDs, or packet output as durable truth.

Changed source areas:

- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/playbooks/loom-api-and-interface-design/SKILL.md`
- `loom-playbooks/playbooks/loom-architecture-deepening/SKILL.md`
- `loom-playbooks/playbooks/loom-branch-finish/SKILL.md`
- `loom-playbooks/playbooks/loom-code-review-and-quality/SKILL.md`
- `loom-playbooks/playbooks/loom-debugging-and-error-recovery/SKILL.md`
- `loom-playbooks/playbooks/loom-deprecation-and-migration/SKILL.md`
- `loom-playbooks/playbooks/loom-doubt-driven-development/SKILL.md`
- `loom-playbooks/playbooks/loom-frontend-ui-engineering/SKILL.md`
- `loom-playbooks/playbooks/loom-git-workspace-isolation/SKILL.md`
- `loom-playbooks/playbooks/loom-incremental-implementation/SKILL.md`
- `loom-playbooks/playbooks/loom-intake-triage/SKILL.md`
- `loom-playbooks/playbooks/loom-parallel-worker-coordination/SKILL.md`
- `loom-playbooks/playbooks/loom-security-and-hardening/SKILL.md`
- `loom-playbooks/playbooks/loom-source-driven-development/SKILL.md`
- `loom-playbooks/playbooks/loom-test-driven-development/SKILL.md`
- `loom-playbooks/commands/*.toml` regenerated from source

Validation run:

- `node loom-playbooks.mjs --write-gemini-commands` wrote 25 command files.
- `npm --prefix loom-playbooks run smoke` passed.
- `npm --prefix loom-playbooks run pack:check` passed.
- `git diff --check` passed.
- Targeted grep over `loom-playbooks/playbooks`, `loom-playbooks/commands`, and `loom-playbooks/loom-playbooks.mjs` for `packet|packets|\.loom/packets|packet:` returned no matches.

Audit: `audit:20260515-ticket-owned-worker-handoffs` returned clear after follow-up and found no remaining Playbook issues. The generated command TOML files are not included in the current Playbooks npm tarball per existing package `files`, but they remain the adapter command surface requested by this ticket and are aligned with source. Unrelated historical `.loom/packets/ralph` worktree records are explicitly excluded from this ticket and were not created or modified for this migration.

## Journal

- 2026-05-15: Created from `plan:20260515-ticket-owned-worker-handoffs` as the Playbook language migration slice.
- 2026-05-15: Started implementation from this ticket and linked records. Preflight found existing unrelated workspace changes outside this ticket's write scope; this slice will leave those changes untouched.
- 2026-05-15: Replaced active packet wording in the shared Playbook macro preamble and targeted Playbooks for source-driven development, TDD, code review, frontend review, incremental implementation, git workspace isolation, intake triage, architecture, deprecation, security, debugging, branch finish, API/interface design, doubt-driven development, and parallel worker coordination. Regenerated command TOML from the Playbook source.
- 2026-05-15: Validation passed: Playbooks smoke, Playbooks pack dry-run, `git diff --check`, and targeted packet grep over Playbook source/commands/entrypoint. Moved ticket to `Status: review`; separate audit remains the next honest move before closure.
- 2026-05-15: Cited `evidence:20260515-ticket-owned-worker-handoffs-validation` and `audit:20260515-ticket-owned-worker-handoffs`; audit returned clear after follow-up. Closed with unrelated historical `.loom/packets/ralph` worktree records excluded from this migration.
