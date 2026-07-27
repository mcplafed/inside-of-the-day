# Research brief — two technical LinkedIn carousels

**Working titles**

- **Carousel A** — *A platform now serves people and agents.*
- **Carousel B** — *Prepare Claude for an incident before the pager goes off.*

**Status:** Research only. No assets, captions, PDFs, schedules, commits, or pushes were produced. Nothing in the existing repository or schedule was altered.

**Claim taxonomy used throughout**

- **Documented** — verified against a primary source (project/vendor/CNCF/Anthropic docs). Safe to state as fact with the link.
- **Example** — a real, public, working reference we point to (repo, cookbook, spec). It demonstrates the pattern; it is not proof of anyone's production outcome.
- **Author framework** — a model or leveling proposed by the source author. Present it as *their* framing, never as an industry/CNCF standard.
- **Representative** — an illustrative file/snippet we author to show the shape of the idea. Not sourced from a real incident, repo, or deployment.

---

## 1. Source-discovery results and confidence

### Carousel A — the platform-serves-agents article

**Identified with HIGH confidence (topic identity).**

- **Title:** *Platform Engineering for AI Agents*
- **Author:** Piotr
- **Publication:** ITNEXT (Medium), 15 March 2026
- **URL:** https://itnext.io/platform-engineering-for-ai-agents-578380c2de47

**Why this is the source:**

| Lead signal | Match |
|---|---|
| Medium / ITNEXT | ✅ ITNEXT |
| Author proposes a maturity model | ✅ Author *extends* the CNCF Platform Engineering Maturity Model with three of their own agent-specific dimensions — **Context management, Memory, Authority** — reusing CNCF's level names (Provisional → Operational → Scalable → Optimizing). This is an **author framework built on top of** the CNCF model, exactly as the brief anticipated. |
| Platform serves people *and* agents | ✅ Central thesis, verbatim: *"the portal and the tool schema are two interfaces to the same provisioning API"* and *"The platform serves its consumers. Now it has two kinds."* |
| Concrete tools | ✅ Names Backstage and MCP tool schemas; conceptual/prescriptive throughout. |

**Honesty caveat on engagement.** The lead reports *54 claps / 2 responses*. I **could not verify** these numbers. Medium's clap/response widget renders client-side and does not appear in fetched page text (fetches returned placeholder low values like "2 claps" for this and other articles, which are unreliable). Treat "54 claps / 2 responses" as the author's own recollection, not a verified figure — and it does not need to appear in the carousel anyway.

**Explicitly ruled out (same search cluster):**
- *"The Best Internal Developer Platform Might Be the One Nobody Opens"* — Artem Lajko, ITNEXT, 9 Jun 2026: **no maturity model** → not the source.
- *"Building an AI Native Developer Platform"* (Santosh Pai) and *"Platform Engineering and Agentic Applications: The Role of Context…"* (Jeremy Cowan): adjacent theme, not fetched to completion (Medium redirect loop); neither is needed given the Piotr match. Listed only as topical neighbours.

### Carousel B — the incident-readiness article

**NOT identified with high confidence. The original Medium article is unconfirmed.**

Six targeted searches (varying the distinctive signal: the exact ordering *memory → skills → hooks → subagents → approval*, "sandbox / simulated data," "before the pager goes off") did **not** surface a single Medium article that clearly owns this workflow. I will not designate any discovered article as "the source."

What the signal *does* trace to cleanly are **Anthropic's own primary materials**, which I use as the verifiable anchors instead:

- **"The site reliability agent"** (Claude Agent SDK cookbook) — a genuinely **sandboxed** example (all-local Docker: PostgreSQL, FastAPI, Prometheus, traffic generator), with scoped edits and bash validation hooks. This is the strongest match to "sandbox with simulated data." https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent
- **"SRE incident responder"** (Claude Managed Agents cookbook) — pager alert → investigate → open PR → **pause for human approval before merge**. Strongest match to the "human approval gate." https://platform.claude.com/cookbook/managed-agents-sre-incident-responder
- **"Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents"** (official Anthropic blog) — owns the exact primitive ordering the lead describes. https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more

