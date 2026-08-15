# Chess Legend

## Invocation

```text
/chess-legend [source game and style]
```

Aliases: `dramatize this chess game`, `turn this game into a legend`

## Intent

Transform a source chess game into a literary or dramatic adaptation while preserving a clear link to the technical source and keeping myth separate from analysis.

## Expansion

Execute `skill.learning.chess-lab` in `legend` mode.

Defaults:
- preserve the source-game relation when a canonical game log exists;
- use named characters for major pieces when the requested style benefits from it;
- obey requested literary register, melodrama level, and whether chess vocabulary should be explicit, subtle, or hidden;
- preserve uncertainty when the source game was still ongoing at the time of adaptation;
- store the adaptation in the user's creative chess archive only when durable capture is requested.

## Inputs

- **Required:** source PGN or canonical game reference.
- **Optional:** style, tone, melodrama level, character names, chess-reference visibility, cliffhanger or ending constraints.

## Output

A finished dramatic adaptation, plus durable-link status when applicable.

## Boundaries

- The adaptation is creative work, not technical analysis.
- Do not alter the canonical PGN to fit the story.
- Private source games and relationship context must not be copied into this public macro body.

## Examples

```text
/chess-legend
Style: Arthurian
Melodrama: 9/10
Chess terms: hidden
Source: [PGN]
```
