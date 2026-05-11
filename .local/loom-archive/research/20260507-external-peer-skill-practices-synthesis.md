---
id: research:external-peer-skill-practices-synthesis
kind: research
status: concluded
created_at: 2026-05-07T08:12:05Z
updated_at: 2026-05-07T08:21:41Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:peerpr07
  research:
    - research:external-skill-activation-deep-dive
    - research:skill-template-benchmark-synthesis
  evidence:
    - evidence:peer-skill-practices-validation
  critique:
    - critique:peer-skill-practices-review
external_refs:
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
  everything_claude_code_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/everything-claude-code
  compound_engineering_plugin_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/compound-engineering-plugin
  mattpocock_skills: https://github.com/mattpocock/skills
  addyosmani_agent_skills: https://github.com/addyosmani/agent-skills
---

# Question

Which peer skill and agent-workflow practices should Loom assimilate into its
existing skill corpus, without importing command wrappers, hooks, plugins,
runtime orchestration, or new truth owners?

# Why This Matters

The user clarified the intended direction: Loom stays Loom. The useful external
material should improve the soul of the `skills/` corpus rather than become a
parallel workflow system. This research preserves the direct-read synthesis so the
protocol changes can be reviewed against evidence instead of subagent summaries.

# Scope

This pass covers direct inspection of the cloned peer repositories in
`/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/`:

- `superpowers`
- `everything-claude-code`
- `compound-engineering-plugin`
- prior Matt Pocock and Addy Osmani skill synthesis from linked research

It excludes adopting peer command names, slash-command pipelines, hook
registrations, MCP/plugin mechanics, worktree scripts, issue tracker behavior,
model routing, or persona-agent catalogs as Loom product truth.

# Method

- Used explorer agents only as topology scouts.
- Read the cited external skill, guide, agent, and reference files directly.
- Compared peer patterns to current Loom `skills/` surfaces and constitutional
  decisions `decision:0006` and `decision:0007`.
- Routed candidate improvements to the existing owner layers and skill surfaces.

# Sources

- Source: `superpowers/skills/brainstorming/SKILL.md` lines 10-18, 70-99, 116-145
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful peer workflow evidence; not Loom authority

- Source: `superpowers/skills/writing-plans/SKILL.md` lines 21-43, 106-132, 134-152
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful peer planning discipline evidence; not Loom authority

- Source: `superpowers/skills/verification-before-completion/SKILL.md` lines 10-37, 40-75, 102-139
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful verification discipline evidence; not Loom authority

- Source: `superpowers/skills/writing-skills/SKILL.md` lines 140-180, 374-457, 533-560
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful skill-authoring and pressure-test evidence; not Loom authority

- Source: `superpowers/skills/subagent-driven-development/SKILL.md` lines 8-15, 104-120, 221-261
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful parent/child and review-loop evidence; not Loom authority

- Source: `superpowers/skills/dispatching-parallel-agents/SKILL.md` lines 10-15, 49-83, 167-174
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful parallel-safety evidence; not Loom authority

- Source: `everything-claude-code/the-shortform-guide.md` lines 13-25, 38-47, 76-96, 137-146, 157-184, 200-208
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful distinction between skills and convenience surfaces; not Loom authority

- Source: `everything-claude-code/the-longform-guide.md` lines 147-170, 174-203, 254-286
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful eval, parallelism, and orchestrator guidance; not Loom authority

- Source: `everything-claude-code/agents/planner.md` lines 18-45, 91-99, 188-212
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful planning quality evidence; not Loom authority

- Source: `compound-engineering-plugin/plugins/compound-engineering/skills/ce-brainstorm/SKILL.md` lines 19-42, 76-86, 129-180, 184-224
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful product-pressure and synthesis evidence; not Loom authority

- Source: `compound-engineering-plugin/plugins/compound-engineering/skills/ce-plan/SKILL.md` lines 33-56, 119-188, 190-260
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful planning/readiness evidence; not Loom authority

- Source: `compound-engineering-plugin/plugins/compound-engineering/skills/ce-work/SKILL.md` lines 47-60, 128-190, 191-244, 282-324
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful execution and parent-integration evidence; not Loom authority

- Source: `compound-engineering-plugin/plugins/compound-engineering/skills/ce-code-review/SKILL.md` lines 56-98, 110-127, 173-208
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:12:05Z
  - Freshness risk / recheck trigger: recheck if benchmark clone changes
  - Trust rationale: useful review mode and scope discipline evidence; not Loom authority

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| Copy peer workflows as commands or plugins | CE LFG, ECC hooks/plugins, slash entries | Strong procedural automation | Violates Loom's skills-only, Markdown-native, no-runtime boundary | Rejected |
| Add new Loom workflow layers for brainstorm/plan/work/review | Peer phase pipelines | Familiar lifecycle words | Duplicates initiative/spec/plan/ticket/Ralph/critique ownership | Rejected |
| Assimilate practices into existing skills | Current Loom skills plus peer direct reads | Improves operator behavior while preserving owner truth | Requires careful wording to avoid ceremony bloat | Chosen |
| Treat explorer-agent synthesis as conclusions | Explorer task outputs | Fast topology | Too shallow for protocol decisions | Rejected; direct reads required |

