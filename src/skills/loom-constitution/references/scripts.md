# Constitutional Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/...` inside `loom-constitution`. Do not switch bundled operator guidance to source-repo-only `build/...` paths.

## `scripts/create_constitution.py`

Purpose:

- create or intentionally replace a constitution record scaffold

Arguments:

- `slug`: constitution slug; use `main` for the primary constitution record
- `--title`: optional title override
- `--status`: optional constitution status override such as `active`
- `--section=Heading=Body`: repeatable section assignment used to seed body sections
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the constitution as workspace-scoped instead of repository-scoped

Output:

- prints the created record path relative to the workspace

Example:

```bash
python3 "scripts/create_constitution.py" main --title "Main Constitution" --status active --section "Vision=Make Loom a portable Markdown-first operating protocol."
```

## `scripts/create_decision.py`

Purpose:

- create one numbered decision record under `.loom/constitution/`

Arguments:

- `slug`: decision slug
- `--title`: optional human-readable title; also influences the generated file slug
- `--status`: optional decision status override
- `--link=KEY=REF`: repeatable typed link assignment such as `--link roadmap=roadmap:bootstrap-the-markdown-first-protocol-corpus`
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the decision as workspace-scoped instead of repository-scoped

Notes:

- the script allocates the next `decision:000N` id automatically

Example:

```bash
python3 "scripts/create_decision.py" packet-trust-boundary --title "Make packet trust boundaries explicit" --status active --link roadmap=roadmap:bootstrap-the-markdown-first-protocol-corpus
```

## `scripts/create_roadmap.py`

Purpose:

- create one roadmap record for strategic direction and milestone framing

Arguments:

- `slug`: roadmap slug used to derive the record id and filename
- `--title`: optional human-readable title
- `--status`: optional roadmap status override
- `--link=KEY=REF`: repeatable typed link assignment
- `--section=Heading=Body`: repeatable section assignment
- `--path=<workspace-path>`: repeatable path used to infer the owning repository or repositories
- `--repository=<repo-id>`: repeatable explicit repository owner override
- `--workspace-scope`: mark the roadmap as workspace-scoped instead of repository-scoped

Output:

- prints the created roadmap path relative to the workspace

Example:

```bash
python3 "scripts/create_roadmap.py" bootstrap-the-markdown-first-protocol-corpus --title "Bootstrap the Markdown-first protocol corpus" --status active --link decision=decision:0001
```

## `scripts/link_records.py`

Purpose:

- add or remove typed links on constitutional records after the prose is in place

Arguments:

- `target`: record ref to mutate, such as `decision:0001` or `roadmap:bootstrap-the-markdown-first-protocol-corpus`
- `--add=KEY=REF` or `--add=kind:ref`: repeatable link addition
- `--remove=KEY=REF` or `--remove=kind:ref`: repeatable link removal

Notes:

- provide at least one `--add` or `--remove`
- `constitution:main` should stay link-free; use this script there only to remove mistaken links

Example:

```bash
python3 "scripts/link_records.py" "roadmap:bootstrap-the-markdown-first-protocol-corpus" --add "decision:0002"
```

## `scripts/validate_record.py`

Purpose:

- validate one constitutional record or the full visible record set

Arguments:

- `path`: optional record path; omit it to validate all discovered records
- `--json`: emit structured JSON issues instead of text

Output:

- success text when no issues are found
- `ERROR <path>: <message>` lines when issues exist
- non-zero exit status on validation problems

Example:

```bash
python3 "scripts/validate_record.py" ".loom/constitution/constitution.md"
```
