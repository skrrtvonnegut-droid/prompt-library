# Prompt Library

A public, versioned registry of reusable AI prompts, named macros, and composable skills for technical work, documentation, analysis, learning, writing, and creative exploration.

Most artifacts here began as something real that needed doing: turning rough notes into durable documentation, making dense technical material understandable to a particular audience, tracing decisions and risks, learning a tool, or getting an AI assistant to behave more like a thoughtful collaborator than a very confident autocomplete.

This repository is not meant to become a heap of clever incantations. It is a small capability system: human-readable instructions, stable identities, explicit invocation names, lifecycle metadata, and Git history.

## The Three Layers

- **Prompt** — the canonical instruction text stored in Markdown.
- **Macro** — a stable, human-friendly alias that invokes a prompt, such as `kb-writer` or `prompt-engineer`.
- **Skill** — a larger capability contract that may include a prompt, supporting references, examples, scripts, or other resources.

A prompt can expose one or more macros without duplicating its content. The Markdown file remains canonical; `catalog.yml` tells agents how to find and invoke it.

## Invoking a Macro

Use an explicit invocation when you want deterministic behavior:

```text
Use macro: kb-writer
Audience: non-technical plant managers
Source material: [paste text or attach documents]
```

```text
Invoke prompt.work.documentation.raw-notes-to-sop with these notes:
[paste notes]
```

```text
Find a macro for turning a group-chat discussion into a cyber-risk decision record.
```

Agents should resolve an exact artifact ID first, then an exact macro alias, and fetch the canonical Markdown file before applying it. The full retrieval and execution contract is defined in [`AGENTS.md`](AGENTS.md).

## What You Will Find Here

- **Technical and systems work** — Microsoft 365, identity, automation, administration, troubleshooting, and operational analysis.
- **Governance and documentation** — structured records, registries, assessments, runbooks, SOPs, knowledge articles, and action plans.
- **Prompt engineering** — reusable frameworks for turning rough intentions into clear instructions.
- **Analysis and synthesis** — extracting themes, comparing evidence, surfacing risks, and tracking decisions.
- **Learning** — tutor and learning-lab prompts designed to build understanding rather than merely produce answers.
- **Writing and reflection** — journaling, rewriting, creative work, and nuanced inquiry.

## Repository Structure

```text
prompt-library/
├── AGENTS.md                 # Agent retrieval, execution, and safety contract
├── catalog.yml               # Machine-readable registry and macro aliases
├── docs/
│   ├── AUTHORING.md          # How to create, classify, and register artifacts
│   └── SKILL-CONTRACT.md     # Prompt, macro, and skill specification
├── schemas/
│   └── catalog.schema.json   # Editor-readable catalog validation contract
├── templates/
│   ├── macro-template.md     # Scaffold for a new single-file macro
│   └── universal-prompt-engineer.md
├── work/
│   ├── documentation/
│   ├── governance/
│   ├── microsoft-365/
│   └── reporting/
├── writing/
│   ├── journaling/
│   ├── rewriting/
│   └── creative-writing/
├── learning/
└── meta/
```

## Catalog

`catalog.yml` is the machine-readable registry. Every published capability receives:

- a stable artifact ID;
- a canonical repository path;
- a domain and concise summary;
- one or more globally unique macro aliases;
- lifecycle and classification metadata;
- search tags.

The catalog describes and routes to artifacts; it does not copy their prompt text. `schemas/catalog.schema.json` defines the catalog shape for editors and automation.

## Design Principles

- **One truth, many references** — prompt content has one canonical file; catalogs, aliases, and documentation point to it.
- **Explicit activation by default** — named macros are easier to audit than invisible keyword magic.
- **Outcome over theatrics** — useful context, constraints, and success criteria matter more than elaborate roleplay.
- **Stable identity** — IDs and aliases should survive file moves and wording revisions.
- **Visible uncertainty** — artifacts should surface gaps, assumptions, conflicting evidence, and unresolved questions.
- **Public by construction** — this repository must not contain personal-private, employer-confidential, or secret material.

## Public Boundary

This repository is public. Only material classified **Public** or intentionally sanitized for a **Professional Portfolio** belongs here.

Do not store passwords, tokens, certificates, private keys, recovery codes, personal-private context, employer-confidential details, proprietary source material, or prompts that depend on those details. Private or organization-specific capabilities belong in a private overlay that references this public foundation.

## Adding a Macro

Invoke the self-hosting authoring macro:

```text
Use macro: create-macro
Source material: [rough request, conversation, or existing prompt]
```

Or start manually with [`templates/macro-template.md`](templates/macro-template.md), then follow [`docs/AUTHORING.md`](docs/AUTHORING.md). Before creating anything new, search the catalog for an existing capability that should be updated, related, or superseded instead.

## Status

This registry is built iteratively. Artifacts are reviewed before publication, especially when they originated in professional or personal work. Git history preserves how each capability evolves without requiring competing durable copies.
