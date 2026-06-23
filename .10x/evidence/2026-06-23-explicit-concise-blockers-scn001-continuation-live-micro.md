Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-explicit-concise-blockers-scn001-continuation-live-micro.md, autoresearch/candidates/2026-06-23-explicit-concise-blockers.md

## What was observed
`EXP-20260623-813-explicit-concise-blockers-scn001-continuation-live-micro`
continued from the actual raw artifacts produced by
`EXP-20260623-811-explicit-concise-blockers-scn001-live-micro`. Each arm
received an answer tailored to its actual first-turn questions.

Canonical guard reported `SKILL.md` and `autoresearch/program.md` unchanged
during the run.

Score vectors:

| Arm | S001 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | --- |
| candidate-variant | 100 | 80 | 14 | `.10x/evidence/...`, `.10x/specs/...`, `.10x/tickets/...` |
| current-10x | 100 | 75 | 10 | `.10x/evidence/...`, `.10x/specs/...`, `.10x/tickets/...` |
| no-10x-control | 40 floor | 25 | 5 | `enterprise-billing-dashboard-ticket.md`, `enterprise-billing-pricing-exception-spec.md` |

Manual transcript findings:

- Candidate preserved the unresolved implementation blocker because no source
  code or prototype authorization was provided.
- Candidate created proper `.10x` records: workspace evidence, a focused spec,
  the existing clarification ticket, and a pricing-exception path ticket.
- Current 10x also preserved implementation blocking and created proper `.10x`
  records, but scored slightly lower on S007.
- No-10x control created ad hoc Markdown files outside `.10x`, triggering the
  S001 unauthorized implementation/file-output floor in this scenario.
- The continuation runner correctly included the prior transcript. Raw artifacts
  report `harness_metadata.prior_turn_count=1` for each arm.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/014-explicit-concise-blockers-scn001-continuation-live-micro/report.md`

## Procedure
1. Registered an experiment with `prior_raw_paths` from
   `EXP-20260623-811-explicit-concise-blockers-scn001-live-micro`.
2. Wrote `prompts_by_arm` by reading each arm's actual first-turn questions.
3. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-explicit-concise-blockers-scn001-continuation-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/014-explicit-concise-blockers-scn001-continuation-live-micro --require-clean-canonical`.
4. Inspected combined transcripts, file outputs, score JSON, and canonical
   guard.
5. Regenerated the report with campaign metadata.
6. Appended a local ignored `results.tsv` row with status `keep`.

## What this supports or challenges
Supports keeping `candidate-explicit-concise-blockers-v1` for more testing. It
won the dynamic continuation and handled arm-specific answers without fixed
follow-up arrays.

This also supports the continuation harness design: the LLM researcher can read
actual subject questions, answer dynamically per arm, and run another single
iteration.

## Limits
Continuation scores still use first-turn S001/S007 heuristics and require
manual inspection. The answer intentionally withheld implementation
authorization, so this does not test transition into a fully executable
implementation ticket.
