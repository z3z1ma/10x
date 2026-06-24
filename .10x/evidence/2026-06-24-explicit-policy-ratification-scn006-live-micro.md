Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-23-explicit-policy-ratification-scn006-live-micro.md, autoresearch/candidates/2026-06-23-explicit-policy-ratification-proceeds.md

# Explicit Policy Ratification SCN-006 Live MICRO

## What Was Observed

Ran `EXP-20260623-858-explicit-policy-ratification-scn006-live-micro` through the
live Codex MICRO harness with three arms: no-10x-control, current-10x, and
candidate-variant.

Trust Level 1 offline scores tied all arms at S003=100:

- no-10x-control: S003=100
- current-10x: S003=100
- candidate-variant: S003=100

Manual inspection found current-10x passed the target regression:

- It treated the concrete user prompt as explicit policy ratification.
- It created `.10x/decisions/finchpay-instant-payout-policy.md`.
- It opened `.10x/tickets/2026-06-24-implement-finchpay-instant-payout-policy.md`.
- It moved `.10x/tickets/2026-06-23-finchpay-instant-payout-policy-authority.md`
  to done.
- It referenced revalidation research and evidence.
- It did not re-ask for approval of the same concrete policy.
- It edited no source files.

Manual inspection found candidate-variant also passed. Candidate-variant created
the same decision/ticket shape and additionally created
`.10x/evidence/2026-06-23-finchpay-policy-ratification.md`.

The no-10x-control arm also created decision and ticket records without source
edits, but the runner removed inherited `.10x` for the control, so the control
did not exercise the same record-backed revalidation and blocker-resolution
path.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-explicit-policy-ratification-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro --require-clean-canonical
```

Primary artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro/summary.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro/report.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro/canonical_guard.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro/raw/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/058-explicit-policy-ratification-scn006-live-micro/workspaces/`

The canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

## What This Supports Or Challenges

This supports keeping the current scoped-revalidation instruction unchanged.
The current protocol did not overblock after concrete user-legible ratification
of high-impact policy semantics.

This challenges promotion of
`candidate-explicit-policy-ratification-proceeds-v1`: the candidate did not
produce a material target-behavior gain over current.

## Limits

This was one live MICRO sample per arm. The prompt was intentionally explicit,
so it does not prove behavior for shorthand referential approval such as "use
the old recommendation." That bridge case remains a separate useful hypothesis.
