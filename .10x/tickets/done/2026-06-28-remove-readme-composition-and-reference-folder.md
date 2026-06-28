Status: done
Created: 2026-06-28
Updated: 2026-06-28
Depends-On: README.md, SKILL.md

# Remove README Composition And Reference Folder

## Scope

Apply the next README cleanup requested by the user.

Included:

- Remove the README Composition section.
- Delete the `references/` folder.
- Update workflow framing to say 10x tunes the agent's default software
  engineering behavior in addition to adding project context.
- Replace the fictional rich-record example with a realistic 10x decision based
  on actual project context.
- Record the real install-path decision if the README uses it as the example.

Excluded:

- Changes to `SKILL.md`.
- Changes to autoresearch tooling or candidates.

## Acceptance Criteria

- AC-001: README has no Composition section.
- AC-002: `references/` is deleted and no live README references to it remain.
- AC-003: Workflow framing mentions both project context and default agent
  behavior tuning for software engineering.
- AC-004: Record example is realistic and grounded in actual repo context.
- AC-005: Validation checks pass.

## Progress And Notes

- 2026-06-28: Opened from user request after README context/workflow refinement.
- 2026-06-28: Removed README Composition section, deleted `references/`, added
  `.10x/decisions/equal-first-class-install-paths.md`, replaced the README
  example with that real decision, and updated workflow framing. Evidence:
  `.10x/evidence/2026-06-28-readme-composition-reference-removal.md`. Review:
  `.10x/reviews/2026-06-28-readme-composition-reference-removal.md`.

## Blockers

None.

## References

- `README.md`
- `SKILL.md`
- `.10x/decisions/equal-first-class-install-paths.md`
