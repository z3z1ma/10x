# Design Room Experience Perfection Pass

ID: plan:20260526-mill-dr-perfection
Type: Plan
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - targeted fixes with clear root causes identified

## Summary

Third polish pass addressing verified bugs from live operator testing plus UX
improvements that make the Design Room feel native and delightful. Every issue
has a clear root cause and fix path.

## Related Records

- `plan:20260526-mill-design-room-polish` - completed; this is the follow-up
- `spec:mill-design-room` - behavior contract

## Strategy

Three focused units: fix bugs (U1), improve chat UX (U2), improve sidebar/editor
UX (U3). All three can run in parallel since they touch different files.

## Execution Units

### Unit 1: Selection Fix + Editor Polish

Ticket: ticket:20260526-mill-dr-selection-editor

Root causes:
- Selection invisible on single-line: `drawSelection()` only renders `.cm-selectionBackground`
  for multi-line/unfocused. Focused single-line uses native browser selection which
  has NO custom CSS applied. Fix: add `::selection` pseudo-element styles.
- Editor doesn't scroll to top on new document: no `scrollTo` after content set.
- Sidebar doesn't sync selection when navigating via Cmd+Click on record link.

### Unit 2: Chat Experience Overhaul

Ticket: ticket:20260526-mill-dr-chat-experience

Root causes:
- Echo mode dumps full prompt: `harness.py` echo returns `[echo] {entire_prompt}`.
  Fix: echo only the user's message, not the system/history/document context.
- No streaming indicator: nothing shows while harness subprocess is running.
- Response appears truncated: echo has `[:500]` slice. Remove the limit.
- Harness config too prominent: takes visual space from actual messages.

### Unit 3: Sidebar UX - Temporal Records + Initial State

Ticket: ticket:20260526-mill-dr-sidebar-ux

Issues:
- Temporal records (tickets with dates) show ALL records as a flat wall. Need
  "most recent N" with "Show N more" expand.
- Initial state shows everything expanded. Should start collapsed except Specs.
- Count in section header should always show total, even when collapsed to N.

## Current State

Plan created. Dispatching all 3 in parallel.

## Journal

- 2026-05-26: Created. Issues verified from live operator testing with screenshots.
  Root causes identified for all bugs.