**Closest third-party Medium neighbours** (overview pieces on the same primitives, none incident-specific; listed for transparency, not cited as the source): Shashank Mishra, "Claude Code Skills, Subagents, Hooks and Plugins — A Practical Overview"; boredhead, "Context, Skills, Hooks, Subagents: How Claude Code Actually Works"; jsmanifest, "The Claude Code Full Stack."

**Consequence for production:** Carousel B must stand on its own primitives + the official Anthropic cookbooks. Do **not** credit or imply a specific Medium article as its basis.

---

## 2. Carousel A — *A platform now serves people and agents*

### 2.1 Core thesis (to test → confirmed defensible)

A modern internal platform should offer **clear, secure, machine-usable interfaces alongside human portals** — the same backend capability exposed twice: a UI for a person and a typed contract for an agent. The maturity framing is the **author's** (Piotr's) extension of CNCF's model, **not** a CNCF or industry standard.

**Verdict:** defensible and buildable. Every pattern below is a real project a team can adopt today; each has a public working reference.

### 2.2 Evidence map (CNCF status verified July 2026)

| Building block | Claim type | CNCF status (verified) | Primary source |
|---|---|---|---|
| CNCF Platform Engineering Maturity Model | Documented (community standard) | Published by CNCF TAG App Delivery, Nov 2023 | tag-app-delivery.cncf.io |
| Piotr's agent-readiness dimensions (Context/Memory/Authority) | **Author framework** | n/a — not a standard | itnext.io article |
| Backstage (Catalog + Scaffolder) | Documented / Example | **Incubating** | backstage.io |
| Crossplane (Compositions, XRDs/CRDs) | Documented / Example | **Graduated** (28 Oct 2025) | docs.crossplane.io |
| Open Policy Agent (Rego, via Gatekeeper) | Documented / Example | **Graduated** (2021) | openpolicyagent.org |
| Kyverno (K8s-native YAML policy) | Documented / Example | **Graduated** (16 Mar 2026) | kyverno.io |
| SPIFFE/SPIRE (workload identity) | Documented / Example | **Graduated** (2022) | spiffe.io |
| Cloud workload identity (GCP/AWS/Azure) | Documented | vendor | cloud.google.com / docs.aws.amazon.com / learn.microsoft.com |
| OpenAPI (shared API contract) | Documented | Linux Foundation / OAI | openapis.org |
| Model Context Protocol (MCP) | Documented (interface protocol) | open project (Anthropic-originated) | modelcontextprotocol.io |

**Two hard guardrails for this carousel:**
1. **Never** present Piotr's maturity model — or the CNCF one — as proof that *your* platform is mature. Name the CNCF levels correctly (Provisional → Operational → Scalable → Optimizing) if you reference them, and attribute the agent dimensions to the author.
2. **MCP is a tool/context interface protocol, not a maturity solution.** Do not claim "adopt MCP and your platform is agent-ready." MCP is one way to expose the machine path; it does not replace catalog, control plane, policy, or identity.

### 2.3 Concrete implementation patterns (5) — each buildable, each with a public reference

Every pattern follows: **human path · agent path · shared contract · build steps · public example · operational benefit · boundary/risk.**

---

**Pattern 1 — Developer portal + golden-path templates**
*(Backstage Software Catalog + Scaffolder)* — **Example**, CNCF **Incubating**

