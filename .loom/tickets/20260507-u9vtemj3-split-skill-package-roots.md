---
id: ticket:u9vtemj3
kind: ticket
status: closed
change_class: code-structure
risk_class: high
created_at: 2026-05-07T22:08:19Z
updated_at: 2026-05-07T22:19:03Z
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
    - ticket:hi5e7nbr
  packet:
    - packet:ralph-ticket-u9vtemj3-20260507T220907Z
    - packet:ralph-ticket-u9vtemj3-20260507T221312Z
  evidence:
    - evidence:skill-package-root-split-check
  critique:
    - critique:skill-package-root-split-review
external_refs: {}
depends_on:
  - ticket:hi5e7nbr
---

# Summary

Create the two physical skill package roots by moving core skills into
`loom-core/skills` and playbook skills into `loom-playbooks/skills`, retiring the
top-level `skills/` directory as a product surface.

# Context

`ticket:hi5e7nbr` already decoupled core prose from optional playbook assumptions.
This ticket performs the next bounded implementation slice from
`plan:split-core-and-playbooks-packages`: the source layout split. Harness
manifests, package metadata, public docs, and runtime validation remain later
tickets.

# Scope

In:

- Create top-level `loom-core/skills` and `loom-playbooks/skills` directories.
- Move the exact core skill directories named by
  `spec:core-and-playbooks-package-contract#REQ-003` into `loom-core/skills`.
- Move the exact playbook skill directories named by
  `spec:core-and-playbooks-package-contract#REQ-004` into `loom-playbooks/skills`.
- Remove the top-level `skills/` directory by emptying it through moves.
- Update moved skill-internal references that would otherwise point at the retired
  top-level root `skills/` as current product truth, preferring package-root or
  relative `skills/...` wording when appropriate.
- Run structural membership scans, skill frontmatter scans, stale root path scans,
  and `git diff --check`.

Out:

- Editing `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, Gemini extension,
  OpenCode package, or root marketplace/catalog files.
- Updating README, INSTALL, ARCHITECTURE, PROTOCOL, AGENTS, or examples except if
  a narrow moved-skill reference requires it.
- Creating final release/package docs.
- Validating harness runtime installs.
- Changing core/playbook membership.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| File moves may use native shell `mkdir`/`mv` because directory moves are bulk filesystem operations, while prose edits use `apply_patch`. | yes | no | accepted |
| Package-root skill prose may still use relative `skills/<skill>` paths when explicitly framed from within a package root. | yes | no | accepted |
| A path reference cannot be made truthful without editing public docs or manifests. | yes | yes | stop and leave for the docs/manifest ticket rather than widening scope |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-001
- spec:core-and-playbooks-package-contract#ACC-002 — structural/package inspection
  only, not harness runtime discovery.
- spec:core-and-playbooks-package-contract#ACC-003 — structural duplicate-core and
  dependency wording inspection only.
- spec:core-and-playbooks-package-contract#ACC-007 — scoped to moved skill corpus
  references, not public docs/manifests/examples.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Closed. The physical source-layout migration landed, follow-up playbook path
cleanup landed, structural evidence is recorded, mandatory critique is recorded,
and all open medium/high critique findings have ticket-owned dispositions.

Blockers:

- None.

Execution notes:

- Ralph iteration 01 moved the skill corpus into `loom-core/skills` and
  `loom-playbooks/skills`, retiring the root `skills/` directory.
- Ralph iteration 02 removed explicit core `skills/...` file paths from playbook
  prose after the package-root split.
- The iteration 01 packet over-granted write scope to `loom-core/**` and
  `loom-playbooks/**`; ticket acceptance treats this as an accepted scoped risk
  because inspection found no out-of-scope package metadata or manifest edits and
  iteration 02 used the narrower `loom-playbooks/skills/**` write scope.

Continuation note:

No action remains for this source-layout ticket. Next work belongs to later
tickets for harness/package surfaces, public docs/examples, and runtime install
validation.

# Evidence

Disposition: sufficient

Records:

- evidence:skill-package-root-split-check

Gaps / limits:

- Evidence is structural only. It does not validate Claude, Codex, Cursor, Gemini,
  OpenCode, or generic harness install behavior.
- Evidence does not update or validate public docs, root catalogs, manifests,
  package metadata, examples, tarball contents, or runtime skill discovery.
- `spec:core-and-playbooks-package-contract#ACC-007` is satisfied only for the
  moved skill corpus in this ticket; full package-surface consistency remains
  later-ticket scope.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: High-risk source-layout and protocol product-surface change.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-surface
- code-structure

Findings:

- critique:skill-package-root-split-review#FIND-001 — resolved. Both Ralph
  packets are now `status: consumed`, child output and parent merge notes are
  recorded, evidence is linked, and this ticket carries acceptance truth.
- critique:skill-package-root-split-review#FIND-002 — resolved. Evidence now
  distinguishes package-root trailing-whitespace scans from tracked-deletion
  `git diff --check` output and no longer treats untracked package-root files as
  covered by normal `git diff --check`.
- critique:skill-package-root-split-review#FIND-003 — accepted_risk. Iteration 01
  over-granted package-root write authority, but inspection found no out-of-scope
  package metadata or manifest edits; the realized writes were the intended skill
  moves and playbook `SKILL.md` dependency wording, and iteration 02 used the
  narrower `loom-playbooks/skills/**` scope.

Promotion disposition: deferred
Promotion / deferral rationale: Public documentation, examples, package metadata,
and harness install guidance belong to later tickets after source layout and
runtime package surfaces are validated. No standalone wiki promotion is required
for this bounded source-layout slice.

Promoted / deferred:

- Deferred to later package/docs/runtime-validation tickets under
  `plan:split-core-and-playbooks-packages`.

Wiki disposition: not_required

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent
Accepted at: 2026-05-07T22:19:03Z
Basis: `evidence:skill-package-root-split-check` supports scoped structural
package-root acceptance, both Ralph packets are consumed, and mandatory critique
`critique:skill-package-root-split-review` has ticket-owned dispositions for all
open medium/high findings.
Residual risks: Harness manifests, package metadata, public docs, examples,
tarball contents, and runtime install/discovery behavior remain unvalidated and
are intentionally deferred to later tickets. Full `ACC-007` consistency remains
broader than this moved-skill-corpus slice.

# Dependencies

Hard prerequisites belong in frontmatter `depends_on`; explain important context
here when useful.

- ticket:hi5e7nbr — closed prerequisite for core prose decoupling.

# Journal

- 2026-05-07T22:08:19Z: Created ready ticket for the physical skill package-root
  split after closing `ticket:hi5e7nbr`.
- 2026-05-07T22:09:07Z: Moved ticket to active and prepared Ralph iteration 01
  for the bounded skill package-root split.
- 2026-05-07T22:14:33Z: Recorded structural evidence after Ralph iteration 01
  moved skills and Ralph iteration 02 cleaned playbook-to-core path references.
- 2026-05-07T22:17:35Z: Recorded mandatory critique. Source split was
  structurally acceptable, but records needed packet lifecycle, evidence wording,
  and write-scope disposition reconciliation.
- 2026-05-07T22:19:03Z: Reconciled Ralph packets, updated evidence wording,
  dispositioned critique findings, accepted the scoped source-layout slice, and
  closed the ticket.
