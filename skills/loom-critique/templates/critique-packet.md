---
id: "packet:critique-<TBD: encoded-target-or-change-slug>-<TBD: UTC compact timestamp>"
kind: packet
packet_kind: critique
status: compiled
target: "<TBD: ticket:<token>, record ref, review target slug, diff handle, or external summary ID>"
review_target:
  kind: "<TBD: choose record, code_change, pull_request, branch, commit, diff, external_summary, release_package, or handoff_package>"
  summary: "<TBD: one-line human-readable review target>"
  ref: "<TBD: record ref, path, branch, commit, PR, package ID, or none>"
  diff: "<TBD: branch, commit range, PR, diff target, or none>"
  paths:
    - "<TBD: changed paths under review, or None - no path-specific target>"
mode: review
change_class: "<TBD: choose one change class before saving>"
# Optional when the parent wants packet-local risk carried explicitly:
# risk_class: "<TBD: choose low, medium, or high before saving>"
style: reference-first
created_at: "<TBD: UTC timestamp>"
updated_at: "<TBD: UTC timestamp>"
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - "<TBD: critique child write refs, or None - reviewer returns output only>"
  paths:
    - "<TBD: critique child write paths, or None - reviewer returns output only>"
parent_merge_scope:
  records:
    - "<TBD: critique:<slug> and ticket:<token> when a ticket owns execution, or None - rationale>"
  paths:
    - "<TBD: parent reconciliation paths, or None - rationale>"
source_fingerprint:
  git_commit: "<TBD: sha or unknown with rationale>"
  integration_remote: "<TBD: remote name, none, or unknown with rationale>"
  integration_ref: "<TBD: ref, tag, commit, or unknown with rationale>"
  integration_commit: "<TBD: sha or unknown with rationale>"
  git_status_summary: "<TBD: clean, dirty_tracked, dirty_untracked, dirty_mixed, or unknown with rationale>"
  git_status_detail: "<TBD: short status detail, or unknown - rationale>"
  compiled_from:
    - "<TBD: record ref or artifact used to compile this review baseline>"
execution_context:
  branch: "<TBD: branch name or unknown with rationale>"
  push_remote: "<TBD: remote name, same_as_integration, none, or unknown with rationale>"
  worktree: "<TBD: path, none, or unknown with rationale>"
  isolation: "<TBD: none, branch, worktree, sandbox, or unknown with rationale>"
  git_shared_metadata_mutations: "<TBD: forbidden, allowed, or unknown with rationale>"
  destructive_commands: "<TBD: forbidden, allowed, or unknown with rationale>"
  network: "<TBD: choose allowed, forbidden, or unknown - rationale that makes launch safe before saving>"
context_budget:
  posture: normal
  max_source_files: 8
  max_excerpt_lines_per_file: 80
  avoid_full_file_reads: true
sources:
  target_records:
    - "<TBD: record ref under review, or None - rationale>"
  evidence:
    - "<TBD: evidence ref to review, or None - rationale>"
  diffs_or_paths:
    - "<TBD: path, branch, commit range, PR, or None - rationale>"
  prior_packets:
    - "<TBD: packet ref to review, or None - rationale>"
links: {}
---

# Mission

What code, behavior, record, or package should be reviewed and why.

# Governing Context

The owner records, evidence, prior packet output, and acceptance or claim coverage
targets that constrain this review. Critique packets are critique-owned review
contracts, not Ralph implementation packets.

# Review Lens

Named critique profiles to apply:

- <TBD: profile names, e.g. code-change, test-coverage, product-ux, visual-design>

Focus risks:

- <TBD: specific concerns the reviewer should pressure-test>

# Evidence Expectations

What evidence, diff, screenshots, tests, or source inspection should be enough to
judge the target. Critique packets do not use Ralph `verification_posture`.

# Source Snapshot

Curated records, evidence, diffs, tests, or changed files that matter most.

# Diff Or Artifact Under Review

Where the reviewer should find the git diff, changed-file list, branch, commit,
pull request, record, screenshot, or package.

# Required Questions

- Did the target satisfy the ticket, spec, acceptance coverage, and declared write boundary?
- Did it add unrequested behavior, scope creep, or a claim in the wrong owner layer?
- Does evidence support the implementation and completion claims, or is it stale, partial, missing, or overclaimed?
- Did the reviewer inspect actual files, records, tests, screenshots, and diffs instead of trusting a summary?
- For UI/product work, is the result meaningfully better than the baseline for the primary user task?
- Are unresolved risks blockers, accepted-risk candidates, or linked follow-up work?

# Stop Conditions

Stop or return `blocked` if the review target, source fingerprint, governing
records, diff/artifact, or reviewer write boundary appears materially stale or inconsistent.

# Output Contract

Return:

- verdict;
- findings with severity/confidence and claim challenges when applicable;
- evidence reviewed;
- file/line or artifact references when practical;
- residual risks;
- follow-up recommendation.

The parent creates or updates real critique and ticket records during reconciliation.

# Working Notes

Optional parent notes.

# Reviewer Output

To be filled after the review.

# Parent Merge Notes

How the parent reconciled the critique into the graph and moved packet status to
`consumed`, `superseded`, or `abandoned`.