- **Human path:** developer browses the portal, picks a "Create service" template, fills a form.
- **Agent path:** agent reads the Software Catalog via its REST API to discover ownership/dependencies and which Scaffolder template to invoke, then triggers the same action.
- **Shared contract:** the `catalog-info.yaml` entity descriptor + the Scaffolder template definition — one source of truth for both.
- **Build steps:** stand up Backstage → register components with `catalog-info.yaml` → author a Scaffolder template (form inputs + steps: create repo, register in catalog, wire CI) → expose the catalog API to trusted agents.
- **Public example:** https://backstage.io/docs/features/software-templates/ · catalog: https://backstage.io/docs/features/software-catalog/
- **Operational benefit:** one golden path; humans and agents can't drift onto different provisioning routes.
- **Boundary/risk:** Backstage is a framework, not turnkey — real frontend/plugin engineering to run; catalog is only as good as the metadata discipline behind it.

---

**Pattern 2 — Declarative self-service infrastructure API**
*(Crossplane Compositions + XRDs/CRDs)* — **Example**, CNCF **Graduated**

- **Human path:** developer fills a Backstage form that renders a small custom resource (a claim/XR).
- **Agent path:** agent emits the same custom resource as YAML and `kubectl apply`s it.
- **Shared contract:** the XRD-defined CRD schema — the platform team's typed API. The control plane reconciles identically regardless of author.
- **Build steps:** define an XRD (your platform API) → write a Composition (or Composition Function) mapping it to managed resources → publish the CRD → let both portal and agents create instances.
- **Public example:** https://docs.crossplane.io/latest/composition/compositions/
- **Operational benefit:** infrastructure requests become a reviewable, declarative API instead of ad-hoc scripts or console clicks.
- **Boundary/risk:** authoring compositions and running the control plane is a real learning curve; the control plane holds broad cloud credentials → large blast radius if compromised.

---

**Pattern 3 — Policy & approval boundaries for machine callers**
*(OPA/Gatekeeper or Kyverno + GitOps PR review)* — **Example**, both CNCF **Graduated**

- **Human path:** a person opens a PR / applies a manifest; reviewers and admission control both gate it.
- **Agent path:** agent-submitted changes hit the **identical** admission policy and PR workflow — no privileged side door.
- **Shared contract:** policy-as-code (OPA **Rego** via Gatekeeper, or **Kyverno** Kubernetes-native YAML). "Allowed / denied and why" is enforced uniformly.
- **Build steps:** pick the engine (Rego = maximal expressiveness; Kyverno = no new language, K8s-only) → codify guardrail policies → run as admission controller → route all changes (human and agent) through GitOps PRs so approval is explicit.
- **Public example:** https://kyverno.io/docs/ · https://www.openpolicyagent.org/docs/
- **Operational benefit:** the same deny rule that stops a risky human change stops a risky agent change — this is what makes agent submissions safe to allow.
- **Boundary/risk:** admission control blocks at deploy time, not design time; over-broad deny rules can silently break legitimate automation. Rego has a steeper learning curve; Kyverno is K8s-scoped only.

---

**Pattern 4 — Workload/agent identity + scoped, short-lived credentials**
*(SPIFFE/SPIRE, or cloud workload identity)* — **Example**, SPIFFE/SPIRE CNCF **Graduated**

- **Human path:** person authenticates via SSO/IdP.
- **Agent path:** the agent's workload receives an **attested, short-lived** identity (SPIFFE SVID, or a cloud-federated token) instead of a static API key.
- **Shared contract:** verifiable workload identity → authorization by *who you provably are*, not by a secret that can leak.
- **Build steps:** run SPIRE (or enable GCP Workload Identity Federation / AWS IRSA or EKS Pod Identity / Azure Workload Identity) → attest workloads → issue rotating SVIDs/tokens → authorize platform APIs by identity.
- **Public example:** https://spiffe.io/docs/ · GCP: https://cloud.google.com/iam/docs/workload-identity-federation · AWS IRSA: https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html · Azure: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview
- **Operational benefit:** no long-lived shared secret handed to an autonomous caller; credentials rotate and expire automatically.
- **Boundary/risk:** SPIRE is operationally heavy (server + attestation policies); cloud equivalents are simpler but tie you to one provider's trust domain.

