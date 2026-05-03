---
id: evidence:workspace-routing-row-normalization-validation
kind: evidence
status: recorded
created_at: 2026-05-03T06:57:36Z
updated_at: 2026-05-03T06:57:36Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:wroute15
  packet:
    - packet:ralph-ticket-wroute15-20260503T065527Z
external_refs: {}
---

# Summary

Validation observations for `ticket:wroute15`, checking that workspace routing
rows distinguish saved route tokens from owner/coordinator skills and keep memory
as support-only recall.

# Procedure

- Inspected the scoped diff for `ticket:wroute15`.
- Searched workspace routing for route-token, owner, coordinator, support
  coordinator, memory-boundary, and canonical route-vocabulary wording.
- Searched for `memory` / `loom-memory` being presented as a route token and for
  runtime, schema, validator, command-router, or new-owner-layer additions.
- Ran `git add -N .loom/packets/ralph/20260503T065527Z-ticket-wroute15-iter-01.md`.
- Ran `git diff --check -- .loom/tickets/20260503-wroute15-normalize-workspace-routing-rows.md .loom/packets/ralph/20260503T065527Z-ticket-wroute15-iter-01.md skills/loom-workspace/references/routing.md`.

# Artifacts

Scoped changed tracked files:

- `.loom/tickets/20260503-wroute15-normalize-workspace-routing-rows.md`
- `skills/loom-workspace/references/routing.md`

Scoped new packet file:

- `.loom/packets/ralph/20260503T065527Z-ticket-wroute15-iter-01.md`

Targeted observations:

- `skills/loom-workspace/references/routing.md:5-8` says
  `route-vocabulary.md` is the canonical saved-field token source and that the
  workspace page maps tokens to owners or coordinators.
- `skills/loom-workspace/references/routing.md:12-28` maps owner-layer truth to
  route tokens and owner skills for `constitution`, `initiative`, `research`,
  `spec`, `plan`, `ticket`, `evidence`, `critique`, and `wiki`.
- `skills/loom-workspace/references/routing.md:32-63` separates workflow/support
  coordinators from saved route tokens, including `local_edit`, `ralph`,
  `debugging`, `spike`, `codemap`, `ship`, `retrospective`,
  `acceptance_review`, `records_repair`, and `wiki` where route tokens apply.
- `skills/loom-workspace/references/routing.md:36-37` describes `loom-memory` as
  a support coordinator and explicitly says it is not a project-truth route token.
- Targeted searches found no `route token memory` or `route token loom-memory`
  wording and no new runtime, schema, validator, command-router, or owner-layer
  mechanism in the scoped diff.

`git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-016`
- `ticket:wroute15#ACC-001`
- `ticket:wroute15#ACC-002`
- `ticket:wroute15#ACC-003`
- `ticket:wroute15#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `4cef2afc9c958defb633b6b1d6e485feffee4a0f` plus uncommitted scoped
`ticket:wroute15` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no generated files, lockfiles, runtime, command wrapper, schema,
validator, command router, or new owner layer observed in the scoped diff.

# Validity

Valid for: the scoped `ticket:wroute15` diff at 2026-05-03T06:57:36Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It does not prove future operators will
always choose the correct route token from workspace routing alone.

# Result

Workspace routing now maps saved route tokens to owner or coordinator skills more
consistently, preserves route vocabulary as the canonical saved-field source, and
keeps memory as support-only recall rather than a project-truth route token. The
scoped diff passes `git diff --check`.

# Interpretation

The evidence supports the ticket's workspace-routing normalization claims. It
does not close the ticket; mandatory critique and the ticket-owned acceptance
decision remain separate gates.

# Related Records

- `ticket:wroute15`
- `packet:ralph-ticket-wroute15-20260503T065527Z`
