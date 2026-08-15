# Prompt Library Archaeologist

## Purpose

Search a body of conversations, notes, documents, or prior AI interactions for **reusable prompts and workflows worth preserving**.

Use this when you have accumulated a lot of useful AI work over time but the valuable parts are buried inside:

- chat histories
- project notes
- one-off requests
- copied prompts
- working sessions
- documentation
- or repeated natural-language workflows

The goal is not to save everything.

The goal is to identify the pieces that have become **small reusable systems**.

---

## Prompt

Act as a prompt archaeologist and workflow curator.

Analyze the source material I provide and identify prompts, instructions, interaction patterns, or repeated workflows that are strong candidates for preservation in a reusable prompt library.

Look beyond messages that are explicitly labeled as prompts.

Some of the best candidates may appear as:

- repeated instructions
- successful conversational workflows
- natural-language automations
- recurring analysis patterns
- structured ways of transforming one kind of input into another
- or a sequence of user corrections that gradually produced a better reusable method

Your job is to recover the underlying reusable system.

Do not simply extract every instruction you find.

---

## Core Principle

Look for places where the conversation contains something like:

> **When I give an AI this kind of input, I want it to reliably perform this kind of transformation.**

That transformation is the thing worth preserving.

---

## 1. Identify Candidate Workflows

Search the source material for patterns such as:

### Input → Structured Output

Examples:

- conversation → decision record
- notes → meeting agenda
- export → governance registry
- logs → health digest
- journal entries → pattern analysis
- rough writing → voice-preserving revision
- source material → study guide

### Repeated Analysis Methods

Examples:

- identifying risks and unresolved questions
- separating facts from assumptions
- translating activity into outcomes
- surfacing recurring patterns
- comparing current state with desired state
- finding automation opportunities
- reviewing something against a consistent rubric

### Reusable Interaction Modes

Examples:

- tutor
- reviewer
- writing partner
- troubleshooting companion
- research analyst
- reflective mirror
- prompt engineer
- implementation planner

### Natural-Language Automations

Look for instructions that effectively describe a small recurring process:

> “Whenever I give you X, inspect it for Y, then produce Z.”

These are especially strong candidates.

---

## 2. Reconstruct the Underlying Prompt

A useful workflow may be spread across several messages.

Reconstruct it from:

- the original request
- later clarifications
- user corrections
- examples of good output
- rejected approaches
- recurring preferences
- and constraints discovered through use

Give later explicit corrections more weight than earlier assumptions.

Do not preserve accidental quirks merely because they appeared in one successful response.

---

## 3. Remove One-Off Context

Separate the reusable mechanism from the specific situation that produced it.

Remove or generalize things such as:

- name

* internal systems
* personal details
* temporary project names
* specific dates
* private incidents
* organization-specific terminology

Replace them with:

- generic descriptions
- clearly labeled placeholders
- or optional context fields

Preserve domain-specific detail when it is essential to the usefulness of the prompt.

Do not generalize a specialized prompt until it becomes meaningless.

---

## 4. Preserve the Important Constraints

Look carefully for corrections that reveal what the prompt **must not do**.

Examples:

- do not invent missing owners
- preserve uncertainty
- do not flatten disagreement into consensus
- preserve the writer's voice
- do not exaggerate routine work
- do not diagnose from journal entries
- do not solve every problem with automation
- do not rewrite previously approved material

Negative constraints often encode lessons learned through actual use.

Treat them as valuable design information.

---

## 5. Distinguish Prompts from Mere Requests

Not every useful response implies a reusable prompt.

A candidate is stronger when it:

- applies to a recurring class of problems
- has a recognizable input
- produces a useful and repeatable outcome
- contains meaningful judgment or structure
- can survive outside the original conversation
- and would save effort or improve consistency when reused

A request is weaker when it:

- depends almost entirely on one specific situation
- is trivial to express again
- contains no meaningful workflow
- or would require nearly complete rewriting for another use

Prefer quality over volume.

---

## 6. Detect Prompt Families

When several prompts appear to solve closely related problems, determine whether they are:

- genuinely different prompts
- variants of one reusable template
- or examples of a broader prompt family

For example:

- daily status summary
- weekly manager update
- monthly operations review

may share a deeper pattern:

> **Operational activity → outcome-oriented management reporting**

Identify these relationships without automatically merging prompts that have meaningfully different purposes.

---

## 7. Evaluate Candidate Quality

Assess each candidate using the following dimensions:

### Reusability

Can it apply to multiple future situations?

### Outcome Clarity

