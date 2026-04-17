# Common Frontmatter

Loom uses YAML frontmatter because it is human-editable and widely understood.

## Common Fields

Most canonical Loom records should carry these fields:

```yaml
---
id: ticket:abcd1234
kind: ticket
status: ready
created_at: 2026-04-17T00:00:00Z
updated_at: 2026-04-17T00:00:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  plan:
    - plan:bootstrap-core
---
```

## Required Common Fields

- `id`
- `kind`
- `status`
- `created_at`
- `updated_at`
- `scope`
- `links`

Some kinds add more:

- tickets add `depends_on`
- packets add `target`, `mode`, `style`, `write_scope`, and `sources`
- wiki pages may add `page_type`
- critique records may add `review_target`

## Scope Shape

Use this general shape:

```yaml
scope:
  kind: repository
  repositories:
    - repo:root
```

Other valid `kind` values:

- `workspace`
- `multi_repository`

For workspace-scoped records, it is acceptable to omit `repositories` entirely or leave it empty.

## Timestamps

Use UTC with `Z` suffix.

Example:

```yaml
created_at: 2026-04-17T19:05:00Z
```

## Links

`links` is a typed mapping.

Good:

```yaml
links:
  initiative:
    - initiative:prove-core-loop
  plan:
    - plan:bootstrap-core
```

Acceptable empty form:

```yaml
links: {}
```

Typed links are not a substitute for prose, but they make the graph legible to search tools.
