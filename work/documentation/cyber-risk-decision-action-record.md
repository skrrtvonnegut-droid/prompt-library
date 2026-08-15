# Cyber Risk Conversation → Decision & Action Record

## Purpose

Turn a messy conversation about a cybersecurity risk, incident, vulnerability, or remediation effort into a clear operational record of:

- what happened,
- what is known,
- what remains uncertain,
- where the team aligned,
- what decisions were made,
- what actions remain open,
- who owns them,
- and what risk remains.

Use this for Teams chats, Slack threads, email chains, meeting transcripts, incident-room conversations, or other collaborative discussions where important decisions and commitments are buried inside informal conversation.

## Prompt

Act as a cybersecurity governance and operational documentation analyst.

Analyze the conversation I provide and turn it into a structured **Cyber Risk Decision & Action Record**.

Your goal is not merely to summarize the discussion. Reconstruct the operational state of the issue so that someone who was not part of the conversation can understand:

- the risk being discussed,
- the relevant evidence and context,
- what remediation has already occurred,
- what the team agreed to do,
- what remains unresolved,
- and what needs to happen next.

### Analysis Instructions

As you review the conversation:

1. Identify the primary cybersecurity risk, incident, vulnerability, control gap, or remediation effort being discussed.
2. Separate **confirmed facts** from:
   - assumptions,
   - speculation,
   - proposed explanations,
   - and unresolved questions.
3. Identify relevant technical evidence, observations, affected systems, users, controls, or dependencies.
4. Reconstruct the remediation work already completed or currently underway.
5. Identify explicit decisions made during the conversation.
6. Identify areas where participants clearly aligned, even when no formal decision language was used.
7. Identify disagreements, competing interpretations, or areas where alignment was not reached.
8. Extract every open action item that appears to require follow-up.
9. Assign an owner only when ownership is explicitly stated or can be directly supported by the conversation.
10. Capture deadlines, target dates, dependencies, blockers, or required approvals when stated.
11. Identify residual risk that remains after completed or proposed remediation.
12. Surface missing information that prevents the issue from being considered resolved.
13. Do not invent owners, deadlines, technical conclusions, or decisions to make the record appear more complete.

If information is ambiguous, preserve the ambiguity and label it clearly.

## Output Format

### 1. Executive Summary

Provide a concise description of:

- the issue,
- its current operational state,
- the most important remediation or decision,
- and whether meaningful risk remains open.

### 2. Risk / Issue Statement

Describe the cybersecurity concern in clear operational terms.

Include, where available:

- affected system or service,
- threat or control gap,
- business or security impact,
- scope,
- and current status.

### 3. Confirmed Facts & Evidence

List only information that is directly supported by the conversation.

For each significant item, include the supporting evidence or observation when available.

### 4. Assumptions, Hypotheses & Open Questions

Separate anything that has not yet been confirmed.

Clearly distinguish between:

- working assumptions,
- possible root causes,
- unresolved technical questions,
- and information still required.

### 5. Remediation Activity

Document remediation discussed or performed.

For each activity, identify:

- **Action**
- **Status** — Proposed / In Progress / Completed / Blocked
- **Owner** — if explicitly known
- **Result or expected outcome**
- **Dependencies or blockers**

### 6. Decisions & Team Alignment

Capture meaningful decisions separately from general discussion.

For each item include:

- **Decision or area of alignment**
- **Rationale**
- **Participants involved**, when relevant
- **Conditions or caveats**

If the conversation contains competing views that were not resolved, document them rather than forcing consensus.

### 7. Open Action Items

Produce an action register using the following fields:

| Action | Owner | Priority | Due Date | Dependency / Blocker | Status |
|---|---|---|---|---|---|

Use `Not specified` when the source does not provide a value.

Do not infer an owner or deadline.

### 8. Residual Risk

Describe what risk remains after the remediation and decisions captured above.

Include:

- unresolved exposure,
- temporary mitigations,
- accepted risk,
- monitoring requirements,
- or conditions that could cause the issue to recur.

If the available information is insufficient to assess residual risk, state that explicitly.

### 9. Items Requiring Follow-Up or Escalation

Identify anything that requires:

- technical validation,
- management decision,
- security approval,
- vendor response,
- change management,
- further investigation,
- or confirmation from another team.

### 10. Record Quality Check

Before finishing, verify that:

- facts are not mixed with assumptions,
- proposed actions are not presented as completed,
- owners and deadlines were not invented,
- disagreement has not been rewritten as consensus,
- unresolved risk remains visible,
- and every meaningful commitment in the source conversation appears in the action register.

## Source Conversation

Paste the conversation, transcript, email thread, or collaborative discussion below:

`[SOURCE CONVERSATION]`
