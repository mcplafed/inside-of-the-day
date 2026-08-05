# Merchant readiness for AI agents - evidence map

Research brief for the post *Your next customer may not have a browser.*

**Framing under test:** not "can an agent pay?" but "can a business sell directly to an
agent?" The merchant is the protagonist; the agent is a new kind of customer. Verified against
primary, publicly accessible documentation between 3-5 August 2026. Anything not traced to a
primary source is listed under **Excluded** and does not appear in public copy.

---

## 0. Headline finding: there is no single universal standard

As of August 2026 there are **three overlapping, vendor-led agentic-commerce specifications**,
each at an early maturity level, plus separate card-network programmes. A merchant cannot
"implement the standard" because there isn't one. This is the single most important disciplinary
fact for the post: the deliverable is a **readiness framework**, not an integration instruction.

| Spec | Maintainers / co-developers | Stated status |
|---|---|---|
| **ACP** - Agentic Commerce Protocol | OpenAI + Stripe as Founding Maintainers (Stripe's docs also credit Meta as a creator) | `beta` - stated verbatim in the repo README and a status badge |
| **UCP** - Universal Commerce Protocol | "UCP Authors", Apache-2.0; co-developers listed on ucp.dev include Google, Shopify, Amazon, Stripe, Walmart; Stripe describes itself as "a member of the UCP Tech Council" | No version number or maturity label published on the site; lodging and food capability specs marked "coming soon" |
| **AP2** - Agent Payments Protocol | Google-initiated (`google-agentic-commerce/AP2`), Apache-2.0; v0.2 announced alongside a **FIDO Alliance donation** | v0.2; roadmap explicitly incomplete (initial version supports "pull" methods like cards only) |

They are not purely rivals - they compose. AP2's own glossary defines UCP as "A protocol
providing a Checkout Object standard when used with the Checkout Mandate", and UCP advertises
"Agent Payments Protocol (AP2), Agent2Agent (A2A), and Model Context Protocol (MCP) support
built-in". But composition is a design intention, not deployed universal infrastructure.

AP2's own overview names the risk in its own words: without a common protocol the industry
faces "a fragmented and insecure ecosystem, characterized by proprietary, siloed solutions that
increase complexity for merchants". That is a description of the present state, written by one
of the parties producing it.

---

## 1. Product discovery vs transacting - two different problems

The distinction matters because most merchants already do the first and none of it makes them
transactable.

### Discovery: vocabularies and feeds (mature, widely deployed)

**Schema.org `Offer`** (verified at https://schema.org/Offer) already carries essentially every
field an agent needs to evaluate an offer:

- `price`, `priceCurrency` (ISO 4217), `priceValidUntil` - "The date after which the price is no
  longer available"
- `availability` (InStock / OutOfStock / PreOrder), `inventoryLevel` - "The current approximate
  inventory level for the item or items"
- `eligibleRegion`, `eligibleCustomerType` - eligibility, not just price
- `shippingDetails` (-> `OfferShippingDetails`), `hasMerchantReturnPolicy`
  (-> `MerchantReturnPolicy`), `itemCondition`

**Critically: `Offer` is a vocabulary, not a transaction interface.** It describes an offer. It
does not create a cart, hold inventory, authorize a buyer, or place an order. A merchant with
perfect structured data is discoverable and still not sellable-to.

**Google merchant listing structured data** (developers.google.com) - required: `name`, `image`,
`offers.price`, `offers.priceCurrency`. Recommended: `availability`, `url`, `itemCondition`,
`priceValidUntil`, plus shipping (`shippingRate`, `shippingDestination`, `deliveryTime`) and
return-policy properties. Notable constraint: "only pages where a shopper can purchase a product
are eligible for merchant listing experiences."

**Google return-policy structured data** - required is *either* `applicableCountry` +
`returnPolicyCategory`, *or* `merchantReturnLink`. `returnPolicyCategory` enum:
`MerchantReturnFiniteReturnWindow` (then `merchantReturnDays` becomes required),
`MerchantReturnNotPermitted`, `MerchantReturnUnlimitedWindow`. This is the first place a
merchant's *post-purchase* contract becomes machine-readable at all.

**GS1 Digital Link + GS1-conformant Resolver** (gs1.org/standards/gs1-digital-link,
ref.gs1.org/standards/resolver) - identifier-first discovery: a GTIN embedded in a web URI
resolves to one or more authoritative sources of information about the identified item, with
context-aware routing. Relevant as the identity/traceability layer beneath a catalog, part of
retail's migration to 2D barcodes. Not a commerce transaction layer.

### Transacting: merchant feeds that gate checkout

**OpenAI product feed spec** (developers.openai.com/commerce/product-feeds/spec) is where
discovery and transactability visibly separate. Required fields include two explicit
merchant-controlled gates:

- `is_eligible_search` (Boolean)
- `is_eligible_checkout` (Boolean)

Other required fields: `item_id`, `title`, `description`, `url`, `brand`, `image_url`, `price`
(with currency code, e.g. "79.99 USD"), `availability` (enum `in_stock` / `out_of_stock` /
`pre_order` / `backorder` / `unknown`), `seller_name`, `seller_url`, `target_countries` (ISO
3166-1 alpha-2), `store_country`. Conditionally required: `availability_date` when availability
is preorder/backorder; `seller_privacy_policy` and `seller_tos` **required if
`is_eligible_checkout` is true**; `return_policy` for the returns section.

The `is_eligible_search` / `is_eligible_checkout` pair is the cleanest primary evidence that
"agent-visible" and "agent-purchasable" are two separate merchant decisions.

**ACP Feed API** (`spec/2026-04-17/openapi/openapi.feed.yaml`) - `POST /feeds`,
`GET /feeds/{id}`, `GET|POST /feeds/{id}/products`. Schemas include `Price`, `Availability`,
`UnitPrice` (normalized unit price for goods sold by weight/volume/measure), `list_price`
(pre-discount reference), variant-level `price`/`availability`/`url`. Validation is enforced -
e.g. "target_country must be an ISO 3166-1 alpha-2 code".

**Shopify** (shopify.dev/docs/agents) - Global Catalog: "Search products across every Shopify
merchant from a single endpoint"; Storefront Catalog scopes discovery to one merchant. The
Catalog MCP server exposes `search_global_products` and `get_global_product_details` (by
Universal Product ID). Requires client credentials from the Dev Dashboard and a Bearer token.

---

## 2. Programmatic checkout - what a merchant actually has to serve

**ACP Agentic Checkout API** (`openapi.agentic_checkout.yaml`, spec version 2026-04-17,
verified from the raw file, 3,365 lines):

Endpoints:

```
POST /checkout_sessions
POST /checkout_sessions/{checkout_session_id}
GET  /checkout_sessions/{checkout_session_id}
POST /checkout_sessions/{checkout_session_id}/complete
POST /checkout_sessions/{checkout_session_id}/cancel
```

Headers: `Authorization` (Bearer), `Content-Type`, `API-Version` (date-based, `YYYY-MM-DD`),
`Idempotency-Key` (UUID v4, **required on all POSTs**), `Request-Id`, `Signature`, `Timestamp`.
Idempotency errors are first-class: `idempotency_key_required` (400), `idempotency_in_flight`
(409, with `Retry-After`), `idempotency_conflict` (422).

Session `status` enum includes `incomplete`, `not_ready_for_payment`, `ready_for_payment`,
`completed`, `canceled`. Session payload carries `line_items` (with `availability_status`,
`disclosures`, `variant_options`), `totals` (items base, discount, subtotal, tax, shipping,
final - in **minor currency units**), `fulfillment_options` (shipping / digital / pickup /
local_delivery, with cost and delivery windows), `fulfillment_details`, `links` (terms of use,
privacy, **return policy**), `capabilities` (supported payment handlers, intervention types:
3ds / biometric / address_verification), `buyer` (email required; `account_type` guest /
registered / business; `authentication_status`), `company` + `tax_exemption` (B2B: tax id,
certificate id, exempt regions, expiry), `loyalty`, `marketing_consent_options` ->
`marketing_consents` recorded on completion, `quote_id` / `quote_expires_at`.

Note what this list is: **the entire commerce contract, rendered as a schema.** Price, tax,
eligibility, fulfilment options, consent and legal links all have to be machine-answerable. That
is the post's core argument, in the form of a primary artifact.

**UCP** (ucp.dev, github.com/Universal-Commerce-Protocol/ucp) - defines composable
**Capabilities** (Checkout, Identity Linking, Order) plus **Extensions** (Discounts,
Fulfillment). Businesses "**Declare** supported capabilities to enable autonomous discovery by
platforms" via a standardized profile; checkout works "with or without human intervention";
transport-agnostic across REST, MCP and A2A. Stripe's summary of UCP: checkout, identity linking
(OAuth 2.0), order tracking, payment token exchange.

**Shopify** - Cart MCP (line items, localization, buyer context), Checkout MCP: "Convert carts
into checkouts and complete purchases **for trusted agents**". Capability negotiation via agent
profiles hosted at well-known URLs, where "higher trust tiers" unlock broader access including
direct checkout completion; rate limits and tool access vary by tier. Universal Cart API ("lets
AI agents collect items from any merchant, on or off Shopify") is **early access, waitlist**.

**OpenAI's role division** (developers.openai.com/commerce/guides/key-concepts): buyer selects;
agent collects buyer/fulfilment/payment info and renders checkout UI; **merchant** validates
orders, determines fulfilment, calculates tax, processes payment on its own systems; PSP handles
the transaction. Merchants must build (1) a product feed, (2) Agentic Checkout Spec-compliant
endpoints, (3) payment handling via a PSP or the Delegated Payment Spec.

Verbatim and load-bearing: **"OpenAI is not the merchant of record in the Agentic Commerce
Protocol."** Merchants accept or decline orders and process payments themselves.

agenticcommerce.dev, verbatim: businesses "maintain their customer relationships as the merchant
of record, retaining control over which products can be sold, how they're presented, and how
orders are fulfilled."

---

## 3. Payment - bounded, scoped tokens (not "the agent has a wallet")

**ACP Delegate Payment API** (`openapi.delegate_payment.yaml`) -
`POST /agentic_commerce/delegate_payment` returns a vault token (`vt_` prefix) representing a
card credential in a controlled, time-limited form, so the merchant's PSP can charge **up to a
capped amount** without holding raw card data. Allowance fields: `reason` (currently `one_time`
only), `max_amount` (minor units), `currency`, `checkout_session_id`, `merchant_id`,
`expires_at`. Also carries a `risk_signals[]` array (`type: card_testing`, `score`, `action`:
`blocked` / `manual_review` / `authorized`).

The shape is the point: the credential is **scoped to one merchant, one session, one ceiling,
one expiry.** That is the opposite of an agent holding a general-purpose wallet.

**ACP Delegate Authentication API** (`openapi.delegate_authentication.yaml`) - worth recording
because it is easy to mis-cite. Despite Stripe's prose summary describing "Delegate
authentication: Delegate authorization with OAuth 2.0", the 2026-04-17 spec file itself is
**3-D Secure 2 consumer authentication**: `POST /delegate_authentication`,
`POST /delegate_authentication/{authentication_session_id}/authenticate`,
`GET /delegate_authentication/{authentication_session_id}`; returns `trans_status`, cryptogram,
ECI. No OAuth flow, no scopes, no agent-to-account binding in that file. **OAuth 2.0 identity
linking is a UCP capability, not this ACP file.** Public copy must attribute OAuth identity
linking to UCP, not to ACP's delegate-authentication spec.

**x402** - OPTIONAL example only (docs.cdp.coinbase.com/x402, coinbase.com developer platform).
Revives HTTP `402 Payment Required`: the server answers a request with 402 plus payment details
(amount, currency, destination), the client pays and retries, the server serves the resource.
Coinbase + Cloudflare; USDC-denominated. Coinbase's own docs position it for **machine-to-machine
payments, pay-per-use API calls and paywalled content** - i.e. digital resource access, **not
physical-goods merchant commerce.** For a merchant-readiness post this is a footnote at most, and
the brief's instruction to keep crypto out of the visual is well founded on the primary source's
own scoping.

**Card networks.** Visa's own developer page for Visa Intelligent Commerce
(developer.visa.com/capabilities/visa-intelligent-commerce) names four services - Tokenization
("a new pass-through payment token, specific to agents"), Authentication (step-up verification
plus Passkey setup), Payment Instructions (controls ensuring "payment credential requests match
the user's authenticated instructions"), Signals (for dispute resolution) - plus an MCP server.
Status, verbatim and unusually candid: **"This product is in the process of development and
deployment. Depictions are representations of potential features and sequences."** Free in
sandbox; contact Visa for production fees.

---

## 4. Authorization - calling the API is not permission to buy

This is the section that makes the post more than a plumbing checklist.

**AP2** states the problem in its own overview: today's payment protocols assume "a human user
directly interacting with a trusted interface" and autonomous agents "shatter this assumption",
leaving three unanswered questions - **Authorization** ("What verifiable proof demonstrates that
the user granted the agent the specific authority to make this particular purchase?"),
**Authenticity of Intent** (how can a merchant be sure the request reflects true intent "without
errors or AI 'hallucinations'"), and **Accountability** (user? agent developer? merchant?
issuer? PSP? orchestration layer?).

Its answer is **verifiable digital credentials (VDCs)** - "tamper-evident, cryptographically
signed digital objects" - carrying two mandate types, each in an open and a closed stage
(verified from `docs/glossary.md` and `docs/ap2/specification.md`):

- **Checkout Mandate** - "A Mandate used for authorizing the completion of a checkout." Its
  purpose, verbatim: "designed to provide the Merchant cryptographic proof that the Shopping
  Agent is authorized to purchase the Checkout that it has assembled." The merchant MUST provide
  a merchant-signed JWT containing the Checkout; the closed mandate is bound to it by
  cryptographic hash. Once the merchant has accepted or rejected it, the merchant **MUST return a
  Checkout Receipt**.
- **Payment Mandate** - "A Mandate used for authorizing the payment for a particular checkout",
  verified by the Credential Provider / network / processor.
- **Open Mandate** - "has not yet been bound to a particular action. It possesses constraints to
  be applied to a closed mandate."
- **Closed Mandate** - "bound to a particular action with a Verifier to authorize the agent to
  perform an action."
- **Trusted Surface** - "A secure, **non-agentic** interface that renders Mandate Content to the
  User for authorization and consent."
- **Mandate Delegation** - "A process where a User authorizes an Agent to perform an action on
  their behalf."

And the two modes, verbatim:

- **Human Present (Direct):** "The User directly sees the closed Checkout and approves it and its
  payment explicitly."
- **Human Not Present (Autonomous):** "The User sees and approves a set of constraints over what
  closed Checkout and Payment would meet their intent. The Shopping Agent then assembles and
  approves a closed Checkout and Payment Mandate on their behalf using these open Mandates."

Verifiers always receive closed mandates in both modes; the difference is only how the signature
is validated - directly from a user credential (Direct) or from an agent key backed by
user-signed open mandates carrying constraints (Autonomous).

Design principles that support the post's claim discipline, verbatim: "**Verifiable Intent, Not
Inferred Action** - Trust in payments is anchored to deterministic, non-repudiable proof of
intent from the user, directly addressing the risk of agent error or hallucination"; and "AP2
provides a non-repudiable, cryptographic audit trail for every transaction, aiding in dispute
resolution."

**W3C Verifiable Credentials Data Model 2.0** - a **W3C Recommendation dated 15 May 2025**
(w3.org/TR/vc-data-model-2.0). Issuer / holder / verifier roles; "a tamper-evident [credential]
whose authorship can be cryptographically verified"; selective disclosure. This is the one piece
of the authorization story that is a genuine, ratified web standard rather than a vendor spec -
worth noting precisely because everything above it is not.

**Merchant-side authorization surfaces that already exist:** ACP checkout `buyer.account_type`
(guest / registered / business) and `buyer.authentication_status`; `capabilities.intervention`
types 3ds / biometric / address_verification; UCP Identity Linking over OAuth 2.0; Shopify's
trust tiers gated on agent profiles at well-known URLs, where only higher tiers may complete
checkout directly.

---

## 5. Post-purchase - the half everybody forgets

**ACP order webhooks** (`openapi.agentic_checkout_webhook.yaml`) - event types `order_create` and
`order_update`; implementations "MUST accept unrecognized values gracefully". Order status values
seen in the spec examples: `created`, `processing`, `shipped`, `completed`. Fulfilment objects
carry `carrier`, `tracking_number`, `tracking_url`. Money reversals use an `adjustments[]` array
(replacing a legacy `refunds[]` field) with `type` (e.g. "refund"), `status`, `amount`,
`currency`, `occurred_at`, `description`; totals include an `amount_refunded` display line.

**OpenAI production requirements** (developers.openai.com/commerce/guides/production) - merchants
must emit `order_created` and `order_updated` webhooks with valid **HMAC signatures**, and use
the order-update webhook to keep ChatGPT informed of refund/chargeback status changes. TLS 1.2+
on port 443 with a valid public certificate. PCI DSS scope depends on the integration method;
OpenAI may require an attestation of compliance (AOC) before production access. Sandbox
certification must cover session creation with and without shipping address, shipping option
updates, payment tokenization, order completion, error scenarios (**missing fields, out-of-stock,
payment decline**) and idempotency safety.

Liability, verbatim: **"Your platform is responsible for handling refunds and chargebacks, as you
accepted the payment directly from the customer as the merchant of record."**

**Shopify** - Order MCP `get_order` for on-demand order state, plus order webhooks for
fulfilment, returns, refunds, exchanges and cancellations. **UCP** - Order capability: shipping,
delivery and returns status via webhook-based lifecycle updates.

Machine-readable return *terms* (as opposed to status) come from schema.org
`hasMerchantReturnPolicy` / `MerchantReturnPolicy` and OpenAI's feed `return_policy` +
`return_deadline_in_days`.

**Gap worth stating honestly:** none of these specs standardizes a **human escalation path**.
There is no primary standard for "get me a person". ACP surfaces `links` (terms, privacy, return
policy) and `messages[]` with resolution `requires_buyer_input` / `requires_buyer_review`, and
that is the closest thing. The checklist row therefore prescribes an escalation path as merchant
practice, not as a standard.

---

## 6. Declining safely - the strongest single piece of evidence

The ACP checkout spec's `MessageError.code` enum, read verbatim from
`spec/2026-04-17/openapi/openapi.agentic_checkout.yaml` (lines ~1856-1878):

```
missing, invalid, out_of_stock, payment_declined, requires_sign_in, requires_3ds,
low_stock, quantity_exceeded, coupon_invalid, coupon_expired, minimum_not_met,
maximum_exceeded, region_restricted, age_verification_required, approval_required,
unsupported, not_found, conflict, rate_limited, expired, intervention_required
```

Three of those are the post's fifth checklist row, already normative in the spec:
**`region_restricted`**, **`age_verification_required`**, **`approval_required`**.

Paired `resolution` enum, verbatim from the spec: "`recoverable`: agent can fix via API.
`requires_buyer_input`: buyer must provide info. `requires_buyer_review`: buyer must authorize."
Plus `severity`: info / low / medium / high / critical.

So the refusal path is not an afterthought a cautious commentator bolted on - **the protocol's
own authors modelled "no, a human has to do this" as a first-class response type.** Combined
with OpenAI's per-product `is_eligible_checkout` flag and Shopify's trust tiers, a merchant has
three independent primary-sourced places to say no: per product, per agent, per attempted order.

---

## Claim discipline for public copy

Safe to state as fact (all primary-verified above):

- No single universal agentic-commerce standard exists; three vendor-led specs overlap, at beta /
  unversioned / v0.2 maturity.
- ACP is `beta`, maintained by OpenAI and Stripe.
- The merchant, not the agent platform, is merchant of record and owns refunds and chargebacks
  (OpenAI, verbatim).
- Schema.org `Offer` already carries price, currency, availability, eligibility, shipping and
  return-policy fields - and is a vocabulary, not a transaction interface.
- Being callable is not being authorized; AP2 exists specifically to supply cryptographic proof
  of user authorization, and distinguishes Human Present from Human Not Present.
- The ACP checkout spec already defines `region_restricted`, `age_verification_required` and
  `approval_required` decline codes, and a `requires_buyer_review` resolution.
- W3C VC Data Model 2.0 is a Recommendation (15 May 2025).
- x402 is scoped by its own docs to machine-to-machine API/resource payments, not physical-goods
  commerce.
- Visa Intelligent Commerce is, in Visa's own words, "in the process of development and
  deployment."

Must **not** be claimed:

- That agents are already a dominant customer type. **No adoption, volume or revenue figure was
  verified, so none appears anywhere in the post, caption or visual.**
- That every business needs agent checkout today.
- That an agent can or should autonomously buy regulated, high-risk, age-restricted, contractual,
  medical, financial or irreversible goods.
- That any of these protocols is settled infrastructure.
- That ACP's delegate-authentication spec is an OAuth delegation mechanism (it is 3DS2).

## Excluded - surfaced but not used in public copy

- **Mastercard Agent Pay / Agentic Tokens.** Only secondary write-ups (eco.com, nmi.com) were
  reachable; no primary Mastercard developer page was verified. Excluded entirely.
- **x402 transaction and volume figures** ("119M transactions on Base", "~$600M annualized").
  Appeared in a search summary attributed to third-party sites, not traced to a primary Coinbase
  or x402 Foundation document. Excluded.
- **"10M+ domains implement schema.org Offer".** Appeared in a fetched summary; not verified in a
  citable Google or schema.org document. Excluded.
- **Google Merchant Center product data specification.** Directly relevant but not fetched in
  this pass; schema.org `Offer` and Google's merchant-listing structured-data docs cover the same
  ground and were verified.
- **AP2 "Intent Mandate / Cart Mandate" terminology.** This is v0.1-era naming that still
  circulates in blog posts. The current primary spec and glossary use **Checkout Mandate** and
  **Payment Mandate**, each open/closed. Public copy uses the current names only.
- **All agentic-commerce "readiness checklist" blog posts** (digitalapplied, charle, paz.ai,
  chargeflow, ucphub). Not primary; not cited; the checklist in this post is derived from the
  specs above.
- **Regulatory claims about 2026 FTC / "AI AGENT Act" rules.** Only blog-level sources surfaced.
  Excluded; the post's regulatory caution is framed as merchant prudence, not as citing law.

## Primary sources

- Agentic Commerce Protocol: https://www.agenticcommerce.dev/
- ACP repository (status `beta`, governance, dated spec versions): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
- ACP 2026-04-17 OpenAPI specs (checkout, webhook, cart, feed, delegate payment, delegate authentication): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/tree/main/spec/2026-04-17/openapi
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
- Shopify, Catalog MCP server: https://shopify.dev/docs/agents/catalog/mcp
- schema.org Offer: https://schema.org/Offer
- Google, merchant listing structured data: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- Google, return policy structured data: https://developers.google.com/search/docs/appearance/structured-data/return-policy
- GS1 Digital Link: https://www.gs1.org/standards/gs1-digital-link
- GS1-Conformant Resolver standard: https://ref.gs1.org/standards/resolver/
- W3C Verifiable Credentials Data Model 2.0 (Recommendation, 15 May 2025): https://www.w3.org/TR/vc-data-model-2.0/
- Coinbase, x402 / HTTP 402 (optional M2M example only): https://docs.cdp.coinbase.com/x402/core-concepts/http-402
- Visa Intelligent Commerce (developer documentation): https://developer.visa.com/capabilities/visa-intelligent-commerce
