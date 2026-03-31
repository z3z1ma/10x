# Memory Housekeeping Workflow

## Goal

Keep `.loom/memories/` structurally trustworthy, small, and easy to navigate.

## Orientation (run FIRST)

Use shell commands to scope work before reading files:

```bash
# What changed since last run? Focus here first.
find .loom/memories/ -type f -name "*.md" -mtime -1 | sort

# Quick entry counts for archival threshold checks (>50 = archive)
grep -c "^- " .loom/memories/system/self-observations.md .loom/memories/user/observations.md 2>/dev/null

# Completed action items count (>10 = archive)
grep -c "^\- \[x\]" .loom/memories/user/action-items.md 2>/dev/null
```

Only read files that need work based on these results. Skip unchanged files.

## Garbage Collection

Archive stale data per the archival thresholds. Group observations by primary tag when archiving. All glacier files must have JSON-compatible frontmatter with `type`, `domain`, `tags`, `date_range`, `entries`, `summary`.

When archiving new entries to an existing glacier file, update the frontmatter: bump `entries`, extend `date_range`, update `tags`.

## Hot-Memory Pruning

Structural rules only — relevance judgment is reflect's job.

Priority order: resolved → past events → SSOT violations → stale (14+ days) → low-signal.

Where trimmed entries go: lasting value → `observations.md`. Purely historical → let them go. Never silently delete.

## Link Audit

For each non-glacier memory file:

1. Entity mentions: scan for names matching `### <Name>` headers in entities.md — add `[[links]]` if missing
2. Cross-domain references: if a file mentions a topic from another domain, add a cross-domain link
3. Action item references: if an observation references a task, link it

Only add links where the reference is substantive.

## Entity Registry Enforcement

1. **3-line max**: entries >3 content lines → compress or flag for thread promotion
2. **Glacier candidates**: `status: inactive` or `last:` date >6 months → move to `glacier/{domain}/entities-inactive.md` (leave stub)
3. **Missing metadata**: flag entries missing `status:` or `last:` fields

## Temporal Fact Maintenance

Scan entities for `(until YYYY-MM)` markers with past dates:

1. No ~~strikethrough~~ → add it
2. Already struck through → move to `## Historical` subsection
3. Report moved facts in debrief

## Index Rebuilds

Glacier index: scan all `glacier/**/*.md`, extract frontmatter, write catalog table.

Link index: scan all non-glacier memory files for `[[wiki-links]]`, record target → source, write backlink table.

## L0 Maintenance

Check all active memory files for missing `<!-- L0: ... -->` headers. If missing: read content, write a one-line summary (max 80 chars), add as first line.

## Archive Philosophy

Archive because the detail stopped being current, not because it stopped mattering.

Glacier is for retrievable history that should stay out of the hot path.

## Anti-Pattern

Do not turn housekeeping into reflection.

If the real work is to interpret repeated observations, switch to `loom-memory-reflect` instead of hiding that judgment inside a mechanical cleanup pass.
