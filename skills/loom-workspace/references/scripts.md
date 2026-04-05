# Workspace Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-workspace`.

## `scripts/loom status`

Purpose:

- summarize current record counts by kind and status

Arguments:

- `--json`: emit a machine-readable JSON summary instead of grouped text

Output:

- grouped text counts by record kind and status
- JSON summary when `--json` is provided

Example:

```bash
scripts/loom status --json
```

## `scripts/loom diagnose`

Purpose:

- check workspace health before trusting packet, review, or durable-edit flows
- with `--fix`, create missing `.loom/` root and canonical subtree directories before reporting

Arguments:

- `--json`: emit a machine-readable doctor report
- `--fix`: create missing `.loom/` directories, then re-check and report the final state

Output:

- text or JSON workspace health report
- non-zero exit status when the workspace is unhealthy

Example:

```bash
scripts/loom diagnose --fix --json
```

## `scripts/loom list`

Purpose:

- list canonical records before linking, routing, or packet compilation

Arguments:

- `--kind`: optional kind filter such as `ticket` or `plan`
- `--status`: optional status filter
- `--include-runs`: include run artifacts in the listing
- `--json`: emit JSON instead of tab-separated text

Output:

- JSON array when `--json` is provided
- otherwise one tab-separated line per record: `id kind status path`

Example:

```bash
scripts/loom list --kind ticket --status ready --json
```

## `scripts/loom create`

Purpose:

- create a new record scaffold or validate an existing record family

Arguments:

- `kind`: record kind such as `ticket`, `spec`, or `doc`
- `slug`: optional slug; omit it to validate that record family
- `--title`, `--status`, `--link`, `--section`: creation inputs
- `--path`, `--repository`, `--workspace-scope`: scope inputs
- `--json`: emit validation issues as JSON

Examples:

```bash
scripts/loom create ticket
scripts/loom create spec helper-cli-reference --title "Helper CLI reference"
```

## `scripts/loom check-links`

Purpose:

- confirm that typed record links resolve across the workspace

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
scripts/loom check-links
```

## `scripts/loom scope`

Purpose:

- discover repository ownership for the workspace or for one target path

Arguments:

- `--path`: optional target path to resolve to one owning repository/worktree
- `--json`: emit structured JSON output

Example:

```bash
scripts/loom scope --json --path ".loom/constitution/constitution.md"
```

## `scripts/loom link`

Purpose:

- add or remove typed record links

Arguments:

- `target`: record ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
scripts/loom link "ticket:0002" --add "verification:ticket-0002-check"
```

## `scripts/loom verify`

Purpose:

- create a verification record under `.loom/verification/`

Arguments:

- `slug`: verification slug
- `--title`, `--link`, `--section`: verification content inputs
- `--path`, `--repository`, `--workspace-scope`: scope inputs

Example:

```bash
scripts/loom verify ticket-0002-check --title "Ticket 0002 verification" --link "ticket:0002"
```

## `scripts/loom packet`

Purpose:

- compile a packet for `ralph`, `critique`, or `docs`

Arguments:

- `target_ref`: canonical target ref
- `subsystem`: one of `ralph`, `critique`, or `docs`
- `--mode`, `--style`, `--allow-write-ref`, `--output`: packet controls

Example:

```bash
scripts/loom packet "ticket:0002" ralph --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/loom memory ...`

Purpose:

- run memory helper commands from the unified CLI

Commands:

- `scripts/loom memory scan [--domain all|system|user] [--json]`
- `scripts/loom memory validate [--json]`
- `scripts/loom memory rebuild-glacier`
- `scripts/loom memory rebuild-links`

Example:

```bash
scripts/loom memory scan --domain user --json
```
