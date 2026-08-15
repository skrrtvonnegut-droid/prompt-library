# Chess Batch

## Invocation

```text
/chess-batch start
/chess-batch complete
```

Natural-language forms:

```text
Start a chess batch.
I am going to send several PGNs; wait until I say I am done.
```

## Intent

Collect several chess games across messages without interrupting the flow with per-game analysis, then synthesize trends when the user explicitly closes the batch.

## Expansion

Execute `skill.learning.chess-lab` in `batch` mode.

Defaults:
- while open, acknowledge each unique game briefly and hold analysis;
- deduplicate repeated PGNs;
- preserve malformed or nonstandard games but lower their weight in trend conclusions when appropriate;
- on completion, analyze the batch longitudinally rather than one game at a time;
- distinguish results from meaningful evidence, especially early abandonments and rating mismatches;
- update durable syntheses or living playbook material only when the user requests capture or the active workflow explicitly includes durable capture.

## Inputs

- **Required:** one or more PGNs supplied while the batch is open.
- **State:** `start`, additional games, or `complete`.
- **Optional:** timeframe, training focus, desired comparison dimensions.

## Output

During collection: a brief receipt only.

On completion: sample summary, improving patterns, persistent risks, emerging strengths, next training block, and any requested durable updates.

## Boundaries

- Do not prematurely analyze an open batch.
- Do not count duplicate PGNs twice.
- Do not silently normalize malformed source games.
- Private game history remains private even though the macro body is public.

## Examples

```text
/chess-batch start
```

```text
/chess-batch complete
```
