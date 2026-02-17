---
"id": "al-4f2d"
"status": "review"
"deps": []
"links": []
"created": "2026-02-17T06:25:50Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-a1ba"
"tags":
- "sprint:Pack-Module-Improvements"
- "pack"
- "security"
- "schema"
"external": {}
---
# Pack manifest contract hardening (path safety + root invariants)

## Objective alignment
Improve pack safety and predictability by enforcing strict manifest/path contracts before any filesystem mutation.

## Scope
- Harden manifest loading/validation in `src/agent_loom/pack/packs.py` and related models.
- Enforce safe normalized repo-relative paths (no traversal/absolute escape).
- Enforce that managed/scaffold/protected globs are consistent with declared install roots and current pack files.
- Add targeted tests for invalid manifests and unsafe file paths.

## Non-goals
- Adding remote pack registries or network downloads.
- Changing pack authoring UX beyond validation/error messaging.
- Redesigning lockfile format.

## Implementation plan
1. Add explicit validation helpers in `src/agent_loom/pack/packs.py` for:
   - path normalization and traversal rejection,
   - install root normalization,
   - glob sanity checks (empty/duplicate/conflicting invariants).
2. Wire validation into `load_manifest()` and `iter_pack_files()` so unsafe entries fail fast.
3. Ensure lifecycle entrypoints in `src/agent_loom/pack/core.py` receive only validated relpaths.
4. Add/extend tests in:
   - `tests/test_pack_lifecycle.py`
   - new focused manifest/path validation test module if needed.
5. Keep error text actionable for operators (`which pack`, `which field`, `why invalid`).

## Verification commands
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest tests/test_pack_lifecycle.py`
- `uv run pytest tests/test_pack_cli_ux.py`

## Acceptance criteria
- Pack operations reject unsafe manifest/path inputs with deterministic errors.
- Relative path traversal (`..`) and absolute path escapes are blocked.
- Valid built-in packs continue to install/update/uninstall successfully.
- Regression tests cover both accepted and rejected cases.

## Risks / edge cases
- Overly strict validation could break legitimate glob patterns.
- Pack resources resolved via `importlib.resources` may have path nuances across environments.
- Mitigation: add explicit fixture coverage for built-in packs + representative edge cases.

## Notes

**2026-02-17T06:28:23Z**

Started implementation: auditing current pack manifest/path validation flow in packs.py/core.py and existing lifecycle tests before changes.

**2026-02-17T06:31:05Z**

Implemented manifest/path hardening in pack loader: added repo-relative path normalization (absolute/traversal rejection), duplicate/overlap checks across glob groups, install-root anchoring checks, and pack-file contract validation in iter_pack_files; wired core path normalization to new helper.

**2026-02-17T06:32:05Z**

Added focused manifest validation test module (tests/test_pack_manifest_validation.py). Fixed glob anchor parsing to support patterns like '.opencode/commands/**'. Targeted pack tests now pass (manifest validation + lifecycle + CLI UX).

**2026-02-17T06:32:34Z**

Verification complete: uv run ruff check . (pass), uv run basedpyright (0 errors), uv run pytest tests/test_pack_lifecycle.py (9 passed), uv run pytest tests/test_pack_cli_ux.py (5 passed), uv run pytest tests/test_pack_manifest_validation.py (7 passed).

**2026-02-17T06:33:02Z**

Completion candidate: implemented manifest/path contract hardening with normalized repo-relative validation, install-root/glob invariants, pack-file consistency checks, and focused invalid-manifest tests.
