# Spec Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-specs`.

## `scripts/create_spec.py`

Purpose:

- create a spec scaffold under `.loom/specs/`

Arguments:

- `slug`: spec slug
- `--title`: optional human-readable title
- `--status`: optional spec status override such as `active`
- `--link=KEY=REF`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the spec as workspace-scoped instead of repository-scoped

Example:

```bash
python3 "scripts/create_spec.py" helper-cli-reference --title "Helper CLI reference" --status active --path "repos/admin-ui/src/main.ts" --link constitution=constitution:main
```

## `scripts/link_records.py`

Purpose:

- add or remove typed upstream and downstream links on a spec

Arguments:

- `target`: spec ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "spec:helper-cli-reference" --add "plan:bootstrap-cli-reference-docs"
```

## `scripts/validate_record.py`

Purpose:

- validate one spec or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/specs/operator-cli-reference.md"
```
