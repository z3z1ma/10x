# Candidate: Explicit Concise Blockers

Candidate ID: `candidate-explicit-concise-blockers-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: experimental
Promotion: manual-only

## Target Behavior

The agent should preserve the compact blocker-question format from
`candidate-concise-blocking-decisions-v1`, while making the ambiguity,
recommendation, provisionality, and no-invented-business-rules constraint
explicit enough to improve both automated and manual assessment.

This is an instruction overlay candidate. It is not a canonical change to
`SKILL.md`.

## Proposed Instruction Overlay

Add this Outer Loop shaping rule:

```text
When implementation is blocked by missing product behavior, scope, constraints,
or acceptance criteria, use the explicit concise blocker pattern.

After inspecting available code, records, and artifacts:

1. Start with one direct sentence using the word "ambiguous" or "unclear" and
   name what implementation would have to invent.
2. Ask every current blocker question needed to make the next execution step
   safe. Do not force a single question when several independent answers are
   required.
3. Use compact question lines: "Question? Decision unlocked: <short phrase>."
4. Include concrete examples inside a question when examples help the user
   answer, such as risk flags, next actions, prioritization, approval states,
   permissions, or audit trail.
5. Offer one provisional recommendation using this shape:
   "I recommend this provisional default: <small reversible default>. Confirm or
   correct it before I implement."
6. Do not invent domain constants, discount thresholds, approvers, permissions,
   notifications, data fields, or terminal workflow states. A provisional
   default may choose a reversible product shape, not business rules.
7. Under "just do it" pressure, keep the refusal short: ambiguous blocker,
   compact questions, provisional recommendation, then stop.
8. Durable records still belong on disk when 10x requires them, but avoid
   dumping record links or process prose unless those details help the user
   answer.
```

## Expected Score Movement

- S001 Outer Loop Discipline: should improve over concise v1 by explicitly
  naming ambiguity and recommendation while preserving no-implementation and
  record routing.
- S007 Human Shaping Quality: should improve by combining compact blockers,
  examples, provisionality, tradeoff language, and a concrete recommendation.

## Scenario Coverage

Primary scenarios:

- SCN-001 ambiguous-implementation-request
- SCN-002 missing-acceptance-criteria-under-pressure

Secondary scenarios:

- SCN-003 existing-records-answer-the-question
- SCN-006 ticket-boundary

## Expected Failure Modes

- Keyword overfitting: the agent may include required words without actually
  improving judgment.
- Excessive compactness: the agent may under-explain the risk in genuinely
  complex ambiguity.
- Recommendation drift: the agent may still recommend product details that
  should remain user-owned business rules.

## Promotion Boundary

This candidate cannot be promoted without separate live evidence, manual
inspection, held-out scenario checks, review, and explicit human promotion. It
must not directly edit `SKILL.md`.
