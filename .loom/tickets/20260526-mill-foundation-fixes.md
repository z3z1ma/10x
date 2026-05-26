# Mill Foundation Fixes: URL Config, Types, WebSocket Resilience

ID: ticket:20260526-mill-foundation-fixes
Type: Ticket
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - type changes touch every component; WebSocket changes affect real-time state

Priority: high - blocks all downstream production-readiness work

## Summary

The Mill frontend has three foundational defects that must be fixed before any
production deployment or downstream polish work:

1. **Hardcoded backend URL**: The port `8765` is hardcoded in 8+ files. Any
   deployment where the backend isn't exactly `localhost:8765` breaks entirely.
2. **Incomplete TypeScript types**: `WorkstationState` is missing fields that are
   actually used at runtime (`ticket_id`, `ticket_slug`, `finished`, `conflict`).
   Components access these fields without type safety.
3. **Fragile WebSocket**: Bare `JSON.parse` with no error boundary, fixed 2-second
   reconnect with no backoff or max retries, and no handling of partial messages or
   connection state edge cases.

Single closure claim: The frontend builds with strict types matching actual runtime
payloads, connects to any backend via environment-driven configuration, and handles
WebSocket failures gracefully.

## Related Records

- `plan:20260526-mill-production-readiness` - parent plan
- `.loom/specs/mill-factory-floor.md` - defines the WebSocket protocol and events

## Scope

### Must Change

- `loom-mill/frontend/src/lib/types.ts` - Add `ticket_id`, `ticket_slug` to
  `WorkstationState`. Add `finished` and `conflict` to `WorkstationStatus` union.
  Ensure all fields used across components are typed.
- `loom-mill/frontend/src/lib/ws.svelte.ts` - Replace hardcoded `:8765` with
  configurable base URL. Add exponential backoff (1s, 2s, 4s, 8s, 16s cap). Add
  max retry counter (display permanent disconnect after 10 failures). Wrap
  `JSON.parse` in try/catch. Add `error` state to store. Add `reconnecting` state
  with attempt count.
- `loom-mill/frontend/src/lib/AndonBoard.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/HarnessConfig.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/IterationsTab.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/Playback.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/ReadyTicketRow.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/WorkstationControls.svelte` - Use shared API base URL.
- `loom-mill/frontend/src/lib/WorkstationRow.svelte` - Use shared API base URL.
- Create `loom-mill/frontend/src/lib/api.ts` - Centralized API configuration:
  ```typescript
  export const API_BASE = import.meta.env.VITE_API_URL || 
    `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;
  export const WS_BASE = import.meta.env.VITE_WS_URL ||
    `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.hostname}:${window.location.port}`;
  ```
  When no env vars are set and the frontend is served from the same origin as the
  backend (production), use relative URLs. When env vars are set (dev), use those.

### Must Not Change

- Backend API contract (no new endpoints needed)
- Component rendering logic (only URL construction changes)
- WebSocket message protocol (only transport resilience)

### Non-Goals

- Adding new API endpoints
- Changing the WebSocket event schema
- Adding authentication or CORS changes

## Acceptance

- ACC-001: No hardcoded port or host string exists anywhere in `loom-mill/frontend/src/`
  - Evidence: `grep -r '8765' loom-mill/frontend/src/` returns zero results
  - Audit: Code review of the new `api.ts` module and all import sites

- ACC-002: `WorkstationState` in `types.ts` includes `ticket_id: string`, `ticket_slug: string`, and `WorkstationStatus` includes `'finished' | 'conflict'`
  - Evidence: `npm --prefix loom-mill/frontend run build` passes with no type errors
  - Audit: Verify types match the backend's actual `WorkstationState` pydantic model

- ACC-003: WebSocket uses exponential backoff starting at 1s, doubling to 16s cap, with max 10 retries before showing permanent disconnect
  - Evidence: Disconnect backend, observe console logs showing backoff intervals; after 10 attempts, `store.error` is truthy
  - Audit: Code review of reconnection logic

- ACC-004: Malformed WebSocket messages do not crash the store
  - Evidence: Inject `ws.onmessage({data: 'not json'})` via console; store continues operating
  - Audit: Verify try/catch wraps JSON.parse

- ACC-005: Frontend builds clean with `npm --prefix loom-mill/frontend run build`
  - Evidence: Build output shows no errors or warnings
  - Audit: CI-equivalent local build

## Current State

Ready to start. First Ralph run should:
1. Create `api.ts` with centralized URL configuration
2. Update `types.ts` with complete types
3. Refactor `ws.svelte.ts` for resilience
4. Update all components to import from `api.ts`
5. Verify build passes

## Journal

- 2026-05-26: Created ticket with Status `open`. Derived from production audit
  finding hardcoded URLs in 8 files, type mismatches across 6 components, and
  unguarded WebSocket in ws.svelte.ts.
