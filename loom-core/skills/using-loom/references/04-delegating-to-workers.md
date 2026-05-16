# Delegating To Workers

Use strict boundaries when the operator is temporarily out of the loop.

When ticket work is executed or delegated, use a bounded Ralph run from the ticket
and linked records. The ticket is the durable execution contract for the work unit;
the launch prompt is only a transient transport wrapper.

The durable context should make one bounded worker run recoverable, reviewable,
and safe to continue after the worker returns without replaying chat or harness
logs.

## Ticket Context Before Launch

A Loom worker run starts from graph-supported context, usually an executable
ticket and its linked records. Before invoking a harness-native subagent, headless
harness command, or manual worker handoff, make sure the ticket or owning surface
contains the durable mission, context, scope, stop conditions, evidence
expectations, and allowed updates.

Keep the launch wrapper thin: identify the ticket or target records to read first,
name the immediate run objective, restate only transient constraints that matter
for transport, and request the required worker output. Do not hide durable scope,
acceptance, write boundaries, or evidence expectations only in the prompt.

When a worker result will support ticket state, audit, evidence, research,
knowledge, or closure, reconcile the material output into the ticket or the Loom
surface that owns it.

## When To Use A Ralph Run

Use a Ralph run when the next worker or review run can be bounded.

Good worker tasks have a clear mission, limited scope, known source records,
defined read and write areas, expected evidence or review output, and recognizable
stop conditions.

Do not delegate work that still needs operator shaping, high-authority judgment,
ambiguous product intent, unresolved policy, broad architectural direction,
unsettled data-model or state-modeling choices, or design-coherence decisions.
Shape that work first.

## Durable Run Context

A useful ticket-owned run context tells the worker:

- the mission for this run
- the source records, refs, evidence, diffs, or artifacts to inspect
- the intended read area
- the intended write area
- the task boundary and non-goals
- relevant assumptions and constraints
- stop conditions
- expected evidence, review output, or validation result
- output expectations
- which records or artifacts should be updated while working

The worker should not have to infer scope from chat history.

The run should be narrow enough that the worker can finish, stop, or report
blockage without inventing a plan of its own. If the durable context is missing,
update or block the ticket before launch instead of putting the missing truth only
in the prompt.

## Worker Authority

The worker operates inside the ticket-owned run boundary.

The worker may update source or work files within scope, the records or evidence
artifacts named by the ticket or launch, and the worker output requested by the
coordinator. If new evidence is needed but not authorized by write scope, the
worker should stop or report the needed evidence instead of widening scope.

The worker should not directly change high-authority direction while executing.
Escalate before changing constitution, specs, plans, or research synthesis.

Knowledge updates should be proposed, not applied, unless the ticket explicitly
authorizes that promotion.

Audit is a separate adversarial pass. A worker implementation report is not audit,
and a worker should not certify its own work as accepted.

## Worker Discipline

The worker should stop and report when:

- the ticket or run context no longer matches reality
- the requested change is broader than the declared scope
- required context is missing
- evidence or review output cannot be gathered
- implementation reveals a product, architecture, policy, or sequencing decision
- the safe next step belongs to another Loom surface

A worker should not silently widen scope to stay busy.

## Worker Output

The worker reports:

- what changed
- what evidence, review output, or validation result was gathered
- what was not verified or reviewed
- what remains blocked or risky
- what records were updated
- what it recommends next

## After Worker Return

The parent reads the ticket, updated records, evidence, changed files, and worker
report instead of reconstructing work from tool logs.

The parent decides whether to stop, run another bounded worker run, gather more
evidence, route to audit, return to outer-loop shaping, update another surface, or
promote learning into knowledge.

When the result will support closure, acceptance, or durable reuse, route the claim
through a bounded Ralph review before treating the work as trustworthy unless the
consuming surface explicitly records why audit would not add useful trust. The
audit may be a narrow pass over the target records, evidence, and diff.

## Run Currency

Use a run only while its target, context, scope, and assumptions still match
reality.

If the work has materially changed, update or block the ticket and launch a fresh
bounded run instead of asking the worker to guess.
