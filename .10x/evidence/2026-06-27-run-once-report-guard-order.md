Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Relates-To: .10x/tickets/2026-06-27-fix-run-once-report-guard-order.md

# Run Once Report Guard Order Evidence

## What Was Observed

`run_once.py` now writes `canonical_guard.json` before rendering `report.md`.
The current cross-harness reports list the guard paths instead of `not found`.

## Procedure

Commands run:

```bash
python3 -m unittest autoresearch.tests.test_run_once
python3 -m unittest discover -s autoresearch/tests
python3 autoresearch/validate.py
python3 -m py_compile autoresearch/*.py
git diff --check
python3 autoresearch/report.py --artifacts .10x/evidence/.storage/2026-06-27-cross-harness-complex/codex --out .10x/evidence/.storage/2026-06-27-cross-harness-complex/codex/report.md
python3 autoresearch/report.py --artifacts .10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode --out .10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode/report.md
rg -n "canonical_guard.json" .10x/evidence/.storage/2026-06-27-cross-harness-complex/*/report.md
```

Results:

- `python3 -m unittest autoresearch.tests.test_run_once`: 11 tests, OK.
- `python3 -m unittest discover -s autoresearch/tests`: 56 tests, OK.
- `python3 autoresearch/validate.py`: `autoresearch contracts valid`.
- `python3 -m py_compile autoresearch/*.py`: OK.
- `git diff --check`: OK.
- Re-rendered reports list:
  - `.10x/evidence/.storage/2026-06-27-cross-harness-complex/codex/canonical_guard.json`
  - `.10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode/canonical_guard.json`

## What This Supports Or Challenges

Supports that report rendering now sees the guard artifact produced by the same
run or by re-rendering from an existing run directory.

## Limits

The subject-agent raw outputs were not rerun for this fix; only reports were
re-rendered from existing artifacts.
