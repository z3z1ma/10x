---
name: cli-ux-regression-tests
description: Write stable, high-signal CLI UX regression tests (stdout/stderr/exit codes) without brittle snapshots.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T05:53:52.854764Z"
  source_episode_ids: "3a041417a4e53b44eba76c7207d0fd7913dd9b5f79cc33443de6f61afaa9dad8,bff9823012420bd7cf1a60643401fd63d759d5e9f72788820421fceb2a78cf42"
  source_instinct_ids: "cli-ux-regression-tests,deterministic-cli-output,cli-changes-require-ux-regression-tests"
  tags: "cli,pytest,testing,ux"
  updated_at: "2026-02-09T05:53:52.854764Z"
  version: "2"
---
<!-- BEGIN:compound:skill-managed -->
# CLI UX Regression Tests

## When to use
- You changed a CLI command's output, flags, exit codes, error messages, or argument validation.
- You fixed a bug that users would experience via CLI.

## Procedure
1. Pick the smallest UX contract to lock in:
   - `returncode` (always)
   - a couple of stable substrings in `stdout` and/or `stderr`
   - avoid asserting exact whitespace, alignment, or full multi-line blocks unless the command is explicitly designed as a stable, versioned format.
2. Add at least one failure-path test:
   - missing file, invalid flag, invalid subcommand, or empty result
   - assert non-zero exit code and a helpful `stderr` fragment.
3. Prefer machine-readable modes when available:
   - if a command has `--json`, test semantic fields rather than free-form text.
   - if color could be enabled, pass `NO_COLOR=1` (or the project equivalent) in the test environment.
4. Run the command in a hermetic temp workspace:
   - use `tmp_path` for filesystem state
   - pass an explicit `cwd=tmp_path`
   - set environment variables explicitly (don't inherit flaky user env when avoidable).
5. Keep assertions minimal but meaningful:
   - assert the user-facing intent ("created", "not found", "0 results")
   - do not assert timings, ordering of unrelated lines, or absolute paths unless the path itself is the feature.

## Implementation template (pytest)
- Use `subprocess.run([...], text=True, capture_output=True)` with `check=False`.
- Assert:
  - `proc.returncode == 0` for success, `!= 0` for failure
  - `"expected fragment" in proc.stdout` or `proc.stderr`

## File placement
- Put tests in `tests/test_*_cli_ux.py` (or extend an existing UX test module for that subsystem).

## Review checklist
- Would this test still pass if help text formatting changes slightly?
- Does the test fail with a useful diff when behavior regresses?
- Does the test avoid coupling to the developer machine (paths, locale, shell config)?
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
