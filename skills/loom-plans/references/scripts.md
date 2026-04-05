# Plan Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-plans`.

## `scripts/loom create plan`

Purpose:

- create a plan scaffold under `.loom/plans/`
- with no slug, validate plans instead

Example:

```bash
scripts/loom create plan bootstrap-cli-reference-docs --title "Bootstrap Loom CLI reference docs" --status active
```

## `scripts/loom link`

Purpose:

- add or remove typed links between a plan and its governing or downstream records

Example:

```bash
scripts/loom link "plan:bootstrap-cli-reference-docs" --add "ticket:0002"
```

## `scripts/loom diagnose`

Purpose:

- validate structural integrity before relying on the plan as live strategic guidance

Example:

```bash
scripts/loom diagnose --json
```
