Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/done/2026-06-28-polish-readme-for-public-launch.md, README.md

# README Public Launch Polish

## What Was Observed

The public README was rewritten as a tighter launch page while preserving the
project's core claims:

- 10x is a self-contained Markdown instruction set.
- Vercel Skills CLI and direct copy-paste are both first-class install paths.
- `.10x/` durable records are the project-memory mechanism.
- `autoresearch/` is optional credibility/evaluation infrastructure, not the
  product surface.

The revised README is 2,250 words, down from 2,506 words before the pass, while
adding first-screen install guidance, an autoresearch credibility section, and
explicit frontmatter guidance for copy-paste vs skill-directory installs.

## Procedure

1. Re-read `SKILL.md`, `README.md`, and relevant `autoresearch/README.md`
   sections.
2. Opened `.10x/tickets/2026-06-28-polish-readme-for-public-launch.md`.
3. Spawned two fresh-context reviewers before editing and one post-edit reviewer
   after the main rewrite.
4. Rewrote `README.md` to move practical value and install guidance above the
   essay, compress repeated explanation, add a concrete behavior example, add
   an autoresearch/evaluation section, and clarify install modes.
5. Verified the Vercel Skills CLI support claim from the upstream README, which
   says the CLI supports OpenCode, Claude Code, Codex, Cursor, and 68 more.
6. Ran local checks:

```text
python3 autoresearch/validate.py
python3 -m unittest discover -s autoresearch/tests
git diff --check
local README link check script
```

Observed outputs:

```text
autoresearch contracts valid
Ran 60 tests in 19.601s
OK
checked 9 local markdown links
```

## What This Supports Or Challenges

Supports closing the README public-launch polish ticket. The README now has a
faster first-screen pitch, equal install paths, an explicit "just Markdown"
philosophy, and a concise explanation of autoresearch as live-trial-backed
improvement infrastructure.

Supports the 70+ agent installer claim when attributed to the Vercel Skills CLI,
not to this repository alone.

## Limits

`npm` is not installed in this container, so `npx skills add z3z1ma/10x` was not
executed locally. The command shape and 70+ support claim were checked against
the Vercel Skills CLI documentation instead.
