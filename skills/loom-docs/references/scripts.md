# Docs Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/docs.py` inside `loom-docs`.

## Direct Docs Query Ideas

The bundled CLI creates docs records, docs packets, links, and verification artifacts.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/docs/` and `.loom/runs/docs/` directly.

Docs by lifecycle state:

```bash
rg -n '"status":\s*"(draft|accepted|stale|superseded)"|"updated_at":' .loom/docs/*.md
```

Docs tied to one target ticket, spec, plan, or critique:

```bash
rg -n 'ticket:0002|spec:minimum-proven-core-workflow-surface|plan:bootstrap-cli-reference-docs|critique:' .loom/docs/*.md
```

Compiled docs packets that likely still need reconciliation back into canonical docs:

```bash
rg -n '"status":\s*"compiled"|"generated_at":|"ref":' .loom/runs/docs/*.md
```

Newest doc updates first:

```bash
rg -H -o '"updated_at":\s*"[^"]+"' .loom/docs | sort -t'"' -k4,4r
```

## `scripts/docs.py create`

Purpose:

- create a documentation record scaffold under `.loom/docs/`

Example:

```bash
scripts/docs.py create admin-query-contract-reference --status draft --link ticket=ticket:0002
```

## `scripts/docs.py packet`

Purpose:

- scaffold a docs packet record under `.loom/runs/docs/`

Example:

```bash
scripts/docs.py packet "ticket:0002" docs --mode execution --style reference-first --allow-write-ref "ticket:0002"
```

## `scripts/docs.py link`

Purpose:

- add or remove truth-source and verification links on a docs record

Example:

```bash
scripts/docs.py link "doc:admin-query-contract-reference" --add "verification:admin-query-contract-doc-evidence"
```

## `scripts/docs.py verify`

Purpose:

- create verification evidence for docs-supporting checks or docs runs

Example:

```bash
scripts/docs.py verify admin-query-contract-doc-evidence --link "doc:admin-query-contract-reference"
