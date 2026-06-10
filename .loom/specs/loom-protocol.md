# Loom Protocol

Status: active
Created: 2026-06-10
Updated: 2026-06-10

## Purpose and Scope

This spec defines the behavioral surface of Loom: the Markdown protocol for project memory and execution discipline. Loom is the core product of the agent-loom repository. Everything else — Mill, harness integrations, skills packaging — is a client of this protocol.

**Covers:** The execution model (two loops), all record types and their contracts, the directory structure, naming and referencing conventions, the agent behavioral model, and distribution invariants.

**Does not cover:** Loom Mill application behavior (see `mill-*.md` specs), specific harness integration UX, or the content of any particular `.loom/` workspace.

## Execution Model

### Two Loops

The protocol defines exactly two operational modes. An agent is always in one of them.

**Outer Loop — Shaping intent into records.**
- Active when scope, behavior, constraints, terminology, or acceptance criteria are not yet concrete enough to execute against.
- The agent interrogates, challenges, proposes, and externalizes understanding into records as things crystallize.
- Produces: decisions, research, specs, knowledge, and tickets that are ready for execution.

**Inner Loop — Executing bounded work.**
- Active when a ticket exists with clear scope and acceptance criteria.
- Work is carried out by sub-agents scoped to a single ticket.
- The agent reads referenced records, implements within scope, produces evidence, and maintains closure discipline.
- Produces: code changes, evidence, reviews, and ticket status updates.

**Transition criteria:**
- Outer → Inner: A ticket exists with explicit scope and testable acceptance criteria. The referenced records (specs, decisions, knowledge) give sufficient context to execute without guessing.
- Inner → Outer: Work reveals new scope, ambiguity, or a question that cannot be resolved within the current ticket's boundaries. A new ticket may be opened, or the outer loop re-engages.

### Sub-Agent Model

- Sub-agents receive a ticket and its referenced records as working context.
- Sub-agents produce claims, not truth. The parent agent judges where output belongs.
- Sub-agents operate within a single ticket's scope. Out-of-scope observations become new tickets.
- Fresh context per sub-agent. The `.loom/` graph provides continuity, not memory.

## Record Types

Seven record types exist. Each has distinct semantics, required structure, and status lifecycle.

### Common Structure

Every record:
- Is a Markdown file under `.loom/<type>/`
- Starts with grepable headers: `Status`, `Created`, `Updated` (YYYY-MM-DD)
- References other records by relative file path
- Has detailed prose content — not placeholders

### Decisions

**Semantics:** A durable choice involving real tradeoffs, constraints, or surprise. ADR format.

**Required content:**
- Context (situation and forces)
- Decision (what was chosen)
- Alternatives considered (what was rejected and why)
- Consequences (what this enables and restricts)

**Statuses:** `active`, `superseded`

**Lifecycle:** Once accepted, never modified. Supersession creates a new record; the old record moves to `superseded/`.

**Naming:** Descriptive slug (`descriptive-slug.md`). Non-temporal.

### Research

**Semantics:** An investigation where the answer took real work to find. Temporal — can go stale.

**Required content:**
- Question (what prompted the investigation)
- Sources and methods (what was consulted)
- Findings (including null results and dead ends)
- Conclusions (synthesis and implications)

**Statuses:** `active`, `done`, `superseded`

**Naming:** Date-stamped (`YYYY-MM-DD-descriptive-slug.md`). Temporal.

**Storage:** Reference materials go in `.loom/research/.storage/`.

### Specs

**Semantics:** A behavior contract. Describes what should happen — not how to build it.

**Required content:**
- Purpose and scope
- Behavior (concrete scenarios, given-when-then)
- Acceptance criteria (testable, unambiguous)
- Constraints (bounds without dictating implementation)

**Statuses:** `draft`, `active`, `superseded`

**Lifecycle:** Supersession creates a new record; old moves to `superseded/`.

**Naming:** Descriptive slug. Non-temporal.

**Quality bar:** Regeneration-grade — clear enough to rebuild the behavior from the spec alone.

### Tickets

**Semantics:** A bounded unit of work. The bridge between shaping and execution.

**Required content:**
- Scope (in and out)
- Acceptance criteria
- Progress and notes (append-only log)
- Blockers

**Statuses:** `open`, `active`, `blocked`, `done`, `cancelled`

**Additional headers:** `Parent`, `Depends-On`

**Lifecycle:**
- Terminal statuses move to sub-folders: `done/`, `cancelled/`
- Parent tickets are plans describing aggregate work, sequencing, and parallelism
- Child tickets are executable units

**Naming:** Date-stamped. Temporal.

**Invariant:** Before creating a ticket, grep existing tickets (active and done) for prior work.

### Evidence

**Semantics:** A durable observation. Temporal facts that must survive the session.

**Required content:**
- What was observed (raw facts)
- Procedure (how to reproduce)
- What this supports or challenges
- Limits (what this does NOT prove)

