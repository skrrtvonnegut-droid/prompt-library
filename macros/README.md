# Macros

Macros are compact named commands that expand into a registered prompt or skill invocation.

A macro is useful when the repeated value is shorthand, a default mode, or a small bundle of parameters:

```text
/skills documentation
/prompt-engineer Create a reusable prompt for this workflow.
/voice [a passage]
/macro [a recurring instruction]
```

Macros should remain thin. Do not copy a full prompt body into a macro when the macro can target a stable artifact ID.

A macro file should explain:

- its invocation form
- the prompt or skill it expands to
- accepted inputs
- defaults
- output expectations
- any meaningful safety boundary

## Creating a Macro Through the Grimoire

Use:

```text
/macro [optional name, target, or instruction]
```

or say:

```text
Make this a macro.
Store this as a macro named [name].
```

These forms resolve `macro.meta.create-macro`, which delegates to `skill.meta.registry-curator`. The curator searches for duplicates, chooses the smallest suitable artifact type, classifies the complete capability, selects the canonical home, updates the source and catalog together, and validates the result.

The curator may decide that the durable object should be a prompt or skill rather than a macro. A memorable handle is useful; hiding a complicated workflow behind the wrong artifact type is not.

## Classification

- Public and intentionally sanitized Professional Portfolio macros may live in this repository.
- Personal Private aliases and defaults belong in the `grimoire-core` overlay.
- Employer Confidential macros belong in an approved employer-controlled system.
- Secret values never belong in a macro. Use safe references to an approved secret-management mechanism.

Start from [`templates/macro.md`](../templates/macro.md), register the macro and aliases in [`catalog.yml`](../catalog.yml), and run the catalog validator.
