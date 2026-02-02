---
name: server-template-ux-contract-testing
description: Use when changing src/agent_loom/server/templates/*.html to keep server-rendered HTML deterministic and regression-tested.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-02T16:44:52.114Z"
  updated_at: "2026-02-02T16:44:52.114Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You changed `src/agent_loom/server/templates/*.html`.
- You made a large refactor in `src/agent_loom/server/templates/dashboard.html`.

## Goal

Lock the server-rendered HTML as a stable UX contract.

## Checklist

1. Find the render/route entrypoint
   - Locate where the template is referenced (search for the literal filename):
     - `dashboard.html`
   - Identify the handler that renders it and whether it is returned directly or wrapped.

2. Define the contract (pick stable invariants)
   - Required headings/sections that must appear.
   - Stable ordering of key sections (don’t rely on dict/set iteration in template loops).
   - Prohibited output:
     - timestamps (unless explicitly required)
     - random IDs
     - machine-specific absolute paths
     - secrets or environment dumps

3. Add/update a focused pytest contract test
   - Prefer a request-level test (exercise the real route/handler) over a direct template render, unless direct render is the established pattern.
   - Assert on stable markers (e.g., key headings, `data-*` hooks, or unique section labels), not exact full HTML.
   - If lists/tables are rendered, assert deterministic ordering.

4. Verification gate
   - `uv run basedpyright`
   - `uv run ruff check .`
   - Run the smallest relevant pytest selection (the specific new/updated test module).

## Common failure modes

- Template loops render in nondeterministic order.
- Tests snapshot full HTML and become brittle due to whitespace/format changes.
- HTML includes absolute paths or environment-specific values.
- Refactors remove/rename user-visible anchors without updating the contract test.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
