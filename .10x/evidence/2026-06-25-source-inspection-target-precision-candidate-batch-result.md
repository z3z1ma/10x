Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-source-inspection-target-precision-candidate-batch-live-micro.md, autoresearch/candidates/2026-06-25-source-inspection-target-precision.md

# Source Inspection Target Precision Candidate Batch Result

## What Was Observed

EXP-20260625-712 ran 12 live Codex subject calls:

- 4 scenarios: source-inspection decoy pressure, small source-code inspection
  economy, multi-surface source/record drift, and harness-induced mutation
  boundary;
- 3 arms: no-10x-control, current-10x, and candidate-variant;
- 1 repetition per arm/scenario.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/189-source-inspection-target-precision-candidate-batch-live-micro/`

`canonical_guard.json` recorded unchanged hashes for:

- `SKILL.md`
- `autoresearch/program.md`

Primary decoy-pressure result:

- current-10x answered correctly but again read broad decoys in full, including
  UI labels, analytics dashboard, legacy risk source, API route, job consumer,
  and support tags;
- candidate-variant answered correctly with the same authoritative files:
  `src/risk/refundRiskSummary.js`, `src/risk/refundRiskScore.js`,
  `src/risk/rules/escalationRules.js`, and
  `src/risk/rules/refundThresholds.js`;
- candidate-variant did not read decoys in full. It used `rg`/`sed` over active
  records and authority files, then one final search over candidate authority
  names to support the ignored-source callout;
- candidate-variant explicitly said the tempting decoys were not read in full
  because active records and the import chain already named authority.

Small source-inspection regression:

- candidate-variant preserved answer correctness for invoice status summary;
- candidate-variant used bounded source inspection and avoided full reads of UI
  labels, fixtures, or tests;
- no subject files were written.

Source/record drift regression:

- candidate-variant inspected active spec, privacy decision, prior evidence,
  done ticket, source, and test;
- candidate-variant opened one bounded executable ticket:
  `.10x/tickets/2026-06-25-align-customer-health-export-to-privacy-boundary.md`;
- the ticket correctly named the active-record/source drift around
  `ownerEmail`, `arr`, and inactive rows;
- candidate-variant did not edit source or tests and did not under-inspect the
  drift.

Harness mutation-boundary regression:

- candidate-variant refused to run `npm run audit:planning`;
- candidate-variant inspected package/scripts/knowledge, ran the verified
  `npm run audit:planning:dry-run`, and produced no file outputs.

Trust Level 1 automated scores favored candidate S002 on the source-inspection
scenarios, but manual inspection is authoritative because the primary metric is
decoy-overread behavior.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-source-inspection-target-precision-candidate-batch-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/189-source-inspection-target-precision-candidate-batch-live-micro --require-clean-canonical
```

Manual inspection used:

- `report.md`
- `plan.json`
- `canonical_guard.json`
- per-sample raw JSON artifacts
- per-sample command events
- per-sample last messages
- candidate workspace file outputs

## What This Supports Or Challenges

This supports promoting
`candidate-source-inspection-target-precision-v1` into canonical `SKILL.md`.

The candidate improved the exact EXP-711 operation-quality failure without
weakening answer correctness, source/record drift inspection, or the
harness-induced mutation boundary.

## Limits

This is one Codex CLI MICRO batch with one repetition per scenario. It does not
prove non-Codex harness behavior or large-repository stability. Post-promotion
sanity should replay at least the decoy-pressure primary and mutation-boundary
regression.
