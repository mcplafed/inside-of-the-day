# CLAUDE CODE JUST ADDED SELF-HOSTED RUNNERS.

**Hook (very large, directly below the headline):** WHAT DOES THAT UNLOCK FOR YOUR TEAM?

**Eligibility badge (first-glance element, never a footnote):**
PUBLIC BETA · TEAM & ENTERPRISE ONLY · ADMIN ENABLED — plus a secondary badge
LINUX / MACOS RUNNER HOSTS.

## Format

Single-image portrait infographic for LinkedIn (4:5). Not a carousel, not a terminal
screenshot. One news-first poster: the announcement headline, a very large "what does that
unlock for your team?" hook, a prominent eligibility badge row, a dominant mechanism flow,
exactly three concrete outcome cards (three short label-free rows each: mechanism /
use case / boundary), a legible secrets strip, the takeaway and the caveat.

Grounded in a same-day primary source: **Claude Code v2.1.224, released 2026-08-07**.

## Editorial thesis

News first, not architecture first. The reader must get three things on the first glance:
Claude Code just shipped self-hosted runners; what the feature means (start a session
anywhere, execute it on your own infrastructure beside the work); and who it is for
(an enterprise/corporate capability — public beta, Team & Enterprise, admin enabled — not a
personal local-Claude upgrade).

The earlier abstract framing ("your infrastructure is now the Claude runtime") was dropped:
it buried the announcement and read as architecture philosophy instead of shipped news.

## Hero mechanism (visually dominant)

One concise line above the flow, verbatim:
*Start a session from web, mobile or desktop. Execute it on your own VM or container beside
the work.*

```
WEB / MOBILE / DESKTOP
          |
          v
YOUR SELF-HOSTED RUNNER
inside your network · your VM / container · Linux or macOS host
          |
          v
REPO · CI · INTERNAL TOOLS · POLICIES
```

Boundary note directly beneath the flow, verbatim:
*Execution stays in your network. Inference and session transcripts still go to Anthropic.*

Never "everything stays local": checkouts, artifacts, secrets and session files stay on
your machines; prompts, responses, tool results and the transcript go to
`api.anthropic.com` (primary-sourced, see taxonomy below).

## The three outcome cards

Concrete outcomes, not abstract architecture categories. Each card: a title plus exactly
three short, label-free full-width rows — mechanism, use case, boundary — set at 20px
logical body type (mobile-legibility correction: the earlier `HOW / USE CASE / BOUNDARY`
label column with 16.6px body copy needed zoom at feed size and was removed). The boundary
row is the only emphasized row (bold, terra color, hairline separator).

### A — START FROM ANYWHERE. EXECUTE WHERE THE WORK LIVES.

Row 1: Web / mobile / desktop session → runner beside repo + CI.

Row 2: Review a PR on web. Run the actual build and tests in the team environment.

Row 3 (boundary): You own the runner image, network egress and credentials. (Docs: "you
build and maintain the runner image, operate the fleet, and control its network"; the
quickstart routes through the security-posture page before real repositories are
connected.)

### B — USE INTERNAL CONTEXT WITHOUT MOVING THE EXECUTION ENVIRONMENT.

Row 1: Runner operates beside approved checkout, CI artifacts and internal tools.

Row 2: Investigate a failed build or update a service in place.