# Evidence Synthesis

- The peer repos are strongest where they pressure the model before it acts:
  one-question-at-a-time clarification, explicit product/assumption probes,
  approach alternatives, and synthesis before a durable artifact lands.
- The reusable Loom version is not a new brainstorm command. It is sharper problem
  shaping in `loom-workspace`, `loom-drive`, and `loom-specs`, with assumptions
  routed into specs, plans, tickets, or research.
- Peer verification language is usefully blunt: no completion claim without fresh
  evidence for that exact claim. Loom already owns this in validation/evidence;
  the corpus should make the gate harder to rationalize away.
- Peer planning guidance reinforces Loom's existing plan/ticket split: plans should
  be specific enough to prevent worker invention, but they should not become
  execution ledgers or implementation scripts.
- Peer subagent guidance is valuable only after translation into Loom's parent/child
  model: subagents are transport; Ralph packets and parent reconciliation own the
  bounded contract and truth merge.
- Peer skill-authoring guidance is especially relevant: descriptions should trigger
  skill loading without summarizing workflow shortcuts, and discipline-enforcing
  skills should be pressure-tested against realistic rationalizations.
- Hook/plugin/worktree/script mechanics are non-transferable as core Loom behavior.
  They can inspire support-boundary wording, but canonical behavior must stay in
  visible Markdown skills, templates, references, and owner records.

# Rejected Options

- Add a new `brainstorm` or `work` skill: rejected because `loom-workspace`,
  `loom-drive`, `loom-specs`, `loom-plans`, `loom-tickets`, `loom-ralph`, and
  `loom-critique` already own the relevant routes.
- Add a command pipeline or hidden validation harness: rejected by `decision:0006`
  and the no-runtime constitution constraints.
- Add mandatory user approval before every spec/plan/ticket: rejected because Loom
  should ask only when owner truth cannot safely infer the next move.
- Treat worktrees as protocol core: rejected because Git isolation belongs in
  `loom-git`/packet execution context when relevant, not as a required runtime.
- Let external agents or peer repositories decide Loom edits: rejected; direct
  reads are evidence only, and Loom owner records decide project truth.

# Null Results

- No peer repo provided a better ontology than Loom's owner-layer model.
- No external plugin/hook/runtime pattern should become a required Loom product
  surface.
- The main gap is not missing artifact kinds. It is sharpening existing skills so
  they pressure assumptions, verification, and parent reconciliation more reliably.

# Conclusions

Assimilate the peer practices as existing-skill improvements:

- `loom-workspace/problem-shaping`: add a compact pressure-check lens for fuzzy
  creative, product, behavior, or architecture requests.
- `loom-drive`: strengthen objective-shaping so delegated autonomy does not skip
  product/assumption pressure.
- `loom-specs`: make problem evidence, beneficiary specificity, current workaround,
  smallest valuable shape, and durability assumptions explicit when relevant.
- `loom-plans`: strengthen readiness around concrete slices, file/write-scope
  clarity, evidence expectations, and plan-specific confidence review without
  turning plans into execution scripts.
- `loom-records` and `loom-evidence`: sharpen evidence-before-claim wording so
  completion, fixed, passing, and ready-to-merge claims require fresh observations.
- `loom-ralph` and `loom-drive`: keep parallel/subagent practices as packetized or
  support-handoff transport with parent reconciliation, not agent-output truth.
- `loom-skill-authoring`: add pressure-scenario validation and workflow-summary
  shortcut cautions as skill review doctrine.

# Recommendations

- Edit existing `skills/` references and templates only; do not add commands,
  hooks, scripts, or runtime assumptions.
- Keep changes compact and positive, aligned with `decision:0007`; add
  counterexamples only where they protect core Loom invariants.
- Validate with direct structural scans, hidden-runtime lexical scans, and a
  mandatory critique because the work changes protocol-authority guidance.

# Open Questions

- Whether a later pass should add project-local pressure scenarios as internal
  examples for maintainers. This should not be product context unless a future
  constitutional decision says so.

# Linked Work

- `ticket:peerpr07`
- `research:external-skill-activation-deep-dive`
- `research:skill-template-benchmark-synthesis`
- `evidence:peer-skill-practices-validation`
- `critique:peer-skill-practices-review`

# Completion Basis

Concluded at 2026-05-07T08:21:41Z. The synthesis was consumed by
`ticket:peerpr07` into existing `skills/` surfaces, with structural validation in
`evidence:peer-skill-practices-validation` and mandatory review in
`critique:peer-skill-practices-review`. Remaining uncertainty is limited to the
open question above about possible future internal examples; it does not block the
current recommendations.
