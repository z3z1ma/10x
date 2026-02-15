---
"id": "al-18ec"
"status": "in_progress"
"deps":
- "al-8d66"
"links": []
"created": "2026-02-15T19:14:56Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-0463"
"tags":
- "sprint:Public-Launch-Architecture-Cleanup"
- "architecture"
- "cli"
- "dedupe"
"external": {}
---
# Extract shared CLI result/output contract

## Objective alignment
Public launch requires consistent CLI JSON/text behavior across all commands. Duplicate output helper implementations increase drift risk and maintenance cost.

## Scope
- Introduce one shared output/payload utility module for CLI entrypoints.
- Migrate duplicated helpers from:
  - `src/agent_loom/team/cli.py`
  - `src/agent_loom/workspace/cli.py`
  - `src/agent_loom/ticket/cli.py`
  - `src/agent_loom/compound/cli.py`
  - `src/agent_loom/pack/cli.py`
  - `src/agent_loom/init.py`
- Preserve existing per-command payload shapes and exit behavior.

## Non-goals
- No CLI feature additions.
- No command naming changes.
- No parser restructuring (handled by separate tickets).

## Implementation plan
1. Add shared module (recommended path: `src/agent_loom/core/cli_output.py`) containing reusable primitives:
   - payload normalization for dataclasses / `to_dict`,
   - JSON emit helper,
   - standard ok/error envelope helpers where applicable.
2. Migrate target CLI files to import shared helpers and delete duplicate local helper blocks.
3. Keep local wrapper functions only when module-specific metadata (e.g. `cmd`, `root`, `meta.generated_at`) is required.
4. Verify no command response contract changes by running targeted CLI UX tests.
5. Remove dead imports/functions left from migration.

## Verification
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest tests/test_team_cli_ux.py tests/test_workspace_cli_ux.py tests/test_ticket_ux.py tests/test_pack_cli_ux.py tests/test_loom_init_cli_ux.py`

## Acceptance criteria
- All listed CLIs use shared output helpers for serialization/emission primitives.
- Duplicated helper implementations are removed from migrated files.
- JSON and text mode behavior for existing commands remains unchanged in tests.
- Lint, type-check, and targeted CLI tests pass.

## Risks / edge cases
- **Risk:** subtle JSON shape drift (`ok`, `data`, `error`, metadata fields).
  - **Detection:** CLI UX test diffs and snapshot mismatches.
  - **Mitigation:** keep command-specific wrappers at call sites while centralizing only shared primitives.
- **Risk:** differing pretty/minified JSON expectations between CLIs.
  - **Detection:** failing tests and manual sample output checks.
  - **Mitigation:** make formatting strategy explicit in shared helper options instead of forcing one global format.

## Notes

**2026-02-15T20:22:59Z**

Execution boundary from al-8d66: this ticket owns only shared CLI serialization/emission contract extraction and migration in team/workspace/ticket/compound/pack/init CLI files. Do not alter argparse command trees or domain business logic. Keep CLI-specific envelopes where needed; centralize primitives only.

**2026-02-15T20:25:07Z**

**2026-02-15 (worker w9)**

Created shared CLI output module at `src/agent_loom/core/cli_output.py` with:
- `normalize_payload`: unify to_dict + dataclass serialization
- `emit_json`: configurable indent/minified output
- `make_ok_envelope`: standard {"ok": True, ...} wrapper
- `make_error_envelope`: standard error response

Now migrating each CLI file.
