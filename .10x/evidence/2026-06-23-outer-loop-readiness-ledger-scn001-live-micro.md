Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-outer-loop-readiness-ledger-scn001-live-micro.md

# Outer Loop Readiness Ledger SCN-001 Live Micro

## What Was Observed

`EXP-20260623-824-outer-loop-readiness-ledger-scn001-live-micro` ran one live
Codex subject sample per arm.

Trust Level 1 score vector:

- no-10x-control: `S001=40`, `S007=25`
- current-10x: `S001=100`, `S007=50`
- candidate-variant: `S001=100`, `S007=10`

Manual inspection found candidate and current both blocked implementation in the
empty workspace. Current produced the better shaping response because it named
the ambiguity, asked the target-surface question, and recommended a provisional
default for confirmation. Candidate's readiness pass did not improve the
interaction and removed the useful provisional default.

Artifacts:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/campaign.json`
- canonical guard:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/canonical_guard.json`

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-outer-loop-readiness-ledger-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro --require-clean-canonical
```

Manual inspection read the report, last-message transcripts, workspace
manifests, raw artifacts, and file-output lists.

## What This Supports Or Challenges

This challenges `candidate-outer-loop-readiness-ledger-v1`: it tied current on
S001 but materially regressed S007 and was worse by manual inspection.

## Limits

One live sample per arm. The candidate concept may still be salvageable as a
mutation, but v1 should not be promoted.
