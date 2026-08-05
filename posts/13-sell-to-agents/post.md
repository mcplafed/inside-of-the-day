# ARE YOU READY TO ACCEPT PAYMENTS FROM AI AGENTS?

**Subhead:** The question is no longer whether agents can pay. It is whether your checkout can
accept them safely.

## Format

Single-image portrait infographic for LinkedIn (4:5). Not a carousel. One editorial poster: giant
headline question, an unmissable four-stage machine pipeline, three substantial implementation
cards (action / example / guardrail), a "merchant owns" bar, the takeaway and a compact protocol
caveat.

This is an **implementation guide with exactly three steps**, not a readiness checklist. The
merchant remains the protagonist: every step is something the merchant builds and controls.

## Core framing

An agent cannot use a normal browser checkout reliably. To accept an agent payment, a merchant
needs an explicit machine path from offer to authorization to a recoverable order outcome.

That path is the post:

```
MACHINE-READABLE OFFER -> AGENT CHECKOUT API -> BOUNDED PAYMENT MANDATE -> ORDER OUTCOME
```

Not a wallet post. Payment credentials are the covered half; the unanswered half is whether the
business exposes a machine-consumable commerce contract and can refuse when it should.

## The three-step implementation blueprint

### STEP 1 - PUBLISH A MACHINE-READABLE OFFER

**Action:** Give the agent a truthful product, price and eligibility record.

**Implement:**

- product/offer data, live price + currency, availability, shipping/tax/returns, and checkout
  eligibility;
- distinguish **discoverable** from **purchasable**.

**Verified examples:**

- **schema.org `Offer`** - vocabulary for product, price, `availability`, `hasMerchantReturnPolicy`,
  `eligibleRegion`. A vocabulary, **not a transaction API**.
- **OpenAI Product Feed** (`developers.openai.com`) - `is_eligible_search` and
  `is_eligible_checkout` as two separate merchant decisions; `seller_privacy_policy` and
  `seller_tos` become required when checkout-eligible.

**Guardrail:** *Discoverable is not purchasable. Keep checkout eligibility explicit.*

### STEP 2 - OPEN AN AGENT CHECKOUT API

**Action:** Let an authenticated agent build, update and complete a bounded checkout session.

**Implement:**

- checkout session lifecycle (create, update, fetch, complete/cancel); exact price, tax,
  fulfilment and terms answers; idempotency for retry-safe requests;
- agent identity/authentication and intervention paths for 3DS / address verification / biometric
  as applicable.

**Verified examples:**

- **Agentic Commerce Protocol - Agentic Checkout API** (`agenticcommerce.dev`) -
  `POST /checkout_sessions` plus update, fetch, `complete`, `cancel`; `Idempotency-Key` required on
  all POSTs; session `status` from `not_ready_for_payment` to `ready_for_payment` to `completed`;
  `capabilities.intervention` = 3ds / biometric / address_verification. Status: **beta**.
- **UCP capability model / OAuth 2.0 identity linking** (`ucp.dev`) - declared capabilities
  (Checkout, Identity Linking, Order) as an alternate, early **vendor-led** path.

**Guardrail:** *A callable endpoint is not authorization. Require an authenticated buyer and
explicit intervention when needed.*

### STEP 3 - ACCEPT A BOUNDED PAYMENT MANDATE

**Action:** Charge only what the buyer authorized - then return an order outcome an agent can act
on.

**Implement:**

- scoped, expiring authorization (amount, currency, merchant/session binding); the merchant
  validates and accepts or declines; machine-readable order confirmation/status, tracking, refund
  and cancellation paths;
- a human approval boundary and decline codes for age-restricted, region-restricted, high-risk and
  ambiguous purchases.

**Verified examples:**

- **AP2 Checkout Mandate / Payment Mandate** (`ap2-protocol.org`) - **v0.2**; the closed mandate is
  bound to a merchant-signed Checkout by cryptographic hash and is signed on a **Trusted Surface**,
  described in the spec as "a secure, non-agentic interface"; the merchant MUST return a Checkout
  Receipt.
- **ACP Delegate Payment + order webhooks** (`agenticcommerce.dev`) - vault token scoped by
  `max_amount`, `currency`, `checkout_session_id`, `merchant_id`, `expires_at`; `order_create` /
  `order_update` webhooks carrying `carrier`, `tracking_number`, `tracking_url` and an
  `adjustments[]` array for refunds.

**Guardrail:** *Agent-ready is not auto-approve. Keep merchant policy, decline paths and human
approval for high-risk orders.*

## Merchant owns

On the visual as an explicit bar: **price / acceptance / fulfilment / refunds / declines.**

