---
name: loom-review
description: "Run adversarial critique against code changes, behavior changes, tickets, packets, specs, wiki pages, or other review targets. Leave durable critique records with prioritized follow-up."
arguments: "<ticket id | record id | branch | commit | PR | diff target>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-critique
  - loom-tickets
  - loom-specs
  - loom-wiki
---

# /loom-review

You are running **Loom Review**.

Review target:
`$ARGUMENTS`

This command is the explicit critique surface.
It handles both direct artifact critique and packetized implementation review.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-critique`
- `loom-tickets`
- `loom-specs`
- `loom-wiki`

## Goals

- choose a pass split proportional to the target's risk
- decide whether the review needs a packet
- choose named critique profiles proportional to the target's risk
- pressure-test code, behavior, and claims against evidence
- leave behind durable critique records
- reconcile review back into the ticket without hiding the trail

## Choose packetized or direct review

Use `skills/loom-critique/references/review-pass-splitting.md` and
`skills/loom-critique/references/critique-lens.md` as the canonical procedure
references.

### Direct artifact critique

Use when the target is a Loom artifact being reviewed as an artifact: ticket
readiness, plan sequencing, spec acceptance, packet quality, wiki certainty,
evidence strength, or external summary fidelity.

Do not compile a packet by default. Read the artifact and enough owner context
to judge it, then write durable findings when needed.

### Packetized implementation review

Use when reviewing code or behavior changes, especially after a Ralph
iteration.

Compile a critique packet with:

- target ticket
- parent plan or initiative
- relevant spec, research, and evidence
- prior Ralph packet output
- acceptance or claim coverage targets
- git diff or changed-file summary
- required critique profiles

The reviewer should use the packet and the diff as the main review surface.

## Choose the pass split

Decide how many passes this target deserves before starting.

### One-pass review

Use when:

- the target is small
- the risk class is low or medium
- one reviewer can hold the whole target in context
- the harness has no fresh-context subagent transport

### Multi-pass review

Use for medium or high risk targets, or whenever one reviewer would struggle to hold the whole surface without bias. Split the review so each pass enters fresh, with a narrow lens, and cannot carry the blind spots of the other lenses.

Default split:

1. **Correctness and scope.** Does the code or artifact satisfy the ticket and spec? Did the change stay inside its declared scope and write boundary? Are acceptance criteria actually met?
2. **Risk, security, and failure modes.** What breaks at the edges? What assumptions are load-bearing? What security or performance concerns did the implementation silently carry?
3. **Operator clarity and follow-through.** Is the ticket truthful? Is the wiki disposition honest? Will the next agent be able to pick this up cold?

Each pass produces its own critique record, or one consolidated record with clearly separated pass sections. Severity and confidence stay explicit per finding.

Use the named profiles from `skills/loom-critique/references/critique-lens.md`
when the target declares them or when the risk class implies them. Profiles are
lenses, not new owner layers.

For packetized implementation review, if the harness supports subagents or
multiple fresh reviewers, launch the passes in parallel with a critique packet
per pass. If not, run them sequentially as distinct fresh-context passes with
narrow prompts. The transport is flexible; the pass boundaries are not.

## Procedure

1. **Anchor the target.**
   - Identify the code diff, branch, commit, ticket, spec, packet, wiki page, or other target being reviewed.
   - If a ticket is the main owner, read it first.

2. **Classify the review shape.**
   - Use direct artifact critique for Loom artifacts unless the review is broad, high risk, or needs fresh-context isolation.
   - Use packetized implementation review for code or behavior changes.

3. **Gather the minimum governing context.**
   - Read the linked plan, spec, evidence, and any recent packet outputs.
   - Inspect the relevant changed files, tests, or artifact diffs.

4. **Choose and compile packets when needed.**
   - Decide the pass split.
   - For packetized implementation review, compile one critique packet per pass under `.loom/packets/critique/`.
   - For direct artifact critique, skip packets unless the review needs fresh-context isolation.

5. **Review through the chosen lenses.**
   - correctness and scope discipline
   - code quality and maintainability for code targets
   - evidence sufficiency
   - hidden assumptions and failure modes
   - maintenance burden
   - the declared named profiles, such as `protocol-change`,
     `code-change`, `test-coverage`, `api-contract`, `data-migration`,
     `security`, `performance`, or `operator-clarity`

6. **Write findings durably.**
   - Each material finding: short title, severity, confidence, observation, why it matters, follow-up.
   - For code findings, include file and line references when practical.
   - Record a verdict and residual risks.

7. **Reconcile review back into Loom.**
   - Update the ticket status or journal if the critique changes what must happen next.
   - Create follow-up tickets for substantial issues.
   - Do not quietly "fix and forget" major findings.

## Native tools to prefer

- `git status --short`
- `git diff --stat`
- `git diff`
- `git diff --check`
- `rg -n '<symbol | behavior | claim>' <relevant paths>`
- `rg -n '^(id|status|review_target):' .loom/{tickets,critique,specs,wiki,evidence} --glob '*.md'`
- `find .loom/packets/critique -type f -name '*.md' | sort | tail`

## Guardrails

- Do not overstate certainty.
- Do not collapse critique into inline comments.
- Do not silently rewrite ticket truth without leaving the review record.
- Do not let one reviewer's blind spot pass as coverage when the target warranted a split.
- Fairness matters: be skeptical, not performatively harsh.

## Required output

- pass split chosen and why
- direct or packetized review shape, and why
- critique profiles used
- critique record and packet paths or IDs
- prioritized findings with severity and confidence
- code file/line references when applicable
- ticket or follow-up updates performed
- recommended next command
