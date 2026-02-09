---
name: sync-distributed-opencode-plugin
description: Procedure to prevent drift between `.opencode/plugins/*` and the shipped copy under `src/agent_loom/**/opencode/plugins/*`.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T05:19:20.993689Z"
  source_episode_ids: "8effd17b5ade4736a0cbbffe48e6e827b159791adb05936c705d1a25cf60eca8"
  source_instinct_ids: "sync-distributed-opencode-plugin"
  tags: "compound,distribution,opencode,workflow"
  updated_at: "2026-02-09T05:19:20.993689Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Sync Distributed Opencode Plugin

Use this when a plugin exists in two places:
- `.opencode/plugins/<name>.ts` (dev copy)
- `src/agent_loom/**/opencode/plugins/<name>.ts` (shipped/distributed copy)

## Steps

1. Identify the two plugin paths that must match.
2. Make the change once, then immediately apply the exact same change to the other copy.
3. Verify they are identical (byte-for-byte) before moving on.
4. Add/keep a regression check that fails if the two files diverge.
5. Run repo gates: `uv run ruff check .` and `uv run basedpyright`, then the relevant tests.

## Guardrails

- Do not rely on memory that "it was copied earlier"; always diff the two files.
- Prefer a deterministic sync/check over human process when possible.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
