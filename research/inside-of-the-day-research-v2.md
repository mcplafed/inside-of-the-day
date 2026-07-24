# Inside of the Day — Research v2

> Idea-finding system for one-image LinkedIn infographics.
> Research document only — not final social copy, not an infographic.
> Compiled 2026-07-21. All impact figures are labelled **Documented** (stated by the vendor),
> **Measured** (a published measurement), or **Expected** (mechanism implies it, no number stated).

---

# 1. Editorial reset

- **One image, one thought.** Each post is a single 1080×1350 infographic (rendered 3× → 3240×4050 PNG). Not a carousel, not a multi-topic roundup, not an "interesting AI news" feed.
- **One operating decision.** Every post communicates exactly one thing a reader can implement or use to make a decision *today*: change X to Y because Z. If it needs a step-by-step tutorial, it does not qualify.
- **One mechanism, in plain English.** The visual must carry problem → mechanism/choice → takeaway on its own, understandable without reading the caption.
- **Credible, concrete effect required.** A candidate must plausibly move at least one of: engineering efficiency, API/model spend, latency, throughput, reproducibility, reliability, quality, safety, or operational clarity. Secondary categories welcome when genuine: coordination overhead, context waste, debuggability, portability, vendor-risk, human/agent handoffs.
- **Operator's field note, not hype.** Practical, opinionated, specific. No "AI is changing everything", no "write better prompts", no vendor cheerleading.
- **Sourced or it does not ship.** Every factual claim cites a canonical primary source (prefer Anthropic/OpenAI official docs & posts). Snippets are not evidence — the source page must be opened. Documented behaviour is separated from our recommendation.
- **Never fabricated.** No invented benchmarks, discounts, limits, API behaviour, or URLs. Expected benefits are labelled expected and explained by mechanism.
- **What disqualifies a candidate:** requires a carousel; benefit is vague or unmeasurable; the only "source" is marketing; it is a minor variation of a topic already published; the reader cannot act on it after one look.

---

# 2. Existing-post map (do-not-repeat boundary)

| # | Topic | Mechanism | Impact category | Sources | Do-not-repeat boundary |
|---:|---|---|---|---|---|
| 1 | Sonnet 5 high vs Opus 4.8 low | Pick the operating point: model × effort × harness; more effort ≠ better | Cost, quality | anthropic.com/news/claude-sonnet-5; platform.claude.com cookbook (agentic-search evals); platform.claude.com/docs pricing | Do not re-argue "compare model×effort" or reuse a benchmark-cost chart as the payload. Effort/thinking-budget candidates must attack a *different* decision (e.g. latency floor, not benchmark cost). |
| 2 | Founder-gated questions | Park the blocked task, keep independent ready work moving, batch founder decisions into the work summary as an async decision interface | Coordination, throughput | Author's operating practice (agent-automation-kit) | Do not repeat "park blocked work / async human decisions / work summary as interface." |
| 3 | The real stopping condition | Ready **queue empty** — not merged PRs — is the done signal for an autonomous system | Operational clarity, throughput | github.com/vlobachev/agent-automation-kit | Do not repeat "queue vs PR count / when is a session done." |
| 4 | Review the work, not the AI label | Review diff + rationale + tests + CI + operational effect; drop AI-attribution footers | Quality, reliability | Author's global CLAUDE.md convention | Do not repeat "provenance vs evidence / drop Co-Authored-By." |
| 5 | Graphiti vs Cognee vs Graphify | Three external memory graphs for three question types (temporal / documents / code structure) | Operational clarity, reproducibility | github.com/getzep/graphiti; github.com/topoteretes/cognee; github.com/Graphify-Labs/graphify | Do not repeat "agent memory layering across external stores." An *in-context* memory/pruning candidate is allowed only if it is clearly about context-window management, not external graphs. |

*Post 5 is complete in the `inside-day-05-scheduled` worktree and is treated as published for de-duplication.*

---

# 3. Candidate scoring rubric

Each candidate is scored 0–5 on six axes; the composite is the sum (max 30). Penalties are subtracted from the composite.

| Axis | 0 | 3 | 5 |
|---|---|---|---|
| **Implementation clarity** | No concrete change | A change a reader could make this week | A one-line/one-flag/one-parameter change a reader can make today |
| **Impact potential** | Marginal or unclear | Real effect on one category | Large, obvious effect on a category engineers care about (cost, latency, reliability…) |
| **Evidence strength** | Marketing/none | Documented behaviour, no number | Vendor-documented **with a figure** or an official measurement |
| **Visual compression** | Needs a tutorial/carousel | Fits with effort | One problem + one mechanism/matrix + one takeaway, trivially |
| **Durability** | Expires in weeks | Useful for a few months | A structural lesson that survives model/version churn |
| **Novelty vs series** | Overlaps an existing post | Adjacent but distinct decision | A decision the series has never made |

