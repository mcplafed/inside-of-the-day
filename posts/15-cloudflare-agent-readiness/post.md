# Check if your site is AI-agent ready

## Editorial premise

Cloudflare shipped **Agent Readiness Diagnostics** on August 6, 2026. It answers an operational question that traditional browser-first QA misses: can an agent enter, discover, read and inspect an explicit action surface on a hostname?

The post is intentionally not a Cloudflare sales pitch and not a repeat of post 13's payment-readiness blueprint. This is the preceding diagnostic layer.

## Public visual copy

**Headline**

> CHECK IF YOUR SITE IS AI-AGENT READY.
>
> CLOUDFLARE JUST SHIPPED A DIAGNOSTIC FOR THAT.

**Scope badge**

> SHIPPED AUG 6 · HOSTNAME DIAGNOSTICS · PASS / FAIL / NEUTRAL + EVIDENCE

**Hero**

> It scans your hostname the way an agent reads it — then shows what is missing.

## Four diagnostic gates

| Gate | Cloudflare examples | Careful conclusion |
|---|---|---|
| Can it enter? | crawler-readable robots.txt, AI-crawler rules | Agent can evaluate access terms. |
| Can it find + read? | XML sitemap, clean Markdown, Content Signals | Agent can discover and parse content. |
| Can it call the right surface? | API catalog, link headers, login instructions | Agent can locate an explicit machine path. |
| Is the site agent-native yet? | OAuth discovery, MCP, A2A cards, skills index, Web Bot Auth, WebMCP | Richer agent-facing surfaces are visible for inspection. |

## Required boundaries

- The output is Cloudflare's product diagnostic, not an industry certification.
- Pass/fail/neutral does not establish authorization, safety or universal compatibility.
- **Discoverable != authorized.**
- Commerce references (x402, ACP, UCP, AP2) are informational at launch and not counted in the readiness score.
- AEO visibility is a separate companion product and not part of this post's capability claim.

## Source

- https://blog.cloudflare.com/aeo/

## Assets

- `source/infographic.html`: self-contained editable poster.
- `source/render.py`: deterministic Chromium/Playwright renderer with layout checks.
- `assets/infographic.png`: 3240x4050 publication asset.
- `assets/infographic-mobile-probe.png`: 400x500 feed legibility probe.