Is it clear what useful result the prompt should produce?

### Input Clarity

Is it clear what the user needs to provide?

### Judgment Value

Does the prompt encode useful reasoning rather than only formatting?

### Constraint Quality

Does it guard against common failure modes?

### Portability

Can it work across AI platforms with little modification?

### Distinctiveness

Does it represent something more useful than a generic “act as an expert” prompt?

### Maturity

Has the workflow been refined through actual use, corrections, or repeated application?

---

## 8. Assign a Maturity Level

Classify each candidate as:

### Seed

A promising idea that has only been used once or remains loosely defined.

### Working

A reusable workflow with a clear purpose and reasonable structure.

### Proven

A workflow that has been used repeatedly or substantially refined through feedback.

### Foundational

A broadly useful prompt or framework that can support many other prompts.

Do not inflate maturity merely because a prompt is long or detailed.

---

## 9. Recommend a Library Location

Suggest a logical location using the existing library taxonomy when available.

Example categories may include:

- `templates/`
- `work/documentation/`
- `work/governance/`
- `work/microsoft-365/`
- `work/reporting/`
- `writing/journaling/`
- `writing/rewriting/`
- `writing/creative-writing/`
- `learning/`
- `meta/`

If no existing category fits naturally, recommend a new category only when several candidates justify it.

Do not create a new folder for every edge case.

---

## Output Format

### 1. Archaeology Summary

Briefly describe:

- the kinds of reusable workflows found
- the strongest recurring design patterns
- and the overall quality of the source material as a prompt library candidate

Keep this concise.

---

### 2. Candidate Inventory

Create a table:

| Candidate | Core Transformation | Suggested Folder | Maturity | Priority |
| --------- | ------------------- | ---------------- | -------- | -------- |

Use:

**Priority**

- High
- Medium
- Low

Prioritize candidates based on usefulness, reusability, and distinctiveness.

---

### 3. Candidate Details

For each **High** or **Medium** priority candidate, provide:

#### Candidate Name

A concise reusable title.

#### Original Pattern

Explain where the workflow appeared and what the user was trying to accomplish.

Do not reproduce sensitive source material unnecessarily.

#### Reusable Core

State the underlying transformation:

> `[INPUT] → [PROCESS / JUDGMENT] → [OUTPUT]`

#### Important Constraints

List the lessons or guardrails that should survive into the reusable prompt.

#### Suggested Inputs

What a future user would need to provide.

#### Suggested Output

What the reusable prompt should produce.

#### Why It Is Worth Preserving

Explain what makes it more useful than simply asking the AI the task from scratch.

---

### 4. Prompt Families

Identify clusters of related candidates.

For each family, explain:

- the common underlying pattern
- which prompts should remain separate
- and whether a shared template may eventually be useful

Do not merge them automatically.

---

### 5. Candidates to Leave Buried

Identify notable instructions or workflows that **should not** be migrated.

Give a short reason such as:

- too specific
- too trivial
- privacy-sensitive
- redundant
- weakly tested
- dependent on unavailable context
- or better represented by another candidate

This section is important.

A good archive is partly defined by what it refuses to preserve.

---

### 6. Recommended Excavation Order

Recommend which prompts should be reconstructed first.

Favor a small, diverse starting set that demonstrates the character of the library.

For each recommendation, explain briefly why it should come before the others.

---

## Optional Reconstruction Mode

If I ask you to reconstruct a candidate, turn it into a standalone reusable Markdown prompt.

Use a structure such as:

- Title
- Purpose
- Prompt
- Analysis or operating instructions
- Output format
- Important constraints
- Input placeholder

Preserve the useful lessons discovered in the original conversations while removing private or one-off context.

Do not publish, save, or modify the prompt library unless I explicitly ask you to.

---

## Final Quality Check

Before finishing, verify that:

- repeated workflows were recognized even when they were not labeled as prompts
- later corrections were incorporated
- private context was not unnecessarily reproduced
- generic requests were not promoted simply to increase the candidate count
- negative constraints and failure modes were preserved
- similar prompts were compared for possible overlap
- maturity reflects actual evidence
- and the strongest candidates represent reusable systems rather than clever wording

Prefer:

> **a small collection of prompts that encode real lessons**

over:

> **a large archive of things someone once asked an AI to do**

The purpose of prompt archaeology is not preservation for its own sake.

It is to discover which conversations accidentally became tools.

---

## Source Material

Paste, attach, or provide access to the conversations, notes, documents, exports, or other material you want searched:

`[SOURCE MATERIAL]`
