# Ticket Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-tickets`.

## `scripts/create_ticket.py`

Purpose:

- create a ticket scaffold under `.loom/tickets/`

Arguments:

- `slug`: ticket slug used in the generated filename
- `--title`: optional human-readable title
- `--status`: optional ticket status override such as `proposed`, `ready`, or `active`
- `--link=KEY=REF` or `--link=kind:ref`: repeatable typed link assignment; plain refs infer their link key from the ref prefix
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the ticket as workspace-scoped instead of repository-scoped

Notes:

- the script allocates the next `ticket:000N` id automatically
- the file name gets a repository-derived prefix such as `agel2-0002-...`

Example:

```bash
python3 "scripts/create_ticket.py" inventory-shared-script-clis --title "Inventory shared Loom script CLIs" --status ready --path "repos/admin-ui/src/main.ts" --link "plan:bootstrap-cli-reference-docs" --link "research:shared-script-cli-inventory"
```

## `scripts/link_records.py`

Purpose:

- add or remove typed ticket links such as verification, critique, docs, or related work

Arguments:

- `target`: ticket ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "ticket:0002" --add "verification:admin-query-contract-sync-validation"
```

## `scripts/create_verification.py`

Purpose:

- create a verification record under `.loom/verification/` and link it to ticket work

Arguments:

- `slug`: verification slug
- `--title`: optional human-readable title
- `--link=KEY=REF` or `--link=kind:ref`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment used to seed command, evidence, or outcome sections
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the verification record as workspace-scoped instead of repository-scoped; when omitted, linked record scopes are inferred when possible

Example:

```bash
python3 "scripts/create_verification.py" admin-query-contract-sync-validation --title "Validate admin UI and query service contract sync" --link "ticket:0002" --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py"
```

## `scripts/validate_record.py`

Purpose:

- validate one ticket or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/tickets/multi-0002-admin-query-contract-sync.md"
```

## `scripts/check_links.py`

Purpose:

- check whether linked record refs resolve across the visible record graph

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/check_links.py"
```

## `scripts/resolve_scope.py`

Purpose:

- discover repository ownership before broadening ticket scope

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
python3 "scripts/resolve_scope.py" --json --path "repos/query-service/src/service.py"
```
