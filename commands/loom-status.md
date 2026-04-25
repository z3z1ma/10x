---
name: loom-status
description: "Produce a current-state Loom snapshot: active queues, blockers, review backlog, acceptance backlog, and the most sensible next move."
arguments: "<topic | path | initiative | ticket | blank for broad status>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-tickets
  - loom-critique
  - loom-wiki
---

# /loom-status

You are running **Loom Status**.

Focus:
`$ARGUMENTS`

This command is the explicit state-synthesis surface.
It should tell the operator what is live, what is stuck, what is waiting for review or acceptance, and what Loom believes the next bounded move should be.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-tickets`
- `loom-critique`
- `loom-wiki`

## Goals

- summarize the current execution graph truthfully
- surface the ready queue and the blocked queue
- notice review and wiki follow-through debt
- notice lifecycle and claim-coverage drift
- identify contradictions or suspicious state drift
- recommend the next explicit command

## Canonical Procedure

Hydrate `loom-workspace` and use its `status-snapshot` reference as the procedure.

In short:

1. orient quickly
2. collect the ticket ledger
3. collect nearby owner records
4. check for state drift
5. summarize queues
6. recommend the next move

## Native tools to prefer

- `rg -n '^status:' .loom/tickets --glob '*.md'`
- `rg -n '^status:' .loom/{constitution,initiatives,research,specs,plans,critique,wiki,evidence,packets} --glob '*.md'`
- `rg -n '[a-z]+:[a-z0-9-]+#(REQ|ACC|CLAIM)-[0-9]{3}' .loom --glob '*.md'`
- `rg -n '^(id|status|review_target):' .loom/{plans,tickets,critique,wiki} --glob '*.md'`
- `find .loom/{tickets,critique,wiki,evidence} -type f -name '*.md' | sort`
- `git status --short`
- `git diff --stat -- .loom`

## Guardrails

- Do not mutate records by default.
- Report contradictions explicitly instead of smoothing them over.
- Do not treat recency alone as truth; respect owner layers.
- Keep the summary compact but concrete.

## Required output

- status snapshot
- active, blocked, review, and acceptance queues
- contradictions or stale state worth fixing
- best next command and why
