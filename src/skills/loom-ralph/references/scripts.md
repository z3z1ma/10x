# Ralph Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-ralph`.

## `scripts/compile_packet.py`

Purpose:

- compile a bounded Ralph execution packet for one target record

Arguments:

- `target_ref`: canonical target ref, usually a ticket ref
- `subsystem`: use `ralph` in this skill
- `--mode`: packet mode; defaults to `execution`; accepted values are `execution`, `review-only`, `diagnostic`, and `reconciliation`
- `--style`: packet style; defaults to `reference-first`; accepted values are `reference-first` and `hermetic`
- `--allow-write-ref`: repeatable allowed-write ref for execution packets
- `--output`: optional output path override

Output:

- prints the compiled packet path relative to the workspace

Example:

```bash
python3 "scripts/compile_packet.py" "ticket:0002" ralph --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/create_verification.py`

Purpose:

- create verification evidence after a Ralph run or supporting check

Arguments:

- `slug`: verification slug
- `--title`: optional human-readable title
- `--link=KEY=REF` or `--link=kind:ref`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment for command, evidence, or outcome text
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the verification record as workspace-scoped instead of repository-scoped; when omitted, linked record scopes are inferred when possible

Example:

```bash
python3 "scripts/create_verification.py" ralph-ticket-0002-run --title "Record Ralph run across admin UI and query service" --link "ticket:0002" --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py"
```

## `scripts/validate_record.py`

Purpose:

- validate one affected record or the full visible record set before and after execution

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/tickets/multi-0002-admin-query-contract-sync.md"
```

## `scripts/check_links.py`

Purpose:

- confirm that reconciliation did not leave broken record links

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/check_links.py"
```

## `scripts/resolve_scope.py`

Purpose:

- resolve repository ownership before packet compilation or launch

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
python3 "scripts/resolve_scope.py" --json --path "repos/admin-ui/src/main.ts"
```
