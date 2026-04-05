# Initiative Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-initiatives`.

## `scripts/loom create initiative`

Purpose:

- create an initiative record scaffold under `.loom/initiatives/`
- with no slug, validate initiative records instead

Example:

```bash
scripts/loom create initiative improve-operator-workflows --title "Improve operator workflows"
```

## `scripts/loom link`

Purpose:

- add or remove typed research, spec, plan, or ticket links on an initiative

Example:

```bash
scripts/loom link "initiative:improve-operator-workflows" --add "plan:bootstrap-cli-reference-docs"
```

## `scripts/loom diagnose`

Purpose:

- validate structural integrity before relying on an initiative as strategic truth

Example:

```bash
scripts/loom diagnose --json
```
