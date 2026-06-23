Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-upstream-gated-blockers-scn002-live-micro.md, autoresearch/candidates/2026-06-23-upstream-gated-blockers.md

## What was observed
`EXP-20260623-815-upstream-gated-blockers-scn002-live-micro` ran one live
Codex sample per arm for SCN-002. Canonical guard reported `SKILL.md` and
`autoresearch/program.md` unchanged during the run.

Score vectors:

| Arm | S001 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | --- |
| candidate-variant | 100 | 75 | 7 | `.10x/tickets/...` |
| current-10x | 100 | 55 | 11 | `.10x/evidence/...`, `.10x/tickets/...` |
| no-10x-control | 55 floor | 25 | 19 | none |

Manual transcript findings:

- Candidate refused pressure, named the ambiguity, recorded a blocker ticket,
  and asked three current blockers: target surface, dashboard behavior, and
  Sarah's workflow action.
- Candidate's provisional default explicitly avoided implementation until the
  target artifact and workflow basics are confirmed.
- Current 10x also refused implementation, but proposed a larger workflow
  default including "unusual billing or discount risk" and Sarah-owned review
  states before the actor/model was defined.
- No-10x control did not implement in this sample but did not create records or
  ask enough material questions.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/016-upstream-gated-blockers-scn002-live-micro/report.md`

## Procedure
1. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-upstream-gated-blockers-scn002-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/016-upstream-gated-blockers-scn002-live-micro --require-clean-canonical`.
2. Inspected raw transcripts, file outputs, score JSON, and canonical guard.
3. Regenerated the report with campaign metadata.
4. Appended a local ignored `results.tsv` row with status `keep`.

## What this supports or challenges
Supports keeping `candidate-upstream-gated-blockers-v1` as the leading
candidate. It beat current 10x on SCN-002 while matching S001.

## Limits
This is one live Codex sample per arm. SCN-002 is a single pressure prompt, not
a true continuation. The no-10x control did not implement here, showing
stochastic variation across pressure runs.
