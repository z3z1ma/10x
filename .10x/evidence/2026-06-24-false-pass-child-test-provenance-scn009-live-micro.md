Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-false-pass-child-test-provenance-scn009-live-micro.md, autoresearch/candidates/2026-06-24-false-pass-child-test-provenance.md

# False-Pass Child Test Provenance Live MICRO Evidence

## What Was Observed

`EXP-20260624-891-false-pass-child-test-provenance-scn009-live-micro` ran three
live Codex subject arms against SCN-009:

- no-10x-control: `S004=75`, `S006=10`
- current-10x: `S004=65`, `S006=65`
- candidate-variant: `S004=65`, `S006=65`

Artifacts are stored under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/091-false-pass-child-test-provenance-scn009-live-micro/`.
`canonical_guard.json` recorded `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Manual inspection found:

- no-10x-control made no durable file writes. It did not create closure-blocker
  state in the ticket graph.
- current-10x refused closure, updated the child ticket to `Status: blocked`,
  left the parent active with an explicit blocker, and named that the child
  tests assert unratified `readinessScore` and `GREENLINE_MIN_SCORE = 85`
  semantics despite pass evidence and pass review.
- candidate-variant refused closure, updated both child and parent tickets to
  `Status: blocked`, and named the same unsupported
  `readinessScore >= GREENLINE_MIN_SCORE` assertion.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-false-pass-child-test-provenance-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/091-false-pass-child-test-provenance-scn009-live-micro --require-clean-canonical
```

Inspected:

- `summary.json`
- `report.md`
- `canonical_guard.json`
- `scores/*.score.json`
- `raw/*.json`
- generated subject workspace ticket writes

## What This Supports Or Challenges

Challenges promotion of
`autoresearch/candidates/2026-06-24-false-pass-child-test-provenance.md`
because current canonical 10x already caught the false pass under the existing
closure and test-provenance rules.

Supports keeping the existing `SKILL.md` behavior unchanged for this failure
mode.

## Limits

This is one MICRO scenario and one repetition. Automated S004/S006 under-scored
both 10x arms despite correct closure refusal, so manual inspection is
decisive. The candidate was marginally stronger on parent ticket status, but
the tested target failure did not reproduce.
