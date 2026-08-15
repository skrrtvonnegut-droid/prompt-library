# IT Documentation Toolkit

This folder contains reusable prompts for turning fragmented technical knowledge into documentation that can survive beyond the person who originally understood the system.

The prompts are designed around a simple idea:

> **Different documentation exists to answer different questions.**

A design document, runbook, SOP, and knowledge article may describe the same technology, but they serve different purposes and audiences.

Rather than using one generic “write documentation” prompt for everything, this toolkit separates those documentation types so the resulting artifact is shaped around how the information will actually be used.

---

## Documentation at a Glance

| Document Type | Primary Question | Typical Use | Typical Audience |
|---|---|---|---|
| **Design Document** | How is this solution built, and why? | Architecture, design review, implementation planning, technical handoff | Engineers, administrators, architects, technical managers |
| **Runbook** | What do I do when this condition occurs? | Troubleshooting, incident response, recovery, recurring operational tasks | Service Desk, operations engineers, administrators |
| **Standard Operating Procedure (SOP)** | How should this organizational process be performed? | Repeatable business or technical processes, governance, auditability | Process owners, IT staff, business teams, auditors |
| **Knowledge Base Article** | What do I need to understand about this topic? | Education, explanation, support context, translating complex information | Any audience, from non-technical employees to administrators |

A useful shorthand is:

> **Design documents explain the solution.**  
> **Runbooks operate the solution.**  
> **SOPs execute the process.**  
> **Knowledge articles explain the knowledge.**

---

# Why Separate the Documentation Types?

Technical documentation often becomes difficult to use because several purposes get mixed into a single artifact.

An architecture document slowly accumulates troubleshooting steps.

A troubleshooting article becomes an unofficial process.

A process document starts explaining product architecture.

Eventually the reader has to search through a large document to figure out which information actually applies to the task in front of them.

Separating documentation by intent keeps each artifact focused.

For example, imagine an organization implements a new identity-management workflow.

The same service might reasonably have all four documentation types:

### Design Document

Explains:

- architecture,
- components,
- integrations,
- identity flow,
- security boundaries,
- design decisions,
- dependencies,
- risks,
- and validation criteria.

### Runbook

Explains:

- how to recognize common failures,
- what diagnostic evidence to collect,
- how to troubleshoot the workflow,
- what remediation steps are safe,
- how to verify service restoration,
- and when to escalate.

### SOP

Explains:

- who initiates the process,
- what approvals are required,
- which teams perform each action,
- what records must be maintained,
- how completion is verified,
- and how exceptions are handled.

### Knowledge Base Article

Explains:

- what the workflow does,
- why it exists,
- how the major pieces interact,
- what terminology means,
- what users or support teams need to understand,
- and where common misunderstandings occur.

The underlying technology is the same.

The **knowledge need is different**.

---

# ITIL and Documentation

These prompts are influenced by ITIL service-management principles, but they are intended to be practical rather than ceremonial.

ITIL does not require every organization to produce a giant library of rigid documents. The more useful idea is that knowledge should support the lifecycle of a service: designing it, introducing change safely, operating it, restoring it when something fails, and improving it over time.

Good documentation reduces the amount of operational knowledge that exists only inside someone's head.

That matters because IT services rarely remain static.

People change roles. Vendors change products. Configurations evolve. Incidents occur months after an implementation. A technician who was not part of the original project may eventually need to understand why a particular decision was made.

Documentation creates continuity between those moments.

---

## Knowledge Management

Knowledge Management is the clearest connection across this entire folder.

Useful knowledge should be:

- understandable,
- appropriately detailed,
- easy to locate,
- trustworthy,
- reusable,
- and maintained over time.

This means documentation should not merely record information.

It should make that information **usable by the next person**.

The prompts in this folder therefore emphasize:

- intended audience,
- evidence quality,
- contextual explanation,
- explicit uncertainty,
- reusable structure,
- and preserving technically meaningful details.

They also intentionally discourage fabricated completeness.

If the available information does not establish something, the documentation should say so.

---

## Incident Management

Incident Management focuses on restoring normal service when something fails or becomes degraded.