**Penalties (subtract from composite):**
- −3 hype / "AI is changing everything" framing with no operating decision.
- −2 vague advice ("use evals", "write better prompts") with no specific mechanism.
- −2 vendor marketing dressed as insight / no primary source with a real claim.
- −2 evidence is only a blog snippet, not an opened primary page.
- −3 cannot survive the one-image constraint (needs multi-step tutorial or carousel).
- −2 minor variation of prompt caching / effort tuning already implied by the backlog.

A candidate scoring below ~20/30 after penalties is rejected for now.

---

# 4. Ranked research backlog

All sources opened as primary pages on **2026-07-21**. Impact is labelled **Documented** (vendor states the behaviour), **Measured** (a published measurement/eval — noted as vendor-internal where relevant), or **Expected** (mechanism implies it, no figure stated). Score is composite /30 minus penalties (see §3).

---

### C1 — "Put the stable part first" (prompt caching) · **Score 29/30**
- **Decision:** Order every prompt as `[stable: system + tools + few-shot + docs] → [variable: user turn]` so the long prefix is cache-eligible.
- **Mechanism:** Both providers cache on an **exact prefix match**. Cached input is billed at a large discount; variable content up front breaks the match and you pay full price on every call.
- **Impact category:** Cost (primary), latency (secondary).
- **Status:** Documented (cost). Latency = Expected/qualitative — neither vendor states a number.
- **Sources:**
  - Anthropic, "Prompt caching", Claude Platform Docs — https://platform.claude.com/docs/en/build-with-claude/prompt-caching (no visible date)
  - OpenAI, "Prompt caching", OpenAI API docs — https://developers.openai.com/api/docs/guides/prompt-caching (no visible date); pricing: https://developers.openai.com/api/docs/pricing
- **Evidence:** Anthropic — "Cache read tokens are 0.10 times the base input tokens price" (~90% off); default 5-min TTL "refreshed for no additional cost each time the cached content is used"; min cacheable prefix is model-specific (1,024 tokens for Opus 4.8 / Sonnet 5). OpenAI — "Caching is enabled automatically… no code changes"; "available for prompts containing 1024 tokens or more"; "Cache hits are only possible for exact prefix matches"; "place static content… at the beginning." Both: "improved time-to-first-token" (qualitative).
- **Caveats:** Cache **reads still cost ~10%** (not free); writes cost more (Anthropic 1.25× at 5-min / 2× at 1-hour; OpenAI 1.25× on GPT-5.6+). OpenAI's exact ~90% is pricing-page-derived and model-specific, not a fixed documented %. Min-token thresholds vary by model.
- **Visual:** Vertical prompt bar split into a big shaded "STABLE PREFIX → cached (0.1×)" block and a thin "VARIABLE TAIL → full price" block, with a dashed cache boundary; one figure callout (`0.1× base input`).
- **Not a duplicate:** Post 1 compared model×effort operating points; the series has never covered request structure / caching.

---

### C2 — "Not urgent? Halve the bill" (Batch API) · **Score 28/30**
- **Decision:** Route non-interactive generation (evals, backfills, embeddings, bulk classification) to the batch endpoint instead of the synchronous API.
- **Mechanism:** Async queue with a completion window; both vendors price it at 50% of synchronous rates.
- **Impact category:** Cost.
- **Status:** Documented.
- **Sources:**
  - Anthropic, "Batch processing", Claude Platform Docs — https://platform.claude.com/docs/en/build-with-claude/batch-processing
  - OpenAI, "Batch API", OpenAI API docs — https://developers.openai.com/api/docs/guides/batch
