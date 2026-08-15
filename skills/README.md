# Skills

Skills are routed capabilities with explicit procedures, dependencies, guardrails, and output contracts.

Each skill lives in its own directory:

```text
skills/
└── example-skill/
    ├── SKILL.md
    ├── references/      # optional
    ├── scripts/         # optional
    └── assets/          # optional
```

`SKILL.md` is the entry point. Supporting files should exist only when they materially improve execution. Avoid hiding the essential operating logic in code or references that a human cannot easily inspect.

## When to Create a Skill

Create a skill when the capability needs more than a standalone prompt—for example, tool routing, multiple operating modes, dependency checks, classification decisions, or explicit failure handling.

For compact reusable shorthand, create a macro instead. For a single coherent instruction set, create a prompt.

Start from [`templates/skill/SKILL.md`](../templates/skill/SKILL.md), register the artifact in [`catalog.yml`](../catalog.yml), and run the catalog validator.
