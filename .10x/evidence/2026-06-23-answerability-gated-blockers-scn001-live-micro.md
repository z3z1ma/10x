Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-answerability-gated-blockers-scn001-live-micro.md

# Answerability-Gated Blockers SCN-001 Live Micro

## What Was Observed

`EXP-20260623-831-answerability-gated-blockers-scn001-live-micro` ran one live
Codex sample per arm against a seeded Nimbus hold-release pilot workspace.

Automated scores:

- candidate-variant: `S001=100;S007=75`
- current-10x: `S001=100;S007=60`
- no-10x-control: `S001=65;S007=20`

Manual inspection:

- Candidate and current both inspected `.10x` records/source before asking.
- Candidate and current both treated target surface, actor, fields, UI copy,
  token, and non-goals as settled.
- Candidate and current both asked only two unresolved blockers: success
  threshold and launch authority.
- Candidate was more compact and got the higher automated S007 score.
- Current gave the safer provisional default: report-only export with no backend
  mutation. Candidate proposed a read-only default and also provisionally named
  a success threshold, which risks inventing a business rule that the seed
  explicitly left unresolved.
- No-10x control had inherited `.10x` removed and asked five broad questions
  from source alone, including data source, operator actions, and release safety
  details already answered or constrained by records in the 10x arms.

Canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-answerability-gated-blockers-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro --require-clean-canonical
```

Inspected:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/report.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/campaign.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/canonical_guard.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/codex/sha256-50f2d761e8d5606703ea90448ca0b6c1fcb0beb3a953948fba8c4a91bf6bc89d.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/codex/sha256-7033fe2b99fe3f626f475c0aabc9704fd885e2e7dfb65d985db638d1d0637fad.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/codex/sha256-e8a30f5948da77f432610f1754db47a612eb29f6c30398ca314ad215b92a7776.last-message.txt`
- workspace manifests for all three arms.

## What This Supports Or Challenges

Supports:

- Current `SKILL.md` already performs answerability-gated blocker subtraction on
  this seed.
- The no-10x control cleanup is working: control saw only source after `.10x`
  removal and behaved less precisely.
- The candidate idea is plausible but needs mutation, because its core behavior
  did not beat current manually.

Challenges:

- `candidate-answerability-gated-blockers-v1` is not promotion-ready despite the
  automated S007 lift.
- The candidate wording may encourage provisional defaults for unresolved
  business thresholds unless explicitly constrained.

## Limits

One live sample per arm. The seed was synthetic and designed to expose stale
ticket subtraction. S007 remains a weak heuristic for this behavior and manual
inspection is authoritative.
