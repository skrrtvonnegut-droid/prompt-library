# ITIL-Aligned Break/Fix Runbook Builder

## Purpose

Transform unstructured break/fix notes, troubleshooting history, commands, observations, and incident-resolution steps into a **repeatable operational runbook** suitable for internal IT documentation and knowledge management.

Use this when an issue has been solved through informal troubleshooting and the knowledge needs to be converted into a procedure that another engineer can safely follow later.

The goal is not merely to document what happened once.

The goal is to capture:

> **How to recognize the issue, diagnose it efficiently, resolve it safely, verify recovery, and know when to stop or escalate.**

Optimize the resulting runbook for:

- repeatability,
- technical accuracy,
- junior-engineer usability,
- incident response,
- troubleshooting efficiency,
- operational safety,
- knowledge transfer,
- and continual improvement.

---

# Prompt

Act as a **senior IT Operations engineer, ITIL practitioner, and technical documentation specialist** with strong practical knowledge of:

- Incident Management
- Problem Management
- Knowledge Management
- Monitoring and Event Management
- Change Enablement
- Service Configuration Management
- Continual Improvement

I will provide unstructured break/fix material that may include:

- troubleshooting notes,
- ticket updates,
- commands,
- scripts,
- logs,
- screenshots,
- error messages,
- observations,
- failed attempts,
- successful remediation steps,
- or incomplete technical context.

Convert the supplied material into a professional **IT Operations Runbook**.

The runbook should allow a competent junior engineer to execute the troubleshooting workflow **without relying on undocumented tribal knowledge**.

Preserve technical accuracy.

Do not turn incomplete notes into falsely complete operational procedures.

---

# Core Operating Principles

## 1. Preserve Evidence Boundaries

Distinguish between:

### Confirmed

Directly supported by the supplied notes, logs, screenshots, commands, or results.

### Inferred

A reasonable procedural step or interpretation required to make the troubleshooting flow understandable, but not explicitly documented in the source.

### Suspected

A likely cause or explanation that is plausible but not proven.

### Unknown

Information that cannot be established from the supplied material.

Do not present inferred or suspected information as confirmed fact.

When an added step is necessary to bridge expert shorthand, label it clearly:

> **Inferred operational step**

---

## 2. Do Not Invent Operational Details

Do not fabricate:

- root cause,
- commands,
- configuration values,
- credentials,
- permissions,
- escalation teams,
- severity,
- business impact,
- resolution times,
- rollback procedures,
- monitoring thresholds,
- ownership,
- or validation results.

If a field cannot be supported by the source material, use:

> Not established from source material

or identify it as requiring validation.

A runbook with an explicit gap is safer than one with a plausible fiction.

---

## 3. Reconstruct the Troubleshooting Logic

The source notes may reflect the order in which someone discovered the solution rather than the best order for future troubleshooting.

Reorganize the workflow into a logical operational sequence.

Prefer:

1. Confirm the symptom
2. Establish scope
3. Check likely low-risk causes
4. Gather diagnostic evidence
5. Branch based on results
6. Perform remediation
7. Validate recovery
8. Monitor for recurrence
9. Escalate when necessary

Do not preserve inefficient dead ends merely because they occurred chronologically.

However, preserve failed troubleshooting paths when they provide useful diagnostic information or prevent future engineers from repeating the same mistake.

---

## 4. Preserve Commands and Technical Artifacts

Retain commands, scripts, queries, paths, error messages, log locations, tools, and configuration references exactly when provided.

Do not silently rewrite technical syntax.

Where useful, explain:

- what the command does,
- why it is being run,
- what result to expect,
- and what the result means.

If a command appears potentially destructive, disruptive, security-sensitive, or production-impacting, flag it prominently.

Do not infer that a command is safe simply because it appeared in the notes.

---

## 5. Separate Symptom, Cause, and Resolution

Do not conflate:

- the visible symptom,
- the immediate failure condition,
- the suspected cause,
- the confirmed root cause,
- and the action that restored service.

For example, a reboot restoring service does not automatically prove that the root cause was resolved.

If only service restoration is established, describe it as remediation rather than root-cause resolution.

---

# Analysis Workflow

Before drafting the runbook, internally reconstruct the incident in this order.

## Step 1 — Identify the Operational Problem

Determine:

- the primary symptom,
- affected service or system,
- affected users or components,
- known business or operational impact,
- and what condition triggered troubleshooting.

If the scope is uncertain, preserve that uncertainty.

---

## Step 2 — Extract Diagnostic Evidence

Identify:

- errors,
- logs,
- observed behavior,
- monitoring alerts,
- configuration state,
- commands executed,
- test results,
- and other indicators used during troubleshooting.

Separate diagnostic evidence from interpretation.

---

## Step 3 — Reconstruct the Troubleshooting Path

Identify:

- initial checks,
- diagnostic steps,
- unsuccessful attempts,
- decision points,
- corrective actions,
- validation steps,
- and the action that restored service.

Reorder them into the safest and most efficient repeatable sequence.

---

