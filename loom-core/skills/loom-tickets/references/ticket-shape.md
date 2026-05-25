# Ticket Shape

A good ticket is prose-rich, bounded, grepable, and actionable. It contains enough
context for a future agent to launch Ralph, reconcile worker output, or continue
without chat history.

## Top Labels

Required:

```text
ID: ticket:YYYYMMDD-<slug>
Type: Ticket
Status: open
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Risk: low|medium|high - reason
```

Optional:

```text
Priority: low|medium|high - reason
Depends On: ticket:YYYYMMDD-<slug>
```

`Priority:` is sequencing pressure. `Depends On:` is only for hard prerequisites;
use `## Related Records` for relevance.

Risk must include a reason: `low` for narrow, reversible, easy checks; `medium` for
meaningful shared behavior or integration; `high` for core architecture, safety,
data integrity, public contracts, or hard-to-reverse decisions.

## Core Sections

Default sections:

- `## Summary`
- `## Related Records`
- `## Scope`
- `## Acceptance`
- `## Current State`
- `## Journal`

Remove `## Related Records` only when no existing record constrains the work.
`## Journal` stays last.

## Section Contracts

Summary names the bounded work, why it matters, the intended outcome, context an
acting agent needs, and the single closure claim.

Related Records lists only records an acting agent should read, with a reason for
each. Move any durable context that exists only in chat or a prompt into the ticket
or another owning record.

Scope names what may change, what must not change, likely files/records/systems,
assumptions, non-goals, and any system-shape, data-model, state, abstraction, or
coherence constraints. If the first Ralph boundary cannot be identified, the ticket
is not ready.

For worker or review handoff, durable scope should include likely read scope,
write scope, constraints, stop conditions, evidence posture, review/audit posture,
expected worker output, and where that output will be reconciled.

Acceptance uses observable `ACC-001`, `ACC-002`, ... criteria. Each criterion
should say what must be true, how evidence will show it, and what audit should
challenge or why separate audit is not useful. Avoid vague criteria like `works`,
`cleaned up`, `aligned`, or `handled` unless made observable.

Current State is the current narrative snapshot: progress, blockers, evidence,
audit state, residual risk, open decisions, and next likely move. Keep it current
enough for continuation.

Journal is append-friendly. Add dated entries for material progress, decisions,
blockers, evidence, audit, status changes, scope or acceptance changes, and closure
or cancellation. Do not rewrite history to look cleaner.

## Closure Shape

A closed ticket should show what changed, why acceptance is satisfied, what
evidence exists, what audit happened or why it was not useful, residual risk, and
why `Status: closed` is truthful.

Close only when the ticket, linked records, evidence, and audit state support the
one closure claim.
