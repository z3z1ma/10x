# Agent Prompt Kernels

ID: ticket:20260525-agent-prompt-kernels
Type: Ticket
Status: closed
Created: 2026-05-25
Updated: 2026-05-25
Risk: medium - changes model-visible Driver and Weaver prompts plus adapter copies, but should preserve accepted behavior.
Priority: medium - aligns explicit agents after Core compression.
Depends On: ticket:20260525-record-skill-kernels

## Summary

Compress Loom Driver and Loom Weaver prompts around their factory roles. The closure claim is that Weaver remains the Design Office and Driver remains the Factory Floor coordinator while duplicated skill doctrine is removed and adapter copies stay aligned.

## Related Records

- `plan:20260525-loom-protocol-compression` - owns sequencing and validation posture.
- `spec:loom-protocol-compression` - defines agent prompt compression in REQ-006.
- `constitution:main` - defines the factory role mapping.
- `spec:loom-driver-agent` - behavior contract for Driver.
- `spec:loom-weaver-agent` - behavior contract for Weaver.
- `ticket:20260525-record-skill-kernels` - provides compressed Core skill vocabulary.
- `AGENTS.md` - product-surface leakage and validation constraints.

## Scope

May change `loom-core/agents/loom-driver.md`, `loom-core/agents/loom-weaver.md`, adapter-specific copies under `loom-core/codex/agents/**`, and the Driver/Weaver specs if their accepted behavior needs wording alignment with the factory framing.

May update package smoke expectations if agent surfaces affect generated or packed output. Do not compress record skills, Playbooks, or broad docs in this ticket.

First Ralph boundary: compare prompts against their specs and the compressed Core skills, remove duplicated doctrine, add factory-role language where it clarifies behavior, align adapter copies, then validate package output.

Stop if factory-role wording would change Weaver or Driver authority, write scope, or execution behavior rather than compressing prompt instructions.

## Acceptance

- ACC-001: Weaver prompt is a concise Design Office instruction: shape records, challenge ambiguity, write only under `.loom/`, and do not launch worker or review runs.
  - Evidence: Source inspection against `spec:loom-weaver-agent` and `constitution:main`.
  - Audit: Fresh-context final audit should challenge authority or write-scope drift.

- ACC-002: Driver prompt is a concise Factory Floor coordinator instruction: start from shaped graph state, coordinate ticket-owned Ralph runs, reconcile output, preserve evidence, route audit, and stop for blockers or higher-authority ambiguity.
  - Evidence: Source inspection against `spec:loom-driver-agent` and `spec:ticket-owned-worker-handoffs`.
  - Audit: Fresh-context final audit should challenge execution and proof loss.

- ACC-003: Canonical and adapter-specific agent surfaces are aligned and do not duplicate full Core skill doctrine.
  - Evidence: Source inspection of `loom-core/agents/**` and `loom-core/codex/agents/**`, plus before/after line counts.
  - Audit: Review should challenge stale adapter copies and hidden second doctrine.

- ACC-004: Product-surface leakage is not introduced.
  - Evidence: Targeted grep/source inspection for package smoke, adapter self-justification, dogfood assumptions, and repository workflow language.
  - Audit: Final audit should inspect leakage search limits.

- ACC-005: Relevant package validation passes.
  - Evidence: Core smoke/pack when touched plus `git diff --check` outputs recorded or cited.
  - Audit: Final audit should inspect evidence sufficiency.

## Current State

Closed. Driver and Weaver prompts were compressed around Factory Floor and Design Office roles, with canonical Markdown and Codex TOML prompt bodies aligned. Evidence is recorded at `evidence:20260525-agent-prompt-kernels-validation`. Fresh-context audit is recorded at `audit:20260525-agent-prompt-kernels-audit` with a pass verdict and no material findings. Residual risk is limited to live model behavior not being tested in a fresh harness session, Playbooks being out of scope for this ticket, and unrelated compression-ticket changes not being inspected by this ticket.

Files changed in this run:

- `loom-core/agents/loom-driver.md`
- `loom-core/agents/loom-weaver.md`
- `loom-core/codex/agents/loom-driver.toml`
- `loom-core/codex/agents/loom-weaver.toml`
- `.loom/evidence/20260525-agent-prompt-kernels-validation.md`
- `.loom/tickets/20260525-agent-prompt-kernels.md`

Validation passed: before/after line counts, canonical/Codex prompt-body alignment check, `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `git diff --check`, targeted source inspection for Driver/Weaver role and behavior guardrails, and targeted product-surface leakage search. An initial smoke/pack attempt failed because compressed wording dropped exact smoke-checked phrases for Weaver's write boundary and Driver's direction-record boundary; the prompts were tightened to retain those guardrails, then validation passed.

## Journal

- 2026-05-25: Created ticket with dependency on record skill compression.
- 2026-05-25: Set status to `active` after record skill compression closed.
- 2026-05-25: Bounded agent-prompt run compressed Driver and Weaver prompt surfaces around Factory Floor and Design Office roles. Line count changed from 890 to 372 total lines across canonical Markdown and Codex TOML agent files. Canonical/Codex prompt bodies are aligned. Validation passed: Core smoke, Core pack check, `git diff --check`, targeted role/guardrail source inspection, and product-surface leakage search. Evidence recorded at `evidence:20260525-agent-prompt-kernels-validation`; ticket moved to `review` pending fresh-context audit.
- 2026-05-25: Fresh-context audit recorded at `audit:20260525-agent-prompt-kernels-audit`. Verdict: pass, with no material findings. Residual risk is limited to live model behavior not being tested in a fresh harness session, Playbooks being out of scope, and unrelated dirty worktree changes from other compression tickets not being inspected.
- 2026-05-25: Coordinator closed ticket. ACC-001 through ACC-005 are supported by validation evidence and fresh-context audit; no source follow-up required by audit.
