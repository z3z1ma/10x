Status: done
Created: 2026-06-27
Updated: 2026-06-27
Depends-On: .10x/specs/10x-autoresearch-loop.md, .10x/tickets/2026-06-27-add-opencode-autoresearch-harness.md

# Simplify Autoresearch Subject Runner

## Scope

Remove confusing duplicate Codex-specific schema paths from the live subject
runner while preserving one canonical runner path for Codex, OpenCode, and
future subject harnesses.

Included:

- Emit one new-run command field, call counter, artifact directory field, and
  summary path shape regardless of harness.
- Keep legacy report fallbacks for old raw artifacts that contain
  `live_codex_calls` or old artifact-directory fields.
- Remove dead harness descriptor fields and unused helper paths.
- Keep harness-specific command construction behind one switch.
- Preserve rich raw command data for both Codex and OpenCode: stdout JSONL,
  stderr, normalized usage, last assistant message, transcript, tool events,
  prompt artifact, command metadata, workspace manifest, and archived workspace.
- Update tests, docs, evidence, and review.

Excluded:

- Deleting historical done records or old ignored `.storage` artifacts.
- Changing the scientific method, scorer policy, or canonical `SKILL.md`.
- Reintroducing fixture-backed scoring or automatic verdicts.

## Acceptance Criteria

- AC-001: New plans, summaries, samples, and raw artifacts use
  `planned_argv`, `live_subject_calls`, and `harness_artifact_dir` as the
  canonical schema; they do not emit `planned_codex_argv`,
  `planned_opencode_argv`, `live_codex_calls`, `codex_artifact_dir`, or
  `opencode_artifact_dir`.
- AC-002: Reports still read legacy artifacts that only contain
  `live_codex_calls` or old artifact-dir fields.
- AC-003: Codex and OpenCode command metadata both include raw stdout/stderr
  paths, normalized usage, command argv with prompt redacted, last assistant
  message path, working directory, and harness metadata.
- AC-004: Tests and validation pass.
- AC-005: Evidence and adversarial review record the simplification and any
  residual compatibility limits.

## Progress and Notes

- 2026-06-27: Opened after user requested one simple subject-runner path and
  removal of unnecessary Codex-specific duplicate code/schema.
- 2026-06-27: Removed duplicate new-run argv, call-count, and artifact-dir
  fields; collapsed `artifact_dirs` to one `harness` key; removed dead runner
  descriptor fields and unused arguments/constants; preserved report-only legacy
  fallbacks. Evidence:
  `.10x/evidence/2026-06-27-subject-runner-schema-simplification.md`. Review:
  `.10x/reviews/2026-06-27-subject-runner-schema-simplification-review.md`.

## Blockers

None.

## Closure

All acceptance criteria met. New outputs use the harness-neutral schema;
legacy names remain only in compatibility tests/report helpers and historical
records.
