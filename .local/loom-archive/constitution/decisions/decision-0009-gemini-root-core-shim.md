---
id: decision:0009
kind: decision
status: active
created_at: 2026-05-07T23:20:14Z
updated_at: 2026-05-07T23:20:14Z
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
    - research:gemini-extension-subdirectory-feasibility
  decision:
    - decision:0008
  ticket:
    - ticket:mbkqbkgq
---

# Decision

Loom will keep a Gemini-specific root extension shim so Gemini tooling and
crawlers that expect `gemini-extension.json` at a repository root can discover and
install Loom core.

The root Gemini extension is a core-only compatibility surface. It may expose
`loom-core` skills through a root `skills` shim and may preload using-Loom context
from the core package. It must not present `loom-playbooks` as installed, must not
duplicate playbook skills, and must not imply that Gemini can discover package
roots from repository subdirectories.

The preferred Gemini install path remains cloning the repository and linking the
explicit package roots:

```text
gemini extensions link ./loom-core
gemini extensions link ./loom-playbooks
```

Remote root install from this repository is allowed to be documented only as a
core-only shortcut:

```text
gemini extensions install https://github.com/z3z1ma/agent-loom
```

# Why This Decision Exists

Gemini CLI currently installs an extension from the source root containing
`gemini-extension.json`; it does not provide a documented extension subdirectory
selector comparable to `gemini skills install --path`.

That means the clean `loom-core/` and `loom-playbooks/` package roots are the
right source layout, but a repository-root `gemini-extension.json` is valuable for
Gemini-native discovery, tooling, and crawlers. The operator explicitly accepts a
Gemini-specific third install surface as long as documentation is clear and the
root extension installs only core.

# Alternatives Considered

- Keep no root Gemini extension. Rejected because it leaves Gemini root-indexing
  tools and direct repository install without a useful core entry point.
- Make the root Gemini extension a full Loom bundle including playbooks. Rejected
  because it would recreate the full root product surface and hide the core versus
  playbooks split.
- Duplicate core skills into root `skills/`. Rejected because duplicate core
  doctrine creates drift risk; any root skill exposure should point at `loom-core`
  rather than become a second source copy.
- Wait for upstream Gemini subdirectory extension support. Rejected as the only
  route because it blocks a useful core-only install that Gemini can support now.
- Use hooks for static preload. Rejected because `contextFileName` remains the
  simpler static preload mechanism.

# Consequences

- `decision:0008` is narrowed for Gemini only: top-level `loom-core/` and
  `loom-playbooks/` remain the intended package roots, but root Gemini files may
  exist as a core-only compatibility shim.
- Documentation must prefer clone-and-link for full Gemini installs and state that
  repository-root `gemini extensions install` installs core only.
- Root `skills/`, if present for Gemini, is not a full compatibility bundle and is
  not the source of product truth; it is a transport shim to expose core skills to
  Gemini's root-extension discovery model.
- Gemini playbooks still require explicit package-root linking or a future
  validated distribution route.
- Stale-reference scans must distinguish the Gemini core shim from old claims that
  root `skills/` is the general product surface.

# Revisit Conditions

Revisit this decision if:

- Gemini adds documented extension subdirectory install support.
- Root Gemini install cannot reliably expose core skills and context from
  `loom-core` without copying core.
- The root shim causes repeated operator confusion despite install documentation.
- A future release distribution route gives Gemini a cleaner core/playbooks remote
  install without a root compatibility shim.

# Supersession

This narrows `decision:0008` only for Gemini. It does not reopen the rejected full
root `skills/` compatibility bundle, and it does not authorize a root OpenCode,
Claude, Codex, Cursor, or generic Loom package surface.
