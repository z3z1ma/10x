---
id: critique:git-dirty-state-fingerprint-review
kind: critique
status: final
created_at: 2026-05-03T07:58:57Z
updated_at: 2026-05-03T07:58:57Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:gitstat26 diff 110728f..working-tree"
links:
  ticket:
    - ticket:gitstat26
  evidence:
    - evidence:git-dirty-state-fingerprint-validation
  packet:
    - packet:ralph-ticket-gitstat26-20260503T075047Z
external_refs: {}
---

# Summary

Mandatory oracle critique for `ticket:gitstat26` after adding machine-readable
packet Git dirty-state categories.

# Review Target

Current working-tree diff from baseline
`110728f57e570bc047b828e0d5158bf641fb9c87`, covering packet frontmatter,
Ralph packet contract guidance, packet-family templates, ticket reconciliation,
Ralph packet consumption, and evidence.

Required critique profiles: `packet-safety`, `git-provenance`, and
`operator-clarity`.

# Verdict

`pass_with_findings` - product guidance satisfies the ticket acceptance criteria,
but ticket ledger F-001 required reconciliation before closure.

# Findings

## F-001 - Stale next route conflicts with current ticket state

Severity: medium

Confidence: high

Profiles: `operator-clarity`

References:

- `.loom/tickets/20260503-gitstat26-add-machine-readable-dirty-state.md:89-93`
- `.loom/tickets/20260503-gitstat26-add-machine-readable-dirty-state.md:160-165`

Issue: the ticket was `status: review_required` and the journal said it moved to
mandatory critique, but `# Next Move / Next Route` still said `Next route: ralph`.

Impact: a fresh operator could route back into Ralph even though the Ralph packet
was consumed and critique was the live next step.

Required follow-up: reconcile the ticket's next route/current step before
acceptance, then record this critique disposition in ticket truth.

Ticket disposition: resolved at 2026-05-03T07:58:57Z by changing the ticket's
next route to `critique` and naming mandatory critique rereview as the current
step. Rereview is required before closure.

# Profile Results

- `packet-safety`: pass. Packet scope, child write boundary, stop conditions, and
  parent merge boundary are explicit. No runtime/helper/schema/new-owner layer
  leaked.
- `git-provenance`: pass. New guidance treats Git status as freshness/provenance
  metadata, not acceptance truth. `git_status_detail` remains available for human
  context.
- `operator-clarity`: pass with finding F-001. The new `git_status_summary`
  categories are clear enough, and `unknown` is constrained to unsafe or
  untruthful inspection with rationale.

# Evidence Reviewed

- Scoped working-tree diff from `110728f57e570bc047b828e0d5158bf641fb9c87`.
- `ticket:gitstat26`
- `packet:ralph-ticket-gitstat26-20260503T075047Z`
- `evidence:git-dirty-state-fingerprint-validation`
- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`
- Targeted searches for old/new grammar and `git_status_summary`.
- `git diff --check`: passed with no output.

# Acceptance Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027`: supported.
- `ticket:gitstat26#ACC-001`: supported. Dirty categories appear in packet
  frontmatter/reference/template guidance.
- `ticket:gitstat26#ACC-002`: supported. `clean` and `unknown` remain, with
  rationale guidance.
- `ticket:gitstat26#ACC-003`: supported. `git_status_detail` remains in
  references/templates.
- `ticket:gitstat26#ACC-004`: supported. Evidence records targeted searches and
  `git diff --check`.
- `ticket:gitstat26#ACC-005`: not satisfied by this review alone because F-001
  required disposition and rereview.

# Residual Risks

- Existing consumed `.loom` packets still contain legacy `git_status_summary:
  dirty`; this is not blocking because they are historical support artifacts, not
  current authoring guidance.

# Required Follow-up

Resolve F-001 in ticket truth and run critique rereview before closure.

# Acceptance Recommendation

`do-not-close-yet` until rereview confirms no unresolved findings.
