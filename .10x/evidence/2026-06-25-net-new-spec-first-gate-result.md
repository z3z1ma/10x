Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-greenfield-spec-before-ticket-continuation-live-micro.md, .10x/research/2026-06-25-net-new-spec-first-gate-candidate-batch-live-micro.md, .10x/research/2026-06-25-net-new-spec-first-corrected-formatting-regression-live-micro.md, .10x/research/2026-06-25-post-promotion-net-new-spec-first-sanity-live-micro.md

# Net-New Spec-First Gate Result

## What Was Observed

Four linked live Codex MICRO experiments tested a reported failure mode:
ratified net-new app behavior collapsing directly into one ticket or direct
implementation instead of a spec-first structure.

1. `EXP-20260625-736-greenfield-spec-before-ticket-continuation-live-micro`
   reproduced the current canonical failure.
2. `EXP-20260625-737-net-new-spec-first-gate-candidate-batch-live-micro`
   tested `candidate-net-new-spec-first-gate-v1`.
3. `EXP-20260625-738-net-new-spec-first-corrected-formatting-regression-live-micro`
   filled the exact formatting regression gap from EXP-737.
4. `EXP-20260625-739-post-promotion-net-new-spec-first-sanity-live-micro`
   confirmed the promoted canonical behavior.

Raw artifact directories:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/214-net-new-spec-first-gate-candidate-batch-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/215-net-new-spec-first-corrected-formatting-regression-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/216-post-promotion-net-new-spec-first-sanity-live-micro/`

EXP-736 current-10x failed:

- Wrote `app.js`, `index.html`, and `styles.css`.
- Updated a ticket and created evidence/review.
- Did not create an active specification.

EXP-737 candidate-variant passed the primary:

- Wrote `.10x/specs/static-browser-todo-app.md`.
- Updated parent plan `.10x/tickets/2026-06-25-create-todo-app.md`.
- Created child ticket
  `.10x/tickets/2026-06-25-implement-static-browser-todo-app.md`.
- Wrote no app implementation files.

EXP-737 candidate-variant also changed only `statusLabel.js` for the exact
one-line edit. Its original formatting prompt was confounded by an absent
selector, so EXP-738 corrected that regression.

EXP-738 candidate-variant passed the corrected exact formatting edit:

- Wrote only `styles.css`.
- Final file content:

```css
.button { color: #111; background: #fff; padding: 6px 10px; }
```

EXP-739 post-promotion current-10x passed:

- Wrote `.10x/specs/static-browser-todo-app.md`.
- Updated parent plan `.10x/tickets/2026-06-25-create-todo-app.md`.
- Created child ticket
  `.10x/tickets/2026-06-25-implement-static-todo-app.md`.
- Wrote no app files in SCN-001.
- Changed only `statusLabel.js` for the exact one-line edit.
- Changed only `styles.css` for the corrected exact formatting edit.

## Procedure

Commands:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-greenfield-spec-before-ticket-continuation-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro --require-clean-canonical
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-net-new-spec-first-gate-candidate-batch-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/214-net-new-spec-first-gate-candidate-batch-live-micro --require-clean-canonical
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-net-new-spec-first-corrected-formatting-regression-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/215-net-new-spec-first-corrected-formatting-regression-live-micro --require-clean-canonical
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-post-promotion-net-new-spec-first-sanity-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/216-post-promotion-net-new-spec-first-sanity-live-micro
```

The final post-promotion run intentionally omitted `--require-clean-canonical`
because `SKILL.md` contained the local candidate promotion. Its
`canonical_guard.json` still recorded that `SKILL.md` and
`autoresearch/program.md` did not change during the run.

Manual inspection read raw outputs, reports, file outputs, final messages,
candidate spec/ticket contents, and corrected formatting workspaces.

## What This Supports Or Challenges

This supports promoting the net-new spec-first gate into `SKILL.md`.

It challenges the prior canonical exit wording that allowed clarified net-new
behavior to proceed straight to implementation or one all-purpose ticket.

## Limits

This covers one ratified to-do app continuation and two exact edit regressions
in Codex. It does not prove Claude Sonnet, OpenCode, oh-my-pi, multi-spec
splitting, or multi-ticket implementation/retrospective execution. Those remain
follow-up experiment targets.
