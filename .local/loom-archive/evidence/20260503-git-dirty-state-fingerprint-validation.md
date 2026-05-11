---
id: evidence:git-dirty-state-fingerprint-validation
kind: evidence
status: recorded
created_at: 2026-05-03T07:54:00Z
updated_at: 2026-05-03T08:02:37Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:gitstat26
  packet:
    - packet:ralph-ticket-gitstat26-20260503T075047Z
  critique:
    - critique:git-dirty-state-fingerprint-review
    - critique:git-dirty-state-fingerprint-rereview
external_refs: {}
---

# Summary

Validation observations for `ticket:gitstat26`, checking that packet source
fingerprints expose dirty Git state through machine-readable categories while
preserving human-readable status detail.

# Procedure

- Inspected the scoped product diff for `ticket:gitstat26`.
- Searched packet frontmatter guidance, Ralph packet contract, and packet-family
  templates for `dirty_tracked`, `dirty_untracked`, `dirty_mixed`,
  `git_status_summary`, and `git_status_detail`.
- Searched `skills/**/*.md` for the old literal `clean|dirty|unknown` packet
  summary grammar.
- Parent-side validation uses `git add -N` for newly created scoped records before
  the final `git diff --check` so new records are included in the whitespace
  check. This happens during parent reconciliation/validation, not during child
  execution; the child did not mutate Git metadata.
- Ran `git diff --check`.

# Artifacts

Scoped changed tracked files:

- `.loom/tickets/20260503-gitstat26-add-machine-readable-dirty-state.md`
- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`

Scoped new Loom record files:

- `.loom/packets/ralph/20260503T075047Z-ticket-gitstat26-iter-01.md`
- `.loom/evidence/20260503-git-dirty-state-fingerprint-validation.md`
- `.loom/critique/git-dirty-state-fingerprint-review.md`
- `.loom/critique/git-dirty-state-fingerprint-rereview.md`

Targeted observations:

- `skills/loom-records/references/packet-frontmatter.md:51` and
  `skills/loom-records/references/packet-frontmatter.md:366` now use
  `git_status_summary: <clean|dirty_tracked|dirty_untracked|dirty_mixed|unknown>`.
- `skills/loom-records/references/packet-frontmatter.md:373-379` defines `clean`,
  `dirty_tracked`, `dirty_untracked`, `dirty_mixed`, and `unknown`, and keeps
  `git_status_detail` for human-readable status details or `unknown - <rationale>`.
- `skills/loom-ralph/references/packet-contract.md:105` now uses the same
  machine-readable summary grammar, and lines `112-118` preserve
  `git_status_detail` for human-readable details and rationale.
- `skills/loom-ralph/templates/ralph-packet.md:35`,
  `skills/loom-critique/templates/critique-packet.md:43`, and
  `skills/loom-wiki/templates/wiki-packet.md:33` now use the revised summary
  grammar.
- Search for `dirty_tracked|dirty_untracked|dirty_mixed|git_status_summary|git_status_detail`
  returned the expected packet guidance and template hits in `skills/`.
- Search for the old literal `clean|dirty|unknown` summary grammar in `skills/`
  returned no files.
- `git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027`
- `ticket:gitstat26#ACC-001`
- `ticket:gitstat26#ACC-002`
- `ticket:gitstat26#ACC-003`
- `ticket:gitstat26#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `110728f57e570bc047b828e0d5158bf641fb9c87` plus uncommitted scoped
`ticket:gitstat26` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no generated files, lockfiles, Git helper runtime, schema engine,
validator, command wrapper, or new owner layer observed in the scoped diff.

# Validity

Valid for: the scoped `ticket:gitstat26` diff at 2026-05-03T08:02:37Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It validates authored packet fingerprint
guidance; actual launch safety still depends on parents recording and comparing
packet source fingerprints truthfully.

# Result

Packet source fingerprint guidance now distinguishes tracked-only,
untracked-only, and mixed dirty worktree states in `git_status_summary`, while
preserving `clean`, `unknown`, and `git_status_detail` for human context and
rationale. The scoped diff passes `git diff --check`.

# Interpretation

The evidence supports the dirty-state fingerprint claims. It does not close the
ticket; mandatory critique and the ticket-owned acceptance decision remain
separate gates.

# Related Records

- `ticket:gitstat26`
- `packet:ralph-ticket-gitstat26-20260503T075047Z`
