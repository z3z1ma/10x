# Docs Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-docs`.

## `scripts/loom create doc`

Purpose:

- create a documentation record scaffold under `.loom/docs/`

Example:

```bash
scripts/loom create doc admin-query-contract-reference --title "Admin UI and query service contract reference" --status draft --link ticket=ticket:0002
```

## `scripts/loom packet`

Purpose:

- compile a docs packet for bounded fresh-context documentation work

Example:

```bash
scripts/loom packet "ticket:0002" docs --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/loom link`

Purpose:

- add or remove truth-source and verification links on a docs record

Example:

```bash
scripts/loom link "doc:admin-query-contract-reference" --add "verification:admin-query-contract-doc-evidence"
```

## `scripts/loom verify`

Purpose:

- create verification evidence for docs-supporting checks or docs runs

Example:

```bash
scripts/loom verify admin-query-contract-doc-evidence --title "Docs evidence" --link "doc:admin-query-contract-reference"
```

## `scripts/loom diagnose`, `scripts/loom check-links`, `scripts/loom scope`

Use these commands for structural validation, graph integrity, and scope resolution around docs work.
