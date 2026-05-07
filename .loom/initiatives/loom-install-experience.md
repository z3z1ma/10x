---
id: initiative:loom-install-experience
kind: initiative
status: active
created_at: 2026-04-25T18:25:20Z
updated_at: 2026-05-07T19:30:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  plan:
    - plan:install-experience-harness-adapters
  research:
    - research:loom-install-distribution-methods
    - research:harness-install-surfaces
    - research:codex-command-skill-installation
    - research:codex-plugin-distribution-surfaces
  spec:
    - spec:opencode-plugin-install-contract
  wiki:
    - wiki:harness-adapter-package-pattern
  ticket:
    - ticket:6uy1rx20
    - ticket:us1brnsv
    - ticket:q7h1d05q
    - ticket:cldrel01
    - ticket:lx9nnztk
    - ticket:7ex8w32y
    - ticket:3t93tsci
    - ticket:ffg8elkb
    - ticket:p9m4x2qt
    - ticket:rd48g1kg
  evidence:
    - evidence:open-loom-smoke
    - evidence:cursor-harness-install-validation
    - evidence:claude-plugin-hybrid
    - evidence:claude-sessionstart-stdout-context
    - evidence:codex-sessionstart-stdout-context
  decision:
    - decision:0005
    - decision:0006
  critique:
    - critique:codex-plugin-hook-config-review
---

# Objective

Make Loom installation feel first-class in every supported harness while keeping
the product itself a Markdown-native protocol bundle rather than a runtime,
daemon, MCP, dashboard, or monolithic product CLI.

The outcome is not a shell script. The desired result is a clear, maintainable
install strategy that maps Loom's canonical `skills/` package into each harness
through the most honest native mechanism available.

# Why Now

The earlier `Makefile` and `scripts/install-loom.sh` proved that user-level global
copy installs were possible, but `decision:0006` rejects that as product shape.
The work now moves to native plugin, extension, or skill-package installs only.

Meanwhile, several harnesses now expose richer first-class distribution systems:
Claude Code plugins, Codex plugins, Gemini CLI extensions, Cursor plugins, and
portable Agent Skills. Loom needs to use those native surfaces while keeping
`skills/` as the product source of truth.

# In Scope

- compare supported harness install surfaces for OpenCode, Claude Code, Codex,
  Gemini CLI, and Cursor
- evaluate first-class plugin, extension, marketplace, and Agent Skills surfaces
  where they exist
- evaluate native skill/plugin installs and generic Agent Skills installs
- compare popular installer precedents such as package managers, standalone
  shell installers, project scaffolders, extension marketplaces, and manual Git
  clone/link workflows
- define the qualities of a better Loom install experience without committing to
  an implementation prematurely
- keep removed installer behavior only as prior evidence, not as a supported path

# Out Of Scope

- creating a required `loom` CLI
- adding a daemon, service, model router, MCP server, dashboard, or hidden
  installer runtime as protocol core
- changing Loom's canonical shipped product surfaces to fit one harness better
- making command wrappers part of Loom product surface
- treating plugin manifests, generated adapter files, or package-manager recipes
  as owners of Loom semantics
- installing dogfooding `.loom/` records or `.opencode/` consumption state into
  downstream users

# Success Metrics

- a future maintainer can explain the recommended native install path for each
  supported harness from `INSTALL.md`
- each supported harness has a documented native install mechanism or an explicit
  accepted decision not to support that harness yet
- first-class plugin, extension, or skill-package systems are used to cover Loom
  skills, and explicitly rejected where they do not
- `using-loom` is discoverable after install, and adapters preload its ordered
  references only where that is supported cleanly
- skill discovery preserves portable Agent Skills semantics and keeps full skill
  content on-demand
- disable/uninstall follows native harness package behavior
- adapter outputs are easy to inspect with ordinary filesystem tools
- no install strategy makes a generated file, fallback script, or marketplace
  package the authority for Loom behavior

# Milestones

1. Preserve broad install-method research that compares native harness surfaces,
   plugin systems, and installer precedents.
2. Decide the preferred install class for each supported harness: plugin or
   extension package, direct config install, generic Agent Skills install, or a
   hybrid.
3. Define adapter fixture expectations for each chosen path so install behavior
   can be reviewed without relying on transcript context.
4. Remove fallback installer and command-wrapper product surfaces.
5. Update `INSTALL.md` and adapter examples to reflect native skill-package
   strategy.

