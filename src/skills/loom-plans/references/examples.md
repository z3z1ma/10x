# Plan Examples

## Example Plan Record

Use one plan when execution strategy, sequencing, validation, and recovery need to be durable across more than one ticket step.

## What To Notice In A Strong Plan

- the plan explains the big picture before enumerating steps
- milestones and concrete steps connect back to the purpose
- validation and recovery thinking are present
- linked tickets show where live execution truth will live

## Worked Example

```text
Purpose / Big Picture
Make the skill and reference corpus detailed enough that another agent can follow Loom procedures without rediscovering them from architecture prose.

Context and Orientation
The current corpus explains key principles but leaves too much operational knowledge trapped in terse references and transcript memory.

Milestones
- rewrite skill frontmatter and activation descriptions
- rewrite packet-consuming references into operational manuals
- add worked examples for the remaining artifact layers
- validate and rebuild after each pass

Plan of Work
1. improve routing cues so the right skill is chosen earlier
2. deepen schema references so record quality has a stronger written standard
3. deepen example references so operators can see good and bad patterns concretely
4. repair helper or naming surfaces only when the written rule is clear first

Validation and Acceptance
- each rewritten reference should help a fresh agent act without guessing
- skill descriptions should remain within spec and validate cleanly
- assembly and workspace health checks should pass after the rewrite

Idempotence and Recovery
- if one reference family lands poorly, revise that family without rolling back unrelated improved references
- keep the plan truthful when discoveries change ordering or scope

Linked Tickets
- one ticket for doctrine and skill corpus quality
- one ticket for helper and build support
- one ticket for proof workflows and durable verification
```

Why this is strong:

- it preserves rationale, sequence, validation, and recovery
- it gives a future reader enough context to resume strategy safely
- it points execution truth back into tickets instead of hoarding it locally

## Weak Example

```text
Steps
1. update docs
2. fix scripts
3. validate
```

Why this is weak:

- there is no big picture
- there is no reason for the chosen order
- no validation or recovery thinking is visible
