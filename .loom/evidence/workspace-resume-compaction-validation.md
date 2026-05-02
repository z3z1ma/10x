---
id: evidence:workspace-resume-compaction-validation
kind: evidence
status: recorded
created_at: 2026-05-02T10:19:55Z
updated_at: 2026-05-02T10:27:56Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  tickets:
    - ticket:1a12d9ff
  packets:
    - packet:ralph-ticket-1a12d9ff-20260502T101425Z
  critique:
    - critique:workspace-resume-compaction-review
  plan:
    - plan:skills-corpus-protocol-sharpening
external_refs: {}
---

# Summary

Structural validation for workspace cold-start, post-compaction, and
pre-compaction recovery guidance added under `ticket:1a12d9ff`.

# Procedure

The parent reviewed the Ralph child output, manually inspected the workspace
skill diff, made a small wording refinement so active-ticket discovery is named
explicitly, reconciled the packet/ticket after initial oracle feedback, recorded
final critique, closed the ticket, and ran targeted structural checks on the
resulting diff.

Commands and searches performed:

```text
git diff --check
git diff --stat
git diff --stat -- skills/loom-workspace/SKILL.md skills/loom-workspace/references/status-snapshot.md
rg recovery-route terms in skills/loom-workspace
rg bootstrap/constitution ordering in workspace entry guidance
rg active-ticket and live-state discovery guidance
rg chat/transcript/generated-context shadow-truth rejection guidance
rg owner-update and loom-drive boundary guidance
```

# Artifacts

Observed product files changed:

- `skills/loom-workspace/SKILL.md`
- `skills/loom-workspace/references/status-snapshot.md`

Observed outputs:

```text
git diff --check
-> no output

git diff --stat
-> 3 files changed, 127 insertions(+), 32 deletions(-)

git diff --stat -- skills/loom-workspace/SKILL.md skills/loom-workspace/references/status-snapshot.md
-> 2 files changed, 82 insertions(+), 10 deletions(-)

rg -n "Cold-Start And Post-Compaction Resume Route|cold-start|post-compaction|pre-compaction" "skills/loom-workspace"
-> found cold-start/post-compaction ownership in SKILL.md and the explicit resume route in status-snapshot.md

rg -n "loom-bootstrap|constitution:main" "skills/loom-workspace/SKILL.md" "skills/loom-workspace/references/status-snapshot.md"
-> found bootstrap doctrine before `constitution:main`, and `constitution:main` before downstream resume steps

rg -n "active ticket|live status|status: \\(active\\|blocked\\|review_required\\|complete_pending_acceptance\\)" "skills/loom-workspace"
-> found active-ticket/live-state wording and the ticket status discovery query

rg -n "chat history|transcript memory|generated context|canonical resume truth|separate resume ledger|canonical memory dependency" "skills/loom-workspace"
-> found rejection of chat history, transcript memory, generated context files, separate resume ledgers, and canonical memory dependency

rg -n "ticket: live status|evidence: observed|critique: adversarial|wiki: accepted|memory: optional|loom-drive" "skills/loom-workspace/references/status-snapshot.md"
-> found pre-compaction owner updates and `loom-drive` as high-level coordinator rather than the only resume route
```

# Supports Claims

- `ticket:1a12d9ff` ACC-001
- `ticket:1a12d9ff` ACC-002
- `ticket:1a12d9ff` ACC-003
- `ticket:1a12d9ff` ACC-004
- `ticket:1a12d9ff` ACC-005
- `ticket:1a12d9ff` ACC-006
- `initiative:skills-corpus-protocol-sharpening#OBJ-003`
- `research:skills-corpus-council-review#CLAIM-004`
- `research:skills-corpus-council-review#CLAIM-007`
- `research:skills-corpus-council-review#CLAIM-009`

# Challenges Claims

None observed.

# Environment

Commit: `6524e42835a3db05065f62e5919298abfad159af` plus the current working-tree
diff for `ticket:1a12d9ff` before commit.

Branch: `main`

Runtime: OpenCode parent session with Ralph fixer subagent and oracle critique
subagent.

OS: darwin

Relevant config: repository has no automated test suite; validation is structural
and manual per `AGENTS.md`.

# Validity

Valid for: the working tree after `packet:ralph-ticket-1a12d9ff-20260502T101425Z`,
parent wording refinement, oracle-driven record reconciliation, final critique,
and ticket closure.

Recheck when: workspace entry, status snapshot, bootstrap-first routing,
ticket-ledger ownership, drive resume boundaries, or memory optionality guidance
changes.

# Limitations

This evidence validates structural presence and consistency of the workspace
recovery route. It does not prove operator behavior in a real cold session, and
it does not replace mandatory critique for this high-risk protocol-authority
change.

# Result

Workspace entry now teaches a concrete cold-start and post-compaction recovery
route, active-ticket discovery, owner-chain follow-through, pre-compaction owner
updates, rejection of chat/transcript/generated-context shadow truth, memory as
support-only recall, and `loom-drive` as a high-level coordinator rather than the
only resume route.

# Interpretation

The observations support acceptance of `ticket:1a12d9ff` only when combined with
mandatory critique and ticket-owned acceptance. Evidence does not itself close
the ticket.

# Related Records

- `ticket:1a12d9ff`
- `packet:ralph-ticket-1a12d9ff-20260502T101425Z`
- `critique:workspace-resume-compaction-review`
- `plan:skills-corpus-protocol-sharpening`
