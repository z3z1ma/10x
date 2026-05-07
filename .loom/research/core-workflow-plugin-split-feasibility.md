---
id: research:core-workflow-plugin-split-feasibility
kind: research
status: active
created_at: 2026-05-07T20:42:59Z
updated_at: 2026-05-07T21:51:37Z
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
  ticket:
    - ticket:hi5e7nbr
  research:
    - research:loom-install-distribution-methods
    - research:codex-plugin-distribution-surfaces
  decision:
    - decision:0004
    - decision:0005
    - decision:0006
    - decision:0008
  critique:
    - critique:core-playbooks-package-contract-review
    - critique:core-playbooks-constitutional-decision-review
external_refs:
  claude_code:
    - https://code.claude.com/docs/en/plugins-reference
    - https://code.claude.com/docs/en/plugin-marketplaces
  codex:
    - https://developers.openai.com/codex/plugins/build
    - https://developers.openai.com/codex/plugins
    - https://developers.openai.com/codex/hooks
  opencode:
    - https://opencode.ai/docs/plugins/
  gemini_cli:
    - https://geminicli.com/docs/extensions/reference/
    - https://geminicli.com/docs/extensions/
  cursor:
    - https://cursor.com/docs/reference/plugins
    - https://cursor.com/docs/plugins
  agent_skills:
    - https://agentskills.io/specification
---

# Question

Can Loom split its shipped skill corpus into two installable plugin packages: a
core plugin for canonical owner layers plus shared record/workspace/using-Loom
operation, and a workflow plugin for optional higher-level engineering workflows
that compose on top of the canonical layers?

# Why This Matters

The current product surface is a single top-level `skills/` corpus. That makes
Loom easy to expose to harnesses, but it blurs two product concepts:

- the canonical Loom layer system and shared record grammar
- optional workflow coordinators such as Ralph, debugging, spike, codemap, ship,
  retrospective, Git isolation, and objective driving

A split package would let users install the Loom canonical layer discipline
without adopting Loom's opinionated workflow pack. It would also let maintainers
reason more clearly about what is canon and what is merely a workflow built on
canon.

# Scope

Covered:

- current repository product constraints and install records
- supported harnesses named by `INSTALL.md`: Claude Code, OpenCode, Codex,
  Cursor, Gemini CLI, and generic skills-directory installs
- official harness docs fetched on 2026-05-07 for plugin, extension, marketplace,
  and Agent Skills surfaces
- initial skill-boundary classification for a core/workflow split

Excluded:

- implementation changes to repo layout, manifests, package metadata, or docs
- runtime validation inside any harness
- final naming, versioning, publication, migration, or compatibility policy
- constitutional acceptance of the split

# Method

- Read `constitution:main`, `decision:0004`, `decision:0006`, `README.md`,
  `INSTALL.md`, `ARCHITECTURE.md`, `PROTOCOL.md`, existing harness manifests,
  `open-loom.mjs`, and linked install research/plan records.
- Fetched current official docs for the supported harness plugin/extension and
  hook surfaces and extracted only facts relevant to multi-plugin packaging,
  skills paths, and optional using-Loom preload.
- Searched the skill corpus for cross-skill references that would matter if a
  core-only install lacks workflow skills.

# Sources

- Source: `constitution:main`
  - Type / provenance: project-owned constitution record
  - Observed at / version: 2026-05-07 local workspace
  - Freshness risk / recheck trigger: recheck before changing product-surface policy
  - Trust rationale: owns Loom product identity and constraints for this repository
- Source: `decision:0004`, `decision:0005`, `decision:0006`
  - Type / provenance: project-owned constitutional decision records
  - Observed at / version: 2026-05-07 local workspace
  - Freshness risk / recheck trigger: recheck if superseded or amended
  - Trust rationale: active decisions constrain self-contained flat skills and native adapter packaging
- Source: `research:loom-install-distribution-methods` and `research:codex-plugin-distribution-surfaces`
  - Type / provenance: project-owned research records
  - Observed at / version: 2026-05-07 local workspace
  - Freshness risk / recheck trigger: recheck harness docs/runtime before implementation
  - Trust rationale: existing citable install-surface synthesis, with noted evidence gaps
- Source: local manifests `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json`, `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`, and `open-loom.mjs`
  - Type / provenance: repository source files
  - Observed at / version: 2026-05-07 local workspace
  - Freshness risk / recheck trigger: recheck after any adapter layout change
  - Trust rationale: current implementation reality for package surfaces
