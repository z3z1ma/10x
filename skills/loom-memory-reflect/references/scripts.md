# Memory Reflection Scripts

Reflection uses the same structural helpers as ordinary memory work.

## Direct Memory Reflection Query Ideas

The bundled CLI keeps the memory structure healthy and provides compact L0 scans.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to spot reflection candidates or memory drift directly.

Memory files changed recently and worth reading first:

```bash
find .loom/memories -type f -name "*.md" -mtime -1 | sort
```

Observation volume that may justify condensation or synthesis:

```bash
rg -c '^- ' .loom/memories/user/observations.md .loom/memories/system/self-observations.md
```

Temporal reminders that may now be stale:

```bash
rg -n '\(until 20[0-9]{2}-[0-9]{2}\)' .loom/memories
```

Entity status and last-seen markers for drift review:

```bash
rg -n '^### |^status: |^last: ' .loom/memories/**/entities.md
```

Regular memory files missing L0 headers before a broad reflection pass:

```bash
rg --files-without-match '^<!-- L0: .+ -->$' .loom/memories/*.md .loom/memories/system/*.md .loom/memories/user/*.md
```

Files with dense cross-links that may hide a reusable thread or pattern:

```bash
rg -n '\[\[[^]]+\]\]' .loom/memories/system/*.md .loom/memories/user/*.md
```

## `scripts/memory.py memory scan`

Use this command before a broad reflection pass so file selection stays deliberate.

```bash
scripts/memory.py memory scan
scripts/memory.py memory scan --domain system
```

## `scripts/memory.py memory validate`

Use this command before and after a substantial reflection pass.

```bash
scripts/memory.py memory validate
```