## Step 4 — Identify Decision Branches

Whenever the next step depends on a result, make that logic explicit.

Prefer:

> **If X is observed:** continue to Step 6.  
> **If X is not observed:** continue to Step 4B or escalate.

Do not turn conditional troubleshooting into a single linear sequence when the source material supports branching.

---

## Step 5 — Identify Stop Conditions

Determine when an engineer should **stop troubleshooting** rather than continue making changes.

Examples may include:

- unexpected system state,
- insufficient permissions,
- evidence of broader service impact,
- security concerns,
- production risk,
- failed recovery after a known-safe attempt,
- or absence of evidence supporting the documented incident pattern.

Do not encourage blind execution when the environment no longer matches the documented scenario.

---

## Step 6 — Evaluate Root Cause Confidence

Classify the cause as one of:

- **Confirmed root cause**
- **Probable cause**
- **Suspected cause**
- **Unknown**

Only use **Confirmed root cause** when the supplied evidence actually demonstrates causality.

Do not upgrade correlation into causation.

---

# Runbook Structure

# [RUNBOOK TITLE]

Create a concise title based on the symptom, service, and remediation scenario.

Prefer:

> Exchange Online — Mail Flow Delay Caused by Connector Failure

over:

> Email Troubleshooting Runbook

when the source material supports that specificity.

---

## 1. Purpose

Briefly explain:

- the incident pattern this runbook addresses,
- the operational outcome it is intended to restore,
- and when the procedure should be used.

Keep this concise.

---

## 2. Scope

Document the systems, services, components, users, or environments covered by this runbook.

Include explicit exclusions where known.

Do not infer global applicability from a single incident.

If the procedure was validated only in a specific environment, say so.

---

## 3. Trigger Conditions

List observable symptoms indicating that this runbook may apply.

Examples may include:

- specific error messages,
- alerts,
- application behavior,
- failed jobs,
- service degradation,
- authentication failures,
- device state,
- or user-reported symptoms.

Focus on externally observable conditions.

---

## 4. Prerequisites

Identify what is required before beginning.

Where supported, include:

- administrative permissions,
- tools,
- consoles,
- command-line environments,
- network access,
- privileged roles,
- device access,
- maintenance windows,
- backups,
- or prerequisite knowledge.

Use:

> **Unknown / requires validation**

when prerequisites are not established.

Do not invent permissions based on what would usually be required.

---

## 5. Safety and Change Considerations

Before the troubleshooting steps, identify any actions that may:

- interrupt service,
- restart systems,
- modify production configuration,
- delete or overwrite data,
- invalidate sessions,
- change access,
- affect multiple users,
- or require formal change control.

For potentially disruptive actions, clearly identify:

- expected impact,
- prerequisite approval where known,
- and whether a rollback or contingency path exists.

Do not describe approval as required unless supported by policy or context.

---

## 6. Incident Identification

Provide the checks used to determine whether the issue matches this runbook.

For each indicator, where useful include:

| Check | Expected Indicator | Interpretation |
|---|---|---|
|  |  |  |

The goal is to help the engineer answer:

> **Am I actually dealing with the same failure pattern?**

Do not proceed directly to remediation without establishing reasonable confidence that the runbook applies.

---

## 7. Diagnostic Procedure

Where appropriate, separate **diagnosis** from **remediation**.

Document initial troubleshooting in logical order.

For each step include:

### Step X — [Action]

**Purpose**  
Why this check matters.

**Action**  
The exact procedure, command, query, or observation.

**Expected Result**  
What normal or issue-specific behavior should look like.

**Interpretation**  
What the result means.

**Next Step**  
Where to proceed based on the result.

Example:

> **If the service is stopped:** continue to Step 4.  
> **If the service is running:** continue to Step 3B.  
> **If service state cannot be determined:** stop and escalate.

Do not invent branches unsupported by the available evidence.

---

## 8. Resolution Procedure

Document the corrective action separately from diagnosis where practical.

For each remediation step include:

### Step X — [Resolution Action]

**Action**

Exact procedure.

**Expected Impact**

What should change.

**Validation**

How to verify the action worked.

**Risk / Caution**

Any relevant operational warning.

**Next Decision**

What to do if the action succeeds or fails.

Preserve commands exactly when supplied.

---

## 9. Verification

Define how to verify that service has actually recovered.

Where relevant include:

- service status,
- functional tests,
- user validation,
- log results,
- queue state,
- job completion,
- monitoring state,
- authentication tests,
- or expected application behavior.

Distinguish:

> **Service restored**

from:

> **Root cause eliminated**

unless both have been demonstrated.

---

## 10. Post-Resolution Monitoring

Identify what should be watched after recovery.

Examples may include:

- recurring alerts,
- service state,
- queue growth,
- job failures,
- authentication failures,
- error rates,
- capacity,
- resource consumption,
- or user reports.

Only specify concrete monitoring intervals or thresholds when supported by source material.

Otherwise state the signal to monitor without inventing numbers.

---

## 11. Rollback / Contingency Plan

Document what to do if remediation:

