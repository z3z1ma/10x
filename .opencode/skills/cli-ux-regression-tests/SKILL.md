---
name: cli-ux-regression-tests
description: Procedure for adding stable, high-signal CLI UX regression tests (stdout/stderr/exit codes) without making brittle assertions.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T04:40:42.182303Z"
  source_episode_ids: "3a041417a4e53b44eba76c7207d0fd7913dd9b5f79cc33443de6f61afaa9dad8"
  source_instinct_ids: "cli-ux-regression-tests,deterministic-cli-output"
  tags: "cli,pytest,testing,ux"
  updated_at: "2026-02-09T04:40:42.182303Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# CLI UX Regression Tests

Use this when you change CLI output/flags/errors and want durable regression coverage.

## Procedure

1. Pick the narrowest invocation surface.
   - If the CLI is built on Typer/Click: use the framework test runner.
   - If the CLI is a thin wrapper over Python functions: call the function directly and capture output.

2. Write a focused pytest in `tests/test_<area>_ux.py`.
   - One test per user story (e.g. `ticket show`, `ticket update`, invalid args).
   - Assert `exit_code`, `stdout`, `stderr`.

3. Assert *stable* strings.
   - Prefer exact multi-line output comparisons using `textwrap.dedent`.
   - Avoid asserting volatile data (timestamps, temp paths, random IDs). If unavoidable, control/freeze it.

4. Keep formatting expectations intentional.
   - Cover newline behavior (exact output, trailing newline).
   - Cover ordering (sorted lists) if multiple items are printed.

5. Run the smallest loop first.
   - `uv run pytest -k ux`

## Framework runners (choose one)

Typer:

```python
from typer.testing import CliRunner

runner = CliRunner()
result = runner.invoke(app, ["ticket", "show", "..."])
assert result.exit_code == 0
assert result.stdout == "...\n"
```

Click:

```python
from click.testing import CliRunner

runner = CliRunner()
result = runner.invoke(cli, ["ticket", "show", "..."])
assert result.exit_code == 0
assert result.output == "...\n"
```
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
