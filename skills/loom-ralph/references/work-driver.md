# Work Driver

The work driver moves one ticket through bounded Ralph iterations and parent
reconciliation.

It is not "just code." It is ticket-owned execution.

## Inputs

- ticket
- linked plan, spec, research, and initiative as needed
- acceptance criteria and coverage targets
- evidence expectations
- critique and wiki disposition

## Procedure

1. Anchor to one ticket.
2. Read the smallest governing chain needed.
3. Check ticket readiness.
4. Move the ticket to `active` only when work is genuinely starting.
5. Compile a Ralph packet with child write scope, parent merge scope, source
   fingerprint, execution context, context budget, verification posture, stop
   conditions, and output contract.
6. Launch the bounded iteration through the available harness transport.
7. Reconcile the child output as parent:
   - check scope discipline
   - check child write boundary
   - record evidence
   - update ticket journal and status
   - update packet status away from `compiled`
8. Decide the next owner:
   - another Ralph iteration
   - critique
   - wiki
   - outer-loop refinement
   - acceptance

## Stop States

- `blocked`: a named blocker exists
- `review_required`: critique is next
- `complete_pending_acceptance`: work and evidence are largely complete
- never mark `closed` from work execution

## Guardrails

- Do not execute without a ticket owning live state.
- Do not let a packet outrank the ticket or owner records.
- Do not widen scope because a nearby fix looks easy.
- The child may recommend ticket updates; the parent commits ticket truth.
