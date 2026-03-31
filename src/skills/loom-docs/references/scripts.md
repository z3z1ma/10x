# Docs Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-docs`.

## `scripts/create_doc.py`

Purpose:

- create a documentation record scaffold under `.loom/docs/`

Arguments:

- `slug`: doc slug
- `--title`: optional human-readable title
- `--status`: optional doc status override such as `draft` or `accepted`
- `--link=KEY=REF`: repeatable typed truth-source or downstream link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the doc as workspace-scoped instead of repository-scoped

Example:

```bash
python3 "scripts/create_doc.py" admin-query-contract-reference --title "Admin UI and query service contract reference" --status draft --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py" --link ticket=ticket:0002
```

## `scripts/compile_packet.py`

Purpose:

- compile a docs packet for bounded fresh-context documentation work

Arguments:

- `target_ref`: canonical target ref for the docs pass
- `subsystem`: use `docs` in this skill
- `--mode`: packet mode; defaults to `execution`; accepted values are `execution`, `review-only`, `diagnostic`, and `reconciliation`
- `--style`: packet style; defaults to `reference-first`; accepted values are `reference-first` and `hermetic`
- `--allow-write-ref`: repeatable allowed-write ref when docs work may mutate records
- `--output`: optional output path override

Example:

```bash
python3 "scripts/compile_packet.py" "ticket:0002" docs --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/link_records.py`

Purpose:

- add or remove truth-source and verification links on a docs record

Arguments:

- `target`: doc ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "doc:admin-query-contract-reference" --add "verification:admin-query-contract-doc-evidence"
```

## `scripts/create_verification.py`

Purpose:

- create verification evidence for docs-supporting checks or docs runs

Arguments:

- `slug`: verification slug
- `--title`: optional human-readable title
- `--link=KEY=REF` or `--link=kind:ref`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the verification record as workspace-scoped instead of repository-scoped; when omitted, linked record scopes are inferred when possible

Example:

```bash
python3 "scripts/create_verification.py" admin-query-contract-doc-evidence --title "Docs evidence for the admin UI and query service contract reference" --link "doc:admin-query-contract-reference" --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py"
```

## `scripts/validate_record.py`

Purpose:

- validate one docs record or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/docs/admin-query-contract-reference.md"
```

## `scripts/check_links.py`

Purpose:

- confirm that truth-source and verification links resolve cleanly

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/check_links.py"
```

## `scripts/resolve_scope.py`

Purpose:

- resolve repository ownership before a docs pass edits records across boundaries

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
python3 "scripts/resolve_scope.py" --json --path "repos/admin-ui/src/main.ts"
```