Row 3 (boundary): Execution stays in your network. Prompts, tool results and transcripts
still reach api.anthropic.com. (Docs verbatim: "a self-hosted environment moves session
execution into your network, not the control plane.")

### C — HAND OFF WORK BETWEEN SESSIONS — EXPLICITLY.

Card carries a small label: **SAME RELEASE · COMPANION CAPABILITY** — cross-session
messaging shipped in the same v2.1.224 release (macOS and Linux per the release note), but
no primary source documents a combined "self-hosted runner + cross-session messaging"
workflow, so the card is worded as a companion capability, never as a guaranteed end-to-end
product workflow.

Row 1: `ListAgents` finds sessions. `SendMessage` transfers task, evidence, decision and
next safe action. (The macOS-and-Linux qualifier moved to the caption, which states it
verbatim; the visual row stays short for feed legibility.)

Row 2: One session investigates. The next gets an evidence-backed handoff, not a copied
chat summary.

Row 3 (boundary): Messaging is transport — not shared memory, not a turnkey multi-agent
orchestrator.

## Secrets strip (legible, above the takeaway — not footer microtype)

**On the visual, verbatim:** "Secrets are not automatically safe. Masking needs explicit
configuration and TLS termination."

## Takeaway

**On the visual, verbatim:** SELF-HOSTED RUNNERS TURN CLAUDE CODE FROM A SESSION INTO A
TEAM EXECUTION PLANE.

## Caveat

**On the visual, verbatim:** "Not a turnkey orchestrator. You still design concurrency,
durable state and permissions."

## Fact / boundary taxonomy

### Established - safe to state as fact (all primary-sourced, fetched 2026-08-07)

| Claim | Source |
|---|---|
| `claude self-hosted-runner` "turns your own machines or containers into a place Claude Code web, mobile, and desktop sessions can run, on Team and Enterprise plans" | Release v2.1.224, verbatim |
| Self-hosted environments are "in public beta on Team and Enterprise plans and are off by default"; an Owner/admin must enable them in claude.ai admin settings ("admin enabled" on the badge) | code.claude.com/docs/en/self-hosted-environments, verbatim |
| Runner host is Linux or macOS (container counts); "Windows isn't supported as a runner host" | Quickstart, verbatim |
| "Repository checkouts, build artifacts, secrets, and any files a session creates or modifies stay on the machines you provision. The conversation itself ... goes to `api.anthropic.com` for model inference", and the transcript is stored by Anthropic | Self-hosted overview, verbatim |
| "a self-hosted environment moves session execution into your network, not the control plane" | Self-hosted overview, verbatim |
| Every connection is outbound; "Anthropic never connects into your network" | Self-hosted overview, verbatim |
| Cross-session `SendMessage` + `ListAgents`, "on any of your machines ... (macOS and Linux)" | Release v2.1.224, verbatim |
| A receiving session is told a message "came from another Claude session, not from you"; an agent cannot approve permissions on your behalf | Agent-teams docs, verbatim |
| Masking needs `network.tlsTerminate`; honored only from user, managed, or `--settings` settings | Release + sandboxing docs, verbatim |
| "There is no built-in credential deny list, so only the files and variables you list are restricted" | Sandboxing docs, verbatim |

### Documented uncertainty - kept OUT of public copy

- Cross-session messaging into a self-hosted-environment session specifically: no source
  combines the two. Card C is explicitly labeled a companion capability from the same
  release; neither visual nor caption claims a documented combined workflow.
- The cross-machine discovery/transport mechanism for `ListAgents`/`SendMessage` is not
  documented; public copy states the capability, never the mechanism.
- `dialogExpiry` mechanics: named in the release; absent from the settings reference as of
  2026-08-07. Not on the visual or in the caption.
- Whether cross-session messaging requires the experimental agent-teams flag: not stated in
  any primary source; no enablement claim is made.

## Boundaries and claim discipline

- **Never "all data stays local."** The flow's boundary note states the split verbatim:
  execution stays in your network; inference and session transcripts still go to Anthropic.
- **Eligibility is a first-glance element**, not a footer disclaimer: public beta, Team &
  Enterprise only, admin enabled, Linux/macOS runner hosts — badge row directly under the
  headline block.
- **Enterprise capability framing throughout** — never a personal local-Claude upgrade.
- **Cross-session messaging is not persistent memory** and not an orchestrator; card C
  boundary and caption say so, and the combined-workflow claim is explicitly avoided.
- **No automatic credential safety.** Dedicated legible strip on the visual, verbatim:
  "Secrets are not automatically safe. Masking needs explicit configuration and TLS
  termination." Repeated in the caption.
- **No invented throughput, security, adoption or cost claims.** None appear anywhere.
- **No fictional case studies. No secondary blogs as fact sources.**
- **No public post number** in the eyebrow or visual (series is dropping public numbers).

## Sources

Full working: `research/self-hosted-claude-sessions.md`.

Primary references named in the caption:

- Claude Code v2.1.224 release: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
- Self-hosted environments: https://code.claude.com/docs/en/self-hosted-environments
- Sandboxing / credential masking: https://code.claude.com/docs/en/sandboxing

Additional primary sources behind the details:

- Changelog (identical 2.1.224 entry): https://code.claude.com/docs/en/changelog
- Self-hosted environments quickstart: https://code.claude.com/docs/en/self-hosted-environments-quickstart
- Agent teams / SendMessage semantics: https://code.claude.com/docs/en/agent-teams
- Settings reference (checked; `crossSessionInbound`/`dialogExpiry` not yet documented): https://code.claude.com/docs/en/settings

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 px mobile-feed legibility probe (downscaled
  from the full render).
- `source/infographic.html`: editable, self-contained visual source (no external assets or
  network dependencies; CSS-only flow and arrows).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device
  scale factor 3) that emits the mobile probe and reports panel overflow plus the rendered
  line count of the headline/hook, badges, flow chips, card titles, card body rows (max 2
  lines each), boundary note and secrets strip.