Primary-sourced: OpenAI states "OpenAI is not the merchant of record in the Agentic Commerce
Protocol" and "Your platform is responsible for handling refunds and chargebacks, as you accepted
the payment directly from the customer as the merchant of record." agenticcommerce.dev says
businesses "maintain their customer relationships as the merchant of record, retaining control over
which products can be sold, how they're presented, and how orders are fulfilled."

## Takeaway

Accepting agent payments is not adding a wallet button.
It is exposing a safe commerce contract: offer -> checkout -> authorization -> outcome.

## Compact visible caveat

**On the visual, verbatim:** "Current protocols are vendor-led and early: ACP is beta; AP2 is v0.2;
UCP has no published maturity label. Use this as an implementation map, not a claim of universal
infrastructure."

| Spec | Maintainers / co-developers | Stated status |
|---|---|---|
| **ACP** (Agentic Commerce Protocol) | OpenAI + Stripe as Founding Maintainers; Stripe's docs also credit Meta as a creator | `beta` - verbatim in the repo README and status badge |
| **AP2** (Agent Payments Protocol) | Google-initiated; v0.2 announced with a FIDO Alliance donation | v0.2; roadmap explicitly incomplete |
| **UCP** (Universal Commerce Protocol) | "UCP Authors", Apache-2.0; co-developers listed on ucp.dev include Google, Shopify, Amazon, Stripe, Walmart | No published version or maturity label |

They compose in intent - AP2's glossary defines UCP as "A protocol providing a Checkout Object
standard when used with the Checkout Mandate" - but composition is a design goal, not deployed
universal infrastructure.

## Boundaries and claim discipline

- **Implementation map, not universal infrastructure.** Stated in plain language on the visual and
  in the caption, not buried here.
- **No adoption, volume, revenue or merchant-count figure** appears anywhere in the post, caption
  or visual - none was verified against a primary source.
- **No claim that every business needs agent checkout today.**
- **No claim that an agent can or should autonomously buy** regulated, high-risk, age-restricted,
  contractual, medical, financial or irreversible goods. Appropriate buyer authorization and
  merchant controls remain necessary; stated in the caption.
- **Not a wallet/crypto post.** No wallet or crypto imagery on the visual; x402 stays in the
  research brief as an optional machine-to-machine example only (Coinbase's own docs scope it to
  API and paywalled-resource access, not physical-goods commerce).
- **OAuth attribution is precise.** OAuth 2.0 identity linking is a **UCP** capability. ACP's
  `openapi.delegate_authentication.yaml` is 3-D Secure 2, despite prose summaries elsewhere
  describing it as OAuth delegation. Do not let an edit merge the two.
- **AP2 naming is current.** "Intent Mandate / Cart Mandate" is v0.1-era terminology still
  circulating in blogs; the current spec uses **Checkout Mandate** and **Payment Mandate**.
- **Mastercard Agent Pay is deliberately absent** - only secondary write-ups were reachable, no
  primary developer documentation was verified.
- **No fictional merchant or customer case studies.**
- **No public post number** in the eyebrow or visual (series is dropping public numbers).

## Sources

Full working: `research/merchant-readiness-for-ai-agents.md`.

Primary references named in the caption:

- schema.org Offer: https://schema.org/Offer
- OpenAI, product feed spec: https://developers.openai.com/commerce/product-feeds/spec
- Agentic Commerce Protocol: https://www.agenticcommerce.dev/
- Agent Payments Protocol (AP2): https://ap2-protocol.org/
- Universal Commerce Protocol: https://ucp.dev
- OpenAI, Agentic Commerce key concepts: https://developers.openai.com/commerce/guides/key-concepts

Additional primary sources behind the step details:

- ACP repository (status `beta`, dated spec versions, governance): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
- ACP 2026-04-17 OpenAPI specs (checkout, webhook, feed, delegate payment): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/tree/main/spec/2026-04-17/openapi
- AP2 repository (specification, glossary, overview): https://github.com/google-agentic-commerce/AP2
- OpenAI, going to production: https://developers.openai.com/commerce/guides/production
- Stripe, Agentic Commerce Protocol: https://docs.stripe.com/agentic-commerce/acp
- Stripe, Universal Commerce Protocol: https://docs.stripe.com/agentic-commerce/protocol
- UCP repository: https://github.com/Universal-Commerce-Protocol/ucp
- W3C Verifiable Credentials Data Model 2.0: https://www.w3.org/TR/vc-data-model-2.0/

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `assets/infographic-mobile-probe.png`: 400x500 px mobile-feed legibility probe (downscaled from
  the full render).
- `source/infographic.html`: editable, self-contained visual source (no external assets or network
  dependencies; CSS-only pipeline arrows).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale
  factor 3) that emits the mobile probe and reports panel overflow plus the rendered line count of
  every headline, pipeline chip, step title, action line and merchant-owns pill.
