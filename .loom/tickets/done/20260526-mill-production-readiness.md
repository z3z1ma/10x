# Mill UI Production Readiness

Status: done
Created: 2026-05-26
Updated: 2026-05-26

Legacy note: Risk — medium - 6 execution units touching shared frontend state; type changes in Unit 1 affect all downstream units

## Summary

The Loom Mill frontend is structurally complete but has 13 material gaps between
current state and production-ready. These range from deployment blockers (hardcoded
backend URL), user-facing stubs ("Full record rendering is future work"), dead
interactions, fragile error handling, accessibility failures, and missing control
room essentials like search, keyboard shortcuts, and notification history.

This plan decomposes the full production-readiness push into 6 ordered execution
units. When complete, every interaction works, every state is handled, the UI is
accessible and responsive, and the control room provides the dense/calm Linear-like
experience operators need to run autonomous agents at scale.

## Related Records

- `.loom/tickets/20260525-production-factory-floor.md` - completed Factory Floor plan; this is the polish pass
- `.loom/specs/mill-factory-floor.md` - production spec for the Factory Floor
- `.loom/tickets/done/20260525-mill-ticket-lifecycle-panel.md` - completed lifecycle panel (immediate predecessor)
- `.loom/knowledge/frontend-expert-agent-preferences.md` - agent dispatch preferences

## Strategy

The route is ordered by dependency: foundation fixes enable everything downstream.
Type safety and URL configuration must land before record rendering or interaction
work can trust the data layer. Record rendering is the single biggest feature gap
visible to operators. Interaction completeness eliminates dead buttons and error
states. Accessibility and keyboard support make the tool usable for power users.
Responsive layout ensures it works across viewports. Polish adds the control room
essentials that distinguish production from prototype.

Units 1-3 are strictly sequential. Units 4-6 can partially parallelize after Unit 3
lands, since they touch orthogonal concerns (accessibility, layout, features).

Recovery: If Unit 1 type changes break downstream units, those units should read
the updated types.ts before starting. If Unit 2 (record rendering) reveals backend
gaps in the record payload, a backend sub-ticket should be filed and resolved
before the frontend work proceeds.

Server startup pattern for all subagent work:
```bash
# Backend
pkill -f 'uvicorn.*loom_mill' || true
cd /Users/alexanderbutler/code_projects/personal/agent-loom
source loom-mill/.venv/bin/activate
nohup python -m uvicorn loom_mill.app:app --host 127.0.0.1 --port 8765 > /tmp/loom-mill-backend.log 2>&1 < /dev/null &

# Frontend
pkill -f 'vite.*loom-mill' || true
cd /Users/alexanderbutler/code_projects/personal/agent-loom/loom-mill/frontend
nohup npm run dev > /tmp/loom-mill-vite.log 2>&1 < /dev/null &
sleep 3
```

## Execution Units

### Unit 1: Foundation Fixes

Ticket: .loom/tickets/done/20260526-mill-foundation-fixes.md

Fix the deployment-blocking hardcoded port, complete the TypeScript types to match
actual runtime payloads, and make the WebSocket connection resilient with exponential
backoff, max retries, error boundaries, and graceful degradation. This is the
substrate all other units build on.

Closure claim: The frontend builds with strict types, connects to any backend URL
via configuration, and handles WebSocket failures gracefully without crashing or
wedging.

### Unit 2: Ticket Record Rendering

Ticket: .loom/tickets/done/20260526-mill-record-rendering.md

Replace the "future work" stub in DetailPanel with a full Markdown-based ticket
record renderer. When a non-workstation ticket is selected, render its full content:
title, metadata badges, acceptance criteria, headings, body text, references, and
status timeline. This is the single biggest feature gap visible to operators.

Closure claim: Selecting any ticket in the left panel shows its complete record
content in the detail panel with proper formatting, metadata display, and section
navigation.

### Unit 3: Interaction Completeness

Ticket: .loom/tickets/done/20260526-mill-interaction-completeness.md

