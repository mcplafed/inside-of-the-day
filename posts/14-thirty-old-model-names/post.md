# Inside of the Day #14 - We retired 30 old model names. Nobody changed a line of code.

Follow-up to "Old models aren't cheaper. They're just dumber." (gpt-5.4-mini → gpt-6-luna, gpt-5.4 → gpt-6.1-terra).

## Mechanism

One alias map at the LLM gateway (LiteLLM `model_group_alias`): the old model name stays valid for callers and is served by a current model. 30 old names point to 8 current models. Rollback is one line.

## Swaps shown

Price is USD per 1M tokens, input / output. Score is Humanity's Last Exam (HLE).

| Old → new | Price | Cut | HLE |
|---|---|---|---|
| claude-4-5-sonnet → claude-5-5-sonnet | 3 / 15 → 2 / 10 | −33% | 7.2 → 55.0 |
| claude-4-7-opus → claude-5-5-opus | 5 / 25 → 4 / 20 | −20% | 42.3 → 61.4 |
| gpt-5.5 → gpt-6.1-sol | 5 / 30 → 2 / 10 | −60–67% | 45.8 → 52.9 |
| gpt-5.6-terra → gpt-6.1-terra | 2 / 12 → 1 / 5 | −50–58% | 42.9 → 46.2 |
| gpt-5.2 → gpt-6.1-terra | 1.75 / 14 → 1 / 5 | −43–64% | 37.7 → 46.2 |

## Takeaway

Most of the saving comes from the busiest models; the long tail removes vendor-retirement risk. Not every swap is silent-safe: a big generation jump changes behaviour, so owners test first.

## Scope

- Public list prices, public benchmarks and percentages only. No employer name, spend in dollars, team or app names.
- "About half the bill" is a rounded share; the author confirms it before posting.

## To verify before publishing

- Prices and HLE scores were taken from a working price table, not re-checked on the web. gpt-6.1-terra is listed as 1 / 5 in one place and 1.20 / 6 in another; the post uses 1 / 5, as the previous post did.

## Sources

- OpenAI, Anthropic and Azure list prices per 1M tokens (Nov 2026).
- Humanity's Last Exam; Artificial Analysis.

## Files

- `caption.txt` - exact LinkedIn text.
- `assets/infographic.png` - 1080×1350 (rendered at 2x).
- `source/` - `template.html` + `build.py` (rows) → `infographic.html`; `render.sh` screenshots it with headless Chrome.
