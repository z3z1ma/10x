Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/tickets/done/2026-06-23-isolate-live-subject-workspaces.md

# Isolate No-10x Control Record Graph

## Scope

Fix the live Codex subject runner so a `no-10x-control` sample cannot inherit a
preexisting `.10x` record graph from a seeded or continuation workspace.

Included:

- Remove inherited `.10x` from the private execution workspace only for
  `no-10x-control` before launching Codex.
- Preserve inherited `.10x` for current and candidate arms so continuation and
  retrieval scenarios can still evaluate record use.
- Continue capturing any `.10x` records the control creates during its own run.
- Record the removal in command, raw artifact, and workspace manifest metadata.
- Add a regression test covering inherited-control cleanup.

Excluded:

- Changing scorer behavior.
- Deleting `.10x` from current or candidate arms.
- Deleting `.10x` after a control run completes.
- Re-running prior experiments.

## Acceptance Criteria

- AC-001: In a prior-workspace continuation where all arms start with `.10x`,
  `no-10x-control` starts execution without inherited `.10x`.
- AC-002: In the same continuation, current and candidate arms still start with
  the inherited `.10x`.
- AC-003: If `no-10x-control` creates `.10x` during its own run, those files are
  archived and scoreable.
- AC-004: Workspace manifests report which control record directories were
  removed before execution.
- AC-005: `python3 -m unittest discover -s autoresearch/tests`,
  `python3 autoresearch/validate.py`, and `git diff --check` pass.

## Progress and Notes

- 2026-06-23: Opened after operator noted that `no-10x-control` should delete a
  preexisting `.10x` folder if one exists. Existing generated-workspace runs
  did not start with `.10x`, but seeded/continuation workspaces could inherit
  one through `prior_raw_paths`.
- 2026-06-23: Added `SUPPRESSED_CONTROL_RECORD_DIRS = [".10x"]` and
  `_remove_inherited_control_records()` to
  `autoresearch/run_codex_subject.py`.
- 2026-06-23: The cleanup runs after the prior workspace is copied into the
  private temporary execution workspace and before Codex launches. It is scoped
  to `variant_id == "no-10x-control"`.
- 2026-06-23: Added
  `CodexSubjectRunnerTest.test_no_10x_control_drops_inherited_record_graph_before_execution`.
  The test seeds `.10x` into every prior workspace, confirms only the control
  starts without it, and confirms a control-created `.10x` file remains
  archived.
- 2026-06-23: Verified the focused runner test, full test suite, validator, and
  diff whitespace check.

## Blockers

None.
