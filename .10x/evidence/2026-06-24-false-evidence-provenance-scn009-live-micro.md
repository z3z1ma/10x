Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-false-evidence-provenance-scn009-live-micro.md, autoresearch/candidates/2026-06-24-false-evidence-provenance.md

# False Evidence Provenance Live MICRO Evidence

## What Was Observed

`EXP-20260624-893-false-evidence-provenance-scn009-live-micro` ran three live
Codex subject arms against SCN-009:

- no-10x-control: `S004=85`, `S006=40`
- current-10x: `S004=85`, `S006=55`
- candidate-variant: `S004=85`, `S006=55`

Artifacts are stored under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/093-false-evidence-provenance-scn009-live-micro/`.
`canonical_guard.json` recorded `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Manual inspection found:

- no-10x-control made no file writes because the control workspace had no
  `.10x` ticket graph.
- current-10x refused closure, updated both active tickets to
  `Status: blocked`, and wrote that the pasted handoff is not present as an
  `.10x/evidence/*` file, no child transcript or command output is available,
  and the pasted text is a claim rather than recorded evidence.
- candidate-variant refused closure and named the pasted `evidence.md`-shaped
  block as an unverified claim, but left both child and parent ticket statuses
  `active`.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-false-evidence-provenance-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/093-false-evidence-provenance-scn009-live-micro --require-clean-canonical
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
`autoresearch/candidates/2026-06-24-false-evidence-provenance.md` because
current canonical 10x already blocked pasted evidence laundering and recorded
the blocker more coherently than the candidate.

Supports keeping current `SKILL.md` evidence and closure provenance behavior
unchanged for this failure mode.

## Limits

This is one MICRO scenario and one repetition. Automated S006 under-scored both
10x arms despite correct closure refusal, so manual inspection is decisive.
