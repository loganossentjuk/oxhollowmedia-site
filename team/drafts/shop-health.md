# Shop health: weekly brief (2026-10-12)

Read-only review of Shopify (store sessjk-nj) against `prints/catalog.json` and `GELATO-FRAMED.md`. Nothing was changed in Shopify or Gelato. This file contains no sales, order or traffic figures; the snapshot goes to the manager in chat and to a file outside the repo.

Checks this week: every Shopify product (status, published or not, variant count, price range) compared with the catalog's `gelato.prices`; the product IDs the catalog links, checked for archived status; the catalog's own prices compared with `gelato.prices`. A full variant-by-variant check of every cart link was not repeated this week; last week's 162 sampled variant IDs all resolved, and no catalog product ID other than the one in issue 2 is archived.

## Resolved since 2026-10-09
- Verdigris Acrylic, Canvas and Wood (live at wrong prices): now archived. Verdigris Paper stays live and correct.
- The eight unpublished `-paper` duplicates at Gelato default prices: all archived.
- Batch 2 framed listings: priced at the catalog prices and published. The catalog now links framed print and framed canvas for 61 of 63 prints. The other two (Verdigris, Copper and Teal) also have live framed listings, which the catalog does not link yet (see issue 3).
- petunia-blush-canvas: archived (but see issue 2, the catalog still links it).
- No product is ACTIVE but unpublished, and no product is in draft.

## Price consistency
- Catalog vs `gelato.prices`: every variant price in `prints/catalog.json` matches `gelato.prices`. No mismatches.
- Shopify vs `gelato.prices`, at product level (min and max price per product): every live product the catalog links matches the tier for its material (paper, canvas, wood, acrylic, framed print, framed canvas), including the square prints (Harbour Pastel).
- Does not match: one live product, `mural-sundown-acrylic-1`, sits at Gelato default prices (see issue 1). Nothing else is off.

## Issues for Logan to fix in Shopify (or for the manager to fix in the catalog)
Urgency: High = customers can buy at the wrong price or hit a dead link now. Medium = confusing or incomplete, no wrong price. Low = tidy-up.

1. **mural-sundown-acrylic-1 (High).** ACTIVE and published at Gelato default prices, well below the catalog acrylic prices ($75 / $100 / $130 / $210). It is also a duplicate of the catalog's `mural-sundown-acrylic` (and there is a second duplicate, `mural-sundown-acrylic-2`, at the correct prices). Fix: archive `mural-sundown-acrylic-1`. It is not linked from the site, so only someone browsing the Shopify store directly could find it.
2. **Catalog links an archived product (High, manager fix).** The `petunia-blush` entry in `prints/catalog.json` still lists canvas variants under `shopify` and `shopify_products.canvas` (product 15418512212210, archived). If the print page still shows a canvas option, its cart link goes to an archived product. Fix: drop the canvas entry for petunia-blush from the catalog (framed replaces it per GELATO-FRAMED.md step 4), then rebuild with `python3 scripts/build_print_pages.py`. Check the live page after the rebuild.
3. **Live listings the catalog does not link (Medium).** These are ACTIVE, published and correctly priced, but the site cannot sell them until the catalog points at them:
   - Verdigris and Copper and Teal: framed print and framed canvas are live (published 2026-10-10). The catalog has no framed entry for either print, and the backlog still says they are held. Add the framed IDs, prices and previews, then rebuild. The backlog item "held until files are re-made" can be closed if Logan confirms the files were re-made.
   - Rising Flame and Sparks: paper, framed print and framed canvas are all live, but neither print is in the catalog at all. These look like new prints from Logan's photo review. They need catalog entries (title, category, alt text, story) before they appear on the site.
4. **A second set of "-1" / "-2" duplicate listings is live (Medium, needs a decision).** For eight prints there are two published sets: the catalog-linked set (3 sizes, up to 16x24) and a newer set with handles ending `-1` (or `-2`), created 2026-10-09 to 2026-10-10 and apparently with a 24x36 size added (12 variants instead of 9). Prices are right on all of them except issue 1. The eight prints are Shorebreak Boulders, Marine Iguana, Amber Glass, Hydrangea Deep Blue, Petunia Blush, Geranium White, Glass Spire and Mural Sundown, plus `harbour-pastel-framed-canvas-1` (adds the 24x24 size at $260). That is about 42 extra products. Two sets for one print is a stray-listing risk and doubles what a visitor to the Shopify store sees. Fix, Logan's choice:
   - If the newer sets are the intended ones (files re-made, 24x36 now available): the manager updates the catalog to the `-1` product and variant IDs and adds 24x36, rebuilds, and then Logan archives the older set.
   - If not: archive the `-1` and `-2` products.
   Either way, one set should be archived within the week. Nothing should be archived before the catalog and the choice agree, or live cart links break.
5. **Stray legacy combined products still live (Low).** `cloudbreak-ridge`, `marsh-at-dusk` and `sun-on-the-water` are ACTIVE and published as single products that mix canvas, wood and acrylic variants. The catalog links none of them (it uses their framed and paper listings). Fix: archive them once Logan confirms no wood or acrylic option for these prints is wanted; if it is, the catalog needs separate wood and acrylic products first.
6. **Handle and title mismatch for Sierra River Bend (Low, unchanged).** The live products carry the handles `autumn-flats-framed-print`, `autumn-flats-framed-canvas` and `autumn-flats-paper`. Carts work because the catalog uses product IDs. Changing a handle breaks shared links, so leave it unless no URL has been shared. `GELATO-FRAMED.md` still lists `autumn-flats` in batch 1; the catalog slug is `sierra-river-bend` (manager fix).
7. **Archived clutter (Low, unchanged).** Safe, nothing to do: the old Sierra River Bend sets, green-water-i, copper-and-teal and verdigris canvas, wood and acrylic, and the archived `-paper` duplicates. Archived items keep working URLs at no cost.
8. **"Default Title" variants on 8x12-only papers (Low, not re-checked this week).** Last week these showed "Default Title" instead of "8x12" (Banyan Light, Conifer Canopy, Palm Canopy and similar). Cosmetic only.

