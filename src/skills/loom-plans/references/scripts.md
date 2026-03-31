# Plan Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-plans`.

## `scripts/create_plan.py`

Purpose:

- create a plan scaffold under `.loom/plans/`

Arguments:

- `slug`: plan slug
- `--title`: optional human-readable title
- `--status`: optional plan status override such as `draft` or `active`
- `--link=KEY=REF`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the plan as workspace-scoped instead of repository-scoped

Example:

```bash
python3 "scripts/create_plan.py" bootstrap-cli-reference-docs --title "Bootstrap Loom CLI reference docs" --status active --path "repos/admin-ui/src/main.ts" --link roadmap=roadmap:bootstrap-the-markdown-first-protocol-corpus
```

## `scripts/link_records.py`

Purpose:

- add or remove typed links between a plan and its governing or downstream records

Arguments:

- `target`: plan ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "plan:bootstrap-cli-reference-docs" --add "ticket:0002"
```

## `scripts/validate_record.py`

Purpose:

- validate one plan or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/plans/bootstrap-loom-cli-reference-docs.md"
```
