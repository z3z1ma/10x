# Loom Protocol Compression

Status: done
Created: 2026-05-25
Updated: 2026-05-25

Legacy note: Risk — high - compresses core model-visible doctrine that controls routing, execution, evidence, audit, and future Loom behavior across adapters.

## Summary

This plan decomposes compression of the portable Loom protocol into ticket-ready slices. The outcome is a smaller skill and agent corpus that preserves Loom's behavior as a prose-first software factory protocol while removing repeated explanation, philosophy, and product-surface leakage.

This needs more than one ticket because session preload doctrine, record station skills, agent prompts, Playbook/doc restatements, and final validation have different write boundaries and closure stories.

## Related Records

- `.loom/decisions/project-constitution.md` - defines the protocol/Mill split and the principle that skills should be operational kernels.
- `roadmap:loom-mill` - identifies protocol compression as the foundation chapter before Loom Mill.
- `.loom/research/20260524-loom-mill-software-factory.md` - records why the protocol is conceptually correct but too verbose.
- `.loom/specs/loom-protocol-compression.md` - behavior contract this plan implements.
- `.loom/specs/ticket-owned-worker-handoffs.md` - worker handoff behavior that compression must preserve.
- `.loom/specs/loom-driver-agent.md` - Driver prompt behavior that compression must preserve.
- `.loom/specs/loom-weaver-agent.md` - Weaver prompt behavior that compression must preserve.
- `AGENTS.md` - contributor constraints for product-surface leakage and validation commands.

## Strategy

Use a contract-first route. The compression spec is the shared quality bar. First lock the model-visible inventory and baseline so later tickets can prove they compressed the right surfaces. Then compress the session kernel because `using-loom` and its preload references have the largest context impact and drive all later routing. After that, compress the record skills into station kernels, then align Driver/Weaver prompts with Design Office and Factory Floor roles, then align Playbooks and public docs that restate Core behavior.

Validation runs last because it needs the full compressed surface: package smoke/pack checks, Markdown diff checks, targeted behavior/leakage searches, and fresh-context audit. Replan if compression reveals behavior that cannot be safely shortened, if active specs contradict the compression contract, or if adapter preload surfaces cannot stay aligned with the new session kernel.

Compression is behavior-first. Each execution ticket should record before/after line counts, but no ticket should delete a guardrail merely to satisfy a numeric target.

## Execution Units

### Unit: Compression Contract And Inventory

Ticket: .loom/tickets/done/20260525-compression-contract-inventory.md

Establish the shared compression contract and model-visible inventory. The ticket should confirm `.loom/specs/loom-protocol-compression.md`, capture the baseline size of Core skills, references, agents, Playbooks, generated commands, and docs that expose protocol behavior, and update this plan if the inventory changes the route.

Likely scope boundary: `.loom/specs/loom-protocol-compression.md`, this plan, inventory notes in the ticket or evidence, and read-only inspection of model-visible source surfaces.

Order reason: all later tickets need the same compression quality bar and baseline.

Validation: source inventory, before line counts, targeted surface list, and `git diff --check` for record changes.

Stop condition: return to shaping if the compression contract conflicts with active specs or constitution records.

### Unit: Session Kernel Compression

Ticket: .loom/tickets/done/20260525-session-kernel-compression.md

Compress `using-loom` and its ordered references into the smallest complete session kernel while preserving activation discipline, loop order, surface ownership, shaping, ticket-owned Ralph handoff, evidence, audit, safety, and active knowledge loading.

Likely scope boundary: `loom-core/skills/using-loom/**`, Core preload surfaces such as `loom-core/loom-core.mjs`, `loom-core/hooks/*`, `loom-core/gemini-bootstrap.md`, and docs only when they directly restate startup doctrine.

Order reason: session doctrine constrains every other skill and adapter preload.

Validation: before/after line counts, source inspection, Core smoke/pack, targeted searches for activation and preload alignment, and `git diff --check`.

Stop condition: block if the session kernel cannot stay complete without retaining a reference topology that needs operator approval.

### Unit: Record Skill Kernels

Ticket: .loom/tickets/done/20260525-record-skill-kernels.md

Compress Core record skills and references into station kernels while preserving each surface's owner truth, lifecycle, record shape, stop conditions, and evidence/audit posture.

Likely scope boundary: `loom-core/skills/loom-constitution/**`, `loom-core/skills/loom-specs/**`, `loom-core/skills/loom-plans/**`, `loom-core/skills/loom-tickets/**`, `loom-core/skills/loom-research/**`, `loom-core/skills/loom-evidence/**`, `loom-core/skills/loom-audit/**`, `loom-core/skills/loom-knowledge/**`, `loom-core/skills/loom-retrospective/**`, `loom-core/skills/loom-ralph/**`, and templates only when compression requires alignment.

Order reason: depends on the session kernel vocabulary and compression contract.

Validation: before/after line counts, source inspection for required station content, Core smoke/pack, targeted searches for behavior loss and leakage, and `git diff --check`.

Stop condition: split the ticket if one skill family reveals independent behavior changes rather than compression.

### Unit: Agent Prompt Kernels

Ticket: .loom/tickets/done/20260525-agent-prompt-kernels.md

