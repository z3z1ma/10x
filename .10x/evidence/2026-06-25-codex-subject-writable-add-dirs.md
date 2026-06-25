Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/tickets/done/2026-06-25-allow-codex-subject-writable-add-dirs.md, .10x/evidence/2026-06-24-skill-authoring-agents-mirror-confounder.md

# Codex Subject Writable Add Dirs

## What Was Observed

The Codex subject runner now supports an experiment definition field named
`writable_add_dirs`. The value must be a list of relative subject-workspace
paths. For each entry, the runner adds `--add-dir <workspace>/<relative-path>`
to the Codex CLI argv while retaining `--sandbox workspace-write`.

Focused unit coverage passed:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.514s

OK
```

Full autoresearch validation also passed:

```text
autoresearch contracts valid
```

```text
...........................................................
----------------------------------------------------------------------
Ran 59 tests in 18.391s

OK
```

`git diff --check` produced no output.

## Procedure

Commands run from `/Users/alexanderbutler/code_projects/personal/10x`:

```bash
python3 -m unittest autoresearch.tests.test_run_codex_subject
python3 autoresearch/validate.py
python3 -m unittest discover autoresearch/tests
git diff --check
```

The focused test suite covers:

- planned argv includes `--add-dir` for `.agents/skills`
- live `subprocess.run` receives the same `--add-dir`
- workspace manifests record `writable_add_dirs`
- non-list, empty, root, parent-traversal, and absolute values are rejected

## What This Supports Or Challenges

This supports using the Codex CLI live harness to fairly test `.agents/skills`
mirroring scenarios that require a subject to create new harness-native skill
directories.

It also supports treating the earlier
`.10x/evidence/2026-06-24-skill-authoring-agents-mirror-confounder.md` result
as a runner limitation rather than a product behavior result.

## Limits

This evidence does not prove `SKILL.md` succeeds at `.agents/skills` mirroring.
It proves the runner can now supply the necessary subject-workspace write
permission for a live experiment to test that behavior.

The change does not grant arbitrary host filesystem access. It only adds
configured relative paths inside the private subject workspace.
