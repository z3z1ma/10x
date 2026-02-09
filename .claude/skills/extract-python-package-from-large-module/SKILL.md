---
name: extract-python-package-from-large-module
description: Procedure for extracting a new Python package from a large module while keeping a stable public API, crisp file roles, and high-signal tests.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T18:25:50.635157Z"
  source_episode_ids: "075e5ebae208428e278ccd9c88dfdaa88003c63ed6666e57aca164f01e88c42a"
  source_instinct_ids: "create-readme-when-introducing-new-subsystem,extract-new-package-from-monolith,prompt-tests-assert-structure-not-strings,refactors-must-update-contract-tests"
  tags: "architecture,packaging,python,refactor,testing"
  updated_at: "2026-02-09T18:25:50.635157Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Extract Python Package From Large Module

Use when a single Python module has grown into multiple responsibilities and a refactor will delete/move large amounts of code.

## Goal
- Split responsibilities into a new package with a small, deliberate public API.
- Keep the diff reviewable and the behavior protected by contract tests.

## Procedure
1. Identify the contract
- List the externally-used entrypoints (functions/classes/CLI hooks) and the behaviors that must not change.
- Decide what becomes the new public API (what callers should import).

2. Create the package skeleton
- Create a new package directory (e.g. `src/<project>/<name>/`).
- Add `__init__.py` that re-exports only the intended public API.
- Add a small package README (scope, non-goals, entrypoints, how to test).

3. Split by file role (keep names boring)
- `models.py`: dataclasses/enums/typed containers; keep mostly import-light.
- `core.py`: pure logic and operations (no side-effect orchestration unless necessary).
- `<registry>.py` (optional): registries, plugin discovery, mappings.
- Avoid cycles: `core.py` can depend on `models.py`; keep the reverse minimal.

4. Move code with mechanical fidelity
- Move code in small chunks; keep behavior identical initially.
- Prefer moving whole symbols (function/class) without rewriting until tests pass.
- Update imports in callers to use the new package’s public API (not deep file paths).

5. Update and prune tests
- Add/adjust contract tests that verify the key behaviors (inputs/outputs, idempotency, lifecycle transitions).
- Remove tests that only validate deleted paths.
- For prompt/template/text outputs: assert on structure/markers and critical values, not full strings.

6. Gates
- Run:
  - `uv run ruff check .`
  - `uv run basedpyright`
  - `uv run pytest`
- Fix any typing drift caused by the move (imports, circular dependencies, missing exports).

## Done when
- Callers import from the package public API.
- The old monolith is either deleted or reduced to a thin compatibility shim (only if explicitly needed).
- Tests cover the contract and no tests reference dead paths.
- Ruff, basedpyright, and pytest are clean.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
