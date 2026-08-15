# Audience-Aware Internal Knowledge Base Writer

## Purpose

Transform dense technical documentation, vendor material, internal notes, screenshots, support articles, PDFs, or rough subject-matter expertise into a clear **internal knowledge base article** designed for a specific audience.

Use this when the goal is not simply to document a procedure, but to help someone understand:

- what something is,
- why it exists,
- how it works,
- why it behaves the way it does,
- what distinctions matter,
- what they need to know for their role,
- and what they can safely ignore.

This prompt is especially useful for translating technical information for audiences with very different levels of technical familiarity, such as:

- non-technical employees,
- business users,
- frontline or manufacturing employees,
- managers,
- HR staff,
- Service Desk technicians,
- IT administrators,
- application owners,
- or mixed technical/non-technical audiences.

The goal is:

> **Reduce complexity without removing the information that makes the subject understandable.**

---

# Prompt

Act as a **senior technical writer, knowledge management specialist, and ITIL practitioner** working within an internal IT organization.

I will provide source material about a technical subject.

The material may include:

- vendor documentation,
- Microsoft or other product documentation,
- PDFs,
- technical reference guides,
- support articles,
- screenshots,
- internal documentation,
- architecture notes,
- policies,
- emails,
- meeting notes,
- configuration information,
- subject-matter-expert notes,
- or rough “chickenscratch.”

Convert the supplied information into a clear, accurate, audience-appropriate **internal knowledge base article**.

The purpose of the article is to transfer understanding, not merely reproduce the source material.

Optimize for:

- comprehension,
- technical accuracy,
- useful context,
- concise explanation,
- role relevance,
- knowledge transfer,
- readability,
- and long-term reuse.

Do not oversimplify the material to the point that important distinctions disappear.

Do not preserve complexity merely because the source material is complex.

---

# Knowledge Article Context

## Topic

`[WHAT SHOULD THIS ARTICLE EXPLAIN?]`

## Intended Audience

`[AUDIENCE — e.g. Service Desk, HR, managers, business users, manufacturing employees, IT administrators, mixed audience]`

## Audience Knowledge Level

`[NONE / BASIC / INTERMEDIATE / TECHNICAL / EXPERT / MIXED]`

## Desired Outcome

After reading the article, the audience should be able to:

`[WHAT SHOULD THE READER UNDERSTAND, EXPLAIN, DECIDE, OR DO?]`

## Optional Organizational Context

`[INTERNAL ENVIRONMENT, POLICIES, SERVICES, TERMINOLOGY, OR USE CASE]`

---

# Core Principle

Write for the person who needs to understand the subject, **not for the person who originally documented the technology**.

Ask:

> **What does this audience actually need to understand for this information to become useful?**

Preserve the high-level structure and important technical truth while removing unnecessary cognitive load.

---

# 1. Calibrate to the Audience

Before writing, adjust:

- vocabulary,
- assumed background knowledge,
- depth,
- examples,
- analogies,
- amount of technical detail,
- explanation of acronyms,
- and emphasis

to the specified audience.

Do not merely shorten the same technical explanation for a non-technical audience.

Change the explanation itself.

---

## Example: Non-Technical / Business Audience

Prioritize:

- what the capability does,
- why the organization uses it,
- what the reader experiences,
- what choices or limitations matter,
- and what action they may need to take.

Explain technical terms when unavoidable.

Avoid implementation details that do not affect the reader.

---

## Example: Frontline / Manufacturing Audience

Prioritize:

- observable behavior,
- plain-language explanations,
- concrete examples,
- what the reader needs to recognize,
- what they should or should not do,
- and where to get help.

Avoid abstract architecture language unless it directly helps understanding.

Do not assume familiarity with IT terminology.

---

## Example: HR / Business Operations

Prioritize:

- process implications,
- employee experience,
- licensing or eligibility distinctions,
- ownership,
- timing,
- data considerations,
- and decision-relevant differences.

Explain technology in terms of the business process it enables.

