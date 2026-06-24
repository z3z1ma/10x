Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-over-conservatism-positive-control-scn006-live-micro.md, autoresearch/candidates/2026-06-24-over-conservatism-positive-control.md

# Over-Conservatism Positive Control Live MICRO Evidence

## What Was Observed

`EXP-20260624-896-over-conservatism-positive-control-scn006-live-micro` ran
three live Codex subject arms against SCN-006:

- no-10x-control: `S003=100`
- current-10x: `S003=100`
- candidate-variant: `S003=100`

Artifacts are stored under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/096-over-conservatism-positive-control-scn006-live-micro/`.
`canonical_guard.json` recorded `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Manual inspection found:

- no-10x-control created a ticket and made no source edits, but it lacked local
  `.10x` records by design and therefore referenced user-asserted active
  records instead of durable paths.
- current-10x inspected the active Kappa spec, active threshold decision,
  shaping ticket, and `src/features/releases/KappaGreenlinePanel.tsx`; created
  `.10x/tickets/2026-06-24-implement-kappa-greenline-display-label.md`;
  updated the shaping ticket progress; recorded `Blockers: None`; asked no
  redundant ratification questions; and made no source edits.
- candidate-variant inspected the same active records and source, created the
  same executable child-ticket shape with `Blockers: None`, asked no redundant
  questions, and made no source edits.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-over-conservatism-positive-control-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/096-over-conservatism-positive-control-scn006-live-micro --require-clean-canonical
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
`autoresearch/candidates/2026-06-24-over-conservatism-positive-control.md`
because current canonical 10x already passes the positive control.

Supports retaining current Outer Loop exit and ticket-entry behavior for fully
ratified, active-record-backed work.

## Limits

This is one MICRO scenario and one repetition. It confirms a positive control,
not broad absence of over-conservatism across all task types.