**Status:** `recorded` (single status — evidence is immutable)

**Additional headers:** `Relates-To`

**Naming:** Date-stamped. Temporal.

**Storage:** Binary artifacts go in `.loom/evidence/.storage/`.

### Reviews

**Semantics:** Adversarial critique. Challenges work before it's considered solid.

**Required content:**
- Target (what's being reviewed)
- Findings (specific issues with severity)
- Verdict (pass, concerns, fail)
- Residual risk (what remains uncertain)

**Status:** `recorded` (single status — reviews are immutable)

**Additional headers:** `Target`, `Verdict`

**Naming:** Date-stamped. Temporal.

### Knowledge

**Semantics:** Reusable context that accumulates. Shared vocabulary, conventions, procedures, troubleshooting.

**Status:** `active` (delete or update when no longer true)

**Naming:** Descriptive slug. Non-temporal.

**Scope:** One topic per record. Split when it covers unrelated things.

## Directory Structure

```
.loom/
  decisions/
    superseded/
  research/
    .storage/
    superseded/
  specs/
    superseded/
  tickets/
    done/
    cancelled/
  evidence/
    .storage/
  reviews/
  knowledge/
```

**Invariants:**
- Active records live at the top level of their type directory
- Terminal-status records live in named sub-folders (`superseded/`, `done/`, `cancelled/`)
- Storage directories (`.storage/`) hold binary/reference artifacts, never record files
- The directory structure is flat within each type — no nesting beyond the terminal sub-folders

## Naming Conventions

Two naming patterns based on temporality:

| Pattern | Format | Used by |
|---------|--------|---------|
| Temporal | `YYYY-MM-DD-descriptive-slug.md` | tickets, evidence, reviews, research |
| Non-temporal | `descriptive-slug.md` | decisions, specs, knowledge |

**Rationale:** Temporal records represent a moment in time. Non-temporal records represent durable ongoing truth.

## Cross-Referencing

- Records reference each other by relative file path from the repo root (e.g., `.loom/specs/loom-protocol.md`)
- When a record is deleted or renamed, all references to it must be repaired
- The reference graph must remain navigable — gaps are invisible work
- External artifacts that correspond to Loom record types get thin pointer records in `.loom/` to keep the graph complete

## Agent Behavioral Model

When Loom is loaded, the agent's behavior changes in these specific ways:

1. **Externalization discipline.** The agent writes things down as they become clear — not at convenient stopping points. A decision made mid-conversation gets a decision record immediately.

2. **Graph-first orientation.** Before shaping new work, the agent searches existing records: open tickets, knowledge, decisions, research, specs. It builds on what exists rather than re-deriving.

3. **Glossary building.** Domain terms, project conventions, and terms of art become knowledge records when they emerge.

4. **Scope honesty.** Out-of-scope observations become new tickets rather than being held in memory or left as comments.

5. **Closure discipline.** Tickets close when records agree — acceptance criteria met, evidence collected, review findings addressed. Not when the agent "feels done."

6. **Record integrity.** The agent maintains link consistency, moves records to terminal sub-folders on status change, and never modifies immutable records (evidence, reviews, accepted decisions).

## Distribution Invariants

The protocol reaches users through multiple channels. These invariants bind them:

1. **Content identity.** `skills/loom/SKILL.md` is byte-identical to `PROTOCOL.md`. Both include the YAML frontmatter (`name`, `description`) which serves double duty — skill metadata for the ecosystem, and the opening of the canonical protocol file.

2. **Version coordination.** All manifests (`.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `gemini-extension.json`, `package.json`) declare the same version string.

3. **Single source of truth.** `PROTOCOL.md` is canonical. All other distribution artifacts derive from it or point to it.

4. **Channel equivalence.** Regardless of install method (copy-paste, `npx skills add`, marketplace install), the user receives the same protocol content.

5. **Context file reference.** `gemini-extension.json` uses `contextFileName: "PROTOCOL.md"` to point at the canonical file.

## Acceptance Criteria

A conforming implementation of this spec means:

1. `PROTOCOL.md` defines all 7 record types with the semantics, required fields, and statuses listed above.
2. The two-loop execution model is described with explicit transition criteria.
3. The directory structure contract is specified and `.loom/` workspaces that follow the protocol produce the documented layout.
4. Naming conventions distinguish temporal from non-temporal records.
5. Cross-referencing rules specify link maintenance obligations.
6. The agent behavioral model is specific enough that an observer can verify whether an agent "is following Loom" or not.
7. All distribution channels deliver identical protocol content (modulo packaging metadata).
8. Version strings are synchronized across all manifests.

## Constraints

- The protocol must work in any system that supports context injection (text pasted into agent instructions). No runtime dependencies.
- The protocol must not require Loom Mill or any specific tooling to function. A model with file system access is sufficient.
- Records are prose-first. Semi-structured labels support topology extraction; prose carries meaning.
- The protocol must not assume a specific model provider, harness, or interface.
