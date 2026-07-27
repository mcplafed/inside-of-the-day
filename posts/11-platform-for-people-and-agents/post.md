# Your platform has two users now: people and agents.

## Format

Single-image portrait infographic for LinkedIn (4:5). Not a carousel. One architecture map: two front doors into one platform contract and control plane, then five buildable implementation layers, guardrails, and a takeaway.

## Core insight

An internal platform now serves two kinds of consumers: people and agents. A portal is a front door built for a human (UI, form, PR). Agents already clone repos, call APIs, and open PRs, so a UI-only platform forces them to screen-scrape or run on a static admin key. The reframe: stop treating the platform as a portal and treat it as a set of safe, discoverable contracts. One control plane, two front doors, the same guardrails behind both.

## Mechanism

A person or an agent expresses the same intent through the portal or a typed contract, both routed through one infrastructure API, one set of policy gates, one approval flow, and one scoped identity. Five layers, each with a human path, an agent path, and a single shared contract:

1. **Discover** — Human browses the catalog and picks a template; agent reads the same catalog and invokes the same template. Shared contract: catalog entry + template. Benefit: one golden path. Example: Backstage Catalog / Scaffolder.
2. **Request infra** — Human fills a platform form; agent emits the same YAML. Shared contract: CRD / XRD schema. Benefit: declarative self-service. Example: Crossplane Composition.
3. **Gate change** — Human opens a PR / applies; agent goes through the same PR and the same admission policy. Shared contract: policy-as-code + GitOps. Benefit: no privileged side door. Example: Kyverno / OPA.
4. **Prove identity** — Human authenticates via SSO; agent gets a short-lived, attested workload identity. Shared contract: identity drives authorization. Benefit: no shared admin key. Example: SPIFFE/SPIRE or cloud workload identity.
5. **Discover tools** — Human reads API docs; agent reads the same typed contract and calls it. Shared contract: OpenAPI. Benefit: no UI scraping. Example: OpenAPI; MCP only as a transport.

## Guardrail

Agent-ready is not agent-admin. Making the machine path first-class does not grant more power: same policy, scoped identity, approval for irreversible change. The guardrail callout sits near layers 3–5 on the visual.

## Takeaway

Design the machine path as a first-class front door — with the same guardrails as the human one.

## Boundaries and claim discipline

- **Author framework, not a standard.** Piotr's agent-readiness dimensions (Context / Memory / Authority) are his extension of the CNCF Platform Engineering Maturity Model, not a CNCF or industry standard. The visual and caption attribute the framing to him and label it as an implementation framework "inspired by" his article.
- **MCP is an interface transport, not a maturity solution.** Stated on the visual and in the caption.
- **OpenAPI describes the interface surface, not every side effect.** Stated on the visual and in the caption.
- **No fabricated evidence.** No adoption metrics, customer names, engagement counts (the "54 claps" figure from the lead is unverified and deliberately omitted), or production outcomes. Every building block is a real, public project.
- **CNCF status (verified July 2026, from the research brief):** Backstage Incubating; Crossplane, OPA, Kyverno, SPIFFE/SPIRE Graduated. Status labels are intentionally not shown on the visual to keep type large and readable; they are recorded here for accuracy.
- **No public post number** in the eyebrow or visual (series is dropping public numbers).

## Sources

- Piotr, Platform Engineering for AI Agents (ITNEXT): https://itnext.io/platform-engineering-for-ai-agents-578380c2de47
- CNCF Platform Engineering Maturity Model: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
- Backstage Software Catalog: https://backstage.io/docs/features/software-catalog/
- Backstage Software Templates (Scaffolder): https://backstage.io/docs/features/software-templates/
- Crossplane Compositions: https://docs.crossplane.io/latest/composition/compositions/
- Kyverno: https://kyverno.io/docs/
- Open Policy Agent: https://www.openpolicyagent.org/docs/
- SPIFFE/SPIRE: https://spiffe.io/docs/
- OpenAPI Initiative: https://www.openapis.org/
- Model Context Protocol: https://modelcontextprotocol.io/
- Research brief: `research/agent-first-platform-and-incident-readiness-carousel-briefs.md`

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 px mobile-feed legibility probe (downscaled from the full render).
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies; inline SVG connector).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3) that also emits the mobile probe.
