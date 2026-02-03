---
name: team-core-prompt-assembly-checklist
description: Use when changing src/agent_loom/team/core.py in ways that affect prompt assembly or agent initialization, to keep prompt contracts deterministic and covered.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-03T00:47:28.532Z"
  updated_at: "2026-02-03T00:47:28.532Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You changed `src/agent_loom/team/core.py` and it touches:
  - prompt construction/assembly, or
  - agent initialization/spawn defaults, or
  - any user-visible prompt text routed through core.

## Goal

Keep team prompt behavior deterministic and locked by focused contract tests.

## Checklist

1. Confirm what contract changed
   - Identify which prompt(s) changed (sections/headings/order).
   - Ensure any list ordering is explicit (no dict/set iteration order).

2. Update prompt contract tests
   - Prefer section-level invariants over full-string snapshots.
   - Update/add assertions in `tests/test_team_prompts.py` to cover:
     - required sections/headings
     - deterministic ordering
     - key defaults that the prompt must reflect

3. If agent init/spawn defaults changed
   - Update/add focused assertions in `tests/test_team_init_agents.py`.

4. Verification gate (repo standard)
   - `uv run basedpyright`
   - `uv run ruff check .`
   - `uv run pytest tests/test_team_prompts.py`
   - If applicable: `uv run pytest tests/test_team_init_agents.py`

## Common failure modes

- Prompt ordering changes due to implicit iteration.
- Tests assert too much exact text and become brittle.
- Core changes alter prompts but only core tests are updated (missing prompt contracts).
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