The **Break/Fix Runbook Builder** supports this by converting troubleshooting history into a repeatable operational procedure.

A good runbook helps an engineer determine:

1. Does this incident match the documented failure pattern?
2. What evidence should I collect?
3. What should I check first?
4. What decision does each result lead to?
5. What corrective action is safe?
6. How do I verify service restoration?
7. When should I stop and escalate?

The runbook therefore emphasizes:

> **diagnose → decide → act → verify**

rather than simply preserving a list of commands that happened to work once.

---

## Problem Management

Restoring service and understanding why the incident occurred are not necessarily the same thing.

A restart may restore an application without establishing why it failed.

A configuration change may remove a symptom without demonstrating root cause.

The runbook prompt therefore separates:

- symptoms,
- immediate failure conditions,
- remediation,
- probable cause,
- and confirmed root cause.

That distinction supports Problem Management by preventing successful recovery from being mistaken for complete understanding.

Over time, repeated runbooks and incident records can also reveal opportunities for:

- permanent remediation,
- monitoring,
- automation,
- architectural improvement,
- or elimination of recurring work.

---

## Change Enablement

Changes to production systems introduce risk.

The **Design Document Builder** therefore treats implementation as more than a configuration exercise.

Where supported by the source material, the design should make visible:

- dependencies,
- testing,
- pilot strategy,
- operational impact,
- validation criteria,
- rollout considerations,
- security implications,
- support readiness,
- and rollback or contingency requirements.

The goal is not to add bureaucracy to every change.

The goal is to make the consequences of the design understandable before the organization depends on it.

---

## Service Design

Service Design asks broader questions than:

> Does the configuration work?

A technically functional solution may still be difficult to:

- support,
- monitor,
- maintain,
- secure,
- troubleshoot,
- or transition between teams.

The design-document prompt therefore includes operational considerations alongside technical architecture.

A useful design should help someone understand both:

> **How does this solution work?**

and:

> **What will it take to keep this solution working?**

---

## Continual Improvement

Documentation should not be treated as a static artifact created once at project completion.

Incidents reveal missing troubleshooting knowledge.

Support requests reveal confusing terminology.

Operational work exposes weak ownership or repetitive manual steps.

Changes reveal assumptions that were never formally documented.

Those discoveries can feed back into:

- design documentation,
- runbooks,
- SOPs,
- knowledge articles,
- monitoring,
- automation,
- or the service itself.

In that sense, documentation becomes part of the improvement loop rather than merely an archive of past decisions.

---

# The Four Prompts

## ITIL-Aligned Design Document Builder

**File:** `itil-aligned-design-document-builder.md`

Use this when source material describes a technical solution, architecture, implementation, or proposed change.

It transforms screenshots, implementation notes, configuration details, and design observations into a structured document covering areas such as:

- current state,
- proposed state,
- architecture,
- design decisions,
- dependencies,
- assumptions,
- risks,
- security,
- operational impact,
- change considerations,
- and validation.

A major design principle of the prompt is maintaining clear evidence boundaries between:

- **Confirmed**
- **Inferred**
- **Assumed**
- **Unknown**
- **Proposed**

This helps prevent incomplete technical notes from turning into confidently invented architecture.

---

## ITIL-Aligned Break/Fix Runbook Builder

**File:** `itil-aligned-break-fix-runbook-builder.md`

Use this when a technical issue has been investigated and resolved, but the troubleshooting knowledge still exists primarily as:

- ticket notes,
- commands,
- screenshots,
- logs,
- chat messages,
- or someone's memory.

The prompt reconstructs the troubleshooting logic into a repeatable operational workflow.

Its emphasis is not simply:

> Here is the fix.

It is:

> Here is how to determine whether this is the same problem, how to investigate it safely, what the evidence means, how to remediate it, and how to verify recovery.

It also preserves useful failed approaches when they prevent future engineers from repeating the same diagnostic dead end.

---

## Raw Notes to Standard Operating Procedure

**File:** `raw-notes-to-sop.md`

Use this when the subject is an organizational process rather than primarily a system failure or technical architecture.

The SOP builder focuses on:

