---
id: evidence:loom-git-skill-validation
kind: evidence
status: recorded
created_at: 2026-04-25T07:42:40Z
updated_at: 2026-04-25T07:48:46Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:h5j0wnkz
  critique:
    - critique:loom-git-skill-review
external_refs: {}
---

# Summary

Validation evidence for adding the `loom-git` skill and wiring it into Ralph and
the package framing.

# Procedure

- Read `constitution:main` and the active skill-authoring guidance.
- Read all shipped `skills/*/SKILL.md` files to match current skill quality and
  structure.
- Read Ralph packet guidance and template surfaces before editing Ralph.
- Created `skills/loom-git/SKILL.md` and four references.
- Updated Ralph, `/loom-work`, `README.md`, `PROTOCOL.md`, and
  `ARCHITECTURE.md` to route Git-backed isolation as a workflow support surface.
- Ran `git diff --check`; it returned no output for tracked-file changes.
- Ran trailing-whitespace searches across `skills/loom-git` and `.loom`; no
  matches were found.
- Ran targeted searches for stale remote/default-branch/base-field assumptions;
  no product-surface matches remained.
- Ran a read-only oracle critique, fixed medium findings, and ran a focused
  re-review that returned no remaining findings in scope.

# Artifacts

Files created:

- `skills/loom-git/SKILL.md`
- `skills/loom-git/references/branch-and-remote-hygiene.md`
- `skills/loom-git/references/worktree-discipline.md`
- `skills/loom-git/references/parallel-ralph-with-git.md`
- `skills/loom-git/references/diff-commit-and-merge-hygiene.md`
- `.loom/tickets/20260425-h5j0wnkz-add-loom-git-skill.md`
- `.loom/evidence/loom-git-skill-validation.md`
- `.loom/critique/loom-git-skill-review.md`

Files updated:

- `skills/loom-ralph/SKILL.md`
- `skills/loom-ralph/references/work-driver.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/references/parent-child-handshake.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `commands/loom-work.md`
- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`

# Supports Claims

- ticket:h5j0wnkz#ACC-001

# Challenges Claims

None after the focused re-review. The initial critique challenged several parts
of the first draft; those were resolved before this evidence was finalized.

# Environment

Commit: 89ccccf
Branch: main
Runtime: Markdown-native Loom repository; no app runtime
OS: darwin
Relevant config: existing worktree had unrelated untracked `.claude-plugin/`
files before this work began

# Validity

Valid for: the uncommitted diff present at 2026-04-25T07:48:46Z
Recheck when: any `loom-git`, Ralph packet, `/loom-work`, or package framing
surface changes again

# Limitations

- There is no automated test suite in this repository.
- The oracle re-review focused on the prior findings, not every possible future
  Git topology.
- This evidence does not prove installer output in every harness; the installer
  copies skill directories generically, so no installer change was required.

# Result

The changed files passed tracked-diff whitespace checking, untracked Markdown
trailing-whitespace checks, targeted stale-assumption searches, and focused
critique re-review.

# Interpretation

The evidence supports that `loom-git` now teaches Git as a general integration
baseline and worktree isolation workflow rather than assuming `origin`, `main`,
GitHub, or this repository's shape.

# Related Records

- ticket:h5j0wnkz
- critique:loom-git-skill-review
