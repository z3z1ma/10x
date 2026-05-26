# Mill Polish + Control Room: Search, Notifications, Transitions

ID: ticket:20260526-mill-polish-control-room
Type: Ticket
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - additive features on stable foundation

Priority: medium - distinguishes production from prototype; operator daily-use quality
Depends On: ticket:20260526-mill-interaction-completeness

## Summary

The final production pass adds control room essentials that transform a functional
UI into an operator's daily tool:

1. **Search/filter in left panel**: With 20+ tickets and workstations, operators
   need instant filtering by name, status, or tag.
2. **Notification center**: Toasts vanish after 4 seconds. If an operator steps
   away, they miss alerts entirely. A persistent notification center (bell icon)
   preserves all events for review.
3. **Smooth transitions**: Mount/unmount, tab switches, panel slides, toast
   enter/exit, list reordering - every state change should be animated with
   appropriate timing (fast for interactions, slow for ambient).
4. **Refined animation timing**: Loading states, skeleton content, progress
   indicators - the UI should feel alive even when waiting.

Single closure claim: Left panel has working search, notifications persist in a
reviewable center, all transitions are smooth, and the overall experience matches
Linear's density and calm.

## Related Records

- `plan:20260526-mill-production-readiness` - parent plan
- `ticket:20260526-mill-interaction-completeness` - all interactions work before polish

## Scope

### Must Change

- `loom-mill/frontend/src/lib/WorkstationList.svelte` - Add search input at top of
  left panel. Filters tickets/workstations by:
  - Name/slug (fuzzy substring match)
  - Status (type status name to filter)
  - Free text across title and metadata
  Show "No results" with clear-filter affordance when filter eliminates all items.
  Preserve search state across selection changes.

- `loom-mill/frontend/src/lib/NotificationCenter.svelte` - New component:
  - Bell icon in header (next to settings gear)
  - Badge showing unread count
  - Click opens a dropdown/panel showing event history:
    - Workstation started/completed/stopped/failed
    - Andon alerts
    - Shipping events (merged/conflict)
    - Connection status changes
  - Each notification has timestamp, icon, message, and optional action ("View")
  - "Mark all read" button
  - Notifications persist in `localStorage` across page reloads
  - Max 100 notifications (oldest evicted)

- `loom-mill/frontend/src/App.svelte` - Integrate NotificationCenter in header.
  Route all toast events to also append to notification center. Add notification
  center open/close state.

- `loom-mill/frontend/src/lib/Toast.svelte` - Add enter/exit transitions:
  - Enter: slide in from top-right + fade in (200ms ease-out)
  - Exit: slide out to right + fade out (150ms ease-in)
  - Stack toasts vertically with 8px gap
  - Auto-dismiss timer shown as a shrinking progress bar at bottom of toast

- `loom-mill/frontend/src/lib/DetailPanel.svelte` - Add crossfade transition on
  tab content change. Content should fade out/in (100ms) rather than hard-swap.

- `loom-mill/frontend/src/lib/WorkstationList.svelte` - Add list transition:
  items entering the list slide in from left (150ms), items leaving slide out to
  right (100ms). Reordering should animate position changes (200ms).

- `loom-mill/frontend/src/lib/SettingsDrawer.svelte` - Drawer slide-in should be
  250ms ease-out with backdrop fade. Slide-out 200ms ease-in.

- `loom-mill/frontend/src/lib/ConnectionBanner.svelte` (from Unit 3) - Add
  slide-down enter (200ms) and slide-up exit (150ms) transitions.

- `loom-mill/frontend/src/app.css` - Add CSS transition utilities:
  ```css
  .transition-slide-in { ... }
  .transition-fade { ... }
  .transition-scale { ... }
  ```
  Add animation keyframes for loading states and skeleton content.

### Must Not Change

- Core data flow (store/WebSocket/types)
- Component semantics (only visual additions)
- Backend

### Non-Goals

- Persisting search state across sessions (just in-memory)
- Notification preferences/muting (all notifications show)
- Sound/vibration alerts
- Complex animation sequencing (keep it simple and fast)

## Acceptance

- ACC-001: Typing in search input filters the left panel list in real-time
  - Evidence: Playwright: type "found" in search → only tickets/workstations with "found" in name visible; clear → all return
  - Audit: Verify filter logic handles empty states and special characters

- ACC-002: Notification center shows persistent event history
  - Evidence: Trigger 3 toasts (start workstation, stop workstation, andon alert) → open notification center → all 3 events visible with timestamps
  - Audit: Verify localStorage persistence by reloading page

- ACC-003: Notification badge shows unread count; "Mark all read" clears it
  - Evidence: 3 unread notifications → badge shows "3"; click "Mark all read" → badge disappears
  - Audit: Verify count updates in real-time as new events arrive

- ACC-004: Toast enter/exit animations are smooth (no flash, no jump)
  - Evidence: Playwright screenshot sequence showing toast sliding in, visible, sliding out
  - Audit: Visual inspection of animation timing

- ACC-005: Tab switch in DetailPanel uses crossfade (no hard content swap)
  - Evidence: Slow-motion observation (or transition timing inspection) shows fade between tabs
  - Audit: Verify CSS transition properties are applied

- ACC-006: Left panel list items animate on enter/exit
  - Evidence: Start a workstation → new row slides in smoothly from left
  - Audit: Verify Svelte transition directives are applied to list items

- ACC-007: All transitions complete within 250ms (no sluggish feel)
  - Evidence: Inspect CSS transition durations; none exceed 250ms
  - Audit: Verify no animation exceeds the timing budget

## Current State

Ready to start after Unit 3 lands. Can parallelize with Units 4 and 5 since it
touches different concerns (features/polish vs. accessibility vs. layout).

First Ralph run should:
1. Add search input to WorkstationList with filtering logic
2. Create NotificationCenter.svelte with localStorage persistence
3. Add transitions to Toast, DetailPanel tabs, WorkstationList items, SettingsDrawer
4. Integrate NotificationCenter in App.svelte header
5. Playwright verify: search, notifications, animations

## Journal

- 2026-05-26: Created ticket with Status `open`. These features transform the UI
  from "it works" to "I want to use this every day." Linear's magic is in the
  micro-interactions and the calm density of information.
