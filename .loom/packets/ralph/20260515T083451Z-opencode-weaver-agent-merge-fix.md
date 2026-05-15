# OpenCode Loom Agent Merge Fix

ID: packet:20260515T083451Z-opencode-weaver-agent-merge-fix
Type: Packet
Status: consumed
Created: 2026-05-15 08:34 UTC
Updated: 2026-05-15 08:37 UTC
Target: ticket:20260515-opencode-weaver-agent-runtime-wiring
Packet Kind: Ralph
Mode: execution
Context Style: hybrid
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Risk: high - changes safety-critical agent registration and smoke coverage.
Verification Posture: test-first

## Mission

Implement the minimal OpenCode Core plugin fix for the diagnosed agent shadowing bug: user-provided model-only `loom-weaver` or `loom-driver` agent entries must not prevent the plugin from installing Loom-owned prompt and permission fields.

The worker should change only the plugin source and update this packet output. Do not modify any user/global OpenCode config.

## Context Bundle

Records:

- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - target ticket and acceptance criteria.
- `evidence:20260515-loom-weaver-runtime-agent-failure` - observed runtime failure.
- `evidence:20260515-opencode-agent-shadowing-diagnosis` - source-backed diagnosis for the `??=` shadowing bug.
- `spec:loom-weaver-agent` - intended Loom Weaver behavior and `.loom/` write boundary.

Files, Diffs, Or External References:

- `loom-core/loom-core.mjs` - configureOpenCode implementation and current smoke checks.
- `loom-core/agents/loom-weaver.md` - canonical Loom Weaver prompt.
- `loom-core/agents/loom-driver.md` - related agent should receive the same merge protection.

Inline Context:

Diagnosis found that `configureOpenCode` currently uses `config.agent[agent.name] ??= { description, mode, prompt, permission }`. If a user config already has `agent.loom-weaver = { model: ... }`, the plugin does not install `prompt` or `permission`, so runtime `loom-weaver` falls back to generic behavior and can edit outside `.loom/`.

Expected implementation direction:

- Preserve user-provided agent fields such as `model`.
- Always install or refresh Loom-owned `description`, `mode`, `prompt`, and `permission` for known Loom agents.
- Add a smoke/regression case that seeds `config.agent["loom-weaver"] = { model: ... }` and `config.agent["loom-driver"] = { model: ... }` before running `configureOpenCode`, then fails unless prompt and permission are installed.
- Keep existing dedupe behavior for `skills.paths`.

## Read Scope

- `.loom/tickets/20260515-opencode-weaver-agent-runtime-wiring.md`
- `.loom/evidence/20260515-loom-weaver-runtime-agent-failure.md`
- `.loom/evidence/20260515-opencode-agent-shadowing-diagnosis.md`
- `.loom/specs/loom-weaver-agent.md`
- `loom-core/loom-core.mjs`
- `loom-core/agents/loom-weaver.md`
- `loom-core/agents/loom-driver.md`

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output` and update `Status:` when appropriate.

Source Paths:

- `loom-core/loom-core.mjs` - minimal plugin merge and smoke/regression changes only.

Explicitly forbidden:

- Do not modify `README.md`.
- Do not modify `~/.config/opencode/opencode.json` or any other user/global OpenCode config.
- Do not modify docs, manifests, package metadata, unrelated Loom records, or numbered-reference files.

## Source Snapshot

At packet compilation, the source tree already contained the ticket/evidence/diagnostic packet records from this session and the earlier numbered-reference work may still be dirty in the parent session. This packet's source write scope is only `loom-core/loom-core.mjs`.

## Task

Make the smallest source change that fixes the diagnosed plugin merge bug and strengthens smoke coverage.

Implementation guidance:

- Replace whole-object `??=` agent installation with a merge that keeps existing user fields but writes Loom-owned fields for plugin-provided agents.
- Ensure both `loom-weaver` and `loom-driver` are covered.
- Add smoke assertions that would have failed for a model-only preexisting agent stub.
- Keep the implementation simple; no broad refactor.

## Launch

Read this packet first, stay inside it, and return the output contract.

## Evidence, Review, Or Verification Expectations

Before changing code, identify a smoke assertion or equivalent local check that would fail under the current `??=` behavior. After the change, run:

- `npm --prefix loom-core run smoke`
- `git diff --check`

If feasible after this source fix, do not run the unbiased live `loom-weaver` runtime task from inside the worker; leave that for parent verification after inspecting the worker output.

## Stop Conditions

- Stop with `blocked` if the correct fix requires changing user/global OpenCode config.
- Stop with `escalate` if source inspection shows OpenCode consumes a different field than `prompt` and the plugin interface shape needs broader design.
- Stop if required changes exceed `loom-core/loom-core.mjs`.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

## Worker Output

Outcome: stop

Files changed:

- `loom-core/loom-core.mjs`

Records changed:

- `.loom/packets/ralph/20260515T083451Z-opencode-weaver-agent-merge-fix.md`

Evidence, validation output, and observations gathered:

- Pre-fix shadowing probe against `configureOpenCode({ agent: { "loom-weaver": { model: "test-model" }, "loom-driver": { model: "test-model" } } })` showed both existing model-only agent entries retained only `model`, with `loomWeaverHasPrompt: false`, `loomWeaverHasPermission: false`, `loomDriverHasPrompt: false`, and `loomDriverHasPermission: false`. The probe exited non-zero, confirming the regression assertion would fail under the previous `??=` behavior.
- Changed OpenCode agent installation from whole-object `??=` to merging existing user fields first, then writing Loom-owned `description`, `mode`, `prompt`, and `permission` for plugin-provided agents.
- Added smoke coverage for preexisting model-only `loom-weaver` and `loom-driver` entries. The smoke now asserts that `model` is preserved while canonical prompts and permissions are installed.
- Post-fix shadowing probe showed both agents have keys `model`, `description`, `mode`, `prompt`, and `permission`, preserve `model: "test-model"`, and have prompt and permission present.
- `npm --prefix loom-core run smoke` passed with `ok: true`, including `modelOnlyLoomWeaverPreservesModel: true`, `modelOnlyLoomDriverPreservesModel: true`, `modelOnlyLoomWeaverPromptHasWriteBoundary: true`, `modelOnlyLoomDriverPromptHasDirectionRecordBoundary: true`, and model-only edit permissions installed.
- `git diff --check` passed with no output.

What was not verified or reviewed:

- Did not run the unbiased live `loom-weaver` runtime task, per packet instruction to leave that for parent verification after worker output inspection.
- Did not run `npm --prefix loom-core run pack:check`; packet only required core smoke and `git diff --check`.
- Did not perform adversarial audit.

Blockers, risks, or assumptions discovered:

- No blocker found inside packet scope.
- Remaining risk: the source fix and smoke regression prove the plugin merge contract, but ticket acceptance still needs a fresh runtime `loom-weaver` invocation to prove OpenCode's actual task/subagent path now receives and follows the canonical prompt and permission boundary.

Recommended next move for the consuming surface:

- Parent should inspect this diff, then run the ticket-level runtime verification for `ACC-004` and package check if moving toward ticket closure. Route results into evidence and audit before closing the ticket.
