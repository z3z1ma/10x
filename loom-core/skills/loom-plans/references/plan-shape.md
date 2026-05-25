# Plan Shape

A plan is prose-rich strategy, not a progress log. It tells future agents what
complex work is being decomposed, why the route exists, which records constrain
it, which child tickets carry execution, what milestones matter, where the plan
stands, and what materially changed.

## Top Labels

```text
ID: plan:YYYYMMDD-<slug>
Type: Plan
Status: open
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Risk: low|medium|high - reason
```

Risk must include a reason. Use `high` for core architecture, safety, data
integrity, migration behavior, public contracts, or hard-to-reverse decisions.
Raise risk when sequencing errors, weak evidence, or expensive failure would make
the plan hard to trust.

## Core Sections

Use these unless the plan has a strong reason to vary:

- `## Summary`
- `## Related Records`
- `## Strategy`
- `## Execution Units`
- `## Milestones`
- `## Current State`
- `## Journal`

Keep `## Journal` last.

## Section Duties

Summary answers what is being decomposed, why it matters, why it needs more than
one ticket, and what completion produces.

Related Records lists only records or paths that materially constrain or explain
the plan. Move chat-only context into the plan or an owning record.

Strategy explains what belongs in the plan, what is left out, why the
decomposition and order make sense, what system-shape/data/state/abstraction
constraints matter, what risks shape the route, what can run independently, what
must be sequential, what validation posture child tickets inherit, and what
triggers replanning. Keep live progress out.

Execution Units point to concrete child ticket IDs. Each unit names outcome,
scope boundary, relevant design constraints, order/dependency reason, validation,
evidence, audit expectations, and loopback/stop conditions. If a unit cannot be
one bounded child ticket, split it or keep shaping.

Milestones are meaningful checkpoints across child tickets. They say what becomes
true and which child tickets contribute. They are not progress checklists.

Current State is a concise plan-level snapshot: strategy state, milestone state,
plan blockers, residual risks, useful child-ticket rollup, and next plan move.
Update it when the plan story would otherwise be stale.

Journal records material creation, child ticket creation, strategy changes,
milestone movement, blockers, review, completion, and cancellation. Do not turn it
into a transcript or rewrite history for neatness.

## Completion Shape

Before `Status: completed`, the plan should show:

- every execution unit has a concrete child ticket ID
- every child ticket is closed, cancelled, or explicitly out of scope with reason
- milestones are satisfied or revised with authority
- unsatisfied milestones are routed to review, cancellation, authorized scope change, or follow-up
- validation, evidence, and audit expectations were handled at the right level
- plan-level audit or review happened when strategy needed independent pressure
- final Current State, Journal, residual risks, and follow-ups are clear

Complete only when the plan tells one truthful strategy story and child tickets
carry the live execution truth.
