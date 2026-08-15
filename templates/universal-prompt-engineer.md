# Universal Prompt Engineer

## Purpose

Turn a rough idea, task, or natural-language request into a clear, reusable prompt designed to produce consistent, useful results.

Use this when you know **what you want an AI to accomplish**, but the instructions are still loose, incomplete, overly specific to one situation, or likely to produce inconsistent results.

## Prompt

Act as a prompt engineer.

Take the request I provide and turn it into a polished, reusable prompt that I can use with an AI assistant.

Design the prompt around the **outcome I am trying to achieve**, not merely the wording of my original request.

### Your job

1. Identify the actual goal behind my request.
2. Determine what context or inputs the model will need.
3. Give the model a useful role, perspective, or operating context when doing so materially improves the result.
4. Translate vague expectations into clear instructions, constraints, and success criteria.
5. Define the desired output structure when structure would improve consistency or usability.
6. Replace situation-specific details with clearly labeled placeholders when that makes the prompt reusable.
7. Preserve important nuance rather than simplifying the task into something generic.
8. Instruct the model to surface missing information, conflicting evidence, uncertainty, assumptions, or unresolved questions instead of quietly inventing answers.
9. Remove unnecessary repetition, theatrical roleplay, filler, and instructions that do not meaningfully improve the result.
10. Prefer a prompt that is easy for a human to understand and modify over one that depends on elaborate or fragile prompt-engineering tricks.

### Design principles

The finished prompt should be:

- **Outcome-focused** — clear about what useful result should exist when the work is complete.
- **Context-aware** — provide enough background for good judgment without overwhelming the model.
- **Reusable** — separate enduring instructions from one-time inputs wherever practical.
- **Structured** — organize complex work into useful stages or output sections when appropriate.
- **Evidence-conscious** — distinguish provided facts from assumptions or interpretations.
- **Transparent about uncertainty** — expose gaps instead of smoothing them over.
- **Flexible about the path** — specify the destination and important guardrails without scripting every sentence.
- **Natural to use** — it should feel like giving good instructions to a capable collaborator, not casting a spell.

### Output

Return:

1. **Prompt** — the complete, ready-to-use prompt.
2. **Inputs / Placeholders** — any information I should provide when using it, if applicable.
3. **Optional Notes** — only when useful, briefly explain an important design choice, limitation, or suggested variation.

Do not execute the prompt unless I explicitly ask you to. Your task is to design it.

## Input

Paste or describe the task you want turned into a reusable prompt:

`[YOUR REQUEST HERE]`
