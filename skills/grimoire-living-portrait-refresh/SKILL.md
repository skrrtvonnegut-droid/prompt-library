# Grimoire Living Portrait Refresh

## Purpose

Incrementally refresh a private living personal profile from the user's direct journal writing while preserving confidence levels, contradiction, change over time, and stable sections that have not materially changed.

## Use When

Use this skill for a monthly or ad hoc Living Portrait refresh, a personal-profile reconciliation, or a review of how newer direct evidence changes the current portrait.

## Do Not Use When

Do not use it for a public biography, personality diagnosis, one-entry reaction, or automatic routing of personal material into a public knowledge garden.

## Inputs

- **Canonical profile** — the existing private Living Portrait and its review marker.
- **Primary evidence** — direct user-authored journal entries newer than the baseline.
- **Corroborating evidence** — assistant reflections, reconstructed entries, or other private context, clearly labeled and weighted below direct writing.
- **Optional older evidence** — only when needed to test whether a newer pattern strengthens, complicates, or contradicts an existing claim.

## Dependencies

- Authorized read access to the private journal and profile.
- Authorized write access to the existing canonical profile.
- A private configuration source for page and database selectors.

## Classification

The procedure is **Public**. The profile, journal, inferred traits, relationships, health, spirituality, finances, and source mappings are **Personal Private**.

## Procedure

### 1. Establish scope

Read the profile and determine the last reviewed-through date from its scope statement or latest change-log entry. Search closely within the incremental journal window.

### 2. Preserve evidence hierarchy

Treat direct user-authored lived records as primary. Use assistant reflections, reconstructions, memory summaries, and non-journal context only as corroboration unless the same pattern appears in direct writing.

Exclude connected newsletters, emails, and third-party biographical text as evidence about the user unless the user explicitly authored or endorsed the relevant claim.

### 3. Evaluate material change

For each existing or candidate pattern, classify the evidence as:

- **Direct observation**;
- **Strong inference**;
- **Tentative interpretation**.

Identify patterns that are new, strengthened, weakened, complicated, contradicted, or retired. Preserve ambiguity and change over time instead of forcing a coherent static identity.

### 4. Update conservatively

Update the existing profile in place. Do not rewrite stable sections for polish or novelty. Add source mentions beside changed claims and update the scope date and evidence count.

Do not alter journal entries, create a parallel profile, or route personal concepts into another durable system without approval.

### 5. Maintain the change log

Append one dated review entry containing the journal period, entries reviewed, sections changed, pattern-state changes, important contradictions, and any proposed—but not automatically routed—knowledge candidates.

If no material change is supported, append only a concise no-material-change review record when the profile's established convention calls for one.

### 6. Verify and report

Re-fetch the profile and report changes, confidence levels, contradictions, and questions requiring the user's judgment.

## Output Contract

~~~markdown
# Living Portrait Refresh

## Review Scope
- Period:
- Entries reviewed:

## Material Changes
- New:
- Strengthened:
- Weakened:
- Complicated:
- Retired:

## Confidence
- Direct:
- Strong inference:
- Tentative:

## Contradictions and Judgment
- Preserved tensions:
- Questions for the user:

## Durable Result
- Profile updated:
- Stable sections unchanged:
~~~

## Guardrails

- Never publish the profile or its source material.
- Never diagnose the user or present interpretation as clinical fact.
- Never treat assistant prose as primary autobiographical evidence.
- Never erase contradiction merely to make the portrait feel coherent.
- Never churn stable sections for stylistic freshness.

## Failure Handling

- **Baseline unclear:** inspect the current scope and report uncertainty before broad edits.
- **Insufficient direct evidence:** preserve the claim state or lower confidence rather than inventing change.
- **Conflicting evidence:** retain both temporal states and explain the tension.
- **Canonical profile unavailable:** return a proposed change log without claiming an update.

## Example

~~~text
/skill living-portrait-refresh
Refresh my private Living Portrait from direct journal evidence added since the last review.
~~~
