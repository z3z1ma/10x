---
id: ticket:hi5e7nbr
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T21:51:37Z
updated_at: 2026-05-07T21:52:48Z
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
  decision:
    - decision:0008
  critique:
    - critique:core-playbooks-package-contract-review
external_refs: {}
depends_on: []
---

# Summary

Decouple core Loom doctrine and operator-routing prose from optional playbooks so
the current core skill corpus can be made coherent for a future core-only package
before any directory move happens.

# Context

`decision:0008` authorizes the product split into `loom-core/` and
`loom-playbooks/`. `spec:core-and-playbooks-package-contract` requires core prose
to remain coherent when playbooks are absent, and the split plan identifies
doctrine decoupling as the first implementation slice before moving skill
directories.

The current source tree still has a top-level `skills/` directory. This ticket
should not point active skill guidance at nonexistent `loom-core/skills` paths.
Instead, it should remove assumptions that optional playbook skills are always
installed and prefer skill-name, owner-layer, or package-role wording where path
specificity would become stale after the package move.

# Scope

In:

- Review core skill prose for assumptions that optional playbook skills are always
  present, mandatory, or part of the core package.
- Update core guidance so optional playbook routes are described as installed
  playbooks or user-provided equivalent workflows, while keeping Ralph,
  retrospective, memory, canonical owner layers, records, and workspace behavior
  core.
- Prefer path-stable wording over hardcoded root `skills/skill-name/...` references
  when cross-skill references would become stale after the package split.
- Target the current core skill surfaces most likely to route to optional
  playbooks: `skills/using-loom`, `skills/loom-workspace`, `skills/loom-records`,
  `skills/loom-plans`, `skills/loom-tickets`, and `skills/loom-research`.
- Run targeted stale-assumption searches for playbook skill names in core skill
  files and preserve the results as evidence.

Out:

- Physically moving `skills/` into `loom-core/skills` or `loom-playbooks/skills`.
- Creating `loom-core/` or `loom-playbooks/` package roots.
- Editing harness manifests, OpenCode packages, Gemini extensions, Codex hooks, or
  marketplace catalogs.
- Rewriting public README/INSTALL/ARCHITECTURE docs except for record links if a
  later ticket scopes that work.
- Changing core/playbook membership established by `decision:0008` and
  `spec:core-and-playbooks-package-contract`.
- Claiming full satisfaction of `spec:core-and-playbooks-package-contract#ACC-002`
  or `#ACC-007`; this ticket covers only the core doctrine/prose subset.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Optional playbook skills should be named as optional compositions, not removed from all examples. | yes | no | accepted; keep useful examples if dependency is clear |
| Active core skill guidance should avoid pointing at `loom-core/skills` until files actually move. | yes | no | accepted; use package-role or skill-name wording where possible |
| A core skill may still mention a playbook when routing a user to an optional installed workflow. | yes | no | accepted if the text names the dependency/optional nature |
| A core skill appears impossible to make coherent without a playbook skill. | yes | yes | stop and route back to spec/plan before widening scope |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-002 — scoped to core doctrine and
  operator prose, not package-root creation.
- spec:core-and-playbooks-package-contract#ACC-007 — scoped to active core skill
  references and optional-playbook assumptions, not all public docs or manifests.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Ready. The constitutional decision, behavior spec, split plan, and spec critique
exist. The scope is bounded to core doctrine/prose decoupling and explicitly
excludes moving directories or editing harness packages.

Blockers:

- None.

Execution notes:

- Start by searching current core skill files for optional playbook skill names:
  `loom-drive`, `loom-git`, `loom-debugging`, `loom-spike`, `loom-codemap`,
  `loom-ship`, and `loom-skill-authoring`.
- Also search for hardcoded root-path references of the form `skills/loom-*` in
  the scoped core files.
- Edit only the minimum prose needed to make core-only operation truthful before
  the physical package move.

Continuation note:

The next agent should implement this as a protocol-authority prose change, gather
structural evidence, then route to mandatory critique before any acceptance claim.

# Evidence

Disposition: pending

Records:

- None - no implementation evidence yet.

Gaps / limits:

- Need targeted search output for optional-playbook assumptions in scoped core
  skill files.
- Need diff review and `git diff --check` after edits.
- Need explicit note of any remaining playbook mentions in core guidance and why
  they are safe.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: High-risk protocol-authority change that affects how agents
route work and understand the core/playbook product boundary.
Critique disposition: pending

Required critique profiles:

- protocol-change
- operator-surface
- operator-clarity

Findings:

- None - no implementation critique yet.

Promotion disposition: pending
Promotion / deferral rationale: Non-trivial product-boundary work may need wiki or
doc promotion after implementation and critique; decide before closure.

Promoted / deferred:

- None yet.

Wiki disposition: pending

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

Hard prerequisites belong in frontmatter `depends_on`; explain important context
here when useful.

None. `decision:0008` and `spec:core-and-playbooks-package-contract` are already
linked as governing owner records, not live ticket dependencies.

# Journal

- 2026-05-07T21:51:37Z: Created ticket as the first implementation slice under
  `plan:split-core-and-playbooks-packages`, scoped to decoupling core doctrine
  from optional playbook assumptions before directory migration.
