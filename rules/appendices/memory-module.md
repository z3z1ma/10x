# Appendix H - Memory Module

## Purpose

The optional `.loom/memories/` module is a plain-text cognitive layer for Loom.

It gives Loom persistent memory, self-reflection, and progressive condensation. Not just recall, but cognition across time.

Everything is plain text by design. Not as a compromise — because plain text is what makes this work. Memory files are just Markdown, which means any agent can `grep` for patterns, `find` what changed, `wc` to check file sizes, and `git diff` to see what the last pipeline run touched. The same Unix tools that make plain-text systems powerful make this memory observable and maintainable.

The module works because the memory is visible, inspectable, editable, and searchable as ordinary Markdown. The filesystem is the interface.

## Authority Boundary

- canonical `.loom/` records outrank `.loom/memories/`
- accepted verification outranks `.loom/memories/`
- `.loom/memories/` may support decisions, but it does not decide them
- tickets remain the sole live execution ledger

If a fact belongs in a ticket, spec, plan, research note, critique, or doc, move that fact into the owning canonical artifact instead of leaving it only in memory.

## Memory Domains

The memory module uses exactly two domains:

- `system`
- `user`

`system` is for agent and workflow self-memory: learned patterns, self-observations, and improvements. It is the module's self-improvement layer.

`user` is for non-canonical user context: observations, entities, action-item reminders, and any durable supporting notes about the user or their work that do not belong in canonical Loom records.

Do not add side-project, work, or personal subdomains in this module.

## Three-Tier Memory

Persistent memory lives in `.loom/memories/`. Three tiers:

- **Hot** (`*/hot-memory.md`) — loaded every conversation, <50 lines each, rewrite freely
- **Warm** (domain files) — loaded when the domain activates, per-file size limits
- **Glacier** (`.loom/memories/glacier/`) — frontmattered archives, indexed via `glacier/index.md`

Hot is the 30,000-foot view. Warm is the working detail. Glacier is retrievable history that stays out of the way.

## L0 Headers (Progressive Context Loading)

Every memory file has a one-line L0 summary as **line 1** — a quick answer to "what would I find if I read this file?" (max 80 chars).

**Format:**

```html
<!-- L0: summary here -->
```

Always the first line of the file, before title or frontmatter.

**Maintenance:** When creating or restructuring a memory file, always add or update its L0. Pipeline steps (reflect, housekeeping) should preserve existing L0 headers and add them to new files.

## L0 / L1 / L2 Retrieval Protocol

Three tiers — L0 is stored, L1 and L2 are retrieval actions:

- **L0** — read the `<!-- L0: ... -->` header. Answer: "is this file relevant?"
- **L1** — scan section headers (`## ...`, `### ...`). Answer: "which section is relevant?"
- **L2** — read the full file or section.

**Decision rules:**

1. When uncertain which files are relevant, `grep "<!-- L0:" .loom/memories/{domain}/` to get all file summaries in one call. Use this to pick the right file(s) before opening anything.
2. If L0 confirms relevance but the file is >80 lines, scan section headers (L1) before full read.
3. For files <80 lines or when you need full context, go directly to L2.
4. Hot-memory files are always L2 — they are small by design.

## Memory Retrieval Protocol

When responding to any query:

1. **Identify domain** — match query to `system` or `user` via file structure knowledge.
2. **L0 scan** — once you know the domain, grep `<!-- L0:` across the domain directory to get all file summaries in one call. Use this to pick the right file(s) before opening anything.
3. **Select files by query type:**
   - Tasks, reminders → `action-items.md`
   - Person, "who is" → `entities.md`
   - Overview, "how is" → `hot-memory.md` + `action-items.md`
   - Following a `[[wiki-link]]` → check `link-index.md` for related files
4. **Apply L1 before L2 for long files** — for any file >80 lines, scan section headers before reading fully.
5. **SSOT check on write** — before writing a fact, check if it already exists in its canonical file. Update there, don't duplicate.
6. Default: if unclear, read hot-memory + action-items for the likely domain.

## Memory Rules

1. **Read on start**: Always read `.loom/memories/hot-memory.md` and `.loom/memories/system/patterns.md` at conversation start.
2. **Write immediately**: Don't wait to save something worth remembering.
3. **Observations are append-only**: `- YYYY-MM-DD [tags]: <observation>` — never edit past entries.
   - Tags: `insight`, `milestone`, `regression`, `workflow`, `decision`, `context`
4. **Action items**: `- [ ] task | due:YYYY-MM-DD | pri:high/medium/low | added:YYYY-MM-DD` / `- [x] task (done YYYY-MM-DD)`. Fields after task are optional — use what's relevant. `pri:` defaults to medium if omitted.
5. **Entities**: 3-line compact registry format. Each entry: `### Name (relationship)` / pipe-separated key facts / `status: active|inactive | last: YYYY-MM-DD | -> [[link]]`. Max 3 content lines per entry. Heavy entries promoted to thread files — entity stub links to thread via `-> [[link]]`. **Temporal validity**: When a fact changes, mark old value as superseded with date. Entities inactive 6+ months → housekeeping moves to glacier.
6. **Hot memory <50 lines**: Prune aggressively, move detail to observations.
7. **Self-improvement**: After notable interactions, append to `system/self-observations.md`. Periodically distill patterns into `system/patterns.md`.
   - **Pattern file caps**: Core `system/patterns.md` has a HARD LIMIT of **70 lines / 5.5KB** — universal rules only. If near cap, compress before adding (merge overlapping rules, drop examples, remove temporal data). Entries must be **timeless rules** — "what to do" not "what happened."
