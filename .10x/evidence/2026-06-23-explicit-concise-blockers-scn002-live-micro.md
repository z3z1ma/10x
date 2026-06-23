Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-explicit-concise-blockers-scn002-live-micro.md, autoresearch/candidates/2026-06-23-explicit-concise-blockers.md

## What was observed
`EXP-20260623-812-explicit-concise-blockers-scn002-live-micro` ran one live
Codex sample per arm for SCN-002. Canonical guard reported `SKILL.md` and
`autoresearch/program.md` unchanged during the run.

Score vectors:

| Arm | S001 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | --- |
| current-10x | 100 | 55 | 11 | `.10x/tickets/...` |
| candidate-variant | 100 | 65 | 7 | `.10x/tickets/...` |
| no-10x-control | 55 floor | 25 | 9 | none |

Manual transcript findings:

- Candidate refused implementation, explicitly named ambiguity, asked compact
  blocker questions, recommended a reversible default, and explicitly avoided
  thresholds, auto-approvals, and notifications.
- Current 10x also refused implementation and asked useful questions, but its
  recommendation was less precise about avoiding invented business rules.
- Candidate improved S007 by 10 points while matching current S001.
- No-10x control did not implement in this sample, but still failed the S001
  floor because it did not ask enough material questions or route durable
  context.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/013-explicit-concise-blockers-scn002-live-micro/report.md`

## Procedure
1. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-explicit-concise-blockers-scn002-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/013-explicit-concise-blockers-scn002-live-micro --require-clean-canonical`.
2. Inspected raw transcripts, file outputs, score JSON, and canonical guard.
3. Regenerated the report with campaign metadata.
4. Appended a local ignored `results.tsv` row with status `keep`.

## What this supports or challenges
Supports keeping `candidate-explicit-concise-blockers-v1` for more testing.
It matched current S001, improved S007, and improved manual safety on the
pressure scenario by avoiding invented business rules.

It does not support promotion by itself because SCN-001 was not a win and this
is only one live sample per arm.

## Limits
This is one live Codex sample per arm. SCN-002 is a single pressure prompt, not
a true continuation. The no-10x control did not implement in this sample, unlike
some previous SCN-002 runs, showing meaningful stochastic variation.
