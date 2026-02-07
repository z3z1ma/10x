---
name: compound-cli-contract-testing
description: Keep Compound CLI behavior deterministic and protected by focused contract tests when refactoring src/agent_loom/compound/cli.py or src/agent_loom/compound/sync.py.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-07T22:03:48.297745Z"
  source_episode_ids: "643f2dcff84c8a8af59de242d82e15e26615ee7bceefa00b773e2968864fc4ed"
  source_instinct_ids: "compound-cli-change-requires-contract-tests,docs-touch-means-ux-claims-check,large-deletion-refactor-requires-behavior-audit"
  tags: "cli,compound,contracts,determinism,testing"
  updated_at: "2026-02-07T22:03:48.297745Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Compound CLI Contract Testing

Use this when changing Compound CLI behavior (especially refactors) so UX + artifacts stay deterministic.

## Scope
- Applies to: `src/agent_loom/compound/cli.py`, `src/agent_loom/compound/sync.py` (and any Compound command wiring they influence)
- Goal: deterministic output, stable semantics, and regression coverage

## Checklist
1. Identify the contract surface
- CLI: command names, flags, help text, exit codes, stderr vs stdout
- Output: headings/labels, ordering, whitespace, and any user-visible paths
- Artifacts: any generated/installed files, rendered templates, or computed lists

2. Make determinism explicit
- Sort lists before printing
- Use stable iteration order (avoid depending on dict insertion order unless guaranteed by construction)
- Avoid timestamps/randomness in outputs unless explicitly part of the contract

3. Update/add focused contract tests
- Prefer extending existing tests that already pin Compound behavior (start by checking `tests/test_compound_install.py`)
- Test both:
  - happy path output/content
  - failure modes (bad args, missing files, partial state) with intentional messages and exit codes

4. Keep docs aligned when you touch them
- If you edit `README.md` or `LOOM.md`, verify any example commands/outputs still match the contract behavior
- Prefer language that mirrors contract-tested output when practical

## Verify (local gates)
- `uv run basedpyright`
- `uv run ruff check .`
- `uv run pytest tests/test_compound_install.py` (plus any new/adjacent tests you add)

## Done when
- Contract tests pin the behavior you intended to preserve
- Gates are green
- No accidental UX drift (output/exit codes) from the refactor
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
