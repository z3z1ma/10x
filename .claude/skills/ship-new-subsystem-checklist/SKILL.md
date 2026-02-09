---
name: ship-new-subsystem-checklist
description: A short procedure for shipping a new Loom subsystem (core + CLI + storage + docs + UX tests) without leaving sharp edges.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T06:31:32.792571Z"
  source_episode_ids: "8b9d287c8371fa5c2a007b3e600278223256c6ef8a0e529b9ac018277992691f"
  source_instinct_ids: "cli-ux-tests-for-new-commands,document-new-subsystem-entrypoints,ignore-new-persistent-artifacts,prefer-basedpyright-over-lsp-diagnostics"
  tags: "cli,docs,git,process,python,subsystem,testing"
  updated_at: "2026-02-09T06:31:32.792571Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Ship New Subsystem Checklist

Use this when you add a new Loom subsystem or a major slice of one (new CLI noun/verb + new storage/indexing + multiple new modules).

## Procedure

1. Define the public contract
   - Decide the CLI shape (`loom <noun> <verb> ...`) and failure semantics (exit codes, stderr vs stdout).
   - Ensure there is a stable machine-readable mode when appropriate (e.g., `--json`).

2. Implement the core first
   - Put domain behavior in `src/agent_loom/<subsystem>/core.py` (or equivalent).
   - Keep side effects (I/O, printing) out of core where possible.

3. Add storage/indexing deliberately
   - Introduce models/types in `src/agent_loom/<subsystem>/models.py`.
   - If there is search/recall/indexing logic, isolate it in its own module (e.g., `recall.py`).
   - Decide where on disk persistent artifacts live; document reset semantics.

4. Wire the CLI entrypoints
   - Implement `src/agent_loom/<subsystem>/cli.py` as a thin layer over core.
   - Standardize error messages for common failure modes (missing args, not initialized, empty results).

5. Add docs at the subsystem level
   - Create/update `src/agent_loom/<subsystem>/README.md` with:
     - Purpose + mental model
     - Data locations
     - Key commands with examples
     - One "smoke path" to validate behavior

6. Add git hygiene
   - Update `.gitignore` for any new persistent artifacts (db/index/cache/tmp).

7. Add CLI UX regression tests
   - Add `tests/test_<subsystem>_cli_ux.py` that asserts:
     - Exit code
     - A few stable stdout/stderr lines (avoid brittle full snapshots)
     - At least one failure-path message

8. Run quality gates
   - `uv run ruff check .`
   - `uv run basedpyright`
   - `uv run pytest`

## Done Criteria
- Users can discover commands via `--help`, run a smoke path, and understand where data is stored.
- New persistent artifacts are ignored and documented.
- UX tests cover at least one happy path and one failure path.
- Ruff + basedpyright + pytest are clean.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
