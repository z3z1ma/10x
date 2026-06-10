# Mill Pipeline UI

Status: done
Created: 2026-05-25
Updated: 2026-05-25
Depends-On: .loom/tickets/done/20260525-mill-watcher.md

Legacy note: Risk — low - frontend rendering of known state shape with no execution side effects.

## Summary

Svelte 5 frontend receives graph state via WebSocket from the backend, renders a ticket pipeline grouped by status (shaped/open → active → blocked → review → closed), shows related evidence/audit records when discoverable, shows recent git changes, and updates live without full page reload.

## Related Records

- `.loom/tickets/20260525-factory-floor-mvp.md` - parent plan, Unit 4.
- `.loom/specs/loom-mill-factory-floor-mvp.md` REQ-003, REQ-012 - pipeline view and tech stack.
- `.loom/research/20260524-loom-mill-software-factory.md` Finding 5 - Tab 2 layout: pipeline top, active detail, backpressure panel, controls.

## Scope

Read scope:
- State model types from Unit 3 (defines the WebSocket message shape).
- Factory Floor layout from research (pipeline + detail + signals).

Write scope:
- `loom-mill/frontend/src/` Svelte components for pipeline view.
- `loom-mill/src/loom_mill/api/` WebSocket endpoint that pushes state model snapshots and deltas.
- Tailwind styling for control-room aesthetic.

Non-goals:
- No execution controls (start/pause/stop) in this ticket; those are Unit 6.
- No harness config UI.
- No backpressure/andon display (Unit 9).
- No inter-iteration summary display (Unit 8).
- No Design Office / shaping UI.

Stop conditions:
- Stop if WebSocket message size for a 100+ record workspace is too large for responsive updates (route to pagination/virtualization research).

## Acceptance

- ACC-001: Dashboard renders tickets grouped by status columns/lanes, with ticket ID, title (first heading), status, and updated date visible.
  Evidence: screenshot or Playwright snapshot showing fixture graph rendered correctly.

- ACC-002: Related evidence and audit records are visible as linked indicators on the relevant ticket when the parser discovered those references.
  Evidence: screenshot showing a ticket with evidence/audit indicators from fixture data.

- ACC-003: Recent git state (branch, last few commits, dirty indicator) is visible in the dashboard.
  Evidence: screenshot showing git state panel.

- ACC-004: UI updates live when a `.loom/` record changes without requiring page refresh.
  Evidence: integration test or manual evidence showing file write → UI update within 2 seconds.

## Current State

Not started. Blocked on watcher + WebSocket API (Unit 3).

## Journal

- 2026-05-25: Created from `.loom/tickets/20260525-factory-floor-mvp.md` Unit 4.
