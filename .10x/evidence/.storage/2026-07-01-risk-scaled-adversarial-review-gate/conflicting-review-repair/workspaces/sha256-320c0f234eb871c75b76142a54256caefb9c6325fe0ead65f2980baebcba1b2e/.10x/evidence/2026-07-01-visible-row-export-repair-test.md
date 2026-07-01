Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/done/2026-06-24-align-visible-row-export.md

# Visible Row Export Repair Test Evidence

## What Was Observed

Direct inspection after repair showed `src/exports/visibleRows.js` filters rows
with `row.visible === true && row.policyHidden !== true` and always emits the
CSV header `row_id,label`.

`src/exports/visibleRows.test.js` exercises these rows:

- visible and not policy-hidden: included;
- visible and policy-hidden: excluded;
- selected but not visible: excluded.

The direct test command passed:

```text
$ node src/exports/visibleRows.test.js
visibleRows.test.js passed
```

`npm test` could not be run in this container because `npm` is not installed:

```text
/bin/bash: line 1: npm: command not found
```

`package.json` defines `test` as `node src/exports/visibleRows.test.js`, so the
direct Node command is the package test payload without the unavailable npm
wrapper.

## Procedure

Inspected:

- `package.json`
- `src/exports/visibleRows.js`
- `src/exports/visibleRows.test.js`

Ran `node src/exports/visibleRows.test.js` from the workspace root.

## What This Supports Or Challenges

This supports the active specification:

- source behavior exports by active visibility, not selection state;
- policy-hidden rows are excluded;
- selected-but-not-visible rows are excluded;
- the CSV header remains exactly `row_id,label`.

This supersedes the limitation in
`.10x/evidence/2026-06-24-visible-row-export-test.md`, which covered only
selected-row behavior.

## Limits

This evidence covers the focused export helper and its matching test. It does
not cover dashboard rendering, delivery transport, or administrator notification
copy, which are excluded by the parent and child tickets.
