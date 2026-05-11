---
name: loom-parallel-worker-coordination
description: "Use when multiple independent tasks or packets can run concurrently and need coordination, non-overlapping write scopes, worker packet boundaries, integration reconciliation, and combined evidence/audit."
---

# loom-parallel-worker-coordination

Parallel worker coordination is a Ralph orchestration playbook.

It proves tasks are independent, dispatches bounded packets, integrates returned
work deliberately, and records evidence and audit before trusting the combined
result.

## Loom Surfaces

Route durable results through `loom-plans`, `loom-tickets`, `loom-ralph`,
`loom-evidence`, `loom-audit`, and `loom-retrospective`.

When routing to any named Loom skill, follow that skill's procedure and guidance
completely. This playbook adds workflow pressure; it does not shorten the target
skill's requirements.

It coordinates packets. It does not make worker reports authoritative.

## Use This Playbook When

Use this playbook when:

- a plan has independent child tickets or execution units
- multiple failures appear in separate files, subsystems, or domains
- each worker can receive a self-contained packet
- write scopes do not overlap
- the integration risk is lower than the cost of sequential work

Skip it when tasks share state, edit the same files, require a common design
decision, depend on each other's output, or need one agent to understand the whole
system before splitting.

## Route

Use this route:

```text
partition -> prove independence -> packetize -> dispatch -> reconcile -> integrate -> verify -> audit
```

## Partition

Start from a plan, ticket set, failure set, or explicit operator goal.

Group work by domain:

- one test file or failure cluster
- one subsystem or adapter
- one independent consumer migration
- one documentation or record subset
- one contract-compatible implementation slice

If a group is still broad, split it before dispatch. If groups depend on each
other, sequence them instead.

## Prove Independence

Before parallel dispatch, check:

- no overlapping write scope
- no shared generated files unless one worker owns them
- no shared database or migration state without ordering
- no common unresolved spec or policy question
- no hidden setup step that mutates shared state
- each worker can verify its own slice

When independence is uncertain, run one packet first or route back to planning.

## Packetize

Create one Ralph packet per independent unit.

Each packet should include:

- governing ticket, plan unit, spec IDs, and evidence targets
- full task text or bounded mission
- read scope and write scope
- explicit files or records the worker may change
- verification posture
- stop conditions
- expected output and status vocabulary

Useful worker statuses are:

- `done`: completed and verified within scope
- `done_with_concerns`: completed but raised correctness, scope, evidence, or design concern
- `needs_context`: requires missing information before safe progress
- `blocked`: cannot proceed without replanning, stronger model, operator decision, or smaller task

Do not ask workers to infer missing context from the parent transcript.

## Dispatch

Dispatch only packets that can safely run together.

Keep the parent focused on coordination:

- track packet IDs and write scopes
- avoid editing the same files while workers run
- preserve worker outputs for reconciliation
- stop dispatching new packets if one returns a blocker that changes shared design

## Reconcile

When workers return, evaluate each output before integration.

For each packet:

- inspect changed files or records, not only the report
- compare output to packet mission and ticket acceptance
- classify concerns, blockers, and evidence gaps
- update the parent ticket or child ticket state
- route durable observations to evidence or audit

Worker success reports are claims to check, not evidence by themselves.

## Integrate

Integrate in an order that minimizes conflicts and preserves traceability.

Check:

- write-scope conflicts
- incompatible assumptions between workers
- duplicated helpers or divergent patterns
- generated-file or formatting churn
- whether one worker's change invalidates another worker's evidence

If integration reveals coupling, stop parallel execution and route back to plans,
specs, tickets, or operator decision.

## Verify And Audit

After integration:

- run focused checks for each slice when still meaningful
- run combined checks that prove the integrated result
- record evidence for before/after or merged verification claims
- use `loom-audit` when the combined result depends on subtle integration,
  non-overlap assumptions, or worker-reported correctness

## Done Means

The parallel coordination pass is done when:

- independence was checked before dispatch
- each worker had a bounded packet and write scope
- worker output was inspected and reconciled
- integrated changes have combined evidence
- conflicts, concerns, blockers, and follow-up are visible in Loom records
