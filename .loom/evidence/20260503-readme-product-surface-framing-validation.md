---
id: evidence:readme-product-surface-framing-validation
kind: evidence
status: recorded
created_at: 2026-05-03T00:16:25Z
updated_at: 2026-05-03T00:16:25Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:readme11
  packet:
    - packet:ralph-ticket-readme11-20260503T001418Z
external_refs: {}
---

# Summary

Observed README framing before and after the `ticket:readme11` Ralph edit, then
ran `git diff --check` against the resulting worktree diff.

# Procedure

Timestamp: 2026-05-03T00:16:25Z.

Before editing `README.md`, ran:

```bash
git rev-parse HEAD
git status --short
rg -n -i 'product surface|product-surface|package product surface' README.md
rg -n -i 'skills/|skill package|skills package|skills-aware|skills-directory|skill map|loom-bootstrap|loom-memory' README.md
rg -n -i 'support|support surfaces|support artifacts|optional utilities|memory|packets' README.md
rg -n -i 'adapter|harness|manifest|transport' README.md
rg -n -i 'example|examples|fixtures' README.md
rg -n -i 'ships|included|package|packaging|runtime|service|daemon|cli|mcp|workflow engine|hidden database|optional utilities' README.md
rg -n -i 'truth owner|truth-owner|owner layer|owning|canonical|source-of-truth|shadow truth|protocol truth|own project truth|owning project truth|define semantics|do not define semantics|not project truth|not canonical truth|not product surface' README.md
```

After editing `README.md`, ran the same README searches, with the truth-owner
query also including `not a separate product surface|not doctrine sources`.

Then ran:

```bash
git diff --check
```

# Artifacts

## Source fingerprint check

- `git rev-parse HEAD` returned
  `2de8a2ec0f84a8867c1c3e223bc9d0216c774cd6`, matching the packet baseline.
- `git status --short` showed pre-existing in-scope Loom handoff changes:
  modified `ticket:readme11` and untracked Ralph packet file.

## Before README searches

- Product-surface query found `README.md:491` saying internal examples are not
  product-surface guidance, `README.md:493` saying the product surface is the
  skill package, and `README.md:535` saying `examples/` is not product surface or
  project records.
- `skills/` query found install and package references, including
  `README.md:101` exposing `skills/`, `README.md:482` calling `skills/` the
  canonical Loom surface, `README.md:493` saying skills are the protocol in
  operational form, and `README.md:537` calling `skills/` the canonical Loom
  skill package.
- Support query found existing support-surface boundaries for packets, memory,
  and `.loom/support/`, including `README.md:155-158`, `README.md:216-222`, and
  `README.md:563`.
- Adapter query found `README.md:468` saying harness adapters are not a second
  doctrine source, but `README.md:488` only said harness manifests and adapters
  are included where useful.
- Examples query found `README.md:491` and `README.md:535` keeping examples as
  maintainer/internal fixtures rather than product surface.
- Packaging query found `README.md:474-493` describing what ships and what Loom is
  not, but no explicit packaging-file support boundary.
- Truth-owner query found existing owner-layer boundaries and support-surface
  wording, but the `What ships` list still mixed `skills/`, support docs,
  harness adapters, architecture notes, and examples before the final product
  surface sentence.

## After README searches

- Product-surface query found `README.md:478` naming the package product surface
  as top-level `skills/`, `README.md:487` naming `skills/` as package product
  surface and canonical skill corpus, `README.md:494` saying `PROTOCOL.md` is not
  a separate product surface, and `README.md:499` saying the product surface is
  `skills/`.
- `skills/` query found the original install mechanics unchanged at
  `README.md:101-116`, plus the new product-surface wording at `README.md:478`,
  `README.md:487`, and `README.md:499`.
- Support query found the existing packet/memory/support boundaries and new
  `README.md:478-481`, which says support docs, harness manifests/adapters,
  examples, packaging files, packets, memory, and saved support artifacts do not
  own protocol truth.
- Adapter query found `README.md:493` framing harness manifests and adapters as
  install/transport support, not doctrine sources.
- Examples query found `README.md:497` saying internal examples and fixtures are
  not product-surface guidance or protocol truth, and `README.md:541` preserving
  the repository-layout fixture note.
- Packaging query found `README.md:496` naming packaging files and repository
  metadata as distribution and maintainer workflow support.
- Truth-owner query found `README.md:481` saying support surfaces do not own
  protocol truth, `README.md:493` saying adapters are not doctrine sources,
  `README.md:494` saying `PROTOCOL.md` is not a separate product surface, and
  `README.md:497` saying examples are not protocol truth.

## `git diff --check`

- Command: `git diff --check`
- Result: exit 0; no output.

# Supports Claims

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-011`
- `ticket:readme11#ACC-001`
- `ticket:readme11#ACC-002`
- `ticket:readme11#ACC-003`
- `ticket:readme11#ACC-004`

# Challenges Claims

None - the observations did not challenge the listed claims.

# Environment

Commit: `2de8a2ec0f84a8867c1c3e223bc9d0216c774cd6`
Branch: `main`
Runtime: Markdown/file-tool Ralph child execution
OS: darwin
Relevant config: packet `packet:ralph-ticket-readme11-20260503T001418Z` with
`verification_posture: observation-first`

# Validity

Valid for: README product-surface/support-surface framing at the observed diff.
Fresh enough for: routing `ticket:readme11` to mandatory critique.
Recheck when: README wording changes again, package framing changes, or critique
requires a revised diff.
Invalidated by: edits that change README product-surface, support-surface,
adapter, example, packaging, packet, memory, or `.loom/support/` framing.
Supersedes / superseded by: None.

# Limitations

This evidence records README search observations and whitespace validation. It
does not establish oracle critique acceptance, public-reader comprehension, or
consistency across every support document.

# Result

The after-state README searches show `skills/` named as the package product
surface and support docs/adapters/examples/packaging files/packets/memory/saved
support artifacts framed as non-truth-owner support. `git diff --check` passed
with no output.

# Interpretation

The observations support moving `ticket:readme11` to mandatory critique. They do
not justify closing the ticket until the required oracle critique and acceptance
disposition are reconciled.

# Related Records

- `ticket:readme11`
- `packet:ralph-ticket-readme11-20260503T001418Z`
