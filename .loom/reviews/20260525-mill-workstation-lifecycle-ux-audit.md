# Workstation Lifecycle UX Audit

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Target: .loom/tickets/20260525-mill-workstation-lifecycle-ux.md

## Summary

Ralph reviewed the workstation lifecycle UX implementation against the ticket acceptance criteria, related spec requirements, scoped source files, backend dismissal path, and available build evidence. The verdict is changes-needed because bulk clear currently deletes resumable stopped workstations, several visible controls call unregistered endpoints, and behavioral evidence for ACC-001 through ACC-004 is still missing.

## Target

The audit targeted `.loom/tickets/20260525-mill-workstation-lifecycle-ux.md` and the current scoped implementation in:

- `loom-mill/frontend/src/lib/WorkstationRow.svelte`
- `loom-mill/frontend/src/lib/WorkstationList.svelte`
- `loom-mill/frontend/src/lib/DetailPanel.svelte`
- `loom-mill/src/loom_mill/api/workstation.py`

## Audit Scope And Lenses

Scope: challenge the ticket closure claim and ACC-001 through ACC-005 against current source and available evidence.

Lenses: acceptance and scope, evidence sufficiency, implementation correctness and integration fit, UX edge states, and follow-through.

Out of scope: full visual design approval, new Playwright fixture authoring, and unrelated Mill frontend changes outside the ticket scope.

## Context And Evidence Reviewed

- Ralph review run: bounded read-only review of the ticket, spec, scoped frontend files, backend workstation API, routing integration, websocket removal handling, and manager teardown path.
- `.loom/tickets/20260525-mill-workstation-lifecycle-ux.md` - ticket acceptance, scope, and current state.
- `.loom/specs/mill-factory-floor.md` REQ-011 and REQ-016 - workstation panel and operator-control requirements.
- `loom-mill/frontend/src/lib/WorkstationRow.svelte` - state-gated row actions and duration display.
- `loom-mill/frontend/src/lib/WorkstationList.svelte` - completed grouping and clear-all behavior.
- `loom-mill/frontend/src/lib/DetailPanel.svelte` - state-specific detail panel messaging and duration display.
- `loom-mill/src/loom_mill/api/workstation.py` - `DELETE /workstations/{id}` behavior.
- `loom-mill/src/loom_mill/workstation/manager.py` - cleanup/removal path through `stop(remove=True)`.
- `loom-mill/frontend/src/lib/ws.svelte.ts` - frontend removal handling for deleted workstations.
- `npm --prefix loom-mill/frontend run build` - passed before audit, supports ACC-005 only.
- Scoped `git diff --check` - passed before audit for the ticket and scoped frontend files.

## Findings

### FIND-001: Clear All Completed Deletes Stopped Workstations

Severity: high. Confidence: high.

`completedWorkstations()` includes `state.status === 'stopped'` in `WorkstationList.svelte`, and `clearAllCompleted()` deletes every item in that group. The UI labels this group `Completed`, but the ticket separates stopped from completed: stopped rows should be resumable and dismissible, while completed rows belong in the completed section. This challenges ACC-002 and the lifecycle UX claim because a bulk "Clear all completed" can remove resumable stopped workstations.

Follow-up: exclude stopped workstations from the bulk completed group, or intentionally relabel and rescope the behavior before closure.

### FIND-002: Visible Row Actions Call Unregistered Endpoints

Severity: high. Confidence: high.

`WorkstationRow.svelte` posts non-dismiss actions to `/workstations/{workstationId}/{action}`. The app registers `/workstations/{workstation_id}/pause` and `/resume`, but not `/stop`, `/resolve`, or `/abort`; stop still exists only on a legacy ticket-based route, and resolve/abort are shipping routes. Visible Stop and conflict controls can therefore render as appropriate controls but fail when clicked, weakening ACC-003 and REQ-016.

Follow-up: fix action routing for Stop and conflict actions, or remove unsupported controls until correctly routed.

### FIND-003: Required Behavioral Evidence Is Missing

Severity: medium. Confidence: high.

ACC-001 through ACC-004 call for Playwright or screenshot/manual behavior proof, but no Playwright/manual live Mill fixture verification has been run. Build evidence supports ACC-005 only.

Follow-up: run live/manual or Playwright fixture verification for dismiss, clear-all, state-appropriate controls, and live/static duration behavior before closure.

## Verdict

changes-needed. The implementation is directionally aligned with the ticket, but it cannot honestly proceed to closure until the bulk-dismiss and action-routing issues are fixed and acceptance evidence is gathered.

## Required Follow-up

- Resolve FIND-001 before claiming ACC-002.
- Resolve FIND-002 before claiming ACC-003.
- Gather behavioral evidence for ACC-001 through ACC-004 before closure.
- Keep `npm --prefix loom-mill/frontend run build` as ACC-005 evidence after fixes.

## Residual Risk

Frontend TypeScript models appear stale for statuses such as `finished` and `conflict` and for `ticket_id`; Vite build does not typecheck this project. This is not by itself a closure blocker for the audited scope, but it increases regression risk for future frontend work.

## Related Records

- `.loom/tickets/20260525-mill-workstation-lifecycle-ux.md` - consuming ticket that owns finding disposition and closure.
