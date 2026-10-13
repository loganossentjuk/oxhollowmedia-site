# Growth plan: print-shop input (shop-manager, 2026-10-13)

Input for the print-shop half of `team/drafts/growth-strategy.md`. Read-only work: nothing in Shopify, Gelato, prices or the catalog was changed. There are no sales figures in this file; the manager has the sales snapshot separately. All sources were read on 2026-10-13. A number marked **(unverified)** comes from a search summary only, because the page itself blocked the fetch.

---

## 1. Which prints to lead with (ads, gift guides, Pinterest)

The picks below reason from `prints/catalog.json` only. There's no sales history to rank by yet, so the criteria are:

- **The full framed ladder.** Framed print and framed canvas at 8x12, 12x18, 16x24 and 24x36. One ad can then show a $115 gift and a $315 statement piece.
- **High-res source.** `source_px` of 6000 or more.
- **On brand.** Ocean, mountains and wildlife, with a place Logan has confirmed in BUSINESS.md.
- **Portrait orientation for Pinterest.** Pinterest recommends 2:3 (1000 x 1500), and wider Pins "might get cut off in people's feeds" ([Pinterest product specs](https://help.pinterest.com/en/business/article/pinterest-product-specs)).

All 65 prints have framed mockups in `previews`, so every pick below already has ad-ready framed imagery.

**Catalog snapshot:**
- 28 prints reach 24x36, 18 have three sizes, 1 has two, and 18 are 8x12 only (2000 px files).
- By category: 24 mountains, 14 ocean, 9 botanical, 9 urban, 6 wildlife, 3 embers.

| Role | Print (slug) | Why | Lead size / material |
|---|---|---|---|
| Hero ad, ocean | Dawn Patrol (`dawn-patrol`) | Top of the gallery wall, 12000 px, full framed ladder, surf silhouette reads at thumbnail size | Framed print 12x18 ($155) and 16x24 ($205) |
| Hero ad, mountains | Valley in Violet (`valley-in-violet`), Snowline (`snowline`) | Eastern Sierra (confirmed), batch 1, full ladder, 6000 px | Framed print 16x24 ($205); framed canvas 16x24 ($195) |
| Pinterest lead (portrait) | Fog Forest (`fog-forest`) | Portrait, 12000 px, every material and size, Seattle (confirmed) | Framed canvas 16x24 ($195), walnut or oak mockup |
| Pinterest lead (portrait) | Aspen and Cobalt (`aspen-and-cobalt`) | Portrait, full ladder, Colorado (confirmed), autumn colour fits the Oct–Nov feed | Framed print 12x18 ($155), oak |
| Local / Bay Area gift guide | Golden Gate, Fog (`golden-gate-fog`) | The one unmistakably SF image; portrait 2:1. Reaches 16x24 only | Framed print 12x18 ($155) |
| Story-led gift (journal tie-in) | Blue-Footed Booby, Humpback Breach, Sea Lion Pup | Galápagos 2021 (confirmed). Journal entry 1 is about them. 8x12 only (2000 px) | Framed print 8x12 ($115): the "gift-sized" price point |
| Set / bundle | Ember Study, Rising Flame, Sparks (`embers`) | A natural triptych, all three with the full ladder; winter and fireside mood | Three framed 8x12 or 12x18 (see offer B) |
| Square Pins / Instagram grid | Harbour, Pastel (`harbour-pastel`) | The only square print; 12x12 to 20x20, plus 24x24 framed canvas | Framed canvas 12x12 ($130) |

**Avoid in paid placements for now:**
- **Verdigris and Copper and Teal.** GELATO-FRAMED.md says they're held until their print files are re-made, although the catalog now lists framed sizes for both. Logan should confirm their status before either is promoted.
- **8x12-only prints as hero ads.** A hero ad needs the size ladder these can't offer.

## 2. How our prices compare (framed and canvas)

Ox Hollow prices, from `gelato.prices`:

| Material | 8x12 | 12x18 | 16x24 | 24x36 |
|---|---|---|---|---|
| Paper | $35 | $50 | $55 | $70 |
| Framed print | $115 | $155 | $205 | $315 |
| Framed canvas | $125 | $150 | $195 | $330 |

Free US shipping on every print (`shipping-returns.html`). Open edition.

| Seller | What | 16x24 | 24x36 | Other terms | Source |
|---|---|---|---|---|---|
| **Ox Hollow** | Paper / framed print / framed canvas | $55 / $205 / $195 | $70 / $315 / $330 | Free US shipping | catalog |
| Opensky (Zenfolio) | Fine art paper / canvas wrap / metal | $149 / $249 / $299 | $249 / $349 / $399 | Price includes printing, shipping and tax. No framed option listed | [opensky.zenfolio.com/prints](https://opensky.zenfolio.com/prints) |
| Carly Tabak (landscape, Sierra) | Unframed / framed print / framed canvas (same price framed or canvas) | $350 / $750 / $750 | $500 / $1,050 / $1,050 | 8x12: $150 unframed, $375 framed. Free contiguous-US shipping. A 30%-off code was advertised on the page | [product page](https://www.carlytabakprintshop.com/products/sierra-stillness) and its public `.json` variant list |
| Clark Little (ocean, Hawaii) | Open-edition matte paper / unstretched canvas / framed metal | $175 / $450 / $1,200 | $285 / $850 / $1,600 | Free US shipping on orders of $99.75–$1,000.99. Limited editions (runs of 95) $600–$1,150 | [prices and shipping](https://clarklittlephotography.com/pages/prices-shipping) |
| Fine Art America (marketplace, "Sierra Nevada" framed) | Framed print, starting prices (size not stated) | $69–$120 list; $55–$96 during a 20%-off sale | | Marketplace floor | [fineartamerica.com](https://fineartamerica.com/shop/framed+prints/sierra+nevada) |
| Mpix (consumer photo lab) | Canvas of your own photo | from $59.99 | | Free standard shipping on orders of $45+. 30%-off sale advertised | [mpix.com canvas](https://www.mpix.com/wall-art/canvas-prints) |
| Joseph Filer (landscape, limited edition) | Paper | from $295 **(unverified)** | | Page returned 403 | [josephfiler.com](https://www.josephfiler.com/gallery/california-landscape-photography/) |
| Richard Wong (California landscape) | Print | from $350 **(unverified)** | | Page returned 403 | [rwongphoto.com](https://www.rwongphoto.com/gallery/california-pictures/) |

**What the table shows:**
- **We sit between the marketplace floor and independent photographers.**
  - Our framed 8x12 ($115) costs about a third of Carly Tabak's ($375).
  - Our framed 16x24 ($205) costs less than Opensky's unframed canvas wrap ($249).
  - Our paper prices are a fraction of every independent seller's.
- **This fits the "$$, affordable" brief.** The ad message can be "original fine art at a fair price, framed, shipped free" rather than a discount.
- **Discounting is everywhere this autumn.** Carly Tabak (30%), Mickey Shannon (20%, [mickeyshannon.com](https://www.mickeyshannon.com/)), Fine Art America (20%) and Mpix (30%) all advertised fall sales on the day I read them. Our list prices are already below most of their sale prices, so a holiday markdown isn't needed to compete. Margin is better protected with non-price offers (section 3).
- **Possible price test later.** The gap at 16x24 and 24x36 framed suggests room for one, but that's Logan's call once sales give a baseline. No change is recommended now.

## 3. Holiday offers that don't change prices (each needs Logan's approval)

**A. Gift-deadline banner (Logan approves wording and date).**
- **Wording:** a single line on `/gallery`, `/prints` and print pages: "Order by [date] for delivery before December 25 (US)."
- **Date:** use Gelato's 2026 last-order date only (section 4).
- **Go-live:** early November.
- **After the cut-off:** swap it for the gift-card line (offer C).
- **Pinterest timing:** Pinterest says self-gifting wishlists build from October and peak in November, and gift ideas for others surge in December ([Social Media Today on Pinterest's holiday guidance](https://www.socialmediatoday.com/news/pinterest-shares-holiday-marketing-tips-2025/759551/)).
- **Cost:** none.

**B. Embers set, or a "pair" link (Logan approves, and creates a discount if he wants one).**
- **The link:** a Shopify cart permalink can hold several variants and apply a code, for example `/cart/<v1>:1,<v2>:1,<v3>:1?discount=CODE` ([Shopify cart permalinks](https://help.shopify.com/en/manual/products/details/cart-permalink)).
- **What the site could offer:** "Buy the set" on Ember Study, Rising Flame and Sparks, or on a pair such as the two Eastern Sierra prints. No bundle app is needed.
- **No discount needed.** With no code, prices are unchanged. If Logan wants a sweetener, a code like 10% off the set is his decision, and only he can create it in Shopify.
- **Margin check:** see section 5. Three framed 12x18 at 10% off still leaves about $220 contribution.

**C. Digital gift cards for the last-minute buyer (Logan approves and enables).**
- **Availability:** "Gift cards are available on all Shopify subscription plans," including our Basic plan ([Shopify help](https://help.shopify.com/en/manual/products/gift-card-products/overview)).
- **Why it helps:** it sells after the Gelato shipping cut-off and has no fulfilment cost until redeemed.
- **Suggested denominations:** $115 (one framed 8x12), $155 and $205, matching the framed price ladder.
- **Logan's steps:** enable gift cards in Shopify, then the site links a gift-card variant.

**D. "Free US shipping, framed and ready to hang" as the headline (Logan approves the ad copy).**
- We already ship free on every print, so a free-shipping threshold offer doesn't apply.
- Put the existing free shipping in every ad and gift guide instead. Clark Little and Carly Tabak both feature it.
- **Cost:** none.

**E. Gift guide by price point (Logan approves the selection).**
- **Under $125:** framed 8x12. Galápagos trio, Golden Gate, Fog.
- **Under $210:** framed 16x24. Dawn Patrol, Valley in Violet, Fog Forest.
- **Statement:** framed 24x36. Dawn Patrol, Snowline.
- Pinterest recommends boards organised by recipient, interest or price point (same source as A).
- One `/gifts` page or a section on `/prints`; the web engineer builds it from the catalog.

## 4. Gelato 2026 US holiday last-order dates

- **Not published publicly as of 2026-10-13.** Gelato's page at [gelato.com/order-deadlines](https://www.gelato.com/order-deadlines) is still headed "Holiday order deadlines 2025" and says the dates will be posted when ready **(unverified: the page returned 403 behind a bot check, so this comes from search summaries)**.
- **Action:** Logan should check the Gelato dashboard, or that page from mid-November.
- **Context only, not Gelato's cut-off:** the USPS 2026 recommended send-by dates for the contiguous US are Ground Advantage Dec 17, Priority Mail Dec 18 and Priority Mail Express Dec 19 ([USPS](https://www.usps.com/holiday/holiday-shipping-dates.htm)).
  - Gelato adds production days before handing parcels to a carrier, and may use other carriers.
  - So Gelato's framed-print date will be earlier than these.
  - Don't put a USPS date on the site as our deadline.

## 5. Rough ad economics (from catalog prices; no sales data)

**Assumptions:**
- **Gelato cost.** `gelato.prices` for framed and paper were set by `gelato_publish.py --quote`: Gelato's US cost (item plus cheapest shipping, dearest frame colour) × 2.5, rounded up to $5. So cost ≈ price / 2.5 (upper bound; true cost sits between (price − 5)/2.5 and price/2.5). Shipping is inside that cost because we ship free.
- **Card fees.** Shopify Basic online card rate: 2.9% + $0.30 ([Shopify pricing](https://www.shopify.com/pricing)). Subscription and tax are excluded.
- **Formula:** break-even cost per purchase (CPA) = price − price/2.5 − (0.029 × price + 0.30) = 0.571 × price − 0.30.
- **Canvas, wood and acrylic** are excluded because their prices weren't set by this rule, so their cost is unknown here. Logan can check them in Gelato.

| Item | Retail | Est. Gelato cost (incl. shipping) | Card fee | **Break-even CPA** | CPA at 50% of margin |
|---|---|---|---|---|---|
| Paper 8x12 | $35 | $14.00 | $1.32 | **$19.68** | $9.84 |
| Paper 24x36 | $70 | $28.00 | $2.33 | **$39.67** | $19.84 |
| Framed 8x12 | $115 | $46.00 | $3.63 | **$65.36** | $32.68 |
| Framed 12x18 | $155 | $62.00 | $4.79 | **$88.20** | $44.10 |
| Framed 16x24 | $205 | $82.00 | $6.25 | **$116.75** | $58.38 |
| Framed 24x36 | $315 | $126.00 | $9.44 | **$179.56** | $89.78 |
| Framed canvas 8x12 | $125 | $50.00 | $3.92 | **$71.08** | $35.54 |
| Framed canvas 16x24 | $195 | $78.00 | $5.96 | **$111.05** | $55.52 |
| Framed canvas 24x36 | $330 | $132.00 | $9.87 | **$188.13** | $94.06 |

Worked example, framed 16x24: $205 − $82.00 − ($5.95 + $0.30) = $116.75.

**Average order value range (single item, from catalog prices):**
- **Whole shop:** $35 (paper 8x12) to $330 (framed canvas 24x36).
- **Likely AOV for framed-led ads:** $115–$205, the 8x12 to 16x24 framed sizes most gift buyers would pick. That's an assumption until there are orders.
- **Planning figure:** at a $155 midpoint (framed 12x18), break-even CPA is about $88, and a CPA of about $44 keeps half the margin.

**Implications:**
- **Advertise framed, never paper alone.** Paper's break-even CPA ($20–$40) is too thin for paid social.
- **The Embers set (offer B), three framed 12x18:**
  - At $465 with no discount, contribution ≈ $465 − $186 Gelato − $13.79 fee = $265.
  - With a 10%-off code ($46.50 off), it's ≈ $418.50 − $186 − $12.44 = $220. That's still above a single 16x24 framed sale.
- **Gift cards (offer C)** carry no product cost until redeemed, but the same margin applies once they are.
- The marketing-lead's CPC and conversion benchmarks can be checked against these CPA ceilings. For example, at a 1% conversion rate, break-even CPC for a $155 order is $0.88. That's illustrative arithmetic, not a forecast.

## Sources (all read 2026-10-13)

**Opened directly:**
- https://opensky.zenfolio.com/prints
- https://clarklittlephotography.com/pages/prices-shipping
- https://www.carlytabakprintshop.com/products/sierra-stillness (plus the public `.json` for variant prices)
- https://fineartamerica.com/shop/framed+prints/sierra+nevada
- https://www.mpix.com/wall-art/canvas-prints
- https://www.mickeyshannon.com/ (fall promo only)
- https://www.usps.com/holiday/holiday-shipping-dates.htm
- https://www.shopify.com/pricing
- https://help.shopify.com/en/manual/products/gift-card-products/overview
- https://help.shopify.com/en/manual/products/details/cart-permalink
- https://help.pinterest.com/en/business/article/pinterest-product-specs
- https://www.socialmediatoday.com/news/pinterest-shares-holiday-marketing-tips-2025/759551/

**Search summary only (unverified; 403 or bot check):**
- https://www.gelato.com/order-deadlines
- https://www.josephfiler.com/gallery/california-landscape-photography/
- https://www.rwongphoto.com/gallery/california-pictures/
