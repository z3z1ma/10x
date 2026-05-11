---
name: loom-idea-refine
description: "Use when an operator's rough product, engineering, workflow, research, or opportunity idea lacks clear problem, audience, constraints, success criteria, direction, or next Core record move."
---

# loom-idea-refine

Idea refinement is an outer-loop playbook for turning a rough concept into a clear
next Loom move.

It explores options, tests assumptions, chooses a direction, and routes durable
results into core records.

## Core Dependency

Use `loom-core` first. This playbook assumes `using-loom` is loaded and routes
durable results through core skills such as `loom-research`, `loom-specs`,
`loom-plans`, `loom-tickets`, `loom-knowledge`, and `loom-constitution`.

This playbook creates no separate idea ledger.

## Use This Playbook When

Use this playbook when:

- the operator has a vague product, engineering, workflow, or research idea
- the problem, audience, success criteria, or constraints are unclear
- several possible directions exist and need comparison
- hidden assumptions need validation before execution
- an idea should become a spec, research record, plan, ticket, knowledge note, or
  constitutional question

Skip this playbook when the next core record move is already clear.

## Route

Use this route:

```text
frame -> expand -> compare -> choose -> route
```

## Frame

Restate the idea as a problem or opportunity.

Clarify:

- who or what the idea is for
- the job, pain, quality gap, or workflow friction it addresses
- what success would look like
- what constraints are real now
- what has already been tried or rejected
- what would make the idea not worth doing

Ask one material question at a time. Recommend a direction when the repository,
records, or constraints point clearly.

## Expand

Generate a small set of distinct directions, not a long list.

Useful lenses:

- inversion: what if the system did the opposite?
- simplification: what is the one-job version?
- constraint removal: what changes if time, budget, compatibility, or platform
  limits change?
- audience shift: who else has the same problem in a sharper form?
- first principles: what is actually true, and what is inherited habit?
- jobs to be done: what is the operator, user, agent, or maintainer trying to get
  done?
- pre-mortem: what failure would make this idea look wrong later?

When inside a codebase, inspect relevant source files and Loom records before
inventing options.

## Compare

Compare promising directions on:

- user or operator value
- implementation feasibility
- differentiation from the current workaround
- risk and reversibility
- dependency on unresolved behavior, policy, source facts, or evidence
- smallest version that tests the important assumption
- explicit non-goals

Name assumptions in three groups:

- must be true: wrong answer kills the direction
- should be true: wrong answer changes the approach
- might be true: later optimization or secondary bet

## Choose

Produce a short decision summary:

- recommended direction
- rejected directions and why they were not chosen
- smallest useful version
- assumptions to validate
- not doing
- open questions
- next Loom surface

Do not save a free-floating one-pager unless the operator explicitly asks for that
artifact. Prefer routing into core records.

## Route To Core

Route by shape:

- unknown facts, market/source comparisons, feasibility, rejected paths, or null
  results -> `loom-research`
- intended behavior, requirements, scenarios, interfaces, or quality bar ->
  `loom-specs`
- multi-ticket sequencing -> `loom-plans`
- executable work -> `loom-tickets`
- durable judgment, constraint, principle, or roadmap direction ->
  `loom-constitution`
- reusable explanation, preference, retrieval cue, or ideation lesson ->
  `loom-knowledge`

## Done Means

The idea-refine pass is done when:

- the problem, audience, success shape, and constraints are clear enough for the
  next move
- explored directions are materially different
- assumptions and non-goals are visible
- one recommended direction or explicit no-go result exists
- durable follow-up is routed into core records
