# Chess Review

## Invocation

```text
/chess-review [optional timeframe]
```

Aliases: `review my chess progress`, `chess trend review`

## Intent

Run a longitudinal review across a meaningful set of chess games and identify what is improving, what is still costing games, and the smallest useful next training block.

## Expansion

Execute `skill.learning.chess-lab` in `review` mode.

Defaults:
- use the canonical game log when available;
- qualify the sample when it contains early abandonments, custom positions, malformed PGNs, or large rating mismatches;
- compare time controls when enough data exists;
- organize mistakes by cause rather than merely win/loss outcome;
- identify emerging strengths as well as persistent risks;
- end with what to train next and what **not** to add yet.

## Inputs

- **Optional:** timeframe, number of games, rating window, time control, or named training focus.
- **Default:** the most recent meaningful sample available in the canonical game log.

## Output

A dated longitudinal review with sample caveats, improving patterns, persistent risks, emerging strengths, representative games, time-control effects, and next training block.

## Boundaries

- Do not treat abandoned games as equivalent to completed competitive games without qualification.
- Do not infer engine evaluations unless real engine evidence is available.
- Do not flatten contradictory evidence into a single progress story.

## Examples

```text
/chess-review this month
```
