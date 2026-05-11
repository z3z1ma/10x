# Shaping With Humans

Before execution, the agent and operator shape the work until the next move is
small, clear, bounded, and honest.

## Outer Loop Posture

Inspect first. Do not ask the operator to restate what the repository or Loom
records can answer.

Then summarize only what gives the operator leverage:

- what you found
- what you think the real problem is
- which surface appears to own the next truth change
- what is unclear, risky, or stale
- what options exist
- which path you recommend and why

Compress the context into a useful decision point.

## Shape Vague Work Into Decisions

Broad requests are normal outer-loop inputs. Treat umbrella requests, quality
adjectives, and large verbs as invitations to identify the real decision behind
the words.

Before writing durable artifacts or executing from them, shape the decision points
that affect the work:

- the user or operator outcome
- the quality bar and non-examples
- the meaningful non-goals
- the source, product, policy, or architecture constraints
- the evidence that would make success believable
- the ticket boundary or plan decomposition that would make execution bounded

When several directions are plausible, offer a small set of materially different
directions, name the tradeoff, and recommend one. Preserve the selected direction
in the surface that owns it.

## Pressure-Test Conversationally

Pressure-test the work until the next move is shaped well enough to trust.

Ask one material question when one answer would unblock good work.

Offer two or three materially different options when the choice is not obvious.
Name the tradeoff. Recommend a path.

Good pressure questions sound like:

- What would make this successful?
- What should not change?
- Is this a local fix or a precedent?
- What would make this risky?
- What should a future agent know before touching this?
- What evidence would convince us this worked?
- Is this ready for a ticket, or are we still shaping the intent?

Do not walk the operator through a form unless the operator asks for one.

## Stay Outer While Work Is Fuzzy

Stay in the outer loop when any of these are unclear:

- purpose or success criteria
- intended behavior
- policy, constraint, or precedent
- evidence baseline
- sequencing or rollout
- risk or audit need
- ticket-sized boundary
- operator authority for a consequential choice

Do not jump from a fuzzy request to the first plausible implementation.

If the work cannot yet be handed to a fresh agent with clear scope, constraints,
evidence expectations, and stop conditions, it is still outer-loop work.

## Shape Toward The Right Surface

The outer loop should end by routing the durable truth.

If the operator makes a durable decision, preserve it in the surface that can
maintain it. Do not leave the real decision only in chat.

Use the surface that owns the truth:

- constitution for durable project judgment, policy, principle, constraint,
  precedent, ADR shape, or roadmap direction
- research for investigation, comparison, synthesis, rejected paths, or null results
- specs for intended behavior, requirements, scenarios, interfaces, or invariants
- plans for operator-shaped strategy across multiple tickets or execution units
- tickets for bounded executable work
- evidence for durable observations
- audit for fresh-context review
- knowledge for preferences, procedures, reusable accepted understanding, and
  retrieval cues
- packets for delegated worker execution

When no durable truth changed, move forward with the smallest useful next step.

## Ready To Execute

Execution is ready when a fresh agent could understand the goal, scope,
constraints, expected evidence, and stop conditions without reading the chat that
produced them.

For product or UI work, readiness also means the operator-facing direction is
clear enough that the agent is not silently choosing the audience, quality bar,
visual language, data depth, rollout expectation, or acceptance evidence.

For complex work, readiness means the next execution unit is ticket-ready. If the
work needs several independent closure stories, create or update the plan and
child tickets before implementation.

If that is not true, keep shaping.

When it is true, stop shaping and route the work into the appropriate surface or
skill.
