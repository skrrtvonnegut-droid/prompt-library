# [Macro Name]

## Purpose

[Describe the useful result this macro creates and why someone would use it.]

## Use When

Use this when:

- [appropriate situation]
- [appropriate situation]

Do not use this when:

- [important boundary or a different artifact that should be used instead]

## Inputs

### Required

- **[Input name]** — [what to provide]

### Optional

- **Audience** — [who will use or read the result]
- **Constraints** — [format, length, policy, tone, tools, or operational boundaries]
- **Existing artifact** — [content to update rather than duplicate, when applicable]

## Prompt

[Write the complete reusable instructions here. Separate enduring instructions from the source material supplied at invocation time.]

Your instructions should make clear:

1. the outcome to produce;
2. how to use the provided evidence or source material;
3. what must be preserved;
4. what assumptions, conflicts, gaps, or uncertainty must be surfaced;
5. what must not be invented;
6. the desired output structure when structure improves usability.

## Output Contract

Return:

1. **[Output section]** — [purpose]
2. **[Output section]** — [purpose]
3. **Open Questions / Assumptions** — include only when applicable.

## Guardrails

- Do not invent missing facts, attachments, decisions, approvals, or organizational context.
- Distinguish supplied evidence from interpretation.
- Preserve privacy, confidentiality, and classification boundaries.
- [Add task-specific constraints.]

## Invocation Example

```text
Use macro: [primary-alias]

[Input label]:
[Paste or attach source material]
```

<!--
Register this artifact in catalog.yml in the same change.
Macro aliases belong in the catalog and must be globally unique.
Do not copy catalog metadata into a second maintained registry.
-->
