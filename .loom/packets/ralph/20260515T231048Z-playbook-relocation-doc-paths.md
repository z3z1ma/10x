# Playbook Relocation Doc Path Follow-up

ID: packet:20260515T231048Z-playbook-relocation-doc-paths
Type: Packet
Status: consumed
Created: 2026-05-15 23:10 UTC
Updated: 2026-05-15 23:15 UTC
Target: ticket:20260515-playbook-skill-corpus-relocation
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 2
Risk: low - narrow path-only documentation alignment after package relocation.
Verification Posture: observation-first
Change Class: Documentation path alignment

## Mission

Update only the stale active documentation path/package-shape references that block `ticket:20260515-playbook-skill-corpus-relocation#ACC-004` after the Playbook corpus moved from `loom-playbooks/skills/` to `loom-playbooks/playbooks/`.

## Context Bundle

Records:

- `ticket:20260515-playbook-skill-corpus-relocation` - target ticket and ACC-004 stale-path requirement.
- `packet:20260515T230227Z-playbook-skill-corpus-relocation` - first relocation packet that moved source and identified stale docs.
- `decision:0001` - durable package decision requiring the corpus move.
- `research:20260515-gemini-playbooks-skills-root` - Gemini root conflict.
- `AGENTS.md` - already updated contributor package-shape guidance.

Files:

- `INSTALL.md` - stale Playbooks path and generic package skills text.
- `README.md` - package tree and product-surface path references.
- `ARCHITECTURE.md` - package surface path references.
- `loom-playbooks/README.md` - package-local path and package contents references.

## Read Scope

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md`
- `.loom/packets/ralph/20260515T230227Z-playbook-skill-corpus-relocation.md`
- `.loom/constitution/decisions/decision-0001-playbook-skill-corpus-root.md`
- `.loom/research/20260515-gemini-playbooks-skills-root.md`
- `AGENTS.md`
- `INSTALL.md`
- `README.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md` - update Current State and Journal with follow-up result.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `INSTALL.md`
- `README.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`

Do not change package source, plugin manifests, Gemini commands, tests, or unrelated docs behavior in this packet.

## Source Snapshot

The first relocation packet moved runtime source to `loom-playbooks/playbooks/` and updated `AGENTS.md`, package code, package files, and native manifests. It found active docs still mentioning old `loom-playbooks/skills/` or generic Playbooks package `skills/` assumptions in `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md`.

## Task

Make the smallest path/package-shape doc edits needed so active human-facing docs no longer tell future agents or users that Playbooks live under top-level `loom-playbooks/skills/`.

Guidance:

- Replace Playbooks corpus references with `loom-playbooks/playbooks/`.
- Preserve Core references to `loom-core/skills/`; do not rewrite those.
- Do not perform the broader docs/tests behavior rewrite from `ticket:20260515-playbook-explicit-macro-docs-tests`.
- Avoid adding new product doctrine to docs; this is path/package-shape alignment only.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside scope, update the ticket and packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Targeted grep showing no stale active references to `loom-playbooks/skills/` outside `.loom/`.
- Source inspection or grep showing Playbooks docs now point to `loom-playbooks/playbooks/` where appropriate.
- `git diff --check`.

## Stop Conditions

- Stop and return `blocked` if the docs require a broader behavior rewrite instead of path alignment.
- Stop instead of editing package source, manifests, Gemini commands, tests, or unrelated docs sections.
- Stop if the first relocation packet's package state no longer matches the docs being aligned.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

## Worker Output

Outcome: stop

Files changed:

- `INSTALL.md` - replaced stale local Playbooks corpus exposure path with `loom-playbooks/playbooks/`; clarified Claude and Cursor fallback wording so Core remains `loom-core/skills/` and Playbooks use `loom-playbooks/playbooks/`.
- `README.md` - updated the repository layout and product-surface list from `loom-playbooks/skills` to `loom-playbooks/playbooks`.
- `ARCHITECTURE.md` - replaced generic package `skills/` assumptions with explicit Core and Playbooks corpus paths; updated the repository-only product-surface list to `loom-playbooks/playbooks`.
- `loom-playbooks/README.md` - updated fallback exposure and npm package wording from the old `skills/` tree to the relocated `playbooks/` tree.

Records changed:

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md` - Current State and Journal updated with this packet's result; status moved to `review` because audit is the next honest move before closure.
- `.loom/packets/ralph/20260515T231048Z-playbook-relocation-doc-paths.md` - status set to consumed and worker output recorded.

Evidence, review findings, validation output, or observations gathered:

- `rg --glob '!/.loom/**' --glob '!.loom/**' 'loom-playbooks/skills' .` returned no matches.
- `rg 'loom-playbooks/playbooks|playbooks/' INSTALL.md README.md ARCHITECTURE.md loom-playbooks/README.md` showed relocated-path references in the scoped docs.
- `git diff --check` passed.
- Source diff inspection showed the edits were limited to path/package-shape documentation alignment in the scoped files.

What was not verified or reviewed:

- No package smoke, pack, Claude/Cursor/Codex/Gemini validation, or runtime invocation was rerun because this packet was limited to Markdown docs path alignment.
- No Gemini command TOML was implemented or validated.
- No adversarial audit was performed in this packet.

Blockers, risks, or assumptions discovered:

- No blockers discovered.
- Assumption: active `.loom/` historical records may continue to mention `loom-playbooks/skills/` as past state; the stale-path grep intentionally excluded `.loom/` per the packet expectation.

Recommended next move for the consuming surface:

- Run a Ralph audit packet for `ticket:20260515-playbook-skill-corpus-relocation` before closure, challenging ACC-001 through ACC-005 with the relocation diff, scoped verification, and this follow-up doc alignment.