---

**Pattern 5 — A discoverable tool contract for agents**
*(OpenAPI as the contract; MCP as one machine transport)* — **Documented**

- **Human path:** developer reads rendered API docs; human-written clients call the API.
- **Agent path:** an agent reads the same OpenAPI document to construct valid calls, or consumes an MCP server that wraps a platform capability (e.g. the catalog or scaffolder).
- **Shared contract:** one **OpenAPI** document as the single source of truth — the cleanest "no drift between what a person and an agent believe the API accepts." MCP is a standardized *transport* for exposing tools/context to an LLM app.
- **Build steps:** publish an accurate OpenAPI spec per platform API → keep it in sync with the implementation → optionally expose selected capabilities via an MCP server for agent consumption.
- **Public example:** https://www.openapis.org/ · MCP: https://modelcontextprotocol.io/
- **Operational benefit:** agents get a typed, discoverable surface instead of scraping a UI meant for humans.
- **Boundary/risk (must state):** OpenAPI describes surface, not behavior/side-effects; a drifted spec misleads humans and agents alike. **MCP does not "solve" platform maturity** — it is plumbing that complements catalog/control-plane/policy/identity, not a replacement.

### 2.4 Implementation outline (how the five compose)

A person or an agent expresses an **intent** (create service, request environment, deploy, inspect) → through the **portal or the typed API/MCP** (Patterns 1 + 5) → the **declarative infra API** materializes it (Pattern 2) → **policy + GitOps** gate the change identically for both (Pattern 3) → the caller acts under a **scoped, attested identity** (Pattern 4). One backend, two front doors, uniform guardrails.

### 2.5 Six-slide storyboard

Slides show **short readable domains**; the caption/source appendix carries **full URLs**.

1. **Hook —** "Your platform has a new kind of user." Portals were built for people. Agents now clone repos, call your APIs, open PRs. A UI-only platform makes them screen-scrape. *Takeaway: the second consumer is already here.*
2. **The shift —** One capability, two interfaces. Same provisioning backend; a portal for a person, a typed contract for an agent. *(Attribute the framing: author's thesis, ITNEXT.)*
3. **Concrete implementation patterns** *(required slide)* — the five, one line each with a short domain:
   - Portal + templates — backstage.io
   - Self-service infra API — docs.crossplane.io
   - Policy + PR gates — kyverno.io / openpolicyagent.org
   - Workload identity — spiffe.io
   - Discoverable contract — openapis.org (+ modelcontextprotocol.io)
4. **One pattern in depth —** the shared contract. A single `catalog-info.yaml` / OpenAPI doc / XRD read by both the human UI and the agent. No drift.
5. **Guardrails —** the same deny rule and the same PR review gate both paths; agents act under short-lived attested identity, never a static key. *Boundary: MCP is a transport, not maturity.*
6. **Takeaway —** "Design the machine path as a first-class front door — with the same guardrails as the human one." Maturity model = author's framework (built on CNCF's four levels), not a standard.

### 2.6 Caption angle

Lead with the reframe: portals were designed for humans, but agents are now first-class consumers of the platform — and a UI-only platform forces them to scrape. Give the mechanism (one backend, two interfaces, uniform guardrails), name the five buildable patterns with links, and close by attributing the maturity framing to the author while pointing to the real CNCF model. Hashtags in the series register (e.g. `#PlatformEngineering #AIAgents #InternalDeveloperPlatform`). Full URLs live in the caption's source block.

### 2.7 Risks / caveats (Carousel A)

- Do not assert the "54 claps" engagement — unverified.
- Do not call Piotr's Context/Memory/Authority dimensions a standard; they are an author framework.
- Keep CNCF statuses current: Backstage **Incubating**; Crossplane, OPA, Kyverno, SPIFFE/SPIRE **Graduated**. Do not upgrade Backstage.
- No production outcomes, adoption figures, or company case studies — the source has none and neither should we.
- MCP overclaim is the single easiest mistake here; the boundary line on slide 5 is mandatory.

