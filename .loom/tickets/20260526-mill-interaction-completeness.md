# Mill Interaction Completeness: Wire Dead Buttons, Fix Error States

ID: ticket:20260526-mill-interaction-completeness
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - wiring existing events and adding error handling to existing fetches

Priority: high - dead buttons destroy user trust immediately
Depends On: ticket:20260526-mill-foundation-fixes

## Summary

Multiple interactions in the UI are dead or fragile:

1. **Dead "View Workstation" in AndonBoard**: Dispatches `open-playback` custom
   event but nothing listens for it. Should navigate to the workstation and select
   its detail panel.
2. **Dead "View History" in WorkstationControls**: Same `open-playback` dispatch
   with no handler. Should switch to the iterations tab for that workstation.
3. **Fetch error wedging**: Multiple components (WorkstationControls, HarnessConfig,
   IterationsTab, Playback, ReadyTicketRow, AndonBoard) have fetch calls that can
   leave the UI in a permanent loading/busy state on network error.
4. **No connection status banner**: When WebSocket disconnects, the only indicator
   is an 8px dot changing from green to red. Operators need an unmistakable banner.
5. **Andon "Clear resolved" mutates local state**: Should call an API endpoint or
   at minimum properly update the store, not silently mutate a prop-backed array.

Single closure claim: Every clickable element performs its advertised action, every
network error shows user-visible feedback with retry affordance, and the connection
status is always unambiguous.

## Related Records

- `plan:20260526-mill-production-readiness` - parent plan
- `ticket:20260526-mill-foundation-fixes` - provides centralized API + error patterns

## Scope

### Must Change

- `loom-mill/frontend/src/App.svelte` - Add handler for `open-playback` events:
  set `selectedWorkstationId` and optionally switch DetailPanel tab. Add a
  connection status banner component that appears on disconnect.

- `loom-mill/frontend/src/lib/ConnectionBanner.svelte` - New component: a full-width
  amber/red banner below the header showing "Reconnecting... (attempt 3/10)" or
  "Disconnected. Retrying in 8s." or "Connection lost. Click to retry." Uses the
  `store.connected`, `store.reconnecting`, `store.error` states from the resilient
  WebSocket (Unit 1).

- `loom-mill/frontend/src/lib/AndonBoard.svelte` - Fix `open-playback` to dispatch
  a proper event that App.svelte handles (or call a shared navigation function).
  Fix "Clear resolved" to properly filter the store's andon_events rather than
  mutating a local copy.

- `loom-mill/frontend/src/lib/WorkstationControls.svelte` - Fix "View History"
  button to navigate to that workstation's iterations tab.

- `loom-mill/frontend/src/lib/HarnessConfig.svelte` - Add try/catch around fetches
  with user-visible error toast on failure. Reset loading state on error.

- `loom-mill/frontend/src/lib/IterationsTab.svelte` - Add error handling with
  "Failed to load iterations. Retry?" message. Reset loading state on error.

- `loom-mill/frontend/src/lib/Playback.svelte` - Add error handling. Show error
  state instead of infinite spinner.

- `loom-mill/frontend/src/lib/ReadyTicketRow.svelte` - Add error handling on the
  start-workstation fetch. Show error feedback and reset button state.

- `loom-mill/frontend/src/lib/WorkstationRow.svelte` - Add error handling on
  action fetches (pause, resume, stop, dismiss).

### Must Not Change

- WebSocket protocol (Unit 1 handles transport)
- Left panel structure
- Backend API contracts

### Non-Goals

- Retry logic inside components (rely on user clicking retry)
- Offline mode or request queuing
- New backend endpoints

## Acceptance

- ACC-001: AndonBoard "View Workstation" button selects that workstation in the left panel and shows its detail
  - Evidence: Playwright test or manual: click "View Workstation" on an andon alert → left panel highlights workstation, detail panel shows its logs
  - Audit: Trace the event path from AndonBoard dispatch to App.svelte handler

- ACC-002: WorkstationControls "View History" switches to iterations tab
  - Evidence: Click "View History" → DetailPanel activeTab becomes 'iterations'
  - Audit: Verify the handler sets the correct tab state

- ACC-003: All fetch calls handle errors without wedging loading state
  - Evidence: Kill backend, click "Start" on a ready ticket → button resets, error toast appears. Same for pause/resume/stop/dismiss/harness test.
  - Audit: Code review showing try/catch/finally pattern on every fetch

- ACC-004: Connection banner appears within 2 seconds of WebSocket disconnect
  - Evidence: Kill backend → amber banner appears showing "Reconnecting..." with attempt count
  - Audit: Visual inspection and timing verification

- ACC-005: Connection banner shows "Connection lost" with retry button after max retries
  - Evidence: Keep backend down for 10+ reconnection attempts → banner changes to permanent disconnect with manual retry
  - Audit: Verify state transition from reconnecting to error

- ACC-006: Andon "Clear resolved" properly updates store state (not local mutation)
  - Evidence: Clear resolved alerts → they don't reappear on next WebSocket snapshot
  - Audit: Code review showing store mutation instead of local array splice

## Current State

All interactions have been wired and error handling added.
- `ConnectionBanner.svelte` created and integrated into `App.svelte`.
- `open-playback` event handled in `App.svelte` to navigate to workstation and select correct tab.
- `AndonBoard` "Clear resolved" uses `store.clearAndonEvents`.
- `try/catch/finally` added to all fetch calls across components.
- Playwright verification completed and evidence recorded.

Ready for review.

## Journal

- 2026-05-26: Created ticket with Status `open`. Audit found 2 dead button paths
  (open-playback), 8 unguarded fetch sites, and no connection banner beyond an
  8px indicator dot.
- 2026-05-26: Implemented all fixes. Created `ConnectionBanner.svelte`, wired `open-playback` in `App.svelte`, fixed Andon clear, and added `try/catch/finally` to all fetch calls. Verified with Playwright. Status changed to `review`.
