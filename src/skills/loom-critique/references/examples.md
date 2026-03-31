# Critique Examples

## Example Review Question

```text
Does the current repo corpus operationalize `constitution:main` strongly enough that another agent can proceed without guessing?
```

## Example Finding Shape

Good critique findings look like this:

- identify one concrete gap
- cite the affected file
- explain why the gap matters operationally
- compare the current state to the stronger expectation in `constitution:main`
- recommend the next corrective direction

## Example Review Skeleton

```text
Target Under Review
Packet compiler behavior for execution-mode packets.

Review Question
Does the current packet output provide a bounded contract strong enough for a fresh worker to execute without widening scope?

Focus Areas
- explicit scope
- write boundary clarity
- freshness and stale-trigger handling
- parent reconciliation readiness
```

## Example Durable Finding

```text
Problem: The packet contract omits a clear write boundary.
Why it matters: A fresh worker could widen scope or mutate the wrong durable record.
Evidence: The packet declares execution mode but does not state allowed write refs or writable paths.
Scope: Ralph execution for one bound ticket.
Severity: high.
Confidence: high.
Recommended action: Recompile the packet with an explicit write boundary and treat the previous packet as stale.
```

## Example Residual Risk Entry

```text
Residual Risks
- the packet contract is now structurally stronger, but packet freshness rules are still easy to under-specify when the governing ticket changes materially after compilation
- no example yet proves how the parent should reconcile contradictory child claims against the ticket ledger
```

## Why This Example Matters

It shows critique as a bounded review protocol that sharpens acceptance quality instead of becoming a second execution ledger.

## Weak Example

```text
Looks pretty good overall. Maybe tighten a few things.
```

Why this is weak:

- there is no concrete problem statement
- no evidence is cited
- the next actor cannot tell what to do