- **Evidence:** Anthropic — "All usage is charged at 50% of the standard API prices"; ≤100,000 requests or 256 MB; "most batches completing within 1 hour," 24-hour hard cap; results kept 29 days; stacks with prompt caching. OpenAI — "50% cost discount compared to synchronous APIs"; "completes within 24 hours"; ≤50,000 requests / 200 MB; supports `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, etc.
- **Caveats:** Only for work that tolerates minutes-to-hours latency. For batches Anthropic recommends the 1-hour cache TTL (jobs can exceed the 5-min window).
- **Visual:** Two lanes — "SYNC · $X · seconds" vs "BATCH · $X/2 · ≤24 h" — with a bold `−50%` badge bridging them.
- **Not a duplicate:** No existing post addresses request scheduling or cost tiers.

---

### C3 — "Stop parsing-and-retrying JSON" (structured outputs) · **Score 28/30**
- **Decision:** Turn on constrained/strict structured outputs instead of prompting for JSON and re-parsing.
- **Mechanism:** The decoder is constrained to your JSON Schema, so malformed output (and the parse-fail → retry loop) largely disappears.
- **Impact category:** Reliability, reproducibility, efficiency (fewer retries).
- **Status:** Documented (with explicit exception cases).
- **Sources:**
  - Anthropic, "Structured outputs", Claude Platform Docs — https://platform.claude.com/docs/en/build-with-claude/structured-outputs (GA)
  - OpenAI, "Structured model outputs", OpenAI API docs — https://developers.openai.com/api/docs/guides/structured-outputs
- **Evidence:** Anthropic — "guarantee schema-compliant responses through constrained decoding"; "Always valid: No more `JSON.parse()` errors"; combine `tool_choice:{"type":"any"}` + `strict:true` to guarantee a schema-valid tool call. OpenAI — outputs "always generate responses that adhere to your supplied JSON Schema"; "No need to validate or retry incorrectly formatted responses."
- **Caveats:** Not unconditional — both carve out **refusals** and **token-limit truncation** (`stop_reason:"max_tokens"` / length). Constrains structure, **not field values**. Anthropic: 20 strict tools/request cap; **incompatible with Citations (400 error)**. OpenAI strict from GPT-4o-2024-08-06 and later.
- **Visual:** Before/after: left = a retry loop (`prompt → parse error → retry ×3`), right = a single arrow into a locked schema box (`valid, first try`).
- **Not a duplicate:** Series has never covered API-level reliability primitives.

---

### C4 — "Pick a speed tier per request" (service_tier: flex / default / priority) · **Score 27/30**
- **Decision:** Set `service_tier` to match each workload's latency SLA to its price — `flex` for cheap/slow, `priority` for fast/premium.
- **Mechanism:** One request parameter selects the processing lane; cost and latency move in opposite directions.
- **Impact category:** Cost ↔ latency dial.
- **Status:** Documented (flex pricing); priority premium multiplier Expected/Unverified.
- **Sources:**
  - OpenAI, "Flex processing", OpenAI API docs — https://developers.openai.com/api/docs/guides/flex-processing
  - OpenAI, "Priority processing", OpenAI API docs — https://developers.openai.com/api/docs/guides/priority-processing
- **Evidence:** Flex — "lower costs… in exchange for slower response times and occasional resource unavailability"; priced "at Batch API rates" (≈50% off); not charged on 429 "Resource Unavailable." Priority — "significantly lower and more consistent latency… billed at a premium to standard." Values: `auto`(default)/`default`/`flex`/`priority`.
- **Caveats:** Flex is **beta** with limited model availability; exact priority premium is **not stated** on the guide (a ~2× figure was summariser-derived — treat as Unverified). OpenAI-specific.
- **Visual:** Three-column tier matrix (Flex / Standard / Priority) × (relative $, relative latency) with arrows showing the trade.
- **Not a duplicate:** Distinct from C2 (batch is async jobs; this is per-request live tiering).

---

### C5 — "One protocol, not N integrations" (MCP) · **Score 27/30**
- **Decision:** Expose tools/data through a Model Context Protocol server (or the API's MCP connector) instead of bespoke per-app, per-model integrations.
- **Mechanism:** A single open client/server standard (JSON-RPC) — "USB-C for AI" — turns an N×M integration matrix into N+M.
- **Impact category:** Portability, vendor-risk reduction, coordination overhead.
- **Status:** Documented (open standard); integration-savings figure Expected (not quantified).
- **Sources:**
  - modelcontextprotocol.io, "What is the Model Context Protocol (MCP)?" — https://modelcontextprotocol.io/ ; spec rev — https://modelcontextprotocol.io/specification/2025-06-18
  - Anthropic, "Introducing the Model Context Protocol", 2024-11-25 — https://www.anthropic.com/news/model-context-protocol ; connector: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- **Evidence:** "an open-source standard for connecting AI applications to external systems"; "Think of MCP like a USB-C port for AI applications"; Anthropic — "replacing fragmented integrations with a single protocol." Official intro lists Claude, ChatGPT, VS Code, Cursor as adopters.
- **Caveats:** API connector is **beta** (header `mcp-client-2025-11-20`, previous one deprecated); connector supports tool calls only, public HTTP servers only, not on Bedrock/Google Cloud, not covered by ZDR. Broader ecosystem-size numbers seen in search were Unverified.
- **Visual:** Left = tangled N×M web of app→tool wires; right = clean hub where apps and tools each plug into one MCP port.
- **Not a duplicate:** Post 5 is about *external memory stores*; this is an *integration/interoperability* standard.

---

### C6 — "Let the agent forget its own scrollback" (context editing) · **Score 26/30**
- **Decision:** Enable server-side context editing so stale tool calls/results are auto-cleared as a long agent run approaches the token limit.
- **Mechanism:** Before the prompt reaches the model, old tool results are dropped from the window (client keeps full history); the run continues instead of hitting context exhaustion.
- **Impact category:** Efficiency/cost, reliability (run completion).
- **Status:** Measured (vendor-internal eval, single benchmark).
- **Sources:**
  - Anthropic, "Context editing", Claude Platform Docs — https://platform.claude.com/docs/en/build-with-claude/context-editing (beta header `context-management-2025-06-27`)
  - Anthropic, "Managing context on the Claude Developer Platform", 2025-09-29 — https://claude.com/blog/context-management
- **Evidence:** "context editing enabled agents to complete workflows that would otherwise fail due to context exhaustion—while reducing token consumption by 84%" (100-turn web-search eval); "Context editing alone delivered a 29% improvement"; with the memory tool, "39% over baseline." Default clearing trigger 100,000 input tokens, keep 3 recent tool uses.
- **Caveats:** 84%/29%/39% are **Anthropic internal-eval figures from one benchmark** — not guarantees. **Beta**; server-side compaction is now positioned as the "primary" long-context strategy. Anthropic-only.
- **Visual:** A filling context bar; older tool-result chunks fade/clear at the 100k mark while recent turns stay, keeping the bar under the ceiling.
- **Not a duplicate:** Post 5 = external memory graphs; this is **in-context** window management.

---

### C7 — "Cite the span or don't answer" (Citations API) · **Score 26/30**
- **Decision:** Enable Citations on source documents so answers return the exact supporting passages.
- **Mechanism:** Documents are chunked to sentences; the model attaches span-level references to each claim, making RAG answers verifiable.
- **Impact category:** Quality, safety (hallucination reduction), auditability.
- **Status:** Documented behaviour + Measured (vendor-internal recall figure).
- **Sources:**
  - Anthropic, "Citations", Claude Platform Docs — https://platform.claude.com/docs/en/build-with-claude/citations
  - Anthropic, "Introducing Citations on the Anthropic API", 2025-06-23 — https://claude.com/blog/introducing-citations-api
- **Evidence:** "Citations return the exact passages that support each claim, so you can verify answers and surface sources"; news — "increasing recall accuracy by up to 15%."
- **Caveats:** "up to 15%" is a vendor internal eval (Jan-2025-era, 3.5 models). **Incompatible with structured outputs (400).** Enable per document.
- **Visual:** An answer with two claims, each underlined and wired to a highlighted sentence in a source-doc panel.
- **Not a duplicate:** No prior post covers grounding/provenance of *model answers* (post 4 is about *human* review of PRs, not citation).

---

### C8 — "Paste the old file to speed up the edit" (Predicted Outputs) · **Score 25/30**
- **Decision:** When regenerating a file/text with small changes, pass the current version as `prediction`.
- **Mechanism:** The model confirms predicted tokens instead of generating them from scratch, cutting time-to-completion for large-but-mostly-unchanged outputs.
- **Impact category:** Latency/speed.
- **Status:** Documented mechanism; latency figure Expected (none stated).
- **Sources:** OpenAI, "Predicted Outputs", OpenAI API docs — https://developers.openai.com/api/docs/guides/predicted-outputs
- **Evidence:** "excels when regenerating text or code files with minor modifications"; rejected predictions are "still billed like other completion tokens."
- **Caveats:** **Rejected prediction tokens are billed** — bad predictions raise cost. Chat Completions only; models gpt-4o / gpt-4o-mini / gpt-4.1 family (not GPT-5); incompatible with `n>1`, penalties, function calling, `max_completion_tokens`.
- **Visual:** A code file with 2 changed lines highlighted; arrow "predict unchanged → regenerate fast," small note "wrong guesses still billed."
- **Not a duplicate:** No latency-mechanism post exists.

---

### C9 — "Know your data posture before you send the token" (no-training-by-default + ZDR) · **Score 24/30**
- **Decision:** Treat "not used for training by default + bounded retention + optional zero-data-retention" as an explicit, verifiable vendor-risk control, and pick the tier your compliance needs.
- **Mechanism:** API inputs/outputs are excluded from training by default; abuse logs have a retention window; OpenAI offers contractual ZDR that also forces `store=false`.
- **Impact category:** Safety/compliance, vendor-risk reduction.
- **Status:** Documented (policy pages) — highly date-sensitive.
- **Sources:**
  - Anthropic, "Is my data used for model training?", 2026-03-16 — https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
  - OpenAI, "Data controls in the OpenAI platform" — https://developers.openai.com/api/docs/guides/your-data
- **Evidence:** Anthropic — "By default, we will not use your inputs or outputs from our commercial products to train our models" (feedback data up to 5 years). OpenAI — "data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in)"; abuse logs "retained for up to 30 days"; ZDR "excludes customer content from abuse monitoring logs."
- **Caveats:** Policies change — re-verify at publish. `openai.com/enterprise-privacy` returned 403 (Unverified by direct fetch); corroborated via the accessible data-controls page. This is more "know + choose a tier" than a code change → lower implementation-clarity.
- **Visual:** Two-vendor matrix rows: Train on API data (No by default) · Retention window · ZDR available.
- **Not a duplicate:** No prior post touches data governance.

---

### C10 — "Instrument LLM calls the vendor-neutral way" (OpenTelemetry GenAI conventions) · **Score 23/30**
- **Decision:** Emit the standard `gen_ai.*` OpenTelemetry attributes (model, provider, token usage) rather than a bespoke logging schema, so you can swap models/observability backends without re-instrumenting.
- **Mechanism:** A shared semantic-convention vocabulary for spans/attributes across providers.
- **Impact category:** Portability, observability, debuggability.
- **Status:** Documented (as an **experimental/Development** convention).
- **Sources:** OpenTelemetry (CNCF), "Gen AI" semantic conventions — https://opentelemetry.io/docs/specs/semconv/gen-ai/ ; attribute registry — https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
- **Evidence:** Standard attributes incl. `gen_ai.provider.name`, `gen_ai.operation.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`/`output_tokens`. Stability badge = **Development**; migration env var `OTEL_SEMCONV_STABILITY_OPT_IN`.
- **Caveats:** **Not stable** — names have already changed (`gen_ai.system`→`gen_ai.provider.name`, `prompt_tokens`→`input_tokens`); content moved repos. Must be labelled "experimental, mid-2026." Lowers durability.
- **Visual:** A single span card with standardised `gen_ai.*` fields feeding three different backend logos.
- **Not a duplicate:** Observability is untouched by the series.

---

### C11 — "Give an agent files, not a bigger prompt" (memory tool) · **Score 23/30**
- **Decision:** Use the provider-native memory tool (client-side `/memories` files) for cross-session persistence instead of stuffing history into context.
- **Mechanism:** The model issues file create/read/update/delete ops your app executes; knowledge persists across sessions with just-in-time retrieval.
- **Impact category:** Efficiency (context savings), continuity.
- **Status:** Documented (GA on Messages API).
- **Sources:** Anthropic, "Memory tool", Claude Platform Docs — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- **Evidence:** "store and retrieve information across conversations… without keeping everything in the context window"; "generally available on the Messages API: no beta header required"; all Claude 4+ models; pairs with context editing.
- **Caveats:** You own storage + path-traversal safety (restrict to `/memories`). Adjacent to Post 5 → novelty capped.
- **Visual:** Context window (small) beside a `/memories` file drawer the agent reads on demand.
- **Not a duplicate (thin):** Post 5 is *external multi-store graphs*; this is *provider-native file memory*. Adjacency noted — hold unless reframed.

---

### C12 — "Long jobs shouldn't hold a socket open" (background mode) · **Score 23/30**
- **Decision:** Run long agent/reasoning tasks with `background:true` on the Responses API and poll, instead of holding a synchronous connection.
- **Mechanism:** The job runs server-side; you poll status (`queued`/`in_progress`) and can resume streaming via `sequence_number`/`starting_after`.
- **Impact category:** Reliability (no timeouts/dropped connections).
- **Status:** Documented; no cost delta.
- **Sources:** OpenAI, "Background mode", OpenAI API docs — https://developers.openai.com/api/docs/guides/background
- **Evidence:** "execute long-running tasks… reliably, without having to worry about timeouts or other connectivity issues."
- **Caveats:** OpenAI-specific; operational (not a cost/quality win); narrower audience.
- **Visual:** Sync call hitting a timeout ✕ vs a background job with a poll loop landing ✓.
- **Not a duplicate:** New operational topic.

---

### C13 — "Buy reasoning only where it pays" (reasoning effort / verbosity floor) · **Score 20/30**
- **Decision:** Default simple tasks (extraction, formatting, classification) to the lowest reasoning setting (`none`/`minimal`) and cap `verbosity`.
- **Mechanism:** Reasoning + output tokens are billed as output; lowering the dial cuts latency and cost where deliberation adds nothing.
- **Impact category:** Cost, latency.
- **Sources:** OpenAI, "Reasoning models" — https://developers.openai.com/api/docs/guides/reasoning ; cookbook "GPT-5 New Params and Tools", 2025-08-07 — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
- **Evidence:** "Lower effort favors speed and lower token usage"; verbosity "output tokens scale roughly linearly": low 560 → medium 849 → high 1,288.
- **Caveats:** **`minimal` (GPT-5 launch) is superseded by `none`** on current models — names churn. **Adjacent to Post 1's effort axis** → −2 novelty penalty applied. `budget_tokens` is not the lever on current Anthropic models (removed/400) — use the effort parameter.
- **Visual:** A dial from `none`→`max` with a cost/latency curve; "simple task = leave it low."
- **Not a duplicate (thin):** Post 1 compares effort *operating points on a benchmark*; this is a *per-task-type default*. Adjacency is real — deprioritised.

---

### C14 — "Chain reasoning, don't replay it" (Responses API statefulness) · **Score 21/30**
- **Decision:** Chain turns with `previous_response_id` so the model carries its reasoning items forward.
- **Mechanism:** Reasoning is handed off between turns "in the most token-efficient manner" without exposing raw chain-of-thought.
- **Impact category:** Efficiency (reasoning handoff), quality (continuity).
- **Sources:** OpenAI, "Conversation state" — https://developers.openai.com/api/docs/guides/conversation-state ; "Reasoning models" — https://developers.openai.com/api/docs/guides/reasoning
- **Evidence:** "Chain responses across turns by passing the previous response ID"; reasoning reuse "in the most token-efficient manner."
- **Caveats (important):** Does **not** reduce *billed* input tokens — "all previous input tokens… are billed as input tokens." "Better cache utilisation" was **not found** in docs → do not claim it. Weakens the headline.
- **Visual:** Turn chain passing a "reasoning" token forward vs re-sending full history.
- **Not a duplicate:** New topic, but the honest benefit is narrow → mid rank.

---

### C15 — "Distil the expensive model into a cheap one" (distillation) · **Score 21/30**
- **Decision:** Capture outputs from a large model tuned to your eval bar, then fine-tune a smaller model on them.
- **Mechanism:** Supervised fine-tuning on large-model traces trains a cheaper model to match the task.
- **Impact category:** Cost (steady-state inference).
- **Sources:** OpenAI, "Supervised fine-tuning" (distillation section; old `/distillation` path redirects here) — https://developers.openai.com/api/docs/guides/supervised-fine-tuning
- **Evidence:** "Tune a prompt for a larger model… Capture results… then use them to fine-tune a smaller model"; Responses API "stores model responses for 30 days by default."
- **Caveats:** The exact `store=true` capture wording was **not confirmed** on the consolidated page (Unverified) — re-verify before quoting. Requires an eval bar + fine-tuning pipeline → borderline on the one-image constraint.
- **Visual:** Big model → arrow of captured examples → small model at lower $/token.
- **Not a duplicate:** New topic; heavier lift.

---

### C16 — "Get run traces for free" (Agents SDK tracing) · **Score 20/30**
- **Decision:** Use the Agents SDK's built-in tracing + Traces dashboard for agent-run observability.
- **Mechanism:** Every run auto-records LLM calls, tool calls, handoffs, guardrails; exportable to third-party backends.
- **Impact category:** Debuggability, reliability.
- **Sources:** OpenAI, "OpenAI Agents SDK" — https://openai.github.io/openai-agents-python/ ; "Tracing" — https://openai.github.io/openai-agents-python/tracing/
- **Evidence:** "built-in tracing, collecting a comprehensive record of events during an agent run"; "Traces dashboard, you can debug, visualize, and monitor your workflows."
- **Caveats:** SDK/vendor-specific (lock-in); overlaps conceptually with C10's neutral approach. Lower novelty/portability.
- **Visual:** A run timeline with nested spans (agent → tool → handoff).
- **Not a duplicate:** New topic, but weaker than C10 on portability.

**Rejected (kept out of the ranked list, see §self-review):** hosted **OpenAI Evals** (page states it goes **read-only 2026-10-31 and shuts down 2026-11-30** — cannot recommend a sunsetting product); **idempotency keys** (documented only for Workspace Agents / Agentic Commerce / webhook dedup, **not** confirmed on core Chat/Responses endpoints); **token-efficient tool-use header** (legacy — "All Claude 4+ models have built-in token-efficient tool use and these headers have no effect"; 70%/14% were 3.7-Sonnet-only); **1M-context surcharge** (now default & standard-priced — the old 2× >200K premium is stale); **"prompt caching + batch stacking"** (a minor variation of C1/C2, not a distinct idea).

---

# 5. Best next 5

The five strongest to produce now — chosen for documented evidence, one-image fit, and series variety (cost, cost, reliability, portability, cost↔latency).

### 1. Prompt caching — "Put the stable part first" (C1)
- **Why it wins:** Highest composite; hardest documented figure (`0.1×` reads); cross-vendor and durable; trivially one-image; the series has no caching post.
- **Thesis:** Order your prompt so the stable prefix is cached — cached input is billed at ~10% of standard, but only on an exact prefix match.
- **Infographic:** *Headline* "Put the stable part first." *Blocks* (1) cache keys on an exact prefix match; (2) STABLE → cached `0.1×`; (3) VARIABLE tail → full price. *Takeaway:* reads still cost ~10%, writes cost a bit more — a stable prefix pays back on every repeat. *Footer:* Anthropic + OpenAI prompt-caching docs.
- **Show:** The prompt-order diagram with the cache boundary + `0.1× base input` callout.
- **Verify before publishing:** Anthropic `0.1×` read multiplier and the per-model min-token threshold; OpenAI cached-input rate on the live pricing page (it is pricing-derived, not a fixed doc %).

### 2. Batch API — "Not urgent? Halve the bill" (C2)
- **Why it wins:** Flat, documented **50%** on both vendors; unambiguous decision; clean two-lane visual.
- **Thesis:** Send anything that tolerates minutes-to-hours latency through the batch endpoint for half price.
- **Infographic:** *Headline* "Half price for work that can wait." *Blocks:* sync vs batch lane; `−50%`; window (≤24 h). *Takeaway:* interactive stays sync; evals/backfills/embeddings go batch. *Footer:* both batch docs.
- **Show:** Sync-vs-batch lane diagram with the `−50%` badge and the 24-hour window.
- **Verify:** the 50% figure and request/size limits on both live docs.

### 3. Structured outputs — "Stop parsing-and-retrying JSON" (C3)
- **Why it wins:** Reliability variety; documented constrained-decoding guarantee; strong before/after visual.
- **Thesis:** Constrained/strict structured outputs remove the malformed-JSON retry loop from your pipeline.
- **Infographic:** *Headline* "Your JSON either validates or it doesn't ship." *Blocks:* retry-loop (before) vs locked schema (after); the two exceptions (refusal, truncation). *Takeaway:* constrain structure, still validate values. *Footer:* both structured-output docs.
- **Show:** `response_format`/`strict:true` snippet + before/after retry diagram.
- **Verify:** current model-support strings; keep the refusal/truncation carve-out visible; note Anthropic's Citations incompatibility.

### 4. MCP — "One protocol, not N integrations" (C5)
- **Why it wins:** Portability/vendor-risk variety; iconic USB-C visual; documented open-standard framing; highly current.
- **Thesis:** A single open protocol turns an N×M tool-integration matrix into N+M.
- **Infographic:** *Headline* "Stop writing one integration per tool per app." *Blocks:* tangled N×M web vs USB-C hub; primitives (resources/tools/prompts). *Takeaway:* build once, integrate everywhere. *Footer:* modelcontextprotocol.io + Anthropic MCP announcement.
- **Show:** The N×M-tangle → hub diagram.
- **Verify:** spec revision date (`2025-06-18`); only claim adopters the official intro lists; flag the connector's beta header/limits if the connector is shown.

### 5. service_tier — "Pick a speed tier per request" (C4)
- **Why it wins:** Turns the abstract cost/latency trade into one parameter; clean tier matrix; complements C2.
- **Thesis:** Match each workload's latency SLA to its price with one `service_tier` value.
- **Infographic:** *Headline* "Speed is a setting." *Blocks:* Flex (≈batch rates, slower) / Standard / Priority (premium, faster). *Takeaway:* stop paying priority prices for background work. *Footer:* flex + priority docs.
- **Show:** Three-tier ($ vs latency) matrix.
- **Verify:** flex beta status + model availability; do **not** print a priority premium multiplier unless confirmed on the live pricing page.

---

# 6. Recommended next post

**Canonical title:** Inside of the Day #6 — Put the stable part first (prompt caching).

**One-sentence thesis:** Order every prompt so the long, stable prefix comes first — cached input is billed at roughly a tenth of the normal price, but only when the prefix matches exactly.

**Audience problem:** Engineers pay full input price on every call because their prompts put variable content (user input, timestamps, retrieved chunks) near the top, breaking the cache prefix — or they assume caching is automatic and free.

**Mechanism:** Both Anthropic and OpenAI cache on an **exact prefix match**. Put stable content — system instructions, tool definitions, few-shot examples, long documents — first, and the variable turn last. On repeat calls the prefix is served from cache at a large discount.

**Expected impact & evidence status:**
- Anthropic **documents** cache reads at **0.10× base input** (~90% off) with a free-to-refresh 5-minute TTL. *(Documented.)*
- OpenAI **documents** automatic caching for prompts **≥1,024 tokens**, exact-prefix-match only, "place static content at the beginning"; its ~90% discount is **pricing-page-derived**, model-specific. *(Documented mechanism; figure pricing-derived.)*
- Latency improvement ("better time-to-first-token") is **Expected/qualitative** — no vendor number.

**Source list:**
- Anthropic, "Prompt caching" — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- OpenAI, "Prompt caching" — https://developers.openai.com/api/docs/guides/prompt-caching (+ pricing: https://developers.openai.com/api/docs/pricing)

**Exact visual copy draft (English, one infographic):**
> **Eyebrow:** Inside of the Day #6 — Prompt caching
> **Headline:** Put the stable part first.
> **Dek:** Cached input costs about a tenth of normal — but only if the prefix matches exactly.
> **Block A (STABLE → cached):** System · tools · few-shot · documents. Anthropic: cache reads = 0.1× base input. OpenAI: automatic at ≥1,024 tokens.
> **Block B (VARIABLE → full price):** User turn · retrieved chunks · timestamps. Put these last.
> **Rule strip:** Caching keys on an *exact prefix match*. Variable content up front = cache miss = full price.
> **Takeaway:** Reads still cost ~10% and writes cost a bit more — a stable prefix pays back on every repeated call.
> **Footer:** Sources: Anthropic & OpenAI prompt-caching docs · @vitalylobachev

**Caption angle (not a long caption):** A short field note — "the cheapest optimisation I know is prompt *order*" — one paragraph on the exact-prefix rule, one line that cache reads aren't free (~10%), no thread.

**Explicit non-claims / caveats:**
- Cache reads are **not free** (~10% of input) and writes cost slightly more (1.25× at 5-min).
- No latency percentage is claimed (vendors state only "faster time-to-first-token").
- OpenAI's exact discount is pricing-page-derived and model-specific — verify per model at publish.
- Min-token thresholds and cache-write multipliers vary by model; the visual should name the model it cites (e.g. Opus 4.8 / Sonnet 5; GPT-5.5/5.6-era).

---

# 7. Source index

Deduplicated primary sources, all accessed **2026-07-21**.

**Anthropic**
- Prompt caching — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Batch processing — https://platform.claude.com/docs/en/build-with-claude/batch-processing
- Extended thinking — https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- Structured outputs — https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Citations (docs) — https://platform.claude.com/docs/en/build-with-claude/citations
- Context editing (docs) — https://platform.claude.com/docs/en/build-with-claude/context-editing
- Memory tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- MCP connector — https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- Context windows — https://platform.claude.com/docs/en/build-with-claude/context-windows
- Pricing — https://platform.claude.com/docs/en/about-claude/pricing
- "Token-saving updates on the Anthropic API", 2025-03-13 — https://claude.com/blog/token-saving-updates
- "Introducing Citations on the Anthropic API", 2025-06-23 — https://claude.com/blog/introducing-citations-api
- "Managing context on the Claude Developer Platform", 2025-09-29 — https://claude.com/blog/context-management
- "Introducing the Model Context Protocol", 2024-11-25 — https://www.anthropic.com/news/model-context-protocol
- "Claude Sonnet 4 now supports 1M tokens of context", 2025-08-12 — https://claude.com/blog/1m-context
- "Is my data used for model training?", 2026-03-16 — https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training

**OpenAI**
- Prompt caching — https://developers.openai.com/api/docs/guides/prompt-caching
- Pricing — https://developers.openai.com/api/docs/pricing
- Batch API — https://developers.openai.com/api/docs/guides/batch
- Flex processing — https://developers.openai.com/api/docs/guides/flex-processing
- Priority processing — https://developers.openai.com/api/docs/guides/priority-processing
- Predicted Outputs — https://developers.openai.com/api/docs/guides/predicted-outputs
- Reasoning models — https://developers.openai.com/api/docs/guides/reasoning
- Background mode — https://developers.openai.com/api/docs/guides/background
- Structured model outputs — https://developers.openai.com/api/docs/guides/structured-outputs
- Conversation state — https://developers.openai.com/api/docs/guides/conversation-state
- Working with evals — https://developers.openai.com/api/docs/guides/evals
- Graders — https://developers.openai.com/api/docs/guides/graders
- Supervised fine-tuning (distillation) — https://developers.openai.com/api/docs/guides/supervised-fine-tuning
- Data controls — https://developers.openai.com/api/docs/guides/your-data
- Cookbook "GPT-5 New Params and Tools", 2025-08-07 — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools
- Agents SDK — https://openai.github.io/openai-agents-python/ ; Tracing — https://openai.github.io/openai-agents-python/tracing/
- *Unverified (HTTP 403 via fetch):* Enterprise privacy — https://openai.com/enterprise-privacy/

**Cross-vendor / standards**
- Model Context Protocol — https://modelcontextprotocol.io/ ; spec rev 2025-06-18 — https://modelcontextprotocol.io/specification/2025-06-18
- OpenTelemetry GenAI semantic conventions — https://opentelemetry.io/docs/specs/semconv/gen-ai/ ; attribute registry — https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/

---

## Self-review (applied)

- **Removed sunsetting/weak items from the ranked list:** hosted OpenAI Evals (read-only 2026-10-31, shutdown 2026-11-30); idempotency keys (not confirmed on core endpoints); token-efficient-tools header (legacy, no effect on Claude 4+); 1M-context surcharge (stale — now standard-priced). All noted explicitly rather than silently dropped.
- **No duplicates of existing posts:** caching/batch/tiers/structured-outputs/MCP/citations/context-editing are all new mechanisms; the two adjacency risks (C11 memory tool vs Post 5; C13 effort floor vs Post 1) are flagged and deprioritised.
- **No fabricated figures:** every number is quoted from an opened primary page and labelled Documented / Measured (vendor-eval) / Expected. Vendor-internal eval figures (15% recall; 84/29/39% context) are marked as such. Latency figures are labelled Expected.
- **One-image survivability:** every top-5 candidate reduces to problem → one mechanism/matrix → takeaway. Distillation (C15) and Agents-SDK tracing (C16) are the closest to needing a tutorial and are ranked low accordingly.
- **Verify-before-publish flags** are attached to each top-5 item; the single most stale-prone fact across the doc is any pricing multiplier — re-read the live pricing pages at publish time.
