---
id: decision:0005
kind: decision
status: active
created_at: 2026-04-26T06:35:59Z
updated_at: 2026-04-26T06:35:59Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  ticket:
    - ticket:jt2vy25y
---

# Decision

Loom's mandatory operating doctrine is now packaged as the `loom-bootstrap` skill.

The ordered doctrine references live under
`skills/loom-bootstrap/references/01-*.md` through
`skills/loom-bootstrap/references/07-*.md`. Harness adapters may still preload
those references as always-on context, but the canonical distribution model is a
skills package with one mandatory bootstrap skill rather than a separate top-level
`rules/` corpus.

# Why This Decision Exists

Remote plugin ecosystems make skills the common package unit. Codex in particular
can expose installed plugin skills, but current source does not show installed
plugins owning always-on instructions or hooks. Keeping Loom's mandatory doctrine
outside the skill package therefore makes remote plugin install look incomplete
even when the harness can install skills correctly.

Packaging the doctrine as a bootstrap skill lets Loom remain Markdown-native and
harness-agnostic while giving every plugin ecosystem one simple entry point:
install the Loom skills, then use `loom-bootstrap` first unless the same doctrine
was already preloaded by an adapter.

# Alternatives Considered

- Keep top-level `rules/` as the canonical always-on corpus. Rejected because it
  makes plugin-first distribution depend on harness-specific extra context wiring
  even when the harness already supports skills well.
- Treat skills as optional expertise and keep bootstrap instructions only in
  `AGENTS.md`-style files. Rejected because it would create many harness-specific
  copies and weaken the self-contained skill package.
- Rely only on skill descriptions without ordered references. Rejected because the
  bootstrap doctrine is too important and too detailed to compress into one
  description.
- Require a hidden installer or runtime to inject the doctrine. Rejected because it
  violates Loom's Markdown-first, no-hidden-runtime policy.

# Consequences

- `skills/loom-bootstrap/SKILL.md` is the mandatory first skill when Loom doctrine
  is not already in the current context.
- The seven former rule files move into `skills/loom-bootstrap/references/` and
  remain ordered by filename.
- Adapter docs and hook configs should reference the bootstrap skill references,
  not top-level `rules/` paths.
- Always-on adapter preload remains valuable but becomes an optimization, not the
  only way Loom can be complete.
- Harness instructions should point agents at `loom-bootstrap` first; they should
  not define independent Loom doctrine.

# Revisit Conditions

Revisit this decision if a major target harness stops exposing skills before work,
if skill descriptions become unavailable in installed plugin UIs, or if empirical
use shows that agents routinely ignore mandatory bootstrap skills without an
always-on adapter layer.

# Supersession

This narrows `decision:0004` by making one explicitly broad bootstrap skill
acceptable as the package entry point. It supersedes the constitutional assumption
that top-level `rules/` files are the canonical always-on doctrine surface while
preserving the requirement that Loom doctrine be loaded before work.
