# OpenCode Agent Shadowing Diagnosis

ID: evidence:20260515-opencode-agent-shadowing-diagnosis
Type: Evidence Observation
Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Observed: 2026-05-15 08:28 UTC

## Observation

A diagnostic Ralph run found that OpenCode Core plugin agent registration can be shadowed by an existing user-defined agent entry.

Key source observations from `packet:20260515T082242Z-opencode-weaver-runtime-diagnosis`:

- `loom-core/agents/loom-weaver.md:47-66` contains the expected `.loom/`-only write boundary.
- `loom-core/loom-core.mjs:229-239` uses `config.agent[agent.name] ??= { ... }`, so the plugin only installs `description`, `mode`, `prompt`, and `permission` when the agent key is absent.
- The installed cached `@z3z1ma/open-loom-core@0.2.4` has the same `??=` behavior.
- A pre-existing global OpenCode config defines `agent.loom-weaver` and `agent.loom-driver` as model-only stubs, which is sufficient to prevent the plugin from installing canonical prompts and permissions.

The diagnostic probe result was:

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

## What This Shows

- Supports `ticket:20260515-opencode-weaver-agent-runtime-wiring#ACC-001`: the likely runtime failure layer is plugin configuration merging, where a user-provided model-only agent entry shadows Loom-owned prompt and permission fields.
- Supports changing the plugin so it preserves user fields such as `model` while ensuring Loom-owned `description`, `mode`, `prompt`, and `permission` are installed for known Loom agents.

## What This Does Not Show

- It does not prove OpenCode's internal `Task` agent resolver field consumption beyond the observed runtime failure and plugin merge behavior.
- It does not prove behavior after a fix; a fresh post-fix runtime invocation is still required.
- It does not justify modifying any user or global OpenCode configuration file.
