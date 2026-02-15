---
"id": "al-9bf8"
"status": "open"
"deps":
- "al-18ec"
- "al-58c0"
- "al-f968"
"links": []
"created": "2026-02-15T19:15:07Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-0463"
"tags":
- "sprint:Public-Launch-Architecture-Cleanup"
- "architecture"
- "quality"
- "launch"
"external": {}
---
# Add architecture guardrails + launch readiness checks

## Objective alignment
After refactors land, we need enforceable guardrails so duplication and oversized CLI/core files do not regress before public launch.

## Scope
- Add/update architecture guard documentation and tests/checks that enforce:
  - shared CLI output primitives are reused,
  - decomposed module boundaries stay intact,
  - hotspot files do not regrow uncontrolled.
- Update relevant READMEs/docs for team/workspace/ticket architecture expectations.

## Non-goals
- No new product features.
- No broad documentation rewrite outside affected modules.
- No replacement of existing test strategy.

## Implementation plan
1. Add architecture notes in module READMEs and/or targeted docs sections describing new boundaries and allowed responsibilities.
2. Add lightweight regression checks (tests or scripted assertions) for critical guardrails, such as:
   - no duplicate local payload/emit helper blocks in targeted CLIs,
   - expected module import paths for command handlers,
   - optional file-size threshold checks for known hotspots.
3. Ensure guardrails are deterministic and low-noise to avoid flaky failures.
4. Run full quality gates and adjust checks for stability.

## Verification
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest`

## Acceptance criteria
- Guardrails exist and fail when core architecture invariants regress.
- Documentation clearly states new module boundaries for maintainers.
- Full gates pass with guardrails enabled.

## Risks / edge cases
- **Risk:** over-strict guardrails create brittle failures.
  - **Detection:** noisy failures on benign refactors.
  - **Mitigation:** assert invariants (behavioral/structural), not incidental formatting.
- **Risk:** docs and checks drift apart.
  - **Detection:** guardrail failures contradict documented expectations.
  - **Mitigation:** co-locate docs with guard checks and update together.
