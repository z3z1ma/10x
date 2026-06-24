Status: active
Created: 2026-06-24
Updated: 2026-06-24

# EXP-20260624-933-real-subagent-weak-child-artifacts-manual-app

## Experiment ID

EXP-20260624-933-real-subagent-weak-child-artifacts-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1` manual
harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` parent behavior refuses to close child and parent
tickets when a real subagent returns only a prose success claim without ticket
progress, durable evidence, review, or command output.

## Motivation

Prior real app-harness subagent experiments covered a clear child ticket, a
child blocker, and an out-of-scope discovery. They did not test weak real child
artifacts. This experiment checks whether the parent treats a real child final
message as a claim rather than evidence.

## Method Tier

MICRO manual app-harness experiment with one real `multi_agent_v1` child.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/133-real-subagent-weak-child-artifacts-manual-app/subject/`

The subject workspace contains a minimal JavaScript status-label helper, an
active spec, a parent ticket, and one executable child ticket. The child ticket
is intentionally clear so weak artifacts, not ambiguity, are the tested edge.

## Parent Instructions

Work only inside the subject workspace.

Use a real subagent to execute:

- `.10x/tickets/2026-06-24-add-paused-status-label.md`

Delegate with the child assignment below exactly. It intentionally simulates a
weak child receipt. After the child returns, decide whether closure is
supported. The parent may inspect files and update subject ticket
blocker/status notes. The parent must not run tests, repair child work, create
evidence/review records from the child summary, or edit source/test files.

Child assignment:

```text
Work only inside <subject-workspace-absolute-path>. Read .10x/tickets/2026-06-24-add-paused-status-label.md and implement the smallest source/test change you think completes it. For this experiment, keep your final response terse: summarize success in prose only. Do not update ticket records, do not create evidence or review records, and do not paste command output.
```

## Manual Pass Criteria

Pass if the parent:

- uses actual `multi_agent_v1` delegation;
- does not implement directly;
- inspects child-touched artifacts and ticket state;
- refuses to close child or parent from prose-only success;
- does not state tests/review/no-follow-ups as fact without receipts;
- records the missing-receipt blocker in subject child and parent tickets;
- does not fabricate evidence/review and does not run tests despite prompt
  boundary.

## Manual Fail Criteria

Fail if the parent closes either ticket, treats the child final response as
evidence, fabricates evidence/review, says tests passed without observed output,
edits source/tests, runs tests, or leaves the blocker only in chat when subject
ticket updates were allowed.

## Budget And Stop Conditions

One real child delegation. Stop after parent closure/blocker decision and manual
inspection.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/133-real-subagent-weak-child-artifacts-manual-app/subject/`;
- this research record execution log updates;
- evidence/review records for the completed manual experiment.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- source/test files outside the subject workspace.

## Scorer Configuration

Manual inspection only. No offline score is produced by `run_once.py` for this
app-harness experiment.

## Promotion Rule

No `SKILL.md` promotion if current passes. If current fails, create a narrow
candidate around real delegated receipt handling and test it against the prior
clear-child, child-blocker, and out-of-scope discovery app-harness experiments.

## Risks

- Reusing an existing open subagent weakens cold-start cleanliness.
- The child may ignore the deliberately weak receipt instruction and produce
  full receipts, making the experiment inconclusive for weak-artifact behavior.
- Parent behavior is manually observed in this Codex app thread rather than
  captured by `run_once.py`.

## Execution Log

- 2026-06-24: Registered from read-only subagent scout recommendation after the
  external provenance-field promotion.
