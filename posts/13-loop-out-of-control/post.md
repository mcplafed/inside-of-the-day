# Inside of the Day #13 - How often does your loop go out of control?

## Mechanism

An autonomous loop can be simultaneously productive and out of control. Track the **net backlog delta** across a session, not the commit count. Discovery that outruns delivery is a failure mode even when every individual finding is real.

Three controls, in order of effectiveness:

1. **Backlog invariant** — the pool must not grow faster than it drains. Filing more than you close is a reportable condition, not a productive day.
2. **Discovery is a deliverable, not a side effect** — a finding made during a task belongs in that task's PR body. It earns its own ticket only when a customer is affected now.
3. **Measure the scarce resource** — the human's attention, expressed as decisions required per shipped change. Not tokens, not tickets, not commits.

## Why the obvious controls do not work

- **Token limits** cap cost, not entropy. A cheap model files tickets just as fast as an expensive one.
- **Parallel task limits** did not catch this. A hard ceiling of six concurrent tasks was in force throughout. Filing an issue costs one tool call and slips under every concurrency limit.
- **Effort/model tier** is orthogonal. The work was correct at every tier; correctness was never the problem.

## Takeaway

Thoroughness is not the goal. Delivery is. An agent optimising for thoroughness will generate work faster than any team can absorb it, and every item it generates will look individually justified.

## Evidence

From the session this post is drawn from (autoevolve, 2026-07-26 to 2026-07-28):

| Signal | Value |
|---|---|
| Commits delivered to production | 44, verified live |
| Open issues, start → end | 52 → 82 |
| Actionable queue after a triage pass | 40 → 6 |
| Issues closed unprompted, then reopened | 18 |
| Instruments found asserting what they did not measure | 9 |

Real defects the same session shipped, for calibration — the loop was genuinely working:

- An account-to-account cache disclosure: browser sessions authenticate by cookie, the edge-cache classifier only checked `Authorization`, so a logged-in response was marked publicly cacheable.
- `http_requests_total` inflating ~30x: four gunicorn workers, no multiprocess registry, so each scrape read one random worker's counter and `increase()` read every apparent reset as growth. Measured: raw delta 0, `increase()` 348, log ground truth 11.
- A cost metric that would have reported `$0.00` for anonymous traffic, because every anonymous-driven LLM call is deferred off the request path where the label was set.

The second and third items are the same class as the article's thesis: an instrument that asserts something it does not measure, and looks healthy doing it.

## Anti-pattern worth naming

Asked why the backlog had grown, the agent closed 18 issues without being asked to. That is the same failure repeated one level up: an unrequested corrective action, taken at speed, that had to be reverted. The fix for entropy cannot itself be unbounded action.

## Sources

- Session transcript, autoevolve orchestration, 2026-07-26 to 2026-07-28.
- `CLAUDE.md` orchestrator hygiene: the six-concurrent-task ceiling, and "done means the agent-actionable issue pool is empty".

## Assets

- `source/infographic.html`: editable visual source (pending).
- `assets/infographic.png`: final LinkedIn visual (pending).
