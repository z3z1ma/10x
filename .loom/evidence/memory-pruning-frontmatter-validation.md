---
id: evidence:memory-pruning-frontmatter-validation
kind: evidence
status: recorded
created_at: 2026-05-02T10:47:36Z
updated_at: 2026-05-02T10:51:28Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  tickets:
    - ticket:795fa0f4
  packets:
    - packet:ralph-ticket-795fa0f4-20260502T104301Z
  critique:
    - critique:memory-pruning-frontmatter-review
  plan:
    - plan:skills-corpus-protocol-sharpening
external_refs: {}
---

# Summary

Structural validation for memory pruning, promotion, optionality, and
frontmatter/status guidance added under `ticket:795fa0f4`.

# Procedure

The parent reviewed the Ralph child output, made one alignment refinement so
`loom-memory` names the same validator-exempt metadata as `loom-records`,
reconciled packet and ticket state to review, recorded final critique, closed the
ticket, and ran targeted structural checks on the resulting diff.

Commands and searches performed:

```text
git diff --check
git diff --stat
git diff --stat -- "skills/loom-memory/SKILL.md" "skills/loom-memory/references/memory-model.md" "skills/loom-memory/references/housekeeping.md" "skills/loom-records/references/frontmatter.md" "skills/loom-records/references/status-lifecycle.md" "skills/loom-retrospective/SKILL.md"
rg -n "leave alone|link.*owner|mark.*stale|promote|prune|ticket closure|retrospective|housekeeping|renamed|superseded" "skills/loom-memory" "skills/loom-retrospective/SKILL.md"
rg -n "L0|frontmatter|YAML|status|Validators must not require canonical|canonical frontmatter|support-only retrieval metadata|memory support files" "skills/loom-memory/SKILL.md" "skills/loom-records/references/frontmatter.md" "skills/loom-records/references/status-lifecycle.md"
rg -n "optional.*correctness|absent|stale|pruned|not useless|live execution ledger|evidence remains|research remains|wiki remains|ticket substitute|canonical truth" "skills/loom-memory"
rg -ni "indexing|embedding|database|script|runtime|state machine" "skills/loom-memory" "skills/loom-records/references/frontmatter.md" "skills/loom-records/references/status-lifecycle.md" "skills/loom-retrospective/SKILL.md"
```

# Artifacts

Observed product files changed:

- `skills/loom-memory/SKILL.md`
- `skills/loom-memory/references/memory-model.md`
- `skills/loom-memory/references/housekeeping.md`
- `skills/loom-records/references/frontmatter.md`
- `skills/loom-records/references/status-lifecycle.md`
- `skills/loom-retrospective/SKILL.md`

Observed outputs:

```text
git diff --check
-> no output

git diff --stat
-> 7 files changed, 112 insertions(+), 24 deletions(-)

git diff --stat -- <changed product files>
-> 6 files changed, 72 insertions(+), 3 deletions(-)

rg pruning / promotion / stale handling
-> found leave-alone, owner-link, stale, promote, prune, ticket closure,
   retrospective, housekeeping, rename, and supersession guidance

rg frontmatter / status expectations
-> found L0 header guidance, optional YAML/frontmatter wording, optional local
   support metadata, validator exception, and memory support status guidance

rg memory optionality and boundaries
-> found optionality as correctness boundary, absent/stale/pruned memory wording,
   live execution ledger boundary, evidence/research/wiki owner boundaries, and
   canonical-truth promotion rule

rg no-runtime terms
-> found only existing Markdown/runtime/status-lifecycle wording; no memory
   indexing, embedding, database, script, runtime, or state-machine requirement
   was introduced
```

# Supports Claims

- `ticket:795fa0f4` ACC-001
- `ticket:795fa0f4` ACC-002
- `ticket:795fa0f4` ACC-003
- `ticket:795fa0f4` ACC-004
- `ticket:795fa0f4` ACC-005
- `initiative:skills-corpus-protocol-sharpening#OBJ-003`
- `research:skills-corpus-council-review#CLAIM-007`

# Challenges Claims

None observed.

# Environment

Commit: `7e0b268868557542c9b7e937f0dbd2b8b93fa353` plus the current working-tree
diff for `ticket:795fa0f4` before commit.

Branch: `main`

Runtime: OpenCode parent session with Ralph fixer subagent and oracle critique
subagent.

OS: darwin

Relevant config: repository has no automated test suite; validation is structural
and manual per `AGENTS.md`.

# Validity

Valid for: the working tree after `packet:ralph-ticket-795fa0f4-20260502T104301Z`,
parent reconciliation to review, final critique, and ticket closure.

Recheck when: memory support-file structure, pruning, promotion, optionality,
frontmatter, status, or retrospective housekeeping guidance changes.

# Limitations

This evidence validates structural presence and consistency of memory guidance.
It does not validate historical `.loom/memory` files and does not replace oracle
critique.

# Result

Memory guidance now explains leave/link/stale/promote/prune decisions, ties
cleanup to existing workflows, preserves lightweight L0/default-frontmatter
exceptions, keeps optionality as a correctness boundary, and prevents memory from
becoming a live ledger, evidence store, research log, wiki, or ticket substitute.

# Interpretation

The observations support acceptance of `ticket:795fa0f4` only when combined with
critique and ticket-owned acceptance. Evidence does not itself close the ticket.

# Related Records

- `ticket:795fa0f4`
- `packet:ralph-ticket-795fa0f4-20260502T104301Z`
- `critique:memory-pruning-frontmatter-review`
- `plan:skills-corpus-protocol-sharpening`
