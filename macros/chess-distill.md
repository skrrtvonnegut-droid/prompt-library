# Chess Distill

## Invocation

```text
/chess-distill [games, analysis, or timeframe]
```

Aliases: `distill these chess games`, `distill this chess lesson`

## Intent

Promote only repeated, durable chess-learning insights from game evidence into the current learning model while leaving raw game records intact.

## Expansion

Execute `skill.learning.chess-lab` in `distill` mode.

Defaults:
- distinguish a one-off tactical lesson from a repeated pattern;
- route historical snapshots to longitudinal synthesis rather than rewriting current living documents;
- update living playbook material only when multiple games support the change;
- prefer a small training adjustment over an expanding checklist;
- preserve contradictory evidence and uncertainty rather than forcing a clean narrative.

## Inputs

- **Required:** one or more analyzed games, a named pattern, or a timeframe.
- **Optional:** existing living playbook, current training focus, desired durable destination.

## Output

A routing decision for each durable insight: living playbook, dated synthesis, existing pattern update, or remain ephemeral.

## Boundaries

- Do not overwrite raw PGNs or historical game analyses.
- Do not turn one dramatic game into permanent doctrine.
- Personal examples remain in the user's authorized private knowledge system.

## Examples

```text
/chess-distill my last ten 15+10 games
```
