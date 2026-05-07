---
id: spec:opencode-plugin-install-contract
kind: spec
status: superseded
created_at: 2026-04-25T22:14:57Z
updated_at: 2026-05-07T23:49:27Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  ticket:
    - ticket:6uy1rx20
    - ticket:us1brnsv
  evidence:
    - evidence:open-loom-smoke
  critique:
    - critique:open-loom-config-hook-review
    - critique:core-playbooks-package-contract-review
  research:
    - research:loom-install-distribution-methods
  decision:
    - decision:0005
    - decision:0006
    - decision:0008
  spec:
    - spec:core-and-playbooks-package-contract
external_refs:
  opencode_docs:
    - https://opencode.ai/docs/plugins/
    - https://opencode.ai/docs/config/
    - https://opencode.ai/docs/skills/
    - https://opencode.ai/docs/commands/
---

# Supersession Note

2026-05-07: `decision:0008` and
`spec:core-and-playbooks-package-contract` supersede this as the active future
OpenCode package target. This record remains historical evidence for the accepted
`open-loom@0.1.0` single-package behavior on OpenCode `>=1.14.22 <2` before the
core/playbooks split. New OpenCode split work should target
`@z3z1ma/open-loom-core` and `@z3z1ma/open-loom-playbooks`, not extend this
single-package contract as current product truth.

# Summary

Define the accepted behavior contract for the OpenCode `open-loom` install path.

This contract applies to OpenCode `>=1.14.22 <2`, matching the published package
metadata for `open-loom@0.1.0`.

# Problem

OpenCode originally had a direct-copy install path. After `decision:0006`, the
accepted product direction is a native OpenCode plugin that exposes canonical
`skills/` and optionally preloads `using-loom` references without creating a
second semantic source of truth.

# Desired Behavior

A normal OpenCode user should be able to configure Loom by adding
`open-loom@0.1.0` or a compatible future `open-loom` package version to
OpenCode's `plugin` array.

When OpenCode loads the plugin, `open-loom` should expose the package's canonical
Markdown surfaces through OpenCode's documented config surfaces:

- ordered `using-loom` references through `config.instructions`
- bundled skills through `config.skills.paths`

Users who clone the repository should be able to point OpenCode at a local file or
package-root plugin path instead of installing from npm.

# Constraints

- `skills/` is the source package surface; package metadata and plugin
  registration do not own Loom semantics.
- The plugin must read bundled files relative to the package or clone location,
  not from dogfooding `.opencode/` or `.loom/` paths.
- Git URL plugin specs are not a supported recommendation for OpenCode because
  current validation found them unsupported in practice.
- The published package must declare the OpenCode compatibility range it was
  validated against.
- Cold-cache first-run npm-plugin behavior is a known OpenCode `1.14.22`
  limitation until `ticket:us1brnsv` resolves it.

# Requirements

- REQ-001: The npm package entrypoint is `open-loom.mjs` and default-exports an
  OpenCode plugin object with `id: "open-loom"` and `server()`.
- REQ-002: The plugin registers ordered
  `skills/using-loom/references/*.md` files as absolute `config.instructions`
  paths.
- REQ-003: The plugin registers the bundled `skills/` root in
  `config.skills.paths` when bundled skills exist.
- REQ-004: The plugin does not register a command-wrapper product surface.
- REQ-005: Missing removed `rules/` or `commands/` directories must not make
  bundle inspection or config registration fail.
- REQ-006: Local clone usage supports a `file://.../open-loom.mjs` or local
  package-root plugin entry.
- REQ-007: The package declares `engines.opencode: >=1.14.22 <2` unless newer
  evidence changes the compatibility contract.
- REQ-008: Install documentation rejects Git URL plugin specs as the normal
  OpenCode path unless future runtime evidence proves support.
- REQ-009: Published package contents include the plugin, `skills/`, and public
  docs needed by the install guide; they do not include top-level `rules/`,
  `commands/`, Makefile, or shell installer surfaces.

# Scenarios

- Npm package user adds `"plugin": ["open-loom@0.1.0"]` to an OpenCode config
  file and OpenCode loads using-Loom references and skills from its package
  cache.
- Repository clone user points OpenCode at `file:///path/to/agent-loom/open-loom.mjs`
  and OpenCode loads the same Loom surfaces from the clone.
- Contributor runs `node open-loom.mjs --smoke` to verify ordered using-Loom
  references, skill path registration, and dedupe behavior without making a model
  request.
- A package without removed `rules/` or `commands/` directories still registers
  using-Loom references and skills without crashing.
- A first cold-cache npm-package run logs `NpmInstallFailedError`; the user runs
  OpenCode again and the cached package resolves. Further investigation belongs to
  `ticket:us1brnsv`.

# Acceptance

- ACC-001: `node open-loom.mjs --smoke` shows eight ordered using-Loom reference
  files and a bundled skill path, with no command-wrapper registration.
- ACC-002: `opencode debug config` with a local plugin file or package-root entry
  shows ordered using-Loom reference paths in `instructions` and a Loom
  `skills.paths` entry.
- ACC-003: `opencode debug skill` discovers Loom skills from the registered
  OpenCode skill path.
- ACC-004: `npm run pack:check` confirms the package dry-run includes all
  published support surfaces used by the install docs.
- ACC-005: `npm view open-loom name version dist-tags engines license --json`
  confirms the published package metadata.
- ACC-006: The ticket acceptance gate records any known OpenCode runtime caveat
  as accepted risk or a linked follow-up before closing the OpenCode ticket.

# Open Questions

- Is the cold-cache first-run `NpmInstallFailedError` caused by OpenCode's npm
  installer, package metadata, config-file load timing, or another factor?
- Should future `open-loom` package versions keep examples in the published
  tarball or move adapter fixture details into external docs once package install
  stabilizes?
- Should `open-loom` eventually support additional OpenCode versions outside
  `>=1.14.22 <2`?