- Source: official harness docs listed in `external_refs`
  - Type / provenance: vendor documentation fetched with web extraction
  - Observed at / version: 2026-05-07
  - Freshness risk / recheck trigger: recheck before implementation because plugin systems are moving quickly
  - Trust rationale: primary source for documented plugin/extension schemas, with runtime gaps explicitly noted
- Source: Agent Skills specification
  - Type / provenance: public skill format specification
  - Observed at / version: 2026-05-07
  - Freshness risk / recheck trigger: recheck if skill frontmatter or package requirements change
  - Trust rationale: portable skill directory baseline, not a package-manager spec

# Source Material Store

- Path: None - web fetch summaries and local record/source observations are small
  enough to cite directly here.
- Captured sources: None.
- Key excerpts / index: N/A.
- Redaction / licensing / sensitivity: No sensitive values captured.
- Retention / tracking: N/A.

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| One plugin manifest declares two Loom plugins | Claude, Codex, Cursor, Gemini docs | Would be the cleanest repo-level shape if supported | No supported harness doc showed `plugin.json` or `gemini-extension.json` declaring multiple plugins/extensions | Reject as an assumed design |
| One plugin exposes two skill roots | Claude/Cursor skill path arrays; OpenCode can register multiple paths programmatically | Simple for full install and may avoid duplication | Does not let users install core alone as a separate plugin when the harness treats the manifest as one plugin | Useful only for full/meta package, not the split boundary |
| Marketplace/catalog lists two plugin roots | Claude, Codex, Cursor marketplace/catalog docs | Supports one repository catalog with `loom-core` and `loom-playbooks` entries | Each plugin root must be self-contained after install/cache; subdirectory/package layout must avoid `../` dependencies | Best fit for Claude/Codex/Cursor, subject to runtime validation |
| Separate npm/OpenCode packages | OpenCode plugin array docs and current `open-loom.mjs` implementation pattern | Users can install core only or both via `plugin` array; package can register exact skill roots and using-Loom references | Requires package/version migration from current `open-loom`; source docs do not describe static skill registration, so local code/runtime evidence remains important | Best fit for OpenCode |
| Separate Gemini extensions | Gemini extension docs | Users can install multiple extensions and core can provide extension context | Docs do not show multi-extension marketplace/catalog from one repo or Git subdirectory install; one `gemini-extension.json` appears to define one extension | Feasible but least clean from one repo; needs dedicated validation/design |
| Generic skills-directory roots | Agent Skills spec plus harness skill roots | Works with core-only by exposing only core skills; full install can expose both roots where harness supports multiple roots | Agent Skills spec does not define package-level multi-root install; each harness decides discovery and precedence | Feasible as a fallback/developer model, not enough for native plugin UX |

# Evidence Synthesis

## Initial Core / Workflow Boundary

Core candidate after scoping:

- `using-loom`
- `loom-workspace`
- `loom-records`
- `loom-ralph`, because compiling Loom graph artifacts into bounded packets for
  fresh-context execution is part of Loom's transaction kernel rather than an
  optional workflow add-on
- `loom-memory`, as support recall bundled with the core operating surface
- canonical owner-layer skills: `loom-constitution`, `loom-initiatives`,
  `loom-research`, `loom-specs`, `loom-plans`, `loom-tickets`, `loom-evidence`,
  `loom-critique`, `loom-wiki`

Playbook candidate:

- `loom-drive`
- `loom-git`
- `loom-debugging`
- `loom-spike`
- `loom-codemap`
- `loom-ship`
- `loom-skill-authoring`

Ambiguous support candidate:

- None after current scoping. `loom-retrospective` belongs in core because
  promotion and closure discipline are part of Loom's compounding mechanism.

## Cross-Skill Coupling Risk

The split is feasible at the harness level, but not just by moving directories.
Current core-candidate files name workflow skills and workflow concepts:

- `skills/using-loom/references/04-ralph-inner-loop.md` makes Ralph part of the
  mandatory ordered doctrine; this supports keeping Ralph in core.
- `skills/using-loom/references/05-critique-and-wiki.md` covers critique/wiki
  routes and packetized sibling workflows; critique/wiki are core owner layers,
  but workflow packetization wording may need separating.
- `skills/using-loom/references/02-truth-and-authority.md` names workflow skills
  such as `loom-drive` and support coordinator `loom-memory` in routing prose.
- `skills/loom-workspace/references/routing.md` and
  `skills/loom-workspace/references/task-routing-catalog.md` route common user
  verbs directly to optional workflow skills.
