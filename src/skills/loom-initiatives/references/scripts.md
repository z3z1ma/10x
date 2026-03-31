# Initiative Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-initiatives`.

## `scripts/create_initiative.py`

Purpose:

- create an initiative record scaffold under `.loom/initiatives/`

Arguments:

- `slug`: initiative slug
- `--title`: optional human-readable title
- `--status`: optional initiative status override such as `active`
- `--link=KEY=REF`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the initiative as workspace-scoped instead of repository-scoped

Example:

```bash
python3 "scripts/create_initiative.py" improve-operator-workflows --title "Improve operator workflows" --status active
```

## `scripts/link_records.py`

Purpose:

- add or remove typed research, spec, plan, or ticket links on an initiative

Arguments:

- `target`: initiative ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "initiative:improve-operator-workflows" --add "plan:bootstrap-cli-reference-docs"
```

## `scripts/validate_record.py`

Purpose:

- validate one initiative or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/initiatives/improve-operator-workflows.md"
```
