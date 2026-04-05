# Research Examples

## Example Research Record

Use one durable research note per meaningful research question, option comparison, investigation, or synthesis pass.

## What To Notice In A Strong Research Note

- the question is explicit
- the note explains why the question matters
- evidence is recorded as evidence, not as vibes
- conclusions and recommendations follow from the evidence
- open questions and rejected paths remain visible

## Worked Example

```text
Question
Should packet-consuming work default to reference-first or hermetic mode?

Objective
Choose a default packet style that improves child-run reliability without making packet generation unreasonably heavy.

Scope
Compare the two packet styles for bounded Loom child execution.

Non-goals
- redesign the entire packet model
- eliminate either packet style entirely

Methodology
Compare replayability, context isolation, packet size, child-run reliability, and parent-side regeneration cost across both modes.

Evidence
- hermetic packets preserve more durable context in one artifact
- reference-first packets stay smaller and cheaper to regenerate
- child runs are more reliable when the packet states the missing context explicitly
- stale linked sources are easier to detect in reference-first mode because source refs remain separate from embedded body text

Rejected Paths
- making all packets hermetic by default was rejected because it makes lightweight runs heavier than necessary
- making all packets reference-first was rejected because some replay and isolation cases genuinely need embedded context

Conclusions
- both modes are useful
- hermetic mode is better when replayability or isolation matters most
- reference-first mode is acceptable when the source set is stable and directly readable

Recommendations
- preserve both modes as first-class options
- make the compiler explicit about inclusion type and freshness
- guide operators toward hermetic mode when packet reuse and auditability matter most

Open Questions
- should some subsystems default differently based on typical evidence size and replay needs
```

Why this is strong:

- it separates method, evidence, conclusions, and recommendations
- it preserves rejected paths so later work does not loop blindly
- it gives downstream specs and plans something reusable to inherit

## Weak Example

```text
We looked into packet styles and hermetic seems better overall.
```

Why this is weak:

- it does not preserve the question or method
- the evidence basis is missing
- the downstream implication is unclear
- a later agent cannot tell what would change the conclusion
