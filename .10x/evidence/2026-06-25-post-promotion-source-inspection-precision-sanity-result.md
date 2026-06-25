Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-post-promotion-source-inspection-precision-sanity-live-micro.md

# Post-Promotion Source Inspection Precision Sanity Result

## What Was Observed

EXP-20260625-713 ran 9 live Codex subject calls:

- 3 scenarios: source-inspection decoy pressure, multi-surface source/record
  drift, and harness-induced mutation boundary;
- 3 arms: no-10x-control, current-10x, and candidate-variant with a no-op
  overlay;
- 1 repetition per arm/scenario.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/190-post-promotion-source-inspection-precision-sanity-live-micro/`

`canonical_guard.json` recorded unchanged hashes for:

- `SKILL.md`
- `autoresearch/program.md`

Current-10x primary decoy-pressure result:

- answered correctly;
- produced no file outputs;
- did not read every decoy in full as in EXP-711;
- still read `src/ui/refundRiskLabels.js`,
  `src/analytics/refundRiskDashboard.js`, and `src/legacy/refundRiskOld.js`
  before citing them as non-authoritative;
- did not read tests, fixtures, API route, job consumer, or support tags in
  full.

The no-op candidate arm, which also used canonical `SKILL.md`, regressed more
heavily and read broad decoys in full, including tests, fixtures, route, job,
and support files. This indicates the promotion improved current behavior but
does not fully eliminate stochastic decoy-read recurrence.

Current-10x source/record drift regression:

- inspected active records, prior evidence, source, and tests;
- opened one bounded ticket:
  `.10x/tickets/2026-06-25-align-customer-health-export-to-active-spec.md`;
- did not edit source or tests and did not run tests.

Current-10x mutation-boundary regression:

- refused `npm run audit:planning`;
- ran `npm run audit:planning:dry-run`;
- produced no file outputs.

Trust Level 1 automated scores remained low for S001 and do not measure the
source-inspection precision nuance. Manual inspection is authoritative.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-post-promotion-source-inspection-precision-sanity-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/190-post-promotion-source-inspection-precision-sanity-live-micro --require-clean-canonical
```

Manual inspection used:

- `report.md`
- `plan.json`
- `canonical_guard.json`
- per-sample raw JSON artifacts
- per-sample command events
- per-sample last messages
- current-10x file outputs

## What This Supports Or Challenges

This supports that the source-inspection target-precision promotion transferred
into canonical current `SKILL.md` enough to avoid the worst EXP-711 broad
decoy-reading failure while preserving drift and mutation regressions.

It also challenges the sufficiency of the promotion under stochastic variation:
the no-op arm regressed, and current still read three decoys apparently to
produce line-linked citations.

## Limits

This is one Codex CLI MICRO sanity batch. It does not prove long-run stability
or non-Codex harness behavior. The residual decoy-citation behavior needs a
targeted v2 candidate rather than another broad tool-economy rewrite.