# Dependencies

- `constitution:main`, especially the constraints against a monolithic Loom CLI,
  hidden runtime, and helper-owned ontology
- `research:loom-install-distribution-methods` for broad install-surface and
  installer-precedent analysis
- `research:harness-install-surfaces` for the earlier concrete path mapping
- `research:codex-command-skill-installation` for the Codex command adapter
  decision
- `research:codex-plugin-distribution-surfaces` for the current Codex plugin and
  marketplace surface assessment
- `ticket:ffg8elkb`, `ticket:p9m4x2qt`, and `ticket:rd48g1kg` for prior
  implementation and validation history
- current official harness docs, because plugin and skill surfaces are changing
  quickly

# Risks

- overcorrecting from a fragile script into a hidden runtime or product CLI that
  violates Loom's constitutional boundary
- choosing plugin packaging because it feels more first-class even when it does
  not provide a clean always-on instruction surface
- letting generated adapter packages drift from canonical `skills/` and
  `using-loom` references
- losing uninstall safety when a harness stores user rules in a non-file config
  database or managed settings surface
- treating generic Agent Skills as sufficient while forgetting that
  `using-loom` must be used first unless an adapter has already loaded it
- expanding install support faster than the project can maintain evidence for
  each harness

# Linked Work

- Plan: `plan:install-experience-harness-adapters`
- Research: `research:loom-install-distribution-methods`
- Prior research: `research:harness-install-surfaces`
- Prior research: `research:codex-command-skill-installation`
- Focused research: `research:codex-plugin-distribution-surfaces`
- Harness ticket: `ticket:6uy1rx20` - validate `open-loom` OpenCode plugin-first install
- Follow-up ticket: `ticket:us1brnsv` - investigate OpenCode cold-cache
  npm-plugin first-run behavior
- Spec: `spec:opencode-plugin-install-contract`
- Wiki: `wiki:harness-adapter-package-pattern`
- Harness ticket: `ticket:q7h1d05q` - prototype Claude Code hybrid install
- Follow-up ticket: `ticket:cldrel01` - harden Claude release packaging before
  broad marketplace distribution
- Claude evidence: `evidence:claude-plugin-hybrid`
- Codex evidence: `evidence:codex-sessionstart-stdout-context`
- Harness ticket: `ticket:lx9nnztk` - blocked Codex remote plugin install
  investigation
- Harness ticket: `ticket:7ex8w32y` - prototype Gemini CLI extension install
- Harness ticket: `ticket:3t93tsci` - prototype Cursor plugin install
- Prior ticket: `ticket:ffg8elkb` - add global harness install Makefile
- Prior ticket: `ticket:p9m4x2qt` - install Codex command adapters as skills
- Prior ticket: `ticket:rd48g1kg` - add Cursor harness install support
- Prior evidence: `evidence:cursor-harness-install-validation`

# Status Summary

This initiative is active. After `decision:0006`, the execution plan targets
harness-native skill or plugin package paths only. The removed Makefile, shell
installer, and top-level command wrappers are historical evidence, not supported
surfaces.

The OpenCode slice has landed the first accepted package-adapter result:
`open-loom@0.1.0` validates a plugin-array install for OpenCode `>=1.14.22 <2`,
exposes `skills/`, and preloads using-Loom references through OpenCode
`instructions`. The remaining OpenCode cold-cache first-run package caveat is
tracked by `ticket:us1brnsv`.

The Claude slice has closed its local/prototype ticket and advanced the release
path through `ticket:cldrel01`: marketplace and plugin for `skills/`, plus
same-session, source-marked per-reference `SessionStart` stdout for optional
using-Loom preload. Remaining Claude release risks are installed marketplace
behavior, package/cache contents, Windows shell behavior, `clear|compact` runtime
events, and installed skill invocation.

The Codex slice has been re-researched against current plugin and hook docs plus
open-source Codex source: Codex plugins are the intended native path for canonical
skills, and Codex config-layer `SessionStart` hooks can emit source-marked
using-Loom references as optional same-session context. Current evidence does not
prove installed Git-backed plugin skill discovery for `using-loom`, so
`ticket:lx9nnztk` remains active for the intended remote plugin install goal.

# Completion Basis

When this initiative is completed, the graph should show a researched,
per-harness native install strategy and any resulting implementation tickets
should have evidence that package enable/disable behavior is harness-appropriate
and still subordinate to Loom's Markdown protocol corpus.
