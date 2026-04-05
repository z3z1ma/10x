# Memory Housekeeping Scripts

## `scripts/loom memory validate`

Use this command to validate the module before and after structural edits.

```bash
scripts/loom memory validate
scripts/loom memory validate --json
```

## `scripts/loom memory scan`

Use this command when you want a quick summary of regular memory files.

```bash
scripts/loom memory scan
```

## `scripts/loom memory rebuild-glacier`

Use this command after archive edits so the glacier catalog stays truthful.

```bash
scripts/loom memory rebuild-glacier
```

## `scripts/loom memory rebuild-links`

Use this command after link-heavy edits so the backlink map stays truthful.

```bash
scripts/loom memory rebuild-links
```
