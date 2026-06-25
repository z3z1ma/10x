Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-control-fixture-record-graph-preservation-scn004-live-micro.md
Verdict: pass

# Control Fixture Record Graph Preservation Review

## Target

Manual review of
`.10x/research/2026-06-25-control-fixture-record-graph-preservation-scn004-live-micro.md`
and raw artifacts under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro/`.

## Findings

- Pass: no-10x-control manifest recorded no fixture `.10x` removal:
  `pre_run_removed_control_record_dirs` was `[]`.
- Pass: no-10x-control archived workspace contained the fixture record graph and
  completed the requested spec rename/reference repair task.
- Pass: no-10x-control did not report `.10x` missing, which was the EXP-701
  harness failure.
- Pass: current-10x and the no-op candidate arm retained normal behavior on the
  same fixture.
- Pass: canonical `SKILL.md` and `autoresearch/program.md` hashes were unchanged
  during the run.
- Minor: S002 still false-negatives this scenario because preserved historical
  old-path references look stale to the heuristic scorer.
- Minor: the no-op candidate arm exists only to satisfy the current comparative
  runner shape and should not be interpreted as candidate evidence.

## Verdict

Pass. The control fixture record graph preservation fix is working for
`seed-workspace` fixtures.

## Residual Risk

The runner still needs careful scenario design: no-10x-control cleanup remains
appropriate for inherited continuation record graphs, but fixtures that use
`.10x` as the mock repository task surface must declare `harness_metadata.kind`
as `seed-workspace`.
