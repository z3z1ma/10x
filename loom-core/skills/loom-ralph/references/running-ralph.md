# Running Ralph

Ralph has two roles: launcher and worker.

The launcher checks durable context, chooses the context style and launch
transport, and starts the bounded run.

The worker reads the named ticket or target records, uses the named context,
performs the bounded task, updates allowed records or artifacts, and returns the
required output.

## Launch Transports

Use the transport the workspace supports:

- harness-native subagent
- headless harness command that reads named records or inlined context
- manual Ralph handoff
- another documented transport

Keep launch wrappers short. Every transport should point the worker at the ticket
or target records, instruct the worker to read them first, and request the run's
output contract. Put durable mission, scope, context, stop conditions, and evidence
expectations in the ticket or owning records before launch.

## Before Launch

Before launching a worker, check:

- target and mission are clear
- context style is explicit
- live references or hermetic excerpts are sufficient for the run
- read scope and write scope are explicit
- branch and worktree are named when repository files may change
- evidence, review, or verification expectations are concrete
- stop conditions are clear
- placeholder text has been resolved where durable truth is required
- the launch prompt points to the ticket or target records instead of becoming the
  durable contract itself

If these checks fail, update or block the ticket or owning surface before launch.

## Worker Procedure

The worker should:

- read the named ticket, target, and linked records
- load live references or inlined context according to the context style
- inspect the source files, records, evidence, claims, or artifacts named by read
  scope
- make only changes allowed by write scope
- gather the expected evidence, review findings, or validation output
- create or update records and artifacts named by the ticket or launch
- return the required output for reconciliation

The worker should not silently widen scope. When the safe next move is outside the
run, return `blocked` or `escalate`.

## Worker Output

Worker output should include:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

The output should be precise enough that the next agent can read the ticket,
changed records, evidence, and diff without replaying the worker's tool log.

## After Worker Return

After the worker returns, read:

- the ticket or target record
- worker output
- changed records or artifacts
- evidence named by the worker
- changed files or diffs

Then decide the next move:

- launch another bounded Ralph run
- request audit or another review pass
- update the consuming surface
- return to outer-loop shaping
- promote reusable learning into knowledge
- stop when the target is satisfied or the run is no longer needed

## Stop Conditions

Common stop conditions:

- ticket or target no longer matches the source state
- needed context is missing
- write scope is too narrow or ambiguous
- work reveals a product, architecture, policy, sequencing, or scope decision
- expected evidence or review output cannot be gathered
- verification posture cannot be satisfied
- the task needs audit, research, specs, planning, or operator judgment before more
  worker execution

Stop when continuing would make the graph less truthful.

## Parallel Ralph Runs

Run workers in parallel only when their dependencies and write scopes do not
overlap.

Avoid parallel execution for shared migrations, generated files, lockfiles,
stateful resources, broad formatting, or ambiguous ownership.

Independent closure stories need separate child tickets. When one ticket truly owns
one closure claim, ticket-defined non-overlapping sub-scopes can coordinate
parallel runs. Reconcile each result before depending on combined work.
