---
name: loom-retrospective
description: "Use after significant completed or reviewed work when durable lessons, prevention notes, follow-up routing, or reusable knowledge should survive the session."
---

# loom-retrospective

Retrospective is Loom's promotion and prevention pass. It reviews significant work
after implementation, audit, investigation, launch, bug fixing, or repeated
friction, then routes reusable lessons into existing Loom surfaces. It has no
directory of its own.

## Use This Skill When

Use this skill when:

- a meaningful ticket is closing or moving through final review
- an audit, Ralph run, research pass, bug fix, spike, migration, or launch produced
  reusable learning
- the same explanation, mistake, question, or operator correction has appeared more
  than once
- a prevention note, follow-up ticket, evidence record, or knowledge record may stop
  repeated work
- a significant work thread is ending and the graph should preserve what matters

Skip retrospective when there is no durable lesson, prevention need, or reusable
context to preserve.

## Dispatch

Run a retrospective pass:

- read `references/promotion-and-prevention.md`
- inspect the work being closed or assimilated: ticket, plan, research, audit,
  evidence, worker output, diff, or related records
- separate durable lessons from one-time execution detail
- route each lesson to the surface that can carry it
- use the owning skill before changing specs, plans, constitution, or research
  synthesis; pause for operator authority when the lesson changes behavior,
  strategy, durable judgment, or conclusions
- update the originating record when follow-through should be visible there

Check whether retrospective is needed:

- inspect the work record and evidence or audit state
- say whether there is durable learning to promote, prevention follow-up to create,
  or no retrospective work needed

## Loop

Use:

```text
observe -> distill -> promote -> prevent
```

Observe concrete signals from records, evidence, audit findings, worker output,
changed files, repeated questions, and operator corrections. Distill durable
lessons separately from local execution detail. Promote accepted lessons through
the owning surface's procedure and authority gates. Prevent repeated mistakes with
the smallest useful follow-through artifact, or record that no durable action is
needed when that helps recovery.

## Routes

- accepted explanation, preference, procedure, troubleshooting pattern, atlas,
  entity note, or retrieval cue -> `loom-knowledge`
- durable investigation result, tradeoff, rejected option, or null result -> `loom-research`
- clarified intended behavior, interface expectation, requirement, scenario, or
  invariant -> specs
- changed strategy, decomposition, sequencing, or recovery route -> `loom-plans`
- durable project judgment, principle, constraint, decision, or roadmap direction
  -> `loom-constitution`
- observed artifact, validation output, reproduction, screenshot, log, scan, or command result -> `loom-evidence`
- executable follow-up work -> `loom-tickets`
- Ralph-backed challenge, risk review, missing-evidence concern, or closure doubt
  -> `loom-audit`

Knowledge is the usual home for reusable explanations and prevention notes. Use a
different surface when the lesson is not knowledge-shaped.

If no prevention artifact is useful, say so in the originating record or final
summary when that improves recovery.

## Originating Records

Update the originating ticket, plan, research record, audit, or worker-output
record when future continuation or closure would be worse without the note. Good
updates include:

- what was promoted
- what follow-up was created
- what was intentionally not promoted
- what remains blocked, risky, or unverified
- which records now carry the durable lesson

The graph should show follow-through in records that already matter.

## Stop Conditions

Stop or route before promotion when:

- the lesson would change intended behavior, strategy, durable judgment, research
  synthesis, or acceptance without the owning skill and needed authority
- the signal is only local execution detail with no future retrieval or prevention
  value
- the right follow-up is executable work that needs a ticket before implementation
- a closure claim still needs evidence or audit rather than a retrospective note

## Done Means

Retrospective work is done when:

- durable lessons are separated from one-time execution detail
- accepted lessons are promoted into existing Loom surfaces
- high-authority promotions used the owning skill and required operator authority
  when they changed intended behavior, strategy, durable judgment, or conclusions
- prevention follow-up exists where it helps
- the originating record says what happened when that improves recovery or closure
- no reusable lesson remains only in chat, worker output, or a hard-to-find journal
- follow-through is visible in existing surfaces
