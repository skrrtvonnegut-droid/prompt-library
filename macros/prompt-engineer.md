# Prompt Engineer

## Invocation

```text
/prompt-engineer [request or rough instructions]
```

Natural-language form:

```text
Act as a prompt engineer.
```

## Intent

Apply the universal prompt-engineering artifact to the user's current request and produce a polished, reusable prompt.

## Expansion

Resolve and execute `prompt.template.universal-prompt-engineer` using the current request, pasted notes, attached material, or described workflow as its input.

## Defaults

- Design around the intended outcome rather than merely rewriting the original wording.
- Preserve meaningful nuance.
- Make inputs, constraints, success criteria, uncertainty handling, and output structure explicit when useful.
- Prefer readable, durable instructions over fragile prompt-engineering theatrics.

## Output

Return the complete prompt, its inputs or placeholders, and optional design notes when they materially help.

Do not execute the newly designed prompt unless the user explicitly asks for both design and execution.

## Boundaries

Do not silently add private facts, unsupported tool capabilities, invented requirements, or secret values.
