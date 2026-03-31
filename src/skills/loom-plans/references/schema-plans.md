# Plans Schema Reference

## Purpose

Plans own sequencing and strategy, not execution truth.

Plans should be self-contained enough that a novice can understand the intended path through the work, but they should still defer live execution detail to linked tickets.

## A Strong Plan Answers

1. what larger goal the plan serves
2. what order of work is intended
3. which milestones matter
4. what validation and recovery expectations exist
5. which tickets realize the strategy

It should also help a later reader understand why this sequence was chosen over obvious alternatives.

It should also make clear what someone can expect to observe as milestones land and how the work can be resumed if interrupted.

## Frontmatter Expectations

Plan records should preserve:

- stable `id`
- `kind: plan`
- truthful `status`
- `repository_scope`
- typed links to the governing constitution, initiative, spec, and downstream tickets when relevant
- timestamps that show material strategy revision

## Core Requirement

Plans must explain milestones, recovery, and validation expectations while remaining distinct from live ticket state.

This repository's plan style should learn from ExecPlan-style documents without copying them literally.

That means plans should be:

- purpose-first
- living documents that absorb discoveries and decisions
- detailed enough for a novice to navigate the work
- explicit about validation, recovery, and interfaces
- linked to tickets instead of embedding all execution nitty-gritty locally

## Body Expectations

The body should usually make these sections useful:

- `Purpose / Big Picture`
- `Progress`
- `Surprises & Discoveries`
- `Decision Log`
- `Outcomes & Retrospective`
- `Context and Orientation`
- `Milestones`
- `Plan of Work`
- `Concrete Steps`
- `Validation and Acceptance`
- `Idempotence and Recovery`
- `Artifacts and Notes`
- `Interfaces and Dependencies`
- `Linked Tickets`
- `Risks and Open Questions`
- `Revision Notes`

The exact shape can vary, but the plan should still feel like strategy rather than a ticket journal.

## Strong Plan Characteristics

Good plans:

- make milestones and sequencing legible
- preserve recovery thinking and idempotence where relevant
- link directly into the ticket set that carries execution truth
- record major strategy changes durably when discoveries shift the path

## Relationship To Neighboring Layers

- specs define what behavior is wanted
- plans define how to reach that behavior
- tickets tell the truth about the current state of execution
- docs explain accepted reality after the plan has materially landed

## Review Checklist

Before relying on a plan, check:

1. is the big picture visible
2. are milestones and sequence legible
3. are validation and recovery expectations explicit
4. are linked tickets visible
5. does the plan still read like strategy rather than execution churn

Good Loom plans should usually include the spirit of these sections, adapted to the repository's plan schema:

- purpose and big picture
- progress
- surprises and discoveries
- decision log
- context and orientation
- plan of work
- validation and acceptance
- idempotence and recovery

The plan should help the next actor understand both the intended path and why that path exists.

## Failure Cases To Avoid

- turning the plan into the live execution ledger
- leaving validation and recovery implicit
- listing steps without explaining why the strategy is shaped that way

## Plan Writing Standard

Write the plan as a living design-and-execution guide.

It should be verbose enough that a novice can:

- understand the overall goal
- understand the sequence of milestones
- understand what linked tickets are expected to do
- understand what evidence will show the plan is working
- resume after interruption without relying on unstated history

At the same time, keep execution nitty-gritty, current blockers, and detailed journaled reality in the linked tickets rather than bloating the plan into a second ledger.

## Done Means

- the strategy is legible to a fresh reader
- validation and recovery thinking are explicit
- linked tickets show who executes the plan
- the plan is durable without becoming a second ledger