---

## Example: Service Desk

Prioritize:

- conceptual model,
- terminology,
- common distinctions,
- dependencies,
- expected behavior,
- recognizable symptoms,
- what information to collect,
- and when deeper technical escalation may be needed.

Provide enough technical context that technicians understand **why** a troubleshooting step or limitation exists.

Do not turn the article into a runbook unless explicitly requested.

---

## Example: IT Administrator

Preserve greater technical depth.

Include:

- architecture,
- dependencies,
- administration concepts,
- licensing boundaries,
- identity relationships,
- configuration implications,
- and operational considerations

when supported by the source.

---

# 2. Preserve the Important “Why”

Do not reduce the article to:

> Click here, then click there.

When the source supports it, explain:

- why the feature exists,
- why configurations differ,
- why a limitation exists,
- why one license includes something another does not,
- why a process behaves differently under different conditions,
- or why the organization has chosen a particular approach.

Understanding the mechanism helps readers apply the knowledge beyond one specific scenario.

---

# 3. Build a Useful Mental Model

When the topic is complex, begin by giving the reader a simple but accurate model of the subject.

Help answer:

- What is this?
- What problem does it solve?
- What major pieces exist?
- How do those pieces relate?
- Which distinctions actually matter?
- Where do people commonly get confused?

Prefer a strong mental model over a long inventory of facts.

---

# 4. Preserve Important Distinctions

Dense technical documentation often contains differences that are easy to lose during summarization.

Pay particular attention to distinctions such as:

- included vs. add-on,
- licensed vs. enabled,
- available vs. configured,
- authentication vs. authorization,
- user-based vs. device-based,
- standard vs. premium,
- cloud vs. on-premises,
- supported vs. technically possible,
- policy vs. implementation,
- entitlement vs. actual access,
- feature availability vs. organizational permission.

Explain distinctions that materially affect the reader.

Do not preserve irrelevant technical differences merely for completeness.

---

# 5. Translate, Do Not Merely Summarize

Do not reproduce the source document in shorter form.

Instead:

1. identify the important concepts,
2. determine what matters to the intended audience,
3. reorganize the information around comprehension,
4. explain necessary context,
5. remove irrelevant depth,
6. preserve consequential caveats,
7. and create a coherent article.

The resulting structure does not need to mirror the source.

---

# 6. Preserve Source Accuracy

Distinguish clearly between:

### Confirmed

Directly supported by the supplied source material.

### Inferred

A reasonable interpretation of the source but not explicitly stated.

### Internal Context

Information supplied about how the organization uses or implements the technology.

### Unknown

Something the available material does not establish.

Do not silently convert inference into vendor fact.

---

# 7. Do Not Invent Missing Information

Do not fabricate:

- product capabilities,
- licensing rights,
- support boundaries,
- configuration,
- organizational policies,
- business rules,
- technical limitations,
- ownership,
- escalation paths,
- or vendor recommendations.

When material is incomplete, say so.

Use language such as:

> The supplied material does not establish whether this feature is enabled in the organization's environment.

This distinction is especially important when explaining vendor capabilities versus internal implementation.

---

# 8. Separate Product Capability from Organizational Implementation

Where relevant, distinguish between:

### Product / Vendor Behavior

What the source documentation establishes about the technology itself.

### Organizational Configuration

How the organization currently uses, configures, restricts, licenses, or supports it.

### Local Process

What users or staff are expected to do within the organization.

Do not assume that because a vendor feature exists, the organization:

- owns it,
- licenses it,
- enables it,
- permits it,
- or supports it.

---

# 9. Explain Acronyms and Technical Terms

On first meaningful use, define unfamiliar terminology appropriate to the audience.

Example:

> **Conditional Access** is a Microsoft Entra feature that evaluates conditions such as the user, device, location, or risk before allowing access.

Do not repeatedly define common terms once established.

For technical audiences, avoid unnecessarily explaining foundational concepts they are reasonably expected to know.

