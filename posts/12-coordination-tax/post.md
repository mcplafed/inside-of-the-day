# Each agent is 90%. Together they hit 50%.

**Subhead:** I kept adding agents to my workflow. The total kept getting worse.

## Format

Single-image portrait infographic for LinkedIn (4:5). Not a carousel. One chart as the visual
centerpiece - effectiveness per agent against agent count, with the gap to the expected flat
90% shaded as the coordination tax - then five named sources of the tax, then the takeaway.

Broad-reach topic: a reader who has tried running two or three assistants on one job should
recognise the problem from the headline alone. No API, framework, or vendor knowledge required.

## Core insight

When you run one AI agent, it handles its task well. Add a second, a third, a fourth - and you
do not get 4x the output. You get coordination overhead: duplicated work, conflicting
decisions, context that has to be re-explained, results that have to be reconciled. The agents
spend more effort coordinating than working.

This is the same pattern Fred Brooks named in 1975 for human teams: adding manpower to a late
software project makes it later. Communication effort grows with the square of the team size.
It applies to agents too.

## Mechanism

### The shape

```
1 agent  -> 90% effective
2 agents -> 70%
3 agents -> 55%
4 agents -> 50%     <- the coordination tax eats the gain
```

**These four numbers are illustrative, not measured.** They are my own observation of my own
workflow, drawn to show a shape. The shape is the point. See "Evidence map" below for what is
established and what is not, and for the measured analogue - which is steeper than this curve,
not gentler.

### Where the tax comes from

1. **Re-explaining context** - every agent needs the full briefing, not just the delta.
2. **Reconciling outputs** - two agents produce two different answers; a human or a third agent
   has to merge them.
3. **Conflicting decisions** - agent A deploys, agent B reverts; agent A writes the test, agent
   B changes what it tests.
4. **Duplicated work** - neither agent knew the other had already done it.
5. **Waiting on dependencies** - agent B cannot start until agent A finishes, and A is waiting
   on C.

Items 1 and 5 are Brooks's non-partitionable work. Items 2, 3 and 4 are his `n(n-1)/2`
intercommunication term: every pair of agents is a pair that can disagree.

## What I changed

- I stopped adding agents to parallelize work that is not actually independent.
- I started asking one question first: is this task decomposable, or am I just adding
  communication overhead?
- I kept one agent on the full chain when the steps depend on each other.
- I split only when the subtasks are truly independent **and** I have a merge strategy.

## Takeaway

The coordination tax is real. More agents is not more throughput - it's more overhead.
Decompose only when the subtasks are truly independent.

## Evidence map

Full working: `research/coordination-tax-research.md`.

### Established - safe to state as fact

| Claim | Source |
|---|---|
| "Adding manpower to a late software project makes it later." | Brooks, *The Mythical Man-Month* (1975), ch. 2, p. 25 - verbatim |
| Communication burden = training (linear, non-partitionable) + intercommunication, where "the effort increases as n(n-1)/2" | Brooks (1975), ch. 2, p. 18 - verbatim |
| "The bearing of a child takes nine months, no matter how many women are assigned." | Brooks (1975), ch. 2, p. 17 - verbatim |
| Actual productivity = potential productivity - process losses (coordination + motivation) | Steiner, *Group Process and Productivity* (1972). For agents only the coordination term applies. |
| Multi-agent vs single-agent performance ranges from **+80.8%** on decomposable financial reasoning to **-70.0%** on sequential planning; every multi-agent variant degraded sequential constraint-satisfaction tasks (-39% to -70%) | Kim et al., arXiv:2512.08296 - 260 configurations, 6 benchmarks, 5 architectures, 3 model families, token budget matched |
| Coordination overhead grows superlinearly with agent count: turn count fits `T = 2.72 x (n+0.5)^1.724` (R^2 = 0.974, exponent CI [1.685, 1.763]), reflecting "quadratic message complexity" | Kim et al., arXiv:2512.08296 |
| When the single-agent baseline is already strong (>45% accuracy on their tasks), adding agents produces **negative** returns, "as coordination costs exceed diminishing improvement potential" | Kim et al., arXiv:2512.08296 (beta = -0.236, p = 0.004) |
| "Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal." 14 failure modes in 3 categories: system design, inter-agent misalignment, task verification | Cemri et al., arXiv:2503.13657 (NeurIPS 2025 D&B) |
| "some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today" | Anthropic, *How we built our multi-agent research system* (13 Jun 2025) - verbatim |
| Multi-agent systems use "about 15x more tokens as chats" | Anthropic (13 Jun 2025) - verbatim |
| Subagents "cannot see what the other was doing and so their work ends up being inconsistent with each other" | Yan, *Don't Build Multi-Agents*, Cognition (12 Jun 2025) - verbatim |

