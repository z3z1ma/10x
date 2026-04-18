---
name: loom-wiki
description: "Create or update a targeted Loom Wiki page from accepted truth so the explanation compounds instead of vanishing into chat."
arguments: "<topic | page slug | ticket | workflow | concept>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-wiki
  - loom-critique
  - loom-research
  - loom-specs
---

# /loom-wiki

You are running **Loom Wiki**.

Page target or topic:
`$ARGUMENTS`

This command is the direct knowledge-promotion surface.
Use it when the operator explicitly wants a wiki page, or when the right next move is accepted explanation rather than more execution.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-wiki`
- `loom-critique`
- `loom-research`
- `loom-specs`

## Goals

- promote accepted understanding into a durable page
- choose the right wiki page family
- ground the page in accepted records and evidence
- improve future retrieval and reuse

## Procedure

1. **Anchor the page.**
   - Decide whether `$ARGUMENTS` points at a concept page, workflow page, or reference page.
   - Find existing pages first; prefer updating the right page over creating duplicates.

2. **Gather accepted sources.**
   - Read the canonical owners and evidence that ground the page.
   - Use critique and research where they sharpen the explanation.
   - Do not source the wiki from unsettled chat residue.

3. **Decide whether a wiki packet is warranted.**
   - If synthesis is non-trivial or the source set is wide, compile a wiki packet under `.loom/packets/wiki/`.
   - Otherwise write directly with the accepted source set in view.

4. **Write or update the page.**
   - Choose the proper page family.
   - Explain clearly, link related pages, and cite the source records or evidence.
   - Make the page genuinely reusable by a future agent.

5. **Reconnect the graph.**
   - Add or update links from the originating ticket, critique, or plan when helpful.
   - If the new page reveals a recurring concept page or neighboring reference page that should exist, note it.

6. **Check truth boundaries.**
   - If the page starts carrying behavior contract or policy authority, move that truth back into spec or constitution and make the wiki refer to it.

## Native tools to prefer

- `find .loom/wiki -type f -name '*.md' | sort`
- `rg -n '<term>' .loom/{wiki,research,specs,plans,tickets,critique,evidence} --glob '*.md'`
- `find .loom/packets/wiki -type f -name '*.md' | sort | tail`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not promote unsettled claims into the wiki.
- Do not let the wiki quietly become the spec or the constitution.
- Avoid transcript residue; write durable explanation instead.

## Required output

- pages created or updated, with paths and IDs
- key claims promoted
- accepted sources used
- related pages or follow-up knowledge gaps
- recommended next command
