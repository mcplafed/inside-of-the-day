# Inside of the Day — Production brief: "Ask for the short version"

> Candidate **T4** from `research/inside-of-the-day-research-v3-harness.md`, expanded
> into a broad-audience production brief. Provisional slot: **#7**. This is a brief,
> not the final infographic. Every quote below was fetch-verified on **2026-07-21**;
> each figure is labelled **Documented** (vendor states it), **Measured** (a published
> example measurement), or **Expected** (mechanism implies it, no vendor number).
>
> **Recommended headline:** **"Ask for the short version."**
> (Backup, if a sharper edge is wanted: *"Name the shape you want."*)

---

## 1. Broad human problem

You ask one small question. The model hands back an essay.

Twelve paragraphs, three headings, a numbered list, a "in summary," and a closing
offer to help further — when all you wanted was the answer. So you skim. You scroll.
The one line that actually mattered is buried in paragraph six, next to four lines
you already knew. You got *more words* and *less answer*.

This is the everyday tax of long output, and it lands on everyone:

- **A person in a chat** loses the thread. The point is in there somewhere, but
  attention is finite and the wall of text spends it before you reach the part you
  needed. Long answers are harder to trust, too — more surface area, more places for
  a wrong sentence to hide.
- **A builder running the model inside an app or a pipeline** pays twice. Output is
  billed by the token, and on most current models output tokens cost *several times*
  more than input. Every extra paragraph the model writes is money — and in an agent
  loop or a long chat, those extra tokens also fill the finite context window, so the
  system forgets sooner and slows down.

The instinct is to blame the model for being chatty. The useful reframe: **length is
a dial you didn't set.** The model guessed how much you wanted and guessed long. You
can just tell it.

---

## 2. One practical choice

**Before you ask, name the shape of the answer you want.**

Not "be concise" as a mood — a concrete container the answer has to fit in:

- **one sentence** — "answer in one sentence."
- **three bullets** — "give me three bullets, no preamble."
- **one paragraph** — "one short paragraph, no headings."
- **decision + reason** — "tell me which one and why, in two lines."
- **full audit** — "walk through every case in detail" — *when depth is the point.*

In a **chat** (ChatGPT, Claude), you do this in plain words: say the shape in the
prompt. In an **app or pipeline** you build, you can set it as a default — OpenAI's
GPT-5 family exposes a `verbosity` control (low / medium / high), and Anthropic
documents asking for conciseness plus a `max_tokens` ceiling. Same idea, two surfaces:
**decide the length instead of accepting the guess.**

The move is not "always shorter." It is "shaped." Sometimes the right shape *is* the
long one (see §5).

---

## 3. Harness mechanism

Why the shape is a real lever and not just a preference:

1. **Output is generated and billed one token at a time.** The model doesn't decide
   the whole answer and then trim it — it emits words until it decides to stop. Ask
   for less and it stops sooner. Length is downstream of your instruction, not a fixed
   property of the model.
2. **Output tokens are a separate, more expensive line item than input.** On current
   flagship pricing tables, output is billed at roughly **6× the input rate** (see
   §4). So a wordy answer is not "a bit more input" — it is the *expensive* half of
   the bill getting bigger.
3. **Every output token also consumes the context window.** In a chat that continues,
   or an agent loop that feeds its own output back in, long answers eat the finite
   space the system has to remember earlier turns. Shorter output leaves more room
   before quality degrades or the window has to be trimmed.
4. **Attention is the scarcest budget of all, and it's yours.** Even when tokens are
   free (a flat-rate chat), a buried answer costs *your* reading time and raises the
   chance you miss the one line that mattered. This benefit needs no pricing table —
   it's simply how reading works.

The dial itself: in the GPT-5 API it's the `verbosity` parameter; with Claude it's a
direct instruction to be concise plus an optional `max_tokens` hard cap. In a consumer
chat, there is **no slider** — the dial is the sentence you type. Either way you are
setting the output shape on purpose instead of letting the model default to long.

---

## 4. Evidence and source links

All URLs fetch-verified (HTTP 200) on **2026-07-21** unless noted.

