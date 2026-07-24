# Inside of the Day #8 - A reusable project brief

## Title

**I stopped re-explaining my project in every chat.** (A reusable project brief)

## First-person thesis

I used to open every new chat by re-pasting the same block: who I am, what the
project is, the goals, the constraints, the two or three style rules. I stopped.
I moved that stable context into one reusable brief - a ChatGPT Project /
Custom Instructions, a Claude Project, or a `CLAUDE.md` for Claude Code - and now
every new chat starts from the same baseline without me re-typing anything.

## Mechanism

- The standing context belongs to the **workspace**, not the message. You write it
  once and attach it to the project / instructions / memory file.
- That saved brief is loaded into the model's context automatically at the start of
  every conversation in that space, so each chat begins already knowing your
  standing rules.
- You stop paying for that context in attention and typing on every turn, and two
  parallel chats no longer drift into two different set-ups.

## Impact

- **Cognitive load + repeated work (primary):** you author the standing context once
  instead of re-typing (and re-deciding) it per chat.
- **Reproducibility (secondary):** every chat - and every teammate on a shared
  project - starts from the same baseline, so results are comparable.

## Evidence

All wording verified against live vendor docs on 2026-07-21.

- **Anthropic - Claude Code memory (Documented).** Page is now titled *"How Claude
  remembers your project."* Verbatim: *"CLAUDE.md files are loaded into the context
  window at the start of every session, consuming tokens alongside your
  conversation."* The page also documents a second, newer mechanism, **Auto memory**
  (*"Both are loaded at the start of every conversation"*); this post references only
  the author-written `CLAUDE.md`, which remains accurate.
- **Anthropic - Manage projects (Documented).** Verbatim: *"Claude will use these
  instructions for all the chats within the project."*
- **OpenAI - Projects in ChatGPT (Documented behaviour; wording search-confirmed
  only).** The help page (article 10169521) returns HTTP 403 to automated fetch, so
  its exact wording could **not** be read directly. Web search of OpenAI-owned sources
  confirms Projects hold *"instructions and uploaded files [that] carry across every
  chat in the project"* and that project instructions *"override your global custom
  instructions"* - **re-read in a browser before publishing** to lift a verbatim
  sentence.
- **Caveat basis (Documented).** Anthropic: *"Claude treats them as context, not
  enforced configuration"* and *"there's no guarantee of strict compliance,
  especially for vague or conflicting instructions."*

## Caveats

- A brief is **context, not a contract** - the model treats it as guidance, with no
  guarantee of strict compliance. Keep it short and unambiguous; a 500-line file gets
  half-followed.
- To *enforce* a rule (not just suggest it) you need a hard mechanism outside the
  brief (e.g. a hook / client-side rule), not more prose in the file.
- Product and feature names move (Custom Instructions, Projects, memory types) -
  re-verify at publish.

## Sources

- Anthropic, "How Claude remembers your project" (Claude Code memory) - https://code.claude.com/docs/en/memory
- Anthropic, "How can I create and manage projects?" - https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- OpenAI, "Projects in ChatGPT" - https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt *(403 to automated fetch; wording confirmed via search - re-read live at publish)*

## Visual contract

- Eyebrow: `Inside of the Day #8 — A reusable project brief`.
- Headline: **I stopped re-explaining my project in every chat.**
- Left panel ("Every chat from zero"): three separate chat cards, each re-typing the
  *same* context block above a one-line question - repetition drawn literally.
- Right panel ("Written once"): one **Project brief** card feeding three chats that
  carry only today's question; a "loaded into every chat" connector.
- Mechanism strip: the brief loads into context at the start of every conversation in
  that space - `CLAUDE.md` · Claude Project · ChatGPT Project.
- Takeaway: write the standing context once; start every chat from the same baseline.
- Caveat line: it's context, not a contract - guidance, not enforced rules.
- Footer: Anthropic memory + Projects, OpenAI Projects, verified date, `@vitalylobachev`.

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 downscaled feed-legibility probe.
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3).
