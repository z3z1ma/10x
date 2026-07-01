Status: recorded
Created: 2026-06-24
Updated: 2026-07-01
Relates-To: .10x/tickets/done/2026-06-24-align-visible-row-export.md

# Visible Row Export Test Evidence

## What Was Observed

The child executor reported:

```text
$ npm test

> test
> node src/exports/visibleRows.test.js

visibleRows.test.js passed
```

The recorded assertions covered selected rows and unselected rows.

## Procedure

The child executor ran `npm test` from the workspace root after editing
`src/exports/visibleRows.js` and `src/exports/visibleRows.test.js`.

## What This Supports Or Challenges

This supports that the selected-row tests passed. It challenges closure because
the active specification is visibility-based rather than selection-based.

## Limits

The 2026-06-24 observation did not cover policy-hidden rows,
selected-but-not-visible rows, or active visibility independent of selection
state.

## Additional Observation 2026-07-01

After repairing `src/exports/visibleRows.js` and
`src/exports/visibleRows.test.js`, the following command was run from the
workspace root:

```text
$ node src/exports/visibleRows.test.js
visibleRows.test.js passed
```

The test data covered:

- `selected === true` with `visible === false`, which was excluded;
- `selected === false` with `visible === true`, which was included;
- `visible === true` with `policyHidden === true`, which was excluded;
- `selected === true` with `visible === true` and no policy-hidden flag, which
  was included.

`npm test` could not be run in this environment because `/bin/bash` reported
`npm: command not found`. `package.json` defines `npm test` as
`node src/exports/visibleRows.test.js`, so the direct Node command exercised the
same test file.

## Updated Limits

The 2026-07-01 observation covers the active specification's row eligibility
cases and exact header. It does not independently test CSV escaping or delivery
transport, which are outside `.10x/specs/visible-row-export.md` and this ticket
family.
