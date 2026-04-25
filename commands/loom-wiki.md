---
name: loom-wiki
description: "Write or audit the Loom Wiki. Write mode promotes accepted owner truth into durable explanation. Audit mode walks the wiki for staleness, broken sources, duplication, and misplaced authority."
arguments: "[audit] <topic | page slug | ticket | workflow | concept>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
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
- `loom-evidence`
- `loom-wiki`
- `loom-critique`
- `loom-research`
- `loom-specs`

## Mode selection

- if `$ARGUMENTS` begins with `audit`, run **Audit mode** against the remaining text as the scope (blank = whole wiki)
- otherwise run **Write mode** against `$ARGUMENTS` as the page target

## Write mode

Produce or update one targeted wiki page from accepted owner truth.

Hydrate `loom-wiki` and use its `wiki-write` reference as the canonical write
procedure.

## Audit mode

Walk the wiki (or the named scope) and surface maintenance debt without silently rewriting it.

Hydrate `loom-wiki` and use its `wiki-audit` reference as the canonical audit
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
- recommended next route, owner layer, or optional command per finding

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
- In audit mode, do not perform substantive rewrites. Apply only obvious
  mechanical link or stale-marker fixes; route substantive changes to write mode.
- In audit mode, do not silently delete pages; mark stale or superseded with forward links.
