# Design Room: Selection Fix + Editor Polish

ID: ticket:20260526-mill-dr-selection-editor
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - CSS fix with clear root cause

Priority: high - broken visual feedback on the most basic editor interaction

## Summary

Three editor issues that break the basic authoring experience:

1. **Text selection has no visible background on single-line selections.** Root
   cause: CodeMirror's `drawSelection()` only renders `.cm-selectionBackground`
   div elements for multi-line or unfocused selections. For a focused editor with
   a single-line selection, the native browser `::selection` pseudo-element is
   used, but we have NO custom CSS for it. The dark theme's default `::selection`
   is invisible or near-invisible against the dark background.

2. **Editor doesn't scroll to top when opening a new document.** When clicking a
   record in the graph, the editor loads content but stays at whatever scroll
   position it was at from the previous document.

3. **Sidebar doesn't highlight the selected record when navigating via Cmd+Click
   on a record reference link.** The `onNavigate` callback loads the document but
   doesn't update `selectedDocumentId` in DesignRoom to match, so the sidebar
   highlight stays on the old record.

## Scope

### Fix 1: Selection CSS (`editor-theme.ts`)

Add native `::selection` styling to the theme. This is the ONLY reliable way to
style single-line focused selections in CodeMirror 6:

```typescript
// Add to millTheme EditorView.theme():
'.cm-content ::selection': {
  backgroundColor: 'rgba(99, 102, 241, 0.35) !important',
},
'.cm-content ::-moz-selection': {
  backgroundColor: 'rgba(99, 102, 241, 0.35) !important',
},
// Also ensure the unfocused/multi-line case is styled:
'&.cm-focused .cm-selectionBackground, .cm-selectionBackground': {
  backgroundColor: 'rgba(99, 102, 241, 0.25) !important',
},
```

Additionally, consider removing `drawSelection()` from the extensions array entirely
since we're not using multiple cursors. Native selection + CSS is simpler and
guaranteed to work. Keep `highlightSelectionMatches()` (that's a different thing).

### Fix 2: Scroll to top on document open (`DocumentEditor.svelte`)

After setting new content, dispatch a scroll-to-top:

```typescript
// In the effect that handles documentPath changes, after setContent():
if (view) {
  view.dispatch({
    effects: EditorView.scrollIntoView(0, { y: 'start' })
  });
}
```

Or simpler: `view.scrollDOM.scrollTop = 0;` after content is set.

### Fix 3: Sidebar selection sync (`DesignRoom.svelte`)

The `onNavigate` prop passed to DocumentEditor is called when the user Cmd+Clicks
a record reference. Currently it only opens the document. It must ALSO update
`selectedDocumentId` so the sidebar shows the correct highlight:

```typescript
function handleNavigate(recordId: string) {
  // Find the record by ID
  const record = store.state.records.find(r => r.metadata.id === recordId);
  if (record) {
    selectedDocumentId = record.path;  // This is what the sidebar uses for highlighting
  }
}
```

Ensure the sidebar's `selectedId` prop receives the same value that was just set.

## Acceptance

- ACC-001: Selecting text within a single line shows a clearly visible purple/blue background
  - Evidence: Playwright screenshot showing single-line selection with visible background
  - Audit: Compare against multi-line selection - both should have same opacity

- ACC-002: Opening a new document scrolls the editor to line 1
  - Evidence: Open a long document (scroll to bottom), then click another document → editor shows line 1
  - Audit: Verify scrollTop is 0 after document switch

- ACC-003: Cmd+Click on a record reference updates the sidebar highlight to match
  - Evidence: Cmd+Click `spec:mill-design-room` in a document → sidebar highlights "Mill Design Room" under Specs
  - Audit: Verify selectedDocumentId updates in DesignRoom state

## Journal

- 2026-05-26: Created. Selection bug root cause confirmed: `drawSelection()` doesn't
  cover focused single-line selections. Native `::selection` CSS is the fix.