The term **"coordination tax" is not invented here** - Kim et al. use it verbatim
("tool-heavy workflows suffer from coordination tax").

### Illustrative - must be labelled as such

- **90% / 70% / 55% / 50%.** My observation, not a benchmark. No published study states these
  numbers, and none was found after searching for one. The visual carries the caveat inline;
  the caption says it in plain language.

The measured analogue, for anyone who wants real numbers. Kim et al., Table 5, success per
1,000 tokens with token budget held constant across architectures: single-agent **67.7**,
independent **42.4**, decentralized **23.9**, centralized **21.5**, hybrid **13.6** - that is
100% -> 63% -> 35% -> 32% -> 20%. Meanwhile raw success rate barely moves (0.452-0.477, with
independent multi-agent *below* the single-agent baseline at 0.370) while coordination
overhead climbs from 0% to 515%. **The real curve is steeper than the one drawn.** The post's
illustration is conservative.

### Rejected - surfaced in search, deliberately not used

- "28 configurations, -4.4% to -35.3% degradation" - no traceable primary source.
- "Coordination overhead grows at O(n^1.4-2.1)" - not in any cited paper. The verified
  superlinear figure is Kim et al.'s exponent 1.724, which measures turn count, not overhead.
- "Multi-agent systems fail in production at 41-87%" - real sentence in a real abstract
  (arXiv:2605.03310), but it is that paper's summary of others' work and the underlying
  measurement was not traced. Not used.

## Boundaries and claim discipline

- **The 90/50 numbers are mine, not a study's.** Stated on the visual and in the caption. Do
  not let an edit turn them into a cited statistic.
- **This is not "multi-agent systems are bad".** The same body of evidence shows large gains on
  genuinely decomposable work: +80.8% (Kim et al.) and Anthropic's +90.2% on a breadth-first
  research eval. The tax is charged on *coupling*, not on headcount.
- **Agent count is not the governing variable; task structure is.** DPBench
  (arXiv:2602.13255) found one condition where going from 5 to 10 agents *reduced* deadlock
  from 90% to 10%, and concluded coordination outcomes are "determined by the protocol, not by
  the model's capability". Kim et al. likewise found an optimum at 7 agents for one model. The
  post therefore prescribes a decomposability test, not "use one agent".
- **Brooks called his own law "oversimplifying outrageously".** It is used as a named parallel,
  not as proof.
- **No page-level quotation from Steiner.** The bibliographic record is verified; the equation
  is cited as the standard restatement of the concept.
- **No vendor-news framing, no fabricated studies, no invented metrics.**
- **No public post number** in the eyebrow or visual (series is dropping public numbers).

## Sources

- Fred Brooks, *The Mythical Man-Month: Essays on Software Engineering*, Addison-Wesley, 1975: https://en.wikipedia.org/wiki/The_Mythical_Man-Month
- Ivan D. Steiner, *Group Process and Productivity*, Academic Press, 1972: https://archive.org/details/groupprocessprod0000stei
- Kim et al., *Towards a Science of Scaling Agent Systems*, arXiv:2512.08296: https://arxiv.org/abs/2512.08296
- Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, arXiv:2503.13657 (NeurIPS 2025): https://arxiv.org/abs/2503.13657
- Anthropic, *How we built our multi-agent research system*: https://www.anthropic.com/engineering/multi-agent-research-system
- Walden Yan, *Don't Build Multi-Agents*, Cognition: https://cognition.com/blog/dont-build-multi-agents
- Hasan & BusiReddyGari, *DPBench*, arXiv:2602.13255: https://arxiv.org/abs/2602.13255
- Research brief: `research/coordination-tax-research.md`

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 px mobile-feed legibility probe (downscaled from the full render).
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies; inline SVG chart).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3) that also emits the mobile probe.
