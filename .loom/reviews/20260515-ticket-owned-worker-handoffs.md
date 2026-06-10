# Ticket-Owned Worker Handoffs Audit

Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Target: .loom/tickets/20260515-ticket-owned-worker-handoffs.md

## Summary

Two bounded Ralph review runs challenged the migration from packet-owned handoffs to ticket-owned worker/review runs. The first review found one Core wording defect and one graph-disposition concern. The wording defect was fixed, validation was rerun, and the follow-up review returned `clear` with no material findings. The remaining condition is closure-record disposition of unrelated historical `.loom/packets/ralph` worktree records.

## Target

The audit targeted:

- `.loom/tickets/20260515-ticket-owned-worker-handoffs.md`
- `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md`
- `.loom/tickets/done/20260515-agent-surfaces-ticket-worker-model.md`
- `.loom/tickets/done/20260515-playbook-ticket-worker-language.md`
- `.loom/tickets/done/20260515-docs-validation-no-packets.md`
- `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md`
- `.loom/specs/ticket-owned-worker-handoffs.md`
- current source/docs/test diffs implementing the migration

## Audit Scope And Lenses

Review lenses:

- stale packet instruction leakage
- concept coherence: no packets, but Ralph remains bounded
- ticket-owned durable context versus prompt-only context
- Driver/Weaver role boundaries
- Playbook explicit invocation preservation
- evidence sufficiency and overclaiming
- product-surface leakage risk
- scope drift or unrelated changes

## Context And Evidence Reviewed

The reviews inspected the plan, four child tickets, decision, spec, current git diff, Core skill corpus, Core agent prompts, Codex agent TOML, OpenCode Core entrypoint permissions, Playbook source bodies, generated Playbook command TOML, human-facing docs, tests, and eval docs.

The follow-up review inspected `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md`, which records:

- `npm --prefix loom-core run smoke` passed.
- `npm --prefix loom-core run pack:check` passed.
- `npm --prefix loom-playbooks run smoke` passed.
- `npm --prefix loom-playbooks run pack:check` passed.
- `git diff --check` passed.
- targeted searches found no packet terminology in active Core skills, Core agents, Codex agents, Playbook source/commands, current docs, tests, or eval surfaces outside historical `.loom` records.

The follow-up review independently reran or relied on the same checks and reported:

- active non-`.loom` product/docs/test surfaces had no packet-term matches;
- targeted Core and Playbooks Markdown/TOML searches had no matches;
- `git diff --check` passed;
- Core and Playbooks smoke and pack checks passed.

## Findings

### FIND-001: Malformed Core Ralph invariant weakened worker permission wording — resolved

The first review found that `loom-core/skills/loom-ralph/SKILL.md` split one invariant into two bullets, leaving `by the ticket, owning surface, or launch` as a nonsensical standalone bullet. That weakened the active Core worker boundary wording.

Disposition: fixed before this audit was recorded. A follow-up worker corrected the bullet, reran `git diff --check` and `npm --prefix loom-core run smoke`, and the final review confirmed `loom-core/skills/loom-ralph/SKILL.md:106-124` now has a well-formed invariant list.

### FIND-002: Packet records remain in the worktree and require explicit closure disposition — condition satisfied by ticket/plan closure notes

The first review found a modified historical packet and two untracked packet records under `.loom/packets/ralph/` related to earlier `playbook-explicit-macro-docs-tests` work. These records were not created by this migration and are not active product doctrine, but closing the migration without naming that exclusion would weaken graph coherence.

Disposition required: migration closure records must explicitly state that historical/current `.loom/packets/ralph` worktree records are unrelated to this migration, remain outside active product-surface validation, and are allowed as historical/out-of-scope artifacts under `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md`.

The follow-up review accepted that disposition condition and reported that the `.loom/packets/ralph` changes do not block this migration if closure records include the exclusion.

## Verdict

Clear after follow-up.

The active product-surface migration is supported: Core doctrine, ticket/Ralph/audit guidance, Driver/Weaver prompts and permissions, Playbook source and generated commands, human-facing docs, tests, and eval docs no longer teach future packet creation or `.loom/packets` as an active surface. Ralph remains as ticket-owned bounded worker/review discipline, and validation evidence is sufficient for closure consideration.

## Required Follow-up

- Closure records for the four child tickets and parent plan should explicitly mention the `.loom/packets/ralph` exclusion from `FIND-002`.
- No source follow-up is required by this audit.

## Residual Risk

- Historical `.loom/packets/ralph` records still exist, including unrelated untracked records already present in the worktree. Future readers could misread them unless they follow `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md` and the closure notes.
- Validation proves current source/package surfaces and package smoke behavior, not every external installed harness runtime beyond those checks.

## Related Records

- `.loom/evidence/20260515-ticket-owned-worker-handoffs-validation.md` - validation dossier reviewed by the follow-up audit.
- `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md` - active decision retiring packets as future active surface while preserving Ralph.
- `.loom/specs/ticket-owned-worker-handoffs.md` - behavior contract audited here.
- `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` - parent migration plan.
