# Appendix C — State Machines

## Ticket States

Allowed ticket statuses:

- `proposed`
- `ready`
- `active`
- `blocked`
- `review_required`
- `complete_pending_acceptance`
- `closed`
- `cancelled`

Allowed transition shape:

- `proposed -> ready`
- `ready -> active`
- `active -> blocked | review_required | complete_pending_acceptance`
- `blocked -> active | cancelled`
- `review_required -> active | complete_pending_acceptance`
- `complete_pending_acceptance -> closed | active`

## Ralph Outcome Reconciliation Matrix

Use this matrix in the parent context after a Ralph child run returns.

### `continue`

Use when the child made valid progress but the ticket still clearly owns more immediate execution work.

Parent expectations:

- ticket usually remains `active`
- packet may remain as the latest packet until superseded
- ticket journal should record what changed
- verification section should record what evidence was produced
- next owning subsystem usually remains `loom-ralph` or `loom-tickets`

### `stop`

Use when the bounded execution step is complete enough that the immediate run should end and the next step is review, acceptance, or docs.

Parent expectations:

- ticket often moves to `review_required` or `complete_pending_acceptance`
- packet may be treated as accepted evidence for that bounded run family
- ticket should link or summarize relevant verification
- next owning subsystem is often `loom-critique`, `loom-docs`, or acceptance handling in `loom-tickets`

### `blocked`

Use when the child could not continue because required context, scope, permissions, or upstream work were missing.

Parent expectations:

- ticket usually moves to `blocked`
- ticket should record the blocker explicitly
- packet may remain durable history but should not be treated as the current forward path without revision
- next owning subsystem is usually `loom-tickets` until the blocker is resolved

### `escalate`

Use when the child discovered a problem that requires a higher-order parent decision, a stronger review, or a different subsystem.

Parent expectations:

- ticket may remain `active` or move to `review_required` depending on the situation
- parent should interpret why escalation happened and choose the next subsystem deliberately
- likely next owners are `loom-critique`, `loom-plans`, `loom-specs`, or `loom-workspace`

## Plan States

- `draft`
- `active`
- `revised`
- `retired`

## Critique Finding States

- `open`
- `accepted`
- `rejected`
- `mitigated`

## Docs States

- `draft`
- `accepted`
- `stale`
- `superseded`

## Packet Lifecycle

- `compiled`
- `launched`
- `superseded`
- `accepted`
- `stale`
- `failed`

### Lifecycle Meaning

- `compiled`: the packet exists and has not yet been used for a child run
- `launched`: a child run has been started from this packet
- `accepted`: the parent has accepted the bounded run outcome as part of durable workflow history
- `stale`: the packet should no longer be trusted for a new run because target, source, doctrine, or scope changed materially
- `superseded`: a newer packet intentionally replaced this packet for the same run family or target
- `failed`: the packet-driven run failed in a way that makes this packet unsuitable as the forward path without revision

### Freshness Guidance

Mark a packet stale or superseded when:

- the target changed materially after packet generation
- one of the critical source records changed materially
- the allowed write boundary changed
- the intended packet mode changed
- the parent had to recompile because the prior packet was incomplete or misleading
