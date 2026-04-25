---
name: loom-orient
description: "Enter a Loom workspace safely: establish structural trust, read constitution first, recover the governing artifact chain, and route to the correct next command."
arguments: "<path | record id | task | blank for broad orientation>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
---

# /loom-orient

You are running **Loom Orient**.

Target or request:
`$ARGUMENTS`

This command is the explicit cold-start and rerouting surface.
Use it when you are entering a repository, the owning layer is unclear, or the operator wants to know what Loom thinks should happen next.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`

## Goals

- confirm the workspace root
- establish structural trust in `.loom/`
- read `constitution:main` before downstream interpretation
- recover the most relevant owner chain for `$ARGUMENTS`
- decide whether the next move is outer-loop work, Ralph execution, critique, wiki work, or acceptance

## Canonical Procedure

Hydrate `loom-workspace` and use its `routing` reference as the procedure.

In short:

1. confirm root and scope
2. inspect Loom structure
3. read `constitution:main`
4. find the relevant owner chain
5. assess execution state
6. route explicitly

## Native tools to prefer

- `git rev-parse --show-toplevel`
- `find .loom -maxdepth 2 -type d | sort`
- `rg -n '^(id|status):|review_target:|page_type:' .loom --glob '*.md'`
- `rg -n '<term>' .loom --glob '*.md'`
- `git status --short`
- `git diff --stat`

## Guardrails

- Do not start implementation from this command.
- Do not trust downstream records before checking Loom structure.
- Do not guess the owner layer when the graph can tell you.
- By default this command is read-mostly; only bootstrap or repair structure when that is clearly the operator's intent.

## Required output

- workspace root and structural-trust assessment
- most relevant records found
- current owner layer and execution state
- the recommended next route, owner layer, or optional command, with reasoning
- any blockers or missing Loom structure
