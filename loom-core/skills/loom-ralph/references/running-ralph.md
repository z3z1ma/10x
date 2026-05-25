# Running Ralph

Ralph has a launcher role and a worker role.

The launcher checks durable context, chooses context style and transport, and
starts one bounded run. The worker reads the named ticket or target records, acts
inside scope, updates allowed records or artifacts, and returns the output
contract.

## Launch Transports

Use the supported transport: harness subagent, headless harness command, manual
handoff, or another documented transport.

Keep launch wrappers short. Point at the ticket or target records, require the
worker to read them first, and request the output contract. Durable mission, scope,
context, stop conditions, and evidence expectations must already be in the ticket
or owning records.

## Before Launch

Check:

- target and mission are clear
- context style is explicit and sufficient
- read scope and write scope are explicit
- branch and worktree are named when repository files may change
- evidence, review, or validation expectations are concrete
- stop conditions are clear
- placeholder text has been resolved where durable truth is required
- the launch points at records instead of becoming the durable contract

If these fail, update or block the ticket or owning surface before launch.

## Worker Procedure

The worker should:

- read the named ticket, target, and linked records
- load live references or inlined context according to context style
- inspect sources, records, evidence, claims, or artifacts named by read scope
- mutate only what write scope allows
- gather expected evidence, review findings, or validation output
- update named records or artifacts when authorized
- return the required output

Do not silently widen scope. Return `blocked` or `escalate` when the safe next move
is outside the run.

## Worker Output

Include outcome (`continue`, `stop`, `blocked`, or `escalate`), files changed,
records changed, evidence/review/validation/observations gathered, what was not
verified, blockers, risks, assumptions, and recommended next move.

Output should let the next agent read the ticket, changed records, evidence, and
diff without replaying the worker's tool log.

## After Return

Read the target record, worker output, changed records/artifacts, named evidence,
and changed files or diff. Then choose another bounded Ralph run, audit/review,
consuming-surface update, shaping, knowledge promotion, or stop.

## Stop Conditions

Stop when the ticket or target no longer matches source state, needed context is
missing, write scope is too narrow or ambiguous, work reveals a product,
architecture, policy, sequencing, or scope decision, expected evidence cannot be
gathered, verification posture cannot be satisfied, or the task needs audit,
research, specs, planning, or operator judgment before more execution.

Parallel runs are safe only when dependencies and write scopes do not overlap.
Independent closure stories need separate child tickets; one ticket may coordinate
non-overlapping sub-scopes only when it still owns one closure claim.
