# Critique Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-critique`.

## `scripts/loom create critique`

Purpose:

- create a critique record scaffold under `.loom/critique/`

Example:

```bash
scripts/loom create critique review-ticket-0002 --title "Review admin UI and query service contract docs" --link ticket=ticket:0002
```

## `scripts/loom packet`

Purpose:

- compile a critique packet for bounded fresh-context review work

Example:

```bash
scripts/loom packet "ticket:0002" critique --mode review-only --style reference-first
```

## `scripts/loom link`

Purpose:

- add or remove reviewed-artifact, follow-up, or verification links on a critique record

Example:

```bash
scripts/loom link "critique:review-ticket-0002" --add "doc:admin-query-contract-reference"
```

## `scripts/loom verify`

Purpose:

- create verification evidence for critique-supporting checks or review runs

Example:

```bash
scripts/loom verify critique-ticket-0002-evidence --title "Critique evidence" --link "critique:review-ticket-0002"
```

## `scripts/loom diagnose`, `scripts/loom check-links`, `scripts/loom scope`

Use these commands for structural validation, graph integrity, and scope resolution around critique work.
