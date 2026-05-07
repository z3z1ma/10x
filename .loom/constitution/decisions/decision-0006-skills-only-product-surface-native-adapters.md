---
id: decision:0006
kind: decision
status: active
created_at: 2026-04-26T07:04:10Z
updated_at: 2026-05-07T19:25:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  decision:
    - decision:0005
  initiative:
    - initiative:loom-install-experience
  ticket:
    - ticket:jt2vy25y
---

# Decision

Loom's distributable product surface is `skills/`.

The repository will not ship a Makefile installer, cross-harness shell installer,
or top-level command-wrapper package as the product. Harness integrations should
use each harness's native plugin, extension, or skill-package system to expose the
same canonical `skills/` directory.

Native adapters may preload `skills/using-loom/references/` when the harness
supports that cleanly. Preload is a bonus over the skill package, not a fallback
install path and not a second source of doctrine.

# Why This Decision Exists

`decision:0005` made Loom's mandatory doctrine part of the skill package through
`using-loom`. That removes the need for a separate installer whose job is to
copy rules into harness-specific instruction locations.

Every target coding harness has or is expected to have a first-class way to
distribute skills or plugin-packaged skills. Leaning into that common surface keeps
Loom simple, portable, and inspectable.

# Alternatives Considered

- Keep `Makefile` and `scripts/install-loom.sh` as fallback installers. Rejected
  because they encode harness behavior in a cross-harness shell script and create
  a shadow product surface.
- Keep top-level command wrappers as a default install surface. Rejected because
  every Loom workflow should be reachable through skills and owner records; a
  command layer should not be necessary for Loom to make sense.
- Keep per-harness generated instruction files as normal distribution output.
  Rejected because generated files can drift from `skills/` and confuse source of
  truth boundaries.

# Consequences

- `Makefile` and `scripts/install-loom.sh` are removed.
- Top-level `commands/` is removed from the product surface.
- Native manifests and plugins should expose `skills/`; OpenCode and Claude may
  additionally preload `using-loom` references.
- Public install docs should teach native harness installs only.
- Adapter examples should describe native plugin/skill-package behavior, not
  fallback copy installers.
- Legacy user-local installs created by the removed shell script are not migrated
  by this repository. They are local state and should be cleaned up manually if a
  user still has them.

# Revisit Conditions

Revisit if a target harness removes first-class skill/plugin distribution, or if
empirical use shows that a skill-only product surface cannot make `using-loom`
discoverable enough for safe operation.

# Supersession

This supersedes any recommendation to keep `Makefile`, `scripts/install-loom.sh`,
or generated command-wrapper installs as supported Loom distribution paths. It
does not supersede `decision:0005`; it sharpens that decision by making `skills/`
the only product surface.
