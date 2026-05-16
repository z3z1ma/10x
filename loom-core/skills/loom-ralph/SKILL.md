---
name: loom-ralph
description: "Use when Loom work needs a bounded Ralph subagent, harness run, implementation slice, review pass, or worker handoff built from tickets, records, files, evidence, claims, or other bounded context."
---

# loom-ralph

Ralph is Loom's bounded worker and review discipline.

A Ralph run starts from durable Loom context, usually a ticket and its linked
records, then uses a transient launch prompt to carry one bounded worker or review
task. The durable context names the target, mission, read scope, write scope, stop
conditions, evidence or review expectations, and output reconciliation target.

Most Ralph runs use a harness-native subagent. A Ralph run can also use a headless
harness command, manual handoff, or another transport that reads the named durable
records and returns the required output. Regardless of transport, the prompt stays
thin and points the worker at the ticket, audit target, evidence request, or other
bounded source of truth.

Ralph supplies run discipline. The consuming surface still records the judgment,
state, or durable result it owns. Tickets may use Ralph for implementation, audit
may use Ralph for adversarial review, and other Loom surfaces may use Ralph when
bounded worker execution improves the work.

A Ralph run has two parts: durable context in the owning Loom surface and a
transient launch transport. The durable context is the worker contract; the launch
wrapper should stay thin so future agents can recover the handoff from the
repository graph.

## Use This Skill When

Use this skill when:

- preparing a bounded worker or review run from Loom records, files, evidence,
  diffs, claims, or external references
- choosing live-reference, hermetic, or hybrid context style for a launch
- launching a bounded subagent or harness run from a ticket or other durable target
- defining read scope, write scope, stop conditions, or worker output
- reconciling worker output into tickets, evidence, audit, knowledge, or another
  owning surface
- deciding whether durable run context is current enough to launch

Shape the work before launching it. A Ralph run should begin from a clear target,
mission, context boundary, write boundary, and output expectation.

## Dispatch

If preparing or launching a Ralph run:

- read `references/run-shape.md`
- read `references/running-ralph.md`
- read `references/verification-posture.md` when the run needs implementation
  or validation evidence
- read the records and source material needed to bind the run context
- ensure durable context lives in the ticket or owning records before launch
- write a launch prompt narrow enough for one worker run
- when launching, point the worker at the ticket or target records and request the
  run's output contract

If executing inside a Ralph run:

- read the named ticket, target, or durable records before editing or reviewing
- read live references or inlined context according to the requested context style
- stay inside the declared read scope and write scope
- update only records named by the ticket, owning surface, or launch when those
  updates are part of the worker contract
- stop when a stop condition applies
- return the required worker output

If reading worker output after a Ralph run:

- read the ticket or target, worker output, changed records, evidence, and changed
  files
- update the consuming surface when additional judgment or routing is needed
- decide whether the next move is another Ralph run, audit, closure, shaping,
  knowledge promotion, or another Loom surface

## Context Styles

Use one of these context styles:

- `live-reference`: the launch names the records, files, evidence, diffs, or
  external references the worker should read in the workspace
- `hermetic`: the launch inlines the relevant record text, excerpts, diffs, or
  artifacts needed for the run
- `hybrid`: the launch inlines the critical context and also points at live sources
  for inspection

Live-reference runs are useful when current workspace state matters. Hermetic runs
are useful when a worker should review a frozen context bundle.

## Worker Outcomes

The worker returns one outcome:

- `continue`: useful progress happened and another run is likely
- `stop`: this run's work is complete
- `blocked`: a concrete blocker prevents safe progress
- `escalate`: the next move needs higher-level shaping, policy, review, or another
  Loom surface

Worker outcome is run output. The consuming surface decides what that outcome
means for its own record.

## Ralph Run Invariants

Every Ralph run should preserve these invariants:

- explicit target or target set
- one bounded worker run
- context packaged as live references, hermetic content, or a deliberate hybrid
- clear mission and output contract
- explicit read scope and write scope
- worker permission to update only the records, files, and evidence artifacts named
  by the ticket, owning surface, or launch
- worker output reconciled durably when the result supports closure, acceptance,
  evidence, audit, research, knowledge, or future recovery
- branch and worktree named when repository files may change
- evidence, review, or verification expectation appropriate to the mode
- stop conditions that fail closed instead of widening scope
- worker output sufficient for the next agent to continue, inspect, or review
- no secret, credential, private key, token, password, or sensitive personal data
- no stale run context used after the target, scope, context, or assumptions changed

## Done Means

Ralph work is done when:

- the durable run context was sufficient and current before launch
- the worker stayed inside the run boundary or stopped when it could not
- named record and evidence updates were made or explicitly reported as missing
- worker output states what happened, what changed, what was observed, what remains
  unverified, and what next move is recommended
- the consuming surface can use the reconciled worker output without replaying the
  worker's tool log