- `skills/loom-records/references/route-vocabulary.md`,
  `skills/loom-records/references/retrospective.md`, and
  `skills/loom-records/references/naming-and-ids.md` mention optional workflow
  skills, packets, and Ralph-specific packet IDs; packet/Ralph grammar should stay
  core while optional playbook routing is decoupled.
- `skills/loom-plans/references/plan-shape.md`,
  `skills/loom-tickets/references/local-execution.md`, and
  `skills/loom-research/references/research-shape.md` point at optional workflow
  skills for packetized implementation, debugging, spike/sketch, or Git-backed
  work.

That means a core-only plugin would need wording that keeps canonical owner
records usable without assuming the workflow pack is installed. Optional workflow
names can remain as examples only if the text explicitly says they require the
workflow plugin or a project-provided equivalent.

## Harness Feasibility Matrix

| Harness | Split support assessment | How it would look | Key risk |
| --- | --- | --- | --- |
| Claude Code | Feasible. `plugin.json` appears single-plugin, but `.claude-plugin/marketplace.json` supports multiple plugin entries with relative sources. Plugin manifests can declare `skills` as a string or array. | A marketplace exposes `loom-core` and `loom-playbooks` plugin roots, each with its own `.claude-plugin/plugin.json` and self-contained skill root. Core plugin owns optional using-Loom `SessionStart` preload. | Plugin roots installed into cache cannot rely on paths outside themselves, so repo layout or release packaging must make each root self-contained. |
| Codex | Feasible in manifest/catalog shape, and current hooks docs address the prior hook-surface gap. `plugin.json` appears single-plugin; `.agents/plugins/marketplace.json` can list multiple plugin entries. | Codex marketplace lists `loom-core` and `loom-playbooks`, each with `.codex-plugin/plugin.json` and `skills`. Core includes `using-loom` and can bundle optional `SessionStart` hook preload through the documented plugin hook surfaces if runtime validation confirms installed-plugin behavior. | Installed Git-backed plugin skill discovery and installed-plugin hook behavior for `using-loom` still need runtime validation before broad release claims. |
| OpenCode | Feasible and probably straightforward. Config `plugin` is an array and current `open-loom.mjs` proves a plugin can register instructions and skill paths through config mutation. | Publish `open-loom-core` and `open-loom-playbooks` npm packages, or equivalent local file/path plugins. Core plugin registers ordered using-Loom references and core skills. Playbooks plugin registers playbook skills only. | Migration/deprecation of current `open-loom` full package needs its own follow-up; the split target is two packages only. |
| Gemini CLI | Feasible as two extensions, but not yet clean as one Git-backed marketplace-like repo. Docs show one `gemini-extension.json` per extension root and do not show a multi-extension repository manifest or Git subdirectory install. | Core extension contains `gemini-extension.json`, `skills/`, and `contextFileName` for optional using-Loom preload. Playbooks extension contains playbook skills. Users install both when they want full Loom. | Need validation or a packaging decision for Git distribution of two extension roots from one source repository. |
| Cursor | Feasible. Cursor docs explicitly support multi-plugin repositories via `.cursor-plugin/marketplace.json`; `plugin.json` appears single-plugin; `skills` can be a string or array. | Cursor marketplace lists `loom-core` and `loom-playbooks` plugin roots. Core may include generated `rules/*.mdc` for optional using-Loom preload plus core skills; playbooks plugin includes playbook skills. | Need runtime validation for plugin rule ordering/applicability and install/reload behavior. |
| Generic skills-directory install | Feasible. A user can expose only the core skill root or expose both roots. | Expose `loom-core/skills` only, or expose both `loom-core/skills` and `loom-playbooks/skills`. | Agent Skills itself defines skill directories, not package catalogs or multi-root precedence. Docs must be harness-specific. |

# Rejected Options

## Assume One `plugin.json` Can Declare Two Plugins

Rejected for now. Claude, Codex, Cursor, and Gemini docs all describe a single
plugin/extension manifest with one `name`. Multi-plugin repository support, where
documented, lives in marketplace/catalog files rather than `plugin.json` itself.

## Put Core And Workflow Skill Roots In One Plugin And Call That Split

Rejected as the primary split. It can make the full install convenient, but it
does not give users a core-only plugin. It is a possible compatibility/meta-plugin
shape after the real split exists.

## Let Playbooks Plugin Depend On A Parent Core Path

Rejected for native plugin packages. Claude docs explicitly note installed
plugins are copied to a cache and cannot reference files outside their directory;
Codex and Cursor similarly install/cache plugin roots. Each installable root must
be self-contained or built into a self-contained release artifact.

# Null Results

- No fetched harness docs showed a supported multi-plugin declaration inside a
  single `plugin.json` or `gemini-extension.json`.
