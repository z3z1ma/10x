---
id: ticket:usng507a
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-07T19:10:00Z
updated_at: 2026-05-07T19:35:57Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:using-loom-rename-validation
  critique:
    - critique:using-loom-rename-review
external_refs: {}
depends_on: []
---

# Summary

Rename Loom's entry skill from `loom-bootstrap` to `using-loom` and align the skill corpus, bootstrap doctrine, public docs, adapter surfaces, and Loom owner records with the current product framing.

# Context

The operator requested fixes for the full skill-corpus review findings plus two additional framing corrections: plans are for high-level complex-change planning, not only sequencing/rollout, and using-Loom doctrine should better reflect the README's model of Loom as a structured paper process for coding agents.

# Scope

In:

- Rename `skills/loom-bootstrap` to `skills/using-loom` and update product-surface references.
- Update adapter/plugin/bootstrap preload paths to the renamed skill.
- Align plan ownership wording across using-loom doctrine, README, architecture notes, and related skills without changing `loom-plans` section structure to satisfy `loom-drive`.
- Fix the prior review findings in ticket acceptance, critique query recipes, drive references, wiki packet/status guidance, and support-surface framing.
- Reconcile constitutional owner records affected by the rename.
- Preserve structural evidence and critique before closure.

Out:

- No hidden runtime, helper-dependent semantics, or command wrapper product surface.
- No edits to unrelated untracked `examples/00-todo-app` content.
- No backwards-compatible duplicate `loom-bootstrap` skill unless a concrete shipped compatibility need is recorded.

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:usng507a#ACC-001 — all old `loom-bootstrap` product-surface references are updated to `using-loom`, including preload paths.
- ticket:usng507a#ACC-002 — plan wording consistently presents plans as high-level complex-change planning that may decompose into detailed tickets.
- ticket:usng507a#ACC-003 — README/using-loom doctrine consistently frame Loom as a structured paper process/work-product graph for coding agents, without a broad rewrite.
- ticket:usng507a#ACC-004 — the eight review findings from the skill audit are addressed in their owning surfaces.
- ticket:usng507a#ACC-005 — structural verification and critique are recorded before closure.

# Finding Disposition

| ID | Finding / request | Disposition |
| --- | --- | --- |
| F-001 | Mandatory critique closure wording in ticket acceptance gate is too weak. | Resolved in `skills/loom-tickets/references/acceptance-gate.md`; mandatory critique closure now requires a final critique record and ticket-owned finding dispositions. |
| F-002 | Critique query recipe does not match critique template headings/body fields. | Resolved in `skills/loom-records/references/query-and-linking.md`; query guidance now matches critique record fields/headings. |
| F-003 | Loom Drive points plans at nonexistent `# Strategy Snapshot`. | Resolved in `skills/loom-drive/references/*`; drive now points at existing plan structure and ticket detail instead of changing `loom-plans` to satisfy drive. |
| F-004 | Loom Drive objective/gap state vocabulary drifts across references. | Resolved across drive references, including the final checkpoint fix to `partially_satisfied` / `out_of_scope`. |
| F-005 | Loom Drive treats ticket claim matrix as required. | Resolved in drive guidance; tickets may use inline coverage when a matrix is unnecessary. |
| F-006 | Wiki packet source-status examples are too narrow. | Resolved in `skills/loom-wiki/templates/wiki-packet.md`; source-status guidance is broader and fails closed. |
| F-007 | Wiki maintenance omits `retired` status. | Resolved in `skills/loom-wiki/references/maintenance.md`. |
| F-008 | Bootstrap support-surface summary omits `.loom/workspace.md` / `.loom/harness.md`. | Resolved by updating using-Loom/support-surface framing to name `.loom/workspace.md` and `.loom/harness.md` where relevant. |
| U-001 | Rename `loom-bootstrap` skill to `using-loom`. | Resolved; `skills/using-loom` exists, `skills/loom-bootstrap/**` is absent, and product/current owner stale-name scans are clean. |
| U-002 | Correct plan framing from sequencing/rollout-only to high-level complex-change planning. | Resolved across README, architecture, using-Loom doctrine, plans, and related skill references. |
| U-003 | Embed README's Loom/LLM framing into entry doctrine without major rewriting. | Resolved in `skills/using-loom/SKILL.md` and the ordered using-Loom references. |

