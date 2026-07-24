# Inside of the Day — Research v3 (harness-first)

> Idea-finding system for one-image LinkedIn infographics, re-centred on the
> **harness around a model**: how context is arranged, how tasks flow, how cost is
> controlled, how output is verified and remembered, how work is routed and handed
> off. Not a model-news feed, not an API-trivia feed.
>
> Research document only — not final social copy, not an infographic.
> Compiled 2026-07-21. All primary sources were opened on that date; every figure is
> labelled **Documented** (stated by the vendor), **Measured** (a published /
> vendor-internal measurement), or **Expected** (mechanism implies it, no number
> stated). Supersedes the *ranked backlog* of research v2 for topic selection; v2's
> API-specific catalogue is retained there for reference.

---

# 1. Direction: harness-first, broad audience

The series explains the **harness**, not the model. A post earns its place when a
normal knowledge worker can look at one image and (a) recognise their own problem
in seconds and (b) walk away with one practical choice.

**The benchmark to beat is Post #1** (Opus 4.8 low vs Sonnet 5 high). It worked
because the insight was legible to almost anyone using AI — not only API
specialists — and reduced to a single, concrete decision.

**Audience we optimise for:** people using ChatGPT/Claude for work; founders and
managers deciding how to use AI; vibe coders and builders; engineers and technical
founders; people building agent systems. **We do not optimise for API specialists.**

**The one-sentence test for any candidate:**
> Can a broad AI user recognise the problem and understand the decision from the
> headline and one diagram — with an obvious benefit in *at least one* of: saving
> money, moving faster, avoiding repeated work, improving quality, making output
> reproducible, reducing coordination overhead, reducing cognitive load, or reducing
> risk?

If the honest answer needs an API detail to make sense, the idea is reframed to the
human problem or rejected.

**Format contract (unchanged):** one large 1080×1350 infographic (rendered 3× →
3240×4050 PNG), one thought / one mechanism / one takeaway, English copy, eyebrow
`Inside of the Day #<number> — <concise topic>`, `@vitalylobachev` footer, default
style *Operator's Field Notes*, no tiny text, no dense API screenshots, no hype.

---

# 2. Do-not-repeat boundary (six topics now spoken for)

| # | Topic | The decision it already made | New candidates must not… |
|---:|---|---|---|
| 1 | Model × effort × harness (Opus 4.8 low vs Sonnet 5 high) | Pick the operating point; more effort ≠ better | …re-argue "compare model×effort" or reuse a benchmark-cost chart |
| 2 | Founder-gated questions | Park the blocked task; keep ready work moving; hand off decisions async | …repeat "park blocked work / async human decisions" |
| 3 | The real stopping condition | Done = ready queue empty, not PRs merged | …repeat "queue vs PR count / when is a session done" |
| 4 | Review evidence, not provenance | Judge the diff/tests/CI/effect, not an AI label | …repeat "provenance vs evidence / drop the AI footer" |
| 5 | Graphiti vs Cognee vs Graphify | Three *external* memory graphs for three question types | …repeat "agent memory layering across external stores" |
| 6 | **Prompt caching** (this round) | Put the stable prefix first so repeats are cached | …repeat "prompt order / exact-prefix caching / cached-input pricing" |

Adjacency is allowed only where the *decision* is genuinely different; where a new
candidate brushes an existing post, the difference is stated explicitly below.

**Intentionally excluded this round — Batch API.** It is a real 50% cost lever, but
the decision ("route non-interactive jobs to a batch endpoint") is API-operational
and does not survive the broad-audience test without turning into an API tutorial.
The *human* version of that idea — "hand off work that can wait" — is carried by
**T5** below, framed without the endpoint.

---

# 3. Scoring rubric (carried from v2, broad-audience emphasis)

Each candidate scored 0–5 on six axes (max 30); penalties subtracted.

| Axis | 0 | 3 | 5 |
|---|---|---|---|
| **Implementation clarity** | No concrete change | A change a reader could make this week | One setting/habit a reader can adopt today |
| **Impact potential** | Marginal / unclear | Real effect on one benefit category | Large, obvious effect a broad user feels |
| **Evidence strength** | Marketing / none | Documented behaviour, no figure | Documented **with a figure** or a published measurement |
| **Visual compression** | Needs a tutorial/carousel | Fits with effort | Problem + one mechanism + one takeaway, trivially |
| **Durability** | Expires in weeks | Useful for months | Structural lesson that survives model churn |
| **Broad legibility & novelty** | API-only or overlaps an existing post | Understandable but niche, or adjacent | A non-engineer recognises it instantly *and* the series has never made this call |

