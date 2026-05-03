# Slicing

A plan should produce bounded tickets.

Use this question repeatedly:

> what is the next smallest slice that can make meaningful progress without widening scope?

A good ticket slice is:

- independently legible
- testable or reviewable
- not secretly several tickets glued together
- small enough for one Ralph iteration or a short sequence of Ralph iterations
- explicit about the likely write boundary and verification posture
- able to stop cleanly if a dependency, behavior question, or evidence gap
  appears

If the plan cannot yield slices like that, keep decomposing.

## Execution

Plans are not executed by checking off plan prose as the live ledger.

Execute a plan by creating or advancing bounded tickets beneath it. The ticket,
linked owner records, evidence, critique disposition, blockers, and journal should
make the next action inferable without a serialized workflow field. Common actions
include a tiny local edit, Ralph packet, reproduce-first debugging, bounded spike,
codemap, evidence recording, critique, wiki/retrospective promotion, ticket-owned
acceptance evaluation, or ship packaging. Shipping does not close the ticket.

If the current state needs operator input, workspace repair, records repair,
owner-layer shaping, evidence preservation, continuation, or stop, handle that
need directly in the owner layer instead of forcing another execution pass.

If a plan step looks like a task checklist, translate it into ticket acceptance,
packet task text, or evidence expectations before a worker starts. Do not let a
plan checkbox become the only place that knows what happened.

## Stop Conditions

Return to plan or upstream shaping when:

- the next slice would touch too many unrelated files or records
- the same slice needs several independent children
- acceptance criteria are missing or contradict a spec
- verification would be impossible to evidence honestly
- two planned children would contend on generated files, lockfiles, migrations,
  shared state, or the same source paths
