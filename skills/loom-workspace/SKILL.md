---
name: loom-workspace
description: "Enter a Loom workspace safely: discover structure, bootstrap the tree, resolve ownership, read constitution first, and route to the correct subsystem before downstream work. Use when the next owner layer is unclear, the workspace may be uninitialized, scope looks ambiguous, or you need to decide whether the next move is outer-loop framing, Ralph execution, critique, or wiki."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  loom_layer: control-plane
  protocol_version: "2.0"
---

# loom-workspace

Use this skill first when you are entering a Loom repository cold or when the next owner layer is not yet obvious.

This skill replaces the old "doctor", "status", and "scope helper" mindset with a more agent-native posture:
inspect the workspace directly, make structural trust explicit, then route to the owning layer.

## What This Skill Owns

- workspace bootstrap
- workspace diagnosis
- repository / scope discovery
- first-read order
- subsystem routing

## First Read Order

When Loom is present and the repo looks structurally plausible:

1. inspect `.loom/`
2. read `constitution:main`
3. read the obvious owner chain for the current task
4. choose the next skill

Do not start deep work before the workspace is structurally trustworthy enough to trust its records.

## Use This Skill When

- `.loom/` is missing, partial, or suspicious
- the target path may belong to one of several repositories
- you do not yet know whether the task belongs to constitution, research, spec, plan, ticket, Ralph, critique, or wiki
- the user asked to set up Loom in a repository
- the workspace needs a health pass before packet work

## Do Not Use This Skill When

- the owner layer is already obvious and structurally sound
- you are already inside a bounded ticket iteration and only need the owning execution skill

## Default Workspace Procedure

1. confirm the workspace root
2. inspect the `.loom/` tree and read order
3. verify `constitution:main` exists or create it if the user is bootstrapping Loom
4. verify the canonical subdirectories exist
5. resolve repository ownership of the target path
6. read the governing artifact chain
7. route into the next owner skill

## Signals That You Should Halt Or Escalate

Halt or escalate when:

- the workspace root is ambiguous
- multiple repository owners look plausible for the same target path
- `.loom/` exists but the canonical tree is malformed enough that you cannot trust it
- the task would require widening scope without a ticket/plan update

## Native Tool Posture

Prefer direct inspection before inventing a helper abstraction:

- `find` / `fd` for tree discovery
- `rg` for IDs, statuses, and refs
- `git rev-parse --show-toplevel` for repository ownership
- `git status --short` and `git diff --stat` for current mutation awareness

## Done Means

- the workspace root is explicit
- structural trust is explicit
- the next owner skill is explicit
- you are not guessing about scope or routing

## Read In This Order

1. `references/workspace-tree.md`
2. `references/routing.md`
3. `references/doctor.md`
4. `templates/harness.md` when fresh-context invocation needs documenting
