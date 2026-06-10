# Ticket-Owned Worker Handoffs

Status: done
Created: 2026-05-15
Updated: 2026-05-15

Legacy note: Risk — high - removes an active Core execution surface and changes worker, audit, agent, Playbook, adapter, and documentation semantics.

## Summary

`.loom/decisions/ticket-owned-worker-handoffs.md` now removes packets as a future Loom surface.

## Related Records

`.loom/decisions/ticket-owned-worker-handoffs.md` - durable product judgment that packets are retired as an active surface and Ralph remains.
- `.loom/specs/ticket-owned-worker-handoffs.md` - behavior contract for ticket-owned worker and audit handoffs.
- `.loom/specs/loom-driver-agent.md` - Driver behavior must coordinate ticket-owned Ralph runs instead of packetized execution.
- `.loom/specs/loom-weaver-agent.md` - Weaver remains outer-loop only and should no longer be framed around non-packet records.
- `.loom/specs/playbook-explicit-macros.md` - Playbook macro bodies must preserve ticket-owned worker/audit discipline.
- `.loom/research/20260510-loom-loop-failure-analysis.md` - historical context for why packet-before-worker doctrine existed.
`.loom/tickets/done/20260513-ticket-execution-ralph-language.md` - historical prior direction now superseded by `.loom/decisions/ticket-owned-worker-handoffs.md`.
`.loom/tickets/done/20260513-ralph-language-consolidation.md` - historical prior direction now superseded by `.loom/decisions/ticket-owned-worker-handoffs.md`.

## Strategy

Use a contract-first migration. The constitution decision and spec define the new model before source edits begin. The first execution unit updates Core doctrine and record skills because every other surface should inherit the new ticket-owned semantics from Core. Agent surfaces then update Driver/Weaver prompts and adapter permissions to stop treating `.loom/packets` as the execution write boundary. Playbooks update afterward so optional workflow lenses preserve Core's new model. Human-facing docs and validation run last to catch stale public explanations and generated-command drift.

This plan deliberately leaves historical `.loom/packets` records alone. Existing tickets, evidence, and audit records may cite packet history; the migration target is active product doctrine and current documentation, not historical rewrite.

Source inspection found packet language in Core skills, Driver/Weaver agent prompts, Codex agent TOML, Playbook macro bodies, generated command TOML, human docs, and OpenCode Core permissions. That breadth is why this is a plan rather than one ticket.

Downstream tickets should inherit these validation expectations:

- target grep for active packet-creation instructions outside historical `.loom` records;
- source inspection proving ticket-owned context replaces packet-owned context;
- Core and Playbooks smoke/pack checks where touched;
- `git diff --check` for Markdown-heavy edits;
- adapter validation only where adapter manifests or bootstrap files change.

Replan if implementation discovers that a supported harness requires `.loom/packets` permissions for unrelated behavior, if ticket templates cannot absorb worker context without becoming unusably broad, or if removing packet wording would also require retiring Ralph rather than preserving it.

## Execution Units

### 1. Core Doctrine And Record Skills

- Child ticket: `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md`
- Outcome: Core skills, references, templates, and directory doctrine stop defining packets as an active surface and make tickets the durable worker/audit execution contract while preserving Ralph as bounded discipline.
- Likely scope boundary: `loom-core/skills/**`, especially `using-loom`, `loom-tickets`, `loom-plans`, `loom-audit`, `loom-ralph`, `loom-evidence`, `loom-retrospective`, templates, and references.
- Order reason: all other surfaces should consume Core semantics instead of inventing their own wording.
- Validation: targeted grep/source inspection over Core skills plus Core smoke/pack where package behavior or packaged files are touched.
- Stop condition: return to shaping if `loom-ralph` cannot remain a meaningful skill without packet records.

### 2. Driver, Weaver, And Adapter Agent Surfaces