**OpenAI — the length dial and that output scales with it**
- *GPT-5 New Params and Tools* (OpenAI Cookbook) —
  https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
  — **fetch-verified.**
  - `verbosity` takes **low / medium / high**. Low = *"terse UX, minimal prose,"*
    medium = *"balanced detail"* (default), high = *"verbose, great for audits,
    teaching, or hand-offs."* — **Documented.**
  - *"the verbosity parameter reliably scales both the length and depth of the model's
    output while preserving correctness and reasoning quality—without changing the
    underlying prompt."* — **Documented.**
  - Worked examples of output tokens by level — **Measured, illustrative, two prompts
    only:** a poetry prompt went **560 → 849 → 1,288** output tokens (low → med →
    high); a Python-sorting prompt went **575 → 943 → 2,381.** These are two examples,
    not a guaranteed ratio.

**OpenAI — output is billed separately, and higher, than input**
- *Pricing* — https://developers.openai.com/api/docs/pricing — **fetch-verified.**
  - Per-model tables have separate columns: **Input | Cached input | Cache writes |
    Output.** Output is billed independently of input. — **Documented.**
  - On the flagship example rows, output runs about **6× the input rate** (example
    rows on the page: input $5.00/1M → output $30.00/1M; input $2.50/1M → output
    $15.00/1M). — **Documented (illustrative rates; specific models and numbers change
    — re-verify at publish, cite only the structure "output ≫ input," not a frozen
    figure).**

**Anthropic — controlling response length is documented too (not just OpenAI)**
- *Reducing latency* (Claude Platform Docs) —
  https://platform.claude.com/docs/claude/docs/reducing-latency — **fetch-verified**
  (301 from the old `docs.anthropic.com/claude/docs/reducing-latency`).
  - *"Ask for shorter responses: Ask Claude directly to be concise. If Claude is
    outputting unwanted length, ask Claude to curb its chattiness."* — **Documented.**
  - *"Minimize the number of tokens in both your input prompt and the expected output
    … The fewer tokens the model has to process and generate, the faster the response
    will be."* — **Documented.**
  - On *how* to ask: *"asking for an exact word count or a word count limit is not as
    effective a strategy as asking for paragraph or sentence count limits"* (LLMs count
    tokens, not words). — **Documented.** *(This is why the practical choice in §2 uses
    "one paragraph / three bullets," not "in 50 words.")*
  - `max_tokens` *"set[s] a hard limit on the maximum length of the generated
    response,"* but *"the response will be cut off, perhaps mid-sentence … a blunt
    technique."* — **Documented** (a ceiling, not a shaping tool).
- *Prompting best practices* (Claude Platform Docs) —
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  — **fetch-verified.**
  - Section *"Communication style and verbosity":* *"Claude's latest models have a more
    concise and natural communication style compared to previous models … **Less
    verbose:** May skip detailed summaries for efficiency unless prompted otherwise."*
    — **Documented** (the default already leans concise; you steer from there).
  - Section *"Control the format of responses":* steer by telling Claude the shape you
    want (*"Tell Claude what to do instead of what not to do"*) rather than forbidding
    formats. — **Documented.**

**Note on reachability:** consumer help pages (`help.openai.com`) return 403 to
automated fetch and are not quoted here; every quote above is from a first-party page
that returned 200.

---

## 5. What can honestly be claimed (and what cannot)

**Can claim — attention / cognitive load (the strong, universal claim):**
- Long output buries the answer and costs reader attention; asking for a shape puts
  the point where you can see it. This holds in *any* interface, paid or flat-rate,
  and needs no pricing data — it's how reading and finite attention work. This is the
  headline benefit.
- Length is a controllable dial, not a fixed trait of the model. **Documented** by both
  vendors (OpenAI's `verbosity`; Anthropic's "ask Claude to be concise" + `max_tokens`).
- The *shape* of the ask matters: paragraph/sentence/bullet counts steer better than
  word-count limits. **Documented** (Anthropic).

