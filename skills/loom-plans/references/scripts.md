# Plan Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/plans.py` inside `loom-plans`.

## Direct Plan Query Ideas

The bundled CLI scaffolds plans and mutates typed links.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/plans/` directly.

Plans by state and recency:

```bash
rg -n '"status":\s*"(draft|active|revised|retired)"|"updated_at":' .loom/plans/*.md
```

Plans already connected to ticket execution:

```bash
rg -n 'ticket:' .loom/plans/*.md
```

Plans with workspace-wide or multi-repo scope:

```bash
rg --multiline -l '"repository_scope":\s*\{\s*"kind":\s*"(workspace|multi_repository)"' .loom/plans
```

Quick navigation to the sections that usually drive next execution decisions:

```bash
rg -n '^# (Milestones|Plan of Work|Concrete Steps|Validation and Acceptance|Linked Tickets)$' .loom/plans/*.md
```

## `scripts/plans.py create`

Purpose:

- create a plan scaffold under `.loom/plans/`
- with no slug, validate plans instead

Example:

```bash
scripts/plans.py create bootstrap-cli-reference-docs --status active
```

## `scripts/plans.py link`

Purpose:

- add or remove typed links between a plan and its governing or downstream records

Example:

```bash
scripts/plans.py link "plan:bootstrap-cli-reference-docs" --add "ticket:0002"
```