- Child ticket: `.loom/tickets/done/20260515-agent-surfaces-ticket-worker-model.md`
- Outcome: Loom Driver coordinates ticket-owned Ralph runs instead of packet compilation; Loom Weaver no longer frames its boundary around non-packet records; adapter agent prompts and Core OpenCode permissions align.
- Likely scope boundary: `loom-core/agents/**`, `loom-core/codex/agents/**`, `loom-core/loom-core.mjs`, and any smoke output expectations tied to Driver permissions.
- Order reason: depends on the Core doctrine vocabulary from unit 1.
- Validation: source inspection of agent prompts and permission checks, Core smoke/pack, and targeted grep for packet-only write boundaries in agent surfaces.
- Stop condition: return to shaping if Driver's role becomes direct implementation instead of coordination.

### 3. Playbook Macro Language And Generated Commands

- Child ticket: `.loom/tickets/done/20260515-playbook-ticket-worker-language.md`
- Outcome: Playbook workflow lenses preserve ticket-owned worker/audit discipline and no longer instruct agents to compile Ralph packets or coordinate by packet IDs.
- Likely scope boundary: `loom-playbooks/playbooks/**`, `loom-playbooks/commands/*.toml`, `loom-playbooks/loom-playbooks.mjs`, and generated-command alignment checks.
- Order reason: Playbooks should mirror Core and agent semantics after units 1 and 2 settle the vocabulary.
- Validation: targeted grep/source inspection over Playbook source and generated command surfaces, Playbooks smoke/pack, and `git diff --check`.
- Stop condition: return to shaping if any Playbook truly needs a durable record separate from tickets, evidence, or audit.

### 4. Human Docs And Final Validation

- Child ticket: `.loom/tickets/done/20260515-docs-validation-no-packets.md`
- Outcome: Human-facing docs, installer examples, architecture explanations, and tests no longer present packets as an active Loom surface; final validation proves active product surfaces align.
- Likely scope boundary: root/package READMEs, `INSTALL.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, relevant tests or smoke snapshots, and documentation-only generated artifacts.
- Order reason: docs should restate the source behavior after Core, agent, and Playbook surfaces have changed.
- Validation: targeted grep excluding historical `.loom` records, Core and Playbooks smoke/pack, applicable adapter validations for changed manifests/bootstrap, and `git diff --check`.
- Stop condition: return to shaping if public docs need to teach a compatibility story for historical packets beyond a short deprecation note.

## Milestones

- Core model migrated: `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md` is closed or in review with evidence that Core no longer creates packet records.
- Agent and workflow surfaces aligned: Driver/Weaver and Playbooks no longer teach packet compilation or packet coordination.
- Public surface coherent: human docs and validation checks show active product doctrine has no future packet surface while historical `.loom` records remain untouched.

## Current State

Completed. All four child tickets are closed: `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md`, `.loom/tickets/done/20260515-agent-surfaces-ticket-worker-model.md`, `.loom/tickets/done/20260515-playbook-ticket-worker-language.md`, and `.loom/tickets/done/20260515-docs-validation-no-packets.md`. Core doctrine, agent surfaces, Playbook language, generated command surfaces, human-facing docs, tests, and eval docs now describe ticket-owned Ralph worker/review discipline instead of packet-owned handoffs or future `.loom/packets` creation.

Validation passed for the full migration: Core smoke, Core pack check, Playbooks smoke, Playbooks pack check, `git diff --check`, and targeted active-surface searches found no packet terminology in shipped Core skills, Core agents, Codex agents, Playbook source/commands, current docs, tests, or eval surfaces outside historical `.loom` records. `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` returned clear after follow-up; its initial malformed Ralph invariant finding was fixed and revalidated.

Unrelated historical `.loom/packets/ralph` worktree records are explicitly excluded from this migration. They are out of scope under `.loom/decisions/ticket-owned-worker-handoffs.md`, were not created by this migration, and do not block completion because active product surfaces no longer teach packets as a future Loom surface.

## Journal

- 2026-05-15: Created plan after operator selected the option to retire packets while preserving Ralph as ticket-owned worker/audit discipline. Created four child tickets for Core doctrine, agent surfaces, Playbook language, and docs/final validation.
- 2026-05-15: Completed plan after all four child tickets closed, shared validation passed, and `.loom/reviews/20260515-ticket-owned-worker-handoffs.md` returned clear after follow-up. Closure explicitly excludes unrelated historical `.loom/packets/ralph` worktree records as out of scope under `.loom/decisions/ticket-owned-worker-handoffs.md`; this migration did not create those records.
