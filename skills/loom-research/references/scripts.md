# Research Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/research.py` inside `loom-research`.

## Direct Research Query Ideas

The bundled CLI scaffolds research notes and mutates typed links.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/research/` directly.

Research notes by state and recency:

```bash
rg -n '"status":\s*"(active|revised|superseded)"|"updated_at":' .loom/research/*.md
```

Research notes already feeding downstream artifacts:

```bash
rg -n '(initiative|spec|plan|ticket|doc|critique):' .loom/research/*.md
```

Where research is actually consumed outside the research layer:

```bash
rg -n 'research:' .loom/{initiatives,specs,plans,tickets,docs,critique}
```

Quick navigation to the sections that usually determine whether research is decision-ready:

```bash
rg -n '^# (Question|Methodology|Evidence|Conclusions|Recommendations|Open Questions)$' .loom/research/*.md
```

## `scripts/research.py create`

Purpose:

- create a research note scaffold under `.loom/research/`
- with no slug, validate research notes instead

Example:

```bash
scripts/research.py create shared-script-cli-inventory
```

## `scripts/research.py link`

Purpose:

- add or remove typed links on an existing research note

Example:

```bash
scripts/research.py link "research:shared-script-cli-inventory" --add "ticket:z8h0g58e"
```
