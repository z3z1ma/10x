# Spec Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-specs`.

## `scripts/loom create spec`

Purpose:

- create a spec scaffold under `.loom/specs/`
- with no slug, validate specs instead

Example:

```bash
scripts/loom create spec helper-cli-reference --title "Helper CLI reference" --link constitution=constitution:main
```

## `scripts/loom link`

Purpose:

- add or remove typed upstream and downstream links on a spec

Example:

```bash
scripts/loom link "spec:helper-cli-reference" --add "plan:bootstrap-cli-reference-docs"
```

## `scripts/loom diagnose`

Purpose:

- validate structural integrity before handing the spec to plans, tickets, critique, or docs

Example:

```bash
scripts/loom diagnose --json
```
