Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-upstream-gated-blockers-scn003-record-retrieval-live-micro.md, autoresearch/candidates/2026-06-23-upstream-gated-blockers.md

## What was observed
`EXP-20260623-817-upstream-gated-blockers-scn003-record-retrieval-live-micro`
continued from records created in
`EXP-20260623-816-upstream-gated-blockers-scn001-continuation-live-micro`.
The prompt asked each arm to answer from existing records without asking the
user to restate context.

Canonical guard reported `SKILL.md` and `autoresearch/program.md` unchanged
during the run.

Score vectors:

| Arm | S001 | S002 | S007 | Tool calls | File outputs |
| --- | ---: | ---: | ---: | ---: | --- |
| current-10x | 100 | 50 floor | 35 | 6 | `.10x/evidence/...`, `.10x/specs/...`, `.10x/tickets/...` |
| no-10x-control | 40 floor | 50 floor | 20 | 2 | `enterprise-billing-pricing-exceptions-spec-ticket.md` |
| candidate-variant | 100 | 60 floor | 80 | 4 | `.10x/specs/...`, `.10x/tickets/...` |

Manual transcript findings:

- Candidate answered from the existing `.10x` records and cited both the
  shaping ticket and draft spec.
- Candidate did not ask the user to restate context.
- Candidate preserved implementation blockers: no real dashboard codebase,
  implementation not authorized, and sales validation still required.
- Current 10x also answered from records and did not ask for restated context,
  but candidate was more concise and clearer about exclusions.
- No-10x control answered from its non-`.10x` ad hoc file and proposed an
  implementation ticket scope, which manual inspection treats as weaker because
  it came from a non-canonical artifact and moved closer to implementation.
- The automated S002 floor is not treated as promotion authority here because
  the scorer is not calibrated for retrieval continuations where the correct
  behavior is to answer from existing records rather than create new records.

Report artifact:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/018-upstream-gated-blockers-scn003-record-retrieval-live-micro/report.md`

## Procedure
1. Registered an experiment with `prior_raw_paths` from
   `EXP-20260623-816-upstream-gated-blockers-scn001-continuation-live-micro`.
2. Used the same retrieval prompt for all arms.
3. Ran `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-upstream-gated-blockers-scn003-record-retrieval-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/018-upstream-gated-blockers-scn003-record-retrieval-live-micro --require-clean-canonical`.
4. Inspected combined transcripts, file outputs, score JSON, and canonical
   guard.
5. Regenerated the report with campaign metadata.
6. Appended a local ignored `results.tsv` row with status `review`.

## What this supports or challenges
Supports the leading candidate's record-retrieval behavior. The candidate used
existing records instead of asking for restated context and preserved known
blockers.

Challenges the current offline S002 scorer for continuation retrieval tasks.
The automated floor is useful as a manual-inspection trigger, not a promotion
verdict.

## Limits
This is one retrieval continuation sample. It does not prove performance on a
fresh seeded workspace or on a real codebase with many `.10x` records. Scorer
trust remains Level 1.
