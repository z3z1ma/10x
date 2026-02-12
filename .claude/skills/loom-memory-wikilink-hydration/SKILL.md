---
name: loom-memory-wikilink-hydration
description: Procedure for implementing or changing Loom memory wikilink hydration with deterministic behavior, UX-visible guarantees, and aligned docs/tests.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-11T21:49:27.460760Z"
  source_episode_ids: "e4839371bc5f19fceb720ecfddf70204dd97ec7a826c7875562727706e171b17,044a58c5c8dcdb13d0e53266c1e4ec08c6994465336f6f6e9b044c0edec52973"
  source_instinct_ids: "hydrate-wikilinks-on-memory-write,memory-golden-tests-for-ux,memory-behavior-change-must-update-readme,memory-hydration-end-to-end-touchpoints,memory-wikilink-hydration-requires-ux-proof"
  tags: "cli-ux,docs,hydration,memory,testing,wikilink"
  updated_at: "2026-02-11T21:49:27.460760Z"
  version: "2"
---
<!-- BEGIN:compound:skill-managed -->
---
name: loom-memory-wikilink-hydration
description: Procedure for implementing or changing Loom memory wikilink hydration with deterministic behavior, UX-visible guarantees, and aligned docs/tests.
---

# Loom memory wikilink hydration

Use this when changing wikilink handling in Loom memory (creation, hydration, stubs, or CLI output).

## 1) Define the contract first

- Specify exact user-visible behavior for `[[wikilinks]]`:
  - normalization rules,
  - when linked notes are created,
  - what output the CLI prints.
- Keep behavior deterministic; avoid order-dependent output.

## 2) Implement across the full memory path

Touch all relevant layers together so behavior stays coherent:

- `src/agent_loom/memory/cli.py`
- `src/agent_loom/memory/core.py`
- `src/agent_loom/memory/hydrate.py`
- `src/agent_loom/memory/models.py`

Do not leave partial logic in one layer only.

## 3) Prove UX behavior and hydration logic separately

- Add/update CLI UX assertions in `tests/test_memory_cli_ux.py`:
  - exact stdout/stderr expectations,
  - exit-code expectations.
- Add/update focused hydration tests in `tests/test_memory_link_hydration.py`:
  - deterministic link extraction/hydration,
  - edge cases around link formatting and stub creation.

## 4) Keep docs in lockstep

- Update `src/agent_loom/memory/README.md` in the same change with examples that match real CLI behavior.
- Ensure docs describe behavior users can observe, not internal implementation details.

## 5) Quality gates

Run:

- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest tests/test_memory_cli_ux.py tests/test_memory_link_hydration.py`

If these pass, run broader tests as needed.

## Done checklist

- Contract is deterministic and explicit.
- CLI/core/hydrate/models stay aligned.
- UX tests and hydration tests both cover the change.
- README examples match actual behavior.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