Compress Driver and Weaver prompts around factory roles: Weaver as Design Office, Driver as Factory Floor coordinator. Remove duplicated skill doctrine while preserving write boundaries, routing, evidence, audit, and worker-output reconciliation.

Likely scope boundary: `loom-core/agents/**`, `loom-core/codex/agents/**`, `.loom/specs/loom-driver-agent.md`, `.loom/specs/loom-weaver-agent.md`, and adapter-facing docs only when they directly restate agent behavior.

Order reason: agent prompts should consume the compressed Core vocabulary rather than define a second protocol.

Validation: before/after line counts, source inspection against agent specs, Core smoke/pack if agent surfaces affect package output, targeted searches for doctrine duplication and leakage, and `git diff --check`.

Stop condition: return to specs if factory-role alignment changes intended Driver or Weaver behavior rather than prompt wording.

### Unit: Playbook And Doc Alignment

Ticket: .loom/tickets/done/20260525-playbook-doc-compression-alignment.md

Align optional Playbooks, generated command surfaces, and human docs with the compressed Core protocol without making Playbooks a second source of doctrine.

Likely scope boundary: `loom-playbooks/playbooks/**`, `loom-playbooks/commands/*.toml`, `loom-playbooks/loom-playbooks.mjs` only if generation output changes, root/package docs such as `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, package READMEs, and tests only when directly tied to exposed protocol language.

Order reason: docs and Playbooks should restate the settled Core compression rather than drive it.

Validation: Playbooks smoke/pack, targeted generated-command comparison, targeted grep for old verbose doctrine and leakage, and `git diff --check`.

Stop condition: block if aligning docs would require changing protocol behavior beyond the compression spec.

### Unit: Validation, Evidence, And Audit

Ticket: .loom/tickets/done/20260525-compression-validation-audit.md

Run final validation and fresh-context audit over the compressed protocol. Preserve evidence, fix or route findings, update this plan, and move the plan toward completion only when the graph supports the claim.

Likely scope boundary: `.loom/evidence/**`, `.loom/audit/**`, this plan, child ticket state, and small source fixes only if validation exposes direct compression regressions within previous-ticket scope.

Order reason: closure depends on all compression slices being implemented.

Validation: Core smoke, Core pack check, Playbooks smoke/pack where touched, `git diff --check`, targeted behavior/leakage searches, and Ralph-backed audit.

Stop condition: route back to the responsible ticket if audit finds behavior loss, unsupported closure claims, or product-surface leakage.

## Milestones

### Milestone: Compression Contract Ready

Child tickets: .loom/tickets/done/20260525-compression-contract-inventory.md

The compression spec, inventory, and baseline are available for all downstream tickets.

### Milestone: Core Kernel Compressed

Child tickets: .loom/tickets/done/20260525-session-kernel-compression.md, .loom/tickets/done/20260525-record-skill-kernels.md

The Core protocol surfaces are smaller operational kernels and still preserve routing, handoff, evidence, audit, and safety behavior.

### Milestone: Consumer Surfaces Aligned

Child tickets: .loom/tickets/done/20260525-agent-prompt-kernels.md, .loom/tickets/done/20260525-playbook-doc-compression-alignment.md

Agent prompts, Playbooks, generated command surfaces, and docs consume the compressed Core protocol without becoming parallel doctrine.

### Milestone: Proof And Review Complete

Child tickets: .loom/tickets/done/20260525-compression-validation-audit.md

Validation evidence and fresh-context audit support the compression closure claim.

## Current State

Completed. All child tickets are closed: inventory, session kernel, record skill kernels, agent prompt kernels, Playbook/doc alignment, and final validation/audit. Final evidence is recorded at `.loom/evidence/20260525-protocol-compression-final-validation.md`; final audit is recorded at `.loom/reviews/20260525-protocol-compression-final-audit.md` with a clear verdict and no material findings. The compression reduced the baseline inventory-category corpus from 18,000 to 14,617 lines across the same 132-file category set while preserving required protocol behaviors within the validated source/record scope. Residual risks remain explicit: live harness/model behavior was not exhaustively simulated, targeted leakage searches are not semantic proof, and Playbook explicit-only behavior was statically validated rather than live natural-prompt tested.

## Journal

- 2026-05-25: Created plan from `.loom/decisions/project-constitution.md`, `roadmap:loom-mill`, `.loom/research/20260524-loom-mill-software-factory.md`, and `.loom/specs/loom-protocol-compression.md` with six child execution units.
- 2026-05-25: Closed inventory baseline ticket and activated session-kernel compression.
- 2026-05-25: Closed session-kernel compression after validation and audit; activated record skill kernels.
- 2026-05-25: Closed record skill kernels after three bounded compression runs, validation evidence, and audit; activated agent prompt kernels.
- 2026-05-25: Closed agent prompt kernels after validation and audit; activated Playbook/doc compression alignment.
- 2026-05-25: Closed Playbook/doc compression alignment after validation and audit; activated final validation/audit.
- 2026-05-25: Completed final validation and audit. Evidence `.loom/evidence/20260525-protocol-compression-final-validation.md` records required command results, final line counts, scoped diff, behavior/leakage searches, generated command sync, and agent alignment checks. Audit `.loom/reviews/20260525-protocol-compression-final-audit.md` records a clear verdict with no material findings. Marked plan completed with residual risks explicit.
