# Product Surface Language Review

ID: packet:20260511T070642Z-product-surface-language-review
Type: Packet
Status: consumed
Created: 2026-05-11 07:06 UTC
Updated: 2026-05-11 07:15 UTC
Target: ticket:20260510-product-surface-language-cleanup
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Risk: medium - review concerns shipped instruction wording and public protocol docs.
Review Lens: product surface leakage, language consistency, evidence sufficiency

## Mission

Review whether the latest language cleanup removes package-boundary guidance and eval-shaped examples from the product-facing instruction corpus while preserving Loom's intended workflow semantics.

## Context Bundle

Records:

- `ticket:20260510-product-surface-language-cleanup` - target ticket and acceptance.
- `evidence:20260510-product-surface-language-cleanup-checks` - command and grep evidence.
- `plan:20260510-core-loop-hardening` - prior completed plan for context only.
- `audit:20260510-loop-hardening-review` - prior audit, now superseded only for this language-leakage concern.

Files, Diffs, Or External References:

- Current git diff in the worktree - primary source for changed product-facing prose.
- `loom-core/skills/**` - shipped skill corpus.
- `loom-playbooks/skills/**` - shipped workflow skill corpus.
- `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, `loom-core/README.md`, `loom-playbooks/README.md` - public docs that restate the route.

## Read Scope

- Read this packet and target ticket.
- Inspect current git diff.
- Inspect changed shipped skill files and docs as needed.
- Treat `.loom/` and `evals/` records as dogfood/internal evidence, not shipped product doctrine.

## Write Scope

Records Or Artifacts:

- None - read-only review. Return output through launch transport.

Source Paths:

- None - do not edit files.

## Source Snapshot

- Branch: `main`.
- Worktree has modified shipped skills and docs plus new dogfood Loom records.
- Package smoke/pack checks and `git diff --check` passed after cleanup.
- Grep checks over shipped skill directories returned no package-boundary or eval-shaped term matches listed in the evidence.

## Task

Review the current diff and answer:

- Do shipped skill bodies avoid explaining workflow precedence through package-layer distinctions?
- Do shipped skill bodies use Loom surfaces and named skills instead of package names where workflow routing matters?
- Were eval-shaped examples removed from the shipped skill corpus?
- Do public docs avoid introducing package-boundary language into operational workflow guidance, while still allowing install/package facts where needed?
- Is the ticket/evidence state honest about what was and was not verified?

Non-goals:

- Do not edit files.
- Do not require removing package names from install/package identity docs where they are factual installation surfaces.
- Do not review the eval app implementation.

## Evidence, Review, Or Verification Expectations

Return findings first with severity and file/line references when practical. Include residual risks and a bounded verdict: `clear`, `concerns`, `changes-needed`, or `inconclusive`.

## Stop Conditions

- Return `blocked` if the diff or target ticket is unavailable.
- Return `escalate` if the correct boundary between install docs and skill-consumer prose needs operator judgment.

## Output Contract

The worker must return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed: expected `None`
- records changed: expected `None`
- findings, observations, and verdict
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

## Worker Output

Outcome: `stop`

Files changed: None by the worker.

Records changed: None by the worker.

Findings and observations:

- FIND-001: `loom-playbooks/README.md` still used package-boundary operational wording by saying results landed in `Core`. This challenged the ticket's public-surface cleanup claim. Parent disposition: resolved after the worker returned by changing the wording to `Loom records`.
- FIND-002: `ARCHITECTURE.md` still used package-boundary operational wording by saying owning truth lived in `Core records`. This challenged the ticket's public-surface cleanup claim. Parent disposition: resolved after the worker returned by changing the wording to `Loom records`.
- The worker did not identify remaining package-boundary or eval-shaped leakage in shipped skill bodies within the reviewed scope.

Verdict: `changes-needed` for the pre-fix reviewed state because the two public-doc findings needed patching before closure.

Not verified or reviewed:

- The worker did not review the post-fix state because the two wording fixes happened after the worker returned.
- The eval app implementation was out of scope.

Recommended next move:

- Patch the two findings, update evidence, then run or record a narrow final review for the patched state before closing the ticket.
