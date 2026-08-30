# Grimoire Daily Tao

## Purpose

Create a source-verified, journal-ready Daily Tao section using a deterministic 81-chapter cycle, a brief copyright-safe quotation, a grounded lesson, a practical orientation, an open reflection, and citations.

## Use When

Use this skill when the user asks for today's Daily Tao, a Daily Tao journal entry, or the deterministic entry for a named calendar date.

## Do Not Use When

Do not use it for an invented quotation, generic motivational content, a random Taoist saying, or a broad chapter commentary that ignores the journal-ready format.

## Inputs

- **Date** — default to the user's current local calendar date.
- **Timezone** — required when the current date could differ from the runtime date.
- **Optional translation preference** — use only when the requested text can be quoted lawfully and verified.

## Dependencies

- Current web access for source verification.
- An academically useful source for chapter identity and classical Chinese, preferably Chinese Text Project.
- A verifiably public-domain English translation for direct quotation, such as James Legge, preferably confirmed through a reputable archive.

If exact wording or attribution cannot be verified, choose another compliant passage or report the limitation.

## Classification

The reusable method and public-domain source references are **Public**. Any journal destination, private reflection, or personal practice context retains its source classification.

## Procedure

### 1. Select the chapter deterministically

Use the date's ordinal day:

~~~text
chapter = ((day_of_year - 1) mod 81) + 1
~~~

Use the user's local date, including leap-year day numbering. Do not explain the algorithm in the finished journal entry.

### 2. Verify the chapter and text

Browse current sources. Confirm the chapter number and passage against an authoritative or academically useful source and a reputable public-domain translation when practical.

Never invent or reconstruct a quotation from memory. If using a modern copyrighted translation for interpretive comparison, paraphrase its contribution rather than reproducing its wording.

### 3. Choose a brief quotation

Quote only the shortest passage needed to anchor the entry. Identify chapter and translator. Preserve important paradox or ambiguity rather than selecting a line merely because it resembles a motivational slogan.

### 4. Write the lesson

Let the selected chapter determine the lesson. Keep it grounded, thoughtful, and usable in ordinary life without turning it into productivity advice, therapeutic cliché, mystical filler, or a simplistic moral.

### 5. Complete the journal section

Write:

- the verified quotation;
- a 100–175 word lesson;
- a one- or two-sentence orientation for the day;
- one genuinely open-ended reflection question;
- a source line with chapter, translator, reliable online source, and citations.

Return only the journal-ready section unless the user asks for analysis.

## Output Contract

~~~markdown
### ☯ Daily Tao

> “A brief verified quotation”

— Tao Te Ching, Chapter N, translated by Translator

**Lesson**

One hundred to 175 words grounded in the selected chapter.

**For Today**

One or two practical orientation sentences.

**Reflection**

One open-ended question.

**Source:** Chapter, translation, reliable source, and citations.
~~~

## Guardrails

- Never fabricate wording, attribution, chapter numbering, or citations.
- Never quote a copyrighted modern translation beyond a short compliant excerpt.
- Never flatten Taoism into generic positivity or self-optimization.
- Never claim one translation exhausts the text's meaning.
- Keep private journal context out of the public registry.

## Failure Handling

- **Chapter mismatch across sources:** investigate numbering differences and identify the convention used.
- **Translation status unclear:** choose a verified public-domain translation.
- **Web access unavailable:** do not quote from memory; return a blocked source-verification note.
- **Date ambiguous:** resolve the user's timezone before selecting the chapter.

## Example

~~~text
/skill daily-tao
Create today's journal-ready entry.
~~~
