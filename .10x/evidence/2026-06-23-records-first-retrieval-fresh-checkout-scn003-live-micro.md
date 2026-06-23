Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-records-first-retrieval-fresh-checkout-scn003-live-micro.md

# Records-First Retrieval Fresh Checkout SCN-003 Live Micro

## What Was Observed

`EXP-20260623-828-records-first-retrieval-fresh-checkout-scn003-live-micro`
ran one live Codex sample per arm over the tracked checkout retry seed.

Automated scores:

- candidate-variant: `S001=55;S002=50;S007=0`
- current-10x: `S001=55;S002=50;S007=0`
- no-10x-control: `S001=55;S002=70;S007=10`

Manual inspection found candidate and current both answered from seeded `.10x`
records. Candidate named:

- `.10x/specs/checkout-retry-policy.md`
- `.10x/decisions/checkout-payment-provider.md`
- `.10x/tickets/2026-06-23-add-checkout-retry-banner.md`

Current cited the same records with absolute temporary workspace links.

The no-10x control removed inherited `.10x` before execution:
`pre_run_removed_control_record_dirs: [".10x"]`. It created no files during the
run. Despite that, it produced a plausible checkout retry answer, so the prompt
and domain were too guessable to isolate record retrieval.

Canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-records-first-retrieval-fresh-checkout-scn003-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro --require-clean-canonical
```

Inspected:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/report.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/campaign.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/canonical_guard.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/codex/sha256-0eea210ac5775c610efd0848540394c6a36a6af962af148287a78c092d3b13f8.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/codex/sha256-9f0d726942fe2a524e9fb48a3fd0839e9988f49e6634e3dc06b85fa48991c4d6.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/codex/sha256-ebf29c88db98dc9a05864593f4da4b4ad094f522fee7be02bea871d90845698b.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/workspaces/sha256-ebf29c88db98dc9a05864593f4da4b4ad094f522fee7be02bea871d90845698b/workspace-manifest.json`

## What This Supports Or Challenges

Supports:

- The no-10x control record graph cleanup works for seeded workspaces.
- Candidate and current 10x can answer from a fresh seeded `.10x` graph.

Challenges:

- This specific checkout seed is not promotion-grade evidence for
  `candidate-records-first-retrieval-v1`, because the no-10x control can infer
  plausible checkout behavior without records.

## Limits

One live sample per arm. The run is a useful confound detector and control
isolation check, not a reliable measurement of records-first retrieval.
