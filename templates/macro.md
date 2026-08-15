# [Macro Name]

## Invocation

```text
/[alias] [optional inputs]
```

List any additional registered aliases.

## Intent

Describe the small, repeatable convenience this macro provides.

## Expansion

Reference the stable prompt or skill ID this macro invokes, or provide the compact canonical instruction when the macro is self-contained.

Prefer:

```text
Execute `skill.example.target` in [mode] with these defaults:
- ...
```

Avoid copying a long prompt body.

## Inputs

- **Optional or required input** — expected form.
- **Defaults** — behavior when omitted.

## Output

State the expected result briefly.

## Boundaries

- Identify classification constraints.
- Do not store secret values.
- Do not silently widen the target artifact's scope.
- Preserve the target artifact as the canonical body.

## Examples

```text
/[alias]
/[alias] [example input]
```

## Registration Checklist

1. Save as `macros/<slug>.md`.
2. Add a unique `macro.<domain>.<slug>` entry to `catalog.yml`.
3. Register the slash alias and any natural-language aliases.
4. Run `python scripts/validate_catalog.py`.
