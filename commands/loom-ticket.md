---
name: loom-ticket
description: "Create, split, tighten, relink, or truthfully update one bounded execution ledger entry without doing the implementation."
arguments: "<ticket id | plan slice | execution request>"
category: support
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-tickets
  - loom-plans
  - loom-specs
  - loom-research
---

# /loom-ticket

You are running **Loom Ticket**.

Ticket target or request:
`$ARGUMENTS`

This command is for direct ticket work.
Use it when the work clearly belongs in the execution ledger and the ticket itself should be created, sharpened, split, relinked, or truthfully updated.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-tickets`
- `loom-plans`
- `loom-specs`
- `loom-research`

## Goals

- ensure the work has one truthful ticket owner
- keep the ticket bounded and ready for Ralph
- correct links, dependencies, acceptance criteria, and status
- stop before implementation

## Canonical Procedure

Use `skills/loom-tickets/SKILL.md`,
`skills/loom-tickets/references/readiness.md`, and
`skills/loom-records/references/claim-coverage.md` as the procedure.

In short:

1. locate or decide the ticket
2. read the governing chain
3. tighten, split, or relink
4. set truthful status
5. recommend the next owner

## Native tools to prefer

- `rg -n 'ticket:[a-z0-9]+' .loom --glob '*.md'`
- `rg -n '^(id|status|depends_on):' .loom/tickets --glob '*.md'`
- `rg -n '<term>' .loom/{plans,specs,research,tickets} --glob '*.md'`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not start implementation from this command.
- Do not let the ticket redefine plan strategy or spec behavior. If the owner chain is wrong, fix the owner record.
- Do not call a ticket `ready` on faith.

## Required output

- ticket(s) created or updated, with paths and IDs
- readiness assessment
- dependencies and links added or changed
- recommended next command
