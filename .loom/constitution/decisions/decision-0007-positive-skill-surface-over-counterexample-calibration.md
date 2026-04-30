---
id: decision:0007
kind: decision
status: active
created_at: 2026-04-30T17:17:21Z
updated_at: 2026-04-30T17:17:21Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  decision:
    - decision:0006
---

# Decision

Loom's product-facing skills should teach positive structure, owner boundaries,
default routes, and done conditions rather than exhaustive counterexample
calibration.

The `skills/` tree remains the only product surface. Internal examples can help
maintainers visualize routes and spot drift, but examples are not loaded into the
normal installed-agent context and must not be treated as product guidance or a
second source of truth.

Loom should provide a type system and transaction grammar. The frontend model and
human operator compose that grammar from the user's verbs, the current owner
records, and the skill boundaries.

# Why This Decision Exists

The skill surface is now broad enough that adding many "when not to use this"
counterexamples would make the product harder to reason about, especially for
weaker models. Too much nuance in the product surface creates branchy,
incoherent instructions and encourages agents to classify edge cases instead of
following the owner model.

The better product shape is a clear positive case: each skill states what it
owns, when it is the right route, what it must not own, and what done means. The
operator and frontend model provide the small amount of situational judgment
needed to compose those pieces.

# Alternatives Considered

- Add extensive calibration counterexamples to the skills. Rejected because this
  would make the installed product surface more verbose, branchy, and harder for
  weaker models to apply consistently.
- Make `examples/` a normative teaching surface. Rejected because examples are
  internal visualization and review fixtures; they are not loaded into the normal
  agent context and are not the product surface.
- Add a runtime router or command layer to decide which workflow applies.
  Rejected because Loom is intentionally not a runtime, product CLI, daemon, or
  hidden workflow engine.
- Make skills extremely terse and rely entirely on model judgment. Rejected
  because Loom still needs visible owner boundaries, default routes, and done
  conditions to keep work recoverable.

# Consequences

- Skill changes should prefer positive guidance and core invariants over long
  lists of counterexamples.
- Add narrow prohibitions or counterexamples to skills only when they protect a
  core invariant, such as truth ownership, ticket ledger authority, scope, or
  anti-runtime boundaries.
- Internal examples may be used to visualize workflows and detect drift, but they
  do not define Loom semantics and must not be referenced as installed context.
- Product-surface review should ask whether new prose makes the skill easier to
  compose, not whether it covers every possible edge case.
- AGENTS guidance and public docs should keep `examples/` separate from the
  skills-only product surface.

# Revisit Conditions

Revisit if repeated real-world use shows that positive guidance plus owner
boundaries is insufficient for safe operation, or if a target harness materially
changes how skills are loaded such that examples become an explicit product
surface by constitutional decision.

# Supersession

This extends `decision:0006` by clarifying that `skills/` is not only the
distribution surface but also the product guidance surface. It narrows older
language that treated examples as canonical protocol corpus: examples remain
internal review fixtures, not product context.
