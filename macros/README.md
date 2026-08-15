# Macros

Macros are compact named commands that expand into a registered prompt or skill invocation.

A macro is useful when the repeated value is shorthand, a default mode, or a small bundle of parameters:

```text
/skills documentation
/macro Turn this into a reusable capability.
/prompt-engineer Create a prompt for this workflow.
/voice [a passage]
```

Macros should remain thin. Do not copy a full prompt body into a macro when the macro can target a stable artifact ID.

A macro file should explain:

- its invocation form
- the prompt or skill it expands to
- accepted inputs
- defaults
- output expectations
- any meaningful safety boundary

## Creating a Macro

Use `/create-macro`, its shorter `/macro` alias, or a registered natural-language form such as **Make this a macro**.

These forms resolve `macro.meta.create-macro`, which delegates durable authoring to `skill.meta.registry-author`. The author skill searches for duplicates, chooses the smallest reliable artifact type, classifies the complete capability, selects the approved canonical home, updates source and catalog together, validates the result, and reports the actual version record.

The author may decide that the true durable object should be a prompt or skill with a thin macro in front of it. A memorable handle is useful; hiding a complicated workflow behind the wrong artifact type is not.

## Classification

- Public and intentionally sanitized Professional Portfolio macros may live in this repository.
- Personal Private aliases and defaults belong only in an authorized secret-free private overlay.
- Employer Confidential macros belong in an employer-approved canonical system.
- Secret values never belong in a macro; use safe references to an approved secret-management mechanism.

Start from [`templates/macro.md`](../templates/macro.md), register the macro and aliases in [`catalog.yml`](../catalog.yml), and run the catalog validator.
