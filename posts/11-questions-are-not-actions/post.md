# Inside of the Day #11 - Questions are not actions

## Title

**I stopped letting my agent turn every question into a fix.**

## First-person thesis

I used to ask an agent why something happened and receive an immediate "Fixed."
That response often removed the visible symptom before it preserved the evidence or
explained the causal chain. I changed the operating rule: a question about an error
is an investigation request, not permission to mutate state. Before remediation, I
want the event, evidence, cause, and a recurrence safeguard. The only exception is
containment of an ongoing harmful condition.

## One mechanism

Use an explicit question-to-investigation gate:

1. Record what happened and preserve relevant evidence.
2. Reconstruct the causal chain and state the confidence/unknowns.
3. Propose a concrete recurrence safeguard, such as a test, validation, alert, or
   operating rule.
4. Ask for approval or receive an explicit remediation instruction before changing
   state.

This separates two different jobs that a fast agent response can conflate:
understanding an error and correcting an error.

## Impact

- **Primary: risk reduction and repeatability.** The operator keeps the evidence and
  gets a reason the error occurred, not only a claim that its visible symptom changed.
- **Secondary: trust.** The agent's action is reviewable because the investigation,
  decision, and remediation are distinct.

This is a first-person operating practice, not a measured universal performance claim.

## Boundaries

- Do not delay containment of active harm. Stop the damage first, then investigate.
- A question can still include an explicit action request, for example: "Why did this
  happen, and please fix it?" In that case, preserve the investigation before or
  alongside the requested remediation.
- Do not turn diagnosis into analysis paralysis. The investigation should be
  proportional to the blast radius and reversible when possible.

## Source provenance

- Primary source: the author's observed agent workflow and the operating rule added to
  the author's global Claude Code configuration on 2026-07-22.
- No external empirical claim is made. Do not imply that this rule is an Anthropic
  product behavior or an official platform recommendation.
- The public Agent Automation Kit repository may be used as an optional series link,
  but it is not the source repository for this particular rule unless the rule is
  published there first.

## Visual contract

- Eyebrow: `Inside of the Day #11 - Questions are not actions`.
- Headline: **I asked why. My agent said "Fixed." That was the problem.**
- Left path: user asks `Why did this happen?` -> agent immediately changes state ->
  evidence fades -> `Same failure returns`.
- Right path: user asks the same question -> four-card investigation gate:
  `What happened` -> `Evidence` -> `Cause` -> `Recurrence guard` -> explicit
  remediation decision.
- Takeaway: **A fast fix cleans up the chat. A causal explanation improves the
  system.**
- Small boundary line: `Contain active harm first. Then investigate.`
- Footer: `inside-of-the-day` on the left; `@vitalylobachev` on the right.

## Status

Draft only. Caption and visual require explicit approval before rendering, scheduling,
or publication.
