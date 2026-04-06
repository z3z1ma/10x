# Memory Housekeeping Scripts

## Direct Memory Housekeeping Query Ideas

The bundled CLI validates the memory module and rebuilds derived indexes.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/memories/` mechanically before or after housekeeping.

Memory files changed recently:

```bash
find .loom/memories -type f -name "*.md" -mtime -1 | sort
```

Archive pressure in observations and completed action items:

```bash
rg -c '^- ' .loom/memories/user/observations.md .loom/memories/system/self-observations.md; rg -c '^- \[x\]' .loom/memories/user/action-items.md
```

Files that contain wiki-links and may need backlink index reconciliation after edits:

```bash
rg -l '\[\[[^]]+\]\]' .loom/memories
```

Regular memory files missing L0 headers before or after housekeeping edits:

```bash
rg --files-without-match '^<!-- L0: .+ -->$' .loom/memories/*.md .loom/memories/system/*.md .loom/memories/user/*.md
```

Glacier batches with their main frontmatter signals:

```bash
rg -n '"type":|"domain":|"tags":|"date_range":|"entries":|"summary":' .loom/memories/glacier/**/*.md
```

## `scripts/memory.py memory validate`

Use this command to validate the module before and after structural edits.

```bash
scripts/memory.py memory validate
scripts/memory.py memory validate --json
```

## `scripts/memory.py memory scan`

Use this command when you want a quick summary of regular memory files.

```bash
scripts/memory.py memory scan
```

## `scripts/memory.py memory rebuild-glacier`

Use this command after archive edits so the glacier catalog stays truthful.

```bash
scripts/memory.py memory rebuild-glacier
```

## `scripts/memory.py memory rebuild-links`

Use this command after link-heavy edits so the backlink map stays truthful.

```bash
scripts/memory.py memory rebuild-links
```
