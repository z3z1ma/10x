# Slicing

A plan should produce bounded tickets.

Use this question repeatedly:

> what is the next smallest slice that can make meaningful progress without widening scope?

A good ticket slice is:

- independently legible
- testable or reviewable
- vertical enough to exercise the relevant user, API, data, or operator path
  instead of only building one horizontal layer
- not secretly several tickets glued together
- small enough for one Ralph iteration or a short sequence of Ralph iterations
- explicit about the likely write boundary and verification posture
- names the source claim, likely affected files or records, and expected
  test/evidence target without becoming a step-by-step implementation script
- able to stop cleanly if a dependency, behavior question, or evidence gap
  appears

If the plan cannot yield slices like that, keep decomposing.

Prefer tracer-bullet slices when possible: one narrow path through the real
interfaces, data, validation, and user/operator surface. Horizontal slices are
acceptable only when the layer itself is the product of the ticket, such as a
schema migration preparation step, a shared validation harness, or an explicitly
bounded refactor prerequisite.

Common slicing modes:

- vertical tracer bullet: one real path through the interface, behavior,
  validation, and observable result; prefer this for product and API work
- contract-first: define or tighten the shared contract first when multiple
  workers or surfaces must integrate against it, then slice implementation
  against that contract
- risk-first: prove the riskiest assumption or integration before filling in safer
  surrounding work
- cleanup-only: isolate behavior-preserving simplification or dead-code removal so
  review can distinguish it from new behavior

Each slice should leave a verifiable or reviewable state. If a slice cannot be
verified independently, either make it smaller, change the evidence plan, or route
back to spec/research/plan shaping.

## Execution

Plans are not executed by checking off plan prose as the live ledger.

Execute a plan by creating or advancing bounded tickets beneath it. The ticket,
linked owner records, evidence, critique disposition, blockers, and journal should
make the next action inferable without a serialized workflow field. Common actions
include tiny local execution, Ralph packet, reproduce-first debugging, bounded spike,
codemap, evidence recording, critique, wiki/retrospective promotion, ticket-owned
acceptance evaluation, or ship packaging. Shipping does not close the ticket.

If the current state needs operator input, workspace repair, records repair,
owner-layer shaping, evidence preservation, continuation, or stop, handle that
need directly in the owner layer instead of forcing another execution pass.

If a plan step looks like a task checklist, translate it into ticket acceptance,
packet task text, or evidence expectations before a worker starts. Do not let a
plan checkbox become the only place that knows what happened.

Avoid micro-step choreography in plans. A slice should tell a worker what outcome,
scope, patterns, verification target, and loopback conditions matter; tickets and
packets own the live execution contract.

For complex implementation handoffs, apply the zero-context worker test before
creating tickets: a capable fresh worker should understand the goal, files or
records likely involved, constraints, verification target, stop conditions, and
non-goals without transcript context. If the plan only says "implement this" or
"handle edge cases," it is not ready to drive a ticket.

## Stop Conditions

Return to plan or upstream shaping when:

- the next slice would touch too many unrelated files or records
- the same slice needs several independent children
- acceptance criteria are missing or contradict a spec
- verification would be impossible to evidence honestly
- two planned children would contend on generated files, lockfiles, migrations,
  shared state, or the same source paths
