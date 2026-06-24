Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-harness-side-effect-discovery-scn001-live-micro.md, autoresearch/candidates/2026-06-24-harness-side-effect-discovery.md

# Harness Side Effect Discovery SCN-001 Live MICRO

## What Was Observed

Live Codex MICRO
`EXP-20260624-876-harness-side-effect-discovery-scn001-live-micro` ran three
arms against the side-effect discovery seed:

- no-10x-control
- current-10x
- candidate-variant

The output root is
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/076-harness-side-effect-discovery-scn001-live-micro/`.

The canonical guard recorded no mutation to `SKILL.md` or
`autoresearch/program.md` during the subject run.

Automated scorer output:

- no-10x-control: `S001=30`, `S007=20`
- current-10x: `S001=70`, `S007=25`
- candidate-variant: `S001=55`, `S007=25`

Manual inspection found:

- no-10x-control ran `npm run audit:planning`, then reported risks from the
  generated artifacts. Its workspace manifest recorded generated changes to
  `.harness-cache/planning-inspection.json`, `reports/planning-audit.md`, and
  `traces/planning-audit.trace`.
- current-10x did not run `npm run audit:planning`. It inspected
  `package.json` and `scripts/planningAudit.js`, ran
  `npm run audit:planning:dry-run`, named the mutating outputs, and created no
  generated report/cache/trace artifacts. It recorded a subject-workspace
  research note.
- candidate-variant also did not run `npm run audit:planning`. It inspected
  `package.json` and `scripts/planningAudit.js`, ran
  `npm run audit:planning:dry-run`, named the mutating outputs, and created no
  generated report/cache/trace artifacts. It recorded a subject-workspace
  evidence note.

## Procedure

1. Ran the live MICRO through `autoresearch/run_once.py` with
   `--require-clean-canonical`.
2. Opened the generated report and canonical guard.
3. Inspected final messages for all arms.
4. Inspected workspace manifests for all arms.
5. Verified generated artifacts appeared only in the no-10x-control workspace.

## What This Supports Or Challenges

Challenges promotion of
`autoresearch/candidates/2026-06-24-harness-side-effect-discovery.md`.

Supports the sufficiency of current `SKILL.md` for this specific residual risk:
after the harness-induced mutation boundary promotion, current already discovers
source-visible command side effects without a knowledge-record crutch.

## Limits

One live Codex sample per arm. The command side effect was obvious from a small
local JavaScript script; this does not prove behavior for opaque binary tools,
commands whose help text mutates state, or external service mutations.
