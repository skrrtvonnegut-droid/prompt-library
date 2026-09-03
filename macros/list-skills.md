# List Skills

## Invocation

```text
/skills [optional topic, domain, or artifact type]
/spells [optional topic or domain]
```

Aliases: `list-skills`, `browse-skills`, `list-spells`, `browse-spells`

## Expansion

Resolve and execute `skill.meta.registry-router` in **Browse** mode.

When invoked through `/spells`, `list-spells`, or `browse-spells`, constrain Browse mode to self-hosted `kind: skill` artifacts in the public Prompt Library. Do not include private-overlay or platform/plugin-installed skills in that view.

Use the optional argument to filter or rank the registry. Examples:

```text
/skills
/skills documentation
/skills microsoft-365
/skills macros
/spells documentation
```

## Output

Return only the most relevant registry entries unless the user asks for the complete catalog. Include:

- artifact name
- stable ID
- kind
- useful aliases
- one-line purpose

Do not load or reproduce full prompt or skill bodies during browsing.
