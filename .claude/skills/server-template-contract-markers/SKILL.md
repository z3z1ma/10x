---
name: server-template-contract-markers
description: Use when refactoring src/agent_loom/server/templates/*.html to preserve agent/user-visible anchors via stable data-* markers and keep tests resilient.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-02T17:53:40.737Z"
  updated_at: "2026-02-02T17:53:40.737Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You are refactoring `src/agent_loom/server/templates/*.html` and the structure/sections may move.
- You are adding new sections that should be addressable by agents/tests.

## Goal

Keep server HTML legible and testable via stable markers, not brittle formatting.

## Checklist

1. Add/keep stable anchors
   - Prefer `data-*` markers for key sections (for example: `data-page`, `data-section`, `data-item`).
   - Avoid using random IDs, timestamps, or absolute paths in attributes/text.

2. Make repeated content deterministic
   - Ensure template loops render in a stable order.
   - If the data source is unordered, sort it before rendering.

3. Write resilient assertions
   - In `tests/test_server_api_contract.py`, assert presence of markers/section labels and ordering.
   - Avoid full HTML snapshots and whitespace-sensitive expectations.

4. Verification gate
   - `uv run basedpyright`
   - `uv run ruff check .`
   - `uv run pytest tests/test_server_api_contract.py`
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
