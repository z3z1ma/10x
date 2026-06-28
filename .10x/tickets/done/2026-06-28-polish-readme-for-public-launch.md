Status: done
Created: 2026-06-28
Updated: 2026-06-28
Depends-On: README.md, SKILL.md, autoresearch/README.md, .10x/evidence/2026-06-28-record-richness-hypothesis-batch.md

# Polish README For Public Launch

## Scope

Tighten the public `README.md` so it is easier to try, easier to share, and
accurately reflects the current state of 10x, including autoresearch as both an
evaluation suite and a scientific improvement environment.

Included:

- Compress repetitive or noisy README passages without flattening the voice.
- Make installation and immediate use obvious for copy-paste and `npx skills`.
- Explain the latest 10x value proposition accurately: disciplined local-agent
  execution, durable project memory, evidence/review/retrospective loops, and
  autoresearch-backed refinement.
- Preserve the human, opinionated, principal-engineer tone.
- Use at least one fresh-context review before finalizing copy.

Excluded:

- Changes to canonical `SKILL.md`.
- Changes to autoresearch runner behavior, seed catalogs, or scoring rubrics.
- Adding marketing claims that cannot be supported from repository contents.
- Broad visual redesign, asset changes, or release automation.

## Acceptance Criteria

- AC-001: README has a faster first-screen pitch and clear install path.
- AC-002: README mentions autoresearch without turning the main page into a
  tooling manual.
- AC-003: README accurately describes the project as instructions/plain
  Markdown with no runtime dependency.
- AC-004: Copy is tighter than the starting README and avoids redundant
  explanations.
- AC-005: Fresh-context review findings are considered before final edits.
- AC-006: Markdown links and anchors are valid for changed sections.
- AC-007: Final diff is reviewed for unsupported claims, tone drift, and
  accidental changes outside scope.

## Progress And Notes

- 2026-06-28: Opened from user request to prepare the project for broader
  sharing after recent skill and autoresearch improvements.
- 2026-06-28: Rewrote `README.md` for a faster first screen, equal Skills CLI
  and copy-paste install paths, compressed philosophy, concrete behavior
  example, autoresearch credibility section, and frontmatter guidance.
- 2026-06-28: Incorporated three fresh-context README reviews. Verification:
  local README link check, `python3 autoresearch/validate.py`,
  `python3 -m unittest discover -s autoresearch/tests`, and `git diff --check`.
  Evidence: `.10x/evidence/2026-06-28-readme-public-launch-polish.md`.
  Review: `.10x/reviews/2026-06-28-readme-public-launch-polish.md`.

## Blockers

None.

## References

- `README.md`
- `SKILL.md`
- `autoresearch/README.md`
- `.10x/evidence/2026-06-28-record-richness-hypothesis-batch.md`
