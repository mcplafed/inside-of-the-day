# Inside of the Day #10 - Give the model the file

## Title

**I gave the model the file, not my memory of the file.** (Attach the source, quote first)

## First-person thesis

I used to paraphrase a document from memory, or paste one fragment of it, and let the
model fill in the gaps - then chase the errors that crept in. Now I hand it the actual
source and ask it to quote the relevant passage first, before it answers. The model
starts from the real text instead of my lossy recollection of it.

## Mechanism

- The model can only reason over what's actually in front of it. A paraphrase or a
  single fragment is a lossy copy; the real file is the ground truth.
- Two moves: put the source itself in the prompt (attach the file / paste the whole
  document), and for long inputs put it near the top, above the question. Then ask the
  model to **quote the relevant passage first** and answer from that quote.
- Quoting first anchors the answer to a specific passage you can see and check, rather
  than to a confident guess.

## Impact

- **Quality + risk reduction (primary):** the answer is grounded in the actual source,
  so it's far less likely to be a fluent invention, and the supporting quote makes it
  checkable.
- **Less re-explaining (secondary):** you stop reconstructing the document from memory
  every time you want to ask about it.

## Evidence

All wording verified against live vendor docs on 2026-07-21.

- **Anthropic - Prompting best practices, long context (Documented; read directly).**
  Verbatim: *"Put longform data at the top: Place your long documents and inputs near
  the top of your prompt, above your query, instructions, and examples. This improves
  performance across all models."* And: *"Ground responses in quotes: For long document
  tasks, ask Claude to quote relevant parts of the documents first before carrying out
  its task."*
- **Query placement improvement (Measured; illustrative).** Verbatim: *"Queries at the
  end can improve response quality by up to 30 percent in tests, especially with
  complex, multidocument inputs."* This is a vendor test result about *query placement*
  on complex multi-document inputs - cite it as illustrative, not a guaranteed gain.
- **Anthropic - Reduce hallucinations (Documented).** Verbatim: *"Use direct quotes for
  factual grounding: For tasks involving long documents (>20k tokens), ask Claude to
  extract word-for-word quotes first before performing its task. This grounds its
  responses in the actual text, reducing hallucinations."* Also: *"Always validate
  critical information, especially for high-stakes decisions."*
- **Anthropic - Citations (Documented).** Verbatim: *"Citations return the exact
  passages that support each claim, so you can verify answers and surface sources to
  your users."*
- **OpenAI - File inputs (Documented; wording via summarizer - RE-VERIFY at publish).**
  OpenAI models can accept files/PDFs as input (e.g. `input_file` items in the Responses
  API), confirming the "attach the real source" habit isn't Anthropic-only.

## Caveats

- Attaching the file helps only when the answer **is** in the file - it won't rescue a
  question the document can't answer.
- Attach the **relevant** source, not everything you own. Dumping a giant, mostly
  irrelevant archive for a one-line lookup just wastes context and can bury the passage
  that matters.
- Grounding reduces error; it doesn't eliminate it. For high-stakes facts, still
  validate.

## Sources

- Anthropic, "Prompting best practices" (long context) - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, "Reduce hallucinations" - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic, "Citations" - https://platform.claude.com/docs/en/build-with-claude/citations
- OpenAI, "File inputs" - https://developers.openai.com/api/docs/guides/pdf-files *(wording retrieved via summarizer - re-read live at publish)*

## Visual contract

- Eyebrow: `Inside of the Day #10 — Give the model the file`.
- Headline: **I gave the model the file, not my memory of it.**
- Left panel ("My memory of it"): a torn scrap / remembered fragment with a gap → a
  plausible but unverifiable answer.
- Right panel ("The actual source"): the full document with a highlighted quote →
  a grounded answer.
- Mechanism strip: put the source at the top and ask it to quote the passage first;
  the answer is grounded in the real text, not a paraphrase.
- Measured note: query-at-the-end / docs-first improved quality up to 30% in tests
  (illustrative).
- Takeaway: give the model the source, not your memory of the source.
- Caveat line: attach only relevant material; a giant irrelevant archive wastes context.
- Footer: Anthropic long-context + reduce-hallucinations + citations, verified date, `@vitalylobachev`.

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 downscaled feed-legibility probe.
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3).
