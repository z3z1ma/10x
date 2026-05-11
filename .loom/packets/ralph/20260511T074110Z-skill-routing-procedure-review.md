# Skill Routing Procedure Review

ID: packet:20260511T074110Z-skill-routing-procedure-review
Type: Packet
Status: consumed
Created: 2026-05-11 07:41 UTC
Updated: 2026-05-11 07:44 UTC
Target: ticket:20260511-skill-routing-procedure-consistency
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Risk: medium - review concerns shipped instruction wording across core doctrine, Ralph guidance, playbook skills, and public docs.
Review Lens: terminology consistency, routed-skill procedure adherence, transport-neutral Ralph launch, product-surface leakage

## Mission

Review the final patched state for `ticket:20260511-skill-routing-procedure-consistency`.

## Context Bundle

Records:

- `ticket:20260511-skill-routing-procedure-consistency` - target ticket and acceptance.
- `evidence:20260511-skill-routing-procedure-consistency-checks` - command and search evidence.
- `ticket:20260510-product-surface-language-cleanup` - prior related cleanup.

Files, Diffs, Or External References:

- Current git diff in the worktree - primary source for changed product-facing prose.
- `loom-core/skills/using-loom/SKILL.md`.
- `loom-core/skills/using-loom/references/how-loom-thinks.md`.
- `loom-core/skills/loom-ralph/SKILL.md`.
- `loom-core/skills/loom-ralph/references/running-packets.md`.
- `loom-playbooks/skills/*/SKILL.md`.
- `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, `loom-core/README.md`, and `loom-playbooks/README.md`.

## Read Scope

- Read this packet, the target ticket, and the evidence record.
- Inspect the current git diff.
- Inspect changed shipped skill files and public docs as needed.
- Treat `.loom/` and `evals/` records as dogfood/internal evidence, not shipped product doctrine.

## Write Scope

Records Or Artifacts:

- None - read-only review. Return output through launch transport.

Source Paths:

- None - do not edit files.

## Source Snapshot

- Branch: `main`.
- Worktree has modified shipped skills and docs plus dogfood Loom records.
- Package smoke/pack checks and `git diff --check` passed after these changes.
- Targeted grep found the routed-skill procedure sentence in all 25 playbook `SKILL.md` files.
- Targeted grep found no stale Ralph wording in core skills that narrows packet-path launch guidance to harness-native subagents.

## Task

Review the current patched state and answer:

- Does product-facing prose clearly distinguish record skills from workflow-specific skills without explaining workflow precedence through package layers?
- Do all playbook `## Loom Surfaces` sections require routed Loom skills to be followed with their own procedure and guidance?
- Is the repeated playbook wording strong enough to prevent treating a route as a shortcut around the target skill?
- Is Ralph launch guidance transport-neutral for harness-native subagents, headless harness commands, manual handoffs, and other worker transports?
- Does the product surface avoid leaking dogfood, eval, or conversation-specific context into shipped skills and public docs?
- Is the evidence honest about what was and was not verified?

Non-goals:

- Do not edit files.
- Do not review eval app implementation.
- Do not require removing factual package/install identity language where it does not explain workflow precedence.

## Evidence, Review, Or Verification Expectations

Return findings first with severity and file/line references when practical. Include residual risks and a bounded verdict: `clear`, `concerns`, `changes-needed`, or `inconclusive`.

## Stop Conditions

- Return `blocked` if the diff, target ticket, or evidence record is unavailable.
- Return `escalate` if the correct boundary between package identity and workflow-precedence wording needs operator judgment.

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

Files changed: None.

Records changed: None.

Findings, observations, and verdict:

- FIND-001: Low severity. `.loom/tickets/20260511-skill-routing-procedure-consistency.md` still said implementation was next even though the diff and evidence described completed wording changes and validation. Parent disposition: resolved by updating the ticket current state, related records, acceptance results, and journal before closure.
- No material findings in the shipped skill or public documentation changes reviewed.
- Product-facing prose distinguishes record skills from workflow-specific skills without explaining workflow precedence through package layers.
- All 25 playbook `SKILL.md` files have `## Loom Surfaces` sections and the routed-skill procedure sentence.
- The repeated playbook wording says to follow the named Loom skill completely and says the playbook does not shorten the target skill's requirements.
- Ralph launch guidance is transport-neutral in the reviewed core skill, reference, and protocol surfaces.
- Product-facing docs did not appear to leak eval or conversation-specific context in the reviewed scope.
- Evidence is honest within its stated scope.

Verdict: `concerns`, limited to the stale target-ticket current-state wording. Shipped prose and evidence reviewed as clear within scope.

What was not verified or reviewed:

- The worker did not rerun package smoke, pack checks, or `git diff --check`; it relied on the evidence record for those command results.
- Eval app implementation was not reviewed.
- Every historical `.loom/` record was not inspected.
- Absence of every possible synonym for stale package-boundary or transport-specific wording was not proven.
- Live agent behavior changes were not verified.

Blockers, risks, or assumptions discovered:

- No blockers.
- Assumption: factual install/package identity language such as `Install Loom Core first` is allowed by the packet non-goal and is not workflow-precedence leakage.
- Residual risk: targeted grep and sampled source review cannot prove complete corpus-wide absence of semantically equivalent stale wording.

Recommended next move:

- Update the target ticket current state and journal to reflect completed implementation, evidence, and review, then proceed toward closure if the maintainer accepts the bounded `concerns` verdict.
