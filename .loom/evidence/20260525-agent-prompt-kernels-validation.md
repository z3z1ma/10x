# Agent Prompt Kernels Validation

ID: evidence:20260525-agent-prompt-kernels-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

This dossier records validation for `ticket:20260525-agent-prompt-kernels`: Driver and Weaver prompt compression, canonical/Codex alignment, package validation, targeted source inspection, and leakage search results.

## Observations

- Observation: Before line counts for scoped agent prompt files were 890 total lines.
  - Procedure/source: `wc -l loom-core/agents/loom-driver.md loom-core/agents/loom-weaver.md loom-core/codex/agents/loom-driver.toml loom-core/codex/agents/loom-weaver.toml` before edits.
  - Actual result: `loom-driver.md` 219, `loom-weaver.md` 227, `loom-driver.toml` 218, `loom-weaver.toml` 226, total 890.

- Observation: After line counts for scoped agent prompt files are 372 total lines.
  - Procedure/source: same `wc -l` command after edits.
  - Actual result: `loom-driver.md` 99, `loom-weaver.md` 88, `loom-driver.toml` 98, `loom-weaver.toml` 87, total 372.

- Observation: Canonical Markdown prompt bodies and Codex `developer_instructions` bodies are aligned.
  - Procedure/source: Node comparison stripped Markdown frontmatter and compared it to each TOML `developer_instructions` body for Driver and Weaver.
  - Actual result: `loom-core/agents/loom-driver.md <-> loom-core/codex/agents/loom-driver.toml: aligned`; `loom-core/agents/loom-weaver.md <-> loom-core/codex/agents/loom-weaver.toml: aligned`.

- Observation: Core smoke passed after prompt wording retained the existing smoke-checked guardrail phrases.
  - Procedure/source: `npm --prefix loom-core run smoke`.
  - Actual result: JSON output reported `"ok": true`, `codexLoomWeaverHasWriteBoundary: true`, `codexLoomWeaverPromptMatchesAgent: true`, `codexLoomDriverHasDirectionRecordBoundary: true`, `codexLoomDriverPromptMatchesAgent: true`, `loomWeaverPromptHasWriteBoundary: true`, and `loomDriverPromptHasDirectionRecordBoundary: true`.

- Observation: Core pack check passed.
  - Procedure/source: `npm --prefix loom-core run pack:check`.
  - Actual result: pack check reran smoke with `"ok": true`, then `npm pack --dry-run` completed and reported 69 tarball files including the compressed agent Markdown and Codex TOML files.

- Observation: Markdown/diff whitespace check passed.
  - Procedure/source: `git diff --check`.
  - Actual result: no output.

- Observation: Targeted source inspection found required role and guardrail phrases in the prompt surfaces.
  - Procedure/source: targeted `grep` over `loom-core/agents` and `loom-core` for Design Office, Factory Floor, `.loom/` write boundary, no Weaver Ralph launch, ticket-owned Ralph, evidence, audit, reconciliation, worker-output-claim, and direction-setting boundary language.
  - Actual result: Weaver prompt contains `Design Office`, `Write only inside .loom/`, `Do not launch Ralph worker or review runs`, shaping/routing, evidence, and audit language. Driver prompt contains `Factory Floor`, `ticket-owned Ralph`, `direction-setting records`, `.loom/tickets/`, `.loom/evidence/`, `.loom/audit/`, worker-output-claim, evidence, audit, and reconciliation language.

- Observation: Targeted product-surface leakage search found no matches in scoped model-visible agent surfaces.
  - Procedure/source: `grep` over `loom-core` agent prompt files for `package smoke`, `adapter self`, `dogfood`, `repository workflow`, `npm pack`, `pack:check`, `why Loom is built`, `contributor`, `AGENTS.md`, `source repo`, and `Loom Mill required`.
  - Actual result: no files found.

## Artifacts

- `loom-core/agents/loom-driver.md` - compressed canonical Driver prompt.
- `loom-core/agents/loom-weaver.md` - compressed canonical Weaver prompt.
- `loom-core/codex/agents/loom-driver.toml` - Codex Driver copy with aligned `developer_instructions`.
- `loom-core/codex/agents/loom-weaver.toml` - Codex Weaver copy with aligned `developer_instructions`.
- Command outputs are in the worker transcript; no raw artifact directory was created.

## What This Shows

- `ticket:20260525-agent-prompt-kernels#ACC-001` - supports - Weaver is compressed around Design Office shaping, `.loom/` write boundary, no worker/review launch, routing, evidence/audit honesty, and handoff behavior.
- `ticket:20260525-agent-prompt-kernels#ACC-002` - supports - Driver is compressed around Factory Floor coordination, graph-supported execution, ticket-owned Ralph runs, output reconciliation, evidence, audit, blockers, and higher-authority escalation.
- `ticket:20260525-agent-prompt-kernels#ACC-003` - supports - canonical and Codex prompt bodies are aligned and line counts show material compression from 890 to 372 total lines.
- `ticket:20260525-agent-prompt-kernels#ACC-004` - supports - targeted leakage search found no contributor-facing product-surface leakage in scoped agent surfaces.
- `ticket:20260525-agent-prompt-kernels#ACC-005` - supports - Core smoke, Core pack check, and `git diff --check` passed after the final edits.

## What This Does Not Show

This evidence does not prove live model behavior in a fresh harness session. It does not audit the prompts adversarially, validate Playbooks, or validate unrelated dirty worktree changes from earlier compression tickets. It does not close the ticket; a fresh-context audit is still needed before closure.

## Related Records

- `ticket:20260525-agent-prompt-kernels` - consuming ticket for this validation.
- `spec:loom-protocol-compression` - compression behavior contract.
- `spec:loom-driver-agent` - Driver behavior contract.
- `spec:loom-weaver-agent` - Weaver behavior contract.
