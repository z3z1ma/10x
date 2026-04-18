# loom-memory-housekeeping

Use this command to perform routine memory housekeeping. Trigger if the user
says "housekeeping", "clean up memory", "prune memory", or similar maintenance
requests.

This command is pure prompt guidance. It should be executable from the visible
memory files and normal file tools alone.

## Goal

Keep Loom's optional memory surface small, current, and clearly subordinate to
the canonical Loom layers.

## Orientation (run FIRST, before deep reads)

Use quick filesystem checks to scope the pass:

```bash
find .loom/memory -type f -name "*.md" 2>/dev/null | sort
rg -n '^<!-- L0:' .loom/memory 2>/dev/null
rg -n '^- ' .loom/memory/*/action-items.md .loom/memory/*/observations.md 2>/dev/null
```

Only read files that appear to need work.

## Housekeeping Pass

1. Prune hot memory.
   - Keep every `hot-memory.md` short and high-signal.
   - Move older supporting detail into `observations.md` when it still matters.
2. Check action items.
   - Remove or mark completed support tasks.
   - Move real execution work into Loom tickets instead of leaving it in memory.
3. Tighten entities.
   - Keep entity entries compact.
   - Add or fix `[[links]]` when they materially help retrieval.
4. Check boundaries.
   - Remove duplicated canonical truth from memory.
   - Point at the canonical Loom record instead when that is clearer.
5. Fix headers.
   - Add an `<!-- L0: ... -->` header to any active memory file missing one.

## Write Rules

- prefer direct file edits over inventing maintenance machinery
- keep memory files small and readable
- do not create archive systems or extra structure unless the repository
  already clearly uses them
- if a change would affect canonical project truth, update the owning Loom layer
  instead of hiding the fix in memory

## Debrief

Summarize:

- every file you modified
- what you pruned or clarified
- any support tasks moved out of memory
- any stale memory you left untouched and why

Never respond with only "Done".
