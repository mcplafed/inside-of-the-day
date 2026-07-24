# Inside of the Day #6 - Prompt caching

## Title

**Put the stable part first.** (Prompt caching)

## Claim

Order every prompt so the stable, repeated context comes first and the changing
content comes last. Both Anthropic and OpenAI serve a matching prefix from cache
at a large discount, so a well-ordered prompt makes every repeat call cheaper and
faster - without changing the model.

## Scope

This is a **harness decision**, not a model upgrade or a prompt-wording trick. It
changes *where* content sits in the request, not *what* you ask. The benefit
appears only on repeated calls that share the same leading bytes (an agent loop,
a chat with fixed system instructions, a pipeline that reuses the same documents).

## Mechanism

- A prompt is sent top to bottom. Caching keys on the **longest identical prefix**
  from the start of the request.
- Put the stable block first: system instructions, tool definitions, few-shot
  examples, project documents. Put the variable tail last: the user's request,
  retrieved chunks, timestamps.
- On a repeat call the leading prefix is a **cache hit** - billed far below the
  normal input rate. Change one byte inside the prefix and it is a **cache miss** -
  the whole prefix is billed at full price again.

## Evidence

All figures verified against the live vendor docs on 2026-07-21.

- **Anthropic (documented):** "Cache reads are 0.1 times the base input tokens
  price" - about a tenth. Cache writes cost 1.25x (5-minute) / 2x (1-hour) of base
  input; default cache lifetime is 5 minutes. Cache hits "require 100% identical
  prompt segments." Minimum cacheable prefix is **1,024 tokens for Claude Opus 4.8
  and Sonnet 5** (differs by model: 4,096 for Haiku 4.5). Pricing table example:
  Opus 4.8 input $5 -> $0.50 per million tokens on a cache read.
- **OpenAI (documented mechanism):** caching "works automatically for eligible
  requests, with no code changes required"; "available for prompts containing 1024
  tokens or more"; "Cache hits are only possible for exact prefix matches"; guidance
  to "place static content like instructions and examples at the beginning of your
  prompt." The ~10x cheaper cached-input rate is **derived from the pricing table**
  (e.g. a current GPT-5.6 model at $5.00 input -> $0.50 cached input), not printed
  as a percentage - so it is stated non-numerically as "about a tenth."
- **Latency (expected / qualitative):** both vendors describe faster
  time-to-first-token from a cache hit, but neither publishes a latency percentage.
  No speed number is claimed.

## Impact

- **Cost (primary):** repeated input on a matched prefix is billed at roughly a
  tenth of the normal input price. The longer and more repeated the stable block,
  the larger the saving.
- **Latency (secondary):** faster first token on a hit - qualitative, no figure.
- **Reproducibility / cognitive load (secondary):** a fixed, ordered prefix is a
  cleaner mental model of the request than ad-hoc prompt assembly.

## Caveats

- Cache reads are **not free** - about 10% of input, not zero.
- Requires an **exact prefix match**; variable content up front breaks the cache.
- Cache writes cost slightly **more** than a normal call, so a prefix has to be
  reused enough to pay back.
- Minimum prefix size, write multipliers, and cache lifetime **vary by model** -
  the visual names Opus 4.8 / Sonnet 5; verify current pricing per model at publish.
- The OpenAI discount is pricing-derived and model-specific; it is stated as "about
  a tenth", never as a fixed universal percentage.

## Sources

- Anthropic, "Prompt caching" - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Anthropic, "Pricing" - https://platform.claude.com/docs/en/about-claude/pricing
- OpenAI, "Prompt caching" - https://developers.openai.com/api/docs/guides/prompt-caching
- OpenAI, "Pricing" - https://developers.openai.com/api/docs/pricing

## Visual contract

- Eyebrow: `Inside of the Day #6 — Prompt caching`.
- Headline: **Put the stable part first.**
- Hero: a single vertical prompt split into a large `STABLE PREFIX · CACHED` block
  and a thin `VARIABLE TAIL · FULL PRICE` block, with a dashed exact-prefix boundary
  between them; "top = sent first" order marker.
- Consequence rail: `Cache hit` (prefix unchanged -> ~0.1x, faster first token) vs
  `Cache miss` (prefix changed -> full price on the whole prefix).
- Mechanism strip: both providers cache on an exact prefix match.
- Caveat line: harness decision, reads still cost ~10%, thresholds vary by model.
- Footer: Anthropic + OpenAI prompt-caching docs, verified date, `@vitalylobachev`.

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 downscaled feed-legibility probe.
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport
  1080x1350, device scale factor 3).
