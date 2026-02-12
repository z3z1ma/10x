---
name: cli-ux-regression-tests
description: Write durable CLI UX regression tests that lock behavior (stdout/stderr/exit codes) while staying low-noise and easy to evolve.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-11T23:42:15.329862Z"
  source_episode_ids: "3a041417a4e53b44eba76c7207d0fd7913dd9b5f79cc33443de6f61afaa9dad8,bff9823012420bd7cf1a60643401fd63d759d5e9f72788820421fceb2a78cf42,eabbfa5d9c3f54969ae5e5bd436f165f0fb90f9638c304f1007044108446648f"
  source_instinct_ids: "cli-ux-regression-tests,deterministic-cli-output,cli-changes-require-ux-regression-tests,cli-ux-contract-tests-for-output-changes,memory-note-ref-single-resolver,typed-result-exhaustive-cli-branching"
  tags: "cli,memory,regression,testing,ux"
  updated_at: "2026-02-11T23:42:15.329862Z"
  version: "3"
---
<!-- BEGIN:compound:skill-managed -->
# CLI UX Regression Tests

Use this when changing any Loom CLI user-facing behavior.

## Procedure

1. Define the UX contract first.
   - List expected `exit code`, `stdout`, and `stderr` for each scenario.
   - Include both success and at least one failure mode.

2. Add focused tests near the affected subsystem.
   - Prefer targeted files like `tests/test_memory_cli_ux.py`.
   - Assert exact high-signal lines instead of full-session snapshots.

3. Cover accepted input forms explicitly.
   - If commands accept multiple reference forms (for example note id/path-like/title-like), add one test per accepted form.
   - Add one not-found/invalid-reference test with expected error channel and code.

4. Make typed outcomes exhaustive.
   - When APIs return multiple result variants, branch explicitly in CLI code and add one test per variant.

5. Keep docs aligned with UX behavior.
   - Update command docs/readmes that describe accepted inputs or output semantics (for example `src/agent_loom/memory/README.md`).

6. Run quality gates before calling work done.
   - `uv run ruff check .`
   - `uv run basedpyright`
   - `uv run pytest <targeted-ux-test-file>`

## Done Checklist

- Every changed user-facing path has an explicit UX contract test.
- Exit-code and output-channel behavior is intentional and stable.
- Docs and tests reflect the same command semantics.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
