# Retrieval

Use progressive loading.

## L0

Read only the `<!-- L0: ... -->` header and maybe headings.

## L1

Scan section headers or compact bullets.

## L2

Read the full file only when it is clearly relevant.

## Query patterns

```bash
rg -n '<!-- L0:' .loom/memory --glob '*.md'
rg -n '\[\[' .loom/memory --glob '*.md'
```

Follow `[[links]]` when they sharpen the answer.
Do not chase them mechanically.
