# Grimoire Grand Line Archive

## Purpose

Reconcile new or materially changed One Piece notes, viewing or reading markers, theories, and reflections into a canonical Grand Line Archive while preserving source custody, user voice, and separation among manga, anime, live-action, and interpretive continuities.

## Use When

Use this skill to maintain, update, reconcile, or run upkeep on an authorized Grand Line Archive.

## Do Not Use When

Do not use it for general One Piece trivia, a one-off review with no durable archival request, wholesale copying of copyrighted material, or unapproved architectural changes.

## Inputs

- **Runtime configuration** — archive hub, voyage log, migration register, continuity-specific pages, source databases, and permitted destinations.
- **New source material** — journal entries, media notes, progress markers, theories, reactions, and corrections not already represented.
- **Current archive** — existing log entries, continuity pages, source custody, fidelity labels, and unresolved gaps.

## Dependencies

- Authorized read access to the source notes and canonical archive.
- Authorized write access to the archive.
- Official sources such as VIZ, Toei Animation, or Netflix when new factual metadata or editorial imagery requires verification.
- A private configuration source for page selectors and source mappings.

## Classification

The reusable archival method is **Public**. Private reactions, journal links, progress, page identifiers, and source mappings retain their source classification. Copyrighted source material remains subject to its original rights.

## Procedure

### 1. Load the current archive

Fetch the hub, voyage log, migration register, continuity pages, and current schemas. Treat the canonical archive as authority and determine the latest reconciled source window.

### 2. Search for new or changed sources

Search authorized journals, media notes, progress markers, theories, and reflections. Fetch the underlying source before writing. Reconcile by source identity and date so reruns remain idempotent.

### 3. Classify continuity and fidelity

Assign each item to the correct continuity and use only these fidelity labels:

- **Verbatim**
- **Light Edit**
- **Synthesis**
- **Reconstructed**

Do not blend adaptations into one canon or silently promote a reconstruction into a quotation.

### 4. Update the Voyage Log

When new material exists, add a dated entry with continuity, unit or arc, source reference, concise reaction, interpretive threads, and fidelity label. Keep the private raw source canonical and link to it when supported.

### 5. Reconcile the appropriate canonical page

Update only the relevant manga, anime, live-action, or long-form interpretive page. Preserve the user's diction and theory boundaries. Do not duplicate the same observation across several pages unless each placement serves a distinct navigational role.

### 6. Verify metadata and imagery

Use official sources for new factual metadata or editorial imagery. Include source captions and useful alt text. Do not reproduce long copyrighted passages or unlicensed image files in the archive.

### 7. Maintain custody and report

Update the migration register only when custody, gaps, or migration status materially changes. Re-fetch changed pages and report sources linked, fidelity decisions, pages updated, and unresolved gaps.

## Output Contract

~~~markdown
# Grand Line Archive Upkeep

## Sources Reconciled
- Source, date, continuity, fidelity:

## Archive Changes
- Voyage Log:
- Manga:
- Anime:
- Live action:
- Long-form interpretation:
- Migration register:

## Verification
- Metadata sources:
- Images and alt text:
- Idempotency check:

## Unresolved Gaps
- Only genuine custody, continuity, or evidence gaps:
~~~

## Guardrails

- Never edit the raw journal source.
- Never collapse distinct continuities.
- Never invent missing prose, quotations, metadata, or theories.
- Never delete, move, or restructure the archive without explicit approval.
- Never copy private source mappings or copyrighted bodies into the public Prompt Library.
- Prefer enrichment of an existing canonical page over a duplicate.

## Failure Handling

- **No new material:** make no edits and report “No archive changes.”
- **Continuity ambiguous:** preserve the source and request classification rather than guessing.
- **Fidelity uncertain:** choose the more conservative label.
- **Official metadata unavailable:** omit the claim or mark it unverified.
- **Structural change needed:** report a proposal instead of changing architecture.

## Example

~~~text
/skill grand-line-archive
Reconcile new One Piece material into my authorized canonical archive.
~~~
