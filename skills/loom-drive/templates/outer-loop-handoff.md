---
id: "support:drive-handoff-<TBD: UTC compact timestamp>-<TBD: slug>"
kind: support-artifact
support_kind: drive-outer-loop-handoff
handoff_kind: outer-loop-synthesis
parent_objective: "<TBD: initiative, spec, plan, or ticket id; unrecorded objective only during intake>"
owner_workflow: loom-drive
parent_responsible: "<TBD: parent workflow or agent responsible for review and reconciliation>"
reconciliation_target:
  records:
    - "<TBD: canonical owner record id where accepted truth must land>"
  paths:
    - "<TBD: canonical owner path if needed, or None>"
stale_or_prune_condition: "<TBD: when to mark reconciled, abandoned, superseded, or pruned after review>"
status: draft
created_at: "<TBD: UTC timestamp>"
updated_at: "<TBD: UTC timestamp>"
scope:
  kind: repository
  repositories:
    - repo:root
links: {}
source_snapshot:
  compiled_at: "<TBD: UTC timestamp>"
  compiled_from:
    - "<TBD: owner record id>"
drive_checkpoint:
  anchor: "<TBD: initiative id>"
  active_tranche: "<TBD: plan section or ticket ids>"
  gate_status: "<TBD: choose clear or blocked before saving>"
handoff_write_scope:
  records:
    - "<TBD: proposal-time record write refs, or None - no writes>"
  paths:
    - "<TBD: proposal-time paths, or None - no writes>"
---

# Outer-Loop Synthesis Handoff

Use only when a dedicated subagent would help the parent manage context while
shaping an objective or tranche. This is a support artifact, not a packet family
and not an owner of objective state, ticket state, acceptance, evidence
sufficiency, critique verdicts, wiki truth, canonical truth, or packet lifecycle.

Accepted proposals must be reconciled into the canonical owner records named in
`reconciliation_target` before downstream work relies on them.

# Bound Context

- Objective / initiative:
- Continuity snapshot:
- Research:
- Spec:
- Plan:
- Tickets:
- Evidence / critique / wiki to inspect:
- Source paths, if any:

# Task

Summarize the current objective state and propose the next bounded tranche.

Include:

- current objective and measurable success criteria;
- known constraints and non-goals;
- included/excluded claims;
- likely tickets, dependencies, and write-scope conflicts;
- evidence and critique gates;
- gaps or ambiguities that block safe continuation;
- proposed owner-record changes;
- focused user questions when owner records cannot safely answer a decision.

# Output Contract

- objective criterion IDs affected and proposed status changes;
- current tranche assessment and proposed next tranche;
- safety gates checked and blockers;
- owner-record changes proposed, grouped by layer;
- ticket slices proposed, with scope and acceptance notes;
- risks and unresolved questions;
- evidence reviewed;
- recommendation for parent reconciliation.

# Parent Merge Notes

To be filled by the parent if this handoff is used. Record which proposals were
applied, rejected, or converted into follow-up work. Then mark this support
artifact `reconciled`, `abandoned`, or `superseded`, or prune it if no longer useful.
