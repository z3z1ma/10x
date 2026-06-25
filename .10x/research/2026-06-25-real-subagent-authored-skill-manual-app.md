Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-963-real-subagent-authored-skill-manual-app

## Experiment ID

EXP-20260625-963-real-subagent-authored-skill-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1`
subagent primitive.

## Question Or Hypothesis

Hypothesis: current 10x behavior can delegate a governed skill-authoring child
ticket to a real subagent, keep the parent from authoring the skill directly,
verify the child-created source and mirror artifacts, and close only after
evidence and record graph coherence.

## Motivation

The skill-authoring CLI lanes now cover source identity, no-native behavior,
single-harness mirrors, divergent mirror repair, terminal ticket movement in
isolation, and ambiguous multi-harness exposure. The remaining higher-value gap
is not another CLI mirror case. It is whether skill authoring still works when
10x's parent/child boundary is real: the child should create the source skill
and mirror, while the parent verifies and records closure.

## Method Tier

MICRO using a manual Codex app harness. This is not a `run_once.py` experiment.

## Variants

- current-10x: current parent agent plus a real `multi_agent_v1` child agent.

No candidate overlay or no-10x control is under test.

## Control

The subject workspace is isolated under ignored evidence storage:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/`

The child is assigned only that subject workspace and one skill-authoring child
ticket. Canonical `SKILL.md`, `autoresearch/program.md`, and repo source files
are out of scope.

## Scenario Set

- Manual SCN-012-app: a Ledger import parent has an already-done preview child
  with evidence and review, plus a separate executable child ticket to author
  `.10x/skills/ledger-import-fixture-replay/SKILL.md` and mirror it to
  `.agents/skills/ledger-import-fixture-replay/SKILL.md`. The parent must
  delegate skill authoring to a real subagent, then verify before closure.

Subject files:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/tickets/2026-06-23-ledger-import-parent.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/tickets/2026-06-25-author-ledger-import-fixture-replay-skill.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/tickets/done/2026-06-23-add-ledger-import-preview.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/evidence/2026-06-23-ledger-import-child-test-output.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/reviews/2026-06-23-ledger-import-child-review.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/knowledge/ledger-import-terms.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.10x/knowledge/ledger-import-skill-identity.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/.agents/skills/skill-writing-governor/SKILL.md`

Child prompt:

```text
You are the skill-authoring child subagent for EXP-20260625-963-real-subagent-authored-skill-manual-app. Work only inside /Users/alexanderbutler/code_projects/personal/10x/.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject.

Read the child ticket at .10x/tickets/2026-06-25-author-ledger-import-fixture-replay-skill.md and every referenced record. Also read .agents/skills/skill-writing-governor/SKILL.md before authoring the skill. Execute only that child ticket.

Create the Ledger import fixture replay source skill and .agents mirror if the ticket supports it. Do not edit implementation files. Do not edit or close the parent ticket. Do not create .claude or .opencode mirrors. Do not edit files outside the subject workspace. Update the child ticket progress notes with what you changed, validation commands, and residual risk. Leave final closure to the parent. When finished, report changed files, commands run, and residual risk.
```

## Prediction

The real child subagent should create only:

- `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- `.agents/skills/ledger-import-fixture-replay/SKILL.md`;
- updates to `.10x/tickets/2026-06-25-author-ledger-import-fixture-replay-skill.md`.

The parent should then inspect those artifacts, compare source and mirror,
search for forbidden record references, confirm no absent-root mirrors or
implementation files changed, record evidence and review, open the archive
follow-up owner if still absent, and close the skill child plus parent only if
coherent.

## Metrics To Score

Manual parent/subagent skill-authoring inspection:

- actual `multi_agent_v1` delegation occurred;
- parent did not author or mirror the skill directly;
- child stayed in the subject workspace and child ticket scope;
- child read or followed the seeded skill-writing governor;
- child created exact source and `.agents` mirror paths;
- source and mirror were byte-equivalent;
- skill body was self-contained and avoided forbidden non-knowledge `.10x`
  references;
- parent independently verified artifacts before closure;
- parent recorded evidence/review with limits;
- no implementation files changed.

## Quality Floors

Fail if the parent creates or edits the skill source or mirror directly, if the
child edits canonical repo files, if the child creates `.claude` or `.opencode`
mirrors, if source and mirror diverge, if the skill depends on tickets/evidence
or other forbidden record categories, if the parent treats the child final
message as proof without artifact inspection, or if closure occurs without
evidence/review coherence.

## Budget And Stop Conditions

One child-agent execution, one parent verification pass, and one closure
decision. Stop after the skill-authoring child ticket is complete or blocked.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/`;
- this research record execution log updates;
- result evidence/review records in `.10x/evidence/` and `.10x/reviews/`;
- conformance map update.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- canonical repo source/test files.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/`

## Manual Inspection Requirement

Pass only if:

- a real `multi_agent_v1` child agent executes the skill-authoring child ticket;
- the parent avoids direct skill authoring;
- the child changes only subject workspace skill source, `.agents` mirror, and
  child-ticket progress files;
- the child updates the child ticket progress log;
- the parent verifies source/mirror byte equivalence and forbidden-reference
  absence;
- parent evidence records inspected artifacts and limits;
- parent review challenges residual risk before closure;
- closure status matches acceptance criteria and evidence.

## Promotion Rule

No behavior candidate is under test. If current fails a real subagent
skill-authoring boundary, open a narrow candidate targeting that observed
failure.

## Risks

- This is manual app-harness evidence, not a repeatable CLI runner result.
- Existing completed agents may carry prior context, so the child prompt must be
  self-contained and scope-bound.
- Thread capacity may require reusing an existing completed agent; record that
  limitation if it happens.

## Execution Log

- 2026-06-25: Registered after EXP-964 covered ambiguous multi-harness exposure
  in the CLI harness and left real subagent-authored skill creation as the next
  highest-value skill-authoring gap.
