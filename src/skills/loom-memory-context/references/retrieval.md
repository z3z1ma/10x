# Memory Retrieval Reference

## Memory Retrieval Protocol

When responding to any query:

1. **Identify domain** — match query to `system` or `user` via file structure knowledge.
2. **L0 scan** — once you know the domain, run `grep -rn "<!-- L0:" .loom/memories/{domain}/` to get all file summaries in one call. This replaces reading every file — faster and fewer tokens. Use this to pick the right file(s) before opening anything.
3. **Select files by query type:**
   - Tasks, reminders → `action-items.md`
   - Person, "who is" → `entities.md`
   - Overview, "how is" → `hot-memory.md` + `action-items.md`
   - Following a `[[wiki-link]]` → check `link-index.md` for related files
4. **Apply L1 before L2 for long files** — for any file >80 lines, scan section headers before reading fully.
5. **SSOT check on write** — before writing a fact, check if it already exists in its canonical file. Update there, don't duplicate.
6. Default: if unclear, read hot-memory + action-items for the likely domain.

Use the minimum files needed to answer the question or store the fact. Memory quality degrades when every query becomes a broad read.

## L0 / L1 / L2 Progressive Context Loading

Three tiers — L0 is stored, L1 and L2 are retrieval actions:

- **L0** — read the `<!-- L0: ... -->` header. Answer: "is this file relevant?"
- **L1** — scan section headers (`## ...`, `### ...`). Answer: "which section is relevant?"
- **L2** — read the full file or section.

**Decision rules:**

1. When uncertain which files are relevant, grep `<!-- L0:` across the domain directory first.
2. If L0 confirms relevance but the file is >80 lines, scan section headers (L1) before full read.
3. For files <80 lines or when you need full context, go directly to L2.
4. Hot-memory files are always L2 — they're small by design.

## Glacier Reads

Glacier is not the starting point.

Read glacier only when:

- the needed context is older than the warm files now emphasize
- the current files clearly point to archived history
- you need historical evidence rather than the current summary

**Retrieval flow:**

1. Read `.loom/memories/glacier/index.md` (one small file — the full catalog)
2. Filter by domain/tags/date_range in the table
3. Read only the matching glacier files

## Deep Recall Queries

Use deep recall when the user asks for history, prior discussion, or a reconstructed narrative from memory.

Examples:

- "what did I say about breaking changes"
- "when did we discuss admin-ui and query-service"
- "find that conversation about packet scope"
- "what is the history of this topic in memory"

### Pass 1: Locate

1. Extract the likely names, topics, dates, and phrases.
2. Read the relevant hot-memory file first.
3. Grep across the likely domain files:
   - `observations.md`
   - `entities.md`
   - `action-items.md`
   - `hot-memory.md`
   - thread files in the same domain
4. If current files are insufficient, read `glacier/index.md` and then only the matching archive files.

### Pass 2: Extract

1. Read the most relevant 3-5 files.
2. Pull the exact passages that answer the query.
3. Track the first mention, later changes, and the latest state.

### Pass 3: Synthesize

1. Answer with a coherent timeline or summary.
2. Prefer dated findings over raw excerpts.
3. Flag memory gaps instead of pretending recall is complete.

## Wiki-Link Behavior

Follow `[[wiki-links]]` when the linked topic is clearly relevant.

Do not chase every link mechanically. Follow links because they sharpen the answer, not because they exist.

**Write-time linking:** When writing or editing ANY memory file, actively add `[[links]]` to related files. This is the main way links get created.

**Write-time back-linking:** When you add a link A→B, ask: "does B benefit from pointing back to A?" If yes, open B and add `[[A]]` where relevant. Not every link needs a reciprocal — only add B→A when B genuinely gains context.

**Discovery:** To find what connects to a file you're reading, check `.loom/memories/link-index.md`.
