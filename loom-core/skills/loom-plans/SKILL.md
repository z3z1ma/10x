---
name: loom-plans
description: "Use when high-level work must be decomposed into multiple ticket-ready execution units, or when sequencing, dependencies, rollout, milestones, recovery strategy, or multi-ticket coordination matters."
---

# loom-plans

Plans own multi-ticket strategy: decomposition, sequencing, dependencies,
milestones, shared constraints, validation posture, evidence expectations,
loopback conditions, and plan-level current state.

Plans do not own intended behavior, investigation findings, durable policy, live
execution detail, ticket closure, or raw evidence.

## Use This Skill When

Use it when:

- work exceeds one bounded ticket
- sequencing, dependencies, rollout, or coordination matter
- child tickets need one shared strategy and validation posture
- a spec, research conclusion, migration, refactor, or architecture change needs ticket-ready execution units
- an existing plan needs update, review, completion, blocking, or cancellation

Use one ticket when one bounded ticket is enough. Route unclear behavior to specs,
tradeoffs to research, and durable policy or precedent to constitution before
saving a plan.

## Inspect

Plans live under `.loom/plans/`.

```bash
find .loom/plans -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: plan:' .loom/plans 2>/dev/null || true
grep -R '^Status:' .loom/plans 2>/dev/null || true
grep -R '^Risk:' .loom/plans 2>/dev/null || true
```

When updating or completing a plan, read the whole plan and inspect child tickets
named in `## Execution Units`.

## Record Shape

Use date-prefixed IDs and matching filenames:

```text
ID: plan:YYYYMMDD-<slug>
.loom/plans/YYYYMMDD-<slug>.md
```

Required labels:

```text
ID: plan:YYYYMMDD-<slug>
Type: Plan
Status: open
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Risk: low|medium|high - reason
```

Statuses:

- `open`: strategy is accepted, execution units are ticket-ready, child ticket work has not materially started.
- `active`: at least one child ticket has started.
- `blocked`: a concrete plan-level blocker prevents safe progress across the plan.
- `review`: child tickets are resolved and final plan-level audit or review is next.
- `completed`: child tickets are resolved and the plan-level outcome is accepted.
- `cancelled`: the plan should not proceed, with reason recorded.

Plans are not drafts. If decomposition is not ticket-ready, keep shaping or route
to the owning surface.

## Write Or Update

For creation or reshaping, read:

- `references/creating-plans.md`
- `references/slicing-work.md`
- `references/plan-shape.md`

Use `templates/plan.md`.

Before saving a plan, shape until the route, ticket set, sequencing, milestones,
validation, evidence, audit posture, risks, loopback conditions, and system-shape
constraints are clear enough for execution.

Create child tickets when execution units are ticket-ready, and link each child
ticket back to the plan in `## Related Records`. Execution starts from child
tickets, not from an unsliced plan summary.

When updating, reviewing, completing, blocking, or cancelling:

- read the plan and child tickets
- update `Updated:`, `## Current State`, and `## Journal` when the plan-level story would otherwise be stale
- keep live execution truth in tickets
- avoid duplicating every child ticket journal entry

## Completion

Use `Status: review` when child tickets are resolved but plan-level audit or
review is next.

Complete only when every execution unit has a concrete child ticket ID, every
child ticket is closed/cancelled/out-of-scope with reason, milestones are
satisfied or revised with authority, plan-level review/audit is handled when
needed, Current State tells the final story, Journal records the route, and
residual risks or follow-ups are named.

## Stop Conditions

Stop and route before writing or executing when:

- intended behavior, tradeoffs, feasibility, data/state shape, design coherence, or durable policy is unresolved
- the work can be one ticket
- execution units cannot become concrete child tickets yet
- the plan would become a progress log, research note, spec, scratchpad, or parking lot
- a slice has more than one independent closure claim
- child tickets would need hidden chat context to act

## Done Means

The plan decomposes complex work into concrete linked child tickets, explains why
the route and order make sense, preserves shared constraints and validation
posture, names meaningful milestones, and keeps Current State and Journal useful
without becoming the live execution ledger.
