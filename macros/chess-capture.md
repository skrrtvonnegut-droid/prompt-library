# Chess Capture

## Invocation

```text
/chess-capture [PGN or game]
```

Aliases: `/chess-game`, `capture this chess game`

## Intent

Capture one chess game as evidence, analyze it at a useful level, and preserve the raw PGN without prematurely turning one game's lesson into durable doctrine.

## Expansion

Execute `skill.learning.chess-lab` in `capture` mode.

Defaults:
- preserve raw PGN verbatim;
- deduplicate against the canonical game log when available;
- label analysis mode truthfully;
- prefer the first consequential mistake or opportunity over exhaustive criticism;
- assign a small theme set and one primary training takeaway;
- write to the user's canonical chess game log only when durable capture is requested and authorized.

## Inputs

- **Required:** PGN, move list, or game source.
- **Optional:** context, self-assessment, engine output, desired depth.

## Output

A single-game record and concise learning analysis, plus the durable-write result when applicable.

## Boundaries

- Never claim Stockfish or engine analysis without an actual engine or supplied trusted output.
- Do not silently repair malformed PGNs.
- Preserve private game history in the user's authorized private system, not in the public registry.

## Examples

```text
/chess-capture
[Site "Chess.com"]
...
```
