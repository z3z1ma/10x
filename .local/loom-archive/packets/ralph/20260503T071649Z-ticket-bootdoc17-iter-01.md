---
id: packet:ralph-ticket-bootdoc17-20260503T071649Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:bootdoc17
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T07:16:49Z
updated_at: 2026-05-03T07:18:35Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-bootstrap/references/06-filesystem-and-tooling.md
parent_merge_scope:
  records:
    - ticket:bootdoc17
  paths:
    - .loom/tickets/20260503-bootdoc17-make-bootstrap-heredoc-copy-safe.md
    - .loom/evidence/20260503-bootstrap-heredoc-copy-safety-validation.md
    - .loom/critique/bootstrap-heredoc-copy-safety-review.md
    - .loom/packets/ralph/20260503T071649Z-ticket-bootdoc17-iter-01.md
source_fingerprint:
  git_commit: f93b432e6c9152ec7ac6db73ca381768ce83a8a2
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: f93b432e6c9152ec7ac6db73ca381768ce83a8a2
  git_status_summary: clean
  git_status_detail: clean working tree at packet compile time
  compiled_from:
    - ticket:bootdoc17
    - plan:skills-corpus-context-integrity-hardening-pass
    - initiative:skills-corpus-context-integrity-hardening-pass
    - research:skills-corpus-third-pass-follow-up-validation
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
  max_source_files: 4
  max_excerpt_lines_per_file: 180
  avoid_full_file_reads: true
sources:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-third-pass-follow-up-validation
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:bootdoc17
  files:
    - skills/loom-bootstrap/references/06-filesystem-and-tooling.md
links: {}
---

# Mission

Make the bootstrap filesystem/tooling here-doc example copy-safe so a fresh agent
does not create a literal `.loom/research/<slug>.md` path when copying the
example.

# Bound Context

The bootstrap reference is high-leverage operator guidance. The solution should
stay Markdown-native and shell-native, using ordinary variables or inline shell
only where it improves copy safety. Do not add a command wrapper, runtime
validator, schema engine, generated index, or broader template catalog.

# Source Snapshot

- `skills/loom-bootstrap/references/06-filesystem-and-tooling.md` currently has
  an `### Emit a here-doc` example that writes directly to
  `.loom/research/<slug>.md`.
- The prose warns operators to replace placeholders, but the command itself is
  still copyable with a literal placeholder path.
- The example already uses an explicit `<TBD: write the research question before
  saving>` placeholder inside the body.

# Verification Targets

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-018`
- `ticket:bootdoc17#ACC-001`
- `ticket:bootdoc17#ACC-002`
- `ticket:bootdoc17#ACC-003`
- `ticket:bootdoc17#ACC-004`

# Task For This Iteration

Make the smallest coherent bootstrap-reference edit:

1. Replace the here-doc command's literal `.loom/research/<slug>.md` output path
   with a safer variable pattern that requires the operator to choose a real slug
   before writing.
2. Keep or add a local placeholder scan near the example so operators can check
   the saved file before treating it as project truth.
3. Preserve the concise Markdown-native shell guidance style.
4. Do not add a command wrapper, runtime validator, schema engine, generated
   index, helper dependency, or broad template catalog.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- whether the here-doc command can write to a literal `<slug>` path;
- whether the example includes or points to a local placeholder scan for the
  saved file;
- whether the edited guidance remains concise and Markdown-native;
- absence of command wrapper, runtime validator, schema engine, generated index,
  helper dependency, or broad template catalog changes.

Run `git diff --check` after editing.

# Stop Conditions

Stop and report `blocked` or `escalate` if satisfying the ticket would require a
new command wrapper, runtime validator, schema engine, generated index, helper
dependency, broad template catalog, or changes outside the declared product file.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled from clean `main` at `f93b432` after closing and pushing
`ticket:phvalid16`.

# Child Output

Outcome: `stop`

Files changed:

- `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`

Records changed by child:

- None. Parent retained ticket, evidence, critique, and packet reconciliation.

Observed result:

- Before: here-doc wrote directly to literal `.loom/research/<slug>.md` if copied
  blindly.
- Before: no local placeholder scan appeared near the here-doc example.
- After: example guards on `slug="<replace-with-real-slug>"` and refuses to write
  until replaced.
- After: output path uses `path=".loom/research/${slug}.md"`.
- After: local scan added: `rg -n '<[^>]+>|TBD' "$path"`.
- After: guidance remains Markdown-native shell guidance; no wrapper, runtime,
  schema, index, helper, or catalog was added.

Verification:

- `git diff --check` passed with no output.

Blockers or residual risks:

- No blockers.
- The local placeholder scan remains heuristic and requires operator review of
  hits.

Recommendation:

- Move `ticket:bootdoc17` to mandatory critique.

# Parent Merge Notes

- 2026-05-03T07:18:35Z: Parent accepted the bounded implementation output,
  recorded `evidence:bootstrap-heredoc-copy-safety-validation`, marked this packet
  `consumed`, and moved `ticket:bootdoc17` to `review_required` for mandatory
  critique.
