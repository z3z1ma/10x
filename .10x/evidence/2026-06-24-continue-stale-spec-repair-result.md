Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-continue-stale-spec-repair-scn004-live-micro.md, .10x/research/2026-06-24-10x-conformance-coverage-map.md

# Continue Stale Spec Repair Result

## What Was Observed

`EXP-20260624-967-continue-stale-spec-repair-scn004-live-micro` ran one live
Codex turn for each arm:

- current-10x: `sha256-ead5ac3a04e9984e24a58f31b8e61674bab7791cbe6a7f975743cc6c461426c4`
- candidate-variant: `sha256-5d8a14ad22fc9812054973d7d03fbb1842a313fbfc57a0d5e99391584fbe5ce0`
- no-10x-control: `sha256-df420aa11eae45181b8fa4c068be571356eb764d6c11b76bdcbc270e91f99851`

Trust Level 1 offline S002 scored current and duplicate-current at `30`, and
control at `15`. Manual inspection overrode the low heuristic scores.

Current `SKILL.md` reused the existing repair ticket, moved it to
`.10x/tickets/done/2026-06-24-repair-audit-export-spec.md`, preserved the stale
CSV-only contract at `.10x/specs/superseded/audit-export-csv-only.md`, replaced
`.10x/specs/audit-export.md` with the active JSON API route contract, repaired
evidence/review references, and recorded
`.10x/evidence/2026-06-24-audit-export-spec-repair-verification.md`.

Candidate-variant also completed the repair and closed the ticket, but replaced
the stale spec in place instead of preserving an explicit superseded record.
That was allowed by the seed but lower-quality than current's graph-preserving
repair.

No-10x-control blocked because its isolated workspace correctly had no `.10x`
record graph to continue.

## Procedure

Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-continue-stale-spec-repair-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/167-continue-stale-spec-repair-scn004-live-micro --require-clean-canonical
```

Inspected the saved subject workspaces and last messages under:

```text
.10x/evidence/.storage/2026-06-23-skill-autoresearch/167-continue-stale-spec-repair-scn004-live-micro/
```

Manual checks verified current's active spec, superseded spec, moved repair
ticket, repair evidence, pre-repair review reference target, and stale-language
search results.

## What This Supports Or Challenges

This supports the record graph maintenance mechanics lane in
`.10x/research/2026-06-24-10x-conformance-coverage-map.md`. It shows current
`SKILL.md` can continue a previously opened record-repair owner, distinguish
active authority from superseded history, preserve provenance, and close record
maintenance work without creating duplicate tickets or source-revert work.

It does not support a `SKILL.md` promotion because current passed and no
candidate behavior improved over current.

## Limits

This was a prompted repeated-session MICRO with an explicit stale-spec repair
ticket. It does not prove behavior under subtler stale-record discovery, a
partially wrong prior repair, or longer multi-session maintenance. The offline
S002 scorer produced false-negative low scores, so the durable verdict depends
on manual inspection.
