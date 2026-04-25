---
name: loom-accept
description: "Invoke the ticket-owned acceptance gate for a ticket or change target: verify evidence and follow-through, then record the honest ticket state or concrete gaps."
arguments: "<ticket id | change target>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-tickets
  - loom-critique
  - loom-wiki
  - loom-specs
  - loom-research
---

# /loom-accept

You are running **Loom Accept**.

Acceptance target:
`$ARGUMENTS`

This command is an invocation adapter over the ticket acceptance gate.
It exists because `closed` is not a vibe; the governed decision belongs in the
ticket.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-tickets`
- `loom-critique`
- `loom-wiki`
- `loom-specs`
- `loom-research`

## Goals

- compare the claimed outcome against the actual acceptance contract
- verify evidence, critique disposition, and wiki disposition
- record `closed` only when the ticket acceptance gate says the durable story is truthful
- otherwise leave a precise and actionable non-closure state

## Canonical Procedure

Use `skills/loom-tickets/references/acceptance-gate.md` as the procedure.

In short:

1. anchor the ticket
2. read the acceptance dossier
3. test evidence, coverage, claim matrix, critique, and wiki disposition
4. choose the honest ticket state
5. record the decision in the ticket journal

## Native tools to prefer

- `rg -n '^(id|status|depends_on):' .loom/tickets --glob '*.md'`
- `rg -n '<ticket-id>|<target>' .loom/{critique,wiki,evidence,specs,research,plans,packets} --glob '*.md'`
- `git status --short`
- `git diff --stat`

## Guardrails

- Fail closed.
- Do not close a ticket because the coding feels done.
- Do not ignore unresolved critique findings.
- Do not let acceptance live only in chat.

## Required output

- acceptance verdict
- ticket status after the decision
- evidence and critique basis for that decision
- follow-up tickets or gaps if not closed
- recommended next owner or command
