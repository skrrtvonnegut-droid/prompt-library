# Authoring and Registering Macros

## The Authoring Rule

Before creating a new artifact, determine:

1. **What is it?** A single-file prompt or a multi-file skill.
2. **What is its classification?** Public, professionally sanitized, private, employer-confidential, or secret.
3. **Where is its canonical home?** This repository is only for publishable capabilities.
4. **Does it already exist?** Search the catalog and repository before creating a parallel version.

Prefer updating, relating, or superseding an existing artifact over duplication.

## Fast Path: Create a Single-File Macro

### 1. Search First

Search `catalog.yml` by:

- outcome;
- domain;
- tags;
- likely alias;
- related artifact names.

If an existing prompt can absorb the new use case without becoming incoherent, update it instead.

### 2. Classify the Material

This is a public repository. The reusable logic may be public even when the source material that inspired it was not.

Remove or generalize:

- names of employers, customers, users, and internal systems;
- tenant IDs, domains, account identifiers, IP addresses, and environment details;
- proprietary process details;
- personal journal material or relationship context;
- credentials, keys, tokens, certificates, recovery codes, and secrets;
- confidential examples copied from source documents.

When sanitization would destroy the capability's meaning, place it in an authorized private overlay instead.

### 3. Choose Identity and Location

Choose:

- a stable dotted artifact ID;
- a domain-aligned path;
- one primary lowercase kebab-case macro alias;
- optional compatibility or discovery aliases;
- concise tags.

Example:

```text
ID:      prompt.work.documentation.change-record-writer
Path:    work/documentation/change-record-writer.md
Macro:   change-record
Domain:  work.documentation
```

Do not put a date or version number in the ID. Git provides version history.

### 4. Create the Artifact

Copy [`../templates/macro-template.md`](../templates/macro-template.md) and replace the placeholders.

Write for a capable collaborator:

- define the outcome;
- identify required and optional inputs;
- preserve important nuance;
- separate source material from instructions;
- provide useful output structure where it improves consistency;
- require uncertainty and missing information to be surfaced;
- remove theatrical filler and brittle prompt tricks;
- include guardrails that are specific to the task.

A prompt should be understandable and editable by a human reader.

### 5. Register It

Add an entry to `catalog.yml` in the same change:

```yaml
  - id: prompt.work.documentation.change-record-writer
    kind: prompt
    name: Change Record Writer
    path: work/documentation/change-record-writer.md
    domain: work.documentation
    summary: Turn implementation notes into a structured change record with scope, risk, validation, rollback, and follow-up.
    macros:
      - change-record
      - write-change-record
    tags:
      - change-management
      - itil
      - documentation
      - risk
    status: active
    classification: Public
```

Macro aliases must be globally unique. The summary should describe the result, not merely repeat the title.

### 6. Review the Invocation

Test the artifact mentally or with a safe sample:

```text
Use macro: change-record
Input: [sanitized sample notes]
```

Check that an agent can determine:

- what source material is required;
- what it should do;
- what it should return;
- when it should stop or ask for missing information;
- what it must not invent or expose.

### 7. Commit Intentionally

The commit or pull request should explain:

- what capability was added or changed;
- why the existing library did not already cover it;
- whether any alias, lifecycle, classification, or path changed;
- how the artifact was reviewed or tested.

## When to Create a Skill Instead

Use a multi-file skill when reliable execution genuinely needs supporting resources such as reference tables, examples, scripts, templates, or validation logic.

Create:

```text
<domain>/<skill-name>/SKILL.md
```

Then place optional resources beneath that folder and register the path to `SKILL.md` with `kind: skill`.

Do not create a directory merely to make a prompt look more important.

## Updating an Existing Artifact

Keep the same artifact ID when:

- wording improves;
- output structure becomes clearer;
- examples change;
- the file moves;
- a new compatible use case is added;
- a macro alias is added.

Consider a new artifact when:

- the outcome has materially changed;
- the audience or operating model requires incompatible instructions;
- the original artifact would become a bundle of unrelated modes;
- independent lifecycle management is needed.

When replacing an artifact, mark the old one `deprecated` and add `replaced_by` rather than deleting history immediately.

## Asking an Agent to Store a Macro

A useful request format is:

```text
Create a public macro in prompt-library.

Name: [human-readable name]
Proposed alias: [optional]
Outcome: [what useful result should exist]
Inputs: [what I will provide]
Constraints: [important guardrails]
Source material: [prompt, notes, or conversation]
```

The agent should search for duplicates, classify and sanitize the content, propose a stable identity, update the canonical artifact and registry together, and use version control rather than creating an untracked copy.
