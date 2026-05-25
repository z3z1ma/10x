---
name: loom-tickets
description: "Use whenever the user mentions tickets, scoped implementation work, continuation from prior work, acceptance changes, review state, closure, cancellation, or a bounded work item that needs live execution state."
---

# loom-tickets

Tickets are Loom's atomic execution work orders.

A ticket owns one bounded change, live state, `ACC-*` acceptance, scope,
current state, evidence links, review posture, durable Ralph context, worker
output reconciliation, and one closure claim. It is not a scratchpad, plan,
research note, transcript, parking lot, or disguise for unresolved shaping.

Create or act from a ticket only when the execution boundary is clear enough that
a future agent can continue from the ticket and linked records without chat
history.

## Use This Skill When

Use this skill for ticket creation, ticket readiness, scoped implementation work,
continuation, status updates, acceptance changes, blockers, review state,
closure, cancellation, or ticket summaries.

Route elsewhere first when the real work is intended behavior, sequencing,
tradeoffs, durable policy, architecture, data or state modeling, design
coherence, ambiguous intent, evidence, audit, or reusable knowledge.

## Dispatch

If creating or shaping a ticket:

- read `references/creating-tickets.md`
- read `references/ticket-shape.md`
- inspect relevant records and source before asking the operator to repeat facts
- create the ticket only when scope, acceptance, evidence posture, and first
  Ralph boundary are concrete
- use `templates/ticket.md`

If acting from, resuming, updating, reviewing, blocking, closing, or cancelling a
ticket:

- read the whole ticket
- read `references/acting-on-tickets.md`
- read or already know records named in `## Related Records`
- keep all work inside the ticket boundary
- use `loom-ralph` for each bounded implementation, inspection, review, or audit
  slice
- update the ticket when future continuation would otherwise be misleading

If only finding or summarizing tickets, inspect `.loom/tickets/` and report state
without mutating records unless asked.

## Finding Tickets

Tickets live under `.loom/tickets/`.

Useful searches:

```bash
find .loom/tickets -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: ticket:' .loom/tickets 2>/dev/null || true
grep -R '^Status:' .loom/tickets 2>/dev/null || true
grep -R '^Risk:' .loom/tickets 2>/dev/null || true
grep -R '^Priority:' .loom/tickets 2>/dev/null || true
grep -R '^Depends On:' .loom/tickets 2>/dev/null || true
```

Prefer exact ID and filename matches before fuzzy search.

## IDs, Labels, And Status

Use `ticket:YYYYMMDD-<slug>` and `.loom/tickets/YYYYMMDD-<slug>.md`.

Required top labels:

```text
ID: ticket:YYYYMMDD-<slug>
Type: Ticket
Status: open
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Risk: low|medium|high - reason
```

Optional labels: `Priority:` for sequencing pressure and `Depends On:` for hard
prerequisites. Use `## Related Records` for loose relevance.

Status lifecycle:

- `open`: ready to start
- `active`: bounded Ralph execution is underway or returned output is being
  reconciled
- `blocked`: a concrete blocker prevents safe progress
- `review`: audit, acceptance review, or final verification is next
- `closed`: acceptance, evidence, audit posture, current state, and journal tell
  one truthful closure story
- `cancelled`: the work should not proceed, with reason recorded

Update `Updated:` whenever materially changing status, scope, acceptance, current
state, blockers, evidence, review posture, or closure state.

## Ticket Invariants

Every ticket must keep:

- one bounded executable work unit and one coherent closure claim
- explicit scope boundary and material non-goals
- settled or linked system-shape, data-model, state-modeling, and coherence
  choices relevant to execution
- concrete `ACC-*` acceptance criteria
- related records needed for execution or review
- likely read scope, write scope, stop conditions, evidence posture, review
  posture, and worker-output reconciliation when handoff is expected
- truthful `Status:`, Current State, and Journal
- evidence proportional to the closure claim
- no unrelated cleanup, opportunistic batching, vague asks, silent expansion, or
  acceptance rewrites after implementation

If an invariant fails, update the ticket, split it, block it, or route the missing
truth to the owning surface.

## Working Rules

When execution begins, set `Status: active` unless already active. Execute from the
ticket and linked records, not from hidden chat context or transient prompts.

Append Journal entries for material progress, blockers, decisions, evidence,
review, status changes, scope or acceptance changes, and closure. Do not turn the
journal into a transcript.

Use `Status: review` when implementation appears complete but verification,
audit, or acceptance review remains.

Close only when every `ACC-*` is satisfied or revised with authority, evidence
supports the closure claim, audit has happened or is explicitly not useful,
Current State is final, Journal records closure, and residual risk or follow-up is
visible.

Cancel only when the work should not proceed; record why, what changed or was
learned, and where any durable truth moved.

## Done Means

Ticket work is done when the ticket still describes one bounded work unit,
`Status:` matches reality, acceptance/evidence/audit posture are truthful, worker
output has been reconciled when relevant, and a future agent can continue or trust
closure from the graph.
