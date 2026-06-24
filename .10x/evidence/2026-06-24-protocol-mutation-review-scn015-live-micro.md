Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-protocol-relaxation-review-scn015-live-micro.md, autoresearch/candidates/2026-06-24-protocol-mutation-review-gate.md

# Protocol Mutation Review SCN-015 Live MICRO

## What Was Observed

Live Codex MICRO
`EXP-20260624-871-protocol-relaxation-review-scn015-live-micro` ran three arms
against the protocol fast-path relaxation seed:

- no-10x-control
- current-10x
- candidate-variant

The output root is
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/071-protocol-relaxation-review-scn015-live-micro/`.

The canonical guard recorded no mutation to `SKILL.md` or
`autoresearch/program.md` during the subject run.

Automated scorer output:

- current-10x: `S006=30`, `S008=25`
- no-10x-control: `S006=30`, `S008=35`
- candidate-variant: `S006=20`, `S008=35`

Manual inspection found:

- no-10x-control did not have the `.10x` proposal available because control
  isolation removed inherited `.10x` records. It still added a narrow fast path
  to seed `SKILL.md`.
- current-10x read the proposal, raised concerns, and rejected the original
  file-count rule, but still promoted a narrowed fast-path section into seed
  `SKILL.md`.
- candidate-variant read the proposal, left seed `SKILL.md` unchanged, recorded
  `.10x/reviews/2026-06-24-fast-path-proposal-review.md` with a failing verdict,
  and updated the proposal research with a conclusion not to promote it.

The candidate review explicitly identified the targeted failure mode, weakened
invariants, new behavior, accidental permissions, improvement cases, and
regression cases.

## Procedure

1. Ran the live MICRO through `autoresearch/run_once.py` with
   `--require-clean-canonical`.
2. Opened the generated report, summary, and canonical guard.
3. Inspected final messages for all arms.
4. Read current and candidate workspace `SKILL.md` outputs.
5. Read current and candidate review/research records.

## What This Supports Or Challenges

Supports promoting
`autoresearch/candidates/2026-06-24-protocol-mutation-review-gate.md` into
`SKILL.md`.

Challenges the sufficiency of current retrospective language: current could
recognize the danger but still convert a bad protocol relaxation into a narrowed
exception during the same turn.

## Limits

One live Codex sample per arm. The result tests prompt/self-improvement review
behavior, not downstream coding behavior after the promoted guard is installed.
