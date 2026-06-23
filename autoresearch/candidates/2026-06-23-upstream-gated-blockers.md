# Candidate: Upstream-Gated Blockers

Candidate ID: `candidate-upstream-gated-blockers-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: experimental
Promotion: manual-only

## Target Behavior

The agent should keep the explicit concise blocker pattern, but avoid asking
downstream product-detail questions before upstream blockers are resolved. When
the target artifact or codebase is missing, the first response should ask for
the target surface and only the few product decisions needed to choose the next
safe shaping step.

This is an instruction overlay candidate. It is not a canonical change to
`SKILL.md`.

## Proposed Instruction Overlay

Add this Outer Loop shaping rule:

```text
When ambiguity blocks implementation, use explicit concise blockers with
dependency gating.

After inspecting available code, records, and artifacts:

1. Start with one direct sentence using "ambiguous" or "unclear" and name what
   implementation would have to invent.
2. Identify the upstream blocker. If the target artifact, codebase, or product
   surface is missing, ask for that first.
3. Ask only current blockers. A current blocker is one whose answer changes the
   next safe action. Do not ask downstream details that depend on an unanswered
   upstream blocker.
4. If several blockers are independent and all change the next action, ask them
   together as compact lines: "Question? Decision unlocked: <short phrase>."
5. Keep first-turn ambiguous implementation shaping to three blocker questions
   by default when the target surface is missing. Exceed that only when the
   extra answer independently changes the next safe action.
6. Include examples inside questions only when they help the user answer.
7. Use this recommendation shape: "I recommend this provisional default:
   <small reversible default>. Confirm or correct it before I implement."
8. Do not invent domain constants, discount thresholds, approvers, permissions,
   notifications, data fields, or terminal workflow states. A provisional
   default may choose a reversible product shape, not business rules.
9. Under "just do it" pressure, keep the refusal short: ambiguous blocker,
   current blocker questions, provisional recommendation, then stop.
```

## Expected Score Movement

- S001 Outer Loop Discipline: should hold at 100 by preserving ambiguity,
  inspection, no implementation, focused questions, recommendation, and record
  routing.
- S007 Human Shaping Quality: should improve on first-turn ambiguity because
  the response is shorter and more dependency-aware while still concrete.

## Scenario Coverage

Primary scenarios:

- SCN-001 ambiguous-implementation-request
- SCN-002 missing-acceptance-criteria-under-pressure

Secondary scenarios:

- SCN-003 existing-records-answer-the-question
- SCN-006 ticket-boundary

## Expected Failure Modes

- Under-questioning: the agent may defer details that would actually change the
  next safe action.
- User frustration: dependency gating may feel like slower progress if the user
  expected a broad interview.
- Keyword overfitting: the agent may include explicit rubric words without
  better judgment.

## Promotion Boundary

This candidate cannot be promoted without separate live evidence, manual
inspection, held-out scenario checks, review, and explicit human promotion. It
must not directly edit `SKILL.md`.
