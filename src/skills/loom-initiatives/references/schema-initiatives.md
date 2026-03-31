# Initiatives Schema Reference

## Purpose

Initiatives are strategic containers for multi-artifact work.

Use an initiative when one cross-cutting outcome needs a durable owner above the spec, plan, and ticket layers.

## What An Initiative Owns

An initiative owns:

- the strategic objective
- why that objective matters now
- how success will be measured
- what milestones or phases matter
- which downstream specs, plans, and tickets execute the work

It does not own live execution updates. Tickets still do that.

## A Strong Initiative Answers

1. what outcome is being pursued
2. why now is the right time
3. how success will be measured
4. which milestones matter
5. which downstream artifacts execute the work
6. why the outcome deserves its own durable strategic container

## Frontmatter Expectations

Initiative records should preserve:

- stable `id`
- `kind: initiative`
- truthful `status`
- `repository_scope`
- links to related research, specs, plans, and tickets when relevant
- timestamps that show when strategic framing changed

## Body Expectations

The body should usually make these sections useful:

- `Objective`
- `Why Now`
- `In Scope`
- `Out of Scope`
- `Success Metrics`
- `Milestones`
- `Dependencies`
- `Risks`
- `Linked Specs, Plans, and Tickets`
- `Status Summary`

The most important thing is not section presence alone. The most important thing is whether the record gives downstream work a clear strategic frame.

## Writing Standard

Good initiative records:

- keep the objective strategic rather than task-sized
- define success in a way that later plans and tickets can inherit
- make the downstream execution graph explicit
- explain why the objective matters now instead of assuming the urgency is obvious
- distinguish scope from implementation detail

## Relationship To Neighboring Layers

- research may justify why the initiative matters
- specs define the behavior that some initiative milestones require
- plans sequence how the initiative is executed
- tickets carry the live work state
- docs may later explain the accepted outcome, but they do not own the strategic frame

## Review Checklist

Before relying on an initiative, check:

1. is the objective strategic rather than task-sized
2. are success metrics specific enough to inherit downstream
3. are milestones legible
4. is the downstream execution graph explicit
5. would a later reader know why this initiative exists separately from one plan or spec

## Failure Cases To Avoid

- turning the initiative into a giant ticket list with no strategic framing
- tracking execution minutiae here instead of in tickets
- leaving success metrics too vague for downstream planning to inherit usefully
- making the initiative so broad that it means little in practice

## Done Means

- one initiative clearly owns the strategic outcome
- success and milestones are visible
- downstream work is explicit
- a future agent could understand why the initiative exists and how to progress it
