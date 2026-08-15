# Preserve My Voice

## Invocation

```text
/voice [passage]
```

Natural-language forms:

```text
Make this sound more like me.
Keep my voice, but tighten this up.
```

## Intent

Improve clarity, rhythm, grammar, and structure while preserving the writer's diction, emotional temperature, ambiguity, and characteristic sentence movement.

## Expansion

Resolve and execute `prompt.writing.rewriting.preserve-my-voice` against the user's current passage.

## Defaults

- Make the smallest changes that produce a meaningful improvement.
- Preserve deliberate roughness, uncertainty, intensity, humor, and unusual phrasing when they are part of the voice.
- Do not replace the writer's voice with polished generic prose.

## Output

Return the revised passage first. Add a brief note only when a meaningful choice, ambiguity, or larger structural concern should be surfaced.

## Boundaries

Do not invent autobiographical details, intensify claims, flatten deliberate ambiguity, or expose private context outside the current task.
