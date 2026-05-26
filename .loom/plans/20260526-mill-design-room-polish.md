# Design Room Deep Polish

ID: plan:20260526-mill-design-room-polish
Type: Plan
Status: completed
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - harness fix requires testing with real subprocess; CodeMirror extensions are well-documented

## Summary

The Design Room is structurally complete but has critical bugs (chat doesn't work,
no undo, invisible selection) and is missing the intelligence that makes it feel
purpose-built for Loom records rather than a generic markdown editor. This plan
delivers: working chat with proper harness integration, an editor with Loom-native
intelligence (record links, autocomplete, section navigation, hover previews), a
graph sidebar that actually shows hierarchy, and the micro-interactions that make
this feel like the future of AI-driven shaping.

## Related Records

- `spec:mill-design-room` - behavior contract
- `plan:20260526-mill-design-room` - completed initial implementation

## Strategy

Fix what's broken first (Unit 1), then add intelligence (Units 2-3), then layer
delight (Unit 4). Units 2 and 3 parallelize after Unit 1.

## Execution Units

### Unit 1: Critical Bug Fixes

Ticket: ticket:20260526-mill-dr-critical-fixes

Fix the three broken things:
- Chat: rewrite harness.py invocation (opencode run takes prompt as positional arg
  or via stdin pipe; -m doesn't exist). Add "echo" test mode. Better error diagnostics.
- Editor: add history() + historyKeymap for Ctrl+Z undo/redo. 
- Editor: enable EditorView.lineWrapping for word wrap.
- Editor: fix selection background for single-line selections (increase opacity/contrast).

### Unit 2: Editor Intelligence

Ticket: ticket:20260526-mill-dr-editor-intelligence

Transform the editor from a generic CodeMirror instance into a Loom-native
authoring tool:
- Record reference links: detect `ticket:X`, `spec:Y`, `knowledge:Z` patterns,
  render as clickable links that navigate to that record in the graph/editor.
- Hover preview: hovering a record reference shows tooltip with title + status.
- Section navigation: dropdown in editor header listing all ## headings, click jumps.
- Record link autocomplete: typing `ticket:` triggers completion from known records.
- Smart ACC/REQ numbering: typing `ACC-` suggests next number.
- Breadcrumb: editor header shows `surface / filename` as clickable path.

### Unit 3: Graph Hierarchy + Search

Ticket: ticket:20260526-mill-dr-graph-hierarchy

Redesign the flat list into a true hierarchical graph:
- Search input at top (filter by title/ID/status).
- Tree hierarchy: plans show child tickets nested below. Specs show citing tickets.
  Tickets with depends_on show under their dependency.
- Expand/collapse nodes with arrow indicators.
- Indentation with subtle connector lines.
- Section counts show filtered/total (e.g., "Tickets (12/47)").
- "Pinned" section at top for frequently accessed records.
- Smooth collapse/expand animations.

### Unit 4: Chat Hardening + Delight

Ticket: ticket:20260526-mill-dr-chat-hardening

Make the chat bulletproof and delightful:
- Harness config in settings (operator picks their command: opencode, claude, codex, echo).
- Error messages show stderr extract and suggest fixes.
- "Test connection" button that sends a simple echo prompt.
- Retry button on failed messages.
- Character/token count on input.
- Message timestamps visible.
- Copy button on assistant messages.
- Keyboard shortcut: Cmd+Enter always sends (even without focus in input).

## Milestones

### Milestone: Working

Child tickets: ticket:20260526-mill-dr-critical-fixes

Chat works. Undo works. Selection is visible. Lines wrap. No broken interactions.

### Milestone: Intelligent

Child tickets: ticket:20260526-mill-dr-editor-intelligence, ticket:20260526-mill-dr-graph-hierarchy

The editor understands Loom records natively. The graph shows real relationships.
It feels purpose-built, not generic.

### Milestone: Delightful

Child tickets: ticket:20260526-mill-dr-chat-hardening

Every interaction has polish. Errors are helpful. Configuration is surfaced.
The shaping experience makes operators want to use it.

## Current State

Plan created. Executing Unit 1 first (critical fixes), then Units 2+3 in parallel,
then Unit 4.

## Journal

- 2026-05-26: Created plan. Operator identified critical bugs from live testing:
  chat fails, no undo, invisible selection, flat sidebar, no search. Extended with
  visionary editor intelligence and graph hierarchy.
