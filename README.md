# Prompt Library

A versioned registry of reusable prompts, skills, macros, and authoring templates for technical work, automation, documentation, analysis, learning, writing, and creative exploration.

Most artifacts here began as something that needed to work more than once: turn messy notes into usable documentation, explain a complex system without losing the important parts, create a repeatable workflow, or help an AI assistant behave more like a capable collaborator than a very confident autocomplete.

The library is both human-readable and machine-discoverable. Markdown files contain the canonical instructions; `catalog.yml` provides stable identity, aliases, lifecycle, classification, and routing metadata.

## Artifact Types

| Type | Use it for |
| --- | --- |
| **Prompt** | A reusable instruction set that runs against supplied inputs. |
| **Skill** | A routed capability with a procedure, dependencies, guardrails, and an output contract. |
| **Macro** | A short named command that expands into a prompt or skill invocation. |
| **Template** | A scaffold for authoring a new registry artifact consistently. |

The distinction is about operational depth, not prestige. A good macro may be three lines. A good skill may coordinate several tools. Both should remain understandable by a human.

## Using the Registry

A compatible assistant can resolve artifacts by stable ID, alias, name, or intent.

```text
/skills documentation
/skill kb-writer
/prompt prompt.work.documentation.design-document
/prompt-engineer Create a reusable prompt for this workflow.
/voice [a passage]
Make this a macro.
```

Resolution follows `catalog.yml`:

1. Match an exact stable ID.
2. Match a registered alias.
3. Match the artifact name.
4. Rank by intent using the artifact summary and domain.
5. Fetch and execute the canonical Markdown file.

The repository is not automatically loaded into every AI conversation. The assistant must have access to the repository and retrieve the catalog and selected artifact at invocation time. Within the Living Grimoire, GitHub is the canonical source and ChatGPT is the orchestration layer.

See [`docs/skill-system.md`](docs/skill-system.md) for the full contract.

## Repository Structure

```text
prompt-library/
├── catalog.yml                 # machine-readable registry
├── docs/
│   └── skill-system.md         # routing and authoring contract
├── macros/
│   ├── README.md
│   ├── create-macro.md
│   ├── list-skills.md
│   ├── preserve-voice.md
│   └── prompt-engineer.md
├── schemas/
│   └── catalog.schema.json
├── scripts/
│   └── validate_catalog.py
├── skills/
│   ├── README.md
│   ├── registry-curator/
│   │   └── SKILL.md
│   └── registry-router/
│       └── SKILL.md
├── templates/
│   ├── skill/
│   │   └── SKILL.md
│   ├── macro.md
│   └── universal-prompt-engineer.md
├── work/
├── writing/
├── learning/
└── meta/
```

Existing prompt paths remain stable. The registry extends the repository without requiring a disruptive migration.

## Adding a Prompt, Skill, or Macro

1. **Classify it first.** This repository is public. Only `Public` and intentionally sanitized `Professional Portfolio` artifacts belong here.
2. **Search before creating.** Prefer improving, relating, or superseding an existing artifact over making a near-duplicate.
3. **Choose the smallest useful type.** Use a macro for a compact expansion, a prompt for a reusable instruction set, and a skill when routing, tools, dependencies, or failure handling matter.
4. **Create the canonical Markdown file.** Start from the templates in `templates/`.
5. **Register it in `catalog.yml`.** Give it a stable ID, aliases, summary, classification, domain, and lifecycle state.
6. **Validate the catalog.** Run:

   ```bash
   python -m pip install pyyaml
   python scripts/validate_catalog.py
   ```

7. **Commit intentionally.** The stable ID should survive renames and moves whenever practical.

Inside the Living Grimoire, `/macro` or the phrase **Make this a macro** invokes `skill.meta.registry-curator`, which performs duplicate search, type selection, classification, authoring, catalog update, and validation.

## Data Membrane

This public repository may contain:

- `Public`
- intentionally sanitized `Professional Portfolio`

It must not contain:

- `Personal Private`
- `Employer Confidential`
- `Secrets`

A deployment may provide a secret-free private overlay for Personal Private aliases, defaults, and capability bodies. The overlay may reference public artifacts by stable ID, but it must not copy public bodies merely to customize them. This public registry defines the overlay contract without publishing or hard-coding a deployment's private topology.

Employer Confidential capabilities belong in an approved employer-controlled repository or knowledge system—not this public registry and not an unrelated personal overlay. A sanitized reusable shell may be promoted only after company-specific identities, mappings, configurations, examples, screenshots, and operational details have been removed or generalized.

Passwords, tokens, certificates, private keys, recovery codes, and comparable secret values should not be stored in any registry. Store only safe references to an approved secret-management mechanism.

## Design Principles

- **One truth, many references.** The Markdown artifact is canonical; catalogs and macros may point to it without copying its body.
- **Stable identity over filenames.** Paths can change; artifact IDs should remain stable.
- **Outcome over ceremony.** Structure should improve execution, not become paperwork for its own sake.
- **Visible uncertainty.** Skills should surface missing inputs, conflicts, and limitations rather than quietly inventing certainty.
- **Human-legible automation.** A person should be able to inspect, understand, and revise every artifact.
- **Privacy before convenience.** A useful macro is not worth leaking the context that made it useful.

## Status

The registry is active and evolves through normal version control. Catalog integrity is checked automatically on pushes and pull requests.