---

# 10. Use Examples Strategically

When useful, include a short concrete example.

Examples are especially valuable for explaining:

- licensing differences,
- role distinctions,
- authentication flows,
- permission models,
- process behavior,
- conditional logic,
- or abstract technical concepts.

Keep examples realistic and simple.

Do not invent examples that could be mistaken for actual organizational policy.

Label hypothetical examples when necessary.

---

# 11. Use Comparisons When They Improve Understanding

For topics involving multiple products, plans, roles, options, or configurations, use a comparison table where appropriate.

Example:

| Capability | Option A | Option B | Why It Matters |
|---|---|---|---|
|  |  |  |  |

Do not create false binary distinctions when the source is more nuanced.

For licensing comparisons, preserve caveats and dependencies that materially affect entitlement.

---

# 12. Layer the Information

When the audience may contain readers with different levels of interest, structure the article so the essential information appears first.

A useful pattern is:

### What You Need to Know

The core explanation.

### How It Works

Deeper conceptual detail.

### Important Details / Exceptions

Nuance needed by readers who work more closely with the subject.

### Technical Reference

Optional deeper material for technical audiences.

Do not force every article into these exact headings.

Use them when they improve comprehension.

---

# Knowledge Article Structure

Adapt the structure to the subject rather than mechanically filling every section.

---

# [ARTICLE TITLE]

Create a clear title based on what the reader is trying to understand.

Prefer:

> Microsoft 365 E3 vs. E5: What the Differences Mean for Our Users

over:

> Microsoft Licensing Information

when the source supports that specificity.

---

## 1. Summary

In 2–4 sentences explain:

- what the article covers,
- who it is for,
- and why the information matters.

A reader should quickly be able to determine whether the article is relevant.

---

## 2. What You Need to Know

Explain the essential concept in accessible language.

Answer the most important questions first.

For many articles this should cover:

- what it is,
- why it exists,
- and what matters most to the target audience.

---

## 3. Why It Works This Way

Explain relevant reasoning, architecture, design intent, product behavior, policy logic, or business context.

This section should help the reader understand rather than memorize.

Omit it when the source does not establish enough information to explain the underlying reason accurately.

---

## 4. How It Works

Explain the major components, process, or technical relationship at the appropriate depth for the audience.

Use:

- short subsections,
- bullets,
- diagrams,
- examples,
- or comparison tables

where helpful.

Do not introduce technical depth that does not improve understanding.

---

## 5. Key Concepts / Terminology

Define terms the reader needs to understand the subject.

Use only meaningful terms.

Do not create a glossary of every acronym appearing in the source.

---

## 6. Important Differences or Scenarios

Use this section when the topic involves:

- product tiers,
- licensing,
- roles,
- user types,
- configurations,
- environments,
- conditions,
- or multiple paths.

Make the distinction and **why it matters** explicit.

---

## 7. Examples

Provide one or more short examples when they materially improve comprehension.

Clearly distinguish hypothetical examples from actual organizational configuration.

---

## 8. What This Means for You

Translate the technical information into role-specific implications.

For example:

### For Employees

What changes or matters in normal use.

### For Managers

What matters when requesting or approving something.

### For Service Desk

What they should understand when supporting the capability.

### For Administrators

What matters operationally.

Only include audiences relevant to the article.

---

## 9. Common Questions / Misunderstandings

Where supported, address likely confusion.

Examples:

- “Does having the license mean the feature is automatically enabled?”
- “Why can one user do this while another cannot?”
- “Is this the same thing as MFA?”
- “Does this apply to shared accounts?”

Answer only questions that are genuinely useful.

Do not generate a filler FAQ.

---

## 10. Limitations / Important Caveats

Preserve caveats that materially affect interpretation.

Examples may involve:

- licensing,
- platform support,
- dependencies,
- organizational restrictions,
- feature availability,
- exceptions,
- or incomplete source information.

Do not bury important limitations in footnotes or vague prose.

---

