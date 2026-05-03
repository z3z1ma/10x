---
id: evidence:readme-route-table-framing-validation
kind: evidence
status: recorded
created_at: 2026-05-03T08:51:36Z
updated_at: 2026-05-03T08:54:24Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:readrte29
  packet:
    - packet:ralph-ticket-readrte29-20260503T085013Z
  critique:
    - critique:readme-route-table-framing-review
external_refs: {}
---

# Summary

Validation observations for `ticket:readrte29`, checking that README frames its
route table as introductory and points to `route-vocabulary.md` for complete
route-token and saved-field route grammar.

# Procedure

- Inspected the scoped README diff for `ticket:readrte29`.
- Searched README for introductory route-table framing, `route-vocabulary.md`,
  saved-field route grammar, and the unchanged `Situation | Loom route` table.
- Parent-side validation used `git add -N` for new scoped Loom records before
  `git diff --check` so the new records were included in the whitespace check.
  This happened during parent reconciliation/validation, not during child
  execution; the child did not mutate Git metadata.
- Ran `git diff --check`.

# Artifacts

Scoped changed tracked files:

- `README.md`
- `.loom/tickets/20260503-readrte29-frame-readme-route-table-as-intro.md`

Scoped new Loom record files:

- `.loom/packets/ralph/20260503T085013Z-ticket-readrte29-iter-01.md`
- `.loom/evidence/20260503-readme-route-table-framing-validation.md`
- `.loom/critique/readme-route-table-framing-review.md`

Targeted observations:

- `README.md:259` says to use the table as introductory orientation, not the
  complete route vocabulary.
- `README.md:260-261` says canonical route tokens and saved-field route grammar
  are owned by `skills/loom-records/references/route-vocabulary.md`.
- `README.md:263-273` preserves the existing `Situation | Loom route` table and
  route entries.
- The README change adds three concise lines of product-facing prose and does not
  duplicate the full route vocabulary.
- `git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-030`
- `ticket:readrte29#ACC-001`
- `ticket:readrte29#ACC-002`
- `ticket:readrte29#ACC-003`
- `ticket:readrte29#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `3434531b3006f53b486344b925ed7e0ed54c290e` plus uncommitted scoped
`ticket:readrte29` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no route-token change, route grammar change, runtime, command
wrapper, schema, or new owner layer changed in the scoped diff.

# Validity

Valid for: the scoped `ticket:readrte29` diff at 2026-05-03T08:51:36Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It validates README framing only;
complete route vocabulary remains in the owning reference, and mandatory critique
remains a separate gate.

# Result

README now frames the route table as introductory and points to
`skills/loom-records/references/route-vocabulary.md` for canonical route tokens
and saved-field route grammar. The scoped diff passes `git diff --check`.

# Interpretation

The evidence supports the README route-table framing claims. It does not close
the ticket; mandatory critique and ticket-owned acceptance remain separate gates.

# Related Records

- `ticket:readrte29`
- `packet:ralph-ticket-readrte29-20260503T085013Z`
- `critique:readme-route-table-framing-review`
