# Recommended Structure

```text
skills/<skill-name>/
├── SKILL.md
├── references/
└── templates/
```

Use `templates/` only when the skill really owns an artifact shape.

Use frontmatter `metadata.skill_kind` to describe the skill surface without
confusing it with owner-layer truth. Owner-layer skills should also name
`metadata.owns_layer`.

Use `references/` for:

- shape details
- review questions
- deeper nuance
- examples that should not bloat the main skill file
