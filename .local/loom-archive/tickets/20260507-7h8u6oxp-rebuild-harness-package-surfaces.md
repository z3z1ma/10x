---
id: ticket:7h8u6oxp
kind: ticket
status: closed
change_class: config
risk_class: high
created_at: 2026-05-07T22:20:29Z
updated_at: 2026-05-07T23:49:27Z
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
  decision:
    - decision:0008
  ticket:
    - ticket:u9vtemj3
  packet:
    - packet:ralph-ticket-7h8u6oxp-20260507T222124Z
  evidence:
    - evidence:harness-package-surface-skeleton-check
  critique:
    - critique:harness-package-surface-skeleton-review
external_refs: {}
depends_on:
  - ticket:u9vtemj3
---

# Summary

Rebuild the non-OpenCode native harness package surfaces around the new
`loom-core/` and `loom-playbooks/` roots so harness metadata and root catalogs no
longer point at the retired root `skills/` product surface.

# Context

`ticket:u9vtemj3` closed the physical skill split: `loom-core/skills` contains the
core skill corpus, `loom-playbooks/skills` contains playbook skills only, and root
`skills/` is retired.

This ticket performs the next `plan:split-core-and-playbooks-packages` unit:
`Rebuild Harness Package Surfaces`. It creates or moves Claude, Codex, Cursor, and
Gemini package metadata into the two package roots and reconciles root catalogs so
they list the two packages instead of a single repository-root plugin.

OpenCode package splitting is intentionally excluded because the plan assigns it a
separate unit with package metadata, package names, smoke checks, and legacy
`open-loom` migration concerns.

# Scope

In:

- Create package-root Claude plugin metadata under `loom-core/.claude-plugin/` and
  `loom-playbooks/.claude-plugin/`.
- Create package-root Codex plugin metadata under `loom-core/.codex-plugin/` and
  `loom-playbooks/.codex-plugin/`.
- Create package-root Cursor plugin metadata under `loom-core/.cursor-plugin/` and
  `loom-playbooks/.cursor-plugin/`.
- Create package-root Gemini extension metadata under `loom-core/` and
  `loom-playbooks/`, including core context/preload files only where the current
  root package already had them.
- Move or copy Claude hook/context files only where they are needed for the core
  package-root plugin to find `loom-core/skills/using-loom` after install/cache.
- Update root marketplace/catalog files that can list multiple package roots so
  they list `loom-core` and `loom-playbooks` with the harness-appropriate relative
  source syntax.
- Remove or neutralize obsolete repository-root single-package plugin metadata when
  leaving it would present root `skills/` as current product truth.
- Run JSON syntax checks, manifest path checks, root catalog source checks, stale
  `skills/` path checks across harness surfaces, and `git diff --check` for changed
  harness/package files.

Out:

- Creating `@z3z1ma/open-loom-core` or `@z3z1ma/open-loom-playbooks` OpenCode
  packages.
- Editing root `package.json` or `open-loom.mjs` except to leave them for the
  OpenCode ticket.
- Publishing packages or changing release versions.
- Updating README, INSTALL, ARCHITECTURE, PROTOCOL, AGENTS, or examples.
- Claiming Codex installed-plugin hook preload or Gemini one-repository
  two-extension runtime support without separate runtime evidence.
- Redesigning skill behavior or core/playbook membership.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Package-root plugin metadata may reuse the current single-package manifest shapes with split names, descriptions, and `./skills/` paths. | yes | no | accepted for structural skeleton |
| Core Claude/Gemini preload files belong in `loom-core` because `using-loom` is core; playbooks should not duplicate core preload doctrine. | yes | no | accepted |
| A harness catalog format cannot truthfully list local package roots with current evidence. | yes | yes | stop and record a gap instead of inventing a format |
| OpenCode package files are needed to make the repository coherent. | yes | yes | stop and leave for the OpenCode split ticket rather than widening scope |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-004
- spec:core-and-playbooks-package-contract#ACC-006 — only as explicit deferral / no
  runtime-preload claim for Codex and Gemini.
