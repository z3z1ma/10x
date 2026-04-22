---
id: evidence:cursor-harness-install-validation
kind: evidence
status: recorded
created_at: 2026-04-22T20:51:34Z
updated_at: 2026-04-22T20:51:34Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:rd48g1kg
  research:
    - research:harness-install-surfaces
external_refs: {}
---

# Summary

Validation for adding Cursor to the Loom installer.

# Procedure

- Ran `bash -n scripts/install-loom.sh`.
- Ran `git diff --check`.
- Ran `HOME=<tmp> make install harness=cursor`.
- Inspected the temporary Cursor install tree.
- Inspected the generated Cursor User Rules managed block and generated
  `loom-review` command.
- Ran `HOME=<tmp> make uninstall harness=cursor`.
- Verified Cursor uninstall preserved an existing non-Loom User Rules value.
- Ran `HOME=<tmp> make install harness=all` and verified Cursor participates in
  aggregate install.
- Ran `HOME=<tmp> make uninstall harness=all`.
- Ran an `id` / `status` frontmatter spot-check on the changed Loom records.

# Artifacts

- Cursor install created:
  - `<tmp>/.cursor/loom/rules/01-core-identity.md` through
    `<tmp>/.cursor/loom/rules/07-validation-and-honesty.md`
  - `<tmp>/.cursor/loom/cursor-user-rules.md`
  - a managed Loom block in Cursor User Rules
  - copied protocol skill directories under `<tmp>/.cursor/skills/`
  - generated command Markdown files under `<tmp>/.cursor/commands/`
- The managed Cursor User Rules block embeds the installed rule corpus.
- Generated `loom-review.md` command strips source frontmatter and replaces
  `$ARGUMENTS` with `<invocation request>`.
- Cursor uninstall removed the Loom-managed Cursor files in the temporary home.
- Cursor uninstall removed the Loom managed User Rules block while preserving
  unrelated User Rules text.
- Aggregate install/uninstall completed for OpenCode, Claude Code, Codex,
  Gemini CLI, and Cursor.

# Supports Claims

- ticket:rd48g1kg#cursor-install-surface

# Challenges Claims

- none

# Environment

Commit: d841a5771b3272dd3d1ddd74e1f4b3ae0253ae93
Branch: main
Runtime: Bash, Python 3 via `PYTHON_BIN`
OS: Darwin 24.6.0 arm64
Relevant config: temporary `HOME` directories created with `mktemp -d`

# Validity

Valid for: the installer implementation at the recorded commit plus current
working-tree changes.

Recheck when: Cursor changes skill or command discovery paths, or when
`scripts/install-loom.sh` changes.

# Limitations

This evidence proves filesystem generation, managed User Rules mutation, and
cleanup behavior. It does not prove that the Cursor UI will display or invoke
the generated command and skill surfaces in every Cursor version or remote
environment.

# Result

All validation commands completed successfully.

# Interpretation

The Cursor harness adapter installs Loom rules into Cursor User Rules and is
reversible in an isolated home directory. Runtime Cursor UI discovery for
commands and skills remains dependent on Cursor's current product behavior.

# Related Records

- ticket:rd48g1kg
- research:harness-install-surfaces
