# <Ticket Title>

ID: ticket:YYYYMMDD-<slug>
Type: Ticket
Status: open
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
Risk: <low|medium|high> - <reason>

<!-- Optional when useful; remove if unused.
Priority: <low|medium|high> - <reason>
Depends On: ticket:YYYYMMDD-<slug>
-->

## Summary

<Describe the bounded executable work unit, why it matters, and the one closure
claim this ticket will prove. Include enough context for the first bounded Ralph
run to start from this ticket and linked records without chat history.>

## Related Records

<List only records an acting agent should read before work, with why each matters.
Remove this section if none materially constrain the ticket.>

- `<record-id or path>` - <why this record matters>

## Scope

<Name what may change, what must not change, non-goals, assumptions, likely read
scope, likely write scope, stop conditions, evidence posture, review/audit posture,
and where worker output should be reconciled. Include system-shape, data-model,
state, abstraction, or coherence constraints when they bound execution.>

## Acceptance

- ACC-001: <observable condition that must be true>
  - Evidence: <test, command, inspection, artifact, or explanation that will prove it>
  - Audit: <target or lens for closure audit, or why separate audit would not add useful trust>

- ACC-002: <observable condition that must be true>
  - Evidence: <test, command, inspection, artifact, or explanation that will prove it>
  - Audit: <target or lens for closure audit, or why separate audit would not add useful trust>

## Current State

<Describe where the work stands now. For a new ticket, say whether it is ready to
start and name the first likely Ralph run. If anything prevents safe execution, use
`Status: blocked` and describe the blocker.>

## Journal

Append material updates at the bottom: progress, decisions, blockers, evidence,
audit, status changes, scope changes, acceptance changes, and closure.

- <YYYY-MM-DD>: Created ticket with Status `open`. <State the source of scope and intended first move.>
