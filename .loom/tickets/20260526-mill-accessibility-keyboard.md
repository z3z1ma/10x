# Mill Accessibility + Keyboard Navigation

ID: ticket:20260526-mill-accessibility-keyboard
Type: Ticket
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - keyboard handling is easy to regress; ARIA requires careful testing

Priority: high - unusable without mouse; fails basic a11y
Depends On: ticket:20260526-mill-interaction-completeness

## Summary

The Mill UI is currently mouse-only. Clickable elements are unsemantic divs, the
settings drawer has no focus trap, toasts are not announced to screen readers,
there's no keyboard navigation between tickets/workstations, and there's no command
palette for power users who want to navigate without touching the mouse.

A production control room must be fully operable via keyboard. Operators monitoring
long-running agents need rapid navigation without context-switching to a trackpad.

Single closure claim: The UI is fully operable via keyboard alone, passes ARIA
landmark checks, traps focus in overlays, announces dynamic content, and provides
a Cmd+K command palette.

## Related Records

- `plan:20260526-mill-production-readiness` - parent plan
- `ticket:20260526-mill-interaction-completeness` - must land first (all interactions working)

## Scope

### Must Change

- `loom-mill/frontend/src/lib/WorkstationList.svelte` - Convert clickable divs to
  `<button>` or add `role="listbox"` with `role="option"` children. Add j/k
  keyboard navigation (move selection up/down). Add Enter to select, Escape to
  deselect.

- `loom-mill/frontend/src/lib/TicketRow.svelte` - Add proper `role="option"`,
  `aria-selected`, `tabindex` management. Currently a plain div with onclick.

- `loom-mill/frontend/src/lib/ReadyTicketRow.svelte` - Same as TicketRow.

- `loom-mill/frontend/src/lib/WorkstationRow.svelte` - Same as TicketRow. Ensure
  action buttons within the row are keyboard-reachable without interfering with
  list navigation.

- `loom-mill/frontend/src/lib/SettingsDrawer.svelte` - Add focus trap (Tab cycles
  within drawer when open). Add Escape to close. Add `role="dialog"`,
  `aria-modal="true"`, `aria-labelledby`.

- `loom-mill/frontend/src/lib/Toast.svelte` - Add `role="alert"` and
  `aria-live="polite"` for screen reader announcement. Toasts must be announced
  without requiring focus.

- `loom-mill/frontend/src/lib/DetailPanel.svelte` - Tab switching should be
  `role="tablist"` with `role="tab"` buttons and `role="tabpanel"` content.
  Arrow keys switch tabs.

- `loom-mill/frontend/src/lib/ThemeToggle.svelte` - Add `aria-label` describing
  current state ("Switch to dark mode" / "Switch to light mode").

- `loom-mill/frontend/src/lib/StatusBar.svelte` - Pills should be `role="button"`
  with `aria-label` describing what they do ("Show 3 shaped tickets").

- `loom-mill/frontend/src/App.svelte` - Add ARIA landmarks: `role="banner"` on
  header, `role="main"` on content area, `role="contentinfo"` on footer.
  Add global keyboard listeners:
  - `Cmd+K` / `Ctrl+K`: open command palette
  - `Escape`: close any overlay (drawer, palette) or deselect
  - `?`: show keyboard shortcut help (small overlay)

- `loom-mill/frontend/src/lib/CommandPalette.svelte` - New component: modal overlay
  with search input, shows available actions:
  - Navigate to ticket by name (fuzzy search over records)
  - Navigate to workstation by slug
  - Toggle settings
  - Toggle theme
  - Focus actions (go to logs, go to iterations)
  - Keyboard shortcut reference

### Must Not Change

- Visual design (only semantic improvements)
- Component structure (add ARIA to existing elements)
- Backend (purely frontend concern)

### Non-Goals

- Full WAI-ARIA compliance audit (focus on keyboard operability and landmarks)
- Screen reader testing on multiple platforms (verify with VoiceOver basics)
- RTL support

## Acceptance

- ACC-001: j/k keys navigate the left panel list; Enter selects; Escape deselects
  - Evidence: Playwright keyboard test sequence: press 'j' 3 times → 3rd item highlighted; press Enter → detail panel shows that item; press Escape → selection cleared
  - Audit: Verify focus management doesn't break with empty lists or single items

- ACC-002: Tab cycles within SettingsDrawer when open; Escape closes it
  - Evidence: Open drawer → Tab repeatedly → focus stays within drawer; press Escape → drawer closes and focus returns to trigger button
  - Audit: Verify no focus escape to background content

- ACC-003: Cmd+K opens command palette with fuzzy ticket search
  - Evidence: Press Cmd+K → palette appears; type ticket slug → matching tickets shown; Enter → navigates to that ticket; Escape → palette closes
  - Audit: Verify palette captures all keyboard input and doesn't pass through to background

- ACC-004: Toasts are announced by screen readers
  - Evidence: Trigger a toast → DOM element has `role="alert"` and `aria-live="polite"`
  - Audit: Inspect rendered HTML for ARIA attributes

- ACC-005: All clickable ticket/workstation rows have proper ARIA roles
  - Evidence: `document.querySelectorAll('[role="option"]')` matches number of visible rows
  - Audit: Inspect rendered HTML for semantic roles

- ACC-006: DetailPanel tabs use `role="tablist"` / `role="tab"` / `role="tabpanel"` with arrow key switching
  - Evidence: Focus tab bar → ArrowRight/ArrowLeft switches active tab
  - Audit: Verify `aria-selected` matches visual state

## Current State

Ready to start after Unit 3 lands. All interactions must work before adding
keyboard support (otherwise keyboard triggers dead buttons).

First Ralph run should:
1. Add ARIA landmarks to App.svelte
2. Convert left panel items to proper listbox pattern with j/k nav
3. Add focus trap to SettingsDrawer
4. Add role="alert" to Toast
5. Add tablist pattern to DetailPanel tabs
6. Create CommandPalette.svelte
7. Verify with Playwright keyboard sequences

## Journal

- 2026-05-26: Created ticket with Status `open`. Audit found clickable divs in 5
  components, no focus trapping, no keyboard navigation, no ARIA landmarks, and
  no screen reader announcements.