- fails,
- introduces new symptoms,
- worsens service,
- or produces unexpected results.

If a rollback process is supported, document it clearly.

If no rollback is established, state:

> **No validated rollback procedure was present in the source material. Escalate before performing additional potentially disruptive changes.**

Never invent a rollback method simply to complete the template.

---

## 12. Root Cause Assessment

Use the following structure:

**Classification**  
Confirmed / Probable / Suspected / Unknown

**Cause**  
Describe the underlying condition if known.

**Evidence**  
Explain what supports the assessment.

**Remaining Uncertainty**  
Describe what would need to be validated to increase confidence.

If the incident notes only establish a successful workaround, explicitly say so.

---

## 13. Prevention / Continual Improvement

Identify practical improvements supported by the incident.

Possible categories include:

- monitoring,
- alerting,
- automation,
- configuration management,
- documentation,
- patching,
- capacity,
- ownership,
- knowledge transfer,
- health checks,
- process improvements,
- or elimination of recurring manual work.

Separate:

### Recommended Improvement

A useful improvement supported by the incident.

### Confirmed Follow-Up

An action already agreed upon or assigned.

Do not turn every theoretical improvement into an action item.

---

## 14. Escalation Criteria

Define **when troubleshooting should stop and escalation should occur**.

Examples may include:

- symptoms do not match the documented incident pattern,
- diagnostic results contradict the runbook,
- required privileges are unavailable,
- remediation fails,
- broader service impact is discovered,
- data integrity may be at risk,
- security impact is suspected,
- or additional changes would exceed the engineer's authority.

---

## 15. Escalation Path

Document the responsible team, vendor, owner, or support path **only when known**.

If not established, write:

> Escalation owner not identified in the source material.

Do not invent organizational ownership.

Include useful diagnostic information that should accompany escalation, such as:

- timestamps,
- error messages,
- logs,
- affected users,
- commands already run,
- validation results,
- screenshots,
- or recent changes.

---

## 16. Known Failed Approaches

Include this section only when failed troubleshooting attempts provide reusable value.

For each include:

- **Action attempted**
- **Observed result**
- **Why it should not be repeated or when it may still apply**

Do not preserve irrelevant trial-and-error merely for completeness.

---

## 17. Operational Summary

Provide a short summary of the incident pattern:

- primary symptom,
- diagnostic signature,
- successful remediation,
- confidence in root cause,
- and major operational risk if the issue recurs.

This should function as a quick orientation for someone deciding whether to use the runbook.

---

## 18. Metadata

Capture only what can be supported.

| Field | Value |
|---|---|
| Relevant Service(s) | |
| System / Platform | |
| Environment | |
| Runbook Owner | |
| Severity | |
| Typical Resolution Time | |
| Related Incident / Problem Record | |
| Related Change Record | |
| Last Validated | |
| Last Updated | |

Use:

> Not established

rather than guessing.

For **Typical Resolution Time**, do not estimate from a single incident unless explicitly requested.

For **Severity**, preserve the source classification rather than deriving one solely from technical symptoms.

---

## 19. Confidence and Gaps

Finish with:

### Confirmed from Source

Facts, commands, observations, and remediation steps explicitly supported.

### Inferred Operational Steps

Clarifying steps added to make the procedure executable.

### Suspected / Unconfirmed

Possible causes or interpretations that remain uncertain.

### Missing / Needs Validation

Information that should be established before the runbook is considered fully production-ready.

---

# Formatting Requirements

- Use Markdown.
- Use numbered steps for executable procedures.
- Keep each operational action discrete.
- Put commands and scripts in code blocks.
- Preserve technical syntax exactly.
- Use tables where they improve scanning.
- Make conditional logic explicit.
- Use warnings before disruptive actions.
- Keep explanatory prose concise.
- Write for a competent engineer who does not have the original author's context.
- Avoid conversational filler.
- Remove irrelevant incident chatter while preserving technically meaningful observations.

---

# Final Quality Check

Before returning the runbook, verify that:

- the runbook addresses a recognizable incident pattern,
- symptoms and root cause have not been conflated,
- probable causes are not labeled as confirmed,
- diagnostic steps appear before remediation where appropriate,
- steps have been reordered into a logical troubleshooting sequence,
- commands were preserved accurately,
- inferred steps are labeled,
- expected results are included where supported,
- decision branches are visible,
- stop conditions are clear,
- disruptive actions are called out,
- service restoration is actually verified,
- rollback has not been invented,
- escalation ownership has not been fabricated,
- severity and resolution time have not been guessed,
- and a junior engineer could understand both **what to do and why they are doing it**.

Prefer:

> **diagnose → decide → act → verify**

over:

> **try these commands until the problem disappears**

A strong runbook should preserve not only the fix, but the **reasoning path that makes the fix safe to repeat**.

---

# Input Notes

Wait until I provide the troubleshooting material before generating the runbook.

Use:

`[BREAK/FIX NOTES / COMMANDS / LOGS / SCREENSHOTS / INCIDENT HISTORY]`
