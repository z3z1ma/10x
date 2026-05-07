---
id: critique:using-loom-rename-review
kind: critique
status: final
created_at: 2026-05-07T19:33:33Z
updated_at: 2026-05-07T19:35:57Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:usng507a working-tree diff"
links:
  ticket:
    - ticket:usng507a
  evidence:
    - evidence:using-loom-rename-validation
external_refs: {}
---

# Summary

Reviewed the working-tree diff for the `using-loom` entry-skill rename, doctrine
alignment, drive/wiki/ticket audit fixes, adapter preload updates, current owner
record reconciliation, and package smoke output.

# Review Target

Target: `ticket:usng507a` working-tree diff in `repo:root`.

Required critique profiles:

- protocol-change
- operator-clarity
- packaging-surface

The review covered product surfaces under `skills/`, public docs, adapter files,
current owner records, `open-loom.mjs`, and internal example fixture consistency.
Unrelated untracked `examples/00-todo-app` files were intentionally ignored.

# Verdict

`pass_with_findings`

The initial critique found five issues. Follow-up edits resolved the code, docs,
fixture, and current owner-record concerns before this final record was written.
A targeted re-check reported no remaining findings in the requested scope.

# Findings

## FIND-001: Drive activation was too literal

Severity: medium
Confidence: high
State: open

Observation: Initial review found `skills/loom-drive/SKILL.md:3` described
activation around the user asking to "drive" an initiative/outcome, while the
skill body expects broad delegated outcome wording. The fixed line now names
build, improve, modernize, clean up, migrate, and continue requests.

Why it matters: A literal activation phrase would make agents miss normal
delegated-objective requests and fail to enter the drive loop when the user did
not say the word "drive".

Follow-up: Fixed in `skills/loom-drive/SKILL.md:3`; ticket should record this as
resolved.

Challenges: ticket:usng507a#ACC-004

## FIND-002: Drive objective-state vocabulary was still inconsistent

Severity: medium
Confidence: high
State: open

Observation: Initial review found `skills/loom-drive/references/checkpoint-resume-protocol.md:28`
still used `partial` and omitted `out_of_scope`. The fixed checkpoint vocabulary
now matches the other drive references: `satisfied`, `partially_satisfied`,
`open`, `blocked`, and `out_of_scope`.

Why it matters: Mixed state vocabulary weakens resumption, critique, and ticket
coverage because different drive references imply different objective-state
contracts.

Follow-up: Fixed in `skills/loom-drive/references/checkpoint-resume-protocol.md:28`;
ticket should record this as resolved.

Challenges: ticket:usng507a#ACC-004

## FIND-003: Packaging owner records had stale reference counts and terminology

Severity: medium
Confidence: high
State: open

Observation: Initial review found current owner records still saying seven
references after `using-loom` had eight ordered references. The spec now requires
eight ordered using-Loom reference files in `.loom/specs/opencode-plugin-install-contract.md:118`,
and install research now avoids the stale seven-reference claim in
`.loom/research/loom-install-distribution-methods.md:374`.

Why it matters: A stale count can make validation omit
`08-trust-boundaries.md`, which is part of the mandatory ordered doctrine.

Follow-up: Fixed in the current owner records; ticket should record this as
resolved.

Challenges: ticket:usng507a#ACC-001

## FIND-004: Ticket ledger was not yet reconciled

Severity: medium
Confidence: high
State: open

Observation: Initial review found `ticket:usng507a` still had pending finding,
evidence, critique, and acceptance fields while implementation was already near
completion.

Why it matters: Tickets are Loom's live execution ledger. The work cannot close
truthfully until the ticket consumes the final evidence, critique, finding
dispositions, and acceptance decision.

Follow-up: Create evidence and critique records, then update `ticket:usng507a`
before closure.

Challenges: ticket:usng507a#ACC-005

## FIND-005: Internal fixture still referenced the deleted entry-skill path

Severity: low
Confidence: high
State: open

Observation: Initial review found the high-risk protocol-change fixture still
referenced `after/skills/loom-bootstrap/...` while surrounding examples had been
renamed. The fixture references now point at
`after/skills/using-loom/references/07-validation-and-honesty.md`, and the fixture
file path was moved under `after/skills/using-loom/`.

Why it matters: Internal golden examples are not product truth, but inconsistent
fixtures slow future review and can make drift look intentional.

Follow-up: Fixed in `examples/04-high-risk-protocol-change-with-critique/after/.loom/evidence/evidence-gate-structural-check.md:29`,
`examples/04-high-risk-protocol-change-with-critique/after/.loom/critique/evidence-gate-review.md:61`,
and the before/after fixture file paths; ticket should record this as resolved.

Challenges: ticket:usng507a#ACC-001

# Evidence Reviewed

- `evidence:using-loom-rename-validation`
- `npm run pack:check` output summarized in `evidence:using-loom-rename-validation`
- `git diff --check` output summarized in `evidence:using-loom-rename-validation`
- Product stale-name scan output summarized in `evidence:using-loom-rename-validation`
- Current owner-record stale-name/count scan output summarized in `evidence:using-loom-rename-validation`
- Skill frontmatter validation output summarized in `evidence:using-loom-rename-validation`
- Targeted drive vocabulary check summarized in `evidence:using-loom-rename-validation`
- Oracle review session `ses_1fc1b46f9ffeO55n0btZlN4zRG`, including final targeted
  re-check with no remaining findings in requested scope
- Representative files inspected:
  `skills/using-loom/SKILL.md`, `skills/using-loom/references/*.md`,
  `skills/loom-drive/SKILL.md`,
  `skills/loom-drive/references/checkpoint-resume-protocol.md`,
  `.loom/specs/opencode-plugin-install-contract.md`,
  `.loom/research/loom-install-distribution-methods.md`, `open-loom.mjs`,
  adapter preload files, and example fixture paths

# Residual Risks

- Runtime installs in Claude, Codex, Gemini, Cursor, and OpenCode were not rerun;
  validation here is structural plus local OpenCode package smoke/dry-run.
- Historical closed `.loom` records still contain old entry-skill names as
  historical observations. They were not rewritten unless they were current owner
  records or touched fixtures.
- `open-loom.mjs` visible smoke keys and helper names now use using-Loom wording;
  external consumers importing old named helpers were not audited.

# Required Follow-up

Before closure, `ticket:usng507a` must consume `evidence:using-loom-rename-validation`,
record ticket-owned dispositions for open findings FIND-001 through FIND-005, and
make the acceptance decision.

# Acceptance Recommendation

`no-critique-blockers`

After the follow-up edits and targeted re-check, critique sees no remaining
required implementation changes before the ticket acceptance gate makes its own
closure decision.
