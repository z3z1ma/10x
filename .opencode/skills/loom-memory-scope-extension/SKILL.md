---
name: loom-memory-scope-extension
description: Procedure for adding or modifying Loom memory scope kinds without contract drift across code, docs, and recall UX tests.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-12T00:06:35.621586Z"
  source_episode_ids: "883055ed0f173f797d74a5673db40cf642b8191663f6ef312188b017e1d17914,517a7d951e2d4ae1ee98b051a0d26883aa07cc0ac86eccf1300d39920d222962,de39f751f660e27dd86ac6a3f4e9fd7bf4cbc258fdb56bb916aded03026b05fb,18a9ba8e6df0ab3097cac38c141c6b8c7a9a1c5726dd78f58e50d76d9411d37d,ef4e733ef16ebd5c555da29b3edc783929b5dfe33963931871ced9cae09ea142"
  source_instinct_ids: "scope-kind-explicit-prefixes,scope-normalize-paths-cautiously,scope-roundtrip-contract,scope-validation-errors-high-signal,centralize-scope-validation-and-normalization,memory-scope-contract-sync,scope-glob-requires-edge-coverage,memory-scope-change-is-cross-layer,remove-stale-scope-paths-immediately,scope-syntax-migration-needs-compat-tests,ship-scope-ux-with-doc-and-skill-sync,memory-scope-change-sync-docs-and-recall-tests,memory-scope-unknown-kind-explicit-failure-tests,memory-work-targeted-test-then-full-gates,memory-scope-change-requires-contract-docs-tests,recall-note-semantics-must-have-ux-regressions,sync-duplicated-skill-content-in-one-change"
  tags: "compound,docs,memory,scopes,tests"
  updated_at: "2026-02-12T00:06:35.621586Z"
  version: "5"
---
<!-- BEGIN:compound:skill-managed -->
# Loom Memory Scope Extension

Use this procedure whenever you add or change a memory scope kind.

## Steps
1. Update the scope contract in `src/agent_loom/memory/scopes.py`.
   - Add/adjust the canonical scope kind definition.
   - Ensure parsing/normalization/validation paths accept exactly the intended format.
2. Thread the change through recall behavior.
   - Confirm all scope-aware recall/filtering paths apply the new kind consistently.
3. Update docs in `src/agent_loom/memory/README.md`.
   - Document supported scope kinds and examples.
   - Keep wording aligned with actual CLI/runtime behavior.
4. Add regression coverage in `tests/test_memory_recall_notes.py`.
   - Add a positive case proving the new scope participates in recall as intended.
   - Add a negative/edge case that would fail if scope handling regresses.
5. If the skill is mirrored, sync both copies in one PR:
   - `.opencode/skills/loom-memory-scope-extension/SKILL.md`
   - `src/agent_loom/compound/opencode/skills/loom-memory-scope-extension/SKILL.md`

## Done Criteria
- Scope contract, recall behavior, docs, and tests all agree.
- Mirrored skill files (if present) are synchronized.
- No ambiguity remains about accepted scope syntax or recall outcomes.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
