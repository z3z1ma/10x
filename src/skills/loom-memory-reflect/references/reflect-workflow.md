# Memory Reflection Workflow

## Goal

Turn scattered supporting notes into sharper memory. Leave things better than you found them.

## Orientation (run FIRST)

Use shell commands to scope work before reading files:

```bash
# What changed since last run? Focus here.
find .loom/memories/ -type f -name "*.md" -mtime -1 | sort

# L0 summaries for all domains — quick routing
grep -rn "<!-- L0:" .loom/memories/ --include="*.md" | grep -v glacier/ | sort

# Entry counts for files approaching archival threshold (>50 = archive)
grep -c "^- " .loom/memories/system/self-observations.md .loom/memories/user/observations.md 2>/dev/null
```

Focus on recently-changed files. Skip files that haven't been modified since last run.

## Consistency Sweep

Systematic contradiction detection:

1. **Hot-memory vs canonical sources**: Read each domain's `hot-memory.md`. For every factual claim, read the canonical source file and verify. Fix hot-memory if stale. Canonical file always wins.
2. **Cross-file fact check**: Verify facts shared between files are consistent. More recent source wins; more specific source wins over summary.
3. **Temporal validity check**: Scan all `entities.md` for `(since YYYY-MM)` where date is >6 months ago — flag. Scan for `(until YYYY-MM)` not yet struck through — add strikethrough.
4. **Cross-domain entity check**: If the same entity appears in multiple `entities.md` files, ensure one is canonical and others are pointers.

## Condensation

Scan observations for clusters of 3+ entries on the same theme/tag:

- Distill into a pattern in `system/patterns.md`
- Don't delete the observations — they stay as the raw record
- Enforce pattern cap: **70 lines / 5.5KB** hard limit
- If near cap, compress (merge overlapping rules, drop examples, remove temporal data)
- Entries must be **timeless rules** — "what to do" not "what happened"

## Hot-Memory Relevance

- **Promote**: If a pattern is heating up → add to appropriate `hot-memory.md`
- **Demote**: If a hot-memory item has gone quiet (no references in 2+ weeks) → remove from hot-memory
- **Goal**: hot-memory = what matters *right now*

## Entity Registry Enforcement

1. **3-line check**: Any entry with >3 content lines → compress or flag for thread promotion
2. **Status/last fields**: Every entry should have `status: active|inactive` and `last: YYYY-MM-DD`
3. **Cross-domain pointers**: Same entity in multiple files → one canonical, others point with `see [[link]]`

## Thread Candidates

A thread candidate is a topic that keeps surfacing across observations over time. Topic appears across 3+ dates or spans 2+ weeks.

- Check if a thread already exists
- If not: "Thread candidate: [topic] — [N] fragments across [date range]"
- Don't auto-create threads — suggest them

## Proactive Synthesis

Cluster last 7 days of observations. If 5+ observations in one domain or on one topic → add "Synthesis Opportunities" to debrief suggesting thread raise or hot-memory update. Never auto-synthesize — suggest and let the user decide.

## Act On Findings

- New self-observations → append. **Cap: max 5 per reflect pass.** Merge lower-signal ones.
- Pattern updates → edit in place
- Improvement ideas → add to improvements.md
- Stale improvement ideas (>30 days) → archive or mark abandoned
- Entity data changed → update in place
- Ensure every file has an L0 header
- Add `[[wiki-links]]` where they add real context
- Apply write-time back-linking: when adding A→B, open B and add `[[A]]` if B gains context

## Good Outcomes

- fewer stale current-state notes
- more durable patterns
- less duplication across files
- compact entity entries
- thread candidates identified
- clearer separation between supporting memory and canonical truth
