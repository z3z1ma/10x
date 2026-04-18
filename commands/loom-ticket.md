---
name: loom-ticket
description: "Create, split, tighten, relink, or update a bounded execution ledger entry without doing the implementation itself."
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
Use it when the operator already knows the work belongs in the execution ledger and wants the ticket itself created, sharpened, split, relinked, or truthfully updated.

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
- avoid performing the implementation itself

## Procedure

1. **Locate or decide the ticket.**
   - If `$ARGUMENTS` names an existing ticket, open that ticket first.
   - If `$ARGUMENTS` is prose, find the governing plan or initiative and decide whether a new ticket or sibling ticket is needed.

2. **Read the governing chain.**
   - Read the linked plan, and any relevant spec or research.
   - Pull in only the upstream context that matters for execution readiness.

3. **Create or refine the ticket.**
   - Use the ticket template and naming guidance.
   - Tighten:
     - `Summary`
     - `Scope`
     - `Non-goals`
     - `Acceptance Criteria`
     - `Evidence`
     - `Critique Disposition`
     - `Wiki Disposition`
   - Add `depends_on` only when a true hard prerequisite exists.

4. **Split if the ticket is too large.**
   - If several independent slices are hiding inside one ticket, split them.
   - Keep the current ticket as the next bounded slice or convert it into the right parent/sibling relationship through links.

5. **Set the truthful status.**
   - `proposed` if it still needs outer-loop work.
   - `ready` if a fresh worker could start honestly.
   - `active` only if work is genuinely underway.
   - `blocked` only if a named blocker exists.

6. **Recommend the next step.**
   - `/loom-work <ticket-id>` when ready.
   - `/loom-plan ...` if the ticket revealed missing outer-loop structure.
   - `/loom-spec ...` or `/loom-research ...` if the ticket exposed missing contract or evidence.

## Native tools to prefer

- `rg -n 'ticket:[a-z0-9]+' .loom --glob '*.md'`
- `rg -n '^(id|status|depends_on):' .loom/tickets --glob '*.md'`
- `rg -n '<term>' .loom/{plans,specs,research,tickets} --glob '*.md'`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not start implementation here.
- Do not let the ticket redefine plan strategy or spec behavior unless you are also updating the owner record.
- Do not call a ticket `ready` if a fresh worker would still need chat history to begin.

## Required output

- ticket(s) created or updated, with paths and IDs
- readiness assessment
- dependencies and links added or changed
- recommended next command
