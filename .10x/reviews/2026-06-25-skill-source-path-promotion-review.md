Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: SKILL.md
Verdict: pass

# Skill Source Path Promotion Review

## Target

Canonical `SKILL.md` promotion of `candidate-skill-source-path-shape-v1`.

## Findings

- **Pass:** EXP-990 showed a concrete improvement: candidate produced
  directory-shaped source skills in both no-native-dir repetitions while current
  produced a flat `.10x/skills/<slug>.md` source once.
- **Pass:** EXP-991 cleared `.agents` mirror regression. Candidate preserved
  source path shape, byte-equivalent mirror content, governor usage, no
  prohibited skill references, no speculative mirrors, and no implementation
  edits.
- **Pass:** EXP-992 cleared `.opencode` mirror regression with the same manual
  floors.
- **Pass:** EXP-993 cleared `.claude` mirror regression with the same manual
  floors and candidate improved S002 versus current.
- **Pass:** The promoted text is narrow and mechanically checkable: it names
  the `.10x/skills/<skill-slug>/SKILL.md` source path, rejects the flat-file
  source shape, and preserves harness-native exposure copies as mirrors.
- **Constraint:** Do not infer broader behavior from this promotion. It does
  not change skill-vs-knowledge routing, mirror selection, slug selection, or
  the rule that skills stay self-contained.

## Verdict

Pass. Promote the narrow source-path sentence into `SKILL.md`.

## Residual Risk

Weak-request slug stability remains only partially tested because one EXP-990
candidate repetition used a different directory-shaped slug. The canonical
change avoids claiming slug-selection behavior and only fixes source-path shape.
