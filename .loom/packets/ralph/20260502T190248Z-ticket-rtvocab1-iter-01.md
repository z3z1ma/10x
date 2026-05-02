---
id: packet:ralph-ticket-rtvocab1-20260502T190248Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:rtvocab1
mode: execution
change_class: protocol-authority
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T19:02:48Z
updated_at: 2026-05-02T19:13:21Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:rtvocab1
    - evidence:route-vocabulary-validation
    - packet:ralph-ticket-rtvocab1-20260502T190248Z
  paths:
    - skills/loom-records/**
    - skills/loom-drive/**
    - skills/loom-tickets/**
    - skills/loom-workspace/**
    - .loom/tickets/20260502-rtvocab1-normalize-route-vocabulary.md
    - .loom/evidence/20260502-route-vocabulary-validation.md
    - .loom/packets/ralph/20260502T190248Z-ticket-rtvocab1-iter-01.md
parent_merge_scope:
  records:
    - ticket:rtvocab1
    - evidence:route-vocabulary-validation
    - packet:ralph-ticket-rtvocab1-20260502T190248Z
  paths:
    - .loom/critique/route-vocabulary-review.md
source_fingerprint:
  git_commit: 86b74e39009eb4eeec4722bec9799f4bbc12705b
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 86b74e39009eb4eeec4722bec9799f4bbc12705b
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-council-precision-pass
    - plan:skills-corpus-council-precision-pass
    - ticket:rtvocab1
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: normal
  max_source_files: 14
  max_excerpt_lines_per_file: 120
  avoid_full_file_reads: true
sources:
  constitution:
    - constitution:main
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:rtvocab1
  references:
    - skills/loom-records/references/query-and-linking.md
    - skills/loom-records/references/semantic-link-usage.md
    - skills/loom-drive/references/checkpoint-resume-protocol.md
    - skills/loom-drive/references/continuity-contract.md
    - skills/loom-workspace/references/status-snapshot.md
    - skills/loom-tickets/templates/ticket.md
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:rtvocab1
  critique:
    - critique:route-vocabulary-review
---

# Mission

Normalize Loom's route vocabulary so next-route/checkpoint/resume guidance uses
one canonical, grep-friendly grammar across drive, tickets, workspace, and route
templates without creating a command router or runtime enum dependency.

# Bound Context

This is the first ticket in `plan:skills-corpus-council-precision-pass` and
covers `initiative:skills-corpus-council-precision-pass#OBJ-001`.

The user delegated sequential execution: Ralph with a fixer child, parent
reconciliation, oracle critique, retrospective disposition, semantic commit, and
push before moving to the next ticket.

# Source Snapshot

Council finding `CR-001` observed route token drift across drive/checkpoint,
ticket readiness, workspace status, and examples. Examples include `ask_user`,
`ask-user`, `ask user`, `Ralph`, `acceptance`, `acceptance_review`, and
`continue` being used inconsistently as route-like tokens.

The ticket requires a shared owner for route vocabulary, downstream alignment, and
explicit separation from ticket lifecycle statuses, command names, and adapter
invocation surfaces.

# Change Class

Declared as `protocol-authority`. This changes operator guidance and routing
semantics, so use observation-first structural validation and expect oracle
critique before closure.

# Verification Targets

- `initiative:skills-corpus-council-precision-pass#OBJ-001`
- `ticket:rtvocab1#ACC-001`
- `ticket:rtvocab1#ACC-002`
- `ticket:rtvocab1#ACC-003`
- `ticket:rtvocab1#ACC-004`

# Task For This Iteration

1. Capture before-state targeted searches for route-like tokens and route-bearing
   sections in the child write scope.
2. Add or update a shared route-vocabulary section/reference in the smallest
   appropriate owner surface, likely `skills/loom-records`.
3. Align direct downstream examples and route sections in `loom-drive`,
   `loom-tickets`, `loom-workspace`, and affected templates.
4. Keep route vocabulary distinct from ticket lifecycle states, command names, and
   adapter invocation surfaces.
5. Create `.loom/evidence/20260502-route-vocabulary-validation.md` with before/after
   observations and `git diff --check`.
6. Update `ticket:rtvocab1` with evidence link, claim matrix support, and a
   recommendation for mandatory oracle critique. Do not close it.

# Verification Posture

`observation-first`.

Before edits, record route-token search observations. After edits, record
targeted searches showing the route vocabulary is centralized/aligned or that any
remaining terms are ordinary prose rather than active route tokens. Run
`git diff --check`.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- route normalization requires new product direction beyond the council finding;
- the fix would add a runtime, command router, hidden validator, or new owner
  layer;
- a route token cannot be normalized without changing ticket state-machine
  semantics;
- the working tree or source fingerprint no longer matches the packet closely
  enough to trust it;
- the change would widen beyond route vocabulary into unrelated style cleanup.

# Output Contract

Return:

- outcome (`continue|stop|blocked|escalate`);
- files changed;
- records changed;
- before/after observations for route-token drift;
- exact validation commands/results, including `git diff --check`;
- self-review findings or concerns;
- blockers or residual risks;
- ticket recommendation, including whether oracle critique is next.

# Working Notes

Parent compiled from clean `main` at `86b74e39009eb4eeec4722bec9799f4bbc12705b`.

# Child Output

Outcome: `stop` — bounded route-vocabulary normalization slice completed and the
ticket is ready for mandatory oracle critique, not closure.

Files changed:

- `skills/loom-records/references/route-vocabulary.md` — added shared route-token
  owner reference.
- `skills/loom-records/SKILL.md` — linked route-vocabulary ownership/read order.
- `skills/loom-drive/SKILL.md` — aligned route examples/read order.
- `skills/loom-drive/references/checkpoint-resume-protocol.md` — normalized
  checkpoint route list and route-federation examples.
- `skills/loom-drive/references/continuity-contract.md` — normalized resume and
  reassessment `next route:` values and separated statuses from route values.
- `skills/loom-drive/references/drive-loop.md` — normalized drive state/route
  examples and linked route vocabulary.
- `skills/loom-drive/references/tranche-decision-protocol.md` — normalized route
  priority table values.
- `skills/loom-drive/templates/outer-loop-handoff.md` — normalized proposed route
  output list.
- `skills/loom-tickets/templates/ticket.md` — normalized ticket route template.
- `skills/loom-tickets/references/readiness.md` — normalized readiness route
  examples and status separation.
- `skills/loom-workspace/references/routing.md` — linked shared route grammar.
- `skills/loom-workspace/references/status-snapshot.md` — added route-token drift
  signal and grammar pointer.
- `.loom/evidence/20260502-route-vocabulary-validation.md` — recorded before/after
  observations and validation.
- `.loom/tickets/20260502-rtvocab1-normalize-route-vocabulary.md` — moved to
  `review_required`, linked evidence, and updated claim support.
- `.loom/packets/ralph/20260502T190248Z-ticket-rtvocab1-iter-01.md` — recorded
  child output.

Records changed:

- `ticket:rtvocab1`
- `evidence:route-vocabulary-validation`
- `packet:ralph-ticket-rtvocab1-20260502T190248Z`

Before observations:

- Parent launch had already modified `ticket:rtvocab1` and created this packet;
  `HEAD` still matched source fingerprint
  `86b74e39009eb4eeec4722bec9799f4bbc12705b`.
- Before-state search found route-value drift: `ask_user`, `ask-user`, `ask user`,
  title-case `Ralph`, phrase-style `local edit` / `ticket acceptance review`, and
  `acceptance / stop` route-table wording across drive, tickets, and templates.

After observations:

- `skills/loom-records/references/route-vocabulary.md` now owns lowercase
  `snake_case` route tokens for route-bearing fields.
- Direct route examples in drive/ticket/workspace surfaces now point to or use the
  shared route vocabulary.
- Remaining search hits for `Ralph`, `acceptance`, `review_required`, and
  `complete_pending_acceptance` are ordinary prose, packet-frontmatter guidance,
  route-vocabulary definitions, or ticket lifecycle status examples rather than
  active route-value examples.

Validation commands/results:

- `rg -n '(next route|next_route|next-route|ask_user|ask-user|ask user|acceptance_review|acceptance review|Ralph|acceptance \||\| acceptance|continue \||ask user)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'` — before search captured route-token drift summarized above.
- `rg -n '(next route:|Route:|proposed next route:|Route Decision Priority|route-vocabulary)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'` — after search showed canonical route fields/lists and route-vocabulary links.
- `rg -n '(ask-user|ask user|workspace/records repair|acceptance / stop|Ralph implementation packet|ticket acceptance review|local edit \||Ralph \||acceptance \|)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'` — remaining matches were not active route-value examples.
- `rg -n '(review_required|complete_pending_acceptance|acceptance_review|ask_user|local_edit|ralph)' 'skills/loom-records/references/route-vocabulary.md' 'skills/loom-tickets/references/readiness.md' 'skills/loom-workspace/references/status-snapshot.md' --glob '*.md'` — confirmed explicit separation of ticket statuses from route tokens.
- `git diff --check` — passed with no output.

Self-review concerns:

- The canonical token set is intentionally broad enough for existing drive/ticket
  examples. Oracle critique should confirm it is not over-broad or missing a
  route future tickets rely on.
- Long inline route lists remain in code blocks/templates for grepability; critique
  should judge whether readability is acceptable.

Blockers/risks:

- No implementation blocker encountered.
- Residual risk: high-risk protocol-authority change still needs mandatory oracle
  critique before acceptance or closure.

Ticket recommendation:

- Keep `ticket:rtvocab1` in `review_required`.
- Next route: `critique` with profiles `protocol-change`, `operator-clarity`, and
  `routing-safety`.
- Do not close until `ticket:rtvocab1#ACC-005` is satisfied and any critique
  findings are ticket-dispositioned.

# Parent Merge Notes

Parent accepted the child route-vocabulary implementation as inside scope and
structurally validated by `evidence:route-vocabulary-validation`.

Oracle critique `critique:route-vocabulary-review` found one packet lifecycle
reconciliation issue: this packet still looked `compiled` after child output had
returned. Parent resolved that issue by marking the packet `consumed` and adding
these merge notes. Ticket acceptance remains ticket-owned.
