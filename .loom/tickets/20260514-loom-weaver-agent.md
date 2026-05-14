# Add Loom Weaver Agent

ID: ticket:20260514-loom-weaver-agent
Type: Ticket
Status: open
Created: 2026-05-14
Updated: 2026-05-14
Risk: high - adds a new model-visible agent persona and cross-harness adapter surfaces with a strict write-boundary requirement.
Priority: high - follows completed direct-agent research and operator request to make Loom shaping directly invocable.

## Summary

Add a Loom Weaver agent surface to Agent Loom. Loom Weaver is an explicit shaping persona that writes only under `.loom/`, challenges operator ideas, presents options with recommendations, and creates or updates the appropriate Loom records instead of implementing source changes.

Single closure claim: Agent Loom ships a Loom Weaver agent/persona whose behavior satisfies `spec:loom-weaver-agent` and whose supported-harness exposure matches `research:20260514-direct-interactive-agent-surfaces` without claiming unsupported universal `@` semantics.

## Related Records

- `spec:loom-weaver-agent` - owns the Loom Weaver behavior contract, write boundary, routing requirements, scenarios, and quality bar.
- `research:20260514-direct-interactive-agent-surfaces` - source-backed comparison of OpenCode, Claude Code, Gemini CLI, Cursor, and Codex agent invocation surfaces.
- `AGENTS.md` - contributor constraints for product-surface leakage, package shape, adapter entrypoints, and validation commands.
- `INSTALL.md` - current install matrix that may need human-facing invocation notes after agent surfaces are added.

## Scope

May change:

- Core package files needed to define and ship the Loom Weaver prompt or agent definitions, likely under a new `loom-core/agents/`, `loom-core/prompts/`, or equivalent package-owned directory.
- OpenCode Core entrypoint `loom-core/loom-core.mjs` if needed to register a `loom-weaver` agent with both user-switchable primary-agent behavior and explicit invocation behavior.
- Core native adapter manifests and extension files when they can expose agent, rule, profile, or subagent surfaces: `loom-core/.claude-plugin/plugin.json`, `loom-core/.cursor-plugin/plugin.json`, `loom-core/.codex-plugin/plugin.json`, `loom-core/gemini-extension.json`, and related package-local files.
- Core package metadata such as `loom-core/package.json` when new shippable prompt or agent files must be included in package artifacts.
- Human-facing docs that explain how to invoke Loom Weaver per harness, including `INSTALL.md`, package READMEs, or root docs that already describe install/use flows.
- This ticket, `spec:loom-weaver-agent`, new evidence records, and any audit or Ralph packet records needed for implementation and review.

Must not change:

- Do not make Loom Weaver the default startup agent automatically unless a separate operator-approved decision changes `spec:loom-weaver-agent`.
- Do not add app runtime infrastructure, daemons, databases, dashboards, or helper CLIs.
- Do not edit `loom-playbooks/` unless a documentation cross-reference is necessary; Loom Weaver belongs to Core unless implementation proves otherwise.
- Do not duplicate the full `using-loom` doctrine into the Loom Weaver prompt. Keep the agent prompt focused on the Weaver posture and route into existing Loom skills/surfaces.
- Do not claim Cursor or Codex support `@<agent>` custom-agent invocation unless newer source-backed research proves it.
- Do not loosen the Loom Weaver runtime write boundary beyond `.loom/`.
- Do not put contributor-only package smoke, adapter mechanics, dogfood state, or repository workflow explanations into model-visible Loom Weaver instructions.

System-shape constraints:

- Treat Loom Weaver as an optional named persona/surface layered on top of Loom Core, not as a replacement for `using-loom` activation doctrine.
- Keep one canonical Loom Weaver behavior source or an explicitly documented minimal duplication strategy so OpenCode, Claude, Gemini, Cursor, and Codex surfaces do not drift.
- Where a harness cannot enforce `.loom/`-only writes mechanically, the prompt and docs must still state the behavioral boundary and the validation/audit should call out the enforcement limit.
- Where a harness only supports proxy-mediated or non-`@` invocation, expose the closest honest surface and document the exact invocation syntax.

Likely harness-specific direction from the research:

- OpenCode: expose `loom-weaver` as the strongest surface, preferably a primary agent that is user-switchable by Tab/keybind and, if supported, also `@` invokable through `mode: all` or equivalent documented configuration.
- Claude Code: expose a plugin or standalone agent named `loom-weaver` that supports `@agent-<name>` / typeahead one-shot invocation and `claude --agent <plugin-scoped-name>` main-session use.
- Gemini CLI: expose an extension subagent or prompt surface that supports `@loom-weaver` one-shot invocation; document `GEMINI_SYSTEM_MD` only if providing a main-session override recipe.
- Cursor: expose the closest supported direct invocation as `/loom-weaver` custom subagent and/or rule-backed main-Agent guidance; document slash syntax, not `@` syntax.
- Codex: expose a profile/instruction-file recipe for direct persona switching and, only if useful, a custom agent TOML for natural-language spawned subagents; do not rely on `@<agent>`.

First likely Ralph packet:

