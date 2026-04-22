---
name: loom-sketch
description: "Run a bounded Loom sketch workflow for UI or product variants, evidence artifacts, critique, and accepted spec/wiki updates."
arguments: "<design question | interface | product variant>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-spike
  - loom-research
  - loom-critique
  - loom-wiki
  - loom-specs
---

# /loom-sketch

You are running **Loom Sketch**.

Sketch target:
`$ARGUMENTS`

Sketch is a product or UI research variant:

`design question -> 2-3 variants -> artifacts -> critique -> accepted wiki/spec updates`

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-spike`
- `loom-research`
- `loom-critique`
- `loom-wiki`
- `loom-specs`

## Goals

- explore a small set of concrete variants
- preserve artifacts and screenshots as evidence when useful
- critique the variants before acceptance
- route accepted behavior to specs and accepted explanation to wiki

## Canonical Procedure

Use `skills/loom-spike/SKILL.md` as the procedure. Sketch is the design
variant of the spike workflow.

In short:

1. frame the design question
2. produce a small set of variants
3. capture artifacts as evidence
4. critique variants before acceptance
5. route accepted behavior to specs and accepted explanation to wiki

## Guardrails

- Do not let visual preference masquerade as accepted behavior.
- Do not promote a sketch into wiki without evidence and critique.
- Do not create a new design layer.

## Required Output

- variants explored
- evidence artifacts
- critique result
- accepted behavior or explanation, if any
- downstream owner recommendation