Wire every dead button, fix every fetch error state, add a visible connection
status banner on disconnect, and ensure no interaction leaves the UI in an
unrecoverable state. The Andon board "View Workstation" must navigate to that
workstation. Controls "View History" must switch to iterations tab. Every fetch
must handle errors with user-visible feedback.

Closure claim: Every clickable element in the UI performs its advertised action,
every network error shows user feedback, and the connection status is always
unambiguous.

### Unit 4: Accessibility + Keyboard

Ticket: .loom/tickets/done/20260526-mill-accessibility-keyboard.md

Full ARIA semantics, focus management, keyboard navigation (j/k list nav, Escape
to deselect, Enter to select, Tab order), focus trapping in drawers/modals, screen
reader announcements for toasts and state changes, and a Cmd+K command palette for
power users.

Closure claim: The UI is fully operable via keyboard alone, passes ARIA landmark
checks, traps focus in overlays, announces dynamic content, and provides a command
palette for rapid navigation.

### Unit 5: Responsive Layout

Ticket: .loom/tickets/done/20260526-mill-responsive-layout.md

Collapse the sidebar on narrow viewports (<1024px becomes overlay, <768px becomes
full-width with back-navigation). The detail panel and settings drawer adapt
gracefully. No horizontal scroll, no overflow clipping, no broken interactions at
any viewport width from 375px to 2560px.

Closure claim: The UI is usable and visually correct at 375px, 768px, 1024px,
1440px, and 2560px viewport widths with no content clipping or broken interactions.

### Unit 6: Polish + Control Room

Ticket: .loom/tickets/done/20260526-mill-polish-control-room.md

Search/filter in the left panel, notification center (bell icon with event history
that persists beyond toast lifetime), smooth transitions on all mount/unmount/tab
switches, and refined animation timing. The control room should feel dense, calm,
and responsive - every state change animated, every list filterable, every past
event retrievable.

Closure claim: Left panel has working search, notifications persist in a
reviewable center, all transitions are smooth, and the overall experience matches
Linear's density and calm.

## Milestones

### Milestone: Solid Foundation

Child tickets: .loom/tickets/done/20260526-mill-foundation-fixes.md

The frontend builds with strict types, connects to configurable backend, and
handles failures gracefully. All downstream units can trust the data layer.

### Milestone: Feature Complete

Child tickets: .loom/tickets/done/20260526-mill-record-rendering.md, .loom/tickets/done/20260526-mill-interaction-completeness.md

Every feature works. No stubs, no dead buttons, no "future work" text anywhere in
the UI. Operators can see all ticket content and interact with every control.

### Milestone: Production Ready

Child tickets: .loom/tickets/done/20260526-mill-accessibility-keyboard.md, .loom/tickets/done/20260526-mill-responsive-layout.md, .loom/tickets/done/20260526-mill-polish-control-room.md

The UI is accessible, responsive, polished, and provides control room essentials.
Ready for daily operator use across devices and preferences.

## Current State

All 6 execution units completed and committed. Frontend builds clean (155.14 kB JS,
40.78 kB CSS, 138 modules). Backend tests pass (49 passed). No "future work" text,
no hardcoded ports, full accessibility, responsive from 375px-2560px, search,
notification center, and smooth transitions throughout.

## Journal

- 2026-05-26: Created plan with Status `open`. Derived from comprehensive frontend
  audit identifying 13 production gaps across 4 severity tiers. Operator approved
  the decomposition and prioritization.
- 2026-05-26: Unit 1 completed (e255868). URL config, types, WebSocket resilience.
- 2026-05-26: Unit 2 completed (5e76b3f). Record rendering endpoint + RecordRenderer + MetadataBadges.
- 2026-05-26: Unit 3 completed (5ad7a27). ConnectionBanner, error handling, navigation wiring.
- 2026-05-26: Units 4+5+6 completed (9a34788). Accessibility, responsive, search, notifications, transitions.
- 2026-05-26: All milestones satisfied. Set Status `completed`.
