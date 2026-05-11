# Packet Shape

A packet should be small enough to run and complete enough that the worker can act
from the packet and its named context.

The packet is the durable handoff. Write it to `.loom/packets/ralph/` before the
worker is launched so the parent, worker, and future agents share the same
inspectable contract.

## Required Shape

A useful packet says:

- what target or target set the run concerns
- what this one worker run should accomplish
- which Loom records, source files, evidence, diffs, claims, or references matter
- whether context is live-reference, hermetic, or hybrid
- what the worker may read
- what the worker may change
- which records or artifacts the worker should update
- what evidence, review, or verification expectation applies
- when the worker must stop, block, or escalate
- what output the worker must return

Put durable decisions in their normal Loom surfaces and cite or inline them from
the packet.

## Target And Mission

The target can be a ticket, audit target, claim, record, diff, branch, package,
source path, or bounded task slug.

The mission should describe the result of this run. If the mission needs unrelated
changes or multiple review jobs, split the work or write narrower packets.

## Context Binding

A Ralph packet binds context across Loom.

Useful context groups include:

- records: tickets, specs, plans, research, constitution, evidence, audit, or
  knowledge
- source files or directories
- diffs, commits, branches, pull requests, packages, or release artifacts
- command outputs, screenshots, logs, reproductions, or other evidence
- external references when the packet names why they matter

Separate intended behavior from current implementation reality. Separate observed
evidence from interpretation. A packet can gather these together without merging
their responsibilities.

## Context Styles

Use `Context Style: live-reference` when the worker should read current records and
source material directly.

Use `Context Style: hermetic` when the packet should carry the relevant context in
the packet itself. Hermetic packets should include the excerpts, diffs, claims,
evidence, and source summaries needed for the run.

Use `Context Style: hybrid` when critical context should be inlined and the worker
should also inspect live sources.

## Read Scope And Write Scope

Read scope names what the worker should inspect.

Write scope names what the worker may mutate.

Write scope may include source paths, Loom records, evidence artifact paths, the
packet's Worker Output section, or `None - <reason>` for read-only runs.

When the packet authorizes record updates, name the exact records or surface. The
worker should keep those records truthful as it works.

High-authority records such as constitution, specs, plans, and research synthesis
should be changed only when the packet names the exact record and the target work
requires that change.

## Branch And Worktree

When repository files may change, name the branch and worktree in the packet top
labels.

If either value is unknown, say `unknown - <reason>` and explain why the packet is
still safe to run. Unknown branch or worktree is a launch smell for mutating work.

The packet needs enough source state for the worker and next agent to understand
where execution happened and whether a fresh packet is needed.

## Source Snapshot

Source snapshot is the packet's freshness handle.

It may include:

- target status, claim state, or current review state
- records, files, diffs, or artifacts inspected before compiling the packet
- branch and worktree
- known dirty or concurrent work that affects the packet
- important excerpts or summaries that would otherwise be easy to miss

If target, context, scope, source state, or assumptions changed materially after
compilation, update the packet before launch or mark it `superseded` and write a
fresh one.

## Worker Record Updates

The packet should say what the worker updates while working.

When observations should remain available, the worker should create or update
evidence and cite it from the consuming surface when applicable.

When the worker changes a record named by write scope, it should update that
record's current state, journal, findings, limitations, or related-record notes in
the way that surface expects.

The packet's Worker Output section should summarize outcome, changed files,
records changed, evidence gathered, unverified claims, risks, blockers, and
recommended next move.

## Freshness

Use a packet only while its target, context, scope, source state, branch, worktree,
and assumptions still match reality.

Refresh or supersede stale packets.
