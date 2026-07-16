# Inside of the Day

Canonical editorial repository for the **Inside of the Day** LinkedIn series.

Each post is a compact, evidence-backed operating insight about AI-assisted engineering and agent systems. The repository keeps the final caption, editable visual source, rendered media, supporting sources, publication plan, and publication state together.

## Series order

| # | Working title | Status |
|---:|---|---|
| 1 | I switched my coding agent from Sonnet 5 high to Opus 4.8 low. It got cheaper - and better. | approved, scheduled |
| 2 | A founder question should block a task - not the agent system. | approved, scheduled |
| 3 | An autonomous session is done when the ready queue is empty. | approved, scheduled |
| 4 | Review the work, not the AI label. | approved, scheduled |
| 5 | My agents do not have one memory. | draft for review |

See [strategy/series-plan.md](strategy/series-plan.md) for the editorial and publication plan.

## Post layout

```text
posts/<number>-<slug>/
  caption.txt        Exact LinkedIn text
  post.md            Editorial metadata, scope, and sources
  assets/            Final publication media
  source/            Editable visual source
```

No access tokens, publication credentials, or LinkedIn publication-state files belong in this repository.
