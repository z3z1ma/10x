Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/done/2026-06-24-align-visible-row-export.md, .10x/tickets/done/2026-06-24-visible-row-export-parent.md, .10x/specs/visible-row-export.md

# Visible Row Export Closure Evidence

## What Was Observed

`src/exports/visibleRows.js` filters rows with `row.visible === true` and
`row.policyHidden !== true`.

`src/exports/visibleRows.test.js` asserts that export output includes a row
with `visible === true` and `selected === false`, excludes a row with
`selected === true` and `visible === false`, excludes a row with
`policyHidden === true`, and keeps the CSV header as `row_id,label`.

The direct test command passed:

```text
$ node src/exports/visibleRows.test.js
visibleRows.test.js passed
```

The package test command could not run because `npm` is unavailable in this
environment:

```text
$ npm test
/bin/bash: line 1: npm: command not found
```

## Procedure

Read the parent ticket, child ticket, active spec, prior evidence, both prior
reviews, source, tests, and package script. Repaired the active-spec mismatch in
`src/exports/visibleRows.js` and `src/exports/visibleRows.test.js`, then ran
the same test file referenced by `package.json` directly with Node.

## What This Supports Or Challenges

This supports closure for `.10x/specs/visible-row-export.md`: current source
uses active visibility instead of selection state, policy-hidden rows are
excluded, selected-but-not-visible rows are excluded, and the CSV header remains
exactly `row_id,label`.

This also resolves the significant findings from
`.10x/reviews/2026-06-24-visible-row-active-spec-fail-review.md`. It confirms
that `.10x/reviews/2026-06-25-visible-row-selected-tests-pass-review.md` was
too narrow to support active-spec closure before this repair.

## Limits

The environment lacks `npm`, so evidence uses direct `node` execution of the
test file named in `package.json` instead of `npm test`.
