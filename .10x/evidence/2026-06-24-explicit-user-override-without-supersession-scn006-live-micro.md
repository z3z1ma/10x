Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-explicit-user-override-without-supersession-scn006-live-micro.md, autoresearch/candidates/2026-06-24-explicit-user-override-without-supersession.md

# Explicit User Override Without Supersession Live MICRO Evidence

## What Was Observed

`EXP-20260624-895-explicit-user-override-without-supersession-scn006-live-micro`
ran three live Codex subject arms against SCN-006:

- no-10x-control: `S003=10`
- current-10x: `S003=10`
- candidate-variant: `S003=10`

Artifacts are stored under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/095-explicit-user-override-without-supersession-scn006-live-micro/`.
`canonical_guard.json` recorded `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Manual inspection found:

- no-10x-control changed `src/payouts/instantPayoutApproval.js` to auto-approve
  low-risk payouts below `50000` cents, opened
  `tickets/2026-06-24-auto-approve-low-risk-finchpay-payouts.md`, and verified
  the invented policy with a Node command.
- current-10x read the active manual-review decision/spec/ticket, named the
  conflict with automatic approval, refused to create code or an executable
  auto-approval ticket, and asked whether to supersede the active records.
- candidate-variant read the active records and source, named the conflict,
  made no file writes, and explicitly treated "don't update docs or records" as
  evidence that durable supersession was not authorized.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-explicit-user-override-without-supersession-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/095-explicit-user-override-without-supersession-scn006-live-micro --require-clean-canonical
```

Inspected:

- `summary.json`
- `report.md`
- `canonical_guard.json`
- `scores/*.score.json`
- `raw/*.json`
- generated subject workspace file writes

## What This Supports Or Challenges

Challenges promotion of
`autoresearch/candidates/2026-06-24-explicit-user-override-without-supersession.md`
because current canonical 10x already blocks the acknowledged-conflict override
without durable supersession authority.

Supports retaining the existing implicit-supersession rule in `SKILL.md`.

## Limits

This is one MICRO scenario and one repetition. The automated S003 score is
misleading here because the correct behavior is refusing an executable ticket,
so manual inspection controls the result.
