# Design Room Editor Intelligence

ID: ticket:20260526-mill-dr-editor-intelligence
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - CodeMirror extensions are well-documented but require careful integration
Depends On: ticket:20260526-mill-dr-critical-fixes

## Summary

Transform the CodeMirror editor from a generic Markdown editor into a Loom-native
authoring tool. Record references become clickable navigation links. Hovering them
shows a preview tooltip. Section headings are navigable via a dropdown. Typing
record prefixes triggers autocomplete. The editor header shows breadcrumb
navigation.

This is what makes the Design Room feel purpose-built for Loom, not just "a
markdown editor next to a chat."

## Scope

### 1. Record Reference Links (clickable navigation)

Create a CodeMirror decoration extension that:
- Detects patterns: `ticket:*`, `spec:*`, `plan:*`, `research:*`, `knowledge:*`, `evidence:*`, `audit:*`
- Renders them as underlined accent-colored text (like links)
- On Cmd+Click: navigate to that record (call onNavigate prop with the ID)
- Visual: underline + accent color, cursor pointer on hover

Implementation: Use `ViewPlugin` with `DecorationSet` to add mark decorations on matching patterns.

### 2. Hover Preview (tooltip on record references)

When hovering a record reference for 300ms:
- Show a tooltip with: title, status badge, surface type, first heading
- Position: above/below the hovered text
- Dismiss on mouse leave
- Data source: look up record in `store.state.records` by ID

Implementation: Use CodeMirror's `hoverTooltip` extension.

### 3. Section Navigation Dropdown

In the editor header, add a dropdown that lists all `##` and `###` headings in the current document:
- Clicking a heading scrolls to that line in the editor
- Updates as document changes
- Show heading level with indentation (## = top, ### = indented)
- Current section highlighted based on cursor position

### 4. Record Link Autocomplete

When the user types a known prefix (`ticket:`, `spec:`, `plan:`, `knowledge:`, `research:`):
- Trigger autocomplete dropdown showing matching records
- Each option shows: status dot + title
- Selecting one inserts the full ID (e.g., `ticket:20260526-mill-foundation-fixes`)
- Filter as user types more characters after the colon

Implementation: Use `@codemirror/autocomplete` with a custom completion source.

### 5. Smart ACC/REQ Numbering

When typing `ACC-` or `REQ-`:
- Suggest the next sequential number based on existing ones in the document
- If ACC-001 and ACC-002 exist, suggest ACC-003

### 6. Breadcrumb in Editor Header

Replace the plain path display with a clickable breadcrumb:
- `Tickets > 20260526-mill-foundation-fixes`
- Surface name is clickable → filters graph sidebar to that surface
- File portion shows the title (first heading) not just the slug

## Acceptance

- ACC-001: Record references (`ticket:X`) render as accent-colored underlined text
- ACC-002: Cmd+Click on a record reference opens that record in the editor
- ACC-003: Hovering a record reference shows tooltip with title and status
- ACC-004: Section dropdown lists all ## headings; clicking scrolls to that heading
- ACC-005: Typing `ticket:` triggers autocomplete with matching tickets
- ACC-006: Typing `ACC-` suggests next sequential number
- ACC-007: Build passes clean

## Journal

- 2026-05-26: Created. These features make the editor Loom-native rather than generic.
