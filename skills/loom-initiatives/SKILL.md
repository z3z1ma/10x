---
name: loom-initiatives
description: "Maintain strategic outcome framing. Use when work spans tickets, needs success metrics, delegated autonomy, or a long-lived objective owner."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: owner-layer
  owns_layer: initiative
---

# loom-initiatives

Initiatives own strategic outcomes.

They are the place where the project says, "this cross-cutting result matters enough to deserve its own durable owner."

## What This Skill Owns

- initiative records
- strategic objectives
- stable `OBJ-*` objective criteria under success metrics
- milestone framing
- success metrics and objective ownership
- explicit downstream execution graph

## Naming

Create new initiative records as `.loom/initiatives/<YYYYMMDD>-<slug>.md`.
The canonical ID remains `initiative:<slug>` without the date prefix. Use the
record creation date for the filename prefix so initiatives support temporal
discovery and future retention or cleanup decisions.

## Milestone Boundary

Initiative milestones are outcome checkpoints for a strategic result.

They are not constitutional roadmap commitments, plan sequencing details, or
ticket progress logs. Use them to show whether the broader outcome is advancing,
then let plans own execution order and tickets own live state.

## Use This Skill When

- several tickets or plans are really serving one bigger outcome
- the work needs durable success metrics
- a strategic objective needs a long-lived home
- the project would otherwise accumulate related tickets with no clear higher owner

## Do Not Use This Skill When

- the work is already ticket-sized
- you only need execution sequencing, not strategic framing
- you are merely recording research or behavior contract detail

## Good Initiative Questions

A strong initiative answers:

- what outcome is being pursued
- why now
- how success will be recognized
- which stable `OBJ-*` criteria downstream work may cite
- what milestones matter
- which plans, specs, research, and tickets execute it

## Done Means

- the strategic outcome is explicit
- downstream work is visible
- a future agent would know why this work exists as a coordinated effort

## Read In This Order

Read immediately when the strategic outcome needs an initiative owner:

1. `references/initiative-shape.md` when deciding what belongs in the
   initiative and how success should be framed.
2. `templates/initiative.md` only when creating or substantially reshaping an
   initiative record.
