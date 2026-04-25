---
name: loom-spike
description: "Run a bounded Loom spike as a research variant with experiment matrix, throwaway scope, evidence, conclusions, null results, and downstream route."
arguments: "<question | experiment | uncertainty>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-spike
  - loom-research
  - loom-wiki
  - loom-specs
---

# /loom-spike

You are running **Loom Spike**.

Spike question:
`$ARGUMENTS`

The spike route is:

`question -> experiment matrix -> bounded throwaway child write scope -> evidence -> conclusions/null results -> downstream route`

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-spike`
- `loom-research`
- `loom-wiki`
- `loom-specs`

## Goals

- answer a bounded technical or product question
- keep throwaway work clearly scoped
- preserve evidence, rejected paths, and null results
- route accepted conclusions to the right owner layer

## Canonical Procedure

Use `skills/loom-spike/SKILL.md` as the procedure.

In short:

1. frame the question
2. search prior research and evidence
3. define the experiment matrix and throwaway child write scope
4. capture evidence and null results
5. route conclusions to the owning layer

## Guardrails

- Do not let throwaway code become production by accident.
- Do not overstate weak evidence.
- Do not skip null results; they are often the most reusable output.

## Required Output

- research record path and ID
- evidence records or artifacts
- conclusion and confidence
- null results or rejected paths
- downstream owner recommendation
