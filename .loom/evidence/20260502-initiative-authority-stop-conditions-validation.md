---
id: evidence:initiative-authority-stop-conditions-validation
kind: evidence
status: recorded
created_at: 2026-05-02T19:46:59Z
updated_at: 2026-05-02T19:51:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:authst4p
  packet:
    - packet:ralph-ticket-authst4p-20260502T194511Z
  critique:
    - critique:initiative-authority-stop-conditions-review
external_refs: {}
---

# Summary

Observation-first validation for `ticket:authst4p`. The implementation added
initiative-owned prompts for delegated authority/autonomy boundaries and
objective-level stop conditions, then aligned drive continuity guidance to those
same field names.

# Procedure

Before changing the source guidance, inspected the packet and target files and
searched for delegated authority, delegated autonomy, autonomy limits,
human-decision triggers, budget/time limits, and objective-level stop-condition
language.

After the edits, repeated targeted searches across `skills/loom-initiatives` and
`skills/loom-drive`, then ran:

```bash
git diff --check
```

# Artifacts

## Before observations

Target file inspection showed:

- `skills/loom-initiatives/templates/initiative.md` had Objective, Why Now, In
  Scope, Out Of Scope, Success Metrics, Milestones, Dependencies, Risks, Linked
  Work, Status Summary, and Completion Basis sections, but no delegated
  authority/autonomy or objective-level stop-condition prompt.
- `skills/loom-initiatives/references/initiative-shape.md` listed core sections
  and objective criteria, but did not state when delegated drive/autonomous work
  makes autonomy or stop-condition fields required.
- `skills/loom-drive/SKILL.md` and drive references already described initiative
  ownership for delegated autonomy, budget/time limits, and objective-level stop
  conditions, but did not consistently point at initiative-owned field names.

Selected before-search observations:

- Delegated authority/autonomy terms were present in `skills/loom-drive/SKILL.md`
  lines 43, 56, 134, 152, 198, and 238; in
  `skills/loom-drive/references/drive-loop.md` lines 76, 168, and 192; and in
  `skills/loom-drive/references/continuity-contract.md` lines 16 and 40.
- Human-decision/user-approval terms were present in
  `skills/loom-drive/SKILL.md` line 154,
  `skills/loom-drive/references/drive-loop.md` line 76,
  `skills/loom-drive/references/checkpoint-resume-protocol.md` line 82, and
  `skills/loom-drive/references/continuity-contract.md` line 41.
- Budget/time language was present in `skills/loom-drive/SKILL.md` lines 57,
  153, and 246; `skills/loom-drive/references/drive-loop.md` lines 77 and 197;
  and `skills/loom-drive/references/continuity-contract.md` lines 16 and 42.
- Objective-level stop-condition language was present in drive guidance and the
  ticket/packet, but not in `skills/loom-initiatives/templates/initiative.md` or
  `skills/loom-initiatives/references/initiative-shape.md`.

## After observations

Targeted after searches found:

- `skills/loom-initiatives/templates/initiative.md` now has
  `# Delegated Authority / Autonomy Boundaries` at line 30 and
  `# Objective-Level Stop Conditions` at line 41.
- `skills/loom-initiatives/references/initiative-shape.md` now lists those field
  names in core sections at lines 11-14 and explains optional vs required use at
  lines 43-64.
- `skills/loom-drive/SKILL.md` now points to
  `# Delegated Authority / Autonomy Boundaries` and
  `# Objective-Level Stop Conditions` at lines 57-58 and repeats the same field
  names in focused objective questions at lines 153-156.
- `skills/loom-drive/references/continuity-contract.md` maps those exact fields
  to the initiative at line 16 and describes them in objective contract fields at
  lines 40-43.
- `skills/loom-drive/references/drive-loop.md` uses the same field names in the
  objective-contract state at lines 30-31 and focused objective questions at
  lines 77-80.
- `skills/loom-drive/references/checkpoint-resume-protocol.md` uses the same
  field names in the authority gate at lines 82-84.

## Validation command output

```text
$ git diff --check
<no output; exit 0>
```

# Supports Claims

- `initiative:skills-corpus-council-precision-pass#OBJ-004`
- `ticket:authst4p#ACC-001`
- `ticket:authst4p#ACC-002`
- `ticket:authst4p#ACC-003`
- `ticket:authst4p#ACC-004`

# Challenges Claims

None - the observed source changes and whitespace validation support the scoped
claims above. Mandatory critique for `ticket:authst4p#ACC-005` is recorded
separately in `critique:initiative-authority-stop-conditions-review`.

# Environment

Commit: `d98a2ef2a26a8519675235fc4c6624a8ab921a93`
Branch: `main`
Runtime: Markdown/source inspection with repository tools
OS: macOS / darwin
Relevant config: observation-first Ralph packet
`packet:ralph-ticket-authst4p-20260502T194511Z`

# Validity

Valid for: working tree after parent reconciliation and oracle critique for
`ticket:authst4p`.
Recheck when: any of the cited initiative/drive guidance, ticket, or packet files
change before acceptance.

# Limitations

This evidence records structural observations and `git diff --check`; it is not
an adversarial critique. Mandatory critique profiles `protocol-change`,
`operator-clarity`, and `routing-safety` are recorded in
`critique:initiative-authority-stop-conditions-review`.

# Result

The target initiative template/reference now expose the delegated authority and
objective-level stop-condition cues, and drive guidance now uses the same
initiative-owned field names. `git diff --check` passed with no output.

# Interpretation

The evidence supports ACC-001 through ACC-004 as implemented and structurally
validated. Mandatory critique for ACC-005 is satisfied by
`critique:initiative-authority-stop-conditions-review`.

# Related Records

- `ticket:authst4p`
- `packet:ralph-ticket-authst4p-20260502T194511Z`
- `critique:initiative-authority-stop-conditions-review`
- `initiative:skills-corpus-council-precision-pass#OBJ-004`
