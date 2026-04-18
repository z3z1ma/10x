# loom-setup

Use this command to initialize or repair a Loom workspace. Trigger if the user
says "set up loom", "initialize loom", "bootstrap loom", "create the loom
directory", or similar workspace-setup requests.

This command is pure prompt guidance. It should be executable by the model from
the visible Loom bundle and normal file tools alone.

## Goal

Create or repair the canonical `.loom/` scaffold so the workspace has the
expected directories and starter files for canonical records, packets,
evidence, optional memory, and harness invocation.

Prefer additive repair over replacement:

- create missing paths and files
- preserve existing Loom content unless the user explicitly asked to replace it
- if a file already exists, do not overwrite it just to match a template

## 0. Resolve Scope First

1. Resolve the workspace root using Loom's normal rule:
   - prefer the nearest ancestor containing both `.git/` and `.loom/`
   - if no established workspace exists yet, use the current working directory
     unless it is a non-root subdirectory of a git repository
   - if the current working directory is a non-root subdirectory of a git
     repository and no established workspace exists above it, fail closed and
     ask the user which repository root should own the workspace
2. Inspect the current `.loom/` state before writing anything.
3. Treat existing records and memory files as user data. Fill gaps; do not
   reset them.
4. After resolving the workspace root, resolve target repository ownership
   separately when the workspace contains nested repositories.

## 1. Create The Canonical Directory Tree

Ensure these directories exist:

```text
.loom/
.loom/constitution/
.loom/constitution/decisions/
.loom/constitution/roadmap/
.loom/initiatives/
.loom/research/
.loom/specs/
.loom/plans/
.loom/tickets/
.loom/critique/
.loom/wiki/
.loom/packets/
.loom/packets/ralph/
.loom/packets/critique/
.loom/packets/wiki/
.loom/evidence/
.loom/memory/
.loom/memory/system/
.loom/memory/user/
```

## 2. Seed Required Starter Files

Create each file below only if it is missing.

### `.loom/harness.md`

Use `skills/loom-workspace/templates/harness.md` as the starter shape.

### `.loom/constitution/constitution.md`

Use `skills/loom-constitution/templates/constitution.md` as the starter shape.

If you create it, fill in:

- `created_at` and `updated_at` with the current UTC timestamp
- `scope.kind: workspace`
- the exact section headings from the template

### Optional memory starter files

If the workspace does not already have a memory surface, seed the default
domains and common files from `loom-memory`:

- `.loom/memory/system/hot-memory.md`
- `.loom/memory/system/observations.md`
- `.loom/memory/system/entities.md`
- `.loom/memory/system/action-items.md`
- `.loom/memory/user/hot-memory.md`
- `.loom/memory/user/observations.md`
- `.loom/memory/user/entities.md`
- `.loom/memory/user/action-items.md`

Starter shape for each `hot-memory.md`:

```markdown
<!-- L0: Small, current, high-signal memory -->
# Hot Memory

- Add current high-signal notes here.
```

Starter shape for each `observations.md`:

```markdown
<!-- L0: Append-only notable facts -->
# Observations
```

Starter shape for each `entities.md`:

```markdown
<!-- L0: Compact registry of recurring people, systems, or topics -->
# Entities
```

Starter shape for each `action-items.md`:

```markdown
<!-- L0: Support tasks that are not canonical Loom tickets -->
# Action Items
```

## 3. Repair Rules While Seeding

While creating the scaffold:

1. Preserve existing files when they already contain user data.
2. Seed a required memory file with starter content when it exists but is empty.
3. Add the `<!-- L0: ... -->` header to an existing memory file when it is
   missing and preserve the rest of the file.
4. Preserve operator-defined profiles in `.loom/harness.md`.
5. Preserve `.loom/constitution/constitution.md` unless the user explicitly
   asked for a reset.

## 4. Verify The Setup

After writing, verify that:

1. every directory in the tree above exists
2. every starter file you intended to create now exists
3. any newly created Loom record uses YAML frontmatter and the expected section
   headings from its template
4. every active memory Markdown file you created starts with an `<!-- L0: ... -->`
   header
5. the scaffold uses `.loom/wiki/`, `.loom/packets/`, `.loom/evidence/`, and
   `.loom/memory/` rather than the retired `docs`/`runs`/`verification`/
   `memories` layout

## 5. Response Contract

When you finish:

1. list every directory you created
2. list every file you created
3. list any existing files you preserved unchanged
4. call out any malformed pre-existing files you could not safely repair
   without user guidance

This command is complete only when both the directory scaffold and the starter
file layer exist, especially `.loom/constitution/constitution.md`, the packet
and evidence directories, and any memory files you chose to seed.
