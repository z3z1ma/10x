Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-lower-assistance-blocked-retrospective-scn012-live-micro.md

# Lower-Assistance Blocked Retrospective Result Evidence

## What Was Observed

Ran `EXP-20260625-979-lower-assistance-blocked-retrospective-scn012-live-micro`
with three live Codex subject arms.

Output root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/179-lower-assistance-blocked-retrospective-scn012-live-micro/`

Canonical guard:

- `unchanged_during_run: true`
- changed canonical paths: none

Score vectors:

- no-10x-control: `S002=65`, `S006=65`
- current-10x: `S002=70`, `S006=85`
- candidate-variant: `S002=70`, `S006=85`

Current `SKILL.md` arm changed only `.10x` records:

- `.10x/knowledge/acme-billing-vocabulary.md`
- `.10x/skills/acme-billing-fixture-replay.md`
- `.10x/tickets/2026-06-25-acme-billing-import-parent.md`
- `.10x/tickets/2026-06-25-add-malformed-discount-amount-coverage.md`
- `.10x/tickets/2026-06-25-implement-acme-billing-event-import.md`

Current behavior details:

- Created an ACME billing fixture replay skill with the tracked
  `testdata/acme-billing/rate-limit-429.json` fixture, the frozen vendor date
  `2026-03-31`, offline fixture replay, and `Retry-After` validation.
- Created ACME billing vocabulary defining `vendorEventId` as the support and
  vendor reconciliation identifier.
- Opened a separate malformed-discount follow-up ticket.
- Marked the child import ticket `blocked` on unresolved duplicate invoice event
  behavior.
- Kept the parent ticket `active`.
- Preserved the duplicate-event reject-row versus quarantine-file blocker.
- Did not edit source or test files.
- Did not claim closure or run tests for unperformed implementation work.

Candidate-variant behavior was materially equivalent. The no-10x-control arm
kept the work blocked but reconstructed a fresh `.10x` graph after control
isolation and routed ACME 429 handling into a follow-up ticket rather than an
operational skill.

## Procedure

1. Registered the experiment
   `.10x/research/2026-06-25-lower-assistance-blocked-retrospective-scn012-live-micro.md`.
2. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-lower-assistance-blocked-retrospective-scn012-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/179-lower-assistance-blocked-retrospective-scn012-live-micro --require-clean-canonical`.
3. Read `report.md`, `summary.json`, `canonical_guard.json`, raw transcripts,
   workspace manifests, and the current arm's generated records.

## What This Supports Or Challenges

Supports that current `SKILL.md` can extract durable learning from a blocked run
without the user enumerating exact record targets in the prompt.

Supports treating the prior explicit ACME blocked-run success as a real
retrospective capability signal rather than prompt overfitting.

Challenges the Trust Level 1 S002 score for this scenario: the current arm
failed the numeric floor despite manually correct record-shape behavior.

## Limits

This was still a single-turn continuation over a compact seed workspace. It
does not prove the same quality across a messy multi-turn blocked execution or
when skill-versus-knowledge routing is less obvious.
