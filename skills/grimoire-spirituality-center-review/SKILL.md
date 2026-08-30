# Grimoire Spirituality Center Review

## Purpose

Reconcile a private spirituality-and-myth center and its living practice pages from newer journal entries and knowledge notes while preserving source provenance, doctrinal differences, and the distinction between lived practice and comparative synthesis.

## Use When

Use this skill for a periodic or ad hoc review of a spirituality center, its tradition-specific living pages, or the emerging throughline across several practices.

## Do Not Use When

Do not use it for a one-off doctrinal question, a general comparative-religion essay, or automatic publication of private spiritual history.

## Inputs

- **Runtime configuration** — canonical center, configured tradition pages, journal and knowledge-note sources, review baseline, and allowed destinations.
- **New evidence** — direct reflections, readings, practices, community participation, questions, and cross-tradition observations since the previous review.
- **Current interpretation** — existing living pages, backlinks, metadata, and unresolved questions.

## Dependencies

- Authorized read access to the configured private evidence sources.
- Authorized write access to the canonical spirituality center.
- Reliable external sources when factual or doctrinal corrections require verification.
- A private configuration source for page selectors and the user's chosen traditions.

## Classification

The reusable review method is **Public**. Religious or spiritual identity, practice history, journal content, community participation, and private page mappings are **Personal Private** unless the user deliberately classifies them otherwise.

## Procedure

### 1. Resolve scope and baseline

Fetch the current center, configured tradition pages, latest review marker, and relevant source schemas. Determine the incremental evidence window without assuming every recent mention is a durable development.

### 2. Gather evidence in separate passes

Search new journal and knowledge material by configured tradition, text, practice, teacher, community, and cross-tradition theme. Fetch the underlying source before using a search hit as evidence.

Distinguish:

- direct lived practice;
- reading or study;
- factual or doctrinal claims;
- assistant-authored reflection;
- emerging synthesis;
- open questions.

### 3. Reconcile tradition pages first

Update the relevant tradition page only when evidence supports a meaningful recurring pattern, lived development, factual correction, useful backlink, or clarified open thread. Preserve the source tradition's own concepts and avoid translating every practice into one preferred framework.

### 4. Reconcile the shared throughline

Update the center-level synthesis only after the tradition-specific evidence is clear. Preserve affinities, tensions, incompatibilities, uncertainty, and changes over time. Do not flatten differences into a universalized spirituality.

### 5. Maintain structure conservatively

Reconcile stale links, duplicate summaries, metadata contradictions, and open threads. Prefer enriching an existing canonical page. Create a new page only when no suitable canonical home exists and the distinction is durable.

### 6. Verify and report

Re-fetch each changed page, confirm intended sections and backlinks, and return created, enriched, unchanged, and unresolved items.

## Output Contract

~~~markdown
# Spirituality Center Review

## Evidence Window
- Reviewed through:
- Sources inspected:

## Durable Changes
- Tradition pages enriched:
- Center synthesis updated:
- Backlinks or metadata repaired:
- Pages created:

## Emerging Throughline
- Strengthened:
- Complicated:
- Newly uncertain:

## Preserved Differences
- Doctrinal or practical distinctions:

## Questions for Judgment
- Only issues that require the user's interpretation:
~~~

## Guardrails

- Never publish or expose private spiritual history through the public registry.
- Never treat assistant reflection as equivalent to the user's direct writing.
- Never collapse distinct traditions into a generic motivational synthesis.
- Never copy entire journal entries into living pages; distill and link.
- Never create new pages merely to make the center look more complete.

## Failure Handling

- **Baseline unavailable:** inspect current pages and report the uncertainty before any broad rewrite.
- **Factual uncertainty:** verify with reliable sources or leave the claim explicitly unresolved.
- **Conflicting reflections:** preserve the change or contradiction instead of choosing one silently.
- **No meaningful developments:** make no durable edits and return a no-change report.

## Example

~~~text
/skill spirituality-center-review
Reconcile my configured spirituality center from evidence added since the last review.
~~~
