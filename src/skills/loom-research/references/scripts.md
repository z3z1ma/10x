# Research Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-research`.

## `scripts/create_research.py`

Purpose:

- create a research note scaffold under `.loom/research/`

Arguments:

- `slug`: research slug
- `--title`: optional human-readable title
- `--status`: optional research status override such as `active`
- `--link=KEY=REF`: repeatable typed upstream or downstream link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the research record as workspace-scoped instead of repository-scoped

Output:

- prints the created research record path relative to the workspace

Example:

```bash
python3 "scripts/create_research.py" shared-script-cli-inventory --title "Inventory shared Loom script CLIs" --status active --link plan=plan:bootstrap-cli-reference-docs
```

## `scripts/link_records.py`

Purpose:

- add or remove typed links on an existing research note

Arguments:

- `target`: research ref to mutate
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Example:

```bash
python3 "scripts/link_records.py" "research:shared-script-cli-inventory" --add "ticket:0002"
```

## `scripts/validate_record.py`

Purpose:

- validate one research note or the full visible record set

Arguments:

- `path`: optional record path
- `--json`: emit structured JSON issues

Example:

```bash
python3 "scripts/validate_record.py" ".loom/research/inventory-shared-loom-script-clis.md"
```
