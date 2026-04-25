---
name: loom-debug
description: "Run a reproduce-first Loom debug workflow that routes reproduction, root cause, fix evidence, critique, and prevention into existing owner layers."
arguments: "<bug report | failing behavior | incident>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-debugging
  - loom-research
  - loom-specs
  - loom-tickets
  - loom-ralph
  - loom-critique
---

# /loom-debug

You are running **Loom Debug**.

Debug target:
`$ARGUMENTS`

Debugging follows:

`reproduce -> localize -> explain -> fix -> evidence -> prevent`

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-debugging`
- `loom-research`
- `loom-specs`
- `loom-tickets`
- `loom-ralph`
- `loom-critique`

## Goals

- reproduce or explicitly fail to reproduce the behavior
- preserve root-cause investigation
- clarify intended behavior when needed
- create a bounded fix ticket
- support the fix with evidence
- route prevention into retrospective when warranted

## Canonical Procedure

Hydrate `loom-debugging` and use its procedure.

In short:

1. reproduce
2. localize
3. explain root cause or preserve uncertainty
4. create or tighten the fix ticket
5. record before and after behavior evidence
6. route to critique and retrospective when warranted

## Guardrails

- Do not skip reproduction unless you explicitly record why it is impossible.
- Do not treat the fix as supported without evidence.
- Do not hide root-cause uncertainty in ticket prose.
- Do not close the ticket from this command.

## Required Output

- reproduction evidence or reproduction blocker
- root-cause status
- records created or updated
- fix ticket and packet, if created
- evidence gathered or still missing
- recommended next route, owner layer, or optional command
