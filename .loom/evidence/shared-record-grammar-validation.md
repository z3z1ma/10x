---
id: evidence:shared-record-grammar-validation
kind: evidence
status: recorded
created_at: 2026-05-02T09:39:09Z
updated_at: 2026-05-02T09:39:09Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  tickets:
    - ticket:4e8ebe92
  packets:
    - packet:ralph-ticket-4e8ebe92-20260502T091549Z
  critique:
    - critique:shared-record-grammar-review
  plan:
    - plan:skills-corpus-protocol-sharpening
external_refs: {}
---

# Summary

Structural validation for shared objective, record-kind, memory exception,
semantic-link, and external-reference grammar added under `ticket:4e8ebe92`.

# Procedure

The parent reviewed the Ralph child output, routed two oracle critique passes back
through the fixer/parent reconciliation, normalized legacy objective references,
and ran targeted structural checks on the final diff.

Commands and searches performed:

```text
git diff --check
git diff --stat
Grep legacy split objective-reference forms in .loom
Grep initiative:<slug>#OBJ-001 and OBJ-* grammar in claim-coverage.md
Grep current kind/ID/path and packet family table entries in naming-and-ids.md
Grep memory frontmatter/status exception wording in loom-records references
Grep supersession, external_refs, and shadow ledger wording in semantic-link-usage.md
Grep objective, ID/path, packet_kind, external_refs, accepted_risk, follow-up, and promotion query examples in query-and-linking.md
```

# Artifacts

Observed product files changed:

- `skills/loom-records/references/claim-coverage.md`
- `skills/loom-records/references/naming-and-ids.md`
- `skills/loom-records/references/frontmatter.md`
- `skills/loom-records/references/status-lifecycle.md`
- `skills/loom-records/references/semantic-link-usage.md`
- `skills/loom-records/references/query-and-linking.md`
- `skills/loom-initiatives/SKILL.md`
- `skills/loom-initiatives/references/initiative-shape.md`
- `skills/loom-initiatives/templates/initiative.md`

Observed Loom record reconciliation:

- Existing old split objective references were normalized to
  `initiative:<slug>#OBJ-*` in active or relevant ticket/evidence/packet records.
- `research:skills-corpus-council-review` now records that objective-reference
  shape and current-supported `kind:` vocabulary questions were resolved by this
  ticket.

Observed outputs:

```text
git diff --check
-> no output

Grep legacy split objective-reference forms in .loom
-> no files found

Grep initiative:<slug>#OBJ-001 and OBJ-* grammar in claim-coverage.md
-> found objective criteria grammar, cross-record reference shape, ticket/evidence/critique examples, and useful queries

Grep current kind/ID/path and packet family table entries in naming-and-ids.md
-> found Current Supported Kinds, IDs, And Paths table, constitution path, ralph/critique/wiki packet rows, and optional memory support metadata row

Grep memory frontmatter/status exception wording
-> found Support-Layer Memory Exception, optional `kind: memory`, no canonical ID guidance, and retrieval-oriented memory status wording

Grep semantic link and external reference wording
-> found superseded record, superseded claim/criterion, external_refs support-surface guidance, and shadow ticket ledger prohibition

Grep query examples
-> found objective criterion tracing, supported ID/path discovery, packet_kind family queries, external_refs, accepted risk, follow-up, and promotion queries
```

Final diff stat before evidence creation:

```text
25 files changed, 275 insertions(+), 81 deletions(-)
```

# Supports Claims

- `ticket:4e8ebe92` ACC-001
- `ticket:4e8ebe92` ACC-002
- `ticket:4e8ebe92` ACC-003
- `ticket:4e8ebe92` ACC-004
- `ticket:4e8ebe92` ACC-005
- `ticket:4e8ebe92` ACC-006
- `initiative:skills-corpus-protocol-sharpening#OBJ-002`
- `research:skills-corpus-council-review#CLAIM-005`
- `research:skills-corpus-council-review#CLAIM-007`

# Challenges Claims

None observed.

# Environment

Commit: `e6687aa122eb88018dc9fb369f9fe0e2c480eb93` plus the current working-tree
diff for `ticket:4e8ebe92` before commit.

Branch: `main`

Runtime: OpenCode parent session with Ralph fixer subagent and oracle critique
subagent.

OS: darwin

Relevant config: repository has no automated test suite; validation is structural
and manual per `AGENTS.md`.

# Validity

Valid for: the working tree after `packet:ralph-ticket-4e8ebe92-20260502T091549Z`
and oracle critique pass `ses_217f5279bffefk2upyJxpbjRGt`.

Recheck when: `skills/loom-records/**`, `skills/loom-initiatives/**`, or
objective-reference grammar changes.

# Limitations

This evidence validates structural presence and consistency of the ticket-scoped
grammar changes. It is not a formal schema validator and does not replace the
final corpus-wide validation in `ticket:cdf664af`.

# Result

The shared grammar now documents `OBJ-*` objective criteria with qualified
`initiative:<slug>#OBJ-*` references, current supported kind/ID/path families,
memory support exceptions, semantic link boundaries, external-reference support
semantics, and ordinary grep-friendly validation queries.

# Interpretation

The observations support acceptance of `ticket:4e8ebe92` when combined with
`critique:shared-record-grammar-review`. Evidence does not itself close the
ticket; the ticket acceptance decision owns closure.

# Related Records

- `ticket:4e8ebe92`
- `packet:ralph-ticket-4e8ebe92-20260502T091549Z`
- `critique:shared-record-grammar-review`
- `plan:skills-corpus-protocol-sharpening`
