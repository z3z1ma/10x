# OpenCode Loom Weaver Runtime Diagnosis

ID: packet:20260515T082242Z-opencode-weaver-runtime-diagnosis
Type: Packet
Status: consumed
Created: 2026-05-15 08:22 UTC
Updated: 2026-05-15 08:28 UTC
Target: ticket:20260515-opencode-weaver-agent-runtime-wiring
Packet Kind: Ralph
Mode: research
Context Style: hybrid
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Risk: high - this diagnoses a safety boundary failure in the runtime agent path.
Verification Posture: observation-first

## Mission

Find the concrete failure point that explains why an actual OpenCode `Task` invocation with `subagent_type="loom-weaver"` edited `README.md` instead of following the shipped Loom Weaver `.loom/`-only instructions.

This run is diagnostic only. It must produce evidence for `ticket:20260515-opencode-weaver-agent-runtime-wiring#ACC-001` by identifying the responsible layer or narrowing it with source-backed observations. Do not implement a fix in this packet.

## Context Bundle

Records:

- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - target ticket and acceptance criteria.
- `spec:loom-weaver-agent` - intended behavior: Loom Weaver writes only under `.loom/` and refuses outside-`.loom` edits.
- `evidence:20260515-loom-weaver-runtime-agent-failure` - observed failure: unbiased `loom-weaver` task edited `README.md`.

Files, Diffs, Or External References:

- `loom-core/loom-core.mjs` - OpenCode plugin agent registration and smoke checks.
- `loom-core/agents/loom-weaver.md` - canonical OpenCode Loom Weaver prompt body.
- `loom-core/codex/agents/loom-weaver.toml` - adapter-specific comparison surface; likely not the OpenCode runtime path.
- Any repository OpenCode config or generated agent surfaces if present.

Inline Context:

The observed failing invocation was exactly:

```text
Task subagent_type: loom-weaver
Task prompt: Add hello world to README.
Task command: @loom-weaver add hello world to README
```

The worker result was:

```text
Added `Hello world.` to `README.md`.

Verified with `git diff --check` with no issues.
```

Existing suspicion from parent inspection: `loom-core/loom-core.mjs` constructs `config.agent[agent.name]` with `prompt: agent.content`, `mode: "all"`, and `.loom/**` edit permission in `configureOpenCode({})`, but the runtime `Task` subagent did not behave as if it received those instructions.

## Read Scope

- `.loom/tickets/20260515-opencode-weaver-agent-runtime-wiring.md`
- `.loom/evidence/20260515-loom-weaver-runtime-agent-failure.md`
- `.loom/specs/loom-weaver-agent.md`
- `loom-core/loom-core.mjs`
- `loom-core/agents/loom-weaver.md`
- `loom-core/codex/agents/loom-weaver.toml`
- Project and global OpenCode config/agent lookup surfaces only as needed to determine whether a local/global runtime agent shadows plugin config. Do not read secrets.

## Write Scope

Records Or Artifacts:

- None - this worker should return diagnostic output to the parent; the parent will preserve it in this packet, ticket, or evidence.

Source Paths:

- None - diagnostic run only. Do not edit source, docs, config, README, package files, tests, or Loom records.

## Source Snapshot

At packet compilation, `git status --short` showed only the new ticket and evidence records as untracked:

```text
?? .loom/evidence/20260515-loom-weaver-runtime-agent-failure.md
?? .loom/tickets/20260515-opencode-weaver-agent-runtime-wiring.md
```

The accidental README edit from the failing runtime test had already been removed.

## Task

Diagnose the runtime prompt/permission failure. Use source-backed observations, not guesses.

Specifically:

- Inspect the OpenCode agent registration code and compare it to how this harness exposes `Task` subagents.
- Check whether `loom-weaver` is actually registered as an OpenCode runtime agent, and whether the runtime task system likely uses `prompt`, another field name, a separate agent catalog, or a built-in/fallback agent when `subagent_type` is unknown.
- Check whether `config.agent[agent.name] ??= ...` could leave an existing stub/shadow agent without the canonical prompt.
- Check whether the existing smoke checks only validate self-constructed config rather than the actual runtime subagent registry.
- Identify the most likely concrete failure point and the minimum next implementation target.

Non-goals:

- Do not implement a fix.
- Do not edit files.
- Do not bias the result by assuming one hypothesis is true without source evidence.

## Launch

Read this packet first, stay inside it, and return the output contract.

## Evidence, Review, Or Verification Expectations

Return observations that are strong enough for the parent to decide the first implementation change. Cite file paths and line numbers where possible. If a runtime command can safely inspect the agent registry without writing files or exposing secrets, describe the command and its result.

## Stop Conditions

- Stop and return `blocked` if diagnosing the actual runtime path requires access to OpenCode internals that are not present in this workspace.
- Stop and return `escalate` if the fix requires a product decision about whether plugin agents should become default agents or how OpenCode should expose plugin-defined agents to `Task`.
- Do not widen into implementation changes.

## Output Contract

The worker must return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- observations gathered, with file/line references where possible
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

## Worker Output

outcome: `stop`

files changed: none

records changed: none

observations gathered:

- Canonical Loom Weaver prompt is correct: `loom-core/agents/loom-weaver.md:47-66` says write only inside `.loom/`, must not edit outside `.loom/`, and must route outside-`.loom` edit requests into Loom records.
- Plugin registration constructs the right agent object only when the agent key is absent: `loom-core/loom-core.mjs:229-239` uses `config.agent[agent.name] ??= { ... prompt, permission ... }`.
- Installed runtime plugin has the same shadowing behavior: cached `@z3z1ma/open-loom-core@0.2.4` uses `config.agent[agent.name] ??=` at lines `247-254`.
- Global OpenCode config already defines `agent.loom-weaver` as a stub with only `model`: `/Users/alexanderbutler/.config/opencode/opencode.json:36-38`.
- That existing stub prevents the plugin from installing the canonical prompt and permissions. Probe command result:

```json
{
  "loomWeaverKeys": ["model"],
  "loomWeaverHasPrompt": false,
  "loomWeaverHasPermission": false,
  "loomDriverKeys": ["model"],
  "loomDriverHasPrompt": false,
  "loomDriverHasPermission": false
}
```

what was not verified or reviewed:

- Did not inspect OpenCode internals for the exact `Task` resolution code.
- Did not run another live `Task` invocation.
- Did not verify the exact field name OpenCode consumes beyond the plugin's current `prompt` usage.
- Did not implement or test a fix.

blockers, risks, or assumptions discovered:

- Most likely failure point: global config shadowed the plugin-provided `loom-weaver` agent because `??=` preserves the existing model-only object, leaving the runtime agent without prompt or permission boundary.
- Existing smoke is self-referential: it calls `configureOpenCode({})`, so it misses the real case where a user config already contains `agent.loom-weaver`.
- Same risk applies to `loom-driver`, which is also present as a model-only stub in global config.

recommended next move for the consuming surface:

- Implement a minimal merge fix in `configureOpenCode`: preserve user-provided fields like `model`, but always ensure Loom-owned `description`, `mode`, `prompt`, and `permission` are present or updated for `loom-weaver` and `loom-driver`.
- Add regression coverage that seeds `config.agent["loom-weaver"] = { model: ... }` before `configureOpenCode(config)` and fails unless prompt plus permissions are installed.
