---
id: research:skill-template-benchmark-synthesis
kind: research
status: concluded
created_at: 2026-05-07T06:17:26Z
updated_at: 2026-05-07T06:36:17Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  constitution:
    - constitution:main
external_refs:
  mattpocock_skills_engineering: https://github.com/mattpocock/skills/tree/main/skills/engineering
  addyosmani_agent_skills: https://github.com/addyosmani/agent-skills
---

# Question

Which external skill-authoring patterns should Loom adopt while simplifying its own templates and preserving Markdown-native owner-layer truth?

# Why This Matters

The todo-app blue/green comparison showed Loom improving auditability, tests, data safety, and continuation, but not making the visible product quality jump obvious enough to justify all ceremony. The user asked to use that result to improve Loom proper: sharper templates, less section noise, more reasoning pressure, and better skill descriptions.

# Scope

This research compares Loom's `skills/` product surface with two cloned public skill repositories. It focuses on reusable skill and template shape, not on copying runtime hooks, scripts, command wrappers, plugin surfaces, or repository-specific tooling into Loom core.

# Method

- Inspected Loom skill templates and references, especially tickets, packets, specs, evidence, critique, plans, research, workspace, memory, and skill-authoring templates.
- Cloned and sampled `mattpocock/skills` under `skills/engineering`.
- Cloned and sampled `addyosmani/agent-skills` skill anatomy and engineering skills.
- Compared how each corpus activates skills, forces decisions, prevents rationalization, and verifies output.

# Sources

- Source: Loom skills product surface
  - Type: repository code/docs
  - Producer / provenance: local repository
  - Access context: local workspace
  - URL or path: `skills/`
  - Observed at: 2026-05-07T06:17:26Z
  - Version/date/commit: current dirty workspace state at observation time
  - Freshness risk: stale if `skills/` changes materially
  - Recheck trigger: skill/template edits, bootstrap doctrine edits, or package framing changes
  - Trust rationale: `skills/` is the product surface named by `constitution:main`.

- Source: Matt Pocock engineering skills
  - Type: external repository
  - Producer / provenance: `mattpocock/skills`
  - Access context: public GitHub clone
  - URL or path: `https://github.com/mattpocock/skills/tree/main/skills/engineering`; local clone `/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills`
  - Observed at: 2026-05-07T06:17:26Z
  - Version/date/commit: shallow clone current at observation time
  - Freshness risk: upstream can change
  - Recheck trigger: future benchmark pass or external skill design change
  - Trust rationale: high-signal public examples requested by the user; advisory input only, not Loom authority.

- Source: Addy Osmani agent skills
  - Type: external repository
  - Producer / provenance: `addyosmani/agent-skills`
  - Access context: public GitHub clone
  - URL or path: `https://github.com/addyosmani/agent-skills`; local clone `/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills`
  - Observed at: 2026-05-07T06:17:26Z
  - Version/date/commit: shallow clone current at observation time
  - Freshness risk: upstream can change
  - Recheck trigger: future benchmark pass or external skill design change
  - Trust rationale: high-signal public examples requested by the user; advisory input only, not Loom authority.

# Evidence Synthesis

- Loom's strongest scaffolds are owner truth, safety, validation, and closure. The weakest scaffolds are quality judgment, assumptions, alternatives, examples/non-examples, and anti-rationalization pressure.
- Loom's ticket template has become a policy manual disguised as a form. It preserves useful gates, but too many sections and embedded tutorials compete with live ledger truth.
- Ralph, critique, wiki, and drive handoff packet templates preserve important safety metadata, but their body prose repeats shared packet doctrine that belongs in references.
- Loom's spec template is not too large; it is too weak. It needs quality bar, examples/non-examples, decision points, assumptions, and evidence plan.
- Addy Osmani's skill anatomy provides a useful skill-shape pattern: overview, when to use, core process, common rationalizations, red flags, and verification.
- Addy Osmani's spec, planning, frontend, code review, browser testing, and simplification skills are strong because they name common excuses, concrete red flags, and verifiable exits.
- Matt Pocock's engineering skills are strong because they are memorable and operational: tracer bullets over horizontal TDD, feedback loop first for diagnosis, branch selection for prototypes, radically different UI variants, and cleanup of throwaway work.
- External hooks, scripts, plugins, MCP assumptions, and command wrappers should not become Loom core. Their useful parts are the visible skill writing patterns and reasoning scaffolds.

# Rejected Options

- Copy external skills directly into Loom: rejected because Loom has a different owner-layer ontology and should not import unrelated runtime or command assumptions.
- Add a new product-quality owner layer: rejected because specs, research, evidence, critique, tickets, and wiki already own the needed truth types.
- Simplify by deleting ticket gates: rejected because the gates are useful; the problem is template presentation and embedded tutorial bulk.
- Keep all detailed doctrine inline in templates: rejected because it causes copy-fatigue and distracts agents from filling the live record.

# Null Results

None.

# Conclusions

Loom should simplify templates by moving reusable doctrine into references and keeping forms compact. It should simultaneously sharpen reasoning by adding assumptions, quality delta, examples/non-examples, anti-rationalization tables, red flags, and evidence-backed verification to the skills and templates that guide execution.

# Recommendations

- Collapse the ticket template into fewer sections while preserving acceptance, evidence, critique, promotion, acceptance decision, dependencies, and journal gates.
- Treat claim matrices as optional complexity tools, not default ticket sections.
- Strengthen specs with quality bar, examples/non-examples, decision points, assumptions, and evidence plan.
- Add product/UX/visual critique profiles and UI/product evidence shape.
- Add quality delta and assumptions to Ralph packets.
- Make `loom-spike` more concrete with logic-vs-UI branch choice and variant matrices.
- Add common rationalizations, red flags, and verification sections to high-risk skills.
- Improve skill-authoring templates so future skills inherit this structure.

# Open Questions

- Whether future releases should split implementation-oriented skills from owner-layer skills more aggressively, or keep current flat skill distribution and improve descriptions.
- How short the packet templates can become without weakening launch safety for fresh-context workers.

# Linked Work

- `ticket:tmplrs07`

Status note: concluded after `ticket:tmplrs07` promoted the research findings
into skill templates, skill references, and SKILL files.
