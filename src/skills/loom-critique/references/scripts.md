# Critique Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-critique`.

## `scripts/create_critique.py`

Purpose:

- create a critique record scaffold under `.loom/critique/`

Arguments:

- `slug`: critique slug
- `--title`: optional human-readable title
- `--status`: optional critique status override such as `active`
- `--link=KEY=REF`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the critique as workspace-scoped instead of repository-scoped

Example:

```bash
python3 "scripts/create_critique.py" review-ticket-0002 --title "Review admin UI and query service contract docs" --status active --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py" --link ticket=ticket:0002
```

## `scripts/compile_packet.py`

Purpose:

- compile a critique packet for bounded fresh-context review work

Arguments:

- `target_ref`: canonical target ref to review
- `subsystem`: use `critique` in this skill
- `--mode`: packet mode; defaults to `execution`; accepted values are `execution`, `review-only`, `diagnostic`, and `reconciliation`
- `--style`: packet style; defaults to `reference-first`; accepted values are `reference-first` and `hermetic`
- `--allow-write-ref`: repeatable allowed-write ref when the packet intentionally permits mutations
- `--output`: optional output path override

Example:

```bash
python3 "scripts/compile_packet.py" "ticket:0002" critique --mode review-only --style reference-first
```

## `scripts/link_records.py`

Purpose:

- add or remove reviewed-artifact, follow-up, or verification links on a critique record

Arguments:

- `target`: critique ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "critique:review-ticket-0002" --add "doc:admin-query-contract-reference"
```

## `scripts/create_verification.py`

Purpose:

- create verification evidence for critique-supporting checks or review runs

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
python3 "scripts/create_verification.py" critique-ticket-0002-evidence --title "Critique evidence for the admin UI and query service contract review" --link "critique:review-ticket-0002" --path "repos/admin-ui/src/main.ts" --path "repos/query-service/src/service.py"
```

## `scripts/validate_record.py`

Purpose:

- validate one critique record or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/critique/review-ticket-0002.md"
```

## `scripts/check_links.py`

Purpose:

- confirm that reviewed-artifact and follow-up links resolve cleanly

Arguments:

- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/check_links.py"
```

## `scripts/resolve_scope.py`

Purpose:

- resolve repository ownership before compiling a critique packet or editing reviewed records

Arguments:

- `--path`: optional target path to resolve to one owner
- `--json`: emit structured JSON output

Example:

```bash
python3 "scripts/resolve_scope.py" --json --path "repos/query-service/src/service.py"
```
