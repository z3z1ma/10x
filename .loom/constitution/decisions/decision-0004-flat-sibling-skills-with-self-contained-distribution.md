---
{
  "created_at": "2026-04-01T18:07:00Z",
  "id": "decision:0004",
  "kind": "decision",
  "links": {
    "roadmap": [
      "roadmap:bootstrap-the-markdown-first-protocol-corpus"
    ]
  },
  "repository_scope": {
    "kind": "repository",
    "repository_id": "repo:root"
  },
  "schema_version": 1,
  "status": "active",
  "updated_at": "2026-04-01T18:07:00Z"
}
---

# Decision

Loom skills in this repository remain flat sibling subsystems, and each distributed skill bundle must stay self-contained even when shared helper code is copied in during assembly.

No skill should depend on hidden inheritance from another skill in order to function correctly when loaded.

# Why This Decision Exists

`CONSTITUTION.md` locks in both the flat sibling skill rule and the self-contained distribution rule because they keep subsystem behavior visible, inspectable, and portable across harnesses.

The current repository already implements that choice through ten top-level skills under `src/skills/`, skill-local references, skill-local `scripts/` directories, and `build/assemble-skills.py` copying shared helper code into each bundle rather than creating a central runtime dependency.

# Alternatives Considered

- nested or inheriting skills with hidden parent behavior
- a central runtime package that every loaded skill must import to work correctly
- allowing build assembly to become the true owner of behavior while the skill Markdown stays thin

# Consequences

- every skill should remain understandable from its own `SKILL.md`, references, and bundled scripts
- shared helper code is acceptable only as packaging support for already-published behavior
- build assembly remains a distribution mechanism, not a new ontology layer
- future skill additions should preserve flat routing and self-contained operation unless a later constitutional change explicitly reopens this choice

# Supersession

This supersedes any assumption that hidden skill inheritance, central runtime coupling, or assembly-time indirection may become the normal way skills gain their operating behavior.
