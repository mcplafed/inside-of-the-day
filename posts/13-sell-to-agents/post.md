# Your next customer may not have a browser.

**Main question:** Are you ready to sell directly to an agent?

**Subhead:** I stopped asking whether agents can pay. I started asking whether my business can
sell to one.

## Format

Single-image portrait infographic for LinkedIn (4:5). Not a carousel. One editorial poster: a
dominant human-customer / agent-customer contrast converging on one shared commerce contract,
then a five-row merchant-ready checklist, then the takeaway.

Broad-reach topic: a merchant or product leader with no protocol knowledge should get the point
from the headline and the contrast block alone. The five questions are business questions, not
integration steps.

## Core insight

The merchant is the protagonist. The agent is a new kind of customer.

Humans buy through pages, forms, visual checkout and ambiguous conversations. An agent needs
structured answers: what exists, what it costs now, whether it is available, whether the buyer is
eligible, how it can pay, what happens after checkout, and how returns and support work. A
beautiful browser storefront is not a machine-readable sales channel.

This is deliberately **not** a post about whether an agent has a wallet. Payment is the easy
half and the most-covered half. The unanswered half is whether the business can state its own
commerce contract in a form a machine can consume, and refuse when it should.

## Mechanism

### The contrast

| Human customer | Agent customer |
|---|---|
| browses pages | reads structured product data |
| compares visual cards | queries price + availability |
| fills a checkout form | sends an authenticated order request |
| receives an email | consumes a machine-readable confirmation |

Both paths must meet in the same middle: **your commerce contract** - catalog, price,
eligibility, checkout, fulfillment, support. Most merchants have built one front door onto it.

### The merchant-ready checklist

1. **Can it find the product?** Structured catalog, offer data, attributes and terms - not only a
   visual page.
2. **Can it trust the price and availability?** Current price, currency, inventory, shipping,
   tax/fees and eligibility returned from a reliable machine interface.
3. **Can it place an authorized order?** Authenticated identity, explicit delegation/consent and
   a bounded checkout API - not an agent scraping buttons.
4. **Can you fulfil and explain the outcome?** Order confirmation, status, tracking,
   cancellation, return/refund rules and a human escalation path.
5. **Can you decline safely?** Merchant controls for high-risk, regulated, age-restricted,
   contractual or ambiguous purchases. "Agent-ready" does not mean "auto-approve."

## Takeaway

A browser storefront is not an agent sales channel. Sell to agents only when your commerce
contract is explicit, authorized and reversible.

## There is no authoritative universal standard - stated plainly

**This is the most important boundary in the post and it is on the visual.**

As of August 2026 three overlapping, vendor-led agentic-commerce specifications exist, all early:

| Spec | Maintainers / co-developers | Stated status |
|---|---|---|
| **ACP** (Agentic Commerce Protocol) | OpenAI + Stripe as Founding Maintainers; Stripe's docs also credit Meta as a creator | `beta` - verbatim in the repo README and status badge |
| **UCP** (Universal Commerce Protocol) | "UCP Authors", Apache-2.0; co-developers listed on ucp.dev include Google, Shopify, Amazon, Stripe, Walmart | No published version or maturity label; lodging/food specs "coming soon" |
| **AP2** (Agent Payments Protocol) | Google-initiated; v0.2 announced with a FIDO Alliance donation | v0.2; roadmap explicitly incomplete (cards / "pull" methods first) |

They compose in intent - AP2's glossary defines UCP as "A protocol providing a Checkout Object
standard when used with the Checkout Mandate" - but composition is a design goal, not deployed
universal infrastructure. Card-network programmes are earlier still: Visa's own developer page
for Visa Intelligent Commerce says "This product is in the process of development and
deployment."

So the post ships a **readiness checklist**, not an integration instruction. Every row is a
question a merchant can answer today regardless of which spec wins.

## What each checklist row rests on

Full working: `research/merchant-readiness-for-ai-agents.md`.

1. **Find.** schema.org `Offer` already carries `price`, `priceCurrency`, `availability`,
   `inventoryLevel`, `priceValidUntil`, `eligibleRegion`, `eligibleCustomerType`,
   `shippingDetails`, `hasMerchantReturnPolicy`, `itemCondition`. It is a **vocabulary, not a
   transaction interface** - perfect structured data makes you discoverable, not sellable-to.
   GS1 Digital Link + a GS1-conformant resolver cover identifier-first discovery.
2. **Trust price and availability.** OpenAI's product feed spec makes `price` (with currency),
   `availability` (`in_stock` / `out_of_stock` / `pre_order` / `backorder` / `unknown`),
   `target_countries`, `store_country`, `seller_name` and `seller_url` required, and requires
   `seller_privacy_policy` + `seller_tos` when a product is checkout-eligible. ACP's Feed API
   models `Price`, `Availability`, `list_price` and normalized `UnitPrice`.
