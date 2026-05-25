---
name: loom-ralph
description: "Use when Loom work needs a bounded Ralph subagent, harness run, implementation slice, review pass, or worker handoff built from tickets, records, files, evidence, claims, or other bounded context."
---

# loom-ralph

Ralph is Loom's bounded worker and review discipline.

A Ralph run has durable context in a ticket or owning surface and a thin transient
launch transport. The durable context names the target, mission, read scope, write
scope, stop conditions, evidence or review expectations, and where worker output
will be reconciled. The launch prompt points at that context; it is not the durable
contract.

Ralph can use a harness subagent, headless harness command, manual handoff, or
other transport. The consuming surface still owns the resulting state or judgment:
tickets own execution and closure, evidence owns observations, audit owns
adversarial review records, and other records keep their own truths.

## Use This Skill When

Use this skill when preparing, launching, executing, or reconciling a bounded
worker or review run from tickets, records, files, diffs, claims, evidence, or
external references.

Also use it when defining read scope, write scope, stop conditions, worker output,
context style, or whether run context is current enough to launch.

Do not launch Ralph to resolve unshaped product intent, policy, architecture,
scope, data/state modeling, or design-coherence choices. Shape or route those
first.

## Dispatch

If preparing or launching:

- read `references/run-shape.md`
- read `references/running-ralph.md`
- read `references/verification-posture.md` when implementation or validation
  evidence is expected
- read records and source needed to bind the run
- ensure durable context lives in the ticket or owning record before launch
- write a short launch that points at the target records and asks for the output
  contract

If executing inside a Ralph run:

- read the named ticket, target, and linked records first
- follow the requested context style: `live-reference`, `hermetic`, or `hybrid`
- stay inside declared read and write scope
- update only named records, files, or artifacts authorized by the ticket, owning
  surface, or launch
- stop when a stop condition applies
- return the required output

If reconciling worker output:

- inspect the ticket or target, worker output, changed records, evidence, and diff
- treat worker output as claims until checked against scope and evidence
- update the consuming surface when future recovery depends on it
- choose the next move: another Ralph run, audit, closure, shaping, knowledge
  promotion, or stop

## Context Styles

- `live-reference`: launch names records, files, evidence, diffs, or external
  references the worker should read in the workspace
- `hermetic`: launch inlines the relevant context bundle
- `hybrid`: launch inlines critical context and points at live sources

Use live-reference when current workspace state matters; hermetic when the review
must use a frozen bundle.

## Worker Outcomes

Worker output returns one outcome:

- `continue`: useful progress happened and another run is likely
- `stop`: this run's work is complete
- `blocked`: a concrete blocker prevents safe progress
- `escalate`: the next move needs shaping, policy, review, or another Loom surface

The consuming surface decides what the run outcome means for its own state.

## Ralph Run Invariants

Every Ralph run keeps:

- one bounded worker or review mission
- explicit target, context style, read scope, and write scope
- durable context in ticket or owning records, not only in the launch prompt
- worker permission limited to named records, files, and artifacts
- branch and worktree named when repository files may change
- evidence, review, or verification expectations appropriate to the mode
- stop conditions that fail closed instead of widening scope
- output sufficient for continuation, inspection, or review
- reconciliation of output when it supports closure, acceptance, evidence, audit,
  research, knowledge, or future recovery
- no secrets or sensitive values persisted
- no stale run context used after target, scope, source state, or assumptions move

## Done Means

Ralph work is done when the worker contract was current, the run stayed in bounds
or stopped, named records/evidence were updated or reported missing, worker output
states changes, observations, unverified claims, risks, and next move, and the
consuming surface can proceed without replaying the tool log.
