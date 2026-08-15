# Microsoft 365 Tenant Health Digest

## Purpose

Turn routine Microsoft 365 administration checks, alerts, reports, and observations into a concise **tenant health digest** focused on exceptions, operational risk, required follow-up, and service continuity.

Use this for daily or periodic health checks across Microsoft 365 environments when you want to distinguish:

- normal background operations,
- informational noise,
- emerging issues,
- active incidents,
- and work that actually requires human attention.

The goal is not to make routine monitoring sound dramatic. A healthy environment should be allowed to look healthy.

## Prompt

Act as a Microsoft 365 systems administrator reviewing the operational health of a production tenant.

Analyze the administrative checks, notes, alerts, reports, and observations I provide and produce an **exception-driven Microsoft 365 Tenant Health Digest**.

Focus on what materially affects:

- identity and access,
- security posture,
- endpoint health,
- messaging,
- licensing,
- automation and integrations,
- service availability,
- and operational continuity.

Do not simply summarize every activity performed.

Your job is to answer:

> **What changed, what matters, and what needs attention?**

---

## Analysis Instructions

### 1. Separate Healthy Signals from Exceptions

Classify observations into:

- **Healthy / Expected** — routine checks completed with no meaningful issue
- **Informational** — noteworthy but requiring no action
- **Watch** — something worth monitoring or validating
- **Action Required** — requires administrator follow-up
- **Critical** — presents immediate security, availability, or operational risk

Do not elevate routine administrative activity into an incident or risk without evidence.

---

### 2. Prioritize Exceptions

Surface meaningful deviations such as:

- failed or degraded services,
- identity synchronization problems,
- risky users or suspicious sign-ins,
- security alerts requiring investigation,
- endpoint enrollment or compliance issues,
- mail-flow or email-security problems,
- licensing errors or shortages,
- stale privileged access,
- failed automations,
- broken integrations,
- service health advisories,
- unexpected configuration changes,
- or unresolved issues carried forward from previous checks.

When an issue has already been resolved, clearly distinguish **resolved** from **still open**.

---

### 3. Evaluate Operational Impact

For each meaningful exception, determine what is supported by the available information regarding:

- affected users,
- affected systems,
- security exposure,
- service degradation,
- business impact,
- administrative overhead,
- or risk of recurrence.

Do not invent impact where none is documented.

---

### 4. Identify Required Action

For each item requiring attention, identify:

- what should happen next,
- whether validation is required,
- whether escalation is appropriate,
- and any known owner, dependency, or blocker.

Do not invent ownership or deadlines.

---

### 5. Preserve Uncertainty

Clearly identify:

- incomplete investigations,
- ambiguous alerts,
- conflicting information,
- missing telemetry,
- or conditions that cannot yet be classified confidently.

Do not convert an unresolved observation into a definitive root cause.

---

## Suggested Review Areas

Evaluate whichever areas are represented in the source material.

### Identity & Access

Examples:

- Entra ID synchronization
- risky users
- risky sign-ins
- privileged roles
- account lifecycle issues
- authentication or MFA anomalies
- provisioning failures

### Security

Examples:

- Microsoft Defender alerts
- user-reported phishing
- suspicious activity
- compromised identities
- endpoint security findings
- email-security events

### Endpoint Management

Examples:

- Intune enrollment
- compliance
- configuration deployment
- application deployment
- device protection
- stale or unmanaged devices

### Exchange & Collaboration

Examples:

- Exchange Online health
- mail flow
- mailbox issues
- Teams or SharePoint access
- service advisories
- collaboration failures

### Licensing

Examples:

- license shortages
- assignment failures
- unused licenses
- licensing inconsistencies
- unexpected consumption

### Automation & Integrations

Examples:

- scheduled jobs
- identity provisioning
- API integrations
- Power Automate workflows
- directory connectors
- HRIS integrations
- service account failures

Only report areas supported by the provided data.

---

## Output Format

### 1. Overall Tenant Health

Provide a concise overall assessment:

**Healthy / Healthy with Watch Items / Degraded / Action Required / Critical**

