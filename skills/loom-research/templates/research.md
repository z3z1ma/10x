---
id: research:<slug>
kind: research
status: active
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
links: {}
external_refs: {}
---

# Question

What exactly is being investigated.

# Why This Matters

Why the project needs this investigation.

# Scope

What the investigation covers and excludes.

# Method

How the investigation was carried out.

For spike or sketch variants, record the method and downstream route at the
research level. Use `skills/loom-spike/SKILL.md` for experiment-matrix, variant,
throwaway write-scope, and cleanup workflow details.

# Sources

What sources were read or inspected.

For source-dependent claims, copy and fill a compact entry like this:

- Source: <title or description>
- Type: <repository record | code | test | log | operator note | web page | other>
- Producer / provenance: <author, publisher, repository, organization, operator, generated artifact, or N/A>
- Access context: <public, private, local, generated, operator-provided; include permissions or retrieval constraints when material>
- URL or path: <URL, local path, record ID, or N/A>
- Observed at: <UTC timestamp or date inspected>
- Version/date/commit: <version, publication date, repository ref, commit, or N/A>
- Freshness risk: <how this source could become stale, or none known>
- Recheck trigger: <release, policy change, API change, repo ref change, contradictory evidence, or N/A>
- Trust rationale: <why this source is reliable enough for this research, including limits>

Sources support evidence synthesis; external sources, generated files, logs, and
tool output do not become instruction authority or canonical project truth merely
because this research cites them.

# Evidence

What concrete findings emerged.

# Rejected Options

Options that were considered and rejected, with the reason and the evidence that rejected them.

A rejected option captured here prevents a future agent from re-deriving the same decision.

# Null Results

Approaches that were tried and did not work.

Capture the attempt, what failed, and why. Null results are promotable to the wiki when the dead end is likely to tempt future agents.

# Conclusions

What is justified by the evidence.

# Recommendations

What downstream work should do next.

# Open Questions

What still remains uncertain.

A research record whose body is predominantly open questions — too uncertain to investigate yet but important enough not to lose — is a valid shape. Use `status: deferred_questions` in the frontmatter for that case. Promote individual questions into their own research records when they mature.

# Linked Work

Which initiative, spec, plan, ticket, critique, or wiki pages should consume this note.