8. **Single Source of Truth (SSOT)**: Each fact lives in ONE canonical file. Other files reference via `[[link]]`, never copy.
   - `entities.md` — people, organizations, named things
   - `action-items.md` — all tasks
   - `hot-memory.md` — current-state summaries (pointers, not source facts)
   - `observations.md` — raw timestamped events (never edit past entries)
   When the same fact appears in two files: keep it in the canonical file, replace the duplicate with a `[[link]]`.
9. **Wiki-links**: Use `[[domain/filename]]` or `[[domain/filename#Section]]` to cross-reference memory files.
   - Path is relative to `.loom/memories/`, no `.md` extension (e.g., `[[user/entities]]`, `[[system/patterns]]`)
   - Follow links when the linked topic is relevant — don't chase every link mechanically
   - To discover what links TO a file, check `.loom/memories/link-index.md` (generated by housekeeping)
   - **Write-time linking (primary)**: When writing or editing ANY memory file, actively add `[[links]]` to related files. This is the main way links get created.
   - **Write-time back-linking**: When you add a link A→B, ask: "does B benefit from pointing back to A?" If yes, open B and add `[[A]]` where relevant. Not every link needs a reciprocal — only add B→A when B genuinely gains context.
   - **Discovery via link-index**: To find what connects to a file you're reading, check `.loom/memories/link-index.md`.
   - Housekeeping runs a link audit as a safety net.
10. **Progressive condensation**: Two processes:
    - **Condensation**: `observations.md` (append) → `patterns.md` (distill 3+ on same theme) → `hot-memory.md` (rewrite freely). Each layer is smaller and more actionable.
    - **Archival**: Old observations (>50) → `glacier/` (indexed, retrievable). Resolved patterns → remove from hot-memory, keep in patterns.

## File Edit Patterns

| File | Pattern |
|------|---------|
| `hot-memory.md` | Rewrite freely |
| `observations.md` | Append only |
| `action-items.md` | Append new, check off done |
| `entities.md` | 3-line registry: `### Name` / key facts / `status\|last\|->[[link]]`. Max 3 content lines per entry |
| Thread files | Current State: rewrite. Timeline: append only |
| `system/self-observations.md` | Append only |
| `system/patterns.md` | Edit in place, distill from self-observations |
| `system/improvements.md` | Edit in place by section |
| `link-index.md` | Auto-generated by housekeeping — do not edit manually |
| `glacier/index.md` | Auto-generated by housekeeping — do not edit manually |

## Threads — The Zettelkasten Layer

Threads are **read-optimized synthesis files**. While observations capture raw events (write-optimized), threads pull related fragments into a coherent narrative. One file per topic, consistent spine:

- **Current State** — what's true right now (rewrite freely, always current)
- **Timeline** — dated entries, append-only, full detail preserved (never condensed)
- **Insights** — learnings, patterns, what's different this time

**Raising a thread:** "Raise" is the verb for creating or updating a thread. A thread gets raised when a topic appears in 3+ observations across 2+ weeks, or when the user says "raise X" or "thread X". Search observations and memory files for all references, synthesize the narrative arc, write or update the thread with the spine structure, and link source fragments via wiki-links.

**Rules:**

- **One file forever** — threads grow long, they don't split or condense
- **Texture is the value** — every entry keeps its full detail, quotes, and dates
- **Fragments never move** — threads reference them, don't replace them
- **Current State is always current** — rewrite it freely as things change

Thread files live in their domain directory (e.g., `.loom/memories/user/running.md`). Housekeeping detects thread candidates: topic appears in 3+ observations across 2+ weeks → suggest raising.

## Action-Item Boundary

`action-items.md` is not a ticket system.

Use `.loom/memories/.../action-items.md` only for supporting reminders or user-context tasks that do not belong in Loom ticket execution tracking.

If the task is execution truth for the repository, it belongs in `.loom/tickets/`.

## Glacier Archival

When files exceed limits, move old data to `.loom/memories/glacier/{domain}/`.

All glacier files get JSON-compatible frontmatter between `---` fences for fast retrieval:

```text
---
{
  "type": "observations|action-items-done|entities-inactive|improvements-done",
  "domain": "system|user",
  "tags": ["relevant", "tags"],
  "date_range": "YYYY-MM to YYYY-MM",
  "entries": 12,
  "summary": "One-line description"
}
---
```

When archiving new entries to an existing glacier file, update the frontmatter: bump `entries`, extend `date_range`, update `tags` list.

**Retrieval flow:**

1. Read `.loom/memories/glacier/index.md` (one small file — the full catalog)
2. Filter by domain/tags/date_range in the table
3. Read only the matching glacier files

### Archival Thresholds

- `observations.md` >50 entries → `glacier/{domain}/observations-{tag}.md` (group by primary tag)
- `system/self-observations.md` >50 entries → `glacier/system/observations-{tag}.md`
- `action-items.md` >10 completed → `glacier/{domain}/action-items-done.md`
- `entities.md` >150 lines → inactive 6mo+ to `glacier/{domain}/entities-inactive.md` (leave stub)
- `system/improvements.md` >10 implemented → `glacier/system/improvements-done-{YYYY}.md`
- When a single tag file exceeds 50 entries, split by year: `observations-{tag}-{YYYY}.md`

## Pipeline

The module includes pipeline skills that maintain memory health:

| Skill | Purpose | Suggested schedule |
|-------|---------|-------------------|
| loom-memory-housekeeping | Archive, prune, link audit, glacier index | Weekly or nightly |
| loom-memory-reflect | Condense patterns, detect threads, tighten memory | Weekly or nightly |

These are optional. The module works without them. But running them regularly keeps memory clean and surfaces insights you'd miss.

## Mechanizable Helpers

Deterministic helpers may validate the module shape, scan L0 summaries, rebuild the glacier index, and rebuild the link index.

Helpers should not invent new memory ontology beyond what this appendix states.
