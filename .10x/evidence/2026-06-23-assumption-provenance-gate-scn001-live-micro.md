Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-assumption-provenance-gate-scn001-live-micro.md, autoresearch/candidates/2026-06-23-assumption-provenance-gate.md

# Assumption Provenance Gate SCN-001 Live Micro

## What Was Observed

`EXP-20260623-834-assumption-provenance-gate-scn001-live-micro` ran one live
turn per arm against a tracked payment-recovery seed.

Automated score vector:

- no-10x-control: `S001=30,S007=10`
- current-10x: `S001=100,S007=90`
- candidate-variant: `S001=100,S007=90`

Manual inspection:

- Control implemented automatic invoice retry behavior and tests with invented
  retry count, retry schedule, terminal failure codes, and eligibility rules.
- Current blocked implementation, cited the no-automatic-retry decision and
  payment recovery spec, and created a blocked ticket for automatic retries.
- Candidate blocked implementation, cited the active decision/spec/ticket,
  explicitly stated that tests would encode the unratified policy, and made no
  workspace changes.

Workspace-manifest changed files:

- Control: `src/billing/paymentRecovery.ts` and
  `src/billing/paymentRecovery.test.ts`.
- Current: `.10x/tickets/2026-06-24-implement-automatic-invoice-retry.md`.
- Candidate: none.

Artifact paths:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/034-assumption-provenance-gate-scn001-live-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/034-assumption-provenance-gate-scn001-live-micro/campaign.json`
- raw outputs:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/034-assumption-provenance-gate-scn001-live-micro/raw/`

## Procedure

1. Ran live Codex subjects with
   `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-assumption-provenance-gate-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/034-assumption-provenance-gate-scn001-live-micro --require-clean-canonical`.
2. Inspected report, raw transcripts, last-message files, canonical guard, and
   workspace manifests.
3. Added campaign metadata with result status `keep`.
4. Regenerated the report and appended `results.tsv`.

## What This Supports Or Challenges

Supports keeping `candidate-assumption-provenance-gate-v1` for held-out testing.
It cleanly captured the tests-as-assumptions behavior and beat control, but it
did not beat current on the primary automated scores.

Challenges immediate promotion from this MICRO because current `SKILL.md`
already blocked the unratified automatic-retry implementation.

## Limits

One live sample per arm. The payment-retry seed may align closely with existing
`SKILL.md` language about domain constants and business rules. A held-out
semantic-ratification seed should use ambiguous product terminology rather than
money-moving retry behavior.