---

## 3. Carousel B — *Prepare Claude for an incident before the pager goes off*

### 3.1 Framing (non-negotiable)

This is an **incident-readiness rehearsal in a sandbox with simulated data**. It is **not** an automated production SRE system, not a case study, and contains **no** invented incident, metric, PR, timeline, or outcome. Every workflow file below is **Representative** unless it links to an official Anthropic example.

**The four distinctions the carousel must hold:**
- **Investigation vs remediation** — the agent gathers evidence freely; changing state is gated.
- **Sandbox/simulated vs production** — everything shown runs on fixtures/local containers.
- **Containing active harm vs changing state** — even "safe" containment is a human decision here.
- **What an agent can gather vs what needs a human** — synthesis is assistive; the call is human.

### 3.2 Evidence map (verified against official Anthropic docs, July 2026)

Canonical docs now live at **code.claude.com/docs** (Claude Code) and **platform.claude.com/docs** (platform/API).

| Primitive | Claim type | What's true (verified) | Primary source |
|---|---|---|---|
| Project memory / CLAUDE.md | Documented | Loaded every session as **context, not enforcement**; files concatenate broadest→specific. To *block*, use a hook. | code.claude.com/docs/en/memory |
| Skills (SKILL.md) | Documented | Folder + `SKILL.md`; loads **on demand**; model-decided invocation via `description`. | code.claude.com/docs/en/skills |
| Hooks (PreToolUse) | Documented | **PreToolUse is the one gate that can block a tool call before it runs** (exit code 2, or JSON `permissionDecision:"deny"`). PostToolUse **cannot** block. | code.claude.com/docs/en/hooks |
| Subagents | Documented | Own context window + restricted tool allow-list; only final summary returns. | code.claude.com/docs/en/sub-agents |
| Permissions / approval | Documented | Modes `default`/`acceptEdits`/`plan`/`bypassPermissions` (+`auto`); `allow`/`ask`/`deny` rules; human gate in `default`/`plan`. | code.claude.com/docs/en/permission-modes |
| Official sandboxed SRE example | Example | All-local Docker sim; scoped edits + validation hooks; human-approval variant. | platform.claude.com/cookbook/... |

