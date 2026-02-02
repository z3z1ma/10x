---
name: server-api-contract-testing
description: Use when changing server-rendered HTML behavior (templates or routes) to keep the server API + HTML contract deterministic and covered by tests/test_server_api_contract.py.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-02T17:11:57.760Z"
  updated_at: "2026-02-02T17:11:57.760Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You changed `src/agent_loom/server/templates/*.html` and the change affects what the server returns.
- You changed the route/handler that serves HTML (wrapping/layout/headers/markers).
- You refactored `src/agent_loom/server/templates/dashboard.html` substantially.

## Goal

Lock server-rendered HTML behavior with a request-level contract.

## Checklist

1. Identify the public surface
   - Which route returns the HTML?
   - Which markers/sections must remain stable for users and agents?

2. Define stable invariants (avoid brittleness)
   - Assert on headings/section labels and `data-*` hooks.
   - Assert on deterministic ordering for repeated items.
   - Avoid asserting raw whitespace or full HTML unless explicitly intended.

3. Keep diffs reviewable (diff hygiene)
   - Avoid formatting-only churn that obscures behavioral changes.
   - Preserve stable anchors even if structure changes.
   - If you must rename/remove an anchor, update the test invariants in the same change.

4. Handle large template refactors safely
   - Prefer adding stable `data-*` anchors over relying on CSS classes or deep DOM structure.
   - Avoid loops that render in nondeterministic order; sort explicitly.

5. Update/add the contract test
   - Prefer `tests/test_server_api_contract.py`.
   - Exercise the real route/handler.
   - Assert required markers/sections and ordering.

6. Verification gate
   - `uv run basedpyright`
   - `uv run ruff check .`
   - `uv run pytest tests/test_server_api_contract.py`

## Common failure modes

- Template loops render in nondeterministic order.
- Tests snapshot full HTML and become brittle due to formatting-only changes.
- HTML includes machine-specific paths or other environment-specific values.
- Refactors remove/rename anchors without updating the contract test.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
