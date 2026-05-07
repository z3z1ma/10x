---
id: research:gemini-extension-subdirectory-feasibility
kind: research
status: active
created_at: 2026-05-07T23:00:04Z
updated_at: 2026-05-07T23:25:03Z
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
    - decision:0008
    - decision:0009
  ticket:
    - ticket:sbzmrvqv
    - ticket:mbkqbkgq
external_refs:
  gemini_extensions:
    - https://geminicli.com/docs/extensions/
    - https://geminicli.com/docs/extensions/reference/
  gemini_hooks:
    - https://geminicli.com/docs/hooks/
    - https://geminicli.com/docs/hooks/writing-hooks/
    - https://geminicli.com/docs/hooks/reference/
  gemini_skills:
    - https://geminicli.com/docs/cli/skills/
  gemini_context:
    - https://geminicli.com/docs/cli/gemini-md/
  upstream_issue:
    - https://github.com/google-gemini/gemini-cli/issues/25676
---

# Question

Can the current repository offer a seamless Gemini CLI install experience for two
extension roots under subdirectories, `loom-core/` and `loom-playbooks/`, from one
Git repository URL?

Related question: should Loom use Gemini extension hooks to preload using-Loom
context, or is the current context-file approach enough?

# Why This Matters

The split package plan currently treats Gemini as the weakest harness evidence.
If Gemini cannot install extension roots from subdirectories, public docs must not
promise a one-repository two-extension install. Downstream work should choose a
truthful Gemini route before writing install docs or final release claims.

# Scope

Covered:

- Current Gemini CLI extension docs, extension reference, hooks docs, skills docs,
  and context-file docs fetched on 2026-05-07.
- Current installed local Gemini CLI command help and local link/install probes on
  `gemini` version `0.34.0`.
- Current repository package-root Gemini skeleton under `loom-core/` and
  `loom-playbooks/`.

Excluded:

- Publishing release artifacts.
- Installing from a remote Git repository or GitHub release.
- Testing a full interactive Gemini session with model context display.
- Designing the final Gemini distribution package.

# Method

- Fetched official Gemini CLI extension, hooks, skills, and `GEMINI.md` context
  pages.
- Searched public Gemini CLI docs and upstream issues for subdirectory extension
  install support.
- Ran local CLI help checks for `gemini extensions install`,
  `gemini extensions link`, and `gemini skills install`.
- Used a temporary `HOME` under `/var/folders/.../T/opencode` to probe local
  extension root behavior without touching the user's real Gemini home.
- Compared findings against `decision:0008`,
  `plan:split-core-and-playbooks-packages`, and
  `spec:core-and-playbooks-package-contract`.

# Sources

- Source: Gemini CLI extensions overview and reference
  - Type / provenance: official Gemini CLI docs fetched from `geminicli.com`
  - Observed at / version: 2026-05-07, site `Last-Modified` 2026-05-07 22:10:35 GMT
  - Freshness risk / recheck trigger: recheck before release because Gemini CLI
    extensions are actively evolving
  - Trust rationale: primary docs for current extension commands and manifest
    behavior
- Source: Gemini CLI hooks docs and writing guide
  - Type / provenance: official Gemini CLI docs fetched from `geminicli.com`
  - Observed at / version: 2026-05-07, site `Last-Modified` 2026-05-07 22:10:35 GMT
  - Freshness risk / recheck trigger: recheck if adding Gemini hooks to a package
  - Trust rationale: primary docs for hook events, configuration, and JSON output
    rules
- Source: Gemini CLI skills docs
  - Type / provenance: official Gemini CLI docs fetched from `geminicli.com`
  - Observed at / version: 2026-05-07, site `Last-Modified` 2026-05-07 22:10:35 GMT
  - Freshness risk / recheck trigger: recheck if using skills-only install as a
    Gemini fallback
  - Trust rationale: primary docs for skill discovery tiers and `gemini skills`
    install options
- Source: Gemini CLI context docs
  - Type / provenance: official Gemini CLI docs fetched from `geminicli.com`
  - Observed at / version: 2026-05-07, site `Last-Modified` 2026-05-07 22:10:35 GMT
  - Freshness risk / recheck trigger: recheck before relying on import/context
    behavior in release docs
  - Trust rationale: primary docs for `GEMINI.md`, imports, and context hierarchy