- Gemini docs fetched here did not show a multi-extension marketplace/catalog file
  equivalent to Claude/Codex/Cursor, nor a Git-subdirectory install shape for one
  repository containing multiple extension roots.
- OpenCode docs fetched here did not document static-resource skill registration;
  current Loom support for OpenCode still rests on repository source plus runtime
  evidence for `config.skills.paths` and `config.instructions` mutation.
- Codex hooks docs address the previous hook-surface uncertainty at the
  documentation level, but this research did not run Codex to prove installed
  `loom-core` plugin hook loading from a real marketplace/cache install.

# Conclusions

1. The split is feasible across the supported harness set, but it is not the same
   shape in every harness.

2. No supported harness should be assumed to let a single plugin manifest declare
   both `loom-core` and `loom-playbooks`. The common pattern is two plugin roots
   or two packages, with a marketplace/catalog or config array exposing both.

3. Claude, Codex, and Cursor can probably use one repository-level marketplace
   or catalog that lists two self-contained plugin roots.

4. OpenCode should use two npm/file plugins because its native install surface is
   the `plugin` array plus JavaScript package/plugin modules.

5. Codex's current hooks documentation makes optional using-Loom preload plausible
   inside the core plugin, not merely as trusted project config. Runtime validation
   is still needed for installed-plugin skill discovery and hook loading.

6. Gemini CLI is the least certain. Two extensions are conceptually supported,
   but one Git-backed repo containing two installable extension roots needs more
   validation or a packaging workaround.

7. A core-only install requires content refactoring, not just packaging. The
   `using-loom`, `loom-workspace`, and `loom-records` surfaces currently teach or
   route to workflow skills as if they are always present.

8. `loom-playbooks` should require `loom-core` rather than duplicate it. Harnesses
   may not enforce plugin dependencies, so the requirement likely needs to appear
   in package docs, marketplace descriptions, and playbook skill activation text.

9. The split reopened constitutional/product-surface truth. `decision:0008` now
   authorizes `loom-core/` and `loom-playbooks/` as the product package roots and
   supersedes the prior single top-level `skills/` surface.

# Recommendations

1. Treat the next step as product architecture/spec work, not direct file moves.
   `decision:0008` now defines the new product surfaces; downstream work should
   create the contract and implementation tickets before moving files.

2. Use this membership boundary unless later planning reopens it: core =
   `using-loom`, `loom-workspace`, `loom-records`, `loom-memory`, `loom-ralph`,
   `loom-retrospective`, and all canonical owner-layer skills; playbooks =
   `loom-drive`, `loom-git`, `loom-debugging`, `loom-spike`, `loom-codemap`,
   `loom-ship`, and `loom-skill-authoring`.

3. Refactor doctrine before package manifests. Core `using-loom` should teach the
   canonical layer and Ralph transaction protocol while mentioning playbooks as
   optional compositions, not mandatory installed skills.

4. Prefer the decided source layout: top-level `loom-core/` and
   `loom-playbooks/`, each containing its own `skills/` and native harness plugin
   or extension metadata. Avoid relying on plugin roots that reference parent
   directories.

5. Keep root-level marketplace/catalog files as repo-level discovery surfaces that
   list both package roots. Do not keep root `skills/` as a full bundle.

6. Validate Gemini separately before promising a one-repo two-extension install.
   If Gemini cannot install two extension roots from one Git repository cleanly,
   use separate release packages or document two local/source installs.

7. After the architecture decision, create bounded tickets per harness for split
   manifests and validation rather than doing a single broad migration.

# Open Questions

- How should the existing published `open-loom` package be deprecated or migrated
  after `open-loom-core` and `open-loom-playbooks` exist?
- What release layout best preserves self-contained plugin roots without making
  generated adapter outputs the semantic owner of Loom?
- Can Gemini install a subdirectory extension from a Git repository, or does it
  require separate repositories/packages for core and workflow extensions?
- Does a real installed Codex plugin load bundled `hooks/hooks.json` or manifest
  hook lifecycle config from the plugin cache, and does `SessionStart` preload
  preserve source-marked using-Loom context as expected?
- How should docs express "bring your own workflows" without implying that
  workflow packs are required for core Loom operation?

# Linked Work

- Initiative: `initiative:loom-install-experience`
- Plan: `plan:install-experience-harness-adapters`
- Research: `research:loom-install-distribution-methods`
- Research: `research:codex-plugin-distribution-surfaces`
- Decision: `decision:0004`
- Decision: `decision:0005`
- Decision: `decision:0006`
- Decision: `decision:0008`
