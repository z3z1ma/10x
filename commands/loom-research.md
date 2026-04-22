---
name: loom-research
description: "Create or refine a durable investigation when evidence, comparison, or discovery is needed before commitment."
arguments: "<question | tradeoff | topic | decision>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-research
  - loom-initiatives
  - loom-plans
  - loom-specs
  - loom-wiki
---

# /loom-research

You are running **Loom Research**.

Research question or topic:
`$ARGUMENTS`

This command creates durable discovery.
Use it when the project needs evidence before committing to a behavior, strategy, or implementation path.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-research`
- `loom-initiatives`
- `loom-plans`
- `loom-specs`
- `loom-wiki`

## Goals

- frame the investigation clearly
- recall prior evidence before inventing new investigation
- gather and synthesize evidence, separating it from inference
- capture rejected options and null results so future agents inherit the dead ends
- route the result to the correct downstream owner

## Canonical Procedure

Use `skills/loom-research/SKILL.md` and
`skills/loom-research/references/research-shape.md` as the procedure.

In short:

1. anchor the question
2. read prior evidence
3. gather and separate evidence from inference
4. write the research record
5. route the result to its downstream owner

## Native tools to prefer

- `rg -n '<term>' .loom/{research,specs,plans,tickets,wiki,evidence} --glob '*.md'`
- `find .loom/{research,evidence,wiki} -type f -name '*.md' | sort`
- `git grep -n '<term>'`
- inline Python only when it is materially clearer than shell for local synthesis

## Guardrails

- Do not present speculation as settled evidence.
- Do not let research become the behavior contract if a spec should own that truth.
- Do not bury the downstream recommendation.
- Do not discard rejected options or null results; they are durable.

## Required output

- research record path and ID
- key conclusions and confidence
- rejected options or null results captured, if any
- downstream implications
- recommended next command
