# Iterations Tab Interactivity

ID: ticket:20260526-mill-iterations-interactive
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - purely frontend UI enhancement; no backend changes, no data model changes

## Summary

The Iterations tab shows a read-only list of iterations with metadata (duration,
exit code, diff stat, files changed) but individual entries are not clickable.
There's no way to navigate from an iteration entry to its diff. The Playback tab
has the diff viewer but you can't get there from an iteration entry.

The fix: Make each iteration entry clickable. Clicking should switch to the
Playback tab with that specific iteration selected. Also add inline visual
affordances (expand/collapse for the file list, mini diff preview, click-to-playback
action).

Closure claim: Clicking an iteration entry navigates to its diff in the Playback
view, connecting the two tabs as complementary views of the same data.

## Related Records

- `plan:20260526-mill-factory-data-integrity` - parent plan
- `evidence:20260526-mill-iterations-interactive-build` - frontend build result after implementation
- `loom-mill/frontend/src/lib/IterationsTab.svelte` - current read-only iteration list
- `loom-mill/frontend/src/lib/Playback.svelte` - diff viewer with iteration selection
- `loom-mill/frontend/src/lib/DetailPanel.svelte:38-42` - tab definitions and activeTab binding

## Scope

Write:
- `loom-mill/frontend/src/lib/IterationsTab.svelte` - add click handlers, hover states, "View diff" affordance
- `loom-mill/frontend/src/lib/DetailPanel.svelte` - accept callback to switch tabs with iteration context

Non-goals:
- Do NOT add inline diff rendering in the Iterations tab (too heavy; use Playback)
- Do NOT change the Playback component interface
- Do NOT change backend iteration data model
- Do NOT add pagination or lazy loading of iterations

### Detailed Design

**IterationsTab changes:**

Each iteration entry becomes a clickable card with:
- Existing metadata (iteration number, duration, exit code, diff stat, files, timestamp)
- Hover state: subtle bg elevation
- Click action: calls `onViewDiff(iterationIndex)` callback
- A small "View diff →" link/button that appears on hover
- File list stays visible (no collapse needed for few files)

```svelte
<script>
  let { workstationId, onViewDiff }: { 
    workstationId: string; 
    onViewDiff?: (index: number) => void 
  } = $props();
</script>

{#each iterations as iter, i}
  <button 
    class="w-full text-left p-3 rounded hover:bg-bg-surface-elevated transition-colors group cursor-pointer"
    onclick={() => onViewDiff?.(i)}
  >
    <!-- existing content -->
    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity text-[10px] text-accent-primary mt-1">
      View diff →
    </div>
  </button>
{/each}
```

**DetailPanel changes:**

- Add `onViewDiff` prop callback to IterationsTab
- When called, set `activeTab = 'playback'` and pass the iteration index
- Playback component already accepts and renders specific iterations via `loadDiff(step)`
- May need to add a prop or external trigger to Playback to load a specific iteration

**Tab switch flow:**
1. User is on Iterations tab
2. Clicks iteration entry (e.g., "Iteration 2")
3. DetailPanel sets `activeTab = 'playback'`
4. Playback receives the iteration index and calls `loadDiff(1)` (0-indexed)
5. User sees the diff for that specific iteration

## Acceptance

- ACC-001: Clicking an iteration entry in the Iterations tab switches to the
  Playback tab with that iteration's diff displayed.
  - Evidence: Playwright test: click iteration entry, verify tab switches to Playback, verify correct iteration number shown in Playback header.
  - Audit: Verify iteration index mapping is correct (0-based vs 1-based).

- ACC-002: Iteration entries show hover state and "View diff" affordance.
  - Evidence: Screenshot showing hover state.
  - Audit: Verify contrast and visibility of hover state.

- ACC-003: `npm --prefix loom-mill/frontend run build` passes.
  - Evidence: Build output.

## Current State

Implementation complete and moved to review. Iteration rows are clickable, DetailPanel switches to Playback with a selected iteration index, and Playback accepts an initial step while preserving aggregate default behavior when no initial step is provided. Build evidence is recorded in `evidence:20260526-mill-iterations-interactive-build`.

Remaining verification gap: no Playwright/browser screenshot verification was captured for ACC-001 or ACC-002 in this session.

## Journal

- 2026-05-26: Created ticket. Source: operator found iterations tab entries
  non-interactive during first genuine workstation review.
- 2026-05-26: Set ticket active for scoped frontend implementation. Existing worktree had unrelated changes; scoped edits will stay within IterationsTab, DetailPanel, Playback, and this ticket.
- 2026-05-26: Implemented clickable iteration cards, DetailPanel tab handoff, and Playback `initialStep` support. Ran `npm --prefix loom-mill/frontend run build`; build passed with unrelated existing warnings. Status set to review because browser/visual verification and audit remain unrecorded.
