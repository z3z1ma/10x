Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-records-first-retrieval-scn003-live-micro.md

# Records-First Retrieval SCN-003 Live Micro

## What Was Observed

`EXP-20260623-826-records-first-retrieval-scn003-live-micro` ran one live Codex
subject sample per arm.

Trust Level 1 score vector:

- no-10x-control: `S001=40`, `S002=50`, `S007=20`
- current-10x: `S001=100`, `S002=50`, `S007=60`
- candidate-variant: `S001=100`, `S002=60`, `S007=80`

Manual inspection found candidate and current both answered from existing
`.10x` records and cited paths. Candidate was more concise and clearer about
implementation blockers. No-10x control answered from a non-`.10x` ad hoc file
and drifted toward implementation-ticket scope.

Artifacts:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro/campaign.json`
- canonical guard:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro/canonical_guard.json`

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-records-first-retrieval-scn003-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro --require-clean-canonical
```

Manual inspection read the report, raw outputs, last-message transcripts, score
artifacts, workspace manifests, and file-output lists.

## What This Supports Or Challenges

This supports keeping `candidate-records-first-retrieval-v1` for more testing:
it beat current on S002 and S007 and repeated the prior manual SCN-003 pattern.

It does not support promotion yet because S002 remained below floor and this was
one seeded retrieval continuation.

## Limits

One live sample per arm. Seed context came from a prior upstream-gated
continuation. The automated S002 scorer remains conservative for retrieval
continuations.
