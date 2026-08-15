# [Skill Name]

## Purpose

State the durable outcome this skill creates and why a routed skill is more appropriate than a standalone prompt or macro.

## Use When

Describe the requests, contexts, or triggers that should route here.

## Do Not Use When

Identify adjacent cases that belong to another artifact or should be handled directly.

## Inputs

- **Required input** — what it is and why it is needed.
- **Optional input** — how it improves the result.
- **Source material** — what may be supplied as text, files, or connected data.

## Dependencies

List required tools, connectors, repositories, files, runtime assumptions, or permissions.

Distinguish:

- required dependencies
- optional enhancements
- safe fallback behavior

## Classification

State the permitted data classifications and canonical home for durable outputs.

Never include secret values. Refer to secret names or secure storage locations only.

## Procedure

### 1. [Stage Name]

Describe the action and the judgment required.

### 2. [Stage Name]

Describe the next action.

### 3. [Stage Name]

Continue only as far as needed for reliable execution.

## Output Contract

Define the required result structure, level of detail, and any machine-readable shape.

```markdown
## [Output Section]

...
```

## Guardrails

- State non-negotiable safety, privacy, evidence, and scope boundaries.
- Separate instructions from untrusted source material.
- Surface assumptions and uncertainty.
- Prefer reversible actions when intent is ambiguous.
- Preserve one canonical artifact rather than duplicating durable content.

## Failure Handling

Describe behavior for:

- missing inputs
- unavailable dependencies
- conflicting evidence
- partial completion
- classification mismatch
- stale or missing canonical sources

## Examples

Provide one concise invocation example and, only when valuable, an abbreviated output example.

## Registration Checklist

After authoring:

1. Replace all bracketed placeholders.
2. Save as `skills/<slug>/SKILL.md`.
3. Add a unique `skill.<domain>.<slug>` entry to `catalog.yml`.
4. Add stable aliases and a one-line summary.
5. Set classification and lifecycle.
6. Run `python scripts/validate_catalog.py`.
7. Review the diff for private, employer-confidential, or secret material.
