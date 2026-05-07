---
name: loom-plans
description: "Maintain sequencing and rollout strategy. Use when a feature, refactor, migration, architecture change, or multi-step objective needs ordered tickets, dependencies, tranches, or parallel execution waves."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: owner-layer
  owns_layer: plan
---

# loom-plans

Plans own execution strategy.

They explain how the work should be sequenced without trying to replace ticket truth.

## What This Skill Owns

- rollout strategy
- decomposition
- sequencing
- milestones at the execution-strategy layer
- explicit route from initiative/spec to ticket work

## Naming

Create new plan records as `.loom/plans/<YYYYMMDD>-<slug>.md`.
The canonical ID remains `plan:<slug>` without the date prefix. Use the record
creation date for the filename prefix so plans support temporal discovery and
future retention or cleanup decisions.

## Milestone Boundary

Plan milestones are execution-sequencing checkpoints.

They are not constitutional roadmap direction, initiative outcome metrics, or
ticket progress state. If a plan starts recording what happened today, move that
truth into the ticket journal or evidence.

## Use This Skill When

- multiple tickets need one sequencing owner
- rollout order matters
- dependencies need to be made visible
- the project needs an execution strategy that should outlive one ticket

## Do Not Use This Skill When

- the work is already one bounded ticket
- the layer should really be initiative or spec
- you are tempted to use the plan as a progress log

## Good Plan Questions

A strong plan answers:

- what the overall route is
- why the sequence is ordered this way
- what milestones exist
- what risks and dependencies shape the sequence
- which tickets should exist beneath it
- which slices are vertical enough to produce working, verifiable progress
- which sections are thin on confidence, such as weak rationale, vague file or
  record scope, missing test/evidence targets, or unresolved owner-layer gaps
- where checkpoints or loopbacks should happen before continuing

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll figure out the order while implementing." | Hidden sequencing becomes rework. Plans exist when order, dependency, or parallelism matters. |
| "A complete plan should decompose everything." | Decompose enough to make the next safe tranche clear; do not manufacture roadmap theater. |
| "Parallel work is faster." | Parallel tickets are safe only when dependencies and write scopes do not conflict. |
| "The plan can track progress." | Tickets own live execution state. Plans own strategy snapshots and sequencing. |

## Red Flags

- tasks are horizontal layers that cannot be verified independently
- ticket slices are too large for one focused execution/review loop
- execution waves lack write-scope or dependency checks
- plan snapshot is being used as a progress log
- evidence or critique expectations are absent for risky tranches

## Verification

- [ ] Claim/acceptance coverage maps to downstream tickets or explains why none applies.
- [ ] Ticket slices are small, ordered by dependency, and leave reviewable checkpoints.
- [ ] Plan confidence gaps have been fixed, routed outward, or recorded as explicit assumptions.
- [ ] Parallel waves, if any, include non-overlap and parent reconciliation checks.
- [ ] Risks name owner-layer loopbacks when execution discovers missing truth.

## Done Means

- a future agent can see the intended route without reading transcript history
- the plan sequences the work without swallowing live execution state

## Read In This Order

Read immediately for normal plan creation or review:

1. `references/plan-shape.md` when creating or reviewing a plan's structure.

Then read conditionally:

2. `references/slicing.md` when decomposing a plan into ticket-sized work.
3. `skills/loom-workspace/references/problem-shaping.md` when the request is
   still too fuzzy to become a plan.
4. `templates/plan.md` only when creating or substantially reshaping a plan
   record.
