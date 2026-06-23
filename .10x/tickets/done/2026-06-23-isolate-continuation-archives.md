Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-increase-autoresearch-throughput.md
Depends-On:

# Isolate Continuation Archives

## Scope

Fix live Codex continuation runs so `prior_raw_paths` seed the next run's
workspace without causing the next run to archive back over the prior
experiment's workspace.

Included:

- Treat the prior workspace as a seed input.
- Archive every continuation sample under the new experiment output root.
- Preserve `prior_raw_path` transcript continuity.
- Record `seed_workspace_dir` in raw harness metadata and returned samples.
- Update continuation tests to assert new output workspaces are used.

Excluded:

- Changing conversation continuation semantics.
- Changing score definitions.
- Changing candidate instructions.
- Running a live continuation as part of this ticket.

## Acceptance Criteria

- AC-001: Continuation raw artifacts still contain the combined prior and new
  transcript.
- AC-002: Continuation workspaces are archived under the new output root, not
  the prior workspace path.
- AC-003: The seed workspace path is preserved in raw harness metadata for
  auditability.
- AC-004: No-10x inherited `.10x` cleanup still applies to seeded continuation
  workspaces.
- AC-005: `python3 -m unittest discover -s autoresearch/tests`,
  `python3 autoresearch/validate.py`, and `git diff --check` pass.

## Progress and Notes

- 2026-06-23: Opened after throughput audit found `run_codex_subject.py`
  reused prior workspace paths from `prior_raw_paths` as archive destinations,
  making shared continuation seeds unsafe for parallel runs and mutating older
  experiment workspaces.
- 2026-06-23: Updated `build_plan()` so every sample archives under
  `artifact_dirs["workspaces"] / stem`, while `planned_seed_workspace_dir`
  records the prior workspace when present.
- 2026-06-23: Updated `_run_sample()` to copy from the seed workspace first,
  then archive results to the new output workspace.
- 2026-06-23: Updated continuation tests to assert output manifests live under
  the new run's `out/workspaces` directory and that no-10x record-graph cleanup
  still works for seeded workspaces.
- 2026-06-23: Focused runner tests passed:
  `python3 -m unittest autoresearch.tests.test_run_codex_subject`.

## Blockers

None.