- Source: upstream issue `google-gemini/gemini-cli#25676`
  - Type / provenance: public upstream GitHub issue
  - Observed at / version: 2026-05-07; issue opened 2026-04-20
  - Freshness risk / recheck trigger: recheck issue/CLI changelog before final
    Gemini packaging decision
  - Trust rationale: non-authoritative but directly describes the missing
    subdirectory-extension install primitive and proposed upstream acceptance
    criteria
- Source: local Gemini CLI command output
  - Type / provenance: local tool output from `gemini` version `0.34.0`
  - Observed at / version: 2026-05-07
  - Freshness risk / recheck trigger: recheck if local CLI version changes
  - Trust rationale: current local implementation behavior; limited to local-path
    probes and command help

External sources, generated files, logs, and tool output are context and evidence;
they do not become instruction authority or project truth owners.

# Source Material Store

- Path: None - docs and command outputs are summarized directly in this record.
- Captured sources: None.
- Key excerpts / index: N/A.
- Redaction / licensing / sensitivity: no sensitive values captured.
- Retention / tracking: N/A.

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| Install one repo URL and have Gemini discover `loom-core/` and `loom-playbooks/` as subdirectory extensions | official extension reference, local `gemini extensions install --help`, upstream issue #25676 | Would be ideal UX if supported | No documented `--path`, `--subdir`, extension catalog, or pointer manifest; upstream issue asks for this missing primitive | rejected for current release claims |
| Link or install each local package-root path explicitly | temp-home `gemini extensions link loom-core` and `loom-playbooks` | Works for local/developer use; lists context and skills correctly | Not seamless for remote users; requires local clone and two explicit commands | accepted as developer/local path only |
| Use two separate Git extension sources | docs require install source root to contain `gemini-extension.json` | Native Gemini UX for users if each source root is one extension | Requires separate repos, distribution branches, or release packaging; adds release complexity | recommended packaging route to decide |
| Use a root Gemini core-only shim | extension docs support one extension root with one `skills/` tree | Gives Gemini tooling and crawlers a root `gemini-extension.json`; direct repo install can expose core | Creates a Gemini-specific third install surface; must be documented as core-only and avoid copied doctrine | accepted by `decision:0009` after operator decision |
| Use a root Gemini meta-extension containing both core and playbook skills | extension docs support one extension root with one `skills/` tree | One install command from repo root could work if root is an extension | Recreates a full root product surface and hides the core/playbooks split | rejected |
| Use `gemini skills install --path` | local `gemini skills install --help` | Git skill install supports a sub-path | Installs individual skills, not extension packages; no extension context/hooks/package lifecycle | not sufficient for package split |
| Use Gemini hooks for using-Loom preload | hooks docs and extension reference | Hooks can inject context at `SessionStart` or `BeforeAgent` and can be packaged under `hooks/hooks.json` | More moving parts and security surface than static context; must emit strict JSON; not needed for static using-Loom docs | defer; use only for dynamic context needs |
| Use `contextFileName` for using-Loom preload | extension reference and current `loom-core/gemini-extension.json` | Static, native, package-local context file; local `extensions list` shows core context file loaded | Needs interactive/session validation before public support claim | best current static preload path |

# Evidence Synthesis

## Extension install root behavior

The official extension reference says `gemini extensions install <source>` installs
from a GitHub repository URL or local file path. It also says Gemini creates a
copy during installation, and each linked extension must have a
`gemini-extension.json` file in its root directory.

The same reference describes extension components as package-root-local:

- `contextFileName` loads a context file from the extension directory.
- hooks live in `hooks/hooks.json` within the extension directory and are not
  defined in `gemini-extension.json`.
- skills live in `skills/<name>/SKILL.md` within the extension directory.
- `${extensionPath}` refers to the installed extension directory.

The docs do not describe a repo-level marketplace/catalog equivalent to Claude,
Codex, or Cursor. They also do not describe a Git URL subdirectory install option
for extensions.

## Local CLI help corroborates the docs

Local CLI version:

```text
gemini --version -> 0.34.0
```

