---
name: compound-install-contract-testing
description: Use when changing src/agent_loom/compound/install.py or src/agent_loom/compound/cli.py to keep installed .opencode outputs deterministic and covered by tests/test_compound_install.py.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-01T04:25:40.311Z"
  updated_at: "2026-02-01T04:25:40.311Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You changed `src/agent_loom/compound/install.py`.
- You changed `src/agent_loom/compound/cli.py` in a way that affects installation/scaffolding.
- You changed any file that is expected to be installed/generated under `.opencode/`.
- You changed Compound-managed templates that are mirrored under `src/agent_loom/compound/opencode/.opencode/` (including `.opencode/plugins/*`).

## Goal

Keep Compound installation outputs deterministic and regression-tested.

## Checklist

1. Identify the install contract
   - What files must be created under `.opencode/`?
   - Pay special attention to:
     - `.opencode/skills/`
     - `.opencode/commands/`
     - `.opencode/plugins/` (for example `.opencode/plugins/compound_engineering.ts`)
   - Which files are templates mirrored under `src/agent_loom/compound/opencode/.opencode/`?
     - For plugins, ensure `.opencode/plugins/*` stays in sync with `src/agent_loom/compound/opencode/.opencode/plugins/*`.
   - Which files must be gitignored (for example `.opencode/memory/observations.jsonl`)?

2. Ensure deterministic content
   - Stable ordering (no set/dict iteration).
   - No timestamps, random IDs, or machine-specific absolute paths.

3. Prevent template drift
   - If you update a file in `.opencode/`, update its mirror under `src/agent_loom/compound/opencode/.opencode/` in the same change.
   - Prefer making `tests/test_compound_install.py` assert:
     - both copies exist for mirrored assets
     - key markers/blocks exist in the installed outputs (avoid full-file snapshots unless the full file is the contract)

4. Update/add contract tests
   - Edit `tests/test_compound_install.py` to assert:
     - required files exist
     - required file contents include key markers/blocks
     - gitignore entries are present and correct

5. Verification gate
   - `uv run basedpyright`
   - `uv run ruff check .`
   - `uv run pytest tests/test_compound_install.py`

## Common failure modes

- Template drift between `.opencode/` and `src/agent_loom/compound/opencode/.opencode/`.
- Tests asserting full file contents that include nondeterministic data.
- Installing files that should be ignored/ephemeral (logs, observations) without adding `.gitignore` rules.
- Plugin changes not mirrored (especially `.opencode/plugins/*`), causing installs to diverge from repo state.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
