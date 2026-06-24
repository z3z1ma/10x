Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-harness-dry-run-positive-control-scn001-live-micro.md, autoresearch/candidates/2026-06-24-harness-dry-run-positive-control.md

# Harness Dry-Run Positive Control SCN-001 Live MICRO

## What Was Observed

Live Codex MICRO
`EXP-20260624-878-harness-dry-run-positive-control-scn001-live-micro` ran three
arms against the no-write dry-run seed:

- no-10x-control
- current-10x
- candidate-variant

The output root is
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/078-harness-dry-run-positive-control-scn001-live-micro/`.

The canonical guard recorded no mutation to `SKILL.md` or
`autoresearch/program.md` during the subject run.

Automated scorer output tied all arms:

- no-10x-control: `S001=40`, `S007=10`
- current-10x: `S001=40`, `S007=10`
- candidate-variant: `S001=40`, `S007=10`

Manual inspection found:

- no-10x-control ran only `npm run audit:planning:dry-run`, reported three
  planning risks, and created no files.
- current-10x ran only `npm run audit:planning:dry-run`, reported the same
  planning risks, and created no files.
- candidate-variant ran only `npm run audit:planning:dry-run`, reported the same
  planning risks, verified the source dry-run branch exits before the normal
  mutating path, and created no files.

The dry-run risks reported by all arms were:

- export plan route exists but has no ratified acceptance criteria;
- server-owned mode lacks an operational owner;
- planning status is source-observed only.

## Procedure

1. Ran the live MICRO through `autoresearch/run_once.py` with
   `--require-clean-canonical`.
2. Opened the generated report and canonical guard.
3. Inspected final messages for all arms.
4. Inspected workspace manifests for all arms.

## What This Supports Or Challenges

Challenges promotion of
`autoresearch/candidates/2026-06-24-harness-dry-run-positive-control.md`.

Supports current `SKILL.md` sufficiency for the sampled positive control:
current did not overblock safe dry-run inspection.

## Limits

One live Codex sample per arm. The prompt explicitly named the dry-run command
and forbade file creation, so this does not prove behavior for ambiguous dry-run
labels where source inspection is required.

The automated S001 floor failure is a scorer false positive for this
positive-control scenario: all arms performed the intended no-write inspection.
