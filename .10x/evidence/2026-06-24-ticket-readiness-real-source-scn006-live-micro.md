Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-ticket-readiness-real-source-scn006-live-micro.md, autoresearch/candidates/2026-06-23-ticket-readiness-gate.md

# Ticket Readiness Real Source SCN-006 Live MICRO

## What Was Observed

Ran `EXP-20260624-861-ticket-readiness-real-source-scn006-live-micro` with one
live Codex sample for each arm after fixing seed workspace manifest resolution.

Clean artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/061b-ticket-readiness-real-source-scn006-live-micro/`

Automated Trust Level 1 score vectors:

- candidate-variant: `S003=100`
- current-10x: `S003=80`
- no-10x-control: `S003=65`, below the active S003 floor

The canonical guard reported no changes to `SKILL.md` or
`autoresearch/program.md` during the clean run.

Manual inspection found:

- candidate-variant inspected `.10x/decisions/enterprise-billing-csv-export.md`,
  `.10x/specs/enterprise-billing-exceptions.md`,
  `src/features/billing/ExceptionsPage.tsx`,
  `src/features/billing/usePricingExceptions.ts`,
  `src/features/billing/PricingExceptionsTable.tsx`, and `package.json`.
  It created exactly one executable ticket with scope, explicit exclusions,
  acceptance criteria, governing context, current source state, evidence
  expectations, implementation notes, and supported `Blockers: None`.
- current-10x inspected the same records/source and created exactly one
  executable ticket, but omitted a dedicated evidence-expectations section and
  was less explicit about closure evidence shape.
- no-10x-control had inherited `.10x` removed by control isolation and created a
  ticket from source/prompt alone, with `Depends-On: none`.

No arm edited implementation files or asked questions.

## Procedure

1. Registered `candidate-ticket-readiness-gate-v1` as active and created the
   `ticket-readiness-real-source` seed.
2. The first run to `061-...` was interrupted and marked confounded because the
   runner resolved `"workspace": "."` relative to the canonical repo root.
3. Fixed seed workspace path resolution and validation, then committed/pushed
   `eca6933e`.
4. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-ticket-readiness-real-source-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/061b-ticket-readiness-real-source-scn006-live-micro --require-clean-canonical`.
5. Read the report, canonical guard, final messages, raw tool invocations,
   archived workspace file lists, and all created ticket records.

## What This Supports Or Challenges

Supports promoting the ticket-readiness gate. On a real-source seed, the
candidate improved executable ticket quality over current 10x by making evidence
expectations and record/source references explicit while preserving the correct
boundary: one ticket, no questions, no implementation.

Challenges the older concern that the prior generated-workspace result was too
weak to promote. The corrected seed gave the no-10x control a clearer failure
and removed the missing-source confound.

## Limits

This is one MICRO seed and one sample per arm. It tests ticket creation quality,
not whether a subagent would successfully implement from the ticket. Future
SCN-007 or closure runs should verify that richer evidence expectations improve
execution and closure coherence rather than only ticket prose.
