# Design Room Graph Hierarchy + Search

Status: done
Created: 2026-05-26
Updated: 2026-05-26
Depends-On: .loom/tickets/done/20260526-mill-dr-critical-fixes.md

Legacy note: Risk — low - tree data structure from existing record metadata

## Summary

Redesign the graph sidebar from flat lists into a true hierarchical tree with
search, expand/collapse, relationship nesting, and the ability to handle hundreds
of records without becoming unusable.

The current sidebar is just `records.filter(r => r.surface === 'tickets')` rendered
as a flat list. With 50+ tickets it's already a wall of text. The vision is a
navigable tree where plans show their child tickets nested below, specs show citing
tickets, and the whole thing is searchable and collapsible.

## Scope

### 1. Search Input

Add a search input at the very top of the sidebar:
- Placeholder: "Search records..."
- Filters all sections by title, ID, slug, or status
- Debounced (150ms) to avoid jank on fast typing
- Shows "No results" with clear button when nothing matches
- Cmd+Shift+F focuses the search from anywhere in Design Room

### 2. Hierarchical Tree Structure

Derive a tree from record metadata:
- **Plans** show their child tickets nested (match via ticket's `Depends On: .loom/tickets/<ticket-slug>.md` or plan's execution units referencing tickets)
- **Specs** show tickets that reference them (match via ticket references containing `.loom/specs/<spec-slug>.md`)
- **Tickets** that depend on other tickets show under their parent
- **Orphan records** (no parent relationship) appear at the top level of their surface section

Implementation:
```typescript
function buildTree(records: LoomRecord[]): TreeNode[] {
  // Group by surface
  // For each plan, find tickets that depend on it
  // For each spec, find tickets that reference it
  // Nest child tickets under their parent
  // Return hierarchical structure
}

interface TreeNode {
  record: LoomRecord;
  children: TreeNode[];
  expanded: boolean;
  depth: number;
}
```

### 3. Expand/Collapse

- Nodes with children show a chevron (▶ collapsed, ▼ expanded)
- Click chevron to toggle
- Default: surface sections expanded, individual parent nodes collapsed
- Remember expand state across sessions (localStorage)
- Expand/collapse all via right-click context menu or keyboard shortcut

### 4. Visual Hierarchy

- Each level indented 16px
- Subtle vertical connector lines (1px, border-color) from parent to last child
- Parent nodes show child count badge: `Plan: Factory Floor (9)`
- Alternating subtle background on depth levels for readability

### 5. Section Counts

Each surface section header shows: `Tickets (12/47)` when filtered (showing 12 of 47 total).

### 6. Pinned Records

- Right-click → "Pin to top"
- Pinned section at very top of sidebar (above search)
- Max 5 pins
- Stored in localStorage
- Unpin via right-click or × on pin

### 7. Smooth Animations

- Expand/collapse: animate height (200ms)
- Filter results: fade in/out (100ms)
- New record appears: slide in from left (150ms)

## Acceptance

- ACC-001: Search input filters records by title/ID across all sections
- ACC-002: Plans show child tickets nested below with indentation
- ACC-003: Expand/collapse works on parent nodes; state persists in localStorage
- ACC-004: Connector lines show parent-child relationships visually
- ACC-005: Section counts show filtered/total when search is active
- ACC-006: Right-click "Pin" adds record to pinned section at top
- ACC-007: Tree handles 100+ records without visible lag

## Journal

- 2026-05-26: Created. Current flat list is the most obvious UX gap in the
  Design Room. Real hierarchy derived from depends_on and references metadata.
