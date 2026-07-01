Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/done/2026-06-24-align-visible-row-export.md, .10x/tickets/done/2026-06-24-visible-row-export-parent.md, .10x/specs/visible-row-export.md

# Visible Row Export Spec Test

## What Was Observed

`src/exports/visibleRows.js` filters rows with `row.visible === true` and
`row.policyHidden !== true`. `src/exports/visibleRows.test.js` expects only the
visible, non-policy-hidden row to be exported from a fixture that also includes
a selected-but-not-visible row and a visible policy-hidden row. The expected CSV
is exactly:

```text
row_id,label
r_2,Beta
```

## Procedure

Commands run from the workspace root:

```text
$ npm test
/bin/bash: line 1: npm: command not found

$ node --version
v18.19.1

$ node src/exports/visibleRows.test.js
visibleRows.test.js passed
```

`package.json` defines `npm test` as `node src/exports/visibleRows.test.js`,
so the direct `node` command exercised the same test entrypoint despite `npm`
being unavailable in this shell.

## What This Supports Or Challenges

This supports closure for the active specification because source and test
coverage now map to:

- inclusion of `visible === true` rows when `policyHidden !== true`;
- exclusion of `policyHidden === true` rows;
- exclusion of selected rows when `visible !== true`;
- exact `row_id,label` header.

This supersedes the limits recorded in
`.10x/evidence/2026-06-24-visible-row-export-test.md` for closure purposes.

## Limits

The evidence covers the local export function and its test entrypoint only. It
does not cover dashboard rendering, delivery transport, or administrator
notification copy, which are outside the ticket family scope.
