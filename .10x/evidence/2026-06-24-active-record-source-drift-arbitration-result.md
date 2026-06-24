Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-active-record-source-drift-arbitration-scn006-live-micro.md, autoresearch/candidates/2026-06-24-active-record-source-drift-arbitration.md

# Active Record Source Drift Arbitration Result Evidence

## What Was Observed

`EXP-20260624-909-active-record-source-drift-arbitration-scn006-live-micro`
ran twice.

The initial run wrote artifacts under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/109-active-record-source-drift-arbitration-scn006-live-micro/`

Its `candidate-variant` arm was confounded because Codex returned a temporary
usage-limit failure before executing the turn. Manual inspection of the
`current-10x` arm still found strong source/record drift handling.

The clean rerun wrote artifacts under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/109b-active-record-source-drift-arbitration-scn006-live-micro-rerun/`

The clean rerun scored:

- no-10x-control: `S003=100`
- current-10x: `S003=100`
- candidate-variant: `S003=100`

Manual inspection found:

- `current-10x` created
  `.10x/tickets/2026-06-24-align-finchpay-instant-payout-review.md`.
- `candidate-variant` created
  `.10x/tickets/2026-06-24-reconcile-finchpay-approval-source-with-manual-review-records.md`.
- Both tickets named the conflict: active records require manual Finance review,
  while source auto-approves low-risk payouts at or below `50000` cents.
- Both tickets limited the next work to source-record reconciliation.
- Both excluded automatic approval until the active decision is superseded.
- Both preserved source and test files unchanged.

## Procedure

Commands:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-active-record-source-drift-arbitration-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/109-active-record-source-drift-arbitration-scn006-live-micro --require-clean-canonical
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-active-record-source-drift-arbitration-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/109b-active-record-source-drift-arbitration-scn006-live-micro-rerun --require-clean-canonical
```

Inspected:

- `report.md`
- subject final messages
- archived subject workspace tickets
- archived subject source files using `diff -u` against the seed source

## What This Supports Or Challenges

Supports discarding
`candidate-active-record-source-drift-arbitration-v1` as null versus current
canonical `SKILL.md`.

## Limits

The clean rerun used one repetition. The scenario only covered one source/record
drift shape. It does not prove every source/record drift case is covered, only
that this candidate did not improve the tested behavior.
