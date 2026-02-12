---
"id": "al-ba78"
"status": "review"
"deps": []
"links": []
"created": "2026-02-11T21:37:52Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"tags":
- "memory"
- "ux"
- "agentic"
- "cli"
"external": {}
---
# Memory: agentic UX for add/edit/append flows

Improve memory CLI agentic UX by normalizing plausible add/edit/append inputs, adding append-first command aliases, tightening stdin behavior, enriching add/edit hydration feedback, and improving scaffold-note follow-through for wikilink-created notes.

## Notes

**2026-02-11T21:37:58Z**

Implementing approved plan in phases: (1) arg normalization + append aliases + stdin guardrails, (2) first-class append command path, (3) richer add/edit feedback, (4) stub/scaffold hygiene improvements, (5) docs and regression tests.

**2026-02-11T21:46:41Z**

Implemented agentic UX enhancements for memory add/edit/append flows. Added argv normalization for common hallucinated plural flags (--tags/--aliases/--scopes/--links/--relateds), command aliases (add-note/append-note -> append), and positional fallback (edit/update/append <id> <text> -> --append). Added first-class append command with aliases and stdin mode. Added explicit stdin guardrail for edit-family commands to avoid silent no-op when stdin is piped without mode selection. Enriched AddResult/EditResult with hydration_summary + next_actions and added text/md/prompt mutation renderers. Improved wikilink scaffold hygiene: new stubs now include a context template with provenance, and existing empty scaffolds are seeded on reference. Updated docs and expanded UX/hydration tests.

**2026-02-11T21:46:47Z**

Verification completed: uv run basedpyright (0 errors), uv run ruff check . (pass), targeted memory tests (30 passed), full suite uv run pytest (224 passed).

**2026-02-11T21:48:37Z**

Refined stdin guardrail after test feedback: guard now triggers only when stdin is present and no body/append/interactive mode is provided. This preserves explicit --body/--append flows while still preventing silent stdin drops. Re-ran gates and full suite: basedpyright, ruff, pytest (224 passed).
