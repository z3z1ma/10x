---
name: loom-debugging
description: "Run reproduce-first debugging. Use when tests fail, builds break, behavior regresses, errors occur, flaky behavior appears, performance drops unexpectedly, root cause is unknown, or a fix needs red/green evidence."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: workflow
---

# loom-debugging

Debugging routes reproduction, root-cause work, fixes, evidence, and prevention
follow-through into the Loom records that own those facts.

## What This Workflow Coordinates

- reproduce-first bug workflow
- root-cause routing
- fix evidence expectations
- prevention handoff into retrospective

## Use This Skill When

- there is a failing behavior or incident
- the root cause is unknown
- intended behavior is ambiguous
- a fix needs regression evidence before acceptance

## Do Not Use This Skill When

- the work is a normal feature with clear acceptance
- the failure cannot be reproduced or observed yet and the only need is intake
- the next step is already a narrow ready ticket with evidence

## Default Procedure

Follow:

`orient -> feedback loop -> reproduce -> localize -> hypothesize -> fix -> evidence -> prevent`

1. orient in the relevant domain language, code paths, decisions, and accepted
   behavior before treating the symptom as the root cause
2. build or improve a fast feedback loop that can show the failure
3. capture reproduction steps or current failing behavior as evidence
4. investigate root cause before proposing a fix; create or update research if
   the root cause is not known
5. generate ranked, falsifiable hypotheses when cause is unclear
6. update or create a spec if intended behavior is ambiguous
7. create or tighten a ticket for the bounded fix
8. choose local execution for a tiny, local, safe fix, or compile a Ralph packet when
   the fix needs fresh context, explicit child write scope, or packetized
   isolation; Ralph packets normally use `verification_posture: test-first`
9. preserve red and green evidence
10. run critique when risk warrants
11. run retrospective if the lesson should prevent repeated mistakes

## Artifact Routing

| Debug output | Owner |
| --- | --- |
| reproduction steps | evidence |
| root cause investigation | research |
| intended behavior clarification | spec |
| fix execution | ticket plus local execution or Ralph packet, according to ticket facts and write-scope needs |
| regression evidence | evidence |
| recurring evidence gap | ticket follow-up or test expectation via retrospective |
| recurring lesson | wiki, research, spec, plan, initiative, constitution, or evidence via retrospective; memory may keep support-only recall or owner-record pointers |

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The fix is obvious." | Obvious fixes still need a feedback loop and evidence that the original failure no longer reproduces. |
| "I cannot reproduce it, but this change might help." | If reproduction is unstable, improve observation or ask for artifacts; do not claim a root-cause fix. |
| "Logging everything will reveal the issue." | Instrument predictions from hypotheses; broad logs create noise and cleanup debt. |
| "A green nearby test proves the bug is fixed." | Regression evidence must exercise the real failure pattern or explicitly state the seam is missing. |

## Red Flags

- no fast or credible feedback loop before code changes
- only one hypothesis was considered for an unknown root cause
- instrumentation is untagged or not mapped to a prediction
- fix addresses symptom but not source
- prevention lesson is left in chat after a repeated failure

## Verification

- [ ] Original failure was reproduced or inability to reproduce is explicit.
- [ ] Hypotheses were falsifiable when root cause was unknown.
- [ ] Fix evidence includes red/green or before/after observations.
- [ ] Temporary instrumentation and prototypes are removed or contained.
- [ ] Prevention route is recorded when the lesson should persist.

## Done Means

- the failure was reproduced or the inability to reproduce is explicit
- root cause is evidence-backed or still marked unknown
- intended behavior is owned by a spec when needed
- the fix is owned by a ticket and either reconciled local execution or packetized
  child result, as appropriate
- evidence exists for before and after behavior
- prevention follow-through is explicit

## Read In This Order

Read immediately for debugging work:

1. `references/systematic-debugging.md` when root cause is unknown, time pressure
   makes guessing tempting, or previous fixes failed.
2. `skills/loom-evidence/SKILL.md` when preserving reproduction, red/green
   output, logs, screenshots, or other evidence.

Then read conditionally:

3. `skills/loom-research/SKILL.md` when root cause is unknown or rejected
   hypotheses should remain citable.
4. `skills/loom-specs/SKILL.md` when intended behavior is ambiguous.
5. `skills/loom-tickets/SKILL.md` when creating or tightening the bounded fix
   ticket.
6. `skills/loom-ralph/SKILL.md` when the fix is ready for a packetized
   implementation iteration.
7. `skills/loom-critique/SKILL.md` when the fix or incident carries review
   risk.
8. `skills/loom-retrospective/SKILL.md` when the prevention lesson should
   persist beyond the ticket.
