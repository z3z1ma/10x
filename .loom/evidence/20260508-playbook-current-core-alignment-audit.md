---
id: evidence:playbook-current-core-alignment-audit
kind: evidence
status: recorded
created_at: 2026-05-08T17:22:43Z
updated_at: 2026-05-08T17:22:43Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:pbcore26
  spec:
    - spec:core-and-playbooks-package-contract
external_refs: {}
---

# Summary

Observed the current `loom-playbooks` corpus against current `loom-core` doctrine
for `ticket:pbcore26`. The audit found no playbook edits needed: playbooks remain
optional workflow routes, do not preload or duplicate core doctrine, declare the
core dependency in each skill, and route closure, evidence, critique, packet, and
owner-layer truth back to core-owned records.

# Observation

Observed at: 2026-05-08T17:22:43Z

Source state: working tree on the current checkout, with pre-existing untracked
`loom.zip` outside scope and new `ticket:pbcore26` / this evidence record in
progress. `git status --short -- loom-playbooks` returned no output.

Procedure: read and searched `loom-playbooks/README.md`, `loom-playbooks/package.json`,
`loom-playbooks/loom-playbooks.mjs`, `loom-playbooks/skills/**/*.md`, current
`using-loom` doctrine, `loom-records/references/status-lifecycle.md`, and
`spec:core-and-playbooks-package-contract`; ran targeted grep scans and package
smoke / dry-run pack checks.

Expected result when applicable: no playbook wording should redefine canonical
owner layers, ticket state, acceptance disposition, evidence sufficiency, critique
verdicts, Ralph outcomes, packet lifecycle, or core dependency behavior.

Actual observed result: no actionable alignment findings were found. The only
risky-looking terms were explicitly framed as support-local checkpoint facts,
non-Ralph transport summaries, ticket-owned dispositions, or core Ralph outcomes.

Procedure verdict / exit code: pass. Command checks exited successfully unless
they intentionally returned no matches.

# Artifacts

- Parallel read-only audit tasks returned no actionable owner-boundary,
  vocabulary, or dependency findings: `ses_1f76f18a0ffe7DjRxY2VricGD5`,
  `ses_1f76f184bffeVAim5AlEf5EuHz`, and
  `ses_1f76f1844ffek2bOzEeaSPqbMd`.
- `npm run smoke` in `loom-playbooks` returned `ok: true`,
  `usingLoomReferenceCount: 0`, `instructionCount: 0`,
  `doesNotPreloadCoreDoctrine: true`, and `skillCount: 22`.
- `npm run smoke` in `loom-core` returned `ok: true`,
  `usingLoomReferenceCount: 8`, `instructionCount: 8`, and `skillCount: 15`.
- `npm run pack:check` in `loom-playbooks` passed and the dry-run tarball listed
  only the playbook package entrypoint, package metadata, README, and playbook
  skill files.
- `git diff --check -- loom-playbooks .loom/tickets/20260508-pbcore26-align-playbooks-with-current-core.md`
  returned no output.
- `rg --files-without-match '^## Core Dependency$' loom-playbooks/skills -g SKILL.md`
  returned no output, supporting that every playbook `SKILL.md` declares the core
  dependency section.
- Targeted scans for owner truth, acceptance, evidence, critique, Ralph outcomes,
  support statuses, and non-Ralph transport labels were manually reviewed. Matches
  were aligned examples such as `loom-agent-orchestration` mapping
  `done_with_concerns` and `needs_context` back to owner truth, `loom-code-review`
  using ticket-owned finding dispositions, and `loom-drive` marking checkpoint
  facts as support-local or owner-cited facts rather than saved workflow state.
- `git diff --name-only -- loom-playbooks` returned no output.
- `git status --short -- loom-playbooks` returned no output.

# Supports / Challenges

Supported claims:

- `spec:core-and-playbooks-package-contract#REQ-004` — package smoke and dry-run
  pack output show `loom-playbooks` exposes only the playbook skill set, not core
  owner-layer skills.
- `spec:core-and-playbooks-package-contract#REQ-005` — playbooks do not preload
  using-Loom doctrine and every playbook skill declares the `loom-core`
  dependency.
- `spec:core-and-playbooks-package-contract#REQ-008` — skill prose fails closed by
  directing agents to load/install core rather than treating a playbook as a
  substitute for doctrine or record grammar.
- `ticket:pbcore26#ACC-001` — targeted scans and manual review found no active
  playbook guidance redefining owner layers, ticket state, acceptance, evidence,
  critique, Ralph outcomes, or packet lifecycle.
- `ticket:pbcore26#ACC-002` — package metadata, smoke output, and skill sections
  preserve playbooks as optional and core-dependent.
- `ticket:pbcore26#ACC-003` — no product prose patch was needed; existing playbook
  workflow value already routes durable facts back to core owner records.

Challenged claims:

- None observed.

Weak or partial support:

- Semantic alignment cannot be completely proven by grep. This evidence combines
  targeted scans, manual spot checks, and independent read-only audit passes, but
  future operator use may still expose softer wording drift.

# Limits

This record does not validate every possible operator interpretation or external
harness install behavior. It does not change `loom-core`, package membership,
manifests, generated adapters, scripts, validators, or hidden runtimes.

Freshness / recheck trigger:

- Recheck when `loom-core/skills/using-loom/**`, `loom-core/skills/loom-records/references/status-lifecycle.md`,
  `spec:core-and-playbooks-package-contract`, `loom-playbooks/package.json`,
  `loom-playbooks/loom-playbooks.mjs`, or `loom-playbooks/skills/**/*.md` changes.

Sensitivity / redaction:

- Safe to keep. No secrets, credentials, private data, or sensitive logs were
  captured.

# Related Records

- ticket:pbcore26
- ticket:pbalign8
- spec:core-and-playbooks-package-contract
- evidence:playbook-core-alignment-check
