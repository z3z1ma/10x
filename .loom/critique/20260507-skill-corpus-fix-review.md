---
id: critique:skill-corpus-fix-review
kind: critique
status: final
created_at: 2026-05-07T18:44:25Z
updated_at: 2026-05-07T18:45:01Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:pkt7z924 and current diff under skills/"
links:
  ticket:
    - ticket:pkt7z924
  evidence:
    - evidence:skill-corpus-fix-structural-checks
external_refs: {}
---

# Summary

Adversarial review of the skill-corpus consistency fixes for `ticket:pkt7z924`.
The review used two oracle passes plus local structural evidence. All valid oracle
findings were addressed in the diff or ticket records before this critique was
finalized.

# Review Target

The target is the uncommitted diff for `ticket:pkt7z924`, focused on changed
`skills/` files and the ticket/evidence/critique records that make the work
recoverable.

# Verdict

`pass_with_findings` — the oracle review found real issues in the first and
second passes, and those findings have been addressed. No critique blockers remain
for ticket acceptance if the ticket records the finding dispositions and cites the
structural evidence.

# Findings

## FIND-001: Status lifecycle transition guard was incomplete

Severity: medium
Confidence: high
State: open

Observation:

The first oracle review found that the status lifecycle clarification only guarded
target statuses, while generic transitions could still imply invalid source
statuses for some record kinds.

Why it matters:

Status lifecycle guidance is shared protocol grammar. Ambiguous source/target
validity can lead future agents to write statuses that the owning kind does not
support.

Follow-up:

Resolved in `skills/loom-records/references/status-lifecycle.md` by requiring both
source and target statuses to be valid for the record kind.

Challenges:

- ticket:pkt7z924#ACC-001

## FIND-002: Spike write-scope wording was overbroad

Severity: medium
Confidence: high
State: open

Observation:

The oracle found that spike guidance could treat ordinary Loom record updates as
write-bearing prototype mutations requiring ticket/Ralph. The second oracle pass
found the read-order wording still carried that problem.

Why it matters:

Spike work should not force ticket/Ralph ceremony for normal research, evidence,
spec, or wiki records. The stricter branch is for throwaway code and non-record
repository mutations.

Follow-up:

Resolved in `skills/loom-spike/SKILL.md` by narrowing the main flow, verification,
Done Means, and read-order text to throwaway code, source-file changes, generated
prototype artifacts, or other non-record repository mutations.

Challenges:

- ticket:pkt7z924#ACC-001

## FIND-003: Ticket acceptance lacked a durable finding list

Severity: medium
Confidence: high
State: open

Observation:

The first oracle review found that `ticket:pkt7z924#ACC-001` referred to “every
finding” without listing or linking those findings in the filesystem graph.

Why it matters:

A future agent should not need transcript context to know what the ticket promised
to fix.

Follow-up:

Resolved by adding a `# Finding Disposition` table to the ticket that lists the
original review findings and oracle findings with dispositions.

Challenges:

- ticket:pkt7z924#ACC-001

## FIND-004: Ticket-owned evidence disposition grammar was fragmented

Severity: medium
Confidence: medium
State: open

Observation:

The oracle found that the ticket template and acceptance gate were aligned, but
`status-lifecycle.md` did not define ticket-owned evidence disposition values and
ticket skill prose used “not required” rather than the exact `not_required` token.

Why it matters:

Evidence disposition is part of ticket acceptance grammar. Fragmented vocabulary
invites drift between template, acceptance gate, and shared lifecycle docs.

Follow-up:

Resolved in `skills/loom-records/references/status-lifecycle.md` and
`skills/loom-tickets/SKILL.md`.

Challenges:

- ticket:pkt7z924#ACC-001

## FIND-005: Critique packet parent merge grammar was ambiguous

Severity: low
Confidence: medium
State: open

Observation:

The first oracle review found that the critique packet template allowed
`parent_merge_scope.records` to use `None` for the critique record while the body
said the parent creates or updates real critique and ticket records.

Why it matters:

Packetized critique should make the durable review target explicit. Mandatory
critique cannot be satisfied by output-only chat.

Follow-up:

Resolved in `skills/loom-critique/templates/critique-packet.md` by requiring a
`critique:<slug>` parent merge target and making ticket reconciliation optional
only when no ticket owns execution.

Challenges:

- ticket:pkt7z924#ACC-001
- ticket:pkt7z924#ACC-003

## FIND-006: Mandatory critique needed a final critique record

Severity: medium
Confidence: medium
State: open

Observation:

The second oracle pass found that the ticket could still satisfy mandatory critique
with chat-only oracle output rather than a final critique record.

Why it matters:

Loom's mandatory critique gate requires a final critique record with verdict,
evidence reviewed, residual risks, and acceptance recommendation.

Follow-up:

Resolved by rewriting `ticket:pkt7z924#ACC-003` to require a final critique record
and by creating this record.

Challenges:

- ticket:pkt7z924#ACC-003

## FIND-007: Ticket lacked dependencies and journal sections

Severity: low
Confidence: high
State: open

Observation:

The second oracle pass found that the ticket omitted standard `# Dependencies` and
`# Journal` sections.

Why it matters:

For an active protocol-authority ticket, a journal improves live execution
recovery and makes the ticket a better ledger.

Follow-up:

Resolved by adding dependencies and journal sections to the ticket.

Challenges:

- ticket:pkt7z924#ACC-003

# Evidence Reviewed

- Oracle adversarial review pass 1 against the initial fix diff: found five valid
  issues, all addressed.
- Oracle adversarial review pass 2 after those fixes: found three valid remaining
  issues, all addressed.
- `evidence:skill-corpus-fix-structural-checks`, including whitespace diff check,
  frontmatter parse check, `change_class` list parity, targeted contradiction
  searches, and evidence disposition vocabulary search.
- Final scoped whitespace and frontmatter parse checks after creating this critique
  record.
- Current diff under `skills/` and `.loom/` for the ticket, evidence, and critique
  records.

# Residual Risks

- The repository has no automated test suite for skill semantics; validation is
  structural plus adversarial review.
- The edits are Markdown protocol guidance, so future operator behavior is not
  mechanically guaranteed by these checks.
- Existing unrelated untracked `examples/00-todo-app` files were intentionally not
  reviewed or modified by this ticket.

# Required Follow-up

None before ticket acceptance. If any of the edited `skills/` or ticket records
change again, rerun the relevant structural checks and reconsider critique.

# Acceptance Recommendation

`no-critique-blockers` — all valid oracle findings have been fixed or have a
ticket-owned resolved disposition. The ticket acceptance gate can decide closure
after linking this critique and the structural evidence.