3. **Authorized order.** Callable is not authorized. AP2 exists to close exactly that gap:
   verifiable digital credentials carrying a **Checkout Mandate** ("cryptographic proof that the
   Shopping Agent is authorized to purchase the Checkout that it has assembled") and a **Payment
   Mandate**, each in an open (constraints) and closed (bound) stage, signed on a **Trusted
   Surface** described as "a secure, non-agentic interface". AP2 separates **Human Present
   (Direct)** from **Human Not Present (Autonomous)**. UCP supplies OAuth 2.0 Identity Linking.
   ACP checkout carries `buyer.authentication_status`, `account_type` and intervention
   capabilities (3ds / biometric / address_verification). Shopify gates direct checkout
   completion behind agent trust tiers. W3C Verifiable Credentials Data Model 2.0 - the one
   ratified web standard in this stack - has been a Recommendation since 15 May 2025.
4. **Fulfil and explain.** ACP order webhooks (`order_create` / `order_update`) carry `carrier`,
   `tracking_number`, `tracking_url` and an `adjustments[]` array for refunds. OpenAI requires
   HMAC-signed `order_created` / `order_updated` webhooks and states the liability plainly: "Your
   platform is responsible for handling refunds and chargebacks, as you accepted the payment
   directly from the customer as the merchant of record." Return **terms** become machine-readable
   via schema.org `hasMerchantReturnPolicy` and Google's `returnPolicyCategory` enum.
5. **Decline safely.** The ACP checkout spec's `MessageError.code` enum already includes
   `region_restricted`, `age_verification_required` and `approval_required`, with a `resolution`
   of `requires_buyer_review` ("buyer must authorize"). Refusal is a first-class response type in
   the protocol's own schema. Plus OpenAI's per-product `is_eligible_search` /
   `is_eligible_checkout` flags and Shopify's trust tiers: three independent places to say no -
   per product, per agent, per attempted order.

## Boundaries and claim discipline

- **Preparedness framework, not a growth guarantee.** Stated on the visual: "Framework for
  readiness - not proof that agents should buy everything autonomously."
- **No claim that agents are already a dominant customer type.** No adoption, volume, revenue or
  merchant-support figure was verified against a primary source, so **no number of that kind
  appears anywhere** in the post, caption or visual.
- **No claim that every business needs agent checkout today.**
- **No claim that an agent can or should autonomously buy** regulated, high-risk, age-restricted,
  contractual, medical, financial or irreversible goods. Human authorization and merchant
  controls remain necessary.
- **Not a wallet/crypto post.** x402 is recorded in the research brief as an optional
  machine-to-machine example only, and Coinbase's own docs scope it to API and paywalled-resource
  access rather than physical-goods commerce. It does not appear in the caption or the visual, and
  the visual contains no wallet or crypto imagery.
- **Vendor-specific and experimental status is stated in plain language** in the caption and on
  the visual, not buried here.
- **OAuth attribution is precise.** OAuth 2.0 identity linking is a **UCP** capability. ACP's
  `openapi.delegate_authentication.yaml` is 3-D Secure 2, despite prose summaries elsewhere
  describing it as OAuth delegation. Do not let an edit merge the two.
- **AP2 naming is current.** "Intent Mandate / Cart Mandate" is v0.1-era terminology still
  circulating in blogs; the current spec uses **Checkout Mandate** and **Payment Mandate**.
- **No fictional merchant or customer case studies.** No named customers, no invented outcomes.
- **Mastercard Agent Pay is deliberately absent** - only secondary write-ups were reachable, no
  primary developer documentation was verified.
- **No public post number** in the eyebrow or visual (series is dropping public numbers).

## Sources

- Agentic Commerce Protocol: https://www.agenticcommerce.dev/
- ACP repository (status `beta`, dated spec versions, governance): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
- ACP 2026-04-17 OpenAPI specs: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/tree/main/spec/2026-04-17/openapi
- Stripe, Agentic Commerce Protocol: https://docs.stripe.com/agentic-commerce/acp
- Stripe, Universal Commerce Protocol: https://docs.stripe.com/agentic-commerce/protocol
- Universal Commerce Protocol: https://ucp.dev
- UCP repository: https://github.com/Universal-Commerce-Protocol/ucp
- Agent Payments Protocol (AP2): https://ap2-protocol.org/
- AP2 repository (specification, glossary, overview): https://github.com/google-agentic-commerce/AP2
- OpenAI, Agentic Commerce key concepts: https://developers.openai.com/commerce/guides/key-concepts
- OpenAI, product feed spec: https://developers.openai.com/commerce/product-feeds/spec
- OpenAI, going to production: https://developers.openai.com/commerce/guides/production
- Shopify, Agentic commerce: https://shopify.dev/docs/agents
- schema.org Offer: https://schema.org/Offer
- Google, merchant listing structured data: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- Google, return policy structured data: https://developers.google.com/search/docs/appearance/structured-data/return-policy
- GS1 Digital Link: https://www.gs1.org/standards/gs1-digital-link
- W3C Verifiable Credentials Data Model 2.0: https://www.w3.org/TR/vc-data-model-2.0/
- Visa Intelligent Commerce: https://developer.visa.com/capabilities/visa-intelligent-commerce
- Research brief: `research/merchant-readiness-for-ai-agents.md`

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 px mobile-feed legibility probe (downscaled from
  the full render).
- `source/infographic.html`: editable, self-contained visual source (no external assets or
  network dependencies; inline SVG converging arrows).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device
  scale factor 3) that also emits the mobile probe.
