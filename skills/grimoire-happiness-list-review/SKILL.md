# Grimoire Happiness List Review

## Purpose

Maintain a simple, grounded list of reusable activities and sensory experiences that reliably support enjoyment, using recent journal evidence without turning private people, places, or obligations into universal recommendations.

## Use When

Use this skill to review, refresh, or reconcile a living happiness list from newer personal evidence.

## Do Not Use When

Do not use it as crisis support, mental-health diagnosis, a gratitude exercise imposed on the user, or a generic self-care list with no evidence.

## Inputs

- **Canonical list** — the current private page and its organizing structure.
- **Evidence window** — journal entries and authorized personal notes since the previous review.
- **Optional preferences** — desired simplicity, categories, exclusions, and whether stale items should be removed or merely flagged.

## Dependencies

- Authorized read access to the user's journal or equivalent evidence source.
- Authorized write access to the existing canonical list.
- A private configuration source for page and database selectors.

When durable access is unavailable, return a proposed change set without claiming the page was updated.

## Classification

The procedure is **Public**. Journal evidence, emotional state, personal relationships, locations, routines, and the resulting tailored list are **Personal Private**.

## Procedure

### 1. Read the current list

Preserve its scale, voice, categories, and any user-authored edits. Determine the previous review baseline and avoid re-adding existing ideas under new wording.

### 2. Review newer evidence

Look for repeated, grounded sources of enjoyment supported by direct user evidence. Give more weight to recurring behavior and explicit positive response than to assistant inference.

### 3. Generalize carefully

Convert a specific instance into a reusable activity only when the generalization remains true. Prefer an activity such as trying new food over a named venue, and a type of connection over a named person, unless specificity is explicitly intended.

### 4. Apply the usefulness test

Add an item only when it is:

- evidence-backed;
- practical to revisit;
- phrased as an invitation rather than an obligation;
- distinct from existing items;
- grounded enough to help on an ordinary difficult day.

Remove or flag an item when recent evidence shows that it has become an obligation, no longer fits, or was inferred too broadly.

### 5. Keep the page simple

Make the smallest useful update. Preserve helpful sensory or activity-based organization when present. Avoid interpretive essays, scores, or excessive metadata.

### 6. Verify and report

Re-fetch the page and report additions, revisions, removals or flags, and unchanged sections.

## Output Contract

~~~markdown
# Happiness List Review

## Changes
- Added:
- Refined:
- Removed or flagged:

## Evidence Basis
- Brief source pattern for each change:

## Preserved
- Existing sections intentionally left unchanged:
~~~

## Guardrails

- Never publish the private list or its source evidence.
- Never invent preferences from demographic or personality assumptions.
- Never make a specific person responsible for the user's emotional regulation.
- Never turn a pleasant activity into a prescription or productivity target.
- Preserve the user's edits over prior assistant phrasing.

## Failure Handling

- **Insufficient evidence:** make no additions.
- **Conflicting evidence:** flag the item for review instead of deleting it automatically.
- **Canonical page unavailable:** return a ready-to-apply change set.
- **No material change:** leave the page untouched and report that result.

## Example

~~~text
/skill happiness-list-review
Review my living happiness list against journal entries added since the last pass.
~~~
