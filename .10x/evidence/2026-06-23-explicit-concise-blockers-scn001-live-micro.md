Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-explicit-concise-blockers-scn001-live-micro.md, autoresearch/candidates/2026-06-23-explicit-concise-blockers.md

## What was observed
`EXP-20260623-811-explicit-concise-blockers-scn001-live-micro` ran one live
Codex sample per arm for SCN-001. Canonical guard reported `SKILL.md` and
`autoresearch/program.md` unchanged during the run.

Score vectors:

| Arm | S001 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | --- |
| candidate-variant | 100 | 65 | 7 | `.10x/tickets/...` |
| current-10x | 100 | 70 | 9 | `.10x/tickets/...` |
| no-10x-control | 55 floor | 25 | 4 | none |

Manual transcript findings:

- Candidate used the intended explicit concise blocker pattern: it named the
  request ambiguous, asked five blocker questions with "Decision unlocked"
  phrases, gave examples inside questions, recommended a provisional default,
  and required confirmation before implementation.
- Current 10x was shorter and scored five S007 points higher. It asked three
  blocker questions and recommended a narrow tomorrow-ready scope.
- Candidate was more comprehensive than current 10x on Sarah's workflow and
  acceptance criteria, but the response was longer and did not earn the brevity
  or tradeoff points.
- No-10x control refused implementation in this sample but remained below the
  S001 active floor.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/012-explicit-concise-blockers-scn001-live-micro/report.md`

## Procedure
1. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-explicit-concise-blockers-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/012-explicit-concise-blockers-scn001-live-micro --require-clean-canonical`.
2. Inspected raw transcripts, file outputs, score JSON, and canonical guard.
3. Regenerated the report with campaign metadata.
4. Appended a local ignored `results.tsv` row with status `mutate`.

## What this supports or challenges
Supports the explicit concise blocker pattern as discipline-preserving. It does
not support promotion on SCN-001 because current 10x still scored higher on
S007.

The next mutation should keep explicit ambiguity/recommendation wording but
either reduce question count when one answer gates the rest or add a compact
tradeoff sentence without exceeding the shaping response budget.

## Limits
This is one live Codex sample per arm. S007 is Trust Level 1 and partly
subjective. This empty-workspace prompt may reward shorter responses more than
a real dashboard project would.
