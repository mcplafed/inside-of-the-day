# Self-hosted Claude sessions - evidence map

Research brief for the post *Your infrastructure is now the Claude runtime.*

**Framing under test:** not "Claude Code shipped a release" and not "agents now share memory".
The claim is narrower: a Claude session can end without the work environment forgetting,
because the execution plane can stay on your own infrastructure beside the repository, CI,
tools and policies - and sessions can exchange an explicit handoff. Memory, state and
permissions still have to be designed deliberately.

Verified against primary, publicly accessible documentation on 7 August 2026, the day of the
release. Anything not traced to a primary source is listed under **Excluded / uncertain** and
does not appear in public copy.

---

## 0. The primary source

**Claude Code v2.1.224**, released 2026-08-07 by @ashwin-ant, commit `66edf53`:
https://github.com/anthropics/claude-code/releases/tag/v2.1.224

The official changelog page (https://code.claude.com/docs/en/changelog) carries the identical
entry labeled "2.1.224 - August 7, 2026". Both were read in full; the four load-bearing bullets
are quoted verbatim below.

1. **Self-hosted environments.** "Added self-hosted environments: `claude self-hosted-runner`
   turns your own machines or containers into a place Claude Code web, mobile, and desktop
   sessions can run, on Team and Enterprise plans"
2. **Cross-session messaging.** "Added cross-session `SendMessage`: Claude Code sessions can
   now message each other, on any of your machines, with `ListAgents` to discover them
   (macOS and Linux)"
3. **Inbound gating.** "Added `crossSessionInbound` and `dialogExpiry` settings: cross-session
   messages sent to a session running with bypassed permissions are held for your approval,
   and messages to other sessions auto-deliver"
4. **Credential masking extensions.** "Added sandbox credential-masking options: `extract` and
   `onExtractNoMatch` for structured env values, `decode: \"jwt\"` with `maskClaims` for
   JWT-aware masking, and `awsPairs`/`sigv4` for AWS SigV4 re-signing; these need
   `network.tlsTerminate` and are honored only from user, managed, or `--settings` settings"

Supporting bullets from the same release, used only as context:

- "Fixed `SendMessage` reporting 'Message sent' when the write to a teammate's inbox had
  actually failed; failed deliveries are now reported as errors" - messaging is inbox-based
  and delivery can fail; a reason to treat it as transport, not as a guarantee.
- "Removed the 200-subagent-per-session spawn cap ... (concurrency and depth limits still
  apply)" - limits remain even as caps loosen.

---

## 1. Self-hosted environments: what is established

Primary docs, all read in full on 2026-08-07:

- Overview: https://code.claude.com/docs/en/self-hosted-environments
- Quickstart: https://code.claude.com/docs/en/self-hosted-environments-quickstart

### Availability and plan gating (safe to state)

- "Self-hosted environments are in public beta on Team and Enterprise plans and are off by
  default." An Owner or admin must turn on **Allow self-hosted environments** in claude.ai
  admin settings. -> Public copy says "public beta, Team & Enterprise plans" - never "GA" and
  never "every plan".
