# Spec Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/specs.py` inside `loom-specs`.

## Direct Spec Query Ideas

The bundled CLI scaffolds specs and mutates typed links.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/specs/` directly.

Specs by state and recency:

```bash
rg -n '"status":\s*"(active|revised|superseded)"|"updated_at":' .loom/specs/*.md
```

Specs already connected to downstream execution work:

```bash
rg -n '(plan|ticket):' .loom/specs/*.md
```

Specs with workspace-wide or multi-repo scope:

```bash
rg --multiline -l '"repository_scope":\s*\{\s*"kind":\s*"(workspace|multi_repository)"' .loom/specs
```

Quick navigation to the sections that usually decide implementation shape:

```bash
rg -n '^# (Desired Behavior|Requirements|Scenarios|Acceptance|Open Questions)$' .loom/specs/*.md
```

## `scripts/specs.py create`

Purpose:

- create a spec scaffold under `.loom/specs/`
- with no slug, validate specs instead

Example:

```bash
scripts/specs.py create helper-cli-reference --link constitution=constitution:main
```

## `scripts/specs.py link`

Purpose:

- add or remove typed upstream and downstream links on a spec

Example:

```bash
scripts/specs.py link "spec:helper-cli-reference" --add "plan:bootstrap-cli-reference-docs"
```
