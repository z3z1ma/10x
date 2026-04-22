# Expected Route

1. Create or update a spec for shipping behavior.
2. Create or update a plan if multiple tickets are needed.
3. Create one bounded ticket.
4. Compile a Ralph packet with source fingerprint, execution context, context
   budget, child write scope, parent merge scope, and verification targets.
5. Execute one bounded implementation slice.
6. Reconcile the child output back into ticket truth.
7. Run packetized implementation critique against the ticket context and git
   diff.
8. Update wiki only if accepted explanation should persist.
