# Custom Macro Builder

## Purpose

Turn a rough request, useful conversation pattern, or existing prompt into a reusable macro registered in the prompt-library repository without creating duplicates or crossing classification boundaries.

Use this when someone wants to say, in effect, “make this a capability we can call again.”

## Prompt

Act as the maintainer of a versioned prompt and skill registry.

Your task is to transform the material I provide into a durable, reusable macro for the `prompt-library` repository. Treat the repository's `catalog.yml`, `AGENTS.md`, authoring guide, and skill contract as authoritative for structure and routing.

### 1. Determine the capability

Identify:

- the enduring outcome the macro should produce;
- the inputs a user will provide at invocation time;
- the intended audience or operating context;
- the expected output contract;
- important constraints, risks, and non-goals;
- whether this is a single-file prompt or a multi-file skill.

Separate reusable logic from one-time examples and private context.

### 2. Classify before writing

Classify the proposed artifact using the repository's data membrane.

This public repository may contain only:

- `Public` material;
- intentionally sanitized `Professional Portfolio` material.

Do not publish `Personal Private`, `Employer Confidential`, or `Secrets` material. Never store passwords, tokens, certificates, private keys, recovery codes, private records, proprietary source content, internal identifiers, or confidential environment details.

When the reusable logic is public but its configuration or examples are private, keep the public logic here and route the private material to an authorized private overlay.

### 3. Search for an existing canonical artifact

Before creating anything new:

1. Read `catalog.yml`.
2. Search artifact IDs, names, summaries, macro aliases, domains, tags, and repository content for the same or substantially overlapping outcome.
3. Decide whether to:
   - update an existing artifact;
   - add an alias or compatible mode to an existing artifact;
   - relate or supersede an existing artifact;
   - create a genuinely new artifact.

Prefer updating the canonical object over creating a parallel copy.

### 4. Design the identity

For a new artifact, propose:

- a stable lowercase dotted artifact ID;
- a domain-aligned repository path;
- a clear human-readable name;
- one primary globally unique lowercase kebab-case macro alias;
- optional compatibility aliases;
- concise discovery tags;
- lifecycle state and classification.

Do not encode dates, versions, employer names, or temporary project names in the stable ID unless they are intrinsic to the enduring capability.

### 5. Build the artifact

Use `templates/macro-template.md` for a single-file prompt or the multi-file structure in `docs/SKILL-CONTRACT.md` for a skill.

The result should:

- define the outcome clearly;
- distinguish required and optional inputs;
- preserve important nuance;
- separate source material from instructions;
- surface missing information, contradictions, assumptions, and uncertainty;
- state what must not be invented;
- include an output contract when structure improves usability;
- remain understandable and editable by a human;
- avoid unnecessary roleplay, filler, and brittle prompt tricks.

Do not execute the newly authored macro unless I explicitly ask you to test or use it.

### 6. Register and version it

Update the artifact and `catalog.yml` in the same change.

When repository write tools and permission are available:

- preserve unrelated work;
- use an intentional branch or commit strategy appropriate to the request;
- include a meaningful commit or pull-request description;
- report the artifact path, stable ID, macro aliases, classification, and resulting Git reference.

When write access is unavailable, return a complete ready-to-apply artifact and catalog patch rather than pretending the repository was changed.

## Output

Return:

1. **Routing Decision** — new, update, alias, supersede, or private overlay, with a brief rationale.
2. **Classification Review** — classification, sanitization performed, and anything intentionally excluded.
3. **Artifact Identity** — name, ID, path, kind, macro aliases, domain, tags, and status.
4. **Artifact Content or Change Summary** — the complete artifact when not writing directly; otherwise a concise description of what changed.
5. **Catalog Entry or Change Summary** — the complete entry when not writing directly; otherwise the registered metadata.
6. **Versioning Result** — commit, branch, pull request, or a transparent explanation that no write occurred.
7. **Open Questions** — only unresolved issues that materially affect safe or correct publication.

## Input

Provide the rough request, conversation excerpt, existing prompt, or capability description to turn into a macro:

`[SOURCE MATERIAL HERE]`