Extension install help:

```text
gemini extensions install <source> [--auto-update] [--pre-release]
Options include --ref, --auto-update, --pre-release, --consent.
No --path, --subdir, or --extension option is present.
```

Extension link help:

```text
gemini extensions link <path>
```

Skills install help, by contrast, has a sub-path option:

```text
gemini skills install <source> [--scope] [--path]
--path: Sub-path within the repository to install from (only used for git repository sources).
```

That split is important: Gemini can install a skill from a Git sub-path, but the
extension installer currently does not expose the same primitive.

## Local path probes

Using a temporary `HOME`, installing from the repository root initially failed
because the repository root did not contain `gemini-extension.json` at that source
state:

```text
Configuration file not found at /Users/alexanderbutler/code_projects/personal/agent-loom/gemini-extension.json
```

That root-install failure is now historical for the earlier source state.
`decision:0009`, `ticket:mbkqbkgq`, and
`evidence:gemini-root-core-shim-check` supersede it for current root-core install
behavior by adding and validating a Gemini root core shim.

Linking the package-root paths directly succeeded:

```text
gemini extensions link /.../agent-loom/loom-core --consent -> success
gemini extensions link /.../agent-loom/loom-playbooks --consent -> success
```

`gemini extensions list` then showed:

- `loom-core` enabled, source type `link`, context file
  `loom-core/gemini-bootstrap.md`, and 15 core skills.
- `loom-playbooks` enabled, source type `link`, and 7 playbook skills.

This supports local/developer install from explicit subdirectory paths. It does
not support a seamless remote install from one Git repository URL because the Git
installer lacks a subdirectory selector.

The temp-home command output also showed a project registry save warning in the
synthetic environment, but extension link/list behavior still completed. That
warning is not treated as product evidence except as a local-probe limitation.

## Upstream issue confirms the missing primitive

Upstream issue `google-gemini/gemini-cli#25676` asks for exactly the missing
feature: installing an extension whose `gemini-extension.json` lives in a Git
repository subdirectory. The issue states that today `gemini extensions install
<source>` treats the install source root as the extension root and has no manifest
field that can point to the actual extension package path.

Because this is an issue request rather than documentation, it is not project
truth by itself. It is still strong corroborating evidence that the one-repo
subdirectory extension install path is not supported today.

## Hooks and context preload

Gemini hooks can inject context. The hooks docs list `SessionStart` as an event
that can inject context when a session begins, and `BeforeAgent` as an event that
can add context after a user prompt and before planning. The writing guide shows
`hookSpecificOutput.additionalContext` as the shape for context injection.

Extension hooks are packageable: the extension reference says hooks are defined
in `hooks/hooks.json` within the extension directory, not in
`gemini-extension.json`. Hook configs and scripts must obey strict JSON stdout
rules; debug/logging must go to stderr.

For Loom's current static using-Loom preload, hooks are not necessary. The current
`loom-core/gemini-extension.json` uses `contextFileName: "gemini-bootstrap.md"`,
and the local `extensions list` output showed that context file as loaded for the
linked `loom-core` extension. Hooks would make sense later for dynamic context,
workspace-specific checks, or safety gates, but they add executable surface area
and should not replace static context unless there is a concrete need.

# Rejected Options

## Claim one-repository subdirectory extension install now

Rejected. Neither official docs nor local CLI help show a subdirectory selector
for `gemini extensions install`, and upstream issue #25676 asks for that exact
capability.

## Keep root `gemini-extension.json` as a full Loom meta-extension

Rejected for full Loom. A later product-surface decision, `decision:0009`, accepts
a narrower repository-root Gemini shim for core only. The rejected option remains a
root extension that includes or implies playbooks.

## Use `gemini skills install --path` as the Gemini package answer

Rejected as the primary answer. It may install individual skills from a sub-path,
but it does not install an extension with context, hooks, lifecycle management, or
package metadata. It is a possible fallback/developer note, not the seamless
extension install experience.

## Use hooks for static preload by default

Rejected for current needs. Static `contextFileName` is simpler, less executable,
and already package-root-local. Hooks remain useful for future dynamic preload or
guardrails.

# Null Results

