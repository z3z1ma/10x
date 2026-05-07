---
id: ticket:xtt24452
kind: ticket
status: closed
change_class: config
risk_class: high
created_at: 2026-05-07T22:37:06Z
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
    - ticket:7h8u6oxp
  packet:
    - packet:ralph-ticket-xtt24452-20260507T223743Z
  evidence:
    - evidence:opencode-split-package-check
  critique:
    - critique:opencode-split-package-review
external_refs: {}
depends_on:
  - ticket:7h8u6oxp
---

# Summary

Split the OpenCode package surface into `@z3z1ma/open-loom-core` and
`@z3z1ma/open-loom-playbooks`, and convert the repository root package into private
non-published repo metadata.

# Context

`ticket:7h8u6oxp` created the common non-OpenCode native harness package skeleton.
The next planned unit is OpenCode-specific packaging. The governing spec now
records the operator decision that the repository root package should become
private/non-published metadata rather than a third published package or
compatibility meta-package.

# Scope

In:

- Add `loom-core/package.json` for package name `@z3z1ma/open-loom-core`.
- Add `loom-core/open-loom-core.mjs` that registers core using-Loom ordered
  references through `config.instructions` and core skills through
  `config.skills.paths`.
- Add `loom-playbooks/package.json` for package name `@z3z1ma/open-loom-playbooks`.
- Add `loom-playbooks/open-loom-playbooks.mjs` that registers only playbook skills
  through `config.skills.paths` and does not preload core using-Loom doctrine.
- Convert root `package.json` to private/non-published repo metadata with scripts
  that smoke-check the two split packages.
- Remove or neutralize root `open-loom.mjs` so the repository root no longer
  presents a third current OpenCode package.
- Run OpenCode package smoke checks, package dry-runs where feasible, root private
  package inspection, stale `skills/`/`open-loom` package claim checks, and
  `git diff --check` for changed OpenCode package files.

Out:

- Publishing packages.
- Creating a compatibility meta-package or deprecation stub for `open-loom`.
- Updating README, INSTALL, ARCHITECTURE, PROTOCOL, AGENTS, or examples.
- Runtime validation in an actual OpenCode install beyond local package smoke
  behavior.
- Changing non-OpenCode harness manifests or skill membership.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Root package becomes private/non-published repo metadata, not a third package. | yes | no | accepted by operator on 2026-05-07 |
| Split package modules may reuse the existing `open-loom.mjs` helper shape with package-local roots. | yes | no | accepted |
| Playbook package should not preload core doctrine because core is a separate dependency. | yes | no | accepted |
| Package dry-run reveals stale file inclusions or missing files. | yes | yes | fix inside this ticket before acceptance |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-005
- spec:core-and-playbooks-package-contract#ACC-007 — scoped to OpenCode package
  files and root package metadata, not public docs/examples.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Closed. Ralph iteration 01 landed the OpenCode split package implementation,
structural/package dry-run evidence is recorded, mandatory critique passed after
the playbooks dependency metadata follow-up, and residual runtime/doc risks are
deferred to later tickets.

Blockers:

- None.

Execution notes:

- Use Ralph for implementation because this changes high-risk package metadata and
  plugin registration behavior.
- Keep root package private and non-published.
- Do not add a compatibility package or public docs in this ticket.

Continuation note:

No action remains for this scoped OpenCode package split ticket. Next work belongs
to later tickets for real OpenCode install validation if needed, Codex validation,
Gemini validation, public docs/examples, and final release-posture critique.

# Evidence

Disposition: sufficient

Records:

- evidence:opencode-split-package-check

Gaps / limits:

- Evidence is local structural/package evidence only; it does not validate a real
  OpenCode install from npm, file path, or plugin array.
- Exact `npm --prefix <pkg> pack --dry-run` commands packed the private root
  workspace package under npm `10.9.4`; evidence instead uses package-root dry-run
  forms and package-local `pack:check` scripts.
- Evidence does not publish packages, update docs, or decide a future deprecation
  notice for the previously published `open-loom` package.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: High-risk OpenCode package metadata affects install behavior
and the transition away from the existing published `open-loom` package surface.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-surface
- package-metadata

Findings:

- No open findings in `critique:opencode-split-package-review`.
- Initial playbooks dependency metadata gap was resolved before final critique by
  adding `@z3z1ma/open-loom-core` to `loom-playbooks/package.json` description and
  `peerDependencies`.

Promotion disposition: deferred
Promotion / deferral rationale: Public docs, examples, package install guidance,
and release migration explanation belong to later documentation/release tickets.

Promoted / deferred:

- Deferred to later package/docs/runtime-validation tickets under
  `plan:split-core-and-playbooks-packages`.

Wiki disposition: not_required

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent
Accepted at: 2026-05-07T22:47:28Z
Basis: `evidence:opencode-split-package-check` supports scoped structural/package
acceptance, Ralph packet `packet:ralph-ticket-xtt24452-20260507T223743Z` is
consumed, and mandatory critique `critique:opencode-split-package-review`
recommends scoped acceptance with no open findings.
Residual risks: No real OpenCode install/plugin-array validation was performed.
`peerDependencies` states the core dependency but does not guarantee OpenCode will
load/register core; docs/operator config remain later-scope work. Public docs,
examples, release packaging, and final stale-reference cleanup remain later-ticket
scope.

# Dependencies

Hard prerequisites belong in frontmatter `depends_on`; explain important context
here when useful.

- ticket:7h8u6oxp — closed prerequisite for package-root harness skeleton and root
  catalogs.

# Journal

- 2026-05-07T22:37:06Z: Created ready ticket for OpenCode split package work after
  root package handling was clarified as private/non-published repo metadata.
- 2026-05-07T22:37:43Z: Moved ticket to active and compiled Ralph iteration 01 for
  the OpenCode split implementation.
- 2026-05-07T22:41:46Z: Consumed Ralph iteration 01, recorded structural/package
  dry-run evidence with the npm-prefix command nuance, and moved the ticket to
  mandatory critique review.
- 2026-05-07T22:45:12Z: Added core dependency metadata to the
  playbooks package after critique, then reran playbooks smoke/dry-run checks and
  tightened evidence wording for untracked files.
- 2026-05-07T22:47:28Z: Recorded final mandatory critique with no open findings,
  accepted the scoped OpenCode split package slice, and closed the ticket.
- 2026-05-07T23:49:27Z: Reconciled package naming after the npm packages were
  scoped as `@z3z1ma/open-loom-core` and `@z3z1ma/open-loom-playbooks`; reran
  `npm run pack:check` successfully.
