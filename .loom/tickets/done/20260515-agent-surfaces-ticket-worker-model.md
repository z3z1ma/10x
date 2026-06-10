# Agent Surfaces Ticket Worker Model

Status: done
Created: 2026-05-15
Updated: 2026-05-15

Legacy note: Risk — high - changes explicit agent persona prompts and adapter permissions for inner-loop coordination.

Priority: high - should follow Core doctrine migration so Driver and Weaver consume the new vocabulary.
Depends-On: .loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md

## Summary

Update Loom Driver, Loom Weaver, and adapter agent surfaces so explicit agents align with ticket-owned worker handoffs. The single closure claim is that agent prompts and Core OpenCode permissions no longer rely on packet compilation or `.loom/packets` as the execution boundary.

## Related Records

- `.loom/decisions/ticket-owned-worker-handoffs.md` - durable decision removing packets while preserving Ralph.
- `.loom/specs/ticket-owned-worker-handoffs.md` - target worker handoff behavior.
- `.loom/specs/loom-driver-agent.md` - updated Driver behavior contract.
- `.loom/specs/loom-weaver-agent.md` - updated Weaver behavior contract.
- `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` - parent plan.
- `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md` - prerequisite Core vocabulary migration.
- `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md` - validation dossier supporting closure.
- `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` - Ralph-backed audit covering this ticket and the parent migration.

## Scope

May change:

- `loom-core/agents/loom-driver.md`
- `loom-core/agents/loom-weaver.md`
- `loom-core/codex/agents/loom-driver.toml`
- `loom-core/codex/agents/loom-weaver.toml`
- `loom-core/loom-core.mjs` permission or smoke expectations tied to `.loom/packets/ralph/**`
- tests or smoke expectations directly tied to the agent permission surface
- this ticket and new evidence/audit records as needed

Must not change:

- Core skill doctrine beyond narrow corrections needed to consume the closed prerequisite
- Playbook macro bodies or generated command TOML
- human docs outside agent/permission validation scope
- historical `.loom/packets/**` records

## Acceptance

- ACC-001: Loom Driver model-visible instructions describe ticket-owned Ralph worker/review coordination, ticket state reconciliation, evidence, and audit routing without packet compilation, packet paths, or packet IDs.
  - Evidence: source inspection and targeted grep over canonical and Codex Driver agent files.
  - Audit: separate audit is expected because this changes the explicit inner-loop persona.

- ACC-002: Loom Weaver instructions remain outer-loop only without using `non-packet` as a live surface distinction. Weaver may create/update appropriate `.loom` records but must not launch worker/review runs or hide durable execution context in prompts.
  - Evidence: source inspection and targeted grep over canonical and Codex Weaver agent files.
  - Audit: included in the agent-surface audit pass.

- ACC-003: Core OpenCode permissions and smoke expectations no longer grant or assert `.loom/packets/ralph/**` write access for Driver as an active workflow requirement; permissions still allow the records Driver legitimately coordinates under the new model.
  - Evidence: source inspection of `loom-core/loom-core.mjs` and smoke output.
  - Audit: challenge whether permission changes accidentally prevent ticket/evidence/audit reconciliation.

- ACC-004: Agent prompts remain product-visible runtime behavior and do not leak contributor-only package process, smoke mechanics, dogfood assumptions, or adapter self-justification.
  - Evidence: targeted source inspection and grep for known leakage terms in agent prompts.
  - Audit: included in the agent-surface audit pass.

- ACC-005: Relevant checks pass.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check`, unless a command is skipped with a recorded reason.
  - Audit: audit reviews command evidence and skipped-command reasons.

## Current State

Closed. Updated canonical and Codex Loom Driver prompts so Driver coordinates ticket-owned Ralph worker/review runs from tickets and linked records, uses transient launch prompts, reconciles output into tickets/evidence/audit, and stops on stale ticket context or higher-authority ambiguity. Updated canonical and Codex Loom Weaver prompts so Weaver remains an outer-loop shaping agent, does not launch Ralph worker/review runs, and shapes ticket-owned durable context for later execution without `non-packet` framing.

Updated `loom-core/loom-core.mjs` so Driver OpenCode permissions and smoke expectations no longer include `.loom/packets/ralph/**`; Driver still allows `.loom/tickets/**`, `.loom/evidence/**`, and `.loom/audit/**` while denying direction-setting records. Validation passed: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check`. Targeted grep over `loom-core/agents`, `loom-core/codex/agents`, and `loom-core/loom-core.mjs` for `packet|packets|\.loom/packets|packet:` returned no matches. Product-surface leakage grep found only Weaver write-boundary wording for `package files` and `adapter files`, which is accepted as runtime write-scope language required by `.loom/specs/loom-weaver-agent.md`, not contributor process leakage.

Audit: `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` returned clear after follow-up and found no remaining agent-surface issues. Existing unrelated worktree changes from other tickets remain present and were not modified except where this ticket's allowed files overlap current package validation output. Unrelated historical `.loom/packets/ralph` worktree records are explicitly excluded from this ticket and were not created or modified for this migration.

## Journal

- 2026-05-15: Created from `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` as the agent-surface migration slice.
- 2026-05-15: Implemented agent-surface migration. Changed `loom-core/agents/loom-driver.md`, `loom-core/agents/loom-weaver.md`, `loom-core/codex/agents/loom-driver.toml`, `loom-core/codex/agents/loom-weaver.toml`, and `loom-core/loom-core.mjs`. Validation passed: Core smoke, Core pack check, `git diff --check`, and targeted packet grep over the touched Core agent/permission surfaces. Moved ticket to `Status: review`; separate audit remains the next honest move before closure.
- 2026-05-15: Cited `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md` and `.loom/reviews/20260515-ticket-owned-worker-handoffs.md`; audit returned clear after follow-up. Closed with unrelated historical `.loom/packets/ralph` worktree records excluded from this migration.
