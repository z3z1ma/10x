# Initiative Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/initiatives.py` inside `loom-initiatives`.

## Direct Initiative Query Ideas

The bundled CLI scaffolds initiatives and mutates typed links.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/initiatives/` directly.

Initiatives by state and recency:

```bash
rg -n '"status":\s*"(active|revised|superseded)"|"updated_at":' .loom/initiatives/*.md
```

The sections that usually drive near-term execution decisions:

```bash
rg -n '^# (Objective|Why Now|Success Metrics|Milestones|Dependencies|Status Summary)$' .loom/initiatives/*.md
```

Initiatives already linked to downstream execution artifacts:

```bash
rg -n '(spec|plan|ticket|research):' .loom/initiatives/*.md
```

Where an initiative is actually referenced downstream:

```bash
rg -n 'initiative:' .loom/{specs,plans,tickets,docs,critique}
```

## `scripts/initiatives.py create`

Purpose:

- create an initiative record scaffold under `.loom/initiatives/`
- with no slug, validate initiative records instead

Example:

```bash
scripts/initiatives.py create improve-operator-workflows
```

## `scripts/initiatives.py link`

Purpose:

- add or remove typed research, spec, plan, or ticket links on an initiative

Example:

```bash
scripts/initiatives.py link "initiative:improve-operator-workflows" --add "plan:bootstrap-cli-reference-docs"
```
