# Research brief - the coordination tax in multi-agent AI systems

Prepared for `posts/12-coordination-tax/`. Research date: 1 August 2026.

Framing under investigation: *"each agent is 90%, but together they hit 50%"* - individual
agent capability is high, collective effectiveness drops because coordination overhead eats
the gain. Working name for the effect: **the coordination tax**.

The central editorial question was whether the "90% / 50%" figures exist in a published
source. **They do not.** They are the author's operator observation. What *is* published, and
verified below, is (a) the theory that predicts this shape, and (b) recent controlled
measurements showing multi-agent systems degrading relative to single-agent baselines on
non-decomposable tasks. The post must present the numbers as illustrative and the mechanism
as evidenced.

---

## 1. Verdict on the "90% / 50%" numbers

| Claim | Status |
|---|---|
| "Each agent is 90% effective alone" | **Illustrative.** No source. Author's observation. |
| "Together they hit 50%" | **Illustrative.** No source. Author's observation. |
| 1 -> 90%, 2 -> 70%, 3 -> 55%, 4 -> 50% curve | **Illustrative.** The *shape* (superlinear overhead, degrading marginal return, negative returns from a strong baseline) is supported; the *values* are not measured. |
| "Coordination overhead is real and grows superlinearly with agent count" | **Verified.** See §3. |
| "More agents is not more throughput on non-decomposable tasks" | **Verified.** See §3. |

**Editorial rule applied:** the visual carries an explicit "illustrative shape, not measured
values" caveat; the caption says the same in plain language; the measured analogue (§3.2) is
cited separately so a reader can check the real numbers.

---

## 2. Established theory (the parallel)

### 2.1 Brooks's Law - primary source, quoted verbatim

Brooks, Frederick P., Jr. *The Mythical Man-Month: Essays on Software Engineering.*
Addison-Wesley, 1975 (anniversary edition 1995). Chapter 2, "The Mythical Man-Month".

Verified verbatim from the book text (page numbers as printed in the chapter):

- p. 17 - non-partitionable work:
  > "When a task cannot be partitioned because of sequential constraints, the application of
  > more effort has no effect on the schedule. The bearing of a child takes nine months, no
  > matter how many women are assigned."

- p. 18 - the two components of communication burden, and the quadratic term:
  > "The added burden of communication is made up of two parts, training and
  > intercommunication. Each worker must be trained in the technology, the goals of the
  > effort, the overall strategy, and the plan of work. This training cannot be partitioned,
  > so this part of the added effort varies linearly with the number of workers.
  > Intercommunication is worse. If each part of the task must be separately coordinated with
  > each other part, the effort increases as n(n-1)/2. Three workers require three times as
  > much pairwise intercommunication as two; four require six times as much as two."

- p. 25 - the law itself:
  > "Oversimplifying outrageously, we state Brooks's Law: Adding manpower to a late software
  > project makes it later."

Two mappings worth making explicit in the post:

- Brooks's **training** term ("cannot be partitioned ... varies linearly") is exactly the
  *re-explaining context* tax: every new agent needs the full briefing, not the delta.
- Brooks's **intercommunication** term (`n(n-1)/2`) is exactly the *reconciling outputs* and
  *conflicting decisions* tax: every pair of agents is a pair that can disagree.

Note on discipline: Brooks himself called the law "oversimplifying outrageously". The post
uses it as a named parallel, not as a proof.

Full-text source used for verification:
https://www.cs.drexel.edu/~yc349/CS451/RequiredReadings/MythicalManMonth.pdf

### 2.2 Steiner's process loss - primary source, bibliographic record verified

