Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/done/2026-06-28-remove-readme-composition-and-reference-folder.md, README.md, .10x/decisions/equal-first-class-install-paths.md

# README Composition Reference Removal

## What Was Observed

The README was updated per user request:

- Removed the Composition section.
- Deleted `references/KARPATHY.md` and `references/MINIMALIST.md`; no files
  remain under `references/`.
- Added `.10x/decisions/equal-first-class-install-paths.md` and used that real
  decision as the README record example.
- Updated workflow framing to say 10x tunes the agent's default behavior toward
  better software engineering while adding a project context layer.
- Confirmed no live README mentions remain for `Composition`, `references/`,
  `KARPATHY`, `MINIMALIST`, `thin ADR`, `project memory`, `RAG`, `vectors`, or
  `longer context windows`.

The README is now 2,467 words. The previous committed README was 2,517 words.

## Procedure

1. Re-read the `SKILL.md` decision and record-shape instructions.
2. Created `.10x/decisions/equal-first-class-install-paths.md` as the real
   decision record used by the README example.
3. Edited `README.md` to remove Composition, replace the record example, update
   workflow framing, and align the before/after example with the real decision.
4. Deleted both files in `references/`.
5. Ran validation checks.

Observed checks:

```text
python3 autoresearch/validate.py
autoresearch contracts valid

python3 -m unittest discover -s autoresearch/tests
Ran 60 tests
OK

git diff --check
<no output>

local README link check
checked 6 local markdown links
```

## What This Supports Or Challenges

Supports closing the cleanup ticket. The README no longer carries the removed
composition/reference story, and the record example is grounded in actual repo
context instead of a generic fictional auth decision.

## Limits

Historical `.10x/` records may still mention removed reference files as past
inspection context. The live README and current decision record do not depend
on `references/`.
