# Grimoire Career Evidence Refresh

## Purpose

Incrementally update a private professional capability profile from verified journal evidence while preserving privacy, provenance, implementation status, and the existing canonical page.

## Use When

Use this skill for a periodic career-evidence refresh, a professional profile reconciliation, or an evidence-backed update to a living capability map.

## Do Not Use When

Do not use it to publish a resume, create a portfolio artifact, rewrite candid personal journaling, or promote aspirations into completed accomplishments. Public portfolio curation belongs to skill.work.portfolio-curator.

## Inputs

- **Canonical profile** — the existing professional identity and evidence page.
- **Journal source** — authorized entries newer than the profile's evidence-refresh date.
- **Capability dimensions** — configured areas such as identity, endpoint management, messaging, security, automation, licensing, business platforms, governance, service management, change, documentation, and capability transfer.
- **Privacy boundary** — employer, acquisition, tenant, stakeholder, and personal details that must remain private.

## Dependencies

- Authorized read access to the private professional journal evidence.
- Authorized write access to the existing profile.
- A private configuration source for selectors, capability dimensions, and denylist rules.

## Classification

The reusable procedure is **Professional Portfolio**. Raw journal entries, employer context, tenant details, stakeholder identities, incidents, and canonical page mappings retain their more restrictive source classification.

## Procedure

### 1. Establish the incremental window

Read the canonical profile first. Use its evidence-refresh marker to define the new journal window. Do not duplicate evidence already represented.

### 2. Search by capability dimension

Run separate searches across the configured capability areas. Fetch and verify representative entries before making a claim. Search hits and summaries are discovery aids, not evidence by themselves.

### 3. Separate claim states

Maintain clear distinctions among:

- journal-verified evidence;
- previously documented claims not re-verified in this pass;
- private-only evidence;
- target, learning, or aspirational practice;
- contradictory or weakening evidence.

Use ownership verbs proportional to the source. Distinguish designed, proposed, supported, implemented, operated, remediated, documented, and taught.

### 4. Protect claim quality

Require a source for every quantitative claim. Preserve confidentiality boundaries. Do not infer organizational ownership from participation, or production implementation from planning.

### 5. Update in place

Update only the existing canonical profile. Preserve its icon, cover, visual structure, source trail, and canonical links. Refresh the capability map, evidence bank, risks or gaps, impact statements, and evidence date only where new evidence warrants it.

Do not update a public resume, public portfolio, or unrelated profile under this skill.

### 6. Verify and report

Re-fetch the profile and return a concise changelog of added, strengthened, corrected, weakened, aspirational, private-only, and unchanged claims.

## Output Contract

~~~markdown
# Career Evidence Refresh

## Evidence Window
- From:
- Through:
- Entries verified:

## Profile Changes
- Added:
- Strengthened:
- Corrected or weakened:
- Risks or gaps:

## Claim Boundaries
- Private-only:
- Aspirational:
- Needs corroboration:

## Durable Result
- Canonical page updated:
- Sections unchanged:
~~~

## Guardrails

- Never expose candid personal journal material in a professional profile.
- Never publish employer-confidential context or identifying tenant details.
- Never inflate participation into ownership or planning into implementation.
- Never update a public resume or portfolio without separate authorization and review.
- Never create a duplicate profile when the canonical page exists.

## Failure Handling

- **No material evidence:** leave the profile unchanged.
- **Quantitative claim lacks a source:** omit or mark it for corroboration.
- **Conflicting evidence:** surface the conflict rather than silently overwriting it.
- **Private source unavailable:** report the blocked capability areas without guessing.

## Example

~~~text
/skill career-evidence-refresh
Refresh my canonical professional profile from verified evidence added since the last review.
~~~
