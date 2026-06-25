Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-control-fixture-record-graph-preservation-scn004-live-micro.md

# Control Fixture Record Graph Preservation Result

## What Was Observed

Ran `EXP-20260625-702-control-fixture-record-graph-preservation-scn004-live-micro`
with one repetition each for no-10x-control, current-10x, and a no-op candidate
arm.

Raw artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro/`

Canonical guard:

- `SKILL.md` before and after hash:
  `6fe94e63670f3354d6d675ce21ac1175e1ceb589be602417090da3c3f158fdd0`
- `autoresearch/program.md` before and after hash:
  `81032b42894e93727fd54ec1aa457edaa3a6e6e1a049dc2e76c52aab77c3d4d5`
- `unchanged_during_run`: `true`

Sample map:

| Arm | Workspace |
| --- | --- |
| no-10x-control | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro/workspaces/sha256-dcdf484103f2574c54876a24273bb7f3920cf8c405fa5826317fa8121c0a509c/` |
| current-10x | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro/workspaces/sha256-3d85c58bb262bbc562db0777700e2d1e359f6a3a24c88ee7a69b3028e8ec4dd0/` |
| candidate-variant | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro/workspaces/sha256-3381953d4448972e33b77f1fc5cb7a247952ef3abf90a23d6c00ea8b401af56a/` |

All three workspace manifests recorded:

- `pre_run_removed_control_record_dirs`: `[]`
- old spec path absent after run:
  `.10x/specs/payments-retry-window.md`
- new spec path present after run:
  `.10x/specs/payments-webhook-retry-policy.md`

No-10x-control changed the expected fixture record files:

- `.10x/evidence/2026-06-25-payments-retry-spec-inspection.md`
- `.10x/reviews/2026-06-25-payments-retry-naming-review.md`
- `.10x/specs/payments-webhook-retry-policy.md`
- `.10x/specs/superseded/payments-local-retry-notes.md`
- `.10x/tickets/2026-06-25-implement-payments-webhook-retry.md`

The no-10x-control final message stated it:

- renamed the active spec;
- repaired live `.10x` references;
- preserved historical prose and fenced command-output references to the old
  path;
- did not touch source files, create tickets, or run tests.

Current and no-op candidate produced the same expected changed-file set and
reported the same safety properties.

Trust Level 1 automated scoring:

- no-10x-control: S002=30
- current-10x: S002=30
- candidate-variant: S002=30

Manual inspection classifies these S002 scores as expected false negatives for
the harness sanity question. The scorer still treats preserved historical
old-path mentions as stale references, but the run proves the control arm now
has access to the fixture `.10x` task surface.

## Procedure

Executed:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-control-fixture-record-graph-preservation-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/179-control-fixture-record-graph-preservation-scn004-live-micro --require-clean-canonical
```

Manual inspection used:

- `plan.json` to map sample hashes to arms;
- `canonical_guard.json` to verify canonical files stayed unchanged;
- `report.md` for score vectors;
- archived workspace manifests for removed control record dirs and changed-file
  sets;
- archived workspaces for old/new spec path existence;
- final subject messages for whether no-10x-control saw and attempted the
  record graph task.

## What This Supports Or Challenges

This supports the harness fix in `autoresearch/run_codex_subject.py`: fixture
`seed-workspace` `.10x` records are preserved for no-10x-control when the record
graph is the task surface.

It also challenges prior EXP-701 no-10x-control results: those controls were
invalid for behavioral comparison because the task surface had been deleted.

## Limits

This is a harness sanity result, not `SKILL.md` behavioral evidence. It does not
show that no-10x-control is a good record maintainer; it only shows the control
can now see and attempt record-graph tasks in seed workspaces.
