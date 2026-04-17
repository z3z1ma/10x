# Workspace Tree

A Loom-enabled project normally uses this canonical tree:

```text
.loom/
├── constitution/
│   ├── constitution.md
│   ├── decisions/
│   └── roadmap/
├── initiatives/
├── research/
├── specs/
├── plans/
├── tickets/
├── critique/
├── wiki/
├── packets/
│   ├── ralph/
│   ├── critique/
│   └── wiki/
├── evidence/
└── memory/
    ├── system/
    └── user/
```

## Bootstrap Command

```bash
mkdir -p \
  .loom/constitution/decisions \
  .loom/constitution/roadmap \
  .loom/initiatives \
  .loom/research \
  .loom/specs \
  .loom/plans \
  .loom/tickets \
  .loom/critique \
  .loom/wiki \
  .loom/packets/ralph \
  .loom/packets/critique \
  .loom/packets/wiki \
  .loom/evidence \
  .loom/memory/system \
  .loom/memory/user
```

## First Files Worth Creating

- `.loom/constitution/constitution.md`
- `.loom/harness.md` if the project wants repeatable fresh-context launch profiles
- the first initiative / plan / ticket chain required by the work

## Why This Tree Matters

The directory names carry semantic information.

That gives you:

- cheap discovery by path
- cheap cross-reference by `rg`
- clear ownership boundaries
- legible durable state without a runtime