**Penalties:** −3 hype with no decision; −2 vague advice ("write better prompts")
with no mechanism; −2 marketing dressed as insight; −2 evidence is only an unopened
snippet; −3 cannot survive one image; −2 minor variation of an existing/queued post.
Below ~20/30 after penalties → rejected for now.

**Source-reachability note (applies to every source list below):** every
`help.openai.com` and `openai.com/index/...` article returns HTTP 403 to automated
fetching (Intercom/edge bot protection). Those URLs are still the canonical
consumer references and are listed as such, but the *fetch-verified* quotes come
from reachable first-party equivalents (`code.claude.com`, `support.claude.com`,
`platform.claude.com`, `claude.com/blog`, `developers.openai.com`,
`academy.openai.com`). This is flagged per topic.

---

# 4. Ranked five (broad-reach harness topics, besides prompt caching)

---

## T1 — "Stop re-explaining your project every chat" (a reusable project brief) · Score 28/30

- **Plain-language problem:** Every new chat starts from zero. You re-paste who you
  are, what the project is, the rules, the tone, the same three reference files —
  again. It is slow, it drifts, and two chats end up with two different set-ups.
- **One choice:** Write the stable context **once** and attach it to the workspace,
  not the message — ChatGPT *Custom Instructions* / a *Project*, a Claude *Project*,
  or a `CLAUDE.md` for Claude Code. Every conversation in that space starts with it.
- **Mechanism:** The saved instructions/files are injected into the model's context
  automatically at the start of each chat, so the model begins every conversation
  already knowing your standing rules — you stop paying for them in effort and
  attention on every turn.
- **Impact category:** Avoiding repeated work + reducing cognitive load (primary);
  reproducibility across chats/teammates (secondary).
- **Evidence type:** **Documented** (behaviour stated; no figure).
- **Primary sources:**
  - Anthropic, "How Claude remembers your project" (Claude Code memory) —
    https://code.claude.com/docs/en/memory — *fetch-verified 200.*
    Quote: *"CLAUDE.md files are loaded into the context window at the start of every
    session"*; *"Treat CLAUDE.md as the place you write down what you'd otherwise
    re-explain."*
  - Anthropic, "How can I create and manage projects?" (Claude Help Center) —
    https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
    — *fetch-verified 200.* Quote: *"Claude will use these instructions for all the
    chats within the project."*
  - OpenAI, "Projects" (OpenAI Academy, work-users) —
    https://academy.openai.com/public/clubs/work-users-ynjqu/resources/projects —
    *fetch-verified 200.* Quote: *"Centralize all instructions, files, and context so
    the model has the same background your whole team does."*
  - OpenAI, "ChatGPT — Custom Instructions" —
    https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions —
    *canonical consumer reference; 403 to fetch, not quote-verified.*
- **Why a non-engineer gets it instantly:** Everyone who uses ChatGPT for work has
  re-typed the same context into a fresh chat and felt the waste. "Save it once" is
  a filing-cabinet idea, not a coding idea.
- **One-image visual concept:** Left — three separate chats, each re-typing the same
  block of context (repetition drawn literally). Right — one "Project brief" card
  feeding all three chats from a single source. Takeaway strip: *write the standing
  context once; every chat starts with it.*
- **Caveat:** Saved instructions are **context, not enforcement**. Anthropic states
  it plainly: *"Claude treats them as context, not enforced configuration… there's
  no guarantee of strict compliance, especially for vague or conflicting
  instructions."* Keep the brief short and unambiguous; it guides, it does not
  guarantee.
