Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-distinct-near-duplicate-owner-scn005-live-micro.md, autoresearch/candidates/2026-06-24-distinct-near-duplicate-owner.md

# Distinct Near-Duplicate Owner Live MICRO

## What Was Observed

One live Codex MICRO run executed for
`EXP-20260624-864-distinct-near-duplicate-owner-scn005-live-micro` with three
arms: `candidate-variant`, `current-10x`, and `no-10x-control`.

Artifacts:

- Output root:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/064-distinct-near-duplicate-owner-scn005-live-micro/`
- Report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/064-distinct-near-duplicate-owner-scn005-live-micro/report.md`
- Canonical guard:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/064-distinct-near-duplicate-owner-scn005-live-micro/canonical_guard.json`

Automated Trust Level 1 scores:

- `current-10x`: S002=100, S005=100.
- `candidate-variant`: S002=30, S005=80.
- `no-10x-control`: S002=80, S005=80.

Manual inspection found current already performed the intended behavior. It
inspected the existing visible-rows CSV quote/newline ticket, recognized that
archive export behavior was excluded, opened one bounded legacy
nightly/archive CSV quote/newline follow-up, and edited no source files.

Candidate also opened a bounded legacy nightly/archive owner, but additionally
updated the related visible-rows ticket with a cross-reference. This did not
create a behavioral improvement over current.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-distinct-near-duplicate-owner-scn005-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/064-distinct-near-duplicate-owner-scn005-live-micro --require-clean-canonical
```

Manual inspection read the report, canonical guard, last messages, raw outputs,
and subject-workspace ticket files for all three arms.

## What This Supports Or Challenges

This challenges promotion of
`autoresearch/candidates/2026-06-24-distinct-near-duplicate-owner.md`. Current
canonical `SKILL.md` already performed the needed near-duplicate ownership
comparison in this scenario.

## Limits

This is one MICRO scenario with one repetition. It supports discarding the
candidate as null or weaker versus current; it does not prove all
near-duplicate ownership cases are solved.
