---
name: loom-retrospective
description: "Run the Loom retrospective pass: assimilate what was learned during a ticket, initiative, or recent work slice into existing owner layers without creating a new ledger."
arguments: "<ticket id | topic | initiative | recent work slice>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-retrospective
  - loom-evidence
  - loom-wiki
  - loom-memory
  - loom-research
  - loom-specs
  - loom-plans
  - loom-initiatives
  - loom-constitution
  - loom-critique
  - loom-tickets
---

# /loom-retrospective

You are running **Loom Retrospective**.

Retrospective target:
`$ARGUMENTS`

A retrospective is how Loom compounds. It is the named pass that takes what was actually learned during recent work and promotes it into the owner layers that will carry it forward.

Retrospective is not a new record kind. It produces no `.loom/retrospectives/` directory. It is a workflow over the existing owner layers: wiki, research, spec, plan, initiative, constitution, evidence, and sparingly memory.

The loop is:

**observe → distill → promote → prevent**

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-retrospective`
- `loom-evidence`
- `loom-wiki`
- `loom-memory`
- `loom-research`
- `loom-specs`
- `loom-plans`
- `loom-initiatives`
- `loom-constitution`
- `loom-critique`
- `loom-tickets`

## Goals

- harvest durable learning from recent work
- separate stable knowledge from transient execution residue
- promote that knowledge into the correct Loom owner layers
- leave the corpus easier for the next agent to reuse
- propose constitutional amendments when the project's principles or constraints shifted
- prevent repeated mistakes by promoting them into exactly one owner artifact

## When to run a retrospective

- on ticket close, especially for non-trivial tickets
- on initiative close
- after a release, a migration, or a rollout
- after a critique that surfaced stable lessons
- when the same question has been answered from transcript context more than once

## The retrospective loop

### 1. Observe

Gather the concrete signals around `$ARGUMENTS`:

- ticket journals
- recent packets
- critiques and findings
- evidence records
- changed specs, plans, or research
- recurring questions or explanations the agent kept having to reconstruct

### 2. Distill

Ask what kind of learning actually emerged, and which owner layer carries that kind of truth:

- accepted explanation or workflow → **wiki**
- durable investigation result, rejected option, or null result → **research**
- clarified intended behavior → **spec**
- changed sequencing or rollout logic → **plan**
- changed strategic outcome framing → **initiative**
- changed durable project policy or principles → **constitution** (including a new decision record if the change is a citable choice)
- observed proof artifact, challenged observation, or validation artifact → **evidence**
- missing proof that still needs work → **ticket follow-up or test expectation**
- support-only continuity or reminders → **memory**

### 3. Promote

Update the right owner layer. Add links so future retrieval is cheap. Remove or prune duplicate support notes that now shadow canonical truth.

Retrospective is the concrete trigger for:

- promoting accepted explanations into wiki pages
- capturing rejected options and null results in research
- proposing constitution amendments or decision records when policy shifted
- trimming memory entries that canonical records now cover

### 4. Prevent

For each repeated mistake, choose exactly one prevention artifact:

| Repeated mistake | Prevention artifact |
| --- | --- |
| behavior ambiguity | spec |
| missed test case or proof gap | evidence when observed, or ticket/test expectation when future work |
| bad architectural choice | constitution decision |
| recurring operator confusion | wiki workflow or reference page |
| repeated implementation pitfall | research null result or wiki troubleshooting |
| repeated project-local technique | project-local skill |
| support-only reminder | memory |

If no repeated mistake exists, say so and avoid creating filler artifacts.

## Canonical Procedure

Use `skills/loom-retrospective/SKILL.md` as the procedure.

In short:

1. observe the source slice
2. distill durable learning
3. promote into the right owners
4. choose exactly one prevention artifact per repeated mistake
5. recommend the next owner

## Native tools to prefer

- `git diff --stat`
- `git log --oneline --decorate -n 10`
- `find .loom/{tickets,critique,wiki,research,specs,plans,evidence,packets} -type f -name '*.md' | sort`
- `rg -n '<term>' .loom/{tickets,critique,wiki,research,specs,plans,evidence,memory} --glob '*.md'`

## Guardrails

- Do not create a shadow learning ledger. Retrospective assimilates into existing owner layers.
- Do not promote unsettled claims into the wiki.
- Do not let memory become a secret second project ledger.
- A retrospective that produces no promotions is honest if there was nothing durable to promote; do not invent artifacts to look busy.
- Retrospective does not close a ticket by itself — acceptance still decides.

## Required output

- retrospective summary
- records or pages created or updated, with paths and IDs
- what learning was promoted, and into which layer
- memory changes, if any
- residual gaps or questions not yet ready to promote
- recommended next command