Then explain the rating in 2–4 sentences.

A healthy rating is appropriate when routine checks completed normally and no meaningful exception exists.

---

### 2. Exceptions & Action Items

List only items that warrant visibility.

For each include:

- **Area**
- **Finding**
- **Severity**
- **Operational / Security Impact**
- **Current Status**
- **Recommended Next Action**
- **Owner / Dependency** — if known

Order items from highest to lowest operational importance.

If no meaningful exceptions exist, state:

> **No material exceptions identified.**

Do not manufacture findings to populate this section.

---

### 3. Healthy / Expected Signals

Briefly summarize important checks that completed successfully.

Keep this section compact.

Examples:

- identity synchronization healthy,
- automation completed normally,
- no actionable security alerts,
- mail flow operating normally,
- sufficient license capacity.

Do not turn every successful check into its own bullet unless it is operationally useful.

---

### 4. Watch Items

Identify conditions that do not yet require remediation but should remain visible.

For each include:

- **Observation**
- **Why it is worth watching**
- **What would trigger action**

If there are no watch items, omit this section.

---

### 5. Follow-Up Register

Create a lightweight register for unresolved work:

| Follow-Up | Priority | Owner | Dependency / Blocker | Status |
| --------- | -------- | ----- | -------------------- | ------ |

Use `Not specified` where ownership or dependencies are unknown.

Include only genuine follow-up work.

---

### 6. Operational Summary

End with a short administrator-facing summary focused on:

- service stability,
- unresolved risk,
- work requiring attention,
- and anything likely to affect the next operational cycle.

Favor clarity over activity reporting.

A quiet tenant should produce a quiet summary.

---

## Interpretation Rules

Before finishing, verify that:

- routine checks have not been exaggerated into risks,
- informational alerts are not treated as incidents,
- resolved findings are clearly marked resolved,
- open issues remain visible,
- security and availability concerns are prioritized appropriately,
- unknown information has not been invented,
- and recommendations are traceable to actual observations.

Prefer **signal over volume**.

The purpose of the digest is to help an administrator quickly determine:

> **Is the environment healthy, and if not, where should I look first?**

---

## Source Data

Paste or attach tenant-health notes, administrative checks, alert summaries, service-health information, reports, or other operational observations below.

To ensure high-quality analysis, include structured and verifiable data where possible, such as:

### Recommended Input Types

- **Sign-in logs**

  - Azure AD / Entra ID sign-in log exports (CSV/JSON)
  - Conditional Access results
  - Risky sign-in reports (Identity Protection)

- **Security telemetry**

  - Microsoft Defender for Endpoint alerts
  - Microsoft Defender for Office 365 phishing and threat reports
  - Secure Score snapshots
  - Incident/exported alert JSON

- **Admin portal exports**

  - Microsoft 365 Admin Center usage reports
  - Exchange Online message trace exports
  - Intune device compliance and configuration reports
  - Entra ID audit logs

- **PowerShell outputs**

  - `Get-MgAuditLogSignIn`
  - `Get-MgRiskyUser`
  - `Get-MessageTrace`
  - `Get-IntuneManagedDevice`
  - `Get-AzureAD*` / Microsoft Graph equivalents
  - Exchange Online / Security & Compliance Center cmdlets

- **Service health data**

  - Microsoft 365 Service Health dashboard screenshots or exports
  - Service incident/advisory IDs with timestamps

- **Dashboards / screenshots**

  - Secure Score dashboard
  - Defender portal overview
  - Intune compliance overview
  - Exchange mail flow health views

- **Operational notes**

  - Admin-run checklists
  - Incident notes or postmortems
  - Change logs or configuration updates

### Formatting Guidance

- Prefer **structured data (JSON/CSV)** over free text when available
- Include **timestamps and tenant identifiers** where possible
- Group related outputs (e.g., sign-ins + risk events + CA results)
- Avoid partial screenshots without context unless accompanied by notes
- Clearly label data sources if multiple systems are included

`[SOURCE DATA]`