- Compile a source-backed implementation packet that reads `spec:loom-weaver-agent`, `research:20260514-direct-interactive-agent-surfaces`, current Core entrypoints/manifests/package files, and official harness docs as needed; then implements the smallest complete Core Loom Weaver surface and updates docs/validation evidence.

## Acceptance

- ACC-001: A canonical Loom Weaver behavior source exists and matches `spec:loom-weaver-agent`: `.loom/`-only writes, shaping-first posture, adversarial challenge, option presentation with recommendations, correct Loom surface routing, and honest evidence/audit limits.
  - Evidence: source inspection plus targeted grep over the canonical prompt/agent files for `.loom/` write boundary, shaping language, challenge language, options/recommendations language, and Loom surface routing.
  - Audit: review should challenge whether the prompt duplicates `using-loom` doctrine or leaks contributor-only package details.

- ACC-002: OpenCode exposes Loom Weaver as a directly user-selectable agent surface, with both primary-agent switching and explicit invocation support when OpenCode configuration supports both.
  - Evidence: source inspection of OpenCode Core configuration plus Core smoke/pack checks; if `mode: all` or equivalent is used, cite the source/docs that prove it supports both primary and subagent invocation.
  - Audit: review should challenge whether OpenCode agent registration is shipped in the package artifact and does not interfere with existing skill registration/bootstrap.

- ACC-003: Claude Code exposes Loom Weaver through a Core plugin agent or documented agent definition that can be invoked explicitly and can run as the main session agent.
  - Evidence: source inspection of Claude agent files/manifests and, after manifest changes, `claude plugin validate "$PWD/loom-core"` when available.
  - Audit: review should challenge plugin-scoped naming, security limitations on plugin agents, and whether docs overclaim automatic/default activation.

- ACC-004: Gemini CLI exposes Loom Weaver through the strongest honest extension-supported surface and documents exact invocation semantics.
  - Evidence: source inspection of Gemini extension files plus `gemini extensions validate "$PWD/loom-core"` and root/playbooks validation if touched.
  - Audit: review should challenge whether the implementation incorrectly treats a subagent as a main prompt, or whether any `GEMINI_SYSTEM_MD` recipe replaces core prompt behavior without warning.

- ACC-005: Cursor support uses documented Cursor semantics and does not claim `@<agent>` custom-agent invocation.
  - Evidence: source inspection of Cursor plugin/rule/agent files plus `git diff --check`; if plugin manifest changes are made, inspect the manifest against Cursor docs/source-backed research.
  - Audit: review should challenge whether `/loom-weaver`, rules, and optional subagent behavior are described honestly.

- ACC-006: Codex support uses documented Codex semantics and does not claim `@<agent>` custom-agent invocation.
  - Evidence: source inspection of Codex plugin docs/config/profile/agent artifacts and any relevant pack/check output; docs must name natural-language spawning, `/agent` thread switching, or profile use as applicable.
  - Audit: review should challenge whether Codex support is overstated because current plugin docs do not document plugin-shipped custom agents.

- ACC-007: Human-facing docs explain how to invoke Loom Weaver per supported harness without turning docs into a second source of model behavior.
  - Evidence: source inspection of updated docs and grep showing model-critical behavior remains in shipped agent/prompt surfaces, not only in README/INSTALL prose.
  - Audit: review should challenge docs for universal syntax claims, default-agent claims, and product-surface leakage.

- ACC-008: Package and Markdown validation appropriate to touched files passes.
  - Evidence: at minimum `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check`; additionally run Claude/Gemini validators after their manifests/extensions change, and run Playbooks checks only if Playbooks files are touched.
  - Audit: review should challenge whether package `files` include new shippable agent/prompt artifacts and whether validation omitted a touched adapter surface.

- ACC-009: A fresh review or audit pass challenges the Loom Weaver prompt and adapter exposure before closure.
  - Evidence: `loom-audit` record or Ralph review packet output covering prompt safety, `.loom/` write boundary, harness support honesty, package inclusion, and product-surface leakage.
  - Audit: this criterion requires separate audit/review; do not close on implementation self-report alone.

## Current State

Open and ready to start. The behavior contract now lives in `spec:loom-weaver-agent`, and the harness capability research lives in `research:20260514-direct-interactive-agent-surfaces`. The first implementation packet should verify exact adapter file shapes from current harness docs/source before editing, then add the smallest complete Core Loom Weaver surface with evidence and review.

No implementation evidence exists yet. Closure requires source inspection, package/manifest validation appropriate to touched files, and a fresh audit/review pass.

## Journal

- 2026-05-14: Created ticket from operator request to add a Loom Weaver agent that writes only under `.loom/`, shapes context with users, challenges weak ideas, presents options with recommendations, and creates the appropriate Loom records. Linked `spec:loom-weaver-agent` and `research:20260514-direct-interactive-agent-surfaces` as the behavior and harness constraints.
- 2026-05-14: Resolved Loom Weaver spec decisions with operator selections: explicit-only default posture, partial Codex support, and Cursor slash invocation accepted with honest syntax documentation.
