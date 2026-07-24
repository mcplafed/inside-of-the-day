# Inside of the Day — First-person field-note ideas (v1)

> Ten broad-reach post ideas for the series, re-centred on the corrected editorial
> voice: a **first-person operator field note**, not an AI-news roundup and not
> generic advice. Compiled 2026-07-21. Builds on the harness-first direction in
> `research/inside-of-the-day-research-v3-harness.md` and the v2 catalogue, and
> re-casts the strongest broad candidates in the author's own voice.
>
> Every product-specific claim below points at a primary source opened 2026-07-21.
> Sources marked *fetch-verified (summarizer)* were retrieved live today through the
> fetch tool's summarizer rather than a raw page read — the URL and substance are
> confirmed, but exact wording must be re-confirmed against the live page at publish.
> Each figure is labelled **Documented** (vendor states it), **Measured** (a published
> example measurement), or **Expected** (mechanism implies it, no vendor number).

---

## 1. Editorial rule: source-backed first-person field notes

Inside of the Day is a field note from someone who runs this every day — not a news
desk and not a tips list. The shape of every post is:

> **I kept seeing X in my workflow → I changed Y → now Z is easier / cheaper /
> faster / more repeatable.**

Concretely, each idea in this document obeys these rules:

- **Lead with the operator, not the vendor.** Open with what the author does, keeps,
  changes, or stops doing. Never open with "OpenAI released…" or "Anthropic added…".
  The source document *proves the mechanism*; it is not the protagonist.
- **First person, bounded.** Use *this is how I handle it*, *I use this when…*, and
  state the boundary out loud. No universal claims ("you should always…").
- **One choice, one benefit.** Exactly one change, tied to exactly one of: money,
  speed, quality, repeatability, cognitive load, or risk.
- **Broad-reach test (the Post #1 benchmark).** Almost anyone using AI for work —
  ChatGPT/Claude users, founders, managers, vibe coders, builders, engineers,
  technical founders — must recognise the problem and understand the choice from one
  headline and one diagram, with no API knowledge required.
- **Source-backed, honestly labelled.** Product-specific claims cite an opened primary
  page; figures are labelled Documented / Measured / Expected; the caveat is visible.
- **Survives one image.** Problem → one mechanism → one takeaway, no carousel.

Scoring uses seven axes, each 0–5 (max **35**): implementation clarity, broad reach,
impact, evidence, visual compression, durability, novelty. Penalties: −2 for
adjacency to an existing post that isn't a genuinely different decision; −2 for a
claim that needs an API detail to make sense; −3 if it can't survive one image.

---

## 2. What the existing series already covers

Twelve decisions are now spoken for — six published/queued posts and the strongest
already-briefed candidates. New ideas must not re-make any of these decisions.

| Ref | Decision already made | New ideas must not… |
|---|---|---|
| **#1** Model × effort × harness (Opus 4.8 low vs Sonnet 5 high) | Pick the operating point on a benchmark; more effort ≠ better | …re-argue "compare model×effort" or reuse a benchmark-cost chart |
| **#2** Founder-gated questions | Park the blocked task; keep ready work moving; hand off decisions async | …repeat "park human-blocked work / async decision interface" |
| **#3** The real stopping condition | Done = ready queue empty, not PRs merged | …repeat "queue vs PR count / when is a session done" |
| **#4** Review evidence, not provenance | Judge the diff/tests/CI/effect, not an AI label | …repeat "provenance vs evidence / drop the AI footer" |
| **#5** Graphiti vs Cognee vs Graphify | Three *external* memory graphs for three question types | …repeat "external memory graphs / three-store routing" |
| **#6** Prompt caching | Put the stable prefix first so repeats are cached | …repeat "prompt order / exact-prefix caching / cached-input price" |
| **#7 (briefed)** Ask for the short version | Name the output *length/shape* before you ask | …re-make "output length is a dial" as its own post (idea #3 here IS this candidate, re-voiced) |

Also formally excluded by direction (from v3): **Batch API, MCP internals,
telemetry/OpenTelemetry schemas, structured-output implementation details** — too
deep / API-specialist to survive the broad-reach test.

**Idea #3 below is candidate T4 ("ask for the short version"), already expanded into a
production brief as provisional #7.** It is kept in this ranked list for completeness
and re-voiced in first person, but it is *already in the pipeline* — the genuinely new
work is ideas #5–#10 and the recommended next topic.

---

## 3. Ranked 10 ideas

Ranked by score after penalties. Each is a first-person field note with one change,
one mechanism, one benefit, a verified source (where product-specific), a one-image
concept, a novelty/duplication check, a score, and a boundary.

---

### Idea 1 — "I stopped re-explaining my project in every chat" (a reusable project brief) · **33/35**

1. **Hook:** *I used to start every chat by re-pasting who I am, what the project is,
   and the same three rules. I stopped. Now I write that once and every chat already
   knows it.*
2. **Problem:** Every new conversation starts from zero, so you re-type the same
   context and two chats drift into two different set-ups.
3. **The one change:** Write the standing context **once** and attach it to the
   workspace, not the message — a ChatGPT Project / Custom Instructions, a Claude
   Project, or a `CLAUDE.md` for Claude Code.
4. **Mechanism (plain):** The saved brief is loaded into the model's context
   automatically at the start of every conversation in that space, so it begins
   already knowing your standing rules — you stop paying for them in effort and
   attention on every turn.
5. **Benefit:** Avoids repeated work + cuts cognitive load (primary); reproducibility
   across chats and teammates (secondary). **Documented** (behaviour stated; no figure).
6. **Sources (verified 2026-07-21):** Anthropic, "Claude Code memory" —
   https://code.claude.com/docs/en/memory ("CLAUDE.md files are loaded into the
   context window at the start of every session"). Anthropic, "Manage projects" —
   https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
   ("Claude will use these instructions for all the chats within the project").
   OpenAI, "Projects" (Academy) —
   https://academy.openai.com/public/clubs/work-users-ynjqu/resources/projects.
7. **Visual:** Left — three separate chats each re-typing the same block of context
   (repetition drawn literally). Right — one "Project brief" card feeding all three
   from a single source. Takeaway strip: *write the standing context once; every chat
   starts with it.*
8. **Not generic / not a duplicate:** "Save it once" is a filing-cabinet idea, not a
   prompt-craft tip — it names a concrete place to put context. No existing post is
   about *standing project context*; it is the human-workspace cousin of #6 (caching
   is about *cost order* on repeats; this is about *not re-authoring context* at all).
