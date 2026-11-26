# Inside of the Day #15 - Client sites break silently after routine updates

Audience: owners of small web agencies and freelancers who run client websites. Draft only, not published. The owner publishes.

## Claim

Routine updates quietly break client sites. Google and AI assistants read what the site serves today, so the break shows up as lost traffic and leads, not as an error.

## Pairs (what changed → what readers and crawlers then see)

| Change | Effect | Number | Source |
|---|---|---|---|
| Plugin or theme update adds noindex | Page is dropped from Google results | WordPress runs 38.4% of all websites (context for how common plugin-driven sites are; not an effect size) | https://w3techs.com/technologies/details/cm-wordpress (page dated 26 Nov 2026, fetched 26 Nov 2026) |
| Sitemap removed or moved | New pages stop getting found | none | Qualitative: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview ("Googlebot might not discover your pages if no other sites link to them") |
| TLS certificate lapses | Browser warns before the site loads | Max certificate validity 398 → 47 days, March 2026 to March 2029 | https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/ (vote closed 11 Apr 2025, fetched 26 Nov 2026) |

noindex behaviour (no number): Google drops a page from results once it crawls the tag. https://developers.google.com/search/docs/crawling-indexing/block-indexing

## Numbers and checks

- 38.4%: web-verified 26 Nov 2026 on W3Techs. It says how much of the web is on WordPress, not how often updates add noindex. The caption states only the fact.
- 398 → 47 days: web-verified on the CA/Browser Forum page. The page gives the endpoints (starting March 2026, concluding March 2029); intermediate steps (200 days from 15 Mar 2026, 100 days from 15 Mar 2027) come from secondary sources and are not used in the post.
- No source found for "visitors leave" after a certificate warning (searched; click-through studies conflict), so the post says "see a browser warning first" and gives no abandonment number.
- No number for the sitemap pair.

## Confirm before posting

- Starter $19/month, weekly re-check, "emails within a day" (from the brief): confirm against plans.py and current pricing before publishing.
- Onbiom mentioned once; the offer line is the owner's own reply promise: the owner must be ready to send checks.
- Legal sweep of the Onbiom claim line if desired.

## Files

- caption.txt: exact LinkedIn text.
- assets/infographic.png: 1080x1350 at 2x, built from source/infographic.html with source/render.sh.
