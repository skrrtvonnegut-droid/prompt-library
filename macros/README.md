# Macros

Macros are compact named commands that expand into a registered prompt or skill invocation.

A macro is useful when the repeated value is shorthand, a default mode, or a small bundle of parameters:

```text
/skills documentation
/manager-update
/preserve-voice
```

Macros should remain thin. Do not copy a full prompt body into a macro when the macro can target a stable artifact ID.

A macro file should explain:

- its invocation form
- the artifact or behavior it expands to
- accepted inputs
- defaults
- output expectations
- any meaningful safety boundary

Start from [`templates/macro.md`](../templates/macro.md), register the macro and aliases in [`catalog.yml`](../catalog.yml), and run the catalog validator.
