# Chess Journal

## Invocation

```text
/chess-journal [game, session, or analysis]
```

Aliases: `journal this chess game`, `summarize this chess session for my journal`

## Intent

Turn a chess game or session into a short first-person journal reflection focused on experience, learning, and the next practical focus rather than duplicating technical analysis.

## Expansion

Execute `skill.learning.chess-lab` in `journal` mode.

Defaults:
- preserve the user's voice when it is known from context;
- mention the result only as context;
- emphasize what felt different, what was learned, and what to carry into the next game;
- keep the reflection concise unless the user requests a longer entry;
- do not silently write to a journal database unless durable capture is requested or the active workflow explicitly includes it.

## Inputs

- **Required:** one game, one session, or an existing chess analysis.
- **Optional:** desired length, emotional emphasis, current training focus, journal destination.

## Output

A short first-person journal-ready reflection.

## Boundaries

- Do not copy the technical move-by-move analysis into the journal entry.
- Do not overstate improvement from a single game.
- Preserve personal material as private by default.

## Examples

```text
/chess-journal this last 15+10 game
```