Steiner, Ivan D. *Group Process and Productivity.* New York: Academic Press, 1972.
viii, 204 pp. ISBN 0-12-665350-X. (Record verified via Internet Archive:
https://archive.org/details/groupprocessprod0000stei)

The equation, as standardly stated:

> Actual productivity = potential productivity - losses due to faulty group process

Process losses are conventionally split into **coordination losses** (mistimed, duplicated, or
conflicting contributions) and **motivation losses** (reduced individual effort in a group).
For an agent system only the coordination term applies - agents do not social-loaf - which
makes Steiner's decomposition a clean fit: potential productivity is the sum of what each
agent could do alone; the coordination tax is the process-loss term.

**Honesty note:** the bibliographic record is verified from the primary catalogue entry; the
equation wording above is the standard restatement found in reference works
(https://www.oxfordreference.com/display/10.1093/oi/authority.20110803100530786), not a page
quotation from the book itself. Cite the concept and the book; do not present a page quote.

---

## 3. Recent empirical evidence on multi-agent LLM coordination (2025-2026)

### 3.1 Kim et al., "Towards a Science of Scaling Agent Systems" - the strongest source

arXiv:2512.08296. Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall,
A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang,
Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff,
Xin Liu. v1 9 December 2025; v3 8 April 2026. https://arxiv.org/abs/2512.08296

Design: 260 configurations, six agentic benchmarks, five canonical architectures (Single-Agent
plus Independent / Centralized / Decentralized / Hybrid multi-agent), three LLM families.
Tools, prompts and total reasoning-token budget standardized (mean 4,800 tokens per trial) to
isolate architectural effects.

Verified verbatim findings:

- **Range of outcomes, by task structure** (abstract):
  > "Relative performance change compared to single-agent baseline ranges from +80.8% on
  > decomposable financial reasoning to -70.0% on sequential planning, demonstrating that
  > architecture-task alignment determines collaborative success."

- **Sequential tasks degrade universally** (introduction):
  > "all multi-agent variants universally degrade performance on tasks requiring sequential
  > constraint satisfaction (planning: -39% to -70%), where coordination overhead fragments
  > reasoning capacity under fixed computational budgets"
  and, conversely, decentralized coordination helps on parallel search
  ("dynamic web navigation: +9.2%").

- **The baseline paradox** - the closest published analogue to "each agent is already 90%":
  > "tasks where single-agent performance already exceeds 45% accuracy experience negative
  > returns from additional agents, as coordination costs exceed diminishing improvement
  > potential"
  (interaction term `P_SA x log(1+n_a)`, beta = -0.236, p = 0.004)

- **Superlinear communication growth** - the measured analogue of Brooks's `n(n-1)/2`:
  > "T = 2.72 x (n + 0.5)^1.724, R^2 = 0.974, 95% CI on exponent: [1.685, 1.763], p < 0.001"
  > "This super-linear exponent (1.724 > 1) reflects quadratic message complexity
  > (all-to-all potential communication)"

- **Error amplification by topology** (trace-level factor `A_e^trace`, single-agent = 1.0):
  independent 17.2x (95% CI [14.3, 20.1]), decentralized 7.8x, hybrid 5.1x, centralized 4.4x
  (95% CI [3.8, 5.0]).
  > "Independent systems amplify trace-level errors 17.2x through unchecked error
  > propagation, where individual mistakes cascade to the final output. Centralized
  > coordination, however, contains this to 4.4x by enforcing validation bottlenecks that
  > intercept errors before aggregation."

- **The paper uses the term "coordination tax" verbatim**: "tool-heavy workflows suffer from
  coordination tax"; "tool-rich environments amplify the coordination tax, making simpler
  architectures more effective."

- **Limitations, in the authors' words:** agent-count scaling was explored only up to nine;
  > "the communication overhead we measured grows superlinearly with agent count, and
  > coordination efficiency degrades substantially beyond moderate team sizes."

### 3.2 The measured analogue of the "90% -> 50%" curve

Table 5 of the same paper (N = 260, token budget matched across all architectures). Column
order as printed: SAS (single-agent), Independent, Decentralized, Centralized, Hybrid.

| Metric | SAS | Independent | Decentralized | Centralized | Hybrid |
|---|---:|---:|---:|---:|---:|
| Success rate `S` | 0.466 | 0.370 | 0.477 | 0.463 | 0.452 |
| Turns `T` | 7.2 | 11.4 | 26.1 | 27.7 | 44.3 |
| Coordination overhead `O%` | 0 | 58 | 263 | 285 | 515 |
| Coordination efficiency `E_c` | 0.466 | 0.234 | 0.132 | 0.120 | 0.074 |
| Trace error amplification | 1.0 | 17.2 | 7.8 | 4.4 | 5.1 |
| **Success per 1K tokens** | **67.7** | **42.4** | **23.9** | **21.5** | **13.6** |

This is the honest, measured version of the post's illustrative curve. Success rate is
essentially flat across architectures (0.452 - 0.477, with Independent *below* the single-agent
baseline at 0.370) while coordination overhead climbs from 0% to 515%. Normalizing success per
1K tokens to the single-agent baseline: **100% -> 63% -> 35% -> 32% -> 20%.**

In other words, the real measured drop in effectiveness-per-unit-of-work is *steeper* than the
90% -> 50% shape the post draws. The post's curve is conservative. This is worth stating: it
protects the claim rather than inflating it.

### 3.3 Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST)

arXiv:2503.13657. Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra,
Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei
Zaharia, Joseph E. Gonzalez, Ion Stoica. v1 17 March 2025; v3 26 October 2025. Published at
NeurIPS 2025, Datasets and Benchmarks Track. https://arxiv.org/abs/2503.13657

Verified from the abstract:

> "Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular
> benchmarks are often minimal."

MAST: 14 failure modes in 3 categories - **(i) system design issues, (ii) inter-agent
misalignment, (iii) task verification** - derived from 150 expert-annotated traces
(inter-annotator agreement kappa = 0.88), with MAST-Data covering 1,600+ annotated traces
across 7 MAS frameworks.

Relevance: the three MAST categories are the academic partition of the same five sources of
tax the post names. "Inter-agent misalignment" covers conflicting decisions and duplicated
work; "task verification" covers reconciling outputs; "system design" covers context handoff
and dependency ordering.

### 3.4 Anthropic, "How we built our multi-agent research system"

Published 13 June 2025. https://www.anthropic.com/engineering/multi-agent-research-system

This is the strongest *pro*-multi-agent primary source, and it draws the boundary the post
needs. Verified quotes:

- The overhead, stated plainly:
  > "agents typically use about 4x more tokens than chat interactions, and multi-agent systems
  > use about 15x more tokens as chats"

- The win, and its scope:
  > "multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents
  > outperformed single-agent Claude Opus 4 by 90.2%"
  (on an internal research eval; "token usage by itself explains 80% of the variance" in the
  BrowseComp evaluation)

- The boundary condition - the single most useful line for this post:
  > "some domains that require all agents to share the same context or involve many
  > dependencies between agents are not a good fit for multi-agent systems today. For
  > instance, most coding tasks involve fewer truly parallelizable tasks than research"

Editorial note: the 90.2% figure must not be used as a counter-argument-killer or as a
general claim. It is a breadth-first research task - the decomposable end of the spectrum,
exactly where Kim et al. also measure gains (+80.8%). Including it makes the post honest
rather than weaker: the tax is a function of task structure, not a verdict against
multi-agent systems.

### 3.5 Yan, "Don't Build Multi-Agents" (Cognition)

Walden Yan, Cognition, 12 June 2025. https://cognition.com/blog/dont-build-multi-agents

Practitioner primary source. Verified quotes:

- Principle 1: "Share context, and share full agent traces, not just individual messages"
- Principle 2: "Actions carry implicit decisions, and conflicting decisions carry bad results"
- "Subagent 1 and subagent 2 cannot see what the other was doing and so their work ends up
  being inconsistent with each other."
- "The decision-making ends up being too dispersed and context isn't able to be shared
  thoroughly enough between the agents."
- "The subtask agent lacks context from the main agent that would otherwise be needed to do
  anything beyond answering a well-defined question."

Note the near-simultaneous publication with §3.4 (12 vs 13 June 2025) and the opposite
conclusion. The reconciliation is task structure, which is precisely what Kim et al. later
measured.

### 3.6 Counter-evidence and nuance (kept deliberately)

- **Agent count is not the variable; structure is.** *DPBench: Structural Determinants of
  Multi-Agent LLM Coordination Under Simultaneous Resource Contention* (Najmul Hasan,
  Prashanth BusiReddyGari, arXiv:2602.13255, v1 2 February 2026; v2 3 June 2026,
  https://arxiv.org/abs/2602.13255) finds coordination outcomes driven by protocol rather than
  model capability, and in one condition *increasing* the group from N=5 to N=10 reduced
  deadlock from 90.0% to 10.0% for Gemini 2.5 Flash. Abstract: "Whether the same model
  coordinates or deadlocks is determined by the protocol, not by the model's capability."
  This is a genuine caution against reading the post's curve as a law of agent count.

- **Kim et al. also found optima above n=1.** Figure 5: Gemini-2.0 Flash "exhibits a clear
  optimum at 7 agents before degradation"; the paper's own summary is that "architecture-task
  alignment, not number of agents, determines collaborative success."

Both are reflected in the post: the tax is charged on *coupling*, not on headcount, and the
prescription is a decomposability test rather than "use one agent".

---

## 4. Rejected claims - surfaced in search, not verified, not used

| Claim | Where it surfaced | Why rejected |
|---|---|---|
| "All 28 multi-agent configurations degraded relative to single-agent baselines, -4.4% to -35.3%" | Search-result summary / secondary blog posts | Not present in any primary abstract or full text checked. No traceable source. Also conflicts with Kim et al., who measure positive results on decomposable tasks. |
| "Coordination overhead grows superlinearly at O(n^1.4-2.1)" | Same | Not found in the cited papers. The verified superlinear result is Kim et al.'s turn-count exponent 1.724 (CI [1.685, 1.763]) - a different quantity with a different meaning. Use the real one. |
| "Multi-agent LLM systems fail in production at rates between 41% and 87%" | Abstract of *Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems* (Nechepurenko & Shuvalov, arXiv:2605.03310, 5 May 2026) | The sentence is real and correctly attributed, but it is that paper's summary of others' work; the underlying production-failure measurements were not traced to a primary source. Not used in the post or caption. |
| Any specific published "90% individually / 50% together" benchmark | - | Does not exist. Searched; not found. Treated as the author's observation throughout. |

---

## 5. What the post is allowed to claim

**Claim as established:**
1. Brooks's Law and its two mechanisms (non-partitionable training; `n(n-1)/2`
   intercommunication) - cite the 1975 book.
2. Steiner's process-loss framing: actual = potential - process loss - cite the 1972 book.
3. Multi-agent LLM performance relative to a single-agent baseline is a function of task
   structure, spanning +80.8% (decomposable) to -70.0% (sequential) - cite Kim et al.
4. Coordination overhead and communication grow superlinearly with agent count - cite Kim et al.
5. When the single-agent baseline is already strong (>45% on their tasks), additional agents
   produce *negative* returns - cite Kim et al.
6. Tasks with shared context or many inter-agent dependencies are a poor fit for multi-agent
   decomposition - cite Anthropic.
7. Multi-agent gains on popular benchmarks are often minimal, and failures cluster in system
   design, inter-agent misalignment, and verification - cite Cemri et al.

**Claim only as illustrative, labelled on the visual and in the caption:**
- The 90 / 70 / 55 / 50 curve. Shape supported; values are the author's own.

**Do not claim:**
- That multi-agent systems are generally worse. They are worse *on coupled work* and better
  *on genuinely decomposable work*, and both directions are measured.
- Any production failure-rate percentage.
- Any page-level quotation from Steiner.
- The rejected figures in §4.

---

## 6. Source list for the caption

- Brooks, *The Mythical Man-Month* (1975): https://en.wikipedia.org/wiki/The_Mythical_Man-Month
- Steiner, *Group Process and Productivity* (1972): https://archive.org/details/groupprocessprod0000stei
- Kim et al., *Towards a Science of Scaling Agent Systems*: https://arxiv.org/abs/2512.08296
- Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*: https://arxiv.org/abs/2503.13657
- Anthropic, *How we built our multi-agent research system*: https://www.anthropic.com/engineering/multi-agent-research-system
- Yan, *Don't Build Multi-Agents*: https://cognition.com/blog/dont-build-multi-agents
