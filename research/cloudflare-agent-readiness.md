# Cloudflare Agent Readiness - evidence map

## Primary source

- **Cloudflare blog, August 6, 2026:** [From ranking to recommended: get your site ready to thrive in the age of AI agents](https://blog.cloudflare.com/aeo/)

## What Agent Readiness Diagnostics does

Cloudflare says its Diagnostics tool scans a hostname "the way an agent reads it." It checks whether an agent is allowed in, can discover content, can obtain a machine-readable copy, and can find interfaces to call.

Its readiness view ranges from **Not Ready** to fully agent-native. Each check returns **pass, fail, or neutral**, explains why it matters, and includes an evidence trail showing the exact request and response seen by Cloudflare.

## Check groups stated by Cloudflare

1. **Quick wins**
   - crawler-readable `robots.txt`
   - XML sitemap
   - AI-crawler rules
   - clean Markdown for agents
2. **Technical groundwork**
   - Content Signals
   - API catalog
   - link headers
   - agent login instructions
3. **Advanced integration**
   - OAuth discovery
   - MCP
   - A2A agent cards
   - skills index
   - Web Bot Auth
   - WebMCP
4. **Commerce**
   - x402, ACP, UCP, AP2
   - informational at launch; **not included in the readiness score**

Cloudflare also says recommended improvements have a next step. When a Cloudflare setting is applicable, the product links to it; otherwise it offers a **Copy Agent Prompt**. Users can re-scan after a change.

## Article boundary

This post covers **Agent Readiness Diagnostics**, not Cloudflare's separate AEO visibility product. The same announcement describes AEO as a companion feature and offers early-access request flow. We do not state that AEO is generally available or conflate its recommendation metrics with Diagnostics.

## Editorial boundary

A diagnostics pass is not an industry certification, security audit, authorization decision, or promise of compatibility with every agent.

The safe conclusion is limited: an agent may be able to find and inspect the surfaced machine path. It does **not** mean the agent is authorized to take an action.

- Discoverable != authorized.
- Callable != authorized.
- Agent-ready != agent-admin.
- Commerce readiness remains distinct from merchant checkout authorization and policy.

## Distinction from Inside of the Day post 13

Post 13 addressed the merchant implementation path for accepting an agent payment: machine-readable offer -> checkout API -> bounded payment mandate.

This post is earlier in the funnel: can an agent enter, discover, read, and find an explicit action surface at all? Commerce is intentionally shown only as a non-scoring informational category.