**Can claim — API token cost (the real but conditional claim, keep it distinct):**
- Output tokens are billed separately from input and, on current flagship models, cost
  **several times more** (≈6× on the example rows). So trimming output cuts the
  *expensive* side of the bill. **Documented** — but present it as structure ("output ≫
  input, per token"), not as a frozen number.
- In multi-turn / agentic use, output also consumes the context window, so shorter
  answers preserve context and delay slowdown/compaction. **Expected** (mechanism;
  neither vendor puts a number on this specific effect).

**Cannot claim (guardrails against overreach):**
- **No universal cost saving.** There is no honest "save X%" number — the saving
  depends on the model, how much shorter you go, and how repeated the call is. The
  560/849/1,288 and 575/943/2,381 counts are **two illustrative prompts**, not a law.
  Do not turn them into a ratio.
- **Not "shorter is always better."** OpenAI's *own* description of high verbosity is
  *"great for audits, teaching, or hand-offs."* Long output is the correct shape for
  teaching a concept, a thorough audit, a handoff document someone else must act on
  without you, and genuinely complex decisions. The claim is *match the shape to the
  job* — not *minimise words.*
- **Not an API feature story.** `verbosity` is a GPT-5-family API parameter; the
  consumer ChatGPT/Claude UI has **no literal slider** — you ask in words. Anthropic
  has no `verbosity` parameter at all; it documents the instruction + `max_tokens`.
  Don't let the post imply a universal button that doesn't exist.
- **`max_tokens` is a guillotine, not a shaper** — it truncates mid-sentence. If the
  post shows a "cap," label it as a hard ceiling, not the recommended way to get a
  short *answer*.

---

## 6. One-image infographic concept

One 1080×1350 canvas, *Operator's Field Notes* style. Structure: **same question,
two answers, side by side.** Nothing else competes with that comparison.

**Eyebrow:** `Inside of the Day #7 — Ask for the short version`

**Headline:** **Ask for the short version.**

**The shared question (top, centred, one line so both sides clearly answer the *same*
thing):** e.g. *"Should we switch our billing to annual?"*

**LEFT panel — "What you usually get":**
- The same question at the top.
- A tall block of dummy "wall of text" (greyed lorem-style lines, a heading, a
  bulleted sub-list) — visibly long, visibly skimmable-not-readable.
- **One line highlighted deep inside it** as *the actual answer*, tagged
  *"← the point, buried."*
- Mood: heavy, crowded.

**RIGHT panel — "What you can ask for":**
- The same question at the top.
- Three tight, useful bullets (a real-feeling decision + reason + caveat), lots of
  whitespace.
- A small tag: *"the action is visible."*
- Mood: light, done.

**Thin explainer strip along the bottom (small, do NOT overcrowd — two facts only):**
- **Attention:** *long answers bury the point — you skim and miss it.*
- **Cost (API):** *output is billed per token, and per token it costs more than input —
  extra words are the expensive half of the bill.*
- A quiet one-liner under both: *long is right for audits, teaching, and hand-offs —
  ask for that when you mean it.*

**Optional micro-detail (only if it doesn't crowd):** a tiny "shapes" chip row between
the panels — `1 sentence · 3 bullets · 1 paragraph · decision+reason · full audit` —
to show the dial has positions, not just "short/long."

**Footer:** source line (OpenAI Cookbook + Anthropic docs), `verified 2026-07-21`,
`@vitalylobachev`.

**Explicitly out:** no token-count bar chart pretending to be a universal ratio, no
API code, no `verbosity` parameter screenshot, no third panel. The whole image is one
before/after and two small "why" facts.

---

## 7. Caption draft (short English LinkedIn caption)

```
INSIDE OF THE DAY #7
Ask for the short version.

You ask one small question. The model hands back an essay — twelve paragraphs, three headings, a summary you didn't ask for. So you skim, and the one line that mattered is buried in paragraph six.

The fix isn't "be concise." It's naming the shape before you ask:
one sentence · three bullets · one paragraph · decision + reason · full audit.

Two reasons it pays off:
- Attention. A shaped answer puts the point where you can see it. A wall of text spends your attention before you reach it.
- Cost, if you build with the API. Output is billed per token, and per token it costs more than input — so extra words are the expensive half of the bill, and in an agent loop they also eat your context window.

Length is a dial you forgot to set. OpenAI's GPT-5 API even exposes it directly (verbosity: low/medium/high); Anthropic documents just asking Claude to be concise. In a normal chat there's no slider — the dial is the sentence you type.

And no, shorter isn't always better. Audits, teaching, and hand-offs want the long version. That's the point: match the shape to the job instead of accepting the guess.

Ask for the shape you actually need.

Sources (verified 2026-07-21):
- OpenAI Cookbook, "GPT-5 New Params and Tools": https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic, "Reducing latency": https://platform.claude.com/docs/claude/docs/reducing-latency
- Anthropic, "Prompting best practices": https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

#InsideOfTheDay #AI #ChatGPT #Claude #Productivity
```

---

## 8. Alternatives and why this is not generic "be concise" advice

**How this is different from "write shorter prompts" / "be concise":**
- Generic advice tells you to *feel* brief. This tells you to hand the model a
  **container** — one sentence, three bullets, decision+reason — so the *output* has a
  defined shape. Anthropic's own guidance backs the mechanism: paragraph/sentence
  counts steer output where "be concise" and word limits don't.
- Generic advice is about *your* input wording. This is about *the model's output*, a
  distinct lever with two distinct payoffs (attention **and**, in API use, token cost +
  context) — and it names when *not* to use it.

**Adjacency check against the existing series (from the harness doc):**
- **#6 Prompt caching** is about the *input* prefix order and *repeat-call* cost. T4 is
  about the *output* side and *single-call* attention/cost. State the split if both are
  ever referenced: caching = cheaper *input on repeats*; short version = less
  *expensive output* + a readable answer now.
- **#1 Model × effort** picks the *operating point*; T4 picks the *output shape* at any
  operating point. No overlap.
- **#4 Review the work / T3 verify** are about trusting output; T4 is about *sizing* it.
  A wall of text is harder to verify, so T4 is complementary, not a repeat.

**Alternative framings considered and set aside:**
- *"Turn down verbosity"* — rejected: makes it an OpenAI-API-parameter story and
  excludes chat users and Claude, who have no such parameter. Fails the broad test.
- *"Long answers cost you money"* — rejected as the lead: true only in API use and only
  as structure, not a number; leading with it invites a fake universal cost figure and
  loses the flat-rate chat user. Cost is the *secondary* beat, attention is the lead.
- *"Prompt like a pro / write better prompts"* — rejected: vague, no mechanism, would
  earn the harness doc's −2 penalty for advice with no concrete change.

**Why the chosen frame wins:** it survives one image (same question, two answers), it
gives one habit anyone can adopt today, and it's honest about the ceiling (long output
is sometimes correct). It reads as a filing/attention idea, not a coding idea.

---

## 9. Final self-review against the broad-reach test

- **Broad legibility (the #1 benchmark):** A non-engineer recognises "I asked one
  thing and got an essay" in seconds, and "tell it the shape you want" is an
  immediately usable habit — no API knowledge required. **Passes**, at the level of
  the Opus-low-vs-Sonnet-high post.
- **One clear decision:** *Name the output shape before you ask.* Single, concrete,
  adoptable today. **Pass.**
- **Human problem before mechanism:** §1 is attention/burying; the API and `verbosity`
  detail is demoted to §3/§5 and framed as "a dial," never as the subject. **Pass —
  not an API tutorial.**
- **Two benefits kept distinct:** attention/cognitive-load (universal, the lead) vs API
  token cost + context (conditional, secondary). Never merged into one overclaim.
  **Pass.**
- **No invented universal number:** cost stated as structure ("output ≫ input per
  token"); the token counts are labelled two illustrative examples. **Pass.**
- **Not "shorter is always better":** teaching / audits / hand-offs / complex decisions
  explicitly reserved for the long version, using OpenAI's own words. **Pass.**
- **Evidence discipline:** every quote fetch-verified 2026-07-21; each figure labelled
  Documented / Measured / Expected; 403 consumer pages excluded. **Pass.**
- **One-image survivability:** problem (buried point) → one mechanism (length is a set
  shape) → takeaway (ask for the shape); before/after fits one canvas without a
  carousel. **Pass.**
- **No hype, no API trivia, no carousel:** honest, opinionated, plain English; the
  parameter is named once and de-emphasised. **Pass.**
- **Stalest facts to re-verify at publish:** the output/input price multiple and
  example model rows (OpenAI pricing changes), whether `verbosity` is still the current
  parameter name and value set, and the two doc URLs (may move). Re-fetch before render.
```
