---
name: loom-decide
description: "Make a citable architectural or policy choice and leave a durable decision record with rejected alternatives, grounded evidence, and explicit consequences."
arguments: "<choice | tradeoff | architectural question | policy question>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-constitution
  - loom-research
  - loom-wiki
---

# /loom-decide

You are running **Loom Decide**.

Decision target:
`$ARGUMENTS`

This command is the explicit architectural decision surface.
Use it when a choice should outlive the current ticket or plan, when future agents should be able to cite the reasoning as precedent, or when a choice contradicts or amends existing constitution.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-constitution`
- `loom-research`
- `loom-wiki`

## When to use this command

- the choice should outlive the current ticket or plan
- future agents should be able to cite the reasoning as precedent
- several plausible options exist and the tradeoff matters
- the choice contradicts or amends existing constitution

If the choice is a ticket-sized implementation preference with no durable consequences, let the ticket carry it. If the question is still exploratory, route to `/loom-brainstorm`. If the evidence is thin, route to `/loom-research` before deciding.

## Goals

- check precedent before adding more
- frame one clear choice, with at least two options
- ground each option in evidence
- record rejected alternatives honestly
- state consequences and revisit conditions
- reconcile downstream records that the decision affects

## Canonical Procedure

Use `skills/loom-constitution/SKILL.md` and the decision template as the
procedure.

In short:

1. check constitutional precedent
2. frame the choice
3. enumerate options
4. gather evidence
5. record rejected alternatives
6. write the decision record
7. reconcile downstream records

## Native tools to prefer

- `ls .loom/constitution/decisions/ | sort`
- `rg -n '<topic>' .loom/constitution`
- `rg -n '<topic>' .loom/{research,wiki,specs,plans}`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not skip rejected alternatives.
- Do not ratify a fait accompli silently; if the choice is already shipped, write the record as retrospective ADR and say so.
- Do not let the decision record turn into a plan; it captures a choice, not a sequence.
- Do not decide from weak evidence; route to `/loom-research` first.
- Do not silently contradict existing constitutional truth; amend or supersede explicitly.

## Required output

- decision record path and ID
- the choice, in one or two sentences
- options considered, with rejected alternatives and reasons
- evidence and precedent cited
- consequences and revisit conditions
- downstream records that now need reconciliation
- recommended next command
