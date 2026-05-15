# OpenCode Loom Agent Merge Fix Audit

ID: packet:20260515T084528Z-opencode-weaver-agent-merge-audit
Type: Packet
Status: consumed
Created: 2026-05-15 08:45 UTC
Updated: 2026-05-15 08:47 UTC
Target: ticket:20260515-opencode-weaver-agent-runtime-wiring
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Risk: high - audit challenges a safety boundary fix and evidence limitations.
Review Lens: audit, code review, evidence sufficiency, runtime-boundary risk

## Mission

Adversarially review the OpenCode Loom agent merge fix and current evidence story. Determine whether the source change plausibly fixes the diagnosed shadowing bug, whether the new smoke coverage would have caught the failure, and what remains before ticket closure.

## Context Bundle

Records:

- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - target ticket, scope, acceptance, and current state.
- `evidence:20260515-loom-weaver-runtime-agent-failure` - original runtime failure.
- `evidence:20260515-opencode-agent-shadowing-diagnosis` - diagnosis evidence.
- `evidence:20260515-opencode-agent-merge-fix-validation` - package check evidence.
- `packet:20260515T082242Z-opencode-weaver-runtime-diagnosis` - diagnostic worker output.
- `packet:20260515T083451Z-opencode-weaver-agent-merge-fix` - implementation worker output.
- `spec:loom-weaver-agent` - behavior contract.

Files, Diffs, Or External References:

- `loom-core/loom-core.mjs` - implementation diff.
- `loom-core/agents/loom-weaver.md` - canonical prompt.
- Current `git diff` for `loom-core/loom-core.mjs`.

## Read Scope

- `.loom/tickets/20260515-opencode-weaver-agent-runtime-wiring.md`
- `.loom/evidence/20260515-loom-weaver-runtime-agent-failure.md`
- `.loom/evidence/20260515-opencode-agent-shadowing-diagnosis.md`
- `.loom/evidence/20260515-opencode-agent-merge-fix-validation.md`
- `.loom/packets/ralph/20260515T082242Z-opencode-weaver-runtime-diagnosis.md`
- `.loom/packets/ralph/20260515T083451Z-opencode-weaver-agent-merge-fix.md`
- `.loom/specs/loom-weaver-agent.md`
- `loom-core/loom-core.mjs`
- `loom-core/agents/loom-weaver.md`
- current diff for the above files as needed

## Write Scope

Records Or Artifacts:

- None - return audit output to parent; parent will preserve the audit record.

Source Paths:

- None - review only. Do not edit files.

## Source Snapshot

The source fix has been applied to `loom-core/loom-core.mjs`. Package check evidence says `npm --prefix loom-core run pack:check`, `git diff --check`, and `git diff -- README.md` passed. Fresh live runtime verification is intentionally still pending because the current OpenCode session may have stale agent registry state.

## Task

Review for:

- correctness of the merge fix: preserves user fields while installing Loom-owned prompt/permission/mode/description
- whether smoke coverage would fail for the original model-only shadowing bug
- whether any unintended override, permission, mode, or config merge risk remains
- whether evidence supports ACC-001, ACC-002, ACC-003, and ACC-005
- whether ACC-004 remains honestly pending and what must happen before closure

## Launch

Read this packet first, stay inside it, and return the output contract.

## Evidence, Review, Or Verification Expectations

Return findings with `FIND-*` IDs if material. Use verdict labels `clear`, `concerns`, `changes-needed`, or `inconclusive`.

## Stop Conditions

- Stop with `blocked` if key records or source files are missing.
- Stop with `inconclusive` if the diff cannot be inspected.
- Do not widen into implementation.

## Output Contract

The worker must return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- findings with IDs or explicit no findings
- verdict and limits
- what was not verified or reviewed
- recommended next move

## Worker Output

outcome: `stop`

files changed: none

records changed: none

findings: explicit no material findings

verdict and limits: `concerns`

The merge fix in `loom-core/loom-core.mjs:233-240` correctly preserves existing user fields via spread, then overwrites Loom-owned `description`, `mode`, `prompt`, and `permission`. This addresses the diagnosed model-only shadowing bug. The new smoke case at `loom-core/loom-core.mjs:393-447` would fail under the previous `??=` behavior because model-only `loom-weaver` and `loom-driver` stubs would lack prompt and permission fields.

Evidence support:

- ACC-001: supported by diagnosis evidence and source-backed shadowing probe.
- ACC-002: supported at plugin/config merge level, not yet live runtime level.
- ACC-003: supported for the diagnosed failure mode; the test faithfully models the model-only shadowing path.
- ACC-004: still pending; no fresh post-reload unbiased runtime invocation was reviewed.
- ACC-005: supported by recorded `pack:check`, `git diff --check`, and README diff evidence after the fix.

what was not verified or reviewed:

- Did not run fresh commands.
- Did not inspect OpenCode internal `Task` resolver beyond the scoped source/evidence.
- Did not perform live runtime `loom-weaver` invocation.
- Did not verify package behavior after any changes beyond the recorded evidence.

recommended next move:

- Do not close the ticket yet.
- After OpenCode reloads the corrected plugin, run an unbiased runtime invocation equivalent to `@loom-weaver add hello world to README`, verify `README.md` remains unchanged, preserve that evidence, then use this audit plus the new runtime evidence for closure.
