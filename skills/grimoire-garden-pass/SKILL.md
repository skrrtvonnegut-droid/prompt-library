# Grimoire Garden Pass

## Purpose

Run low-risk maintenance across a versioned Grimoire control plane and its living-memory projection: review knowledge queues, reconcile bridges, inspect backup health, repair a bounded amount of high-confidence metadata drift, record the pass, and surface work requiring approval.

## Use When

Use this skill for a weekly or ad hoc Garden Pass, developing-knowledge review, control-plane drift check, or backup-health inspection.

## Do Not Use When

Do not use it for destructive cleanup, broad architecture redesign, automatic public publication, bulk metadata rewriting, or remediation whose intended state is not already defined.

## Inputs

- **Control plane** — canonical manifest and its referenced operating procedures, classification policy, migration playbook, and backup/recovery contract.
- **Living memory** — configured knowledge queues, migration gaps, bridge registry, Garden Pass history, and backup log.
- **Recent work** — authorized conversation and repository changes that may contain distillable or versionable candidates.
- **Maintenance limits** — default to at most five high-confidence legacy metadata repairs per pass.

## Dependencies

- Read access to the current versioned control plane and connected living-memory system.
- Write access to the configured Garden Pass log and low-risk maintenance targets.
- A private configuration source for page, database, and repository selectors.
- Configured backup destinations when backup health is expected to be green.

## Classification

The reusable procedure is **Public**. Invocation-time content retains its source classification. Personal Private and Employer Confidential material must remain within their approved boundaries; Secrets are never valid garden content.

## Procedure

### 1. Load the current control plane

Start with the canonical manifest and follow its declared paths. Read the current Garden Pass, work-knowledge migration, classification, backup, and recovery procedures rather than relying on remembered versions.

### 2. Inspect living-memory queues

Review developing knowledge, active learning, work-knowledge review, migration gaps, bridge status, prior Garden Pass history, and backup/recovery records. Search before creating or repairing.

### 3. Review recent work for candidates

Identify material that may deserve distillation into living knowledge or versioning into a repository. Treat recent conversation as evidence, not as authority to bypass canonical routing or classification.

### 4. Enforce the data membrane

Never publish or personally back up Employer Confidential or Personal Private content outside defined rules. Never store secret values. When classification is ambiguous, choose the more restrictive route and surface it.

### 5. Perform bounded maintenance

Perform only low-risk internal maintenance whose intended state is already defined. Repair no more than five high-confidence legacy metadata records per pass. Leave ambiguous records unchanged.

### 6. Inspect backup health

Treat unconfigured storage as a blocker, not healthy state. Unless the current control plane defines newer thresholds, flag:

- versioned source snapshots older than 8 days;
- living-memory or control-plane exports older than 35 days;
- conversation exports or recovery drills older than 100 days.

Do not claim backup success from configuration alone.

### 7. Record and report

Create one dated Garden Pass log entry with current health, counts, observations, actions, provenance, and approval-required work. Re-fetch it and return a concise prioritized summary.

## Output Contract

~~~markdown
# Grimoire Garden Pass

## Health
- Overall:
- Control-plane revision:
- Bridge status:
- Backup status:

## Queues and Counts
- Developing knowledge:
- Active learning:
- Work review:
- Migration gaps:

## Actions
- Distilled or versioned:
- Metadata repaired:
- Links or registry reconciled:

## Approval Required
1.
2.

## Durable Record
- Garden Pass log:
- Failed or deferred steps:
~~~

## Guardrails

- Never make destructive or public-facing changes automatically.
- Never exceed the bounded metadata-repair limit.
- Never move restricted data across the membrane for convenience.
- Never mark an unverified backup as healthy.
- Preserve ambiguous records until their intended state is known.

## Failure Handling

- **Canonical manifest unavailable:** stop durable maintenance and return a blocked report.
- **Storage unconfigured:** record a backup blocker; do not improvise a destination.
- **Ambiguous metadata:** leave it unchanged.
- **Partial maintenance:** record exactly what changed and what remains.
- **Log write unavailable:** return the result but state that the pass was not durably recorded.

## Example

~~~text
/skill grimoire-garden-pass
Run one low-risk Garden Pass using the current canonical control plane.
~~~
