Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Relates-To: .10x/tickets/2026-06-27-simplify-autoresearch-subject-runner.md, .10x/specs/10x-autoresearch-loop.md

# Subject Runner Schema Simplification Evidence

## What Was Observed

The live subject runner now emits one harness-neutral schema for new Codex and
OpenCode runs:

- `planned_argv`
- `live_subject_calls`
- `harness_artifact_dir`
- `artifact_dirs.harness`

It no longer emits duplicate new-run fields such as `planned_codex_argv`,
`planned_opencode_argv`, `planned_subject_argv`, `live_codex_calls`,
`codex_artifact_dir`, or `opencode_artifact_dir`.

Legacy report readers still normalize older artifact fields into the current
names.

## Procedure

Focused verification:

```bash
python3 -m unittest autoresearch.tests.test_run_subject autoresearch.tests.test_run_once autoresearch.tests.test_report
python3 -m py_compile autoresearch/run_subject.py autoresearch/run_once.py autoresearch/report.py
```

Observed:

- `Ran 37 tests in 9.248s`
- `OK`
- `py_compile` exited zero.

Schema dry-run:

```bash
python3 autoresearch/run_subject.py \
  --experiment .10x/evidence/.storage/2026-06-27-opencode-smoke/experiment.json \
  --dry-run \
  --out /tmp/10x-opencode-schema-check
```

Observed parsed plan summary:

```json
{
  "artifact_dir_keys": ["harness", "prompts", "raw", "workspaces"],
  "has_planned_argv": true,
  "old_argv_keys": [],
  "has_live_subject_calls": true,
  "has_live_codex_calls": false
}
```

Full verification:

```bash
python3 -m unittest discover autoresearch/tests
python3 autoresearch/validate.py
python3 -m py_compile autoresearch/*.py
```

Observed:

- `Ran 54 tests in 16.872s`
- `OK`
- `autoresearch contracts valid`
- `py_compile` exited zero.

## What This Supports Or Challenges

Supports:

- There is one active runner path: `autoresearch/run_once.py` delegates to
  `autoresearch/run_subject.py`.
- New runner outputs use one schema across Codex and OpenCode.
- OpenCode-style nested `part.tokens` and Codex-style top-level `usage` both
  normalize into raw artifact `usage`.
- Codex raw artifacts now preserve the same normalized `usage` field already
  used by OpenCode, while both harnesses preserve transcript, raw stdout JSONL,
  stderr, command metadata, prompt artifact, last assistant message, tool
  invocations, workspace manifest, and archived workspace references.
- Report compatibility for old `live_codex_calls` is explicit and tested.

Challenges / findings handled:

- Removed unused harness descriptor fields.
- Removed the unused scenario path constant and unused `_run_sample` parameter.
- Removed duplicate planned argv fields and per-harness summary artifact-dir
  fields from new outputs.

## Limits

- Historical `.10x/` records and old ignored `.storage` artifacts may mention
  old field names because they describe older runs. Active code and docs now use
  the neutral schema.
