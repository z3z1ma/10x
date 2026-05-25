# Ralph Run Shape

A Ralph run is one bounded worker or review mission that can act from the ticket or
target records named by launch.

The durable handoff belongs in the owning Loom surface, usually a ticket. The
launch prompt is transport. Put mission, scope, read/write boundaries, stop
conditions, evidence expectations, and reconciliation needs in durable records
before launch.

## Required Shape

A useful run names:

- concrete target or target set
- one mission
- records, files, evidence, diffs, claims, or references to inspect
- context style: `live-reference`, `hermetic`, or `hybrid`
- read scope and write scope
- expected evidence, review, or validation output
- stop, block, and escalation conditions
- output contract
- reconciliation target for worker output

Put durable decisions in their owning surfaces and cite or inline only what the
worker needs for this run.

## Target, Scope, Currency

The target can be a ticket, audit target, claim, record, diff, branch, package,
source path, or bounded task slug. Split if the mission needs unrelated changes or
multiple review jobs.

Read scope names what to inspect. Write scope names what may mutate, including
source paths, Loom records, evidence artifacts, or `None - <reason>` for read-only
runs. High-authority records such as constitution, specs, plans, and research
synthesis change only when the ticket or owning surface names the exact record.

Source snapshot is the run's currency handle: target status, record/file/diff state
inspected before launch, branch and worktree, known dirty work, and key excerpts.
If target, context, scope, source state, or assumptions change materially, update
or block the ticket or owning surface before launch.

## Context Binding

A run can gather records, source files, diffs, command outputs, screenshots, logs,
external references, and evidence without merging their responsibilities. Keep
intended behavior separate from implementation reality, and observations separate
from interpretation.

## Reconciliation

Say where worker output belongs. Preserve observations in evidence when another
surface will rely on them. When the worker changes a named record, update that
record in the way its surface expects.

Worker output should include outcome, changed files, changed records, evidence or
review gathered, unverified claims, risks, blockers, and recommended next move.
Preserve it in the ticket or another surface when recovery depends on it.
