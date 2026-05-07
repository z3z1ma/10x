---
id: ticket:artf507
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T15:09:40Z
updated_at: 2026-05-07T15:37:30Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:artifact-store-validation
  critique:
    - critique:artifact-store-review
external_refs: {}
depends_on: []
---

# Summary

Add Loom guidance for optional gitignored raw artifact stores under evidence and
research, while preserving evidence and research records as the primary durable
understanding.

# Context

The user asked for evidence to pull and store logs, traces, responses, screenshots,
and related raw outputs in a canonical `.loom/evidence/...` directory, and for
research to support a similar subdirectory for articles, web requests, PDFs, peer
repos, and other source material. These stores should usually be gitignored and
useful during live work, but not guaranteed to exist. The records remain the source
future agents should read first.

# Scope

In:

- Define optional raw artifact store paths for evidence and research.
- Teach that the stores are support caches, not canonical owner records or truth
  owners.
- Update evidence/research templates to cite artifact store paths and explain
  whether raw artifacts were captured, omitted, redacted, or intentionally tracked.
- Gitignore default raw artifact store directories for this repository's dogfood
  workspace.
- Validate structurally and run critique before closure.

Out:

- Do not add scanners, uploaders, download managers, MCP requirements, databases,
  or helper runtimes.
- Do not require artifact stores to exist for every evidence or research record.
- Do not store secrets or sensitive personal data in raw artifact stores.
- Do not modify unrelated todo-app example files.

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:artf507#ACC-001
- ticket:artf507#ACC-002
- ticket:artf507#ACC-003
- ticket:artf507#ACC-004
- ticket:artf507#ACC-005

Ticket-local criteria:

- ACC-001: Evidence guidance defines the `.loom/evidence/artifacts/` slugged subdirectory as an optional raw artifact store for logs, traces, responses, screenshots, command output, and similar observations.
- ACC-002: Research guidance defines the `.loom/research/artifacts/` slugged subdirectory as an optional source-material store for articles, web fetches, PDFs, arXiv papers, repo clones, snapshots, and other investigation inputs.
- ACC-003: Guidance states artifact stores are usually gitignored support caches, may be absent, and may be inspected during live work, but the Markdown evidence/research record is the primary understanding future agents should rely on.
- ACC-004: Templates and shared record guidance make artifact-store citation, redaction, retention, and optional tracked-artifact exceptions explicit without introducing a hidden runtime or new owner layer.
- ACC-005: Structural validation and mandatory critique find no unresolved high/medium blockers, hidden-runtime drift, or owner-layer boundary regression.

# Current State

Status rationale:

`closed` because artifact-store guidance, template updates, `.gitignore` coverage,
validation evidence, mandatory critique, and acceptance reconciliation are recorded.

Blockers:

None.

Execution notes:

- Product write boundary is evidence/research/records guidance and templates plus
  `.gitignore` and this ticket's support records.
- Raw artifact directories should be documented and gitignored; do not create a
  new runtime or canonical record family.

Continuation note:

No immediate continuation is required for this ticket.

# Evidence

Disposition: sufficient for closure

Records:

- `evidence:artifact-store-validation`

Gaps / limits:

- Evidence is structural and content-anchor based; it does not prove future agents
  will capture, redact, or interpret raw artifacts well.
- Validation did not create a raw artifact directory; `.gitignore` coverage was
  checked with representative paths.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority changes to evidence/research truth boundaries and filesystem support surfaces.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency

Findings:

- `critique:artifact-store-review#FIND-001`: resolved by this ticket reconciliation
  linking evidence and critique, recording finding disposition, and filling
  acceptance provenance.

Promotion disposition: completed
Promotion / deferral rationale: accepted guidance landed in existing evidence,
research, and record-grammar skill surfaces plus `.gitignore`.

Promoted / deferred:

- Promoted into `skills/loom-evidence/SKILL.md`,
  `skills/loom-evidence/references/evidence-quality.md`,
  `skills/loom-evidence/templates/evidence.md`, `skills/loom-research/SKILL.md`,
  `skills/loom-research/references/source-handling.md`,
  `skills/loom-research/templates/research.md`,
  `skills/loom-records/references/naming-and-ids.md`, and `.gitignore`.

Wiki disposition: not_required - the product skill corpus carries the accepted
guidance; no separate wiki page is needed for closure.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent under user-delegated Loom operation
Accepted at: 2026-05-07T15:37:30Z
Basis: `ticket:artf507#ACC-001` through `ticket:artf507#ACC-005` are supported by
the scoped skill/template/`.gitignore` edits, `evidence:artifact-store-validation`,
and mandatory critique `critique:artifact-store-review`; no high/medium blockers
remain.
Residual risks: Raw stores under canonical owner directories may confuse naive
tooling or operators despite guidance; secret/sensitive-data handling remains
operator discipline, not a scanner/runtime; template additions add some burden.

# Dependencies

None.

# Journal

- 2026-05-07T15:09:40Z: Created ticket after user requested canonical optional raw artifact stores for evidence and research, usually gitignored and explicitly secondary to the evidence/research records.
- 2026-05-07T15:12:08Z: Added artifact-store guidance, template sections, record
  grammar, and `.gitignore` entries; recorded validation evidence.
- 2026-05-07T15:37:30Z: Mandatory critique found no high/medium blockers; linked
  evidence and critique, dispositioned the low ledger finding, recorded acceptance,
  and closed the ticket.
