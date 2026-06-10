# Agent Prompt Kernels Audit

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Target: .loom/tickets/done/20260525-agent-prompt-kernels.md

## Summary

Fresh-context adversarial review inspected the Driver and Weaver prompt compression against the ticket acceptance criteria, agent specs, compression contract, evidence dossier, scoped source diff, and validation output. No material findings were identified within this audit scope; the evidence supports ticket closure if the ticket records this audit and residual risk honestly.

## Target

This audit targets `.loom/tickets/done/20260525-agent-prompt-kernels.md`, which compresses Loom Driver and Loom Weaver prompt surfaces around the Factory Floor and Design Office roles while preserving accepted behavior, canonical/Codex alignment, product-surface hygiene, and validation evidence.

Reviewed source targets:

- `loom-core/agents/loom-driver.md`
- `loom-core/agents/loom-weaver.md`
- `loom-core/codex/agents/loom-driver.toml`
- `loom-core/codex/agents/loom-weaver.toml`

## Audit Scope And Lenses

Scope was limited to the ticket's Driver/Weaver prompt compression closure claim, evidence strength, and scoped source diff. Lenses used: acceptance, behavior preservation, canonical/adapter alignment, product-surface leakage, evidence sufficiency, surface boundary, and follow-through.

Specific review questions:

- Does Weaver remain the Design Office: shaping-first, constructively adversarial, `.loom/` only write boundary, no Ralph worker or review launch, and handoff through owning records?
- Does Driver remain the Factory Floor coordinator: graph-supported execution, ticket-owned Ralph runs, worker-output reconciliation, evidence, audit, truthful closure, and read-only direction-setting records?
- Do canonical Markdown and Codex TOML prompt bodies remain aligned?
- Did compression avoid duplicating full Core doctrine and avoid contributor-facing product-surface leakage?
- Does evidence support the line-count, validation, alignment, and leakage claims used for closure?

Out of scope: live model behavior in a fresh harness session, Playbooks validation, unrelated dirty worktree changes from other compression tickets, and final plan-level compression closure.

## Context And Evidence Reviewed

- Ralph review run: direct fresh-context audit as a `general` worker per operator transport constraint; reviewed the ticket, linked records, scoped diff, prompt source files, and validation outputs.
- `.loom/tickets/done/20260525-agent-prompt-kernels.md` - ticket scope, acceptance criteria, current state, evidence link, and closure posture.
- `.loom/evidence/20260525-agent-prompt-kernels-validation.md` - validation dossier and claimed observations.
- `.loom/specs/loom-protocol-compression.md` - REQ-006, REQ-008, REQ-009, and compression quality bar.
- `.loom/specs/loom-driver-agent.md` - Driver behavior contract and validation expectations.
- `.loom/specs/loom-weaver-agent.md` - Weaver behavior contract and validation expectations.
- `.loom/decisions/project-constitution.md` - Design Office / Factory Floor role mapping and product-surface hygiene constraints.
- `.loom/tickets/20260525-loom-protocol-compression.md` - sequencing, validation posture, and agent prompt unit scope.
- `AGENTS.md` - repository constraints for shipped product surfaces, leakage scanning, and validation commands.
- `git diff -- loom-core/agents/loom-driver.md loom-core/agents/loom-weaver.md loom-core/codex/agents/loom-driver.toml loom-core/codex/agents/loom-weaver.toml` - scoped source diff inspected.
- `wc -l loom-core/agents/loom-driver.md loom-core/agents/loom-weaver.md loom-core/codex/agents/loom-driver.toml loom-core/codex/agents/loom-weaver.toml` - confirmed after line counts are 99, 88, 98, 87, total 372.
- Node canonical/Codex comparison - confirmed Driver and Weaver Markdown bodies align with Codex `developer_instructions` bodies.
- `npm --prefix loom-core run smoke` - passed with `ok: true`, prompt match checks true, Weaver write-boundary checks true, Driver direction-record-boundary checks true, and model-only edit permissions preserving the expected Weaver/Driver write boundaries.
- `npm --prefix loom-core run pack:check` - passed; dry-run package includes compressed agent Markdown and Codex TOML files, total files 69.
- `git diff --check` - passed with no output.
- Targeted behavior searches - found required Driver and Weaver role, write-boundary, no-launch, ticket-owned Ralph, evidence, audit, reconciliation, and direction-setting guardrail phrases in scoped prompt surfaces.
- Targeted leakage searches over `loom-core/agents/*.md` and `loom-core/codex/agents/*.toml` - no matches for package smoke, adapter self, dogfood, repository workflow, npm pack, pack:check, why Loom is built, contributor, AGENTS.md, source repo, Loom Mill required, package process, adapter mechanics, test harness, skill-authoring, or self-justification.

## Findings

None - no material findings within audited scope.

## Verdict

Pass. The compressed prompts preserve the accepted Driver and Weaver behavior within the reviewed scope, canonical Markdown and Codex TOML bodies are aligned, scoped prompt surfaces do not show contributor-facing leakage, and validation evidence supports the ticket's line-count and package-check claims. This audit does not itself close the ticket; it supports closure if the ticket records the audit result and keeps residual risk bounded to the uninspected areas below.

## Required Follow-up

- Update `.loom/tickets/done/20260525-agent-prompt-kernels.md` with this audit result and disposition before closure.
- No source changes are required before closure based on this audit.

## Residual Risk

This audit did not run live model behavior in a fresh harness session and did not validate Playbooks or unrelated dirty worktree changes from prior compression tickets. The review is source-and-validation based, so subtle model interpretation drift remains possible despite preserved guardrail language and passing smoke checks.

## Related Records

- `.loom/tickets/done/20260525-agent-prompt-kernels.md` - consuming ticket.
- `.loom/evidence/20260525-agent-prompt-kernels-validation.md` - validation dossier inspected by this audit.
- `.loom/specs/loom-protocol-compression.md` - compression behavior contract.
- `.loom/specs/loom-driver-agent.md` - Driver behavior contract.
- `.loom/specs/loom-weaver-agent.md` - Weaver behavior contract.
