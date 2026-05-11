# Running Packets

Ralph has two roles: launcher and worker.

The launcher gathers context into a packet, chooses the context style and launch
transport, and starts the bounded run.

The worker reads the packet, uses the named context, performs the bounded task,
updates the records or artifacts the packet names, and returns the required output.

## Launch Transports

Use the transport the workspace supports:

- harness-native subagent
- headless harness command that reads the packet path
- manual fresh-context handoff
- another documented transport

Keep launch wrappers short. Every transport should point the worker at the packet
path, instruct the worker to read it first, and request the packet's output
contract. Put the mission, scope, context, stop conditions, and evidence
expectations in the packet itself.

## Before Launch

Before launching a worker, check:

- target and mission are clear
- context style is explicit
- live references or hermetic excerpts are sufficient for the run
- read scope and write scope are explicit
- branch and worktree are named when repository files may change
- evidence, review, or verification expectations are concrete
- stop conditions are clear
- placeholder text has been resolved where packet truth is required
- the packet has been saved under `.loom/packets/ralph/` and the launch wrapper
  points to that path

If these checks fail, fix the packet before launch.

When the packet file is writable, set `Status: running` immediately before or as
part of launch so future agents can distinguish an unlaunched packet from an
in-flight worker run.

## Worker Procedure

The worker should:

- read the whole packet
- load live references or inlined context according to `Context Style:`
- inspect the source files, records, evidence, claims, or artifacts named by read
  scope
- make only changes allowed by write scope
- gather the expected evidence, review findings, or validation output
- create or update records and artifacts named by the packet
- fill the packet Worker Output section when allowed by write scope
- set packet status to `consumed` when output is recorded

When the packet file is not writable, return output through the launch transport
and identify where the parent must preserve it. Runs that support closure,
acceptance, evidence, audit, research, knowledge, or future recovery should leave
durable packet output or a cited durable record, not transport-only output.

The worker should not silently widen scope. When the safe next move is outside the
packet, return `blocked` or `escalate`.

## Worker Output

Worker output should include:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

The output should be precise enough that the next agent can read the packet,
changed records, evidence, and diff without replaying the worker's tool log.

## After Worker Return

After the worker returns, read:

- the packet
- worker output
- changed records or artifacts
- evidence named by the worker
- changed files or diffs

Then decide the next move:

- launch another packet
- request audit or another review pass
- update the consuming surface
- return to outer-loop shaping
- promote reusable learning into knowledge
- stop when the target is satisfied or the run is no longer needed

## Stop Conditions

Common stop conditions:

- packet no longer matches the target or source state
- needed context is missing
- write scope is too narrow or ambiguous
- work reveals a product, architecture, policy, sequencing, or scope decision
- expected evidence or review output cannot be gathered
- verification posture cannot be satisfied
- the task needs audit, research, specs, planning, or operator judgment before more
  worker execution

Stop when continuing would make the graph less truthful.

## Parallel Packets

Run packets in parallel only when their dependencies and write scopes do not
overlap.

Avoid parallel execution for shared migrations, generated files, lockfiles,
stateful resources, broad formatting, or ambiguous ownership.

Each parallel worker gets its own packet and records its own output. Read each
result before depending on combined work.