9. **Score:** impl 5 · reach 5 · impact 5 · evidence 4 · visual 5 · durability 5 ·
   novelty 4 = **33**. Penalties 0.
10. **Boundary:** A brief is **context, not enforcement** — Anthropic states the model
    "treats them as context… no guarantee of strict compliance." Keep it short and
    unambiguous; don't bury it in a 500-line file it will half-follow.

---

### Idea 2 — "I stopped describing the style I wanted and started showing it" (examples beat adjectives) · **32/35**

1. **Hook:** *I used to write a paragraph describing the tone and format I wanted, then
   fight the output. Now I paste three examples of the thing I want and say "like
   these." The arguing stopped.*
2. **Problem:** You describe the desired style in the abstract ("professional but
   friendly, structured, concise") and the model keeps missing what you meant.
3. **The one change:** Put **3–5 concrete examples** of the input→output you want right
   next to the task, instead of describing the style in words.
4. **Mechanism (plain):** A model matches patterns far better than it interprets
   adjectives. Examples pin down format, tone, and edge cases directly; a description
   leaves them to guess. Show the target, don't narrate it.
5. **Benefit:** Quality + repeatability (primary); cognitive load — you stop rewording
   instructions (secondary). **Documented** (Anthropic: examples are "one of the most
   reliable ways to steer" output; "include 3–5 examples").
6. **Sources (verified 2026-07-21):** Anthropic, "Prompting best practices" (Use
   examples / multishot) —
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
   ("Examples are one of the most reliable ways to steer Claude's output format, tone,
   and structure"; "Include 3–5 examples for best results") — *fetch-verified
   (summarizer).* OpenAI, "Prompt engineering" —
   https://developers.openai.com/api/docs/guides/prompt-engineering ("Few-shot learning
   lets you steer a large language model toward a new task by including a handful of
   input/output examples in the prompt") — *fetch-verified (summarizer).*
7. **Visual:** Left — a prompt made of adjectives ("professional, structured,
   concise") pointing at a messy off-target answer. Right — the same task with three
   tidy example cards ("like these →") pointing at a clean matching answer. Takeaway:
   *show three examples; stop describing the style.*
8. **Not generic / not a duplicate:** Not "write better prompts" — it's one concrete
   swap (adjectives → examples) with a documented mechanism and a number (3–5). No
   existing post covers *how you specify* what you want; distinct from #6 (input
   ordering) and #7 (output length).
9. **Score:** impl 5 · reach 4 · impact 4 · evidence 5 · visual 5 · durability 5 ·
   novelty 4 = **32**. Penalties 0.
10. **Boundary:** Examples must be **relevant and varied** — Anthropic warns to cover
    edge cases so the model "doesn't pick up unintended patterns." Three near-identical
    examples teach the wrong lesson; and for a genuinely one-off ask, examples aren't
    worth assembling.

---

### Idea 3 — "I gave the model the file instead of my memory of it" (attach the source) · **31/35**

1. **Hook:** *I used to paste half-remembered snippets and let the model fill the
   gaps — then chase the errors that crept in. Now I hand it the actual file and ask
   it to quote from it before answering.*
2. **Problem:** You paraphrase a document from memory or paste a fragment, and the
   model confidently answers about the parts you left out — or invents them.
3. **The one change:** Give the model the **actual source** (attach the file / paste
   the whole document near the top), and for long inputs, ask it to **quote the
   relevant parts first** before it answers.
4. **Mechanism (plain):** The model can only reason over what's in front of it. A
   fragment or a paraphrase is a lossy copy; the real file is the ground truth.
   Placing long text up top and forcing a quote-first pass anchors the answer to the
   document instead of to a guess.
5. **Benefit:** Quality + risk reduction (primary); avoids re-explaining (secondary).
   **Documented** (placement + quote-first grounding); the "up to 30%" quality figure
   is **Measured** (vendor test, one setting — cite as illustrative).
6. **Sources (verified 2026-07-21):** Anthropic, "Prompting best practices" (Long
   context) —
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
   ("Put longform data at the top… above your query"; "Queries at the end can improve
   response quality by up to 30 percent in tests"; "ask Claude to quote relevant parts
   of the documents first") — *fetch-verified (summarizer).* OpenAI, "File inputs" —
   https://platform.openai.com/docs/guides/file-inputs ("OpenAI models can accept files
   as `input_file` items") — *fetch-verified (summarizer).*
7. **Visual:** Left — a person handing the model a torn scrap of paper ("what I
   remember"), model outputs a plausible-but-wrong line. Right — the whole document
   handed over, model quotes a highlighted line then answers. Takeaway: *give it the
   file, not your memory of the file.*
8. **Not generic / not a duplicate:** One concrete habit (attach the source + quote
   first), not "use RAG." Distinct from #4/idea 4 (those verify an *answer*; this fixes
   the *input* so the answer is grounded from the start). Distinct from #6 (which is
   about *cost* of prefix order; this is about *correctness* of what you include).
9. **Score:** impl 5 · reach 5 · impact 4 · evidence 4 · visual 4 · durability 5 ·
   novelty 4 = **31**. Penalties 0.
10. **Boundary:** Attaching the file helps only when the answer *is* in the file — it
    won't fix a question the document can't answer, and dumping a 300-page PDF for a
    one-line lookup wastes context. Attach the relevant source, not everything you own.

---

### Idea 4 — "I stopped acting on the first confident answer" (add a check before you act) · **30/35**

1. **Hook:** *A fluent, confident answer used to be enough for me to act. Then a made-up
   number cost me an afternoon. Now anything that matters gets one verify step before
   I move.*
2. **Problem:** AI answers are fluent and confident even when wrong, so people act on
   an invented figure, citation, or legal-sounding line.
3. **The one change:** For anything that matters, add a **verification step** — ask the
   model to ground each claim in a supporting quote and retract what it can't support,
   give it explicit permission to say "I don't know," and check high-stakes facts
   yourself.
4. **Mechanism (plain):** Grounding forces the answer to point at the exact passage
   that backs it, which makes it checkable; permission to say "I don't know" removes
   the pressure to fabricate. The step turns an unauditable assertion into something
   you can inspect before it becomes a decision.
5. **Benefit:** Quality + risk (primary); auditability (secondary). **Documented**
   (behaviour + explicit guidance).
6. **Sources (verified 2026-07-21):** Anthropic, "Reduce hallucinations" —
   https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
   ("Allow Claude to say 'I don't know'…"; "have Claude verify each claim by finding a
   supporting quote… If it can't find a quote, it must retract the claim"; "Always
   validate critical information, especially for high-stakes decisions"). Anthropic,
   "Citations" —
   https://platform.claude.com/docs/en/build-with-claude/citations ("Citations return
   the exact passages that support each claim, so you can verify answers").
7. **Visual:** Two paths from one fluent answer. Path A — trust it → a hidden error
   ships. Path B — one "verify" gate (grounded quote / "I don't know") → the claim is
   confirmed or retracted before use. Takeaway: *a check is cheaper than a wrong
   decision.*
8. **Not generic / not a duplicate:** Post #4 is about how a *human reviews AI work*
   (read the diff/tests). This builds a *verification step into the flow* so the output
   isn't trusted on first pass — a mechanism, not a review posture. Keep the framing on
   "add a check step."
9. **Score:** impl 4 · reach 5 · impact 5 · evidence 4 · visual 4 · durability 5 ·
   novelty 3 (adjacent to #4) = **30**. Penalties 0 (adjacency handled by framing).
10. **Boundary:** Verification **reduces but does not eliminate** error — Anthropic is
    explicit. Don't gate *everything*; reserve the check for outputs where being wrong
    is expensive, or it becomes friction you'll route around.

---

### Idea 5 — "I let AI draft, but I never let it decide the irreversible things" (keep the last call human) · **30/35**

1. **Hook:** *I let the model draft almost everything now. What I don't do is let it
   press the button on anything I can't take back — the send, the deploy, the price
   change, the legal commitment.*
2. **Problem:** As AI gets good at drafting, it's tempting to let it also *act* — and
   the failure that hurts isn't a bad draft, it's an irreversible action taken on one.
3. **The one change:** Split *draft* from *decide*. Let AI produce the work; keep the
   **final commit on high-cost / hard-to-reverse actions** with a human who owns the
   outcome.
4. **Mechanism (plain):** Reversible work is cheap to get wrong — you just redo it.
   Irreversible work isn't. Matching the *decision authority* to the *cost of being
   wrong* keeps the speed of AI drafting without betting an unrecoverable outcome on a
   confident guess.
5. **Benefit:** Risk reduction (primary); it also *unblocks* delegation — you can hand
   off more once the irreversible step is fenced (secondary). **Documented** (vendor
   guidance to validate high-stakes outputs) + **Expected** (the human-authority
   framing is an operating principle, not a vendor feature).
6. **Sources (verified 2026-07-21):** Anthropic, "Reduce hallucinations" —
   https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
   ("Always validate critical information, especially for high-stakes decisions").
   *(This is primarily an operating-practice post; the source backs the "high-stakes →
   human validation" principle, it does not describe a product feature.)*
7. **Visual:** A conveyor: AI drafts → a fork. Reversible items (a first draft, a
   summary, a code sketch) roll straight through. Irreversible items (send email, ship
   to prod, change price, sign) hit a human "approve" gate. Takeaway: *draft with AI;
   decide the unrecoverable things yourself.*
8. **Not generic / not a duplicate:** Not "keep a human in the loop" as a slogan — the
   line is drawn on **reversibility/cost**, a concrete test. Distinct from #4 (review
   posture) and idea 4 (verify the *content*): this is about *who has authority to act*
   on a class of decisions.
9. **Score:** impl 4 · reach 5 · impact 5 · evidence 4 · visual 4 · durability 5 ·
   novelty 3 (adjacent to #4 / idea 4) = **30**. Penalties 0.
10. **Boundary:** Don't gate *reversible* work behind a human — that just recreates the
    bottleneck AI was meant to remove. The gate is for the unrecoverable step only;
    everything you can undo should flow freely.

---

### Idea 6 — "I stopped accepting a wall of text; I name the shape first" (ask for the short version) · **29/35**

> **Already briefed as provisional #7** (`research/t4-ask-for-the-short-version.md`).
> Listed for completeness and re-voiced in first person; not new work.

1. **Hook:** *I used to ask one small question and get an essay, then skim for the one
   line that mattered. Now I name the shape before I ask — "one sentence," "three
   bullets," "decision plus reason."*
2. **Problem:** You ask something small and get twelve paragraphs; the answer is buried
   and every extra word costs attention (and, in an app, tokens and context).
3. **The one change:** Name the **shape** of the answer up front — a container
   (one sentence / three bullets / one paragraph / decision + reason), not a mood.
4. **Mechanism (plain):** Output is generated word by word until the model decides to
   stop; length is downstream of your instruction, not a fixed trait. A named shape
   stops it early and puts the point where you can see it.
5. **Benefit:** Cognitive load (primary, universal); saved cost + preserved context in
   API use (secondary). **Documented** (length is a dial) + **Measured** (illustrative
   token counts, two prompts — not a ratio).
6. **Sources (verified 2026-07-21):** OpenAI Cookbook, "GPT-5 New Params and Tools" —
   https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools.
   Anthropic, "Prompting best practices" (verbosity) & "Reducing latency" ("Ask for
   shorter responses… ask Claude to curb its chattiness"). See the full brief for
   verbatim quotes.
7. **Visual:** Same question, two answers side by side — a buried-point wall of text vs
   three tight lines — with a small "shapes" chip row. Takeaway: *set the length; long
   answers cost you attention twice.*
8. **Not generic / not a duplicate:** It's the *output* lever (distinct from #6's
   *input* order). Already de-duplicated in its own brief.
9. **Score:** impl 4 · reach 5 · impact 4 · evidence 4 · visual 4 · durability 4 ·
   novelty 4 = **29**. Penalties 0.
10. **Boundary:** Shorter isn't always better — audits, teaching, and hand-offs want the
    long version. Match the shape to the job.

---

### Idea 7 — "I stopped sending one giant prompt and broke it into a few steps" (decompose the ask) · **28/35**

1. **Hook:** *I used to cram the whole job into one enormous prompt and hope. Now I run
   it as three short steps and check the middle one — the quality jumped and I can see
   where it goes wrong.*
2. **Problem:** One giant prompt asking for everything at once produces a muddled
   answer, and when it's wrong you can't tell which part failed.
3. **The one change:** Break a complex request into **a few sequential steps** —
   draft → review against criteria → refine — instead of one monolithic prompt.
4. **Mechanism (plain):** Each step is a clean, focused task the model does well, and
   the seam between steps is a place you can *inspect* — catch a bad draft before it
   contaminates the final answer. One prompt hides its own mistakes; a short pipeline
   surfaces them.
5. **Benefit:** Quality + repeatability (primary); debuggability — you can see and fix
   the failing step (secondary). **Documented** (chaining / self-correction pattern).
6. **Sources (verified 2026-07-21):** Anthropic, "Prompting best practices" (Chain
   complex prompts) —
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
   ("The most common chaining pattern is self-correction: generate a draft → have
   Claude review it against criteria → have Claude refine"; "Each step is a separate
   API call so you can log, evaluate, or branch") — *fetch-verified (summarizer).*
   OpenAI, "Prompt engineering" —
   https://developers.openai.com/api/docs/guides/prompt-engineering ("Decompose the
   user's query into all required sub-tasks and confirm that each is completed") —
   *fetch-verified (summarizer).*
7. **Visual:** Left — one bloated prompt → a tangled answer with a hidden ✗. Right —
   three linked cards (Draft → Check → Fix) with a magnifying glass on the middle seam.
   Takeaway: *a few steps you can inspect beat one prompt you can't.*
8. **Not generic / not a duplicate:** One concrete restructuring with an inspectable
   seam, not "think step by step." No existing post covers task decomposition; distinct
   from #3 (queue of *issues*, not steps of one *prompt*).
9. **Score:** impl 4 · reach 4 · impact 4 · evidence 4 · visual 4 · durability 4 ·
   novelty 4 = **28**. Penalties 0.
10. **Boundary:** Don't over-split — a simple ask doesn't need a pipeline, and every
    extra step adds latency and cost. Chain when you need to *inspect the middle* or
    the task genuinely has distinct stages.

---

### Idea 8 — "I stopped re-wording the same prompt and saved it as a template" (one slot, not a rewrite) · **27/35**

1. **Hook:** *I kept re-typing the same prompt with one detail changed, slightly
   different every time — and getting slightly different results every time. Now it's
   one saved template with a single blank to fill.*
2. **Problem:** You retype a near-identical prompt for a recurring task, and the small
   wording drift gives you inconsistent output you can't compare or trust.
3. **The one change:** Freeze the recurring prompt as a **template with one variable
   slot**; change only the slot each run, not the whole prompt.
4. **Mechanism (plain):** The fixed part stays byte-identical, so the only thing that
   varies between runs is the input you meant to vary. Same structure in → comparable
   output out. You stop re-deciding the wording every time.
5. **Benefit:** Repeatability + cognitive load (primary); it also sets up cache reuse
   from #6 as a bonus (secondary). **Documented** (template consistency/efficiency).
6. **Sources (verified 2026-07-21):** Anthropic, "Prompt templates and variables"
   (Console prompting tools) —
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-tools
   ("A prompt template combines these fixed and variable parts, using placeholders for
   the dynamic content"; "Consistency: Ensure a consistent structure… across multiple
   interactions"; "use prompt templates… when you expect any part of your prompt to be
   repeated in another call") — *fetch-verified (summarizer).*
7. **Visual:** Left — five sticky notes of the "same" prompt, each subtly different,
   arrows to five inconsistent answers. Right — one template card with a highlighted
   `{{slot}}`, arrows to consistent answers. Takeaway: *stop rewording it — save it
   with one blank.*
8. **Not generic / not a duplicate:** A concrete artefact (a reusable template), not
   "reuse your prompts." Distinct from idea 1 (that saves *project context*; this saves
   a *task prompt* shape). Complements #6 rather than repeating it (that's cost order;
   this is consistency + not re-authoring).
9. **Score:** impl 4 · reach 4 · impact 4 · evidence 4 · visual 4 · durability 4 ·
   novelty 3 (adjacent to idea 1) = **27**. Penalties 0.
10. **Boundary:** Templates suit *recurring* tasks; a genuine one-off doesn't need one,
    and a template applied to a task it wasn't shaped for quietly forces the wrong
    structure. Template the repeats, write the one-offs fresh.

---

### Idea 9 — "I gave my routine work to the small model and kept the big one for the hard calls" (route by stakes) · **28/35**

1. **Hook:** *I used to run everything through the most capable model "to be safe."
   Then I noticed most of my calls were formatting, extraction, and quick lookups. Now
   the small fast model does those, and the big model only sees the hard decisions.*
2. **Problem:** Defaulting every task to the biggest model is slow and expensive for
   the 80% of work that a small, fast model handles perfectly well.
3. **The one change:** **Route by task type**, not by habit — cheap/fast model for
   simple high-volume work (formatting, extraction, classification, first drafts),
   most capable model reserved for genuinely hard or high-value decisions.
4. **Mechanism (plain):** Capability, speed, and cost trade against each other. Simple
   tasks don't consume the extra capability you paid for, so a smaller model returns
   the same usable answer faster and cheaper; you spend the expensive model only where
   its extra intelligence changes the outcome.
5. **Benefit:** Money + speed (primary); it also frees you to run *more* small tasks
   without watching the bill (secondary). **Documented** (vendor model-selection
   guidance) — no universal savings figure claimed.
6. **Sources (verified 2026-07-21):** Anthropic, "Choosing the right model" —
   https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
   ("balancing three key considerations: capabilities, speed, and cost"; "starting with
   a faster, more cost-effective model… can be the optimal approach"). OpenAI, "Model
   selection" —
   https://developers.openai.com/api/docs/guides/model-selection ("Optimize for cost
   and latency second: … maintain accuracy with the cheapest, fastest model possible")
   — *fetch-verified (summarizer).*
7. **Visual:** A two-lane sorter. A stream of tasks drops onto a fork: "simple / high
   volume" → small-fast-cheap model lane; "hard / high value" → big model lane.
   Takeaway: *match the model to the stakes, not to your default.*
8. **Not generic / not a duplicate — adjacency to #1 flagged:** Post #1 makes a
   *benchmark* claim ("on BrowseComp, Opus-low beats Sonnet-high" — one counterintuitive
   operating point). This makes a *routing habit* claim ("send simple work to the
   small model, reserve the big model for decisions") — no benchmark, no cost chart.
   The framings are genuinely different, but the visual must **not** reuse a
   model×effort cost chart or it collapses into #1.
9. **Score:** impl 4 · reach 5 · impact 4 · evidence 4 · visual 4 · durability 4 ·
   novelty 3 (adjacent to #1) = **28**. Penalties 0 (adjacency neutralised by the
   routing framing; would incur −2 if drawn as a benchmark chart).
10. **Boundary:** "Simple" is about the *task*, not the topic — a short prompt can still
    hide a hard judgement. Spot-check that the small model actually clears your bar on a
    task type before you route it there permanently; when accuracy outweighs cost, start
    big.

---

### Idea 10 — "I make every answer separate what's known, what was decided, and what's next" (three sections, not soup) · **26/35**

1. **Hook:** *I kept getting one smooth paragraph that blended facts, opinions, and
   to-dos — and I couldn't tell which was which. Now I ask for three labelled parts:
   facts, decisions, next actions.*
2. **Problem:** A single fluent block mixes verified facts with the model's guesses and
   with things you're supposed to do, so you can't see what to trust or what to act on.
3. **The one change:** Ask every substantive answer to come in **three labelled
   sections — Facts / Decisions / Next actions** — instead of one undivided block.
4. **Mechanism (plain):** Steering the *format* is one of the most reliable levers you
   have. Forcing the separation makes the model sort its own output: what it's asserting
   as fact, what it concluded, and what it's asking you to do — so you can verify the
   facts, own the decisions, and act on the list without untangling them.
5. **Benefit:** Cognitive load + risk (primary — facts you can check are separated from
   guesses); repeatability across answers (secondary). **Documented** (format control /
   examples steer structure) + **Expected** (the specific three-section split is an
   operating habit, not a vendor feature).
6. **Sources (verified 2026-07-21):** Anthropic, "Prompting best practices" (Control
   the format of responses; Use examples) —
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
   ("Examples are one of the most reliable ways to steer Claude's output format, tone,
   and structure") — *fetch-verified (summarizer).* *(This is primarily a practice; the
   source backs "format is a steerable lever," not this exact template.)*
7. **Visual:** Left — one grey blob paragraph with facts/opinions/to-dos tangled
   (colour-coded words scattered through it). Right — three clean stacked cards: FACTS ·
   DECISIONS · NEXT ACTIONS, each colour sorted. Takeaway: *make it sort itself:
   what's known, what was decided, what's next.*
8. **Not generic / not a duplicate:** A named output contract, not "be organised."
   Distinct from #7/idea 6 (that's *length*; this is *semantic structure*) and from #2
   (that's a *decision record you keep over time*; this is the *shape of a single
   answer*).
9. **Score:** impl 4 · reach 4 · impact 4 · evidence 3 · visual 5 · durability 4 ·
   novelty 3 (adjacent to idea 6 / #2) = **26**. Penalties 0.
10. **Boundary:** Three sections suit answers you'll *act on*; for a quick factual
    lookup or a creative draft the scaffolding is overhead. And the labels don't make
    the "Facts" true — you still verify them (idea 4). Structure aids trust; it doesn't
    grant it.

---

### Also considered, held back this round

- **"Reset the thread, keep the record" (a long chat is not your memory).** This was
  candidate **T2** (v3, 25/30) — reset a bloated thread and start fresh from a compact
  decision record. It is strong and broad, but it sits between #5 (external memory) and
  idea 2 (project brief), and its cleanest cut still overlaps idea 10's "keep decisions
  legible." Held for a later round to be framed sharply as *in-context window hygiene*
  so it doesn't read as a memory-store post. (Not counted in the ranked ten to keep the
  list to genuinely distinct decisions.)
- **"Queue it, don't babysit it" (async / background work).** Candidate **T5** (v3,
  24/30). Broad and clean, but it splits into two mechanisms (consumer Tasks vs a
  developer background job) and leans toward the excluded Batch API territory. Held
  until it can be voiced as one first-person attention decision.

---

## 4. Best 3 to produce next

Chosen for the highest scores, the strongest one-image legibility, mutual
distinctness, and evidence that's documented today. Together they form one coherent
run — **"arrange the context on purpose"** — without repeating any shipped post.

1. **Idea 1 — the reusable project brief (33).** Highest score, benchmark-level reach
   ("everyone has re-typed the same context"), a filing-cabinet idea a non-engineer
   gets instantly, trivially one image, well-sourced. *Recommended as the single next
   post — see §5.*
2. **Idea 2 — examples beat adjectives (32).** The strongest *evidence* of the set
   ("most reliable way to steer," "3–5 examples"), a crisp before/after visual, and it
   teaches something most casual users never learned — show, don't describe.
3. **Idea 3 — give the model the file, not your memory (31).** High reach and durable;
   pairs naturally with idea 2 (what you *show*) and idea 1 (what you *save*), and lands
   a quality/risk benefit the audience feels immediately.

Sequencing note: idea 6 (ask for the short version) is already briefed as #7 and should
ship on its existing plan; ideas 4, 5, 7 form a strong "verify / decide / decompose"
follow-on cluster after the three above.

---

## 5. Recommended next topic + infographic copy draft

**Recommended next post: Idea 1 — "I stopped re-explaining my project in every chat"
(a reusable project brief).**

Why this one: it tops the ranking (33/35), it is the most broadly legible idea in the
set — the "re-typed the same context into a fresh chat" moment is nearly universal —
and it survives one image as cleanly as the Post #1 benchmark. It is distinct from
everything shipped, and in the author's first-person voice it reads as a genuine
operating change, not a tip.

**One-image infographic copy draft (single 1080×1350 canvas, *Operator's Field Notes*):**

- **Eyebrow:** `Inside of the Day #8 — A reusable project brief`
- **Headline:** **I stopped re-explaining my project in every chat.**
- **Dek (one line):** *Write the standing context once — attach it to the workspace,
  not the message.*
- **LEFT panel — "Every chat from zero":** three separate chat windows, each re-typing
  the *same* block ("who I am · the project · the rules · the 3 reference files").
  Small tag: *slow, drifts, two chats end up different.*
- **RIGHT panel — "Written once":** a single **Project brief** card feeding all three
  chats from one source. Small tag: *every chat starts already knowing it.*
- **Mechanism strip (one line):** *The brief is loaded into context at the start of
  every conversation in that space — ChatGPT Project / Custom Instructions · Claude
  Project · `CLAUDE.md`.*
- **Takeaway (bold):** **Write the standing context once; stop paying for it every
  turn.**
- **Caveat line (small, visible):** *It's context, not a contract — the model treats a
  brief as guidance, not enforced rules. Keep it short and unambiguous.*
- **Footer:** `Sources: Anthropic — Claude Code memory & Projects · OpenAI — Projects ·
  verified 2026-07-21 · @vitalylobachev`

**Caption angle (not a full caption):** a short field note — *"the first thing I paste
into a new chat used to be my project; now I never paste it at all"* — one paragraph on
attaching the brief to the workspace, one line that it's context not enforcement, no
thread.

**Re-verify before render:** the exact "loaded into the context window at the start of
every session" wording (code.claude.com/docs/en/memory), the Projects-instructions
wording (support.claude.com), and current product names/paths (Custom Instructions,
Projects) — feature names move.

---

## 6. Source index

All opened 2026-07-21. Entries marked *(summarizer)* were fetched live today through the
fetch tool's summarizer — URL and substance confirmed, exact wording to be re-confirmed
against the live page at publish. Anthropic's standalone prompt-engineering sub-pages
(multishot, chain-prompts, long-context-tips) now redirect into the consolidated
**"Prompting best practices"** page; sections are named per topic.

**Anthropic / Claude**
- Claude Code memory — https://code.claude.com/docs/en/memory *(ideas 1)*
- Manage projects (Help) — https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects *(idea 1)*
- Managing context (blog) — https://claude.com/blog/context-management *(held-back T2)*
- Prompting best practices (examples · chaining · long-context · format) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices *(ideas 2, 3, 7, 10 — summarizer)*
- Prompt templates & variables (Console prompting tools) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-tools *(idea 8 — summarizer)*
- Reducing latency (ask for shorter responses) — https://platform.claude.com/docs/claude/docs/reducing-latency *(idea 6)*
- Citations — https://platform.claude.com/docs/en/build-with-claude/citations *(idea 4)*
- Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations *(ideas 4, 5)*
- Choosing the right model — https://platform.claude.com/docs/en/about-claude/models/choosing-a-model *(idea 9)*

**OpenAI**
- Projects (Academy) — https://academy.openai.com/public/clubs/work-users-ynjqu/resources/projects *(idea 1)*
- Prompt engineering — https://developers.openai.com/api/docs/guides/prompt-engineering *(ideas 2, 7 — summarizer)*
- Model selection — https://developers.openai.com/api/docs/guides/model-selection *(idea 9 — summarizer)*
- Reasoning (effort tradeoff) — https://developers.openai.com/api/docs/guides/reasoning *(idea 9 — summarizer)*
- File inputs — https://platform.openai.com/docs/guides/file-inputs *(idea 3 — summarizer)*
- GPT-5 New Params and Tools (Cookbook, verbosity) — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools *(idea 6)*
- Pricing — https://developers.openai.com/api/docs/pricing *(ideas 6, 9 — output≫input structure only; specific model rows not cited)*

**Reachability note:** consumer `help.openai.com` pages return 403 to automated fetch
and are not quoted. The OpenAI model *names/prices* surfaced by the summarizer are
**not** cited as fact anywhere above — only the structural guidance ("cheapest, fastest
model possible"; output billed above input) is used, and pricing must be re-read live at
publish.

---

## 7. Self-review

- **Generic advice?** Each idea names one concrete change with a mechanism, not a mood:
  *attach the brief* (not "give context"), *paste 3–5 examples* (not "be specific"),
  *attach the file + quote first* (not "use RAG"), *three labelled sections* (not "be
  organised"), *route by task type* (not "save money"). Anything that read as a slogan
  ("keep a human in the loop," "write better prompts") was rewritten to a testable rule
  (reversibility gate; examples-over-adjectives). **Pass.**
- **News framing?** No idea leads with a vendor or a release. Every hook is a
  first-person operating change ("I stopped…", "I gave…", "I make…"); the source proves
  the mechanism and never opens the post. **Pass.**
- **Duplication?** All ten are checked against the twelve spoken-for decisions (§2).
  Three real adjacencies are flagged with an explicit distinction and a visual
  guardrail: idea 4 ↔ #4 (verify *step* vs review *posture*), idea 5 ↔ #4/idea 4
  (decision *authority* vs content *review*), idea 9 ↔ #1 (routing *habit* vs benchmark
  *operating point* — must not reuse a cost chart). Idea 6 is disclosed as the
  already-briefed #7. T2 and T5 are held back rather than force-fit. **Pass.**
- **Unsupported claims?** Product-specific claims cite an opened page; figures are
  labelled Documented / Measured / Expected. The one number in play (long-context "up to
  30%") is marked Measured and illustrative. Ideas 5 and 10 are labelled as *operating
  practice* where the source backs only the underlying principle, not a feature. No
  universal cost/quality percentage is asserted. **Pass.**
- **Evidence caveat (honest limitation):** several quotes were captured today via the
  fetch summarizer, not a raw page read, and are marked *(summarizer)*; exact wording
  must be re-confirmed at publish. The OpenAI model IDs the summarizer returned are
  treated as possibly unreliable and are **not** cited — only structural guidance is
  used. **Flagged, not hidden.**
- **One-image survivability:** every idea reduces to problem → one mechanism →
  takeaway, each with a concrete before/after visual. **Pass.**
- **Stalest facts to re-verify at publish:** product/feature names and paths (Projects,
  Custom Instructions, prompt-tools, file-inputs), the consolidated prompting-best-
  practices anchors, the "up to 30%" figure, and all pricing. Re-fetch before render.
