# Grimoire Chess Weekly Development

## Purpose

Review the immediately preceding completed week of canonical chess evidence, create one dated historical synthesis, and update living development pages only when the evidence supports a material revision.

## Use When

Use this skill for the Weekly Chess Development review, a manual weekly chess reconciliation, or an evidence-backed update to the current training model.

## Do Not Use When

Do not use it to repair individual game records, file new PGNs, or analyze one isolated game. Daily record compliance belongs to skill.grimoire.chess-daily-reconciliation; general chess analysis belongs to skill.learning.chess-lab.

## Inputs

- **Runtime configuration** — timezone, canonical Chess Games source, synthesis destination, living-page selectors, standard marker, engine contract, and baseline selectors.
- **Weekly evidence** — every game in the preceding completed Monday-through-Sunday interval.
- **Current interpretation** — the existing training focus, pattern ledger, opening playbook, tactical priorities, endgame/conversion model, and player-style page.

## Dependencies

- Authorized read access to canonical game records and current living pages.
- Authorized write access to the historical synthesis and living pages.
- Current page-standard reference and baseline.
- A private deployment configuration for record identifiers and source mappings.

If a required dependency is unavailable, return a blocked report without writes.

## Classification

The procedure is **Public**. Game history, ratings, usernames, private notes, database identifiers, and personal learning profiles remain private unless deliberately published.

## Procedure

### 1. Establish scope and compliance

Calculate the preceding completed Monday-through-Sunday interval in the configured timezone. Fetch destination schemas, current living pages, the standard reference, the baseline, the latest comparable synthesis, and every game in scope.

Reconcile only by exact Source Key. Produce a database-wide compliance census that distinguishes canonical rows, committed standard rows, scored debt, legitimate zero-move debt, and independent context rows.

### 2. Gate the evidence set

A scored game is eligible only when its standard marker, unique source identity, engine and depth, telemetry, PGN, evidence order, and provenance all satisfy the configured contract. If any scored current-week game fails, block all synthesis and living-page writes and return the failed records plus the census.

Keep legitimate zero-move sources in inventory but exclude them from CPL, errors, conversion, strongest-game, and development denominators. Segment bot or coach practice from human-opponent development claims.

### 3. Build the weekly evidence model

Measure games, W-D-L, score rate, colors, opponents, time controls, openings, mean of game Mean CPL, median of game Median CPL, errors, best-move rate, phase profiles, winning edges, conversion, decisive choices, motifs, narrative lessons, contradictions, and changes versus comparable baselines.

Pair mean with median, preserve sample sizes, identify outliers, and avoid causal claims from opponent mix, rating, time control, or opening alone.

### 4. Apply evidence thresholds

- Treat one game as an example, not a model change.
- Normally require three distinct human games, or two that reinforce an established baseline pattern, before changing a focus, ledger state, tactical priority, endgame curriculum, or opening emphasis.
- Require five comparable lifetime games before converting an opening observation into a practical rule.
- Require at least five human games plus two independent signals, or a clear multi-week trend, before changing the player-style model.
- Distinguish **emerging**, **active**, **improving**, and **integrated** patterns.

Preserve contradiction. A no-change conclusion is valid.

### 5. Reconcile one historical synthesis

Create or update exactly one synthesis for the completed week, using a deterministic title and embedded Source Key inventory. Include scope, provenance, compliance census, segmentation, metrics, phase and conversion findings, per-game evidence links, supported patterns, provisional signals, contradictions, baseline comparison, living-page decisions, confidence limits, and the next experiment.

Do not rewrite an unchanged synthesis.

### 6. Update living pages conservatively

Update only the configured living pages whose current interpretation materially changed. Keep at most one primary and one secondary training focus. Append one dated revision note to each changed page with the evidence, sample size, confidence, and synthesis link. Preserve existing user prose, icons, callouts, baselines, links, and prior evidence.

### 7. Verify and report

Re-fetch every created or changed object and verify titles, properties, source inventory, revision markers, links, and revised sections. Report changed and unchanged pages explicitly.

## Output Contract

~~~markdown
# Weekly Chess Development Review — YYYY-MM-DD → YYYY-MM-DD

## Sample and Record
- Games and W-D-L:
- Metric summary:
- Segmentation:

## Evidence
- Strongest game:
- Most instructive game:
- Supported trends:
- Provisional signals:
- Contradictions:

## Compliance
- Census:
- Debt:
- Blockers:

## Living Model
- Pages changed:
- Pages unchanged:
- Primary focus:
- Secondary focus:
- Next experiment:
~~~

## Guardrails

- Never repair individual game records in this workflow.
- Never synthesize from noncompliant scored games.
- Never treat preserved human notes as engine evidence.
- Never overfit the current model to a dramatic outlier.
- Never publish private game history or runtime identifiers.

## Failure Handling

- **Current-week compliance failure:** write nothing and return a blocked report.
- **No eligible scored games:** create no synthesis and edit no living page.
- **Eligible games but no model change:** create the historical synthesis and leave living pages unchanged.
- **Concurrent or duplicate weekly synthesis:** reconcile the canonical object rather than creating another.

## Example

~~~text
/skill chess-weekly-development
Review the last completed week using my authorized chess evidence.
~~~
