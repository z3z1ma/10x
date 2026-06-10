# Design Room: Sidebar UX - Temporal Records + Initial State

Status: done
Created: 2026-05-26
Updated: 2026-05-26

Legacy note: Risk — low - frontend-only UI changes

Priority: high - sidebar is the primary navigation and currently shows too much

## Summary

The sidebar has two UX problems that get worse with scale:

1. **Temporal records (tickets, plans, research, evidence, audit) show ALL items
   regardless of count.** With 50+ tickets, this is an unscrollable wall. Records
   with dates in their filenames (YYYYMMDD-*) should show the most recent N (10)
   with a "Show N more" expand button. The section count in the header still shows
   the total.

2. **Initial sidebar state has everything expanded.** This overwhelms the operator
   on first load. The correct default: only Specs expanded (since those are the
   stable reference documents operators check most). Everything else starts
   collapsed. The operator expands what they need.

## Scope

### Fix 1: Temporal record truncation (`GraphSidebar.svelte`)

For surfaces where records have temporal filenames (tickets, plans, research,
evidence, audit), sort by date descending and show only the most recent 10:

```typescript
const TEMPORAL_SURFACES = new Set(['tickets', 'plans', 'research', 'evidence', 'audit']);
const INITIAL_SHOW_COUNT = 10;

// Per-section state:
let showAllMap = $state<Record<string, boolean>>({});

// When rendering a section:
function visibleNodes(surface: string, nodes: TreeNode[]): TreeNode[] {
  if (!TEMPORAL_SURFACES.has(surface)) return nodes;
  
  // Sort by date (extract YYYYMMDD from filename/ID)
  const sorted = [...nodes].sort((a, b) => {
    const dateA = extractDate(a.record);
    const dateB = extractDate(b.record);
    return dateB.localeCompare(dateA);  // newest first
  });
  
  if (showAllMap[surface]) return sorted;
  return sorted.slice(0, INITIAL_SHOW_COUNT);
}

function extractDate(record: LoomRecord): string {
  // Extract YYYYMMDD from path or ID
  const match = (record.path || record.metadata.id || '').match(/(\d{8})/);
  return match ? match[1] : '00000000';
}
```

The "Show more" button:
```svelte
{#if TEMPORAL_SURFACES.has(surface) && !showAllMap[surface] && totalCount > INITIAL_SHOW_COUNT}
  <button onclick={() => showAllMap[surface] = true}
    class="w-full text-center py-1.5 text-[10px] text-accent-primary hover:text-accent-primary-hover">
    Show {totalCount - INITIAL_SHOW_COUNT} more
  </button>
{/if}
```

Section header always shows total: `TICKETS 47 ▼` (not the truncated count).

### Fix 2: Default collapsed state

Change the initial `expandedSections` set to only include `specs`:

```typescript
// Before:
let expandedSections = $state(new Set(['specs', 'plans', 'tickets', 'research', 'knowledge', 'evidence', 'audit', 'constitution']));

// After:
let expandedSections = $state(new Set(['specs']));
```

On first load, operator sees:
- SPECS ▼ (expanded, showing spec records)
- PLANS ▶ 3 (collapsed, showing count)
- TICKETS ▶ 47 (collapsed, showing count)
- RESEARCH ▶ 5 (collapsed, showing count)
- KNOWLEDGE ▶ 8 (collapsed, showing count)
- ... etc

This is clean and calm. The operator clicks what they need.

### Additional: Sort non-temporal records alphabetically

Specs, knowledge, constitution: sort alphabetically by title for predictable ordering.

## Acceptance

- ACC-001: Tickets section (expanded) shows only 10 most recent with "Show N more" button
  - Evidence: Expand tickets section → 10 items visible + "Show 37 more" button
  - Audit: Verify newest tickets are shown (sorted by date in filename)

- ACC-002: Clicking "Show N more" expands to show all records in that section
  - Evidence: Click "Show 37 more" → all 47 tickets now visible, button disappears
  - Audit: Verify scroll position doesn't jump

- ACC-003: Section header always shows total count regardless of truncation state
  - Evidence: Collapsed tickets section shows "TICKETS 47 ▶"
  - Audit: Count matches actual number of ticket records

- ACC-004: On first load, only Specs section is expanded; all others are collapsed
  - Evidence: Fresh page load screenshot showing Specs expanded, everything else collapsed with counts
  - Audit: Verify localStorage is not pre-populated on first visit

- ACC-005: Non-temporal records (specs, knowledge) are sorted alphabetically
  - Evidence: Specs section shows records in A-Z order by title
  - Audit: Compare against alphabetical sort of spec titles

## Journal

- 2026-05-26: Created. The current "show everything" approach doesn't scale.
  Temporal truncation + smart defaults make 100+ records manageable.
