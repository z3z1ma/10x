---
name: loom-wiki
description: "Write or audit the Loom Wiki. Write mode promotes accepted truth into a durable page. Audit mode walks the wiki for staleness, broken sources, duplication, and misplaced authority."
arguments: "[audit] <topic | page slug | ticket | workflow | concept>"
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

Argument:
`$ARGUMENTS`

This command has two modes.

- **Write mode** promotes accepted understanding into a durable page. It is the default.
- **Audit mode** walks the wiki and surfaces maintenance debt without silently rewriting it. It is triggered when `$ARGUMENTS` begins with `audit` (case-insensitive).

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-wiki`
- `loom-critique`
- `loom-research`
- `loom-specs`

## Mode selection

- if `$ARGUMENTS` begins with `audit`, run **Audit mode** against the remaining text as the scope (blank = whole wiki)
- otherwise run **Write mode** against `$ARGUMENTS` as the page target

## Write mode

Produce or update one targeted wiki page from accepted truth.

### Goals

- promote accepted understanding into a durable page
- ground the page in accepted records and evidence
- prefer improving an existing page over forking a new one
- refuse policy or behavior-contract drift into the wiki

### Procedure

1. **Anchor the page.**
   - Decide whether `$ARGUMENTS` points at a concept, workflow, or reference page.
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
   - If a neighboring page should exist, note it.

6. **Check truth boundaries.**
   - If the page starts carrying behavior contract or policy authority, move that truth back into spec or constitution and make the wiki refer to it.

### Write-mode required output

- pages created or updated, with paths and IDs
- key claims promoted
- accepted sources used
- related pages or follow-up knowledge gaps
- recommended next command

## Audit mode

Walk the wiki (or the named scope) and surface maintenance debt without silently rewriting it.

Use `skills/loom-wiki/references/wiki-audit.md` as the canonical audit
procedure.

In short:

1. walk the page scope
2. compare claims to accepted sources
3. classify findings
4. apply only low-risk mechanical fixes
5. route substantive rewrites to the owning workflow

### Audit-mode required output

- pages scanned
- findings table (page → classification → evidence → proposed action)
- low-risk mechanical fixes applied, if any
- recommended next command per finding

## Native tools to prefer

- `find .loom/wiki -type f -name '*.md' | sort`
- `rg -n '<term>' .loom/{wiki,research,specs,plans,tickets,critique,evidence} --glob '*.md'`
- `rg -n '^(id|status|page_type):' .loom/wiki --glob '*.md'`
- `find .loom/packets/wiki -type f -name '*.md' | sort | tail`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not promote unsettled claims into the wiki.
- Do not let the wiki quietly become the spec or the constitution.
- Avoid transcript residue; write durable explanation instead.
- In audit mode, do not rewrite pages — propose, then let write mode do the work.
- In audit mode, do not silently delete pages; mark stale or superseded with forward links.
