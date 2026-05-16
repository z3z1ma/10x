# Core Ticket-Owned Worker Doctrine

ID: ticket:20260515-core-ticket-owned-worker-doctrine
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: high - changes Core loop doctrine, record skill procedures, templates, and the meaning of Ralph worker/audit handoffs.
Priority: high - this ticket establishes the vocabulary required by the downstream agent, Playbook, and docs tickets.

## Summary

Update Core Loom skills and references so packets are no longer an active surface. The single closure claim is that Core doctrine teaches ticket-owned worker and audit handoffs: tickets and linked records hold durable context, Ralph remains the bounded worker/review discipline, and future Core guidance does not create `.loom/packets` records.

## Related Records

- `decision:0002` - durable decision removing packets while preserving Ralph.
- `spec:ticket-owned-worker-handoffs` - target behavior for ticket-owned worker and audit handoffs.
- `plan:20260515-ticket-owned-worker-handoffs` - parent plan and sequencing.
- `research:20260510-loom-loop-failure-analysis` - historical failure mode this migration must not reintroduce.
- `evidence:20260515-ticket-owned-worker-handoffs-validation` - validation dossier supporting closure.
- `audit:20260515-ticket-owned-worker-handoffs` - Ralph-backed audit covering this ticket and the parent migration.

## Scope

May change:

- `loom-core/skills/using-loom/**`
- `loom-core/skills/loom-tickets/**`
- `loom-core/skills/loom-plans/**`
- `loom-core/skills/loom-audit/**`
- `loom-core/skills/loom-ralph/**`
- `loom-core/skills/loom-evidence/**`
- `loom-core/skills/loom-retrospective/**`
- Core skill templates and references that mention packets, packet directories, packet IDs, or packet output
- this ticket and new evidence/audit records as needed

Must not change:

- `loom-core/agents/**`, Codex agent TOML, Playbooks, human docs, or adapter permissions except to note follow-up blockers; those are separate child tickets
- historical `.loom/packets/**` records or historical tickets/audits that cite packets
- product behavior unrelated to worker/audit handoff semantics

Durable worker context that previously lived in packets should move into ticket shape only when it is needed for future recovery: related records, likely read scope, likely write scope, constraints, stop conditions, evidence posture, audit posture, and expected worker-output reconciliation.

## Acceptance

- ACC-001: Core `using-loom` doctrine and references no longer list packets as a Loom surface, canonical directory, or required worker contract for future work.
  - Evidence: source inspection and targeted grep over `loom-core/skills/using-loom/**` for `packet`, `packets`, `.loom/packets`, and `packet:` after edits, with historical references excluded only when explicitly labeled historical/deprecated.
  - Audit: separate audit is expected because this changes Core loop behavior.

- ACC-002: `loom-tickets` guidance and templates make tickets the durable execution contract for bounded worker/review runs, including related records, read/write boundaries, stop conditions, evidence posture, audit posture, and worker-output reconciliation.
  - Evidence: source inspection of `loom-core/skills/loom-tickets/**` after edits.
  - Audit: challenge whether tickets became too bloated or still leave durable context in transient prompts.

- ACC-003: `loom-ralph` and `loom-audit` guidance preserve Ralph as bounded worker/review discipline without requiring packet files, packet IDs, or `.loom/packets/ralph/` paths.
  - Evidence: source inspection of `loom-core/skills/loom-ralph/**` and `loom-core/skills/loom-audit/**` after edits.
  - Audit: challenge whether Ralph remains clear rather than generic sub-agent prompting.

- ACC-004: Plans, evidence, retrospective, and related Core references no longer make packet output or packet requirements a current active dependency; worker output needed for trust is reconciled into tickets, evidence, audit, or knowledge as appropriate.
  - Evidence: targeted grep/source inspection over Core skills after edits.
  - Audit: included in the Core audit pass.

- ACC-005: Core package checks that are relevant to skill corpus changes pass.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check`, unless a command is skipped with a recorded reason.
  - Audit: audit reviews the command evidence and skipped-command reasons.

## Current State

Closed. Core skill corpus edits are complete. Updated `using-loom`, `loom-tickets`, `loom-ralph`, `loom-audit`, `loom-plans`, `loom-specs`, and `loom-retrospective` so active doctrine uses tickets and linked records as durable worker/review context while Ralph remains the bounded run discipline. Deleted obsolete `loom-ralph` packet reference/template files and added `run-shape.md` plus `running-ralph.md`.

Validation run:

- `npm --prefix loom-core run smoke` passed.
- `npm --prefix loom-core run pack:check` passed.
- `git diff --check` passed.
- Targeted grep over `loom-core/skills` for `packet|packets|\.loom/packets|packet:` returned no matches.

Audit: `audit:20260515-ticket-owned-worker-handoffs` initially found a malformed `loom-ralph` invariant; the finding was fixed and the follow-up review returned clear. The audit accepted the explicit exclusion of unrelated historical `.loom/packets/ralph` worktree records from this migration closure. Residual risk is limited to external installed harness behavior beyond smoke/pack checks and historical packet records that remain by design under `decision:0002`.

## Journal

- 2026-05-15: Created from `plan:20260515-ticket-owned-worker-handoffs` as the first source-changing slice for retiring packets from Core doctrine.
- 2026-05-15: Implemented Core skill-corpus migration from packet-owned handoffs to ticket-owned Ralph runs. Changed `using-loom` doctrine/references; `loom-tickets` skill, references, and template; `loom-ralph` skill and references; `loom-audit` skill, reference, and template; `loom-plans`, `loom-specs`, and `loom-retrospective` packet references. Deleted obsolete `loom-ralph` packet reference/template files and added Ralph run reference files.
- 2026-05-15: Validation passed: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `git diff --check`, and targeted grep over `loom-core/skills` for `packet|packets|\.loom/packets|packet:`. Moved ticket to `Status: review`; separate audit remains the next honest move before closure.
- 2026-05-15: Recorded `evidence:20260515-ticket-owned-worker-handoffs-validation` and `audit:20260515-ticket-owned-worker-handoffs`. Fixed audit finding for malformed Ralph invariant, reran validation, and closed. Unrelated historical `.loom/packets/ralph` worktree records are explicitly excluded from this ticket and were not created or modified for this migration.
