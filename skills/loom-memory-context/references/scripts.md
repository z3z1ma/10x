# Memory Context Scripts

## `scripts/loom memory scan`

Purpose:

- list compact L0 summaries of memory files before deciding what to read

Arguments:

- `--domain all|system|user`: restrict output to one memory domain
- `--json`: emit structured JSON rows

Examples:

```bash
scripts/loom memory scan
scripts/loom memory scan --domain user
scripts/loom memory scan --json
```

## `scripts/loom memory validate`

Purpose:

- validate the manifest, required files, and L0 coverage for the memory module

Arguments:

- `--json`: emit structured JSON summary

Examples:

```bash
scripts/loom memory validate
scripts/loom memory validate --json
```
