# Create Macro

## Invocation

```text
/create-macro [source material or capability request]
```

Aliases: `create-macro`, `macro-builder`

## Intent

Turn a useful recurring instruction, conversation pattern, or existing prompt into a classified, deduplicated, registered, and versioned Prompt Library capability.

The word “macro” is the user-facing entry point. The authoring skill may choose a prompt, skill, thin macro, or a prompt/skill plus macro when that produces a cleaner canonical design.

## Expansion

Execute `skill.meta.registry-author` with these defaults:

- requested artifact kind: `auto`
- preferred invocation interface: macro alias
- target: the canonical Prompt Library or the classification-appropriate overlay
- duplicate policy: search and update before creating
- versioning: use an intentional branch and draft pull request for multi-file or architectural changes
- validation: run the repository-aware catalog validator before reporting success

Do not execute the newly authored capability unless the user also asks to test it.

## Inputs

- **Source material** — rough request, prompt, notes, conversation excerpt, or existing artifact.
- **Desired outcome** — optional when clear from the source material.
- **Proposed name or alias** — optional.
- **Audience and constraints** — optional but useful when they materially shape the capability.
- **Classification or target home** — optional; infer conservatively and surface the routing decision.

## Output

Return the authoring skill's routing decision, artifact identity, validation result, and Git reference. When durable writing is unavailable, return a complete ready-to-apply artifact and catalog patch instead.

## Boundaries

- Keep a macro thin when a prompt or skill is the true canonical body.
- Search the current registry before creating a new object.
- Do not publish `Personal Private`, `Employer Confidential`, or `Secrets` material to the public repository.
- Never store secret values in any registry.
- Never claim a write or validation that did not occur.

## Examples

```text
/create-macro Turn these recurring meeting notes into a decision-and-action record.
```

```text
/create-macro
Name: Change Readiness Review
Outcome: Evaluate an implementation plan for operational readiness, rollback, ownership, and communications.
Source material: [paste notes]
```