**Accuracy landmines flagged by verification (must respect):**
- **CLAUDE.md does not "prevent" anything.** It shapes behavior probabilistically. The docs explicitly say: to block regardless of what Claude decides, use a **PreToolUse hook**. Slide copy must not call CLAUDE.md a guardrail that "prevents."
- **Only PreToolUse blocks.** PostToolUse runs *after* the tool; its error only surfaces after the fact. Do not attribute blocking to PostToolUse.
- **Subagent tool restriction is scoping, not a hard security boundary under `auto` mode** (the parent session's permission rules apply). Describe subagents as context isolation, not a sandbox wall.
- **`bypassPermissions` is not total** (`deny`/`ask` rules and `rm -rf /` circuit-breakers still apply) and "offers no protection against prompt injection" — only ever describe it as isolated-container-only. For a rehearsal, prefer `plan`/`default`, not bypass.

### 3.3 Safe representative rehearsal implementation

All snippets are **Representative** — illustrative shapes, not sourced from a real incident or repo. The real, citable, sandboxed reference is Anthropic's "site reliability agent" cookbook (local Docker: PostgreSQL, FastAPI, Prometheus, traffic generator; edits scoped to `config/`; bash validation hooks).

**(a) `CLAUDE.md` — escalation boundaries (context, not enforcement)**
```markdown
# Incident rehearsal — house rules (SANDBOX, simulated data only)
- This environment is a sandbox with synthetic fixtures. No real customers, no real infra.
- Investigation is unrestricted: read logs, metrics, config, change history.
- You may NOT change state. Proposing a remediation is allowed; applying it is not.
- Any destructive or state-changing command must stop and ask for human approval.
- If root cause is uncertain, present findings + options — do not guess-and-fix.
# Enforcement note: these are guidelines. Hard blocks live in PreToolUse hooks, not here.
```

**(b) A narrow incident-investigation skill** (`.claude/skills/incident-triage/SKILL.md`)
```markdown
---
description: Triage a simulated incident — gather logs, metrics, and recent changes,
  then produce a findings summary with candidate root causes. Investigation only.
---
1. Pull recent error logs and the metric that alerted (delegate to subagents).
2. Diff the last N config/deploy changes.
3. Correlate timeline: change → symptom.
4. Output: symptom, evidence, ranked candidate causes, proposed (NOT applied) fix.
Never edit, deploy, restart, or delete. End with an explicit "Awaiting human approval."
```

**(c) A PreToolUse hook that blocks destructive/state-changing commands** (`.claude/settings.json`)
```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": ".claude/hooks/block-unsafe.sh" }] }
    ]
  }
}
```
```bash
#!/usr/bin/env bash
# block-unsafe.sh — deny state-changing commands during a rehearsal.
# Reads the tool call on stdin; emits a PreToolUse deny decision.
input=$(cat)
cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // ""')
if printf '%s' "$cmd" | grep -Eq '(kubectl (apply|delete|rollout)|helm (up|un)|rm -rf|systemctl|docker (rm|kill)|terraform apply)'; then
  # JSON path (exit 0): richer, explicit deny with a reason surfaced to Claude.
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"State-changing command blocked in rehearsal. Propose it for human approval instead."}}'
  exit 0
fi
exit 0   # no decision → normal flow (investigation proceeds)
```
*Verified mechanics: PreToolUse blocks either via exit code 2, or via `permissionDecision:"deny"` JSON on stdout with exit 0. Only PreToolUse can block before execution.*

**(d) Specialist subagents** (`.claude/agents/*.md`) — context isolation for noisy gathering
```markdown
---
name: log-scout
description: Search and summarize simulated log fixtures. Read-only.
tools: Read, Grep, Glob
model: haiku
---
Find error/warn lines around the incident window; return a compact timeline. Do not edit anything.
```
Companion agents: `metrics-reader` (query the sim metrics endpoint, read-only) and `change-historian` (read git/deploy history, read-only). Each keeps heavy output out of the main context and returns only a summary. *Note: tool restriction is scoping; it is not an independent security boundary under `auto` mode — the hard block is the PreToolUse hook.*

**(e) Human approval gate before remediation**
- Run the rehearsal in `plan` or `default` mode so any edit/command pauses for inline approval.
- Mirror the official pattern: agent investigates → **proposes** a fix as a PR → **pauses for a human to approve before merge** (Managed Agents "SRE incident responder" cookbook).
- The agent's output ends at *"proposed fix + awaiting human approval,"* never at *"applied."*

### 3.4 Six-slide storyboard

**Every slide carries a conspicuous label: `SANDBOX REHEARSAL — NOT PRODUCTION PROOF`.**

1. **Hook —** "The time to prepare Claude for an incident is before the pager goes off." Rehearse the readiness, not the panic. *(Label present.)*
2. **The stack —** five primitives, in order: memory → skill → hooks → subagents → approval. One line each, mapped to a job.
3. **Investigation vs remediation —** the agent gathers evidence freely; changing state is a separate, gated act. This line is the whole point.
4. **The one hard gate —** a **PreToolUse hook** is the only thing that deterministically blocks a command. CLAUDE.md guides; the hook enforces. (Correct the common myth on-slide.)
5. **The human stays in the loop —** subagents summarize logs/metrics/changes; a human approves any remediation. Agent can gather; the decision is human.
6. **Takeaway —** "Rehearse readiness in a sandbox: investigation is automatable, remediation is a human decision." Point to Anthropic's public sandboxed SRE cookbook. *(Label present.)*

### 3.5 Caption angle

Open on the honest frame: this is a **rehearsal in a sandbox with simulated data**, a way to build muscle memory before a real incident — explicitly *not* an autonomous production SRE. Walk the five primitives as jobs (memory sets boundaries, a skill scopes the triage, a **hook** is the only real block, subagents keep the context clean, approval keeps a human in the loop). Land the distinction between investigation (automate it) and remediation (human decides). Link the official Anthropic cookbooks as the real, sandboxed reference. Note the source Medium article is unconfirmed, so make no claim about it. Hashtags e.g. `#IncidentResponse #ClaudeCode #SRE #AIAgents`.

### 3.6 Risks / caveats (Carousel B)

- The `SANDBOX REHEARSAL — NOT PRODUCTION PROOF` label on **every** slide is mandatory.
- Never imply a real incident, metric, issue, PR, timeline, or outcome.
- Do not describe CLAUDE.md, skills, or subagent tool-lists as things that "prevent"/"block" — only the **PreToolUse hook** does, and say so precisely.
- Do not call this "automated production SRE." The agent proposes; a human disposes.
- The original Medium source is **unconfirmed** — do not attribute the workflow to a specific article. Anchor on Anthropic's official docs and cookbooks only.
- Prefer `plan`/`default` modes on-slide; never showcase `bypassPermissions` for a rehearsal.

---

## 4. Recommended sequencing (after the currently scheduled posts)

Current series state (from `strategy/series-plan.md` and `README.md`): #1 model×effort operating point, #2 founder-gated questions, #3 ready-queue stopping condition, #4 review-not-provenance (all **scheduled**), #5 three memory layers (**draft for review**). The repo is also moving away from **public post numbers** (current branch `content/inside-day-5-publish-no-number`), so these carousels should ship **without a public number** in the visual/eyebrow.

Neither carousel duplicates a published topic. Memory confirms "platform engineering serving agents" is already an intended pipeline theme, so Carousel A is a planned continuation, not a new tangent.

**Recommended order:**

1. **Finish and ship #5 (three memory layers) first.** It is the nearest-term draft and thematically primes both carousels (memory as a first-class agent concern).
2. **Carousel A — *A platform now serves people and agents*.** Natural next step: it broadens #5's "agents as first-class consumers" idea from memory to the whole platform. Higher reach potential and less caveat-heavy → good lead carousel.
3. **Carousel B — *Prepare Claude for an incident before the pager goes off*.** Ship after A. It is the most caveat-sensitive (sandbox labelling, source unconfirmed), so it benefits from going out once the carousel format is established. It also pairs well as the "operational safety" bookend to A's "operational capability."

**Rationale:** capability (A) before safety-of-operation (B); both after the memory post that motivates treating agents as real platform users. Reassess cadence per the plan's post-#4 note using actual reach.

---

## 5. Source index (direct public URLs)

**Carousel A — source & framing**
- Piotr, *Platform Engineering for AI Agents*, ITNEXT — https://itnext.io/platform-engineering-for-ai-agents-578380c2de47
- CNCF Platform Engineering Maturity Model — https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
- CNCF maturity model announcement — https://www.cncf.io/blog/2023/11/20/announcing-the-platform-engineering-maturity-model/

**Carousel A — implementation references**
- Backstage Software Catalog — https://backstage.io/docs/features/software-catalog/
- Backstage Software Templates / Scaffolder — https://backstage.io/docs/features/software-templates/
- Backstage CNCF status (Incubating) — https://www.cncf.io/projects/backstage/
- Crossplane Compositions — https://docs.crossplane.io/latest/composition/compositions/
- Crossplane graduation (Oct 2025) — https://www.cncf.io/announcements/2025/11/06/cloud-native-computing-foundation-announces-graduation-of-crossplane/
- Open Policy Agent docs — https://www.openpolicyagent.org/docs/
- OPA CNCF status (Graduated) — https://www.cncf.io/projects/open-policy-agent-opa/
- Kyverno docs — https://kyverno.io/docs/
- Kyverno graduation (Mar 2026) — https://www.cncf.io/announcements/2026/03/24/cloud-native-computing-foundation-announces-kyvernos-graduation/
- SPIFFE/SPIRE docs — https://spiffe.io/docs/
- SPIFFE CNCF status (Graduated) — https://www.cncf.io/projects/spiffe/
- GCP Workload Identity Federation — https://cloud.google.com/iam/docs/workload-identity-federation
- AWS IAM Roles for Service Accounts (IRSA) — https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html
- AWS EKS Pod Identity — https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html
- Azure Workload Identity — https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview
- OpenAPI Initiative — https://www.openapis.org/  · Spec — https://spec.openapis.org/oas/latest.html
- Model Context Protocol — https://modelcontextprotocol.io/  · GitHub — https://github.com/modelcontextprotocol

**Carousel B — primary anchors (source Medium article unconfirmed)**
- Steering Claude Code (CLAUDE.md/skills/hooks/subagents) — https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- Claude Code memory / CLAUDE.md — https://code.claude.com/docs/en/memory
- Claude Code skills — https://code.claude.com/docs/en/skills
- Claude Code hooks — https://code.claude.com/docs/en/hooks  · guide — https://code.claude.com/docs/en/hooks-guide
- Claude Code subagents — https://code.claude.com/docs/en/sub-agents
- Claude Code permission modes — https://code.claude.com/docs/en/permission-modes  · rules — https://code.claude.com/docs/en/permissions
- Cookbook: The site reliability agent (sandboxed) — https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent
- Cookbook source dir — https://github.com/anthropics/claude-cookbooks/tree/main/claude_agent_sdk/site_reliability_agent
- Cookbook: SRE incident responder (human approval gate) — https://platform.claude.com/cookbook/managed-agents-sre-incident-responder

---

## 6. Final fact-check checklist (before production)

**Both carousels**
- [ ] Every empirical claim maps to a Documented / Example / Author-framework / Representative label — nothing unlabelled asserted as fact.
- [ ] No public post number in the eyebrow/visual (series is dropping numbers).
- [ ] Footer credit `@vitalylobachev`; English throughout; series visual register.
- [ ] Full URLs in caption/source block; short readable domains on slides.
- [ ] No fabricated outcomes, adoption figures, company names, or metrics.

**Carousel A**
- [ ] Piotr's maturity dimensions labelled **author framework**, never a standard.
- [ ] CNCF levels named correctly if used: Provisional → Operational → Scalable → Optimizing.
- [ ] CNCF statuses current: Backstage **Incubating**; Crossplane/OPA/Kyverno/SPIFFE/SPIRE **Graduated**.
- [ ] MCP boundary line present: interface protocol, **not** a maturity solution.
- [ ] "54 claps / 2 responses" **not** stated (unverified).
- [ ] The `Concrete implementation patterns` slide is present with visible short-domain links.

**Carousel B**
- [ ] `SANDBOX REHEARSAL — NOT PRODUCTION PROOF` label on **every** slide.
- [ ] Only **PreToolUse hook** described as blocking; CLAUDE.md/skills/subagents described as guidance/scoping, not enforcement.
- [ ] Investigation vs remediation clearly separated; remediation is human-approved.
- [ ] Not described as "automated production SRE."
- [ ] Source Medium article stated as **unconfirmed**; anchored on Anthropic docs/cookbooks.
- [ ] No invented incident, metric, PR, issue, timeline, or outcome; workflow files labelled **Representative**.
- [ ] `bypassPermissions` not showcased for a rehearsal.
