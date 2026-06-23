Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/tickets/done/2026-06-23-isolate-no-10x-control-record-graph.md

# No-10x Control Record Graph Isolation

## What Was Observed

The live Codex subject runner now removes inherited `.10x` only from
`no-10x-control` execution workspaces before launching Codex.

Regression coverage:

- `CodexSubjectRunnerTest.test_no_10x_control_drops_inherited_record_graph_before_execution`
  seeds `.10x/knowledge/seed.md` into every prior workspace.
- The mocked Codex process observes `.10x` absent for `no-10x-control`.
- The mocked Codex process observes `.10x` present for `current-10x` and
  `candidate-variant`.
- The control writes `.10x/knowledge/control-created.md` during execution, and
  the archived manifest includes that file while excluding the inherited seed.
- Current and candidate archived manifests still include the inherited seed.

Validation output:

```text
python3 -m unittest autoresearch.tests.test_run_codex_subject
.......
----------------------------------------------------------------------
Ran 7 tests in 0.370s

OK
```

```text
python3 -m unittest discover -s autoresearch/tests
................................................
----------------------------------------------------------------------
Ran 48 tests in 11.545s

OK
```

```text
python3 autoresearch/validate.py
autoresearch contracts valid
```

```text
git diff --check
```

`git diff --check` produced no output.

## Procedure

Commands run from `/Users/alexanderbutler/code_projects/personal/10x`:

```text
python3 -m unittest autoresearch.tests.test_run_codex_subject
python3 -m unittest discover -s autoresearch/tests
python3 autoresearch/validate.py
git diff --check
```

Manual diff inspection checked:

- `autoresearch/run_codex_subject.py`
- `autoresearch/tests/test_run_codex_subject.py`

## What This Supports Or Challenges

This supports the claim that `no-10x-control` no longer inherits a seeded
`.10x` record graph through prior raw artifacts while current and candidate
continuation behavior remains intact.

It also supports that control-created `.10x` output remains visible to scoring
and manual inspection.

## Limits

The regression uses a mocked Codex subprocess, not a live Codex call. It proves
runner workspace preparation and artifact capture semantics, not model behavior.
It does not re-evaluate prior live experiment verdicts.
