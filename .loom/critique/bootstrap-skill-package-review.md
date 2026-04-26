---
id: critique:bootstrap-skill-package-review
kind: critique
status: final
created_at: 2026-04-26T07:04:10Z
updated_at: 2026-04-26T07:23:57Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:jt2vy25y
links:
  ticket:
    - ticket:jt2vy25y
  decision:
    - decision:0005
    - decision:0006
  evidence:
    - evidence:bootstrap-skill-package-validation
external_refs: {}
---

# Summary

Reviewed the high-risk protocol-authority change that moves Loom's mandatory
doctrine into `skills/loom-bootstrap/references/` and makes `skills/` the native
product surface.

# Review Target

`ticket:jt2vy25y`, `decision:0005`, `decision:0006`, and the uncommitted product
diff spanning bootstrap references, native adapter manifests, docs, examples,
OpenCode plugin code, Claude/Codex hook fixtures, and removed fallback surfaces.

# Verdict

pass

The bootstrap skill direction is sound. The first review pass correctly found
that fallback installers and command wrappers contradicted the skills-only model.
Follow-up edits removed those product surfaces and updated native adapter docs.
Later blocker checks found stale active research and spec records; those were
reconciled or superseded.

# Findings

## FIND-001: Legacy fallback installer surface contradicted skills-only packaging

Severity: high
Confidence: high
Disposition: resolved

Observation:

The first review pass found `Makefile`, `scripts/install-loom.sh`, and generated
fallback installer docs still present after the bootstrap skill move.

Why it matters:

Keeping a cross-harness shell installer would make the script a shadow product
surface and weaken the claim that `skills/` is the product.

Follow-up:

Resolved by deleting `Makefile` and `scripts/install-loom.sh`, removing fallback
installer sections from docs, and recording `decision:0006`.

Challenges:

- ticket:jt2vy25y

## FIND-002: Command-wrapper packaging contradicted skills-only product surface

Severity: high
Confidence: high
Disposition: resolved

Observation:

Top-level `commands/`, Claude manifest command exposure, and OpenCode command
registration remained after the product surface was narrowed to skills.

Why it matters:

If command wrappers ship as product surface, future operators may treat command
prompts as Loom behavior owners instead of using the owning skills and records.

Follow-up:

Resolved by deleting top-level `commands/`, removing `commands/` from package and
Claude plugin manifests, removing `config.command` registration from `open-loom`,
and deleting stale command-adapter examples.

Challenges:

- ticket:jt2vy25y

## FIND-003: Codex remote plugin discovery remains unvalidated

Severity: medium
Confidence: high
Disposition: open

Observation:

Codex docs now correctly say the plugin path still needs installed skill-discovery
validation for `loom-bootstrap`.

Why it matters:

The skills-only model depends on the installed Codex plugin exposing
`loom-bootstrap` reliably. The repository has validated hook preload and manifest
shape, not installed remote plugin skill invocation.

Follow-up:

Keep `ticket:lx9nnztk` active until installed Git-backed plugin skill discovery is
validated or a clear limitation is recorded.

Challenges:

- ticket:lx9nnztk

## FIND-004: Legacy local installs are not automatically migrated

Severity: low
Confidence: high
Disposition: accepted_risk

Observation:

Removing the shell installer means old user-local generated files from prior
`make install` runs are not automatically removed.

Why it matters:

Existing local users may have stale generated instruction blocks or copied rule
files until they clean them up manually.

Follow-up:

Accepted as local-state risk. `INSTALL.md` now states that older generated installs
are legacy local state and should be cleaned up manually if still present.

Challenges:

- ticket:jt2vy25y

## FIND-005: Active historical install research still recommended fallback install

Severity: high
Confidence: high
Disposition: resolved

Observation:

`research:harness-install-surfaces` remained active and still recommended a
Makefile/direct-copy installer path.

Follow-up:

Resolved by marking the research `superseded`, adding a `decision:0006`
supersession note, and replacing recommendations with native skills-package
guidance.

Challenges:

- ticket:jt2vy25y

## FIND-006: Active Codex command research still recommended generated wrappers

Severity: high
Confidence: high
Disposition: resolved

Observation:

`research:codex-command-skill-installation` remained active and still recommended
generated `loom-command-*` adapter skills from top-level command wrappers.

Follow-up:

Resolved by marking the research `superseded`, adding a `decision:0006`
supersession note, and replacing recommendations with a warning not to generate
command adapter skills as product surface.

Challenges:

- ticket:jt2vy25y

## FIND-007: OpenCode spec still required removed rules and commands surfaces

Severity: high
Confidence: high
Disposition: resolved

Observation:

`spec:opencode-plugin-install-contract` still required top-level `rules/`,
command wrappers, and `config.command` registration.

Follow-up:

Resolved by updating the spec to require `skills/loom-bootstrap/references/` via
`config.instructions`, `skills/` via `config.skills.paths`, no command-wrapper
registration, and package contents that exclude removed product surfaces.

Challenges:

- ticket:jt2vy25y

# Evidence Reviewed

- `skills/loom-bootstrap/SKILL.md`
- `skills/loom-bootstrap/references/*.md`
- `decision:0005`
- `decision:0006`
- `ticket:jt2vy25y`
- `evidence:bootstrap-skill-package-validation`
- `research:harness-install-surfaces`
- `research:codex-command-skill-installation`
- `spec:opencode-plugin-install-contract`
- `open-loom.mjs`
- `hooks/hooks.json`
- `.codex/hooks.json`
- `.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`
- `.agents/plugins/marketplace.json`
- `README.md`, `INSTALL.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `AGENTS.md`
- adapter fixtures under `examples/adapters/`

# Residual Risks

- Codex installed plugin skill discovery for `loom-bootstrap` remains unvalidated.
- Claude runtime hook behavior has not been re-probed after the path move, though
  structural plugin validation passes and the hook paths are explicit.
- Legacy user-local files from removed installers may remain on machines that used
  older install targets.

# Required Follow-up

- Validate Codex installed plugin skill discovery in `ticket:lx9nnztk`.
- Re-probe Claude runtime hook preload before broad Claude marketplace release.
- Keep legacy installer cleanup out of the supported product surface unless a
  separate, explicitly scoped cleanup note or migration ticket is requested.

# Acceptance Recommendation

`ticket:jt2vy25y` can close after recording accepted residual risks and
wiki/retrospective disposition. Remaining Codex and Claude release validation
belongs to linked follow-up tickets, not this product-surface ticket.
