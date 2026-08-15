# Chess Migrate

## Invocation

```text
/chess-migrate [archive, conversation, or source collection]
```

Aliases: `migrate this chess archive`, `migrate this chess chat`

## Intent

Convert a historical chess conversation, notebook, or game archive into a structured learning system while separating evidence, longitudinal synthesis, current living guidance, creative adaptations, duplicates, and ephemeral chatter.

## Expansion

Execute `skill.learning.chess-lab` in `migrate` mode.

Defaults:
- discover the destination structure before writing;
- search for existing chess hubs and records before creating new ones;
- preserve unique raw PGNs first;
- deduplicate repeated games;
- flag malformed or nonstandard sources rather than silently repairing them;
- migrate dated syntheses separately from living playbook pages;
- link dramatic adaptations to source games;
- omit acknowledgements, transitional chatter, and superseded repetitive advice;
- reconcile navigation surfaces last.

## Inputs

- **Required:** conversation, archive, notebook, export, or game collection.
- **Optional:** target knowledge system, canonical-home rules, classification constraints, preferred taxonomy.

## Output

A migration result covering game records, syntheses, living documents, legends, duplicates/anomalies, and any remaining gaps.

## Boundaries

- Do not dump an entire chat verbatim when durable structure is more appropriate.
- Preserve private source material as private by default.
- Do not create competing copies of a living artifact across systems.
- Reusable workflow bodies belong in the canonical registry, not duplicated into notes.

## Examples

```text
/chess-migrate this chess conversation into my learning system
```
