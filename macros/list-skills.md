# List Skills

## Invocation

```text
/skills [optional topic, domain, or artifact type]
```

Aliases: `list-skills`, `browse-skills`

## Expansion

Resolve and execute `skill.meta.registry-router` in **Browse** mode.

Use the optional argument to filter or rank the registry. Examples:

```text
/skills
/skills documentation
/skills microsoft-365
/skills macros
```

## Output

Return only the most relevant registry entries unless the user asks for the complete catalog. Include:

- artifact name
- stable ID
- kind
- useful aliases
- one-line purpose

Do not load or reproduce full prompt or skill bodies during browsing.
