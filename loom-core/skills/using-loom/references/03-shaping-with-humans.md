# Shaping With Humans

Before execution, shape the work until the next move is small, clear, bounded,
and honest. If the ask is not concrete enough to act without hidden design
choices, pinpoint the ambiguity with the operator before patching, ticketing, or
launching Ralph.

## Concrete Ask Gate

A fuzzy ask is not an implementation brief.

Treat a request as concrete only when these are clear enough to act without
choosing direction silently:

- operator or user outcome
- target surface, code area, workflow, or artifact
- scope boundary and important non-goals
- source, product, policy, or system constraints
- system-shape, data model, state, data-flow, or abstraction implications
- quality bar, success criteria, and non-examples
- evidence posture or observable proof path
- ticket, plan, spec, research, or other next Loom surface

If any of those are missing and would materially change what gets built, mandatory
shaping is next:

- inspect source and Loom records before asking what they already answer
- name the specific ambiguity or hidden choice
- ask one material question or offer two or three materially different options
- recommend a path when the tradeoff is clear
- preserve the resolved truth in the surface that owns it

Concrete enough means the remaining choices are local execution choices inside an
accepted direction.

## Outer Loop Posture

Inspect first. Do not ask the operator to restate what the repository or Loom
records can answer.

Then summarize only leverage:

- what you found
- what you think the real problem is
- which surface appears to own the next truth change
- what is unclear, risky, or stale
- what options exist
- which path you recommend and why

## Shape Vague Work Into Decisions

Broad requests are outer-loop inputs. Locate the product, behavior, system-shape,
workflow, evidence, or scope ambiguity that would make implementation a guess.

Shape the hard parts explicitly:

- which outcomes belong in this direction
- which adjacent outcomes are deliberately excluded
- which system seams, data model, or state relationships the work implies
- how the pieces should fit together as one design
- what would make the design incoherent even if the code runs
- which surface should own each resulting decision before execution depends on it

When several directions are plausible, offer a small set of materially different
directions, name the tradeoff, recommend one, and preserve the selected direction
in its owning surface.

## Pressure-Test Conversationally

Ask one material question when one answer would unblock good work. Offer two or
three materially different options when the choice is not obvious. Name the
tradeoff. Recommend a path.

Good pressure questions sound like:

- What should this become, and what should it explicitly not become?
- What system seam, data model, state relationship, or abstraction should this reinforce?
- What would make the design internally inconsistent?
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
- user, audience, or operator outcome
- intended behavior
- quality bar or non-examples
- policy, constraint, or precedent
- system shape, data model, state model, or abstraction boundary
- design coherence
- evidence baseline
- sequencing or rollout
- risk or audit need
- ticket-sized boundary
- operator authority for a consequential choice
- what `better`, `done`, `simple`, or similar shorthand excludes

If the work cannot yet be handed to a future agent with clear scope, constraints,
evidence expectations, and stop conditions, it is still outer-loop work.

## Shape Toward The Right Surface

If the operator makes a durable decision, preserve it in the surface that can
maintain it. Do not leave the real decision only in chat.

Use the surface that owns the truth:

- constitution for durable project judgment, policy, principle, constraint, precedent, ADR shape, or roadmap direction
- research for investigation, comparison, synthesis, rejected paths, or null results
- specs for intended behavior, requirements, scenarios, interfaces, or invariants
- plans for operator-shaped strategy across multiple tickets or execution units
- tickets for bounded executable work
- evidence for durable observations
- audit for Ralph-backed adversarial review
- knowledge for preferences, procedures, reusable accepted understanding, and retrieval cues

When no durable truth changed, take the smallest useful next step.

## Ready To Execute

Execution is ready when a future agent could understand the goal, scope,
constraints, expected evidence, and stop conditions without reading the chat that
produced them.

For product or UI work, readiness also means the operator-facing direction is
clear enough that the agent is not silently choosing the audience, quality bar,
visual language, data depth, rollout expectation, or acceptance evidence.

For complex work, readiness means the next execution unit is ticket-ready. If the
work needs several independent closure stories, create or update the plan and
child tickets before implementation.

If that is not true, keep shaping. When it is true, route to the appropriate
surface or skill and execute within that boundary.
