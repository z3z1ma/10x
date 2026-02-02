---
name: server-template-refactor-hygiene
description: Use when doing a large refactor of src/agent_loom/server/templates/*.html so diffs stay meaningful and server HTML contracts stay deterministic.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-02T18:09:49.726Z"
  updated_at: "2026-02-02T18:09:49.726Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You are about to make a large change to `src/agent_loom/server/templates/*.html` (especially `src/agent_loom/server/templates/dashboard.html`).
- You expect lots of line churn (reindent, rearranging sections, extracting repeated markup).

## Goal

Make the refactor readable and keep the server-rendered HTML contract deterministic.

## Checklist

1. Preserve stable anchors
   - Prefer `data-*` hooks for sections/components that tests and agents rely on.
   - Keep headings/section labels stable unless you are intentionally changing UX.

2. Minimize formatting-only churn
   - Avoid mass reformatting that obscures structural/behavior changes.
   - If formatting churn is unavoidable, keep changes isolated and explainable (single theme per edit).

3. Enforce deterministic output
   - Explicit ordering for repeated items (no set/dict iteration).
   - Avoid timestamps/random IDs/absolute paths in rendered HTML.

4. Update the request-level contract test
   - Prefer `tests/test_server_api_contract.py`.
   - Assert required markers/sections and ordering (avoid full HTML snapshots).

5. Verification gate
   - `uv run basedpyright`
   - `uv run ruff check .`
   - `uv run pytest tests/test_server_api_contract.py`
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
