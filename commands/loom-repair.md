---
name: loom-repair
description: "Fix graph drift across the Loom workspace: broken references, stale supersessions, status-vs-journal mismatches, orphan packets, owner-layer conflicts, and structural record failures. Apply safe repairs, route the rest."
arguments: "<scope path | record id | blank for whole workspace>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-evidence
  - loom-tickets
  - loom-constitution
  - loom-specs
  - loom-wiki
  - loom-critique
---

# /loom-repair

You are running **Loom Repair**.

Repair scope:
`$ARGUMENTS`

This command is the explicit graph-hygiene surface.
Use it when `/loom-status` has surfaced drift that nothing has fixed, when a scan should walk the tree periodically, or when a specific record or path needs reference reconciliation.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-evidence`
- `loom-tickets`
- `loom-constitution`
- `loom-specs`
- `loom-wiki`
- `loom-critique`

## Scope

- if `$ARGUMENTS` is blank, scan the whole `.loom/` tree
- if `$ARGUMENTS` names a path or record ID, narrow the scan to that slice and its immediate links

Narrow scans are preferred for routine hygiene. Whole-workspace scans are for periodic passes.

## Goals

- classify drift per class with inspectable evidence
- apply only the repairs that are genuinely safe
- route everything else to the right owner skill
- leave the repair trail visible, not silent

## Canonical Procedure

Use `skills/loom-records/references/repair-and-drift.md` as the procedure.

In short:

1. walk the requested scope
2. classify drift with evidence
3. separate safe repairs from owner-layer changes
4. apply safe repairs in small verified batches
5. route semantic repairs to the owning skill
6. leave the repair trail visible

## Native tools to prefer

- `find .loom -type f -name '*.md' | sort`
- `rg -n '^id:' .loom --glob '*.md'`
- `rg -n '<kind>:<id>' .loom --glob '*.md'`
- `rg -n '^status:' .loom/tickets --glob '*.md'`
- `rg -n '^status:' .loom/{constitution,initiatives,research,specs,plans,critique,wiki,evidence,packets} --glob '*.md'`
- `rg -n '[a-z]+:[a-z0-9-]+#(REQ|ACC|CLAIM)-[0-9]{3}' .loom --glob '*.md'`
- `git log --oneline -- .loom/ | head -20`
- `git diff --stat`

## Guardrails

- Fail closed when ownership is ambiguous; surface the conflict and route, do not guess.
- Do not rewrite canonical records silently; safe repairs are for broken-link hygiene, not semantic edits.
- Do not reconcile contradictions by deletion; rename, supersede with forward links, or amend with explicit reasoning.
- Do not treat recency as truth; the owning layer decides.
- Do not widen scope mid-pass; note larger drift and route rather than triggering an unbounded rewrite.

## Required output

- drift findings table (class, record, evidence, proposed action, risk)
- safe repairs applied, with paths and one-line summaries
- routed findings with the recommended next command per finding
- residual drift that cannot be fixed from here and why
- recommended next command
