# Inside of the Day #9 - Examples beat adjectives

## Title

**I stopped describing the style I wanted. I started showing it.** (Examples beat adjectives)

## First-person thesis

I used to write a line of adjectives - "professional, concise, structured" - and
hope the model understood what I meant, then fight the output when it didn't. Now I
put 3-5 concrete examples of the thing I want right next to the task and say "make
the next one like these." The output gets more consistent because the target is
visible instead of abstract.

## Mechanism

- A model matches patterns far more reliably than it interprets adjectives.
  "Professional" is a word each of us fills in differently; three examples pin down
  the exact format, tone, and edge cases with no interpretation gap.
- Show the target instead of narrating it: put the examples beside the task, then ask
  for the next output in the same shape.
- This is one specific swap - adjectives → examples - not "write better prompts."

## Impact

- **Quality + repeatability (primary):** output lands closer to the target and stays
  consistent across runs, because every run is anchored to the same visible pattern.
- **Cognitive load (secondary):** you stop re-wording an abstract description you
  can't verify and start pointing at a concrete one you can.

## Evidence

All wording verified against live vendor docs on 2026-07-21.

- **Anthropic - Prompting best practices, "Use examples" (Documented; read
  directly).** Verbatim: *"Examples are one of the most reliable ways to steer
  Claude's output format, tone, and structure. A few well-crafted examples (known as
  few-shot or multishot prompting) improve accuracy and consistency."* The page states
  a specific count: *"Include 3–5 examples for best results."* On variety, the
  "Diverse" bullet reads: *"Cover edge cases and vary enough that Claude doesn't pick
  up unintended patterns."*
- **OpenAI - Prompt engineering, "Few-shot learning" (Documented; wording via
  summarizer - RE-VERIFY at publish).** Verbatim as retrieved: *"Few-shot learning
  lets you steer a large language model toward a new task by including a handful of
  input/output examples in the prompt, rather than fine-tuning the model."* OpenAI
  frames it as "a handful" of examples and does **not** state a fixed count.

## Caveats

- Examples must be **relevant and varied**. Near-identical examples teach a narrow,
  wrong pattern; off-target examples teach an off-target style. Anthropic's own
  guidance is to vary them "so Claude doesn't pick up unintended patterns."
- For a genuine one-off ask, assembling examples isn't worth the effort - this pays
  back on outputs you produce repeatedly.
- The "3-5" figure is Anthropic's stated recommendation; OpenAI says "a handful" with
  no number. Treat it as guidance, not a hard rule.

## Sources

- Anthropic, "Prompting best practices" (Use examples / multishot) - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting
- OpenAI, "Prompt engineering" (Few-shot learning) - https://developers.openai.com/api/docs/guides/prompt-engineering *(wording retrieved via summarizer - re-read live at publish)*

## Visual contract

- Eyebrow: `Inside of the Day #9 — Examples beat adjectives`.
- Headline: **I stopped describing the style. I started showing it.**
- Left panel ("Describe it"): a row of adjective chips (`professional · concise ·
  structured`) → an off-target, mismatched output.
- Right panel ("Show it"): three example cards (`like these →`) → an output that
  matches the pattern.
- Mechanism strip: examples are one of the most reliable ways to steer format, tone,
  and structure - include 3-5.
- Takeaway: show the pattern instead of describing it.
- Caveat line: examples must be relevant and varied; bad examples teach bad patterns.
- Footer: Anthropic prompting best practices, OpenAI few-shot, verified date, `@vitalylobachev`.

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 downscaled feed-legibility probe.
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3).
