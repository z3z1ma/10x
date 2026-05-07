---
id: research:external-skill-activation-deep-dive
kind: research
status: concluded
created_at: 2026-05-07T07:39:36Z
updated_at: 2026-05-07T07:54:12Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:actvskill
  research:
    - research:skill-template-benchmark-synthesis
external_refs:
  mattpocock_skills: https://github.com/mattpocock/skills
  addyosmani_agent_skills: https://github.com/addyosmani/agent-skills
---

# Question

How should Loom update its skills and paper process so ordinary coding prompts
activate the right Loom skill, while preserving Loom's stronger owner-layer
premise?

# Why This Matters

The README states Loom's core advantage: every engineering thought product has a
place to live, and agents do better work when they are forced through shaped
artifacts instead of collapsing prompt to patch. The external skill repos are
weaker as truth systems but stronger at activation: their descriptions name the
ordinary phrases and coding situations that should trigger each skill.

# Scope

This pass compares the cloned `mattpocock/skills` and
`addyosmani/agent-skills` repositories against Loom's current `skills/` product
surface. It focuses on activation descriptions, routing coverage for common
coding work, missing paper-process shapes, and change classification. It does not
adopt external command wrappers, hooks, MCP dependencies, issue trackers, or
runtime surfaces as Loom truth owners.

# Method

- Read the root Loom README framing around artifact-driven engineering work.
- Inspected external skill README files and representative skill files for
  activation language and workflow coverage.
- Ran read-only subagent inspections focused on Addy-style lifecycle coverage,
  Matt-style engineering skills, and Loom activation gaps.
- Compared findings against current Loom skill descriptions and routing refs.

# Sources

- Source: Loom README and `skills/`
  - Type / provenance: local repository product surface
  - Observed at / version: 2026-05-07T07:39:36Z, dirty workspace
  - Freshness risk / recheck trigger: recheck when `skills/` descriptions or routing references change
  - Trust rationale: source product surface named by `constitution:main`

- Source: `addyosmani/agent-skills`
  - Type / provenance: external repository clone
  - Observed at / version: 2026-05-07T07:39:36Z, shallow clone from prior benchmark pass
  - Freshness risk / recheck trigger: upstream can change
  - Trust rationale: advisory examples requested by user; not Loom authority

- Source: `mattpocock/skills`
  - Type / provenance: external repository clone
  - Observed at / version: 2026-05-07T07:39:36Z, shallow clone from prior benchmark pass
  - Freshness risk / recheck trigger: upstream can change
  - Trust rationale: advisory examples requested by user; not Loom authority

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| Keep Loom descriptions owner-layer-native only | Current skill descriptions | Accurate truth ownership | Weak autoactivation for normal coding prompts | Rejected |
| Copy external lifecycle commands | Addy `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship` | Easy command mental model | Commands become tempting shadow workflow authority | Rejected |
| Add common-task trigger language while preserving owner routing | Broaden skill descriptions and task routing catalog | Improves activation without new layers | Requires careful wording to avoid route tokens | Chosen |
| Add one implementation skill | External incremental/build skills | Clearer build trigger | Duplicates tickets/Ralph/debug/spike and creates new workflow owner | Rejected for now |

# Evidence Synthesis

- Addy's skills are strong at broad activation. Descriptions use ordinary triggers such as "implementing any logic," "changing any behavior," "building or debugging anything that runs in a browser," "before merging any change," and "making any code change."
- Addy's lifecycle table is discoverable because it maps normal phases to skill families. Loom has a stronger layer model, but its routing docs are mostly owner-truth-oriented rather than prompt/task-oriented.
- Matt's skills are strong at phrase-level triggers and concrete engineering shapes: "debug this," "red-green-refactor," "prototype this," "try a few designs," "convert a plan into issues," and "understand how this fits into the bigger picture."
- Matt's domain language and grilling skills show a gap in Loom's activation/paper process: Loom owns wiki/spec/research, but it does not foreground shared terminology and one-question alignment as strongly as its premise permits.
- Loom's closed `ticket:tmplrs07` improved rationalizations, red flags, and verification, but descriptions still often say "Maintain X" or "Preserve Y" instead of naming the coding tasks that should trigger the skill.
- Current change classes cover protocol, behavior, data, security, and release work, but common coding work such as behavior-preserving refactors, test-only work, dependency/tooling changes, performance work, and UI/product changes are not first-class enough in the classification path.
- The missing shape is not a new truth owner. It is an activation/routing surface that maps ordinary prompts to existing owner layers, plus a lightweight local execution paper process under ticket truth.

# Rejected Options

- Add command wrappers as canonical routes: rejected because Loom truth belongs in owner records, not command surfaces.
- Add an implementation owner layer: rejected because tickets already own live execution and Ralph owns bounded child contracts.
- Add a domain-language record kind: rejected because accepted reusable language belongs in wiki/spec/research depending on truth type.
- Copy external skill text wholesale: rejected because Loom has a different ontology and trust boundary.

# Null Results

No need to revisit the previous conclusion that Loom's owner-layer premise is
stronger. The gap is activation discoverability and practical coding-task route
coverage, not the core model.

# Conclusions

Loom should keep its owner-layer model but make skill activation descriptions
broad and task-language-rich. The paper process should explicitly cover common
coding prompts with a task-routing catalog and a local execution loop under ticket
truth. Change-class vocabulary should make common coding work visible so tickets,
evidence, critique, and packets can fail closed without guessing from vibes.

# Recommendations

- Broaden every core skill description to include common coding prompts and plain-language trigger aliases.
- Add `skills/loom-workspace/references/task-routing-catalog.md` mapping common requests to owner routes.
- Add `skills/loom-tickets/references/local-execution.md` for tiny/single bounded implementation under ticket truth.
- Add or document first-class change classes for code structure, validation instrumentation, dependency/tooling, performance-sensitive, and UI/product work.
- Update `loom-skill-authoring` guidance so future skills write descriptions for activation, not just ownership.
- Update read orders so the routing catalog and local execution process are discoverable.

# Open Questions

- Whether a future release should add a dedicated shared-language workflow page under wiki/codemap/spec guidance. This pass can improve routing without adding that larger workflow.
- Whether README's skill map should be updated after the source skill descriptions settle.

# Linked Work

- `ticket:actvskill`

Status note: concluded after `ticket:actvskill` promoted the findings into skill
descriptions, routing references, ticket local-execution guidance, change-class
guidance, wiki shared-language guidance, and skill-authoring guidance.