- **Rubric:** impl 5 · impact 5 · evidence 4 · visual 5 · durability 5 · legibility/novelty 4 = **28**. Penalties 0.
- **Not a duplicate:** No existing post is about *standing project context*. It is
  the human-workspace cousin of prompt caching (#6) — caching is about *cost order*,
  this is about *not re-authoring context* — state the distinction if both are ever
  referenced.

---

## T2 — "A long chat is not your memory" (context hygiene: reset + keep a record) · Score 25/30

- **Plain-language problem:** The longer a single thread runs, the more it drifts,
  forgets its own earlier decisions, and slows down. People treat one endless chat
  as the project's memory — and it quietly stops being reliable.
- **One choice:** Stop hoarding one mega-thread. Keep a **compact running record**
  of decisions (or turn on the product's memory feature) and start a **fresh chat**
  from that record when a thread gets long, instead of scrolling forever.
- **Mechanism:** A context window is finite and fills with stale turns; quality
  degrades as it fills. A short external record (or a memory feature that persists
  facts *outside* the thread) lets a fresh, clean context start already knowing what
  was decided — the durable knowledge lives in the record, not in the scrollback.
- **Impact category:** Quality + avoiding repeated work (primary); reducing
  cognitive load (secondary).
- **Evidence type:** **Documented** (mechanism) + **Measured** (vendor-internal
  benchmark figures, labelled as such).
- **Primary sources:**
  - Anthropic, "Managing context on the Claude Developer Platform" (blog) —
    https://claude.com/blog/context-management — *fetch-verified 200.*
    Quotes: *"Context editing automatically clears stale tool calls and results from
    within the context window when approaching token limits"*; the memory tool stores
    information *"outside the context window through a file-based system"* that
    *"persists across conversations."* (100-turn eval figures ~84% token reduction /
    ~39% improvement are **Anthropic-internal**, not independently audited.)
  - Anthropic, "Claude Code memory" — https://code.claude.com/docs/en/memory —
    *fetch-verified 200.* Quote: *"Each Claude Code session begins with a fresh
    context window"* (so durable knowledge must live in a record, not the thread).
  - OpenAI, "Customizing ChatGPT" (OpenAI Academy) —
    https://academy.openai.com/public/clubs/work-users-ynjqu/resources/customizing-chatgpt
    — *fetch-verified 200.* Quote: *"Enable memory so ChatGPT can remember your style
    preferences and reuse them across conversations."*
  - OpenAI, "Memory FAQ" — https://help.openai.com/en/articles/8590148-memory-faq —
    *canonical consumer reference; 403 to fetch, not quote-verified.*
- **Why a non-engineer gets it instantly:** Anyone with a 200-message ChatGPT thread
  has felt it "lose the plot." The lesson — the chat is not the filing cabinet — is
  intuitive.
- **One-image visual concept:** Left — one bloated thread, a "context" bar filling to
  the brim and quality dropping. Right — a short "decisions" card + a fresh chat
  starting from it, bar back near empty. Takeaway: *the thread is working memory; the
  record is memory.*
- **Caveat:** Memory features persist facts imperfectly and across contexts you may
  not intend; a hand-kept decision log is only as good as what you write down. The
  vendor efficiency numbers are internal-benchmark, not guarantees.
- **Rubric:** impl 4 · impact 4 · evidence 4 · visual 5 · durability 5 · legibility/novelty 3 = **25**. Penalties 0.
- **Not a duplicate (adjacency flagged):** Post #5 is about **external** memory
  *graphs* for agent systems. T2 is about **in-context** hygiene for ordinary
  chat/agent users — window management + a plain record — and must be framed that way
  to stay clearly distinct.

---

## T3 — "Trust the draft, verify the decision" (add a check before you act) · Score 25/30

- **Plain-language problem:** AI answers are fluent and confident even when wrong.
  People act on the first draft — a number, a legal-sounding line, a citation — and
  only later find it was invented.
- **One choice:** For anything that matters, add a **verification step** to the flow
  instead of trusting the first answer: ask the model to ground each claim in a
  source (and retract what it can't support), give it explicit permission to say "I
  don't know," and check high-stakes facts yourself.
- **Mechanism:** Grounding forces the answer to point at the exact supporting
  passage, which makes it checkable; a permitted "I don't know" removes the pressure
  to fabricate. The verification step turns an unauditable assertion into something
  you can inspect before it becomes a decision.
- **Impact category:** Quality + reducing risk (primary); auditability (secondary).
- **Evidence type:** **Documented** (behaviour + explicit guidance).
- **Primary sources:**
  - Anthropic, "Citations" (Claude Platform Docs) —
    https://platform.claude.com/docs/en/build-with-claude/citations — *fetch-verified
    200.* Quote: *"Citations return the exact passages that support each claim, so you
    can verify answers and surface sources to your users."*
  - Anthropic, "Reduce hallucinations" (Claude Platform Docs) —
    https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
    — *fetch-verified 200.* Quotes: *"Even the most advanced language models… can
    sometimes generate text that is factually incorrect"*; *"have Claude verify each
    claim by finding a supporting quote after it generates a response. If it can't
    find a quote, it must retract the claim"*; *"Allow Claude to say 'I don't know'."*
- **Why a non-engineer gets it instantly:** Everyone has been burned by a
  confident-but-wrong AI answer. "Add a check for the things that matter" is common
  sense once named.
- **One-image visual concept:** Two paths from one fluent answer. Path A — trust it →
  a hidden error ships. Path B — one "verify" gate (grounded quote / "I don't know")
  → the claim is confirmed or retracted before it's used. Takeaway: *a check is
  cheaper than a wrong decision.*
- **Caveat:** Anthropic is explicit that verification **reduces but does not
  eliminate** error: *"while these techniques significantly reduce hallucinations,
  they don't eliminate them entirely. Always validate critical information,
  especially for high-stakes decisions."*
- **Rubric:** impl 4 · impact 5 · evidence 4 · visual 4 · durability 5 · legibility/novelty 3 = **25**. Penalties 0.
- **Not a duplicate (adjacency flagged):** Post #4 is about how a **human reviews AI
  work** (read the diff/tests, ignore the AI label). T3 is about **building a
  verification step into the flow** so an important output isn't trusted on first
  pass — a mechanism, not a review posture. Keep the framing on "add a check step,"
  not "review the diff," to stay distinct.

---

## T4 — "Ask for the short version" (output length costs attention and money) · Score 24/30

- **Plain-language problem:** The model answers a one-line question with a wall of
  text. You skim, you lose the point, and — in an app or a long pipeline — every one
  of those extra words is billed and eats the context you have left.
- **One choice:** Ask for the length you actually want. In the API, set the output
  **verbosity** low for terse answers and reserve verbose output for teaching or
  hand-offs; in a chat, just say "one paragraph" / "just the answer."
- **Mechanism:** Output is generated and billed token by token; longer answers cost
  more tokens and consume more of the finite context window. Output length is a
  controllable dial, not a fixed property of the model.
- **Impact category:** Reducing cognitive load (primary); saving money + preserving
  context (secondary).
- **Evidence type:** **Documented** (verbosity control) + **Measured** (illustrative
  token counts from one worked example — labelled as illustrative).
- **Primary sources:**
  - OpenAI, "GPT-5 New Params and Tools" (OpenAI Cookbook) —
    https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools —
    *fetch-verified 200.* Quotes: the `verbosity` parameter *"lets you hint the model
    to be more or less expansive in its replies"* (low = *"terse UX, minimal prose,"*
    high = *"verbose, great for audits, teaching, or hand-offs"*); *"the output tokens
    scale roughly linearly with verbosity"* (worked example: low 560 → medium 849 →
    high 1,288 output tokens — **illustrative, one prompt**).
  - OpenAI, "Pricing" — https://developers.openai.com/api/docs/pricing —
    *fetch-verified 200.* Lists separate per-million **input** and **output** rates
    for every model (output tokens are billed independently — longer = more).
- **Why a non-engineer gets it instantly:** Everyone has been annoyed by an
  over-long AI answer. "You can ask for less, and less is cheaper" is immediately
  useful.
- **One-image visual concept:** Same question, two answers side by side — a wall of
  text vs three tight lines — with a small token/cost bar under each (tall vs short).
  Takeaway: *set the length; long answers cost you twice — attention and tokens.*
- **Caveat:** The 560/849/1,288 figures are one illustrative example, not a
  guaranteed ratio. `verbosity` is a **GPT-5-family API parameter**; the consumer
  ChatGPT UI has no literal verbosity slider (you ask in words). Don't over-trim —
  audits, teaching, and hand-offs legitimately want the long version.
- **Rubric:** impl 4 · impact 4 · evidence 4 · visual 4 · durability 4 · legibility/novelty 4 = **24**. Penalties 0.
- **Not a duplicate:** No existing post addresses output shape / attention-and-cost
  of length. Distinct from prompt caching (#6), which is about *input* order.

---

## T5 — "Queue it, don't babysit it" (hand off work that can wait) · Score 24/30

- **Plain-language problem:** For a big job you sit and watch a spinner, keep the tab
  open, and hope the connection doesn't drop. Your attention is held hostage by work
  that doesn't need you present.
- **One choice:** Hand long or scheduled work to run **in the background** and get
  the result later, instead of blocking on it — the consumer version is ChatGPT
  *Tasks* (run now/later, delivered by notification or email); the builder version is
  a *background* job you kick off and poll.
- **Mechanism:** The work runs server-side and reports back when done, so you don't
  hold a live connection or your own attention open for the duration. Waiting becomes
  asynchronous: start it, leave, collect the result.
- **Impact category:** Moving faster / throughput (primary); reducing coordination
  overhead and cognitive load (secondary).
- **Evidence type:** **Documented**.
- **Primary sources:**
  - OpenAI, "Background mode" (OpenAI API docs) —
    https://developers.openai.com/api/docs/guides/background — *fetch-verified 200.*
    Quotes: *"execute long-running tasks… reliably, without having to worry about
    timeouts or other connectivity issues"*; *"kicks off these tasks asynchronously,
    and developers can poll response objects to check status over time."*
  - OpenAI, "Tasks" (OpenAI Academy — consumer analogue) —
    https://academy.openai.com/public/clubs/work-users-ynjqu/resources/tasks —
    *fetch-verified 200.* Quote: *"Tasks let ChatGPT proactively perform an
    instruction at a future time (once or a schedule) and deliver the result back to
    you in a push notification or an email."*
  - OpenAI, "Scheduled Tasks in ChatGPT" —
    https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt —
    *canonical consumer reference; 403 to fetch, not quote-verified.*
- **Why a non-engineer gets it instantly:** Everyone has watched a slow generation
  finish while doing nothing else. "Let it run and ping me" is how we already treat
  long downloads and renders.
- **One-image visual concept:** Left — a person staring at a spinner, blocked. Right
  — the job dropped into a "background / scheduled" tray, the person walks off, a
  notification lands later with the result. Takeaway: *presence is not required for
  work that can wait.*
- **Caveat:** These are **two distinct mechanisms** — consumer *Tasks* (schedule +
  delivery) vs a developer *background* API — don't conflate them in one claim.
  Background results are also short-lived (retained only long enough to poll), so
  it's async, not permanent storage. This is the **human** framing of the
  deliberately-excluded Batch API cost lever — keep it about attention/throughput,
  not endpoint pricing.
- **Rubric:** impl 3 · impact 4 · evidence 4 · visual 5 · durability 4 · legibility/novelty 4 = **24**. Penalties 0.
- **Not a duplicate:** No existing post addresses synchronous-vs-async work. Distinct
  from Post #2 (which parks *human-blocked* tasks); T5 is about *machine* work you
  don't need to watch.

---

### Ranking summary

| Rank | Topic | Score | Primary benefit | Adjacency to watch |
|---:|---|---:|---|---|
| 1 | T1 — reusable project brief | 28 | avoid repeated work, cognitive load | none (workspace cousin of #6) |
| 2 | T2 — a long chat is not memory | 25 | quality, avoid repeated work | #5 external memory → frame as in-context |
| 3 | T3 — verify the important result | 25 | quality, risk | #4 review → frame as a *mechanism*, not review |
| 4 | T4 — ask for the short version | 24 | cognitive load, cost | none (input vs output vs #6) |
| 5 | T5 — queue it, don't babysit it | 24 | speed, coordination | #2 parks *human* work; T5 is *machine* work |

---

# 5. Also-considered, held back this round

- **"One giant prompt vs staged steps" (task decomposition).** Broad and relatable,
  but the payoff is quality/steerability that is harder to prove with a primary
  source and harder to reduce to one honest number; hold until it can be framed as a
  single sharp choice with evidence.
- **"Give it your files, don't make it guess" (grounding / retrieval).** Strong human
  problem, but the clean version overlaps T3 (verification) and drifts toward a RAG
  tutorial; revisit as a distinct "attach the source" post only if it stays one-image.
- **Structured outputs, MCP, service tiers, OpenTelemetry (from v2).** Real and
  documented, but implementation-heavy or API-specialist — they fail the
  broad-legibility axis unless reframed into an unmistakable human problem. Kept in
  v2's catalogue, not promoted here.
- **Batch API.** Excluded by direction (see §2); its human form is T5.

---

# 6. Harness thesis (the principles that unify the series)

Seven principles. Every post is one concrete instance of one of these; the series is
their accumulation.

1. **The harness beats the model.** Most day-to-day wins come from *how* you arrange
   context, tasks, cost, and verification around a model — not from a bigger model.
   (Posts #1, #6.)
2. **Arrange context on purpose.** Where content sits, and how much of it there is,
   decides cost, speed, and quality. Stable-first ordering, a short standing brief,
   and a clean window are arrangement choices. (Posts #6, T1, T2, T4.)
3. **The thread is not the memory.** Working context is disposable and finite;
   durable knowledge belongs in a record, a brief, or a memory layer that outlives
   any one conversation. (Posts #5, T1, T2.)
4. **Match the setting to the job.** Model, effort, output length, and urgency are
   dials, not defaults — pick per task instead of running everything at one setting.
   (Posts #1, T4, T5.)
5. **Verify before you trust; judge by evidence.** Fluency is not correctness. Add a
   check for what matters, and judge work by its diff/tests/sources, not by its
   confidence or its label. (Posts #4, T3.)
6. **Don't stop the system for one blocker; don't hold it open for one wait.** Park
   human-blocked work and keep ready work moving; hand off machine work that can run
   without you. (Posts #2, #3, T5.)
7. **One decision, one image, sourced.** Each post is a single implementable choice a
   broad user can act on today, backed by a primary source and honest about its
   caveat — never hype, never an unowned number.

---

# 7. Source index (v3 additions, accessed 2026-07-21)

Fetch-verified (200) unless marked. Consumer `help.openai.com` / `openai.com/index`
articles are canonical but return 403 to automated fetch — listed for the reader,
quotes taken from reachable equivalents.

**Anthropic / Claude**
- Claude Code memory — https://code.claude.com/docs/en/memory
- Claude Help: manage projects — https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Managing context (blog) — https://claude.com/blog/context-management
- Citations — https://platform.claude.com/docs/en/build-with-claude/citations
- Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Prompt caching (Post #6) — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Pricing (Post #6) — https://platform.claude.com/docs/en/about-claude/pricing

**OpenAI**
- Projects (Academy) — https://academy.openai.com/public/clubs/work-users-ynjqu/resources/projects
- Customizing ChatGPT (Academy) — https://academy.openai.com/public/clubs/work-users-ynjqu/resources/customizing-chatgpt
- Tasks (Academy) — https://academy.openai.com/public/clubs/work-users-ynjqu/resources/tasks
- GPT-5 New Params and Tools (Cookbook) — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
- Background mode — https://developers.openai.com/api/docs/guides/background
- Prompt caching (Post #6) — https://developers.openai.com/api/docs/guides/prompt-caching
- Pricing — https://developers.openai.com/api/docs/pricing
- *Canonical consumer refs, 403 to fetch:* Custom Instructions —
  https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions ·
  Memory FAQ — https://help.openai.com/en/articles/8590148-memory-faq ·
  Scheduled Tasks — https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt

---

## Self-review (applied)

- **Harness-first, broad-audience:** all five pass the "recognise it in seconds"
  test with a human problem; none require an API detail to make sense (T4/T5 name the
  API feature but the decision is stated in plain terms).
- **No repeats:** none of the five re-make the six spoken-for decisions; the two real
  adjacencies (T2↔#5, T3↔#4) are flagged with an explicit distinction. Batch API is
  excluded by direction and re-expressed as the human idea T5.
- **Evidence discipline:** every quote is verbatim from a page opened 2026-07-21;
  vendor-internal benchmark numbers (T2) and illustrative token counts (T4) are
  labelled as such; no figure is presented as a universal guarantee. The 403-blocked
  consumer pages are marked and never quoted as fetch-verified.
- **One-image survivability:** each candidate reduces to problem → one mechanism →
  takeaway; T5 carries a two-mechanism caveat so it does not overclaim.
- **Stalest facts to re-verify at publish:** any pricing/output-token figure (T4),
  product-feature availability (Tasks, verbosity parameter, memory), and the exact
  consumer-help URLs (may move).
