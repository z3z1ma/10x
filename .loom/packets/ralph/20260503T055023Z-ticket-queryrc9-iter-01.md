---
id: packet:ralph-ticket-queryrc9-20260503T055023Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:queryrc9
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T05:50:23Z
updated_at: 2026-05-03T05:54:03Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-records/references/query-and-linking.md
    - skills/loom-records/SKILL.md
    - skills/loom-bootstrap/references/06-filesystem-and-tooling.md
parent_merge_scope:
  records:
    - ticket:queryrc9
  paths:
    - .loom/tickets/20260503-queryrc9-consolidate-query-recipes.md
    - .loom/evidence/20260503-query-recipe-validation.md
    - .loom/critique/query-recipe-review.md
    - .loom/packets/ralph/20260503T055023Z-ticket-queryrc9-iter-01.md
source_fingerprint:
  git_commit: 477b6fe7b77dc0752daef13e1b78c7319a8eb115
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 477b6fe7b77dc0752daef13e1b78c7319a8eb115
  git_status_summary: clean
  git_status_detail: clean working tree at packet compile time
  compiled_from:
    - ticket:queryrc9
    - plan:skills-corpus-context-integrity-hardening-pass
    - initiative:skills-corpus-context-integrity-hardening-pass
    - research:skills-corpus-context-integrity-hardening-review
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: tight
  max_source_files: 6
  max_excerpt_lines_per_file: 180
  avoid_full_file_reads: true
sources:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:queryrc9
  files:
    - skills/loom-records/references/query-and-linking.md
    - skills/loom-records/SKILL.md
    - skills/loom-bootstrap/references/06-filesystem-and-tooling.md
links: {}
---

# Mission

Consolidate common Markdown-native graph query recipes for `ticket:queryrc9` so
fresh agents can recover tickets, packets, claim traces, critique state, and
placeholder risk without a generated index, CLI, dashboard, MCP, schema validator,
or command wrapper.

# Bound Context

The existing `skills/loom-records/references/query-and-linking.md` already proves
that Loom is grep-friendly and contains several useful queries. The council
finding is that common recipes are scattered or incomplete for cold start,
active/open tickets, stale compiled packets, claim-to-evidence/critique traces,
open critique findings, stale/superseded records, and placeholder scans. Keep the
surface Markdown-native and example-oriented.

# Source Snapshot

- `ticket:queryrc9` requires ordinary-tool query recipes, no hidden indexes or CLI
  surfaces, coverage for stale compiled packets and claim/evidence/critique
  traces, evidence, and mandatory critique.
- `plan:skills-corpus-context-integrity-hardening-pass` requires sequential
  tickets, structural evidence, critique, retrospective disposition, commit, and
  push per ticket.
- `research:skills-corpus-context-integrity-hardening-review` rejects validators,
  schema engines, command routers, CLIs, dashboards, MCP dependencies, hidden
  helpers, and new canonical owner layers.

# Verification Targets

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009`
- `ticket:queryrc9#ACC-001`
- `ticket:queryrc9#ACC-002`
- `ticket:queryrc9#ACC-003`
- `ticket:queryrc9#ACC-004`

# Task For This Iteration

Make the smallest coherent query-recipe consolidation:

1. Add or expand records query guidance so common graph queries are easy to find
   from the records/tooling surface.
2. Cover at least: cold-start orientation, active/open tickets, pending/stale
   compiled packets, claim-to-evidence/critique traces, open critique findings,
   stale/superseded records, and placeholder scans.
3. Frame recipes as examples that use ordinary filesystem tools, not mandatory
   runtime dependencies or proof by query alone.
4. If a pointer from bootstrap tooling improves discovery, add only a short
   pointer. Do not expand bootstrap into a large recipe catalog.
5. Do not introduce generated indexes, dashboards, MCP dependencies, schema
   validators, command wrappers, or new owner layers.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- current and updated query coverage for active/open tickets;
- pending/stale compiled packets;
- claim-to-evidence/critique traces;
- open critique findings;
- stale/superseded records;
- placeholder scans;
- wording that recipes are ordinary-tool examples, not runtime dependencies or
  validation proof by themselves.

Run `git diff --check` after editing.

# Stop Conditions

Stop and report `blocked` or `escalate` if satisfying the ticket would require a
generated index, dashboard, MCP dependency, schema validator, command wrapper,
new owner layer, or making every recipe mandatory for every task.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled from clean `main` at `477b6fe` after closing and pushing
`ticket:localed7`. The parent normalized the ticket's existing `change_class`
from invalid `records-grammar` profile vocabulary to valid `protocol-authority`
before launch.

# Child Output

Outcome: stop - bounded query recipe consolidation completed within child write
scope.

Files changed:

- `skills/loom-records/references/query-and-linking.md`
- `skills/loom-records/SKILL.md`
- `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`

Records changed: none by child.

Before observations:

- Active/open tickets had only a basic `rg -l` status query.
- Pending compiled packets already had useful discovery guidance.
- Claim/evidence/critique tracing existed only as scattered single-purpose
  queries.
- No dedicated open critique findings recipe existed.
- Stale/superseded coverage was split between stale wiki and later semantic
  queries.
- No placeholder scan recipe existed.
- Discovery-not-proof wording existed locally but not as global framing.

After observations:

- Added explicit discovery-not-proof framing.
- Added cold-start graph orientation.
- Expanded active/open ticket queries with IDs, status, updated time, and links.
- Retained and clarified pending/stale compiled packet guidance.
- Added claim tracing across specs, tickets, packets, evidence, critique, and
  wiki.
- Added open critique findings discovery.
- Added stale/superseded lifecycle discovery.
- Added placeholder risk scans with caution about intentional template
  placeholders.
- Added records skill and bootstrap tooling pointers without turning recipes into
  a mandatory runtime.

Validation: `git diff --check` passed with no output.

Self-review: edits stayed within the three allowed child write paths and kept
recipes Markdown-native and ordinary-tool based.

Blockers/residual risks: no blockers. Parent needs evidence, mandatory critique,
and ticket-owned acceptance review.

Recommendation: `review_required`; next route is parent evidence recording, then
mandatory critique.

# Parent Merge Notes

Accepted child output as in scope. Parent will record structural evidence and
route to mandatory critique before ticket acceptance.
