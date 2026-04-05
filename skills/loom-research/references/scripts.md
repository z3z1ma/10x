# Research Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-research`.

## `scripts/loom create research`

Purpose:

- create a research note scaffold under `.loom/research/`
- with no slug, validate research notes instead

Example:

```bash
scripts/loom create research shared-script-cli-inventory --title "Inventory shared Loom script CLIs"
```

## `scripts/loom link`

Purpose:

- add or remove typed links on an existing research note

Example:

```bash
scripts/loom link "research:shared-script-cli-inventory" --add "ticket:0002"
```

## `scripts/loom diagnose`

Purpose:

- validate structural integrity before downstream work relies on the note as evidence

Example:

```bash
scripts/loom diagnose --json
```
