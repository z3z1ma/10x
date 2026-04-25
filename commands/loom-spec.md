---
name: loom-spec
description: "Create or sharpen a durable behavior contract when intended behavior, constraints, or acceptance criteria are still too fuzzy for honest execution."
arguments: "<capability | workflow | ticket | behavior>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-specs
  - loom-research
  - loom-plans
  - loom-tickets
  - loom-critique
---

# /loom-spec

You are running **Loom Spec**.

Target behavior or scope:
`$ARGUMENTS`

This command is the explicit behavior-contract surface.
Use it when the project needs one stable statement of intended behavior before execution or critique can stay honest.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-specs`
- `loom-research`
- `loom-plans`
- `loom-tickets`
- `loom-critique`

## Goals

- define what the system should do, separate from how
- ground the contract in evidence, not wishful behavior
- make acceptance criteria and scenarios durable
- reconcile downstream tickets and critique with one contract

## Canonical Procedure

Hydrate `loom-specs` and use its `spec-shape` reference as the procedure.

In short:

1. anchor the spec
2. read evidence and constraints
3. write or refine behavior and acceptance
4. reconcile downstream artifacts
5. recommend the next route or owner layer

## Native tools to prefer

- `rg -n '<term>' .loom/{research,specs,plans,tickets,critique,wiki} --glob '*.md'`
- `git grep -n '<behavior term>'`
- `git diff --stat`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not let the ticket or wiki quietly become the spec.
- Do not encode wishful behavior that evidence or constitution contradicts.
- Do not overfit the contract to one incidental implementation.

## Required output

- spec record path and ID
- key behaviors, constraints, and acceptance expectations
- downstream artifacts updated or needing reconciliation
- recommended next route, owner layer, or optional command
