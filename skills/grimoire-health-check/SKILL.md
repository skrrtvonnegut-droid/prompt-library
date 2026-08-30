# Grimoire Health Check

## Purpose

Refresh Grimoire health signals, investigate non-green findings, record a historical health run, and reconcile the operator dashboard only when visible state changes.

## Use When

Use this skill for a weekly or ad hoc Grimoire system-health review, a non-green queue inspection, or a scheduled-task replacement.

## Do Not Use When

Do not use it to redesign the Grimoire, remediate failures without authorization, or run the broader knowledge-maintenance Garden Pass.

## Inputs

- **Runtime configuration** — health signal definitions, observation cadence, historical run store, and operator dashboard.
- **Native signals** — directly observable health from the Grimoire runtime and durable sources.
- **External observations** — configured checks that are due for refresh.
- **Previous run** — the last comparable historical snapshot.

## Dependencies

- Read access to configured health sources.
- Execution access for due observations.
- Write access to the historical run store and operator dashboard.
- A private configuration source for environment-specific endpoints and identifiers.

## Classification

The reusable method and status taxonomy are **Public**. Endpoint details, private source identifiers, health evidence, incidents, and operational topology retain their source classification.

## Procedure

### 1. Resolve the current health contract

Fetch current signal definitions, due-observation rules, status taxonomy, previous run, and dashboard state. Do not rely on remembered configuration when the canonical source is available.

### 2. Refresh health evidence

Refresh native health signals and execute only external observations that are due. Record timestamps, evidence source, freshness, and whether a check was direct, inferred, or unavailable.

### 3. Inspect the non-green queue

Review all findings in **attention**, **degraded**, **critical**, or **unknown** state. Investigate unexpected changes far enough to establish the affected component, evidence, scope, and confidence. Diagnosis does not authorize remediation.

### 4. Compare with the prior run

Identify newly non-green, recovered, unchanged, stale, and ambiguous findings. Do not label missing evidence as healthy.

### 5. Record and project

Create one historical health-run record. Reconcile the operator dashboard only when visible state changed. Preserve the historical record even when dashboard publication fails.

### 6. Report concisely

Return overall status, changes since the prior run, every non-green finding, evidence freshness, and any action requiring separate approval.

## Output Contract

~~~markdown
# Grimoire Health Check

**Overall:** green | attention | degraded | critical | unknown

## Changes Since Prior Run
- New:
- Recovered:
- Unchanged:

## Non-Green Findings
- Component:
  - Status:
  - Evidence:
  - Freshness:
  - Scope:
  - Confidence:

## Durable Result
- Historical run:
- Dashboard updated:

## Attention Required
- Approval or follow-up:
~~~

## Guardrails

- Never infer healthy state from a missing, stale, or blocked check.
- Never remediate or make architecture changes without separate authority.
- Never expose private topology, endpoint details, or identifiers in a public artifact.
- Preserve historical runs rather than rewriting past health.

## Failure Handling

- **Health contract unavailable:** return blocked without inventing checks.
- **Observation unavailable:** mark the signal unknown and identify the missing dependency.
- **Historical write failure:** return the live result but state that the run was not durably recorded.
- **Dashboard write failure:** preserve the run and report projection drift.

## Example

~~~text
/skill grimoire-health-check
Run the current health review and report non-green findings.
~~~