# Current State

Status rationale:

Closed; implementation, structural evidence, mandatory critique, finding
dispositions, and acceptance review are complete for the scoped rename and
doctrine-alignment work.

Blockers:

None.

Execution notes:

- Existing untracked `examples/00-todo-app` files are unrelated and were not modified.
- The final critique found five issues during review; follow-up edits resolved the
  implementation and owner-record concerns before closure.

# Evidence

Disposition: sufficient

Records:

- evidence:using-loom-rename-validation

Gaps / limits:

- Evidence does not prove Claude, Codex, Gemini, Cursor, or OpenCode runtime
  install behavior outside the local `open-loom` smoke/package dry-run.
- Historical closed `.loom` records may still contain old entry-skill names as
  historical observations.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: This rename and doctrine framing affect protocol authority, entry-skill activation, public docs, and adapter preload behavior.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-clarity
- packaging-surface

Findings:

| Finding | Ticket-owned disposition |
| --- | --- |
| critique:using-loom-rename-review#FIND-001 | resolved - drive activation wording now covers broad delegated outcome requests. |
| critique:using-loom-rename-review#FIND-002 | resolved - drive objective-state vocabulary now matches across references. |
| critique:using-loom-rename-review#FIND-003 | resolved - current packaging owner records no longer encode seven-reference using-Loom expectations. |
| critique:using-loom-rename-review#FIND-004 | resolved - this ticket now consumes final evidence, critique, dispositions, and acceptance. |
| critique:using-loom-rename-review#FIND-005 | resolved - the high-risk protocol-change fixture paths now use `using-loom`. |

Promotion disposition: completed
Promotion / deferral rationale: Constitutional, initiative, plan, research, spec,
and accepted wiki owner records that currently constrain the product surface were
reconciled to the renamed entry skill and updated plan framing. No new wiki page
was required because this changed existing product doctrine rather than adding a
new reusable concept.

Wiki disposition: not_required with reason - this repairs product-surface doctrine and owner records rather than introducing a new reusable explanation page.

# Acceptance Decision

Accepted and closed.

Basis:

- ACC-001 satisfied by the `using-loom` directory rename, adapter preload path
  updates, OpenCode smoke output, package dry-run contents, and stale-name scans.
- ACC-002 satisfied by plan framing updates in using-Loom doctrine, README,
  architecture notes, plans, and related skills.
- ACC-003 satisfied by the structured paper process / typed work-product graph
  framing added to using-Loom and aligned public docs.
- ACC-004 satisfied by the resolved finding disposition table and the final
  critique fixes.
- ACC-005 satisfied by `evidence:using-loom-rename-validation` and
  `critique:using-loom-rename-review`.

Residual risks are limited to runtime validation outside the local OpenCode smoke
and package dry-run; those harness-specific runtime checks are outside this ticket
unless future adapter tickets require them.

# Dependencies

Hard prerequisites:

- None.

Soft links / related work:

- ticket:pkt7z924 — earlier closed skill-corpus fix pass; superseded only for newly identified follow-up scope.

# Journal

- 2026-05-07T19:10:00Z — Created active ticket for entry-skill rename and doctrine alignment.
- 2026-05-07T19:32:42Z — Recorded `evidence:using-loom-rename-validation` after stale-name scans, skill frontmatter validation, `git diff --check`, and `npm run pack:check` passed.
- 2026-05-07T19:33:33Z — Recorded final mandatory critique `critique:using-loom-rename-review`; initial findings were fixed and targeted re-check found no remaining issues in scope.
- 2026-05-07T19:34:17Z — Accepted and closed the ticket after linking evidence, dispositioning critique findings, and recording acceptance basis.
- 2026-05-07T19:35:57Z — Reconciled the remaining before/after high-risk fixture paths, confirmed no `**/loom-bootstrap/**` file paths remain, and updated evidence/critique notes without changing the acceptance decision.
