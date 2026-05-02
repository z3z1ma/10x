---
id: evidence:packet-frontmatter-grammar-validation
kind: evidence
status: recorded
created_at: 2026-05-02T16:00:07Z
updated_at: 2026-05-02T16:14:35Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:4ilnwsnl
  packet:
    - packet:ralph-ticket-4ilnwsnl-20260502T155908Z
  critique:
    - critique:packet-frontmatter-grammar-review
external_refs: {}
---

# Summary

Structural validation for the shared packet-frontmatter grammar pass. The checks
support `ticket:4ilnwsnl` acceptance criteria for creating a shared grammar,
aligning Ralph/critique/wiki packet templates, preserving packet-family
boundaries, and running `git diff --check`.

# Procedure

1. Read the Ralph packet and bounded write-scope files.
2. Added `skills/loom-records/references/packet-frontmatter.md` as the shared
   packet frontmatter grammar.
3. Updated `loom-records` routing, Ralph packet-contract guidance, and packet
   templates for Ralph, critique, and wiki.
4. Ran `git diff --check`; because the new grammar and evidence files were
   untracked, also ran `git diff --check --no-index` against those new files.
5. Ran targeted searches for packet frontmatter fields and packet template
   frontmatter.
6. Manually compared the Ralph, critique, and wiki packet template frontmatter
   against the shared grammar.

# Artifacts

## `git diff --check`

Command:

```bash
git diff --check
```

Output:

```text
<no output>
```

Result: no whitespace errors were reported in the current diff.

Additional new-file whitespace checks:

```bash
git diff --check --no-index -- /dev/null "skills/loom-records/references/packet-frontmatter.md"
git diff --check --no-index -- /dev/null ".loom/evidence/packet-frontmatter-grammar-validation.md"
```

Output:

```text
<no output>
```

Result: no whitespace errors were reported for the two new files created by this
Ralph child iteration.

## Targeted field search

Search pattern:

```text
packet_kind|child_write_scope|parent_merge_scope|source_fingerprint|execution_context|context_budget|verification_posture|mode:|style:
```

Search scope: `skills/**/*.md`.

Observed relevant matches:

- `skills/loom-records/references/packet-frontmatter.md` defines the shared
  packet field set and valid values for `packet_kind`, `mode`, `style`,
  `child_write_scope`, `parent_merge_scope`, `source_fingerprint`,
  `execution_context`, `context_budget`, and Ralph-only
  `verification_posture`.
- `skills/loom-records/references/frontmatter.md` routes packet frontmatter to
  `references/packet-frontmatter.md`.
- `skills/loom-ralph/references/packet-contract.md` cites the shared grammar and
  keeps Ralph-specific packet contract guidance.
- `skills/loom-ralph/templates/ralph-packet.md` contains `packet_kind: ralph`,
  `mode: execution`, `style`, `verification_posture`, `child_write_scope`,
  `parent_merge_scope`, `source_fingerprint`, `execution_context`, and
  `context_budget`.
- `skills/loom-critique/templates/critique-packet.md` contains
  `packet_kind: critique`, `mode: review`, `style`, `child_write_scope`,
  `parent_merge_scope`, `source_fingerprint`, `execution_context`, and
  `context_budget`; it intentionally omits Ralph `verification_posture`.
- `skills/loom-wiki/templates/wiki-packet.md` contains `packet_kind: wiki`,
  `mode: synthesis`, `style`, `child_write_scope`, `parent_merge_scope`,
  `source_fingerprint`, `execution_context`, and `context_budget`; it
  intentionally omits Ralph `verification_posture`.

## Packet template frontmatter search

Search pattern:

```text
^---$|^id: packet:|^kind: packet|^packet_kind:|^mode:|^style:|^verification_posture:|^child_write_scope:|^parent_merge_scope:|^source_fingerprint:|^execution_context:|^context_budget:
```

Search scope: `skills/**/*packet.md`.

Observed packet template frontmatter:

- `skills/loom-ralph/templates/ralph-packet.md` has frontmatter fences at lines
  1 and 56, with the shared packet fields plus Ralph-specific `change_class`,
  `verification_posture`, `iteration`, and typed `sources` defaults.
- `skills/loom-critique/templates/critique-packet.md` has frontmatter fences at
  lines 1 and 48, with the shared packet fields plus critique-specific
  `review_target` and `change_class`.
- `skills/loom-wiki/templates/wiki-packet.md` has frontmatter fences at lines 1
  and 45, with the shared packet fields and wiki-owned synthesis posture.

# Supports Claims

- `ticket:4ilnwsnl#ACC-001`
- `ticket:4ilnwsnl#ACC-002`
- `ticket:4ilnwsnl#ACC-003`
- `ticket:4ilnwsnl#ACC-004`
- `initiative:skills-corpus-perfection-council-followup#OBJ-002`

# Challenges Claims

None observed.

# Environment

Commit: `330a7b2d59c284e55b2fdbbd1e4649026cb253cf`
Branch: `main`
Runtime: Markdown structural edits; no runtime validator or test suite.
OS: macOS / Darwin
Relevant config: packet `source_fingerprint.git_status_summary` was compiled as
clean; validation was run against the working tree after the Ralph child edits.

# Validity

Valid for: the working-tree packet-frontmatter grammar and template state after
the Ralph child implementation on 2026-05-02T16:04:48Z.

Recheck when: any packet template, `skills/loom-records/references/frontmatter.md`,
`skills/loom-records/references/packet-frontmatter.md`, or
`skills/loom-ralph/references/packet-contract.md` changes.

# Limitations

- This is structural evidence, not automated YAML schema validation.
- The targeted searches confirm field presence and routing text; they do not
  prove every future packet instance will fill placeholders correctly.
- Manual comparison checked Ralph/critique/wiki packet templates against the new
  shared grammar but did not inspect every historical packet under `.loom/packets`.
- Oracle critique is recorded separately in
  `critique:packet-frontmatter-grammar-review`.

# Result

The shared grammar exists in `loom-records`; `frontmatter.md` and
`loom-records/SKILL.md` route packet questions to it; Ralph packet-contract
guidance cites it; Ralph, critique, and wiki packet templates carry the shared
packet fields and valid packet-family values while preserving critique/wiki
workflow ownership.

# Interpretation

The evidence supported moving `ticket:4ilnwsnl` to `review_required` for mandatory
oracle critique. Together with `critique:packet-frontmatter-grammar-review`, it
now supports ticket closure.

# Related Records

- `ticket:4ilnwsnl`
- `packet:ralph-ticket-4ilnwsnl-20260502T155908Z`
- `critique:packet-frontmatter-grammar-review`
- `initiative:skills-corpus-perfection-council-followup#OBJ-002`
