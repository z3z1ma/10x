Status: done
Created: 2026-06-27
Updated: 2026-06-28
Depends-On: .10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md

# Harden Autoresearch Baseline Replay Hygiene

## Scope

Remove the remaining replay and inspection friction found while running the
cross-harness seed baseline.

Included:

- Make the 25 continuation definitions with missing ignored prior raw artifacts
  replayable from tracked seed packages, or explicitly retire them from the
  seed-backed baseline index with durable rationale.
- Make the 19 older generated-workspace definitions either seed-backed or
  explicitly classified outside the seed-backed baseline.
- Reduce OpenCode `.opencode/node_modules` changed-file noise in archived
  workspaces and reports without hiding real subject changes.
- Make ad hoc OpenCode reruns fail fast with a clear prerequisite message or
  discover the installed binary path consistently.

Excluded:

- Reintroducing fixture-backed scoring, calibration fixtures, or automatic
  verdicts.
- Deleting historical research records only because they are not seed-backed.
- Hiding real subject mutations from workspace manifests.

## Acceptance Criteria

- AC-001: A fresh scientist can ask for "all seed-backed scenarios" and get a
  deterministic inventory whose exclusions are expected and documented.
- AC-002: Continuation experiments needed for the baseline do not depend on
  untracked `.10x/evidence/.storage` artifacts.
- AC-003: OpenCode mirror/skill scenarios still archive required artifacts, but
  generated dependency trees no longer dominate changed-file summaries.
- AC-004: OpenCode CLI prerequisite handling is explicit enough that direct
  `run_once.py` reruns do not fail with an unexplained `No such file or
  directory: 'opencode'`.
- AC-005: Evidence and review record the replay-hygiene result.

## Progress And Notes

- 2026-06-27: Opened from the cross-harness seed baseline. The campaign excluded
  44 registered definitions and observed six OpenCode changed-file manifests
  dominated by `.opencode/node_modules`.
- 2026-06-28: Implemented the deterministic replay boundary in tracked seed
  metadata: `autoresearch/trial-seeds/index.json` now records
  `baseline_replay_scope`, and
  `autoresearch/trial-seeds/baseline-exclusions.json` classifies the 25 ignored
  storage-dependent continuation definitions and 19 older generated-workspace
  definitions as outside the seed-backed baseline until promoted to tracked seed
  packages.
- 2026-06-28: Updated OpenCode live execution to resolve `OPENCODE_BIN`, `PATH`,
  or `~/.opencode/bin/opencode` before calling the subject, with a clear
  prerequisite error when unavailable.
- 2026-06-28: Filtered `.opencode/node_modules/**` from changed-file and
  `file_outputs` summaries while preserving archived workspaces plus suppression
  count/sample metadata in raw artifacts and workspace manifests.
- 2026-06-28: Recorded evidence in
  `.10x/evidence/2026-06-28-autoresearch-baseline-replay-hygiene.md` and pass
  review in
  `.10x/reviews/2026-06-28-autoresearch-baseline-replay-hygiene-review.md`.
  Closed this ticket.

## Blockers

None.

## References

- `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md`
- `.10x/evidence/2026-06-28-autoresearch-baseline-replay-hygiene.md`
- `.10x/reviews/2026-06-28-autoresearch-baseline-replay-hygiene-review.md`
- `.10x/evidence/.storage/2026-06-27-cross-harness-seed-experiment-baseline/campaign_manifest.json`
- `autoresearch/trial-seeds/index.json`
- `autoresearch/trial-seeds/baseline-exclusions.json`
- `autoresearch/run_subject.py`