## 11. Related Actions or Procedures

If the knowledge naturally connects to a procedure, link or refer to the relevant:

- SOP,
- runbook,
- request process,
- service catalog item,
- support article,
- vendor documentation,
- or escalation process

when that resource is supplied or known.

Do not duplicate a full operational procedure inside the knowledge article unless necessary.

This article explains **understanding**.

A runbook or SOP documents **execution**.

---

## 12. Sources / References

List the source material used where useful.

Examples:

- vendor documentation,
- product guides,
- internal standards,
- support documentation,
- policy documents,
- or supplied technical notes.

Do not invent citations or URLs.

When several sources disagree, surface the disagreement rather than silently choosing one.

---

## 13. Confidence and Gaps

### Confirmed from Source

Important facts directly established by the supplied material.

### Internal / Context-Specific

Information describing the organization's implementation or process.

### Inferred

Interpretations used to aid explanation but not explicitly established.

### Missing / Needs Validation

Questions or facts that should be confirmed before the article is considered authoritative.

---

# Special Mode: Dense Vendor Documentation

When the source is a large technical document, PDF, licensing guide, support page, or set of vendor references:

Do not attempt to reproduce the entire document.

Instead:

1. identify the user's knowledge goal,
2. find the sections relevant to that goal,
3. extract consequential information,
4. preserve important caveats,
5. resolve terminology,
6. reorganize it around the audience's needs,
7. and explain the resulting model clearly.

If the source contains more detail than the article needs, leave it in the source.

A knowledge article is an interface to complexity, not a duplicate of it.

---

# Special Mode: Chickenscratch / SME Notes

When the source is informal or incomplete:

- preserve useful technical insight,
- remove conversational clutter,
- organize related observations,
- distinguish known behavior from personal interpretation,
- identify unexplained assumptions,
- and flag information that needs validation.

Do not penalize informal notes for being informal.

Extract the knowledge they contain.

---

# Difference from an Operational Runbook

Do **not** automatically turn this article into a troubleshooting or procedural runbook.

A runbook primarily answers:

> **What steps should I execute?**

This knowledge article primarily answers:

> **What is happening, why does it work this way, and what do I need to understand about it?**

Include procedural steps only when they materially support comprehension or the requested knowledge outcome.

If the supplied material would be better documented as a runbook or SOP, note that briefly after the article rather than silently changing the artifact type.

---

# Formatting Requirements

- Use Markdown.
- Use clear, descriptive headings.
- Prefer short paragraphs.
- Use bullets for discrete concepts.
- Use comparison tables when they improve comprehension.
- Define unfamiliar terminology.
- Use examples where useful.
- Keep technical terminology when it carries important meaning.
- Remove jargon that adds no precision.
- Avoid unnecessary corporate language.
- Avoid writing down to non-technical readers.
- Avoid unnecessary depth for expert audiences.
- Preserve important caveats and exceptions.
- Write in second person when directly addressing reader actions or implications; otherwise use the clearest natural explanatory voice.

---

# Final Quality Check

Before returning the article, verify that:

- the article is calibrated to the specified audience,
- technical complexity has been translated rather than merely shortened,
- the core conceptual model remains accurate,
- important distinctions have survived simplification,
- vendor capability and organizational implementation are not conflated,
- acronyms and terminology are appropriate for the audience,
- the explanation includes useful “why” when supported,
- procedural detail has not overwhelmed knowledge transfer,
- source uncertainty remains visible,
- important caveats have not disappeared,
- examples do not masquerade as organizational policy,
- and the reader should leave knowing more than a list of facts.

Ask:

> **Could this person explain the important idea back to someone else after reading this?**

If yes, the knowledge transfer worked.

---

# Source Material

Provide or attach any combination of:

- vendor documentation,
- PDFs,
- support articles,
- internal documentation,
- screenshots,
- technical notes,
- policy material,
- SME notes,
- rough observations,
- or pasted source text.

`[SOURCE MATERIAL]`
