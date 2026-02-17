---
"id": "al-c09c"
"status": "review"
"deps":
- "al-d94d"
"links": []
"created": "2026-02-09T19:29:11Z"
"type": "feature"
"priority": 2
"assignee": "z3z1ma"
"parent": "al-a1ba"
"tags":
- "sprint:Pack-Module-Improvements"
- "pack"
- "cli"
- "ux"
"external": {}
---
# Pack CLI drift diff contract completion

## Objective alignment
Finish and harden the operator-facing drift diff workflow so pack drift inspection is consistent, discoverable, and test-covered across relevant commands.

## Scope
- Audit `src/agent_loom/pack/cli.py` diff behavior for `status`, `install`, `update`, and `uninstall`.
- Ensure JSON and text modes expose consistent diff metadata.
- Standardize user guidance when drift exists but `--diff` is omitted.
- Expand CLI UX tests for no-drift, drifted-text, and diff-unavailable cases.

## Non-goals
- Rewriting core lifecycle semantics.
- Implementing binary diff rendering.
- Adding paging or interactive TUI diff viewers.

## Implementation plan
1. Consolidate diff rendering and drift guidance helpers in `cli.py` to reduce duplicated branch behavior.
2. Ensure output contract parity between text and `--json` payloads where applicable.
3. Verify that commands remain stable on exit codes while surfacing clear next actions.
4. Expand `tests/test_pack_cli_ux.py` with matrix cases:
   - drifted file + `--diff`,
   - drifted file without `--diff`,
   - no drift,
   - non-text or unavailable diff paths.
5. Update pack docs/help strings if CLI behavior changed.

## Verification commands
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest tests/test_pack_cli_ux.py`
- `uv run pytest tests/test_pack_lifecycle.py -k pack`

## Acceptance criteria
- `loom pack status --diff` reliably prints per-file unified diffs for drifted text files.
- Install/update/uninstall commands provide consistent drift guidance and optional diff output.
- JSON mode includes deterministic diff payloads when `--diff` is requested.
- CLI UX tests cover drift and no-drift branches.

## Risks / edge cases
- Diff rendering for large files can overwhelm output.
- Non-text/binary files may not produce diffs; messaging must remain clear.
- Mitigation: preserve truncation limits and explicit “diff unavailable” messaging.

## Notes

**2026-02-17T06:36:25Z**

Started implementation. Audited pack CLI: status/install/update/uninstall each currently duplicate diff rendering; status guidance text differs from install/update/uninstall guidance. Next: consolidate diff payload/render helpers and expand tests for status+install/update/uninstall text/json parity including diff-unavailable path.

**2026-02-17T06:38:10Z**

Implemented CLI drift/diff contract consolidation in src/agent_loom/pack/cli.py: unified diff item collection + rendering for status/install/update/uninstall, standardized drift guidance messaging when --diff omitted, and aligned JSON diff payloads to include deterministic entries for unavailable diffs (ok=false,diff=''). Expanded tests/test_pack_cli_ux.py to cover no-drift status --diff, status/install JSON diff-unavailable branches, and update/uninstall guidance parity. Verified with uv run pytest tests/test_pack_cli_ux.py and uv run pytest tests/test_pack_lifecycle.py -k pack.

**2026-02-17T06:39:08Z**

Verification sweep: uv run ruff check . and uv run basedpyright both pass. Targeted pack tests pass: uv run pytest tests/test_pack_cli_ux.py and uv run pytest tests/test_pack_lifecycle.py -k pack. Full uv run pytest currently fails on unrelated pre-existing compound/init suites (20 fails, e.g. loom-compound-core pack manifest validation for .opencode/.gitignore and init CLI rc mismatches); no failures in modified pack CLI tests.