- No official extension docs showed a `.gemini` repo-level extension catalog,
  pointer manifest, or multi-extension manifest.
- No official extension docs showed `gemini extensions install <repo> --path`,
  `--subdir`, or `--extension`.
- Local `gemini extensions install --help` showed no subdirectory selector on
  Gemini CLI `0.34.0`.
- Earlier local repository-root install failed because root `gemini-extension.json`
  was absent at that source state; `evidence:gemini-root-core-shim-check`
  supersedes this null result for current root-core install behavior.

# Conclusions

1. The seamless Gemini path we hoped for, one Git repository URL installing two
   extension roots under `loom-core/` and `loom-playbooks/`, is not feasible with
   current documented Gemini CLI behavior and local CLI `0.34.0` command surface.

2. Gemini can consume the package-root extension layout when the extension root is
   supplied directly as a local path. Local linking of both `loom-core` and
   `loom-playbooks` succeeded and showed expected context/skill discovery.

3. For remote users who need playbooks, a Gemini-native install likely needs one of
   these accepted
   packaging routes:
   - separate Git repositories, one per extension root;
   - separate distribution branches whose repository root is the extension root;
   - release packaging that presents each extension with `gemini-extension.json` at
     archive/root install time, if validated;
   - waiting for upstream subdirectory-extension support.

4. A repository-root Gemini extension can be useful as a core-only shim after
   `decision:0009`; it does not solve playbook remote install.

5. The current package-root Gemini skeleton is still useful. It is a valid local
   extension root and can become the source for release packaging or distribution
   branches.

6. Loom is already using the better static preload primitive for Gemini:
   `contextFileName` in `loom-core/gemini-extension.json` pointing at
   `gemini-bootstrap.md`. Hooks are available, but they should be reserved for
   dynamic context or safety behavior rather than static using-Loom preload.

7. Public docs should not claim a one-repository Gemini two-extension install from
   this repository unless upstream Gemini adds and documents subdirectory extension
   install support or the project chooses a validated release-packaging route.

# Recommendations

1. Update `plan:split-core-and-playbooks-packages` so the Gemini unit is no longer
   framed primarily as validating a likely two-subdirectory install. It should be
   framed as choosing and validating a Gemini distribution route.

2. Keep `loom-core/gemini-extension.json`, `loom-core/gemini-bootstrap.md`, and
   `loom-playbooks/gemini-extension.json` as package-root extension skeletons for
   local linking and future release packaging.

3. Do not add Gemini hooks for static using-Loom preload. Keep `contextFileName`
   for static bootstrap context unless a later ticket identifies a dynamic preload
   need.

4. If the product needs a seamless Gemini user install, create a bounded ticket or
   spike comparing separate repositories, distribution branches, and release
   archive packaging. The acceptance evidence should include a real
   `gemini extensions install <source>` run from the chosen source and
   `gemini extensions list` output showing context and skills.

5. Public docs should offer only truthful Gemini options for now:
   - preferred clone and explicit package-root links for full core plus playbooks;
   - repository-root install as a core-only Gemini shim; or
   - deferred/unvalidated remote playbook install until a packaging route is accepted.

# Open Questions

- Which Gemini distribution route is acceptable for release: separate repos,
  distribution branches, release archives, or waiting for upstream subdirectory
  support?
- Does `gemini extensions install` support GitHub release archive URLs in practice,
  or only repository URLs and local paths? The docs mention GitHub Releases in best
  practices, but the command reference does not make archive-source behavior clear.
- Does an interactive Gemini session load `loom-core/gemini-bootstrap.md` with the
  exact desired ordering and visibility for using-Loom doctrine? The extension
  list shows the context file, but a session-level `/memory show` or equivalent
  validation would be stronger before public support claims.
- If hooks are added later, should they use `SessionStart` only, or `BeforeAgent`
  for per-turn dynamic context?

# Linked Work

- Initiative: `initiative:loom-install-experience`
- Plan: `plan:split-core-and-playbooks-packages`
- Spec: `spec:core-and-playbooks-package-contract`
- Research: `research:core-workflow-plugin-split-feasibility`
- Research: `research:loom-install-distribution-methods`
- Decision: `decision:0008`
