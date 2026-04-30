# Retrieval

Use progressive loading.

Memory retrieval should reduce orientation cost without letting memory answer
canonical-truth questions by itself. Use memory to find the right records; use
the owner records to decide what is true.

## L0

Read only the `<!-- L0: ... -->` header and maybe headings.

Use this to decide whether the file is relevant enough to inspect further.

## L1

Scan section headers or compact bullets.

Use this to collect retrieval cues, links, aliases, or preferences that may
shape the next read.

## L2

Read the full file only when it is clearly relevant.

After reading memory at L2, follow links into canonical records before making a
project-truth claim.

## Query patterns

```bash
rg -n '<!-- L0:' .loom/memory --glob '*.md'
rg -n '\[\[' .loom/memory --glob '*.md'
```

Follow `[[links]]` when they sharpen the answer.
Do not chase them mechanically.

## Retrieval Discipline

- Start with memory when orientation cost is high and the needed truth owner is
  not yet obvious.
- Skip memory when the ticket, spec, plan, or evidence target is already known.
- Treat memory as a pointer surface. Confirm live state in tickets, accepted
  explanation in wiki, intended behavior in specs, and proof in evidence.
- If a memory item is the only source for an important claim, promote or verify it
  before relying on it.
- If memory contradicts an owner record, trust the owner record and queue memory
  housekeeping.
