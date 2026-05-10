# <Plan Title>

ID: plan:<YYYYMMDD-slug>
Type: Plan
Status: open
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
Risk: <low|medium|high> - <reason>

## Summary

<Describe the complex work being decomposed, why it matters, why it needs more
than one ticket, and what outcome should exist when the plan is complete.>

## Related Records

<List records an agent should understand before using this plan. Remove unrelated
or nearby-only entries.>

- `<record-id or path>` - <why this record matters>

## Strategy

<Explain the route through the work. Include why this decomposition and order make
sense, what risks shape the route, what validation posture child tickets should
inherit, and how to recover if execution discovers the plan is wrong.>

## Execution Units

Each unit should map to a concrete child ticket. The child ticket owns executable
detail and live state; this plan owns the decomposition and order.

### Unit: <Name>

Ticket: ticket:<YYYYMMDD-child-slug>

<Describe the outcome, scope boundary, order or dependency reason, validation and
evidence expectations, child-ticket audit expectations, plan-level audit trigger
when relevant, and loopback or stop conditions.>

## Milestones

<Name meaningful checkpoints across child tickets. Say what will be true when each
milestone is reached. Do not turn milestones into a live progress checklist.>

### Milestone: <Name>

Child tickets: ticket:<YYYYMMDD-child-slug>, ticket:<YYYYMMDD-child-slug>

<What becomes true at this checkpoint and how the plan should know.>

## Current State

<Concise plan-level snapshot. Mention strategy state, child ticket rollup,
milestone state, blockers, residual risks, and next plan-level move when useful.>

## Journal

Append material updates at the bottom. Record plan creation, child ticket creation,
strategy changes, milestone movement, blockers, review, completion, and
cancellation.

- <YYYY-MM-DD>: Created plan with Status `open` and child tickets linked from the
  execution units.
