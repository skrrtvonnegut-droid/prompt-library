# Microsoft 365 Admin Brief

## Purpose

Produce a source-backed briefing on consequential Microsoft 365 administration changes from the preceding seven days, emphasizing operational impact, security posture, rollout state, deadlines, and concrete administrator actions.

## Use When

Use this skill for a weekly or ad hoc Microsoft 365 admin briefing across Entra ID, Intune, Exchange Online, Defender for Office 365 and email security, Power Automate, and relevant Power Platform administration.

## Do Not Use When

Do not use it for tenant-specific health telemetry, incident response, unsupported roadmap speculation, or a general Microsoft news roundup.

## Inputs

- **Time window** — default to the preceding seven days.
- **Service scope** — default to identity, endpoint management, messaging, email security, licensing, deprecations, defaults, rollout timing, and automation.
- **Optional prior brief** — used to avoid repeating unchanged items.
- **Optional tenant profile** — licensing and prerequisites may refine relevance, but private tenant details must remain private.

## Dependencies

- Current web access.
- Authoritative Microsoft sources whenever available, including Microsoft Learn, Message Center documentation, Microsoft 365 Roadmap, product blogs, and official lifecycle notices.
- A prior brief or tracking source when deduplication across weeks is required.

## Classification

The reusable method and public source synthesis are **Professional Portfolio**. Tenant configuration, licensing inventories, incident history, internal risk acceptance, and organization-specific actions retain their source classification.

## Procedure

### 1. Establish the evidence window

Define the exact seven-day interval and retrieve current authoritative Microsoft material. Distinguish publication date from the date a change was announced, began rollout, reached general availability, or takes effect.

### 2. Filter for consequence

Include changes that materially affect:

- operations or administrator workflow;
- identity governance or access control;
- endpoint management or compliance;
- mail flow or email security;
- licensing, prerequisites, or entitlement;
- defaults, deprecations, retirements, or deadlines;
- Power Automate or Power Platform administration.

Exclude minor feature noise, consumer-only items, low-impact UI changes, and unchanged items already covered.

### 3. Verify status and scope

For each candidate, verify the affected service, tenant population, prerequisites, rollout state, dates, and official source. Clearly label:

- announced;
- rolling out;
- generally available;
- deprecated or retiring.

When official sources conflict or timing differs by tenant, preserve the uncertainty.

### 4. Explain operational meaning

For each meaningful change, state what changed, why it matters, who is affected, risks, deadlines, and concrete actions. Separate immediate action from monitor-only items.

### 5. Build the watchlist

End with a short prioritized watchlist for the coming week. Rank by deadline, blast radius, security impact, and likelihood of administrator effort.

## Output Contract

~~~markdown
# Microsoft 365 Admin Brief

**Window:** YYYY-MM-DD → YYYY-MM-DD

## Microsoft Entra ID
### Consequential change title
- **Status:**
- **What changed:**
- **Why it matters:**
- **Affected tenants / prerequisites:**
- **Risk:**
- **Action:**
- **Source:**

## Microsoft Intune
Repeat the change structure for consequential Intune items.

## Exchange Online and Email Security
Repeat the change structure for consequential messaging and email-security items.

## Automation and Power Platform
Repeat the change structure for consequential automation and platform-administration items.

## Prioritized Watchlist
1.
2.
3.
~~~

## Guardrails

- Prefer primary Microsoft sources and link every material claim.
- Never present roadmap timing as guaranteed tenant timing.
- Never expose private tenant details in a public briefing.
- Never repeat unchanged items merely to fill sections.
- Never invent licensing, rollout, deadline, or security impact.
- Treat third-party commentary as supplemental, not authoritative.

## Failure Handling

- **No consequential change in a service:** say so briefly rather than adding noise.
- **Official status unclear:** label the uncertainty and avoid prescriptive action.
- **Prior brief unavailable:** deduplicate within the current evidence window and disclose that cross-week comparison was unavailable.
- **Web access unavailable:** do not generate a current briefing from memory.

## Example

~~~text
/skill m365-admin-brief
Brief consequential Microsoft 365 administration changes from the last seven days.
~~~