- spec:core-and-playbooks-package-contract#ACC-007 — scoped to harness manifests
  and root catalogs, not public docs/examples/OpenCode.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Closed. Ralph iteration 01 landed the common non-OpenCode harness package
skeleton, structural evidence is recorded, mandatory critique passed after the
Cursor root marketplace follow-up, and residual runtime-validation risks are
deferred to later tickets.

Blockers:

- None.

Execution notes:

- Use Ralph for implementation because this changes high-risk package metadata and
  root catalogs.
- Keep the implementation structural: package-root metadata and root catalogs only.
- Treat Codex hook preload and Gemini two-extension runtime support as evidence
  gaps unless separate runtime validation is performed in later tickets.

Continuation note:

No action remains for this structural harness-skeleton ticket. Next work belongs
to later tickets for OpenCode packages, Codex runtime validation, Gemini runtime
validation, public docs/examples, and final release-posture critique.

# Evidence

Disposition: sufficient

Records:

- evidence:harness-package-surface-skeleton-check

Gaps / limits:

- Evidence is structural only; it does not validate Claude, Codex, Cursor, Gemini,
  OpenCode, or generic harness runtime install/discovery behavior.
- Evidence does not create or validate `@z3z1ma/open-loom-core` or
  `@z3z1ma/open-loom-playbooks`
  packages.
- Evidence does not update public docs, examples, root `package.json`, or
  `open-loom.mjs`.
- `spec:core-and-playbooks-package-contract#ACC-007` is satisfied only for changed
  harness manifests and root catalogs in this ticket.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: High-risk native harness package metadata controls install and
preload behavior, and stale root `skills/` paths would mislead users.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-surface
- package-metadata

Findings:

- No open findings in `critique:harness-package-surface-skeleton-review`.
- Initial Cursor root discovery gap was resolved before final critique by adding
  `.cursor-plugin/marketplace.json` with `loom-core` and `loom-playbooks` entries.

Promotion disposition: deferred
Promotion / deferral rationale: Public docs, examples, and accepted installation
explanations belong to later documentation and runtime-validation tickets after
OpenCode/Codex/Gemini posture is settled.

Promoted / deferred:

- Deferred to later package/docs/runtime-validation tickets under
  `plan:split-core-and-playbooks-packages`.

Wiki disposition: not_required

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent
Accepted at: 2026-05-07T22:34:47Z
Basis: `evidence:harness-package-surface-skeleton-check` supports scoped
structural package metadata/catalog acceptance, Ralph packet
`packet:ralph-ticket-7h8u6oxp-20260507T222124Z` is consumed, and mandatory
critique `critique:harness-package-surface-skeleton-review` recommends scoped
acceptance with no open findings.
Residual risks: Claude, Codex, Cursor, Gemini, OpenCode, and generic harness
runtime install/discovery behavior remain unvalidated. Codex preload and Gemini
two-extension support remain deferred evidence needs. OpenCode packages, public
docs/examples, release packaging, and global `ACC-007` cleanup remain later-ticket
scope.

# Dependencies

Hard prerequisites belong in frontmatter `depends_on`; explain important context
here when useful.

- ticket:u9vtemj3 — closed prerequisite for physical `loom-core/skills` and
  `loom-playbooks/skills` package roots.

# Journal

- 2026-05-07T22:20:29Z: Created ready ticket for the non-OpenCode native harness
  package skeleton after closing `ticket:u9vtemj3`.
- 2026-05-07T22:21:24Z: Moved ticket to active and compiled Ralph iteration 01 for
  the common harness package skeleton.
- 2026-05-07T22:26:09Z: Consumed Ralph iteration 01, recorded structural evidence,
  and moved the ticket to mandatory critique review.
- 2026-05-07T22:29:50Z: Added `.cursor-plugin/marketplace.json` after critique
  found the missing Cursor root discovery surface, then reran JSON/catalog checks.
- 2026-05-07T22:34:47Z: Recorded final mandatory critique with no open findings,
  accepted the scoped structural harness skeleton, and closed the ticket.
