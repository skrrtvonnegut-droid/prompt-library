# Chess Engine Check

## Invocation

```text
/chess-engine-check [PGN or analyzed game]
```

Aliases: `engine check this game`, `verify this chess analysis with an engine`

## Intent

Verify a human-readable chess analysis against a real engine or trusted engine output, focusing on the first major evaluation swing and any tactical fact that materially changes the learning lesson.

## Expansion

Execute `skill.learning.chess-lab` in `engine-check` mode.

Defaults:
- use an actual available engine or trusted supplied engine output;
- identify the first major evaluation swing rather than dumping long principal variations;
- compare computer-best play with the human-practical lesson;
- correct earlier manual analysis when engine evidence materially changes it;
- mark durable records Engine-assisted only when engine evidence was genuinely used.

## Inputs

- **Required:** PGN or canonical game reference.
- **Required dependency:** available chess engine or trusted engine output.
- **Optional:** existing manual analysis to compare against.

## Output

A concise verification report separating engine fact, practical lesson, and any correction to the prior analysis.

## Boundaries

- Never simulate Stockfish output.
- If no engine is available, stop engine-check mode and say so; manual analysis may be offered separately.
- Preserve the raw PGN unchanged.

## Examples

```text
/chess-engine-check [PGN]
```