Stale check: apart from issues 3, 4 and 5, every ACTIVE product is linked from the catalog. Every catalog print has a live paper listing.

## Research: what to sell and how to offer it
Sources and dates read: all 2026-10-12 unless stated. Search tooling only returned summaries; the Gelato pages could not be fetched from this environment (DNS), so open each link before relying on a number or date.

**What sells.** The shop has no order history to read a best seller or a popular size from, so there is no evidence yet on which categories or price points win. Do not infer one. Marketing's plan should treat sales data as the first thing to collect (UTM links on every post, and a check of Shopify's Sales by product report after the first few orders). Until then the only defensible statements are about the range: 63 prints (mountains 25, ocean 14, botanical 9, urban 9, wildlife 6), paper from $35, framed prints from $115, framed canvas from $125, wood from $80, acrylic from $75. A Q4 art-print piece argues that holiday buying is driven by price point, so a spread of price points helps capture gift buyers and first-time buyers: https://aba.arthelper.com/print-on-demand/how-does-print-on-demand-help-artists-during-the-holiday-sea/ (vendor article, weak evidence).

**Gelato holiday cut-offs.**
- Gelato's own deadlines page still shows 2025 dates, so there is no official 2026 table in the search index: https://www.gelato.com/order-deadlines
- A Gelato Resource Center article dated 2026-10-06, "Holiday shipping deadlines: a practical plan for your store", may carry 2026 dates. Only the teaser was visible: https://www.gelato.com/resource-center
- Gelato's holiday tips post is general advice and gives no product cut-off: https://www.gelato.com/blog/holiday-shipping-tips
- Calendar facts for 2026 from third-party pages: Christmas is Friday, Dec 25. USPS suggests shipping by Dec 17 (Ground Advantage), Dec 18 (Priority Mail), Dec 19 (Priority Mail Express). Hanukkah runs Dec 4 to 12, earlier than usual. Sources (third party, confirm with carriers): https://via.delivery/blog/holiday-shipping-deadlines-2026 and https://textconnects.com/pages/holiday-shipping-deadlines
- Gelato adds production time before the carrier clock starts, so a store's order-by date must be earlier than a carrier date. Do not publish a date on the site until Logan reads the real 2026 US cut-off for framed prints and framed canvas from his Gelato dashboard, or from the 2026-10-06 article.

**Print-offer tactics found (vendor blogs; none gives hard benchmarks, so treat as ideas to test):**
- Framed-print bundles and gallery-wall sets, and "buy 2, get the 3rd free" style promotions: https://www.pictureit.co/blog/3-holiday-shopping-strategies-for-shopify-art-stores
- Black Friday for Shopify art stores: 10 to 30 percent off prints, front-page placement and limited runs. Read in the previous brief: https://www.pictureit.co/blog/3-black-friday-tactics-for-shopify-art-stores-in-2024
- Free-shipping threshold set just above the average order to nudge one more item. Framed prints are costly to ship, so check it against Gelato shipping cost first: https://www.gooten.com/blog/how-to-increase-your-average-cart-size-this-holiday-season/
- Bundles on Shopify: native bundling is limited; apps handle variant-level bundles. Logan would need to add an app (a decision and a possible cost; the team cannot): https://podvector.ai/articles/print-on-demand/strategy/how-to-create-holiday-collection-shopify-pod-products-fast . Printify on bundles and average order value: https://printify.com/knowledge-hub/shopify-product-bundling/
- Start holiday marketing early: https://www.customily.com/post/the-q4-personalized-product-playbook-for-print-on-demand-how-to-launch-with-customily-merchone
- Price comparables from last week still apply (read 2026-10-09): Opensky https://opensky.zenfolio.com/prints, Joseph Filer https://www.josephfiler.com/gallery/prints-and-framing/, Mark Gray https://blog.markgray.com.au/blog/pricing-landscape-photography-prints-a-complete-guide, The Print Space https://www.theprintspace.com/help-center/knowledge-base/how-to-price-your-online-art-prints/ . Ox Hollow framed and paper prices sit at or below the low end of them.

## Offer ideas for Logan to decide
1. **Clean the shelf first.** Resolve issues 1 to 4 before any promotion. A wrong-price listing or a dead cart link during a holiday push costs more than any offer earns. Also finish adding the live-but-unlinked prints (issue 3) so the gallery can show them.
2. **Holiday gift-deadline banner.** One line on `/gallery` and print pages: "Order by [date] for delivery before Christmas". Needs the confirmed 2026 Gelato date first. No discount, no invented date. Aim for early November. Also mention Hanukkah gifts need an earlier date (about three weeks before Christmas).
3. **"Gift wall" featured row.** Framed 8x12 ($115) and 12x18 ($155) as the gift-sized choice on the home page and `/gallery`, plus paper from $35 as the low-price entry point. Cost-free, no price change. Choose from prints with a clean listing.
4. **Matched pair or gallery-wall set (later).** Two or three related prints (the petunia or geranium prints; the Galápagos five) at a small fixed saving, using a Shopify discount Logan creates. Only after the cleanup, and only if margin holds against Gelato cost.
