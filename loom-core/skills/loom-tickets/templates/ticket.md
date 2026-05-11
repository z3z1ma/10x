# <Ticket Title>

ID: ticket:<YYYYMMDD-slug>
Type: Ticket
Status: open
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
Risk: <low|medium|high> - <reason>

<!--
Add only when useful. Remove this comment before saving if unused.

Priority: <low|medium|high> - <reason>
Depends On: <ticket:YYYYMMDD-slug>
-->

## Summary

<Describe the bounded executable work unit in plain language.

Include enough context for an acting agent to understand what change is needed,
why it matters, and what outcome should exist when the ticket is complete. The
ticket should be executable from this record and its linked records without
relying on chat history.>

## Related Records

<List only records an acting agent should read before work. Say why each matters.
Remove this section if no related records materially constrain the ticket.>

- `<record-id or path>` - <why this record matters>

## Scope

<Describe the executable boundary in prose.

Name what may change, what must not change, and any nearby work that should not be
pulled into this ticket. Be specific enough that an acting agent can stay inside
the boundary without asking what is in scope.>

## Acceptance

Use stable acceptance IDs. Each criterion should be observable and should name
the evidence and audit posture needed for closure.

- ACC-001: <observable condition that must be true>
  - Evidence: <test, command, inspection, artifact, or explanation that will prove it>
  - Audit: <target or lens for closure audit, or why separate audit would not add useful trust>

- ACC-002: <observable condition that must be true>
  - Evidence: <test, command, inspection, artifact, or explanation that will prove it>
  - Audit: <target or lens for closure audit, or why separate audit would not add useful trust>

## Current State

<Describe where the work stands now.

For a new ticket, say whether it is ready to start and name the first likely move.
If anything prevents safe execution, set Status: blocked instead of open and
describe the blocker here.>

## Journal

Append material updates at the bottom. Record progress, decisions, blockers,
evidence, audit results, status changes, scope changes, acceptance changes, and
closure.

- <YYYY-MM-DD>: Created ticket with Status `open`. <Briefly state the source of
  the scope and the intended first move.>
