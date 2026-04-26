---
name: loom-bootstrap
description: "Mandatory: use this first in a Loom workspace when Loom doctrine is not already present in the current context. Seeing this skill means Loom is active; read this skill and its ordered references before any work unless an adapter has already loaded the same bootstrap doctrine earlier in the context window."
compatibility: Markdown-native, skill-packaged Loom protocol.
metadata:
  skill_kind: bootstrap
---

# loom-bootstrap

This is Loom's first skill.

Use it to load the mandatory operating doctrine that was formerly shipped as
top-level always-on rule files. Loom can be distributed as a skills package; this
skill is the package entry point that tells an agent how to become a Loom operator.

## What This Skill Owns

- initial Loom operating doctrine
- the mandatory first-read route for agents that do not already have Loom context
- the ordered bootstrap reference list
- the boundary between skill-package install and optional always-on adapter boosts

## What This Skill Does Not Own

- live execution state; tickets own that
- project policy; constitution records own that
- intended behavior contracts; specs own those
- evidence, critique, wiki, packets, or memory truth
- harness adapter mechanics beyond naming the expected bootstrap contract

## Mandatory Bootstrap Rule

If Loom is active and the ordered bootstrap doctrine is not already in your current
context, read the references below before doing any work.

If a harness adapter has already loaded these same references into the current
context, do not waste context rereading them. Treat this skill as the index and
continue using the loaded doctrine.

If you are unsure whether the doctrine is loaded, fail closed: read the references
in order.

## Read In This Order

Read immediately for normal Loom use unless the same ordered doctrine is already
present earlier in the context window:

1. `references/01-core-identity.md`
2. `references/02-truth-and-authority.md`
3. `references/03-outer-loop.md`
4. `references/04-ralph-inner-loop.md`
5. `references/05-critique-and-wiki.md`
6. `references/06-filesystem-and-tooling.md`
7. `references/07-validation-and-honesty.md`

Then activate the task-specific Loom skill that owns the next truth change.

## Suggested Harness Instruction

For harnesses with a project instruction file such as `AGENTS.md`, `CLAUDE.md`,
`GEMINI.md`, or equivalent, use wording like:

```md
Loom is active in this workspace. Before any work, use the `loom-bootstrap` skill
unless Loom's ordered bootstrap doctrine is already loaded in the current context.
After bootstrap, route work through the Loom skill that owns the next truth
change.
```

This instruction is a pointer, not a new source of truth. The bootstrap doctrine
lives in this skill's ordered references.

## Adapter Guidance

Harness adapters may preload these references as always-on context when the
harness supports it cleanly. That is a performance and reliability boost, not a
different protocol.

When an adapter preloads bootstrap context, it should preserve source markers or
paths that identify the ordered references so future operators can tell which
doctrine was loaded.
