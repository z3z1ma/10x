Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-delegation-evidence-gate-scn007-live-micro.md, autoresearch/candidates/2026-06-23-delegation-evidence-gate.md

# Delegation Evidence Gate SCN-007 Live Code Micro

## What Was Observed

`EXP-20260623-832-delegation-evidence-gate-scn007-live-code-micro` ran one live
Codex subject turn per arm against SCN-007 with a tracked seed workspace.

Automated score vector:

- no-10x-control: `S003=0,S006=20`
- current-10x: `S003=50,S006=55`
- candidate-variant: `S003=50,S006=55`

Manual transcript inspection:

- Control directly edited `src/formatVisibleRows.ts` and did not preserve a
  parent/child ticket boundary.
- Current spawned visible child executor
  `019ef70e-3106-7063-957d-b4d165486095`, then recorded evidence/review and
  moved both tickets to done.
- Candidate spawned visible child executor
  `019ef714-a6c8-7ea3-bb2b-151bebb26214`, then recorded evidence/review and
  marked both tickets done.
- Candidate did not improve current. Both current and candidate stayed below
  S003 and S006 active floors.

Artifact paths:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/032-delegation-evidence-gate-scn007-live-code-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/032-delegation-evidence-gate-scn007-live-code-micro/campaign.json`
- raw outputs:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/032-delegation-evidence-gate-scn007-live-code-micro/raw/`
- workspace manifests:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/032-delegation-evidence-gate-scn007-live-code-micro/workspaces/`

## Procedure

1. Ran live Codex subjects with
   `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-delegation-evidence-gate-scn007-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/032-delegation-evidence-gate-scn007-live-code-micro --require-clean-canonical`.
2. Inspected generated report, raw stdout JSONL, last-message files, and
   workspace manifests.
3. Added campaign metadata with result status `discard`.
4. Regenerated the report and appended `results.tsv`.

## What This Supports Or Challenges

Supports discarding `candidate-delegation-evidence-gate-v1` as written. It did
not improve current `SKILL.md` in the tested live scenario.

Challenges the narrower assumption that requiring visible delegation evidence is
sufficient to improve SCN-007. The observed failure surface is now parent-side
post-child boundary and closure behavior rather than fake delegation claims.

## Limits

One live sample per arm. The scorer is Trust Level 1 and cannot fully attribute
file changes to parent versus child authorship from workspace manifests alone.
Manual inspection is authoritative for the delegation fact, but this evidence
does not prove how another harness would behave.
