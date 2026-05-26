# Mill Responsive Layout

ID: ticket:20260526-mill-responsive-layout
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - CSS-only changes with well-defined breakpoints

Priority: medium - control room is primarily desktop but must not break on other viewports
Depends On: ticket:20260526-mill-interaction-completeness

## Summary

The Mill UI has a fixed 320px sidebar, a fixed 400px settings drawer, and no
responsive breakpoints. On screens narrower than ~1200px, content clips or
overflows. On screens wider than ~1600px, the detail panel stretches awkwardly.
The layout must gracefully adapt from 375px (mobile, for monitoring on the go) to
2560px (ultrawide desktop) without breaking interactions or clipping content.

Single closure claim: The UI is usable and visually correct at 375px, 768px,
1024px, 1440px, and 2560px viewport widths with no content clipping or broken
interactions.

## Related Records

- `plan:20260526-mill-production-readiness` - parent plan
- `ticket:20260526-mill-interaction-completeness` - interactions must work before responsive testing

## Scope

### Must Change

- `loom-mill/frontend/src/App.svelte` - Add responsive breakpoints:
  - `≥1280px`: Current layout (sidebar + detail + optional drawer)
  - `1024-1279px`: Narrower sidebar (240px), drawer overlays content
  - `768-1023px`: Sidebar becomes slide-over overlay, triggered by hamburger; detail is full-width
  - `<768px`: Single-column: list view OR detail view with back button
  Add a layout state: `'desktop' | 'tablet' | 'mobile'` derived from viewport width.
  Add hamburger menu button visible at <1024px.

- `loom-mill/frontend/src/lib/WorkstationList.svelte` - At mobile widths, the list
  becomes full-height with no visible detail panel. Selecting an item transitions
  to detail view.

- `loom-mill/frontend/src/lib/DetailPanel.svelte` - At mobile widths, add a back
  button that returns to list view. Max content width of 800px centered on ultrawide.

- `loom-mill/frontend/src/lib/SettingsDrawer.svelte` - At <1024px, drawer becomes
  full-screen overlay instead of 400px side panel. Max-width 400px centered.

- `loom-mill/frontend/src/lib/StatusBar.svelte` - At <768px, collapse to show only
  counts (no labels). At <480px, hide entirely (info available in footer).

- `loom-mill/frontend/src/app.css` - Add CSS custom properties for breakpoints.
  Add container queries where appropriate for component-level responsiveness.

- `loom-mill/frontend/src/lib/LogViewer.svelte` - Ensure log lines wrap properly
  at narrow widths (no horizontal scroll within the log viewer).

### Must Not Change

- Desktop experience (current layout at ≥1280px stays identical)
- Backend (purely CSS/layout concern)
- Component internal logic

### Non-Goals

- Native mobile app experience
- Touch gesture support (pinch, swipe)
- Offline/PWA support

## Acceptance

- ACC-001: At 375px width, UI shows single-column list; selecting a ticket shows detail with back button
  - Evidence: Playwright screenshot at 375px showing list view, then screenshot after selecting showing detail with back button
  - Audit: Verify no content clipping or horizontal scroll

- ACC-002: At 768px width, sidebar is an overlay triggered by hamburger
  - Evidence: Playwright screenshot at 768px showing hamburger icon; click opens sidebar overlay
  - Audit: Verify overlay doesn't push content, backdrop dismisses it

- ACC-003: At 1024px width, sidebar is 240px; drawer overlays content
  - Evidence: Playwright screenshot at 1024px showing narrower sidebar and content area
  - Audit: Verify no content is cut off

- ACC-004: At 1440px width, layout matches current desktop design exactly
  - Evidence: Playwright screenshot at 1440px matches previous visual baseline
  - Audit: Side-by-side comparison with current state

- ACC-005: At 2560px width, detail content is max-width 800px centered, no awkward stretch
  - Evidence: Playwright screenshot at 2560px showing centered content
  - Audit: Verify no elements stretch beyond readable width

- ACC-006: No horizontal scrollbar appears at any width between 375px and 2560px
  - Evidence: Playwright evaluation: `document.body.scrollWidth <= document.body.clientWidth` at each breakpoint
  - Audit: Automated check across 5 widths

## Current State

Ready to start after Unit 3 lands. Can parallelize with Units 4 and 6.

First Ralph run should:
1. Add breakpoint CSS custom properties
2. Implement mobile single-column layout with back nav
3. Implement tablet overlay sidebar
4. Add hamburger toggle
5. Constrain detail panel max-width on ultrawide
6. Playwright verification at 375, 768, 1024, 1440, 2560px

## Journal

- 2026-05-26: Created ticket with Status `open`. Current layout is hardcoded to
  fixed widths with no breakpoints. App.svelte line 132 sets w-80 (320px) with
  no responsive override.
