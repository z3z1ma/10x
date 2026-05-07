---
id: decision:0008
kind: decision
status: active
created_at: 2026-05-07T21:35:47Z
updated_at: 2026-05-07T21:43:18Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:split-core-and-playbooks-packages
  spec:
    - spec:core-and-playbooks-package-contract
  research:
    - research:core-workflow-plugin-split-feasibility
    - research:loom-install-distribution-methods
  decision:
    - decision:0004
    - decision:0005
    - decision:0006
    - decision:0007
  critique:
    - critique:core-playbooks-constitutional-decision-review
---

# Decision

Loom's distributable product surface will be split into two top-level,
self-contained package roots:

- `loom-core/`
- `loom-playbooks/`

Each package root owns its own `skills/` directory and the native harness plugin,
extension, hook, package, or metadata files needed to expose that package. The
current top-level `skills/` directory is retired as a product surface rather than
kept as a duplicate full bundle.

`loom-core/` owns the Loom kernel:

- `using-loom`
- `loom-workspace`
- `loom-records`
- `loom-memory`
- `loom-ralph`
- `loom-retrospective`
- canonical owner-layer skills for constitution, initiatives, research, specs,
  plans, tickets, evidence, critique, and wiki

Ralph remains core because compiling Loom graph artifacts into bounded packets
for fresh-context execution is part of Loom's transaction protocol. Retrospective
remains core because closure, promotion, and compounding discipline are part of
the protocol kernel. Memory remains core as support recall that helps operation
without becoming canonical project truth.

`loom-playbooks/` owns optional higher-level workflow playbooks that compose on
top of core Loom:

- `loom-drive`
- `loom-git`
- `loom-debugging`
- `loom-spike`
- `loom-codemap`
- `loom-ship`
- `loom-skill-authoring`

`loom-playbooks` requires `loom-core`. It must not duplicate core doctrine,
canonical owner-layer skills, record grammar, using-Loom references, Ralph, or
retrospective. Harnesses may not enforce this dependency mechanically, so package
metadata, marketplace descriptions, install docs, and playbook skill text should
state the dependency clearly.

Repository-level marketplace or catalog files may remain at the repository root
when a harness uses them to discover multiple package roots. Those catalogs are
discovery and transport surfaces only; they do not own Loom semantics.

# Why This Decision Exists

The single `skills/` surface made Loom easy to expose to early harness adapters,
but it now blurs two different product concepts:

- the core Loom kernel: canonical layers, shared record grammar, using-Loom
  doctrine, Ralph packets, retrospective closure, workspace orientation, and
  support recall
- optional playbooks: named engineering workflows that route through the core
  graph but should not be required for Loom to work

Users should be able to install only the core package and bring their own
workflow layer from another skill system, plugin, or local team practice. Users
who want Loom's opinionated workflow pack can install `loom-playbooks` as a
second package.

This also sharpens maintainer judgment. Core changes must preserve Loom's canon
and transaction kernel. Playbook changes may add or improve workflow routes as
long as they leave truth in core owner layers and depend on core instead of
creating another ontology.

Current harness evidence supports this direction at the packaging level:
Claude, Codex, and Cursor can use repository-level catalogs or marketplaces to
list multiple plugin roots; OpenCode can load multiple package/file plugins from
its plugin array; Gemini can conceptually install multiple extensions, though its
exact one-repository two-extension path still needs validation. Codex hooks now
also provide a documented `SessionStart` context surface that can support core
using-Loom preload once installed-plugin behavior is validated.

# Alternatives Considered

- Keep one top-level `skills/` package. Rejected because it prevents a truthful
  core-only install and keeps optional playbooks visually indistinguishable from
  Loom canon.
- Keep top-level `skills/` as a full compatibility bundle after adding package
  roots. Rejected because it would create a third product surface with high drift
  risk.
- Use `skills-core/` and `skills-workflows/` as bare skill roots. Rejected because
  supported harnesses need self-contained plugin or extension roots with their
  own metadata, not just separate skill directories.
- Place both packages under one internal `plugins/` directory. Rejected for now
  because the desired source shape is explicit top-level package roots named for
  the user-facing products.
- Make `loom-playbooks` standalone by copying core skills into it. Rejected
  because duplicate core doctrine and record grammar would violate the
  self-contained-skill intent by creating two competing copies of the kernel.
- Move Ralph to playbooks. Rejected because Ralph is the transaction protocol
  that turns graph truth into bounded packetized execution.
- Move retrospective to playbooks. Rejected because promotion and closure
  discipline are part of Loom's compounding mechanism, not a merely optional
  workflow add-on.

# Consequences

- `constitution:main`, public docs, install docs, architecture notes, AGENTS
  guidance, package manifests, examples, and references must stop describing
  top-level `skills/` as the product surface.
- `using-loom` remains the mandatory entry skill when doctrine has not already
  been loaded, but its package path moves under `loom-core/skills/using-loom/`.
- Native adapters should expose `loom-core/skills` and, when installed,
  `loom-playbooks/skills` through their native package mechanisms.
- OpenCode package work should target `open-loom-core` and
  `open-loom-playbooks`; the existing `open-loom` package needs separate
  migration or deprecation handling.
- Root-level catalog files may list both package roots for Claude, Codex, Cursor,
  or similar harnesses, but they are not semantic owners.
- `loom-playbooks` skill text must fail closed when core is absent instead of
  pretending playbooks can define Loom truth by themselves.
- The package split does not authorize a monolithic Loom CLI, hidden runtime,
  fallback shell installer, top-level command-wrapper product surface, or external
  system as Loom truth owner.
- Existing self-contained skill guidance still applies inside each package root:
  skills should be understandable from their own `SKILL.md`, references, and
  templates rather than hidden inheritance.
- Harness-specific validation remains required before docs claim a split package
  works in that harness. Gemini two-extension behavior and Codex installed-plugin
  hook behavior remain evidence needs, not assumed release facts.

# Revisit Conditions

Revisit this decision if:

- a supported harness cannot consume top-level package roots or multiple package
  roots without unsafe duplication
- `loom-playbooks` cannot practically depend on `loom-core` without hidden
  inheritance or copied doctrine
- empirical use shows core-only Loom is not understandable without installed
  playbooks
- marketplace packaging forces generated bundles to become semantic owners
- future harnesses converge on a cleaner multi-package skill distribution model
  that makes the top-level package-root layout unnecessarily heavy

# Supersession

This supersedes `decision:0006` as the active product-surface policy. It preserves
`decision:0006`'s rejection of fallback Makefile installers, shell installers,
and top-level command-wrapper product surfaces, but replaces the single top-level
`skills/` product surface with `loom-core/` and `loom-playbooks/`.

This narrows `decision:0005` only at the package path level: using-Loom doctrine
remains skill-packaged and mandatory, but its target package location is now
`loom-core/skills/using-loom/` rather than top-level `skills/using-loom/`.

This extends `decision:0004`: skills remain flat and self-contained, but the
product now has two self-contained package roots instead of one flat repository
root skill tree.

This updates `decision:0007`'s product-surface wording. Positive skill guidance
remains the writing standard, but it now applies to package-root skills under
`loom-core/skills` and `loom-playbooks/skills`.
