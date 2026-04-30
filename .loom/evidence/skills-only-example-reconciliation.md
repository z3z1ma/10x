---
id: evidence:skills-only-example-reconciliation
kind: evidence
status: recorded
created_at: 2026-04-30T16:40:28Z
updated_at: 2026-04-30T16:43:49Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:9bgilfwy
  critique:
    - critique:skills-only-example-reconciliation-review
external_refs: {}
---

# Summary

Structural validation evidence for reconciling core examples with the skills-only
product boundary.

# Procedure

Inspected example fixtures and ran targeted checks:

- `git diff --check`
- `git diff --stat`
- Glob `examples/**/commands/**`
- Grep for Loom slash-command route text: `` `/loom-` ``, `via `/loom`, `# /loom`, and ` /loom-*`
- Grep for `commands/loom`, `after/commands`, and `# /loom-`
- Grep for `command wrapper|command-wrapper`

# Artifacts

- `git diff --check` returned no output.
- `git diff --stat` showed the example reconciliation changed nine example
  files, including deletion of
  `examples/03-feature-with-spec-plan-ticket-ralph/after/commands/loom-ship.md`.
- Glob `examples/**/commands/**` returned no files.
- Slash-command route grep returned no files.
- `commands/loom`, `after/commands`, and `# /loom-` grep returned no files.
- `command wrapper|command-wrapper` grep returned only negative guidance: common
  wrong behavior or explicit statements that examples do not define
  command-wrapper product surfaces.
- Grep for stale `adding a command without a spec` wording returned no files
  after critique fix.

# Supports Claims

- ticket:9bgilfwy#ACC-001
- ticket:9bgilfwy#ACC-002
- ticket:9bgilfwy#ACC-003
- ticket:9bgilfwy#ACC-004
- ticket:9bgilfwy#ACC-005

# Challenges Claims

None.

# Environment

Commit: `9ca081c`
Branch: `main`
Runtime: Markdown-only protocol corpus; no app runtime
OS: macOS / Darwin
Relevant config: dirty worktree containing memory-support-layer changes and this
example reconciliation tranche

# Validity

Valid for: the current working-tree diff at 2026-04-30T16:43:49Z.
Recheck when: any `examples/**` fixture or examples index changes before
acceptance.

# Limitations

This evidence validates structural example wording and fixture paths. It does
not prove future operators will avoid command wrappers in practice.

# Result

Core examples no longer include a command-wrapper fixture or `/loom-*` acceptance
route. Example 03 now points the shipping feature implementation at the
`skills/loom-ship` surface, and examples 02/06 route acceptance through ticket
acceptance review.

# Interpretation

The evidence supports the ticket-local acceptance criteria pending recommended
operator-surface critique disposition.

# Related Records

- ticket:9bgilfwy
- critique:skills-only-example-reconciliation-review
