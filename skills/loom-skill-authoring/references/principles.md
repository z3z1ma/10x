# Principles

## 1. One owner

A skill should own one coherent subsystem.

Owner-layer skills should name the layer they own. Workflow, control-plane,
inner-loop, authoring, support, and shared-grammar skills should say what they
coordinate without pretending to be new truth layers.

## 2. Strong description

The description should make activation discoverable without loading the whole skill first.

Descriptions should include the clearest "use when" trigger and, when relevant,
the owner boundary that prevents the skill from becoming a shadow ledger.

## 3. Operational clarity

A skill should tell the agent what to do, not just what the skill is about.

## 4. Templates when needed

If the skill creates records or pages, include templates.

## 5. Reference depth without bloat

Put nuance in `references/`.
Keep the main skill file strong enough to orient the reader quickly.

## 6. Progressive disclosure with judgment

Do not make `Read In This Order` a bare index.

Name which references are immediate for normal use and which are conditional.
Each entry should say when the agent should open it.
