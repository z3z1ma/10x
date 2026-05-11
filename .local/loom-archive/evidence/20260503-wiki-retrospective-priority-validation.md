---
id: evidence:wiki-retrospective-priority-validation
kind: evidence
status: recorded
created_at: 2026-05-03T06:51:39Z
updated_at: 2026-05-03T06:51:39Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:wikiret14
  packet:
    - packet:ralph-ticket-wikiret14-20260503T064951Z
external_refs: {}
---

# Summary

Validation observations for `ticket:wikiret14`, checking that drive route priority
has distinct `wiki` and `retrospective` rows while preserving reconciliation to
the correct owner layers.

# Procedure

- Inspected the scoped diff for `ticket:wikiret14`.
- Searched the drive tranche decision protocol for `wiki`, `retrospective`, and
  reconciliation target wording.
- Searched for new record-kind, retrospective-directory/ledger, runtime, schema,
  validator, command-router, or owner-layer additions.
- Ran `git add -N .loom/packets/ralph/20260503T064951Z-ticket-wikiret14-iter-01.md`.
- Ran `git diff --check -- .loom/tickets/20260503-wikiret14-split-wiki-retrospective-priority.md .loom/packets/ralph/20260503T064951Z-ticket-wikiret14-iter-01.md skills/loom-drive/references/tranche-decision-protocol.md`.

# Artifacts

Scoped changed tracked files:

- `.loom/tickets/20260503-wikiret14-split-wiki-retrospective-priority.md`
- `skills/loom-drive/references/tranche-decision-protocol.md`

Scoped new packet file:

- `.loom/packets/ralph/20260503T064951Z-ticket-wikiret14-iter-01.md`

Targeted observations:

- `skills/loom-drive/references/tranche-decision-protocol.md:76` now routes
  accepted reusable explanation, architecture explanation, or workflow concept
  capture to `wiki`.
- `skills/loom-drive/references/tranche-decision-protocol.md:77` now routes
  accepted learning that should compound or promote across owner layers before
  closure to `retrospective`.
- `skills/loom-drive/references/tranche-decision-protocol.md:146-147` preserves
  reconciliation of wiki/retrospective results into wiki, research, spec, plan,
  initiative, constitution, or memory as appropriate, plus ticket disposition.
- Targeted searches did not find any new retrospective directory, ledger, record
  kind, route token, runtime, schema, validator, command router, or owner-layer
  mechanism in the scoped diff.

`git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-015`
- `ticket:wikiret14#ACC-001`
- `ticket:wikiret14#ACC-002`
- `ticket:wikiret14#ACC-003`
- `ticket:wikiret14#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `922e342cedd88378d6ef5f02c7f162bc2e2edc58` plus uncommitted scoped
`ticket:wikiret14` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no generated files, lockfiles, runtime, command wrapper, schema,
validator, command router, retrospective ledger, or new owner layer observed in
the scoped diff.

# Validity

Valid for: the scoped `ticket:wikiret14` diff at 2026-05-03T06:51:39Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It does not prove future drive operators
will always choose between wiki and retrospective correctly.

# Result

Drive route priority now has distinct `wiki` and `retrospective` rows and retains
the shared reconciliation target guidance for owner-layer promotion. The scoped
diff passes `git diff --check`.

# Interpretation

The evidence supports the ticket's wiki/retrospective route-priority claims. It
does not close the ticket; mandatory critique and the ticket-owned acceptance
decision remain separate gates.

# Related Records

- `ticket:wikiret14`
- `packet:ralph-ticket-wikiret14-20260503T064951Z`
