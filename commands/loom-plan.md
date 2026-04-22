---
name: loom-plan
description: "Turn a raw request into governed Loom work by creating or updating the minimal correct outer-loop chain: initiative, research/spec when needed, plan, and ready tickets."
arguments: "<idea | problem | request | outcome>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-initiatives
  - loom-research
  - loom-specs
  - loom-plans
  - loom-tickets
  - loom-memory
  - loom-wiki
---

# /loom-plan

You are running **Loom Plan**.

Request:
`$ARGUMENTS`

This command is the explicit outer-loop shaping surface.
Read before inventing, create only the layers that actually need to exist, and leave behind a plan and ticket set that a fresh worker could honestly execute.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-initiatives`
- `loom-research`
- `loom-specs`
- `loom-plans`
- `loom-tickets`
- `loom-memory`
- `loom-wiki`

## Goals

- recover relevant prior knowledge before creating new records
- choose the minimal correct owner chain
- create or update a durable plan
- slice the work into bounded, dependency-aware tickets
- stop before implementation

## Canonical Procedure

Use `skills/loom-plans/SKILL.md`, `skills/loom-plans/references/plan-shape.md`,
and `skills/loom-tickets/references/readiness.md` as the procedure.

In short:

1. orient and recall prior knowledge
2. choose the minimal owner chain
3. write or refine owner records
4. slice into bounded tickets
5. check readiness
6. recommend the next owner

## Native tools to prefer

- `find .loom -maxdepth 2 -type d | sort`
- `rg -n '<term>' .loom/{initiatives,research,specs,plans,tickets,wiki,memory} --glob '*.md'`
- `rg -n '^(id|status|links):' .loom/{initiatives,research,specs,plans,tickets} --glob '*.md'`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`
- `git status --short`
- `git diff --stat`

## Guardrails

- Do not implement product code in this command.
- Do not create empty ceremony layers.
- Do not leave live progress in the plan.
- Do not widen scope because a nearby improvement looks tempting.

## Required output

- concise planning summary
- records created or updated, with paths and IDs
- ticket list with status and dependencies
- unresolved questions, risks, or assumptions
- recommended next command
