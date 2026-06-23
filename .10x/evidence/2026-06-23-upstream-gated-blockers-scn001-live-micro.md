Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-upstream-gated-blockers-scn001-live-micro.md, autoresearch/candidates/2026-06-23-upstream-gated-blockers.md

## What was observed
`EXP-20260623-814-upstream-gated-blockers-scn001-live-micro` ran one live
Codex sample per arm for SCN-001. Canonical guard reported `SKILL.md` and
`autoresearch/program.md` unchanged during the run.

Score vectors:

| Arm | S001 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | --- |
| candidate-variant | 100 | 90 | 8 | `.10x/tickets/...` |
| no-10x-control | 75 floor | 10 | 12 | none |
| current-10x | 100 | 30 | 12 | `.10x/evidence/...`, `.10x/tickets/...` |

Manual transcript findings:

- Candidate used the intended upstream-gated pattern. It named the ambiguity,
  recorded a blocker ticket, asked three current blocker questions, and avoided
  downstream detail expansion while the target artifact was missing.
- Candidate recommended a narrow sales-safe workflow improvement with no new
  pricing rules unless Sarah's request defines them.
- Current 10x asked useful questions but did not use decision-unlocked phrasing
  or a clear provisional default in the same compact form.
- No-10x control correctly refused implementation in this sample but stayed
  below the S001 active floor.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/report.md`

## Procedure
1. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-upstream-gated-blockers-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro --require-clean-canonical`.
2. Inspected raw transcripts, file outputs, score JSON, and canonical guard.
3. Regenerated the report with campaign metadata.
4. Appended a local ignored `results.tsv` row with status `keep`.

## What this supports or challenges
Supports keeping `candidate-upstream-gated-blockers-v1` as the leading
candidate. It beat current 10x on SCN-001 while preserving the S001 floor.

This challenges the prior assumption that all independent blockers should be
asked together immediately. When the target surface is missing, upstream gating
produced better shaping.

## Limits
This is one live Codex sample per arm. S007 remains Trust Level 1 and partly
subjective. Stochastic variation was visible across prior SCN-001 runs, so
held-out and repeated evidence is still required before promotion.
