# Ralph Run Shape

A Ralph run should be small enough to run and complete enough that the worker can
act from the ticket or target records named by the launch.

The durable handoff lives in the owning Loom surface, usually a ticket. The launch
prompt is transport. Write durable mission, scope, read and write boundaries, stop
conditions, evidence expectations, and reconciliation needs into the ticket or
owning records before launch.

## Required Shape

A useful Ralph run has:

- a concrete target or target set
- one worker mission
- records, files, evidence, diffs, claims, or references to inspect
- a context style: live-reference, hermetic, or hybrid
- read scope
- write scope
- expected evidence, review, or verification output
- stop, block, and escalation conditions
- an output contract
- a reconciliation target for worker output

Put durable decisions in their normal Loom surfaces and cite or inline only what
the worker needs for the run.

## Target And Mission

The target can be a ticket, audit target, claim, record, diff, branch, package,
source path, or bounded task slug.

The mission should describe the result of this run. If the mission needs unrelated
changes or multiple review jobs, split the work or launch narrower runs from
separate tickets or target records.

## Context Binding

A Ralph run binds context across Loom without creating a separate truth surface.

Useful context groups include:

- records: tickets, specs, plans, research, constitution, evidence, audit, or
  knowledge
- source files or directories
- diffs, commits, branches, pull requests, packages, or release artifacts
- command outputs, screenshots, logs, reproductions, or other evidence
- external references when the launch names why they matter

Separate intended behavior from current implementation reality. Separate observed
evidence from interpretation. A run can gather these together without merging their
responsibilities.

## Read Scope And Write Scope

Read scope names what the worker should inspect.

Write scope names what the worker may mutate.

Write scope may include source paths, Loom records, evidence artifact paths, or
`None - <reason>` for read-only runs.

When the run authorizes record updates, name the exact records or surface. The
worker should keep those records truthful as it works.

High-authority records such as constitution, specs, plans, and research synthesis
should be changed only when the ticket or owning surface names the exact record and
the target work requires that change.

## Source Snapshot

Source snapshot is the run's currency handle.

It may include:

- target status, claim state, or current review state
- records, files, diffs, or artifacts inspected before launch
- branch and worktree
- known dirty or concurrent work that affects the run
- important excerpts or summaries that would otherwise be easy to miss

If target, context, scope, source state, or assumptions change materially before
launch, update or block the ticket or owning surface before launching.

## Worker Output Reconciliation

The coordinator should say where worker output belongs after return.

When observations should remain available, create or update evidence and cite it
from the consuming surface when applicable.

When the worker changes a record named by write scope, it should update that
record's current state, journal, findings, limitations, or related-record notes in
the way that surface expects.

Worker output should summarize outcome, changed files, records changed, evidence
gathered, unverified claims, risks, blockers, and recommended next move. Preserve
that output in the ticket or another owning surface when future recovery depends on
it.

## Run Currency

Use a Ralph run only while its target, context, scope, source state, branch,
worktree, and assumptions still match reality.

Refresh the ticket or owning surface before relaunching stale work.
