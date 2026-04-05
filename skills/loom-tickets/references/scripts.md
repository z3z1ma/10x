# Ticket Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-tickets`.

## `scripts/loom create ticket`

Purpose:

- create a ticket scaffold under `.loom/tickets/`
- with no slug, validate all ticket records instead of creating one

Arguments:

- `slug`: ticket slug used in the generated filename
- `--title`: optional human-readable title
- `--status`: optional ticket status override
- `--link=KEY=REF` or `--link=kind:ref`: repeatable typed link assignment; plain refs infer their link key from the ref prefix
- `--section=Heading=Body`: repeatable section assignment
- `--path`, `--repository`, `--workspace-scope`: scope controls

Example:

```bash
scripts/loom create ticket inventory-shared-script-clis --title "Inventory shared Loom script CLIs" --status ready --path "repos/admin-ui/src/main.ts" --link "plan:bootstrap-cli-reference-docs"
```

## `scripts/loom link`

Purpose:

- add or remove typed ticket links such as verification, critique, docs, or related work

Arguments:

- `target`: ticket ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
scripts/loom link "ticket:0002" --add "verification:admin-query-contract-sync-validation"
```

## `scripts/loom verify`

Purpose:

- create a verification record and link it to ticket work

Arguments:

- `slug`: verification slug
- `--title`, `--link`, `--section`: verification content inputs
- `--path`, `--repository`, `--workspace-scope`: scope inputs

Example:

```bash
scripts/loom verify admin-query-contract-sync-validation --title "Validate admin UI and query service contract sync" --link "ticket:0002"
```

## `scripts/loom diagnose`

Purpose:

- validate structural record health before status changes or handoff

Arguments:

- `--json`: emit a machine-readable doctor report

Example:

```bash
scripts/loom diagnose --json
```

## `scripts/loom check-links`

Purpose:

- check whether linked record refs resolve across the visible record graph

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
scripts/loom check-links
```

## `scripts/loom scope`

Purpose:

- discover repository ownership before broadening ticket scope

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
scripts/loom scope --json --path "repos/query-service/src/service.py"
```