- process triggers,
- roles,
- responsibilities,
- prerequisites,
- required inputs,
- procedural steps,
- decision points,
- exceptions,
- completion criteria,
- records,
- audit evidence,
- and governance controls.

Its core model is:

> **clear ownership + explicit actions + observable evidence**

Although it lives in this IT documentation folder, the underlying workflow is broadly applicable to business processes outside IT as well.

---

## Audience-Aware Internal Knowledge Base Writer

**File:** `audience-aware-internal-kb-writer.md`

Use this when the primary objective is **understanding**.

The source material might be:

- vendor documentation,
- product PDFs,
- support articles,
- licensing guides,
- internal documentation,
- technical notes,
- screenshots,
- or informal SME knowledge.

The writer then adapts that information for a specified audience such as:

- business users,
- manufacturing employees,
- HR,
- managers,
- Service Desk,
- administrators,
- or mixed audiences.

The prompt attempts to preserve the important technical model while changing how that model is explained.

A Service Desk technician and a manufacturing employee may need to understand the same technology, but they do not need the same explanation.

The core principle is:

> **Translate complexity rather than merely shortening it.**

---

# Choosing the Right Artifact

When deciding which prompt to use, start with the question the reader needs answered.

### “How was this built?”

Use a **Design Document**.

### “Something is broken. What should I do?”

Use a **Runbook**.

### “How are we supposed to perform this process?”

Use an **SOP**.

### “What is this, and why does it work this way?”

Use a **Knowledge Base Article**.

Sometimes a mature service will need all four.

That is not duplication when each artifact serves a different operational need.

---

# Shared Design Principles

Although the prompts produce different artifacts, they share several principles.

## Preserve Uncertainty

Missing information should remain visible.

The prompts prefer language such as:

- Confirmed
- Inferred
- Assumed
- Suspected
- Proposed
- Unknown
- Needs validation

over quietly filling gaps with plausible-looking information.

---

## Optimize for the Next Person

Documentation should make sense to someone who:

- was not in the meeting,
- did not build the system,
- did not troubleshoot the original incident,
- and does not know what the original author “obviously meant.”

This is one of the simplest tests of useful operational documentation.

---

## Preserve the Why

Procedural instructions are easier to apply when the reader understands the reason behind them.

Where the source material supports it, these prompts preserve:

- design rationale,
- diagnostic reasoning,
- business context,
- dependencies,
- and important technical distinctions.

---

## Avoid Documentation Theater

More sections do not automatically create better documentation.

These prompts intentionally avoid inventing:

- controls,
- approvals,
- ownership,
- severity,
- timelines,
- architectural details,
- or policies

simply because a template contains a field for them.

Documentation should describe the service and process that actually exist—or clearly identify what remains unknown.

---

## Keep Knowledge Maintainable

A useful document should be:

- structured enough to scan,
- concise enough to maintain,
- detailed enough to trust,
- and explicit enough to hand off.

The objective is not maximal documentation.

It is **useful operational knowledge**.

---

# A Simple Documentation Lifecycle

These artifact types can also reinforce one another.

A new service might begin with:

**Design Document**  
↓  
explains architecture and implementation

**Knowledge Base Articles**  
↓  
teach users and support teams how the capability works

**SOPs**  
↓  
formalize recurring organizational processes around the service

**Runbooks**  
↓  
capture operational and incident-response knowledge

**Incidents, feedback, and operational experience**  
↓  
feed improvements back into all four

This creates a lightweight knowledge lifecycle:

> **design → teach → operate → learn → improve**

---

# About This Toolkit

These prompts grew out of practical documentation needs rather than an attempt to reproduce formal ITIL templates.

The recurring problem was usually the same:

> Important operational knowledge existed, but it was scattered across screenshots, ticket notes, vendor documentation, conversations, configuration consoles, and people's heads.

The prompts are designed to help reconstruct that knowledge into artifacts that are easier to:

- review,
- maintain,
- transfer,
- audit,
- and use.

They are intentionally written to work across different AI assistants and are designed as **natural-language workflows rather than platform-specific prompt tricks**.

Feel free to adapt them to your environment, documentation standards, or service-management practices.

The important part is not the exact template.

It is knowing **what question the document is supposed to answer**.
