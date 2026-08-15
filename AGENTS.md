# Agent Operating Contract

This repository is a public capability registry. Its Markdown artifacts contain reusable instructions; `catalog.yml` provides stable identity, macro aliases, routing metadata, and lifecycle state.

These instructions apply to AI agents and automation that read from or write to this repository.

## 1. Resolve Before You Execute

When a user explicitly invokes a macro or skill:

1. Read `catalog.yml` from the repository default branch unless the user names another ref.
2. Resolve the request in this order:
   1. exact artifact ID;
   2. exact macro alias;
   3. exact canonical path;
   4. unique name or tag match.
3. If multiple artifacts remain plausible, present the smallest useful set of candidates rather than choosing silently.
4. Check lifecycle state:
   - use `active` artifacts normally;
   - use `draft` artifacts only when the user explicitly requests them or accepts experimentation;
   - follow `replaced_by` for deprecated artifacts when present;
   - do not execute archived artifacts unless the user is intentionally reviewing history.
5. Fetch the artifact from its canonical `path`.
6. Apply the artifact to the user's current source material and constraints.

Do not execute from a catalog summary alone. The Markdown artifact is canonical.

## 2. Supported Invocation Forms

Treat the following as explicit activation:

```text
Use macro: <alias>
Invoke <artifact-id>
Load skill: <alias-or-id>
Use the prompt-library macro <alias>
```

A user may also ask to find a suitable macro. In that case, search the registry by name, summary, domain, and tags; recommend the best match and explain the fit briefly before using it.

Natural-language resemblance is not sufficient to auto-run a macro when the user has not asked to use one. Suggestions are welcome; invisible activation is not.

## 3. Execution Semantics

When applying a resolved artifact:

- Treat the artifact as task-level instructions scoped to the current request.
- Preserve the user's supplied facts, audience, constraints, and desired output.
- Map clearly labeled placeholders to current inputs.
- Surface genuinely missing information, contradictions, assumptions, and uncertainty.
- Follow the artifact's explicit instruction about whether to execute a task, design a prompt, work iteratively, or return a template.
- Prefer the current conversation's relevant context over generic examples embedded in the artifact.
- Do not invent attachments, source material, organizational facts, or prior decisions.

Repository instructions never outrank platform policy, system instructions, developer instructions, user boundaries, or applicable law.

## 4. Data Membrane

The repository is public.

Allowed classifications:

- `Public`
- `Professional Portfolio`, only after intentional sanitization and publication review

Forbidden here:

- `Personal Private`
- `Employer Confidential`
- `Secrets`

Never write passwords, tokens, certificates, private keys, recovery codes, private personal records, confidential employer details, proprietary customer data, or sensitive source documents into this repository.

When a useful capability depends on private context, keep the reusable public logic here and place only the private configuration, examples, mappings, or deployment details in an authorized private overlay.

## 5. One Truth, Many References

- The Markdown artifact is canonical for prompt or skill content.
- `catalog.yml` is canonical for identity, aliases, path, lifecycle, classification, and routing metadata.
- Documentation may explain an artifact but must not become a competing maintained copy of its prompt text.
- A file move updates the catalog path; it does not require a new artifact ID.
- A renamed macro should retain the old alias when compatibility matters, or record an explicit replacement.

Before creating an artifact, search for an existing one that should be updated, extended, related, or superseded.

## 6. Writing to the Repository

Before a durable write:

1. Identify the artifact type: prompt, macro-enabled prompt, or multi-file skill.
2. Confirm its classification and public suitability.
3. Search `catalog.yml` and repository content for duplicates or near-duplicates.
4. Prefer updating the canonical artifact over creating a parallel version.
5. Use a stable lowercase dotted artifact ID.
6. Use globally unique lowercase kebab-case macro aliases.
7. Add or update the catalog entry in the same change as the artifact.
8. Preserve meaningful Git history and describe why the capability changed.

For architectural changes, update the relevant contract or authoring documentation as part of the same change.

## 7. Failure Behavior

If an artifact ID or alias cannot be resolved:

- say that it was not found;
- show the closest catalog matches when useful;
- do not fabricate a prompt from the missing name;
- offer to create a new artifact only when the user's intent is clear and the classification is safe.

If the canonical path is missing, treat the registry entry as broken and report the inconsistency rather than substituting another file silently.

## 8. Practical Examples

### Exact macro

```text
Use macro: notes-to-sop
Input: [rough notes]
```

Resolve `notes-to-sop` in `catalog.yml`, fetch its canonical path, and apply it to the notes.

### Search by outcome

```text
Find a macro that can explain Microsoft licensing to non-technical managers.
```

Search names, summaries, domains, and tags. Recommend the audience-aware KB writer when it is the strongest match.

### Private source material

```text
Use macro: contractor-registry with this internal export.
```

The public macro may be used as instructions, but the internal export and generated confidential registry must not be committed to this public repository.