- Requires **Claude Code v2.1.224 or later** on the runner host ("earlier versions don't
  recognize the `self-hosted-runner` subcommand") and **Git 2.24+**.
- Runner host: "A Linux or macOS host or container ... Windows isn't supported as a runner
  host; run the runner in a Linux container instead."
- Unavailable for organizations with Zero Data Retention enabled; inference cannot be routed
  through Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an LLM gateway.

### Architecture (safe to state)

- Model: **environment** (named destination created in claude.ai admin settings) -> **runner**
  (a process you deploy; "the idea is the same as a self-hosted CI runner") -> **session**
  (one Claude Code task). Sessions route to an environment, not to an individual runner.
- Surfaces that can route to a self-hosted environment: "Claude Code on the web, the mobile
  and desktop apps, scheduled routines, and the terminal, with `claude --cloud`". This is the
  basis for the visual's WEB / MOBILE / DESKTOP interface row.
- Start command, verbatim from the quickstart:
  `claude self-hosted-runner --environment-secret-file '/etc/claude/environment-secret' --base-dir '<writable-dir>'`
- Network: every connection is **outbound** HTTPS; "Anthropic never connects into your
  network." The runner polls `api.anthropic.com`; polling doubles as the heartbeat.

### The execution/interface split (the post's core fact, verbatim)

> "Repository checkouts, build artifacts, secrets, and any files a session creates or modifies
> stay on the machines you provision. The conversation itself, including prompts, responses,
> and tool results, goes to `api.anthropic.com` for model inference, and the session
> transcript is stored by Anthropic so a session can be picked up from any surface."

> "Session orchestration, queueing, and the claude.ai interface remain Anthropic-hosted: a
> self-hosted environment moves session execution into your network, not the control plane."

This is why the post must NOT say "everything stays local". Artifacts stay local; the
conversation and transcript do not. The visual's boundary box is labeled "execution plane"
for exactly this reason.

### Isolation is still the operator's job (basis for boundary 1)

- "plan for the operational ownership it carries: you build and maintain the runner image,
  operate the fleet, and control its network."
- Quickstart: "Before you connect real repositories or internal systems, work through
  [Deploy to production], which covers the security posture, egress control, git credentials,
  and orchestration."
- "The runner clones with whatever git credentials the host already has" (quickstart test
  step) - host credentials are live inside the runner unless you configure otherwise.
- Runner lifecycle: a runner locks to the first user whose session it picks up and serves
  only that user; production guidance is an orchestrator restart with "a fresh filesystem per
  restart". Isolation between users is by runner, not by magic.

---

## 2. Cross-session messaging: what is established

- From the release (verbatim above): sessions can message each other "on any of your
  machines"; `ListAgents` discovers them; scoped "(macOS and Linux)".
- Pre-existing `SendMessage` semantics from the agent-teams docs
  (https://code.claude.com/docs/en/agent-teams), which describe the same tool inside one
  session's team:
  - "When one agent sends another a message over `SendMessage`, Claude Code tells the
    receiving agent the message came from another Claude session, not from you. A teammate
    cannot approve a permission prompt or supply consent on your behalf, and a teammate that
    was denied an action cannot relay it to another teammate to bypass the check."
  - In auto mode, a permission classifier "reviews each message an agent sends before Claude
    Code delivers it"; blocked messages never reach the recipient.
  - Delivery is mailbox/inbox-based (JSON inbox files); the v2.1.224 fix list confirms inbox
    writes can fail and now surface as errors.
- v2.1.222 changelog: "messages sent to other agent sessions via SendMessage are now
  evaluated by the permission classifier before dispatch."

-> Safe public framing: discovery + message transfer between sessions, with an approval gate
on sensitive targets. NOT persistent memory, NOT an orchestrator, NOT a state store.

## 3. Inbound gating: what is established

- Release note, verbatim: "`crossSessionInbound` and `dialogExpiry` settings: cross-session
  messages sent to a session running with bypassed permissions are held for your approval,
  and messages to other sessions auto-deliver."
- The settings reference (https://code.claude.com/docs/en/settings) does **not** yet document
  either setting as of 2026-08-07 (checked; absent). Public copy therefore states only the
  release-note behavior for `crossSessionInbound` and does not describe `dialogExpiry`
  mechanics at all beyond naming it in this brief.

## 4. Sandbox credential masking: what is established

Primary doc, read in full: https://code.claude.com/docs/en/sandboxing

- Masking model: "the sandboxed command sees a per-session sentinel value instead of the real
  one"; the sandbox proxy "replaces the sentinel with the real value" on egress to
  `injectHosts`. "The command and anything it logs never hold the real credential."
- **Hard prerequisite:** "Set `network.tlsTerminate` so the proxy terminates TLS itself.
  Without it, masking fails without exposing anything: the command still sees only the
  sentinel, but the sentinel reaches the server unchanged and authentication fails."
- **Settings-source restriction:** masking "is honored only from settings you or your
  administrator control: user settings, managed settings, and the `--settings` CLI flag" -
  ignored in a repository's `.claude/settings.json` / `.claude/settings.local.json`.
- AWS: "mask `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` together"; the proxy detects
  SigV4 by the access key's sentinel and re-signs after substitution.
- Platform asymmetry: on macOS a masked *file* is blocked outright (no sentinel copy, tools
  that need it don't work in the sandbox); sentinel-file substitution is Linux/WSL2 behavior.
  Env-var masking sentinels work per the doc on both.
- **No default protection:** "There is no built-in credential deny list, so only the files and
  variables you list are restricted."

-> Basis for boundary 3 and the caption line "secrets are not automatically safe;
unconfigured is unprotected."

---

## 5. Excluded / uncertain - documented here, absent from public copy

| Item | Status | Why excluded |
|---|---|---|
| `dialogExpiry` semantics (values, defaults, exact behavior) | Named in the release note only; absent from the settings reference as of 2026-08-07 | Cannot describe mechanics beyond the release sentence; the visual and caption name `crossSessionInbound` behavior only |
| Cross-machine transport for `ListAgents`/`SendMessage` (how sessions on different machines find each other's inboxes) | Not documented as of 2026-08-07 | "On any of your machines (macOS and Linux)" is stated; the mechanism is not, so public copy states capability, not mechanism |
| Whether cross-session messaging requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Agent-teams docs predate the release and cover in-session teams; no doc ties the flag to the new cross-session path | Public copy avoids any claim about flags/enablement for messaging |
| Cross-session messaging INTO a self-hosted-environment session | No source combines the two features | The post presents them as capabilities from one release that compose as a pattern, under an explicit "not a turnkey orchestrator" caveat |
| JWT `decode`/`maskClaims` and env-var `extract` details | Release note names them; the sandboxing page documents `extract` for files in detail, env-value specifics are thinner | Visual carries no JWT/SigV4 config detail; caption names the capabilities only |
| Scout-digest phrasing "credential masking requires TLS termination" for *all* masking | Verified for masking (env + file) per sandboxing doc | Kept, phrased as the doc phrases it |
| Any throughput, adoption, cost, or security-outcome numbers | None published | Never invented |
| "Distributed pool of coding agents" (scout's extrapolation) | Not a documented product claim | Post says "pattern", caveat says orchestration remains your design problem |

## 6. Claim discipline distilled for the editor

- Say "public beta on Team and Enterprise plans" - the release says "Team and Enterprise
  plans", the docs add "public beta" and "off by default".
- Say "runners on Linux and macOS" (containers count as Linux hosts); say cross-session
  messaging "(macOS and Linux)" exactly as the release scopes it.
- Never say "all data stays local": checkouts/artifacts/secrets/files stay; prompts, tool
  results and transcripts go to `api.anthropic.com`.
- Never call `SendMessage` memory, sync, or orchestration.
- Never claim automatic credential safety: masking needs explicit configuration,
  `network.tlsTerminate`, and user/managed/`--settings` scope; there is no built-in deny list.
- Freshness hook is legitimate: release date 2026-08-07 equals research date.

## Sources

Primary (all fetched 2026-08-07):

- Release v2.1.224: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
- Changelog: https://code.claude.com/docs/en/changelog
- Self-hosted environments overview: https://code.claude.com/docs/en/self-hosted-environments
- Self-hosted environments quickstart: https://code.claude.com/docs/en/self-hosted-environments-quickstart
- Sandboxing / credential masking: https://code.claude.com/docs/en/sandboxing
- Agent teams (SendMessage semantics): https://code.claude.com/docs/en/agent-teams
- Settings reference (checked for `crossSessionInbound`/`dialogExpiry`; absent): https://code.claude.com/docs/en/settings

Secondary (not used for facts): the internal scout digest of 2026-08-07, used only for topic
selection; every claim in it was re-verified or excluded above.
