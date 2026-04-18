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
- gather and synthesize evidence
- leave behind a reusable research note
- make downstream implications visible without smuggling owner truth into the wrong layer

## Procedure

1. **Anchor the question.**
   - Determine what decision, uncertainty, or tradeoff `$ARGUMENTS` refers to.
   - Link the research to any relevant initiative, plan, spec, or ticket.

2. **Read what already exists.**
   - Search for prior research, accepted wiki pages, specs, ticket journals, and evidence records.
   - Reuse prior investigation where it remains valid.

3. **Gather evidence.**
   - Use repository evidence, experiments, or external sources as appropriate.
   - If the question depends on current outside facts and the harness can browse, gather and cite those sources.
   - Keep raw evidence separate from your conclusions.

4. **Write the research record.**
   - Capture:
     - question
     - why it matters
     - method
     - evidence
     - conclusions
     - recommendation
     - uncertainty
   - Make the conclusions proportional to the evidence.

5. **Route the result to the right downstream owner.**
   - If the work clarified behavior, recommend or update a spec.
   - If it changed sequencing, recommend or update a plan.
   - If it only produced accepted explanation, recommend or update a wiki page.
   - If it materially changes durable project direction, escalate to initiative or constitution.

## Native tools to prefer

- `rg -n '<term>' .loom/{research,specs,plans,tickets,wiki,evidence} --glob '*.md'`
- `find .loom/{research,evidence,wiki} -type f -name '*.md' | sort`
- `git grep -n '<term>'`
- inline Python only when it is materially clearer than shell for local synthesis

## Guardrails

- Do not present speculation as settled evidence.
- Do not let research become the behavior contract if a spec should own that truth.
- Do not bury the downstream recommendation.

## Required output

- research summary
- research record path and ID
- key conclusions and confidence
- downstream implications
- recommended next command
