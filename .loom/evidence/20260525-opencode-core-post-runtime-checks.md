# OpenCode Core Post Runtime Checks

ID: evidence:20260525-opencode-core-post-runtime-checks
Type: Evidence Observation
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

After the fresh `loom-weaver` runtime boundary probe and record updates, the Core smoke check, Core package check, and Markdown diff whitespace check passed.

## Observation

Procedure and observed results:

```text
$ npm --prefix loom-core run smoke
Result: passed. Smoke output included "ok": true and confirmed the OpenCode Loom Weaver edit permission as {"*":"deny", ".loom/**":"allow"}.

$ npm --prefix loom-core run pack:check
Result: passed. The command reran smoke successfully and completed `npm pack --dry-run` for @z3z1ma/open-loom-core@0.3.0.

$ git diff --check
Result: passed with no output.
```

## Artifacts

- Terminal output from `npm --prefix loom-core run smoke` - passed and reported `loomWeaverEditPermission` as denying `*` and allowing `.loom/**`.
- Terminal output from `npm --prefix loom-core run pack:check` - passed, including smoke and dry-run package listing.
- Terminal output from `git diff --check` - no output.

## What This Shows

- `ticket:20260515-opencode-weaver-agent-runtime-wiring#ACC-005` - supports - the requested Core smoke, Core package, and Markdown diff checks passed after the fresh runtime probe and record reconciliation.
- `ticket:20260515-opencode-weaver-agent-runtime-wiring#ACC-003` - supports - the smoke output still includes the model-only Loom Weaver prompt and permission checks that cover the diagnosed shadowing failure mode.

## What This Does Not Show

- It does not add new runtime coverage beyond `evidence:20260525-opencode-weaver-runtime-boundary-verification`.
- It does not independently audit the ticket closure story.
- It does not cover Playbooks or non-OpenCode adapter packages, which are outside this ticket's acceptance checks.

## Related Records

- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - consuming ticket for the OpenCode Loom Weaver runtime wiring fix.
- `evidence:20260525-opencode-weaver-runtime-boundary-verification` - fresh runtime boundary probe that preceded these checks.
