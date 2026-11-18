# Inside of the Day #15 - Your AI bill has a hidden discount.

Status: draft for review. Not scheduled or published.

Follow-up to #14: compare cache-read prices as well as ordinary input and output prices when testing model replacements.

## Cache-read comparison

Standard API list prices in USD per 1M cache-read tokens, checked 18 November 2026. Savings compare the new model's cache-read rate with the old model's cache-read rate, not uncached input or the total request bill.

| Old model → candidate | Old cache read | New cache read | Saving |
|---|---:|---:|---:|
| Claude Haiku 4.5 → Claude Haiku 5.5 | $0.10 | $0.01 | −90% |
| GPT-5.4 mini → GPT-6 Luna | $0.075 | $0.01 | −87% |
| GPT-5.4 → GPT-6.1 Terra | $0.25 | $0.05 | −80% |
| GPT-5.5 → GPT-6.1 Sol | $0.50 | $0.10 | −80% |
| Claude Sonnet 4.5 → Claude Sonnet 5.5 | $0.30 | $0.10 | −67% |

Formula: `(1 − new cache-read rate / old cache-read rate) × 100`, rounded to the nearest whole percent. Mini → Luna is 86.67%; Sonnet is 66.67%.

Haiku 5.5's $0.01 rate applies to prompts ≤100k tokens. Above 100k, its $0.05 cache-read rate gives a 50% reduction versus Haiku 4.5, not 90%.

## Capability as well as price

Newer models can outperform their predecessors while costing less. This is a reason to test the candidates, not a claim that every replacement wins on every task. Validate quality, tool use and reliability alongside cost per successful task. No unverified benchmark scores are included.

## Scope and caveats

- These are candidates worth testing, not guaranteed drop-in replacements.
- Cache-read savings only. No claim of a 90% reduction in the entire AI bill.
- A model switch requires a new cache to warm up. Cache writes, retention, hit rate, output tokens and retries affect the actual bill.
- Tokenization and cache rules differ between models. Compare measured cost per successful task on real traffic.
- No universal five-request break-even claim: the result depends on the write tier, cache lifetime, token count and baseline.
- Public prices only; no employer, customer, internal spend or usage information.

## Sources

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)

## Files

- `caption.txt`: exact English LinkedIn draft.
- `assets/infographic.png`: final infographic with the selected headline and percentage savings.
- `source/design-brief.md`: visual content and generation specification. The image is generated raster artwork, not an HTML render.

Recheck current prices before publication. Saving this draft does not schedule or publish it to LinkedIn.
