# Ralph Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-ralph`.

## `scripts/loom packet`

Purpose:

- compile a bounded Ralph execution packet for one target record

Arguments:

- `target_ref`: canonical target ref, usually a ticket ref
- `subsystem`: use `ralph` in this skill
- `--mode`: packet mode
- `--style`: packet style
- `--allow-write-ref`: repeatable allowed-write ref for execution packets
- `--output`: optional output path override

Output:

- prints the compiled packet path relative to the workspace

Example:

```bash
scripts/loom packet "ticket:0002" ralph --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/loom verify`

Purpose:

- create verification evidence after a Ralph run or supporting check

Arguments:

- `slug`: verification slug
- `--title`, `--link`, `--section`: verification content inputs
- `--path`, `--repository`, `--workspace-scope`: scope inputs

Example:

```bash
scripts/loom verify ralph-ticket-0002-run --title "Record Ralph run across admin UI and query service" --link "ticket:0002"
```

## `scripts/loom diagnose`

Purpose:

- validate structural record health before and after execution

Arguments:

- `--json`: emit a machine-readable doctor report

Example:

```bash
scripts/loom diagnose --json
```

## `scripts/loom check-links`

Purpose:

- confirm that reconciliation did not leave broken record links

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
scripts/loom check-links
```

## `scripts/loom scope`

Purpose:

- resolve repository ownership before packet compilation or launch

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
scripts/loom scope --json --path "repos/admin-ui/src/main.ts"
```
