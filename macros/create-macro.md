# Create or Update a Macro

## Invocation

```text
/macro [optional name, target, or instruction]
```

Useful natural-language forms include:

```text
Make this a macro.
Store this as a macro named manager-update.
Add an alias for our existing KB writer.
```

## Intent

Turn the current request, selected material, or recurring workflow into the smallest safe reusable capability, preferring a thin macro when an alias and defaults are sufficient.

## Expansion

Resolve and execute `skill.meta.registry-curator` in authoring mode with `macro` as the preferred kind.

Do not force the result to remain a macro. The curator should promote it to a prompt or skill when the behavior requires a substantial standalone instruction body, several stages, branching logic, tool orchestration, durable-write rules, or failure handling.

## Inputs

- **Current material** — the instruction, conversation result, prompt, or workflow to make reusable.
- **Optional name or aliases** — preferred command names.
- **Optional target** — a known prompt or skill ID.
- **Optional classification** — use when already known; otherwise classify conservatively.

## Output

Return the curator's registry result: action, stable ID, kind, aliases, target, classification, canonical path, validation result, and version record.

## Boundaries

- Search the public catalog and authorized private overlay before creating anything.
- Do not publish personal data, employer-confidential material, or secret values.
- Employer Confidential capabilities stay in an approved employer-controlled system; only an intentionally sanitized reusable shell may be considered for these personal repositories.
- Do not create a macro-to-macro chain.
- Do not claim a durable write occurred unless the repository action succeeded.
