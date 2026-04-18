---
name: loom-compound
description: "Run the explicit Loom compound-learning pass: observe recent work, distill stable lessons, and promote them into the proper owner layers, especially the wiki."
arguments: "<ticket id | topic | initiative | recent work slice>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
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

# /loom-compound

You are running **Loom Compound**.

Learning target:
`$ARGUMENTS`

This command makes the compounding behavior explicit.

The old intuition still applies:
**observe -> distill -> evolve**.

But in Markdown-native Loom, that loop does **not** create a second shadow ontology of “instinct” artifacts.
Instead, it promotes stable learning into the owner layers that already exist.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
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

- harvest useful learning from recent work
- separate stable knowledge from transient execution residue
- promote that knowledge into the correct Loom owner layers
- leave the corpus easier for the next agent to reuse

## The compound loop

### 1. Observe

Gather the concrete signals around `$ARGUMENTS`:
- ticket journals
- recent packets
- critiques and findings
- evidence records
- changed specs, plans, or research
- repeated questions or explanations that kept surfacing

### 2. Distill

Ask what kind of learning actually emerged:
- accepted explanation or workflow -> **wiki**
- durable investigation result -> **research**
- clarified intended behavior -> **spec**
- changed sequencing or rollout logic -> **plan**
- changed strategic outcome framing -> **initiative**
- changed durable project policy or principles -> **constitution**
- support-only continuity or reminders -> **memory**

### 3. Promote

Update the right owner layer.
Add links so future retrieval is cheap.
Remove or prune duplicate support notes if they are now shadowing canonical truth.

## Procedure

1. **Anchor the source slice.**
   - Identify the governing ticket, initiative, or topic.
   - Read the most relevant critiques, packets, evidence, and wiki pages.

2. **Find repeated or stable learning.**
   - Look for answers the agent had to rediscover.
   - Look for lessons that changed how future work should be done.
   - Look for explanations that future agents would otherwise have to reconstruct.

3. **Promote into the right owners.**
   - Prefer the wiki for accepted explanation.
   - Use research, spec, plan, initiative, or constitution only if that layer truly owns the new truth.
   - Use memory sparingly for support continuity, not for canonical facts.

4. **Link and prune.**
   - Link originating tickets, critiques, wiki pages, research notes, and specs.
   - If memory now duplicates canonical truth, replace or trim the duplicate.
   - If the wiki page already exists, improve it rather than forking another one.

5. **Recommend the next move.**
   - `/loom-accept` if closure is the remaining question.
   - `/loom-wiki` if more targeted page work is still needed.
   - `/loom-plan` if the learning materially changed the route forward.

## Native tools to prefer

- `git diff --stat`
- `git log --oneline --decorate -n 10`
- `find .loom/{tickets,critique,wiki,research,specs,plans,evidence,packets} -type f -name '*.md' | sort`
- `rg -n '<term>' .loom/{tickets,critique,wiki,research,specs,plans,evidence,memory} --glob '*.md'`

## Guardrails

- Do not create a shadow learning ledger when an existing owner layer can carry the truth.
- Do not promote unsettled claims into the wiki.
- Do not let memory become a secret second project ledger.
- Compounding is about durable learning, not decorative documentation.

## Required output

- compound summary
- records or pages created or updated
- what learning was promoted, and where
- memory changes, if any
- remaining gaps or next command
