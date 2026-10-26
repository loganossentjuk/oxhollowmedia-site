# Shop health: weekly check (2026-10-26)

Read-only review of Shopify (store sessjk-nj, Admin API 2026-10) against `prints/catalog.json`. Nothing in Shopify was changed. No sales, revenue or customer data is in this file; the sales snapshot goes in the PR body.

## Result
- **Listing health is clean.** Every ACTIVE product is published to the Online Store; there are no ACTIVE-but-unpublished products and no DRAFT products. No plain Canvas listing is live any more.
- **All four items flagged on 2026-10-14 are now fixed.** `mural-sundown-acrylic-1`, `sun-on-the-water`, `marsh-at-dusk` and `cloudbreak-ridge` are all ARCHIVED, and the correct "Sundown Silhouette - Acrylic" (`mural-sundown-acrylic-2`) is live. The plain Canvas listings are archived too. (This closes the Shopify item in the BACKLOG "Reminders for Logan"; it can be ticked.)
- **Price consistency: pass at product level.** The catalog agrees with `gelato.prices` in all 773 Shopify price entries and all 116 Etsy price entries (0 mismatches). In the live store, every ACTIVE product's lowest and highest variant price sits on the `gelato.prices` tier for its material and size set (framed, framed canvas, paper, wood, acrylic; the square Harbour Pastel set is also on its square tiers). No product shows a Gelato default (non-round) price. Limit of this check: it compared each product's min and max price, not all ~1,600 individual variants (the 2026-10-14 run did that and found 0 mismatches). A mid-range variant drifting would not show here.
- **Duplicates and strays:** none found among ACTIVE products (no repeated titles, no leftover old-name combined listings).
- **Discount codes:** the only code, OHM-SAMPLE-7Q4K, is now EXPIRED (single use, used once). No code currently active can sell below cost. One automatic app discount exists (see issue 2).

## Issues for Logan to fix in Shopify
1. **Sample order priced at Gelato cost: Info, no action.** The International Orange acrylic 16x24 sample order (#1001) was sold at exactly Gelato's unit cost using OHM-SAMPLE-7Q4K. That is below true cost once Gelato shipping and the card fee are counted, as expected for a sample Logan chose. Now fulfilled. Fix: none; just don't reuse at-cost codes for the public.
2. **Automatic app discount: Low, please look.** Shopify lists one automatic discount of type "app" (an installed app's discount function). The API doesn't show its rules. Fix: in Shopify admin, Discounts, open it and confirm it is intended and can't take a price under Gelato cost (framed 8x12 keeps $67, acrylic 8x12 keeps $47, so any deep percentage-off could erase the margin). Deactivate it if you don't recognise it.
3. **Odd handles on live products: Low, cosmetic.** Several products kept their old URL handle after the rename, for example `sunflare-oak-*` for Autumn Flare, `fog-forest-*` for Drift and Timber, `autumn-flats-*` for Before the Wind, `sun-on-the-water-framed-canvas` and `marsh-at-dusk-framed-canvas` for the Sun on the Tide and Tidal Twilight canvases. Titles are right and cart links use variant IDs, so nothing is broken. Fix: leave as is (changing handles can break shared links); only fix if no URL has been shared.
4. **Suffixes on handles ("-1", "-2"): Low.** Many framed print and some other handles end in -1 or -2 from earlier re-creations. The old products are archived, so these are not duplicates. Fix: none.

## Catalog notes (for the team, not Shopify)
- The BACKLOG still lists "Remove the archived Petunia Blush Canvas entry from the catalog" and the Shopify archive reminder as open. The Shopify side is done; the catalog entry removal is still a team task. Not changed here (only this file may be touched).
- The BACKLOG item "decide canonical set for duplicate -1/-2 Shopify products" appears resolved: no active duplicates remain.

## Etsy vs Shopify consistency (catalog only)
There is no Etsy connector in this session, so live Etsy listings were not checked; this covers what the catalog records.
- 20 prints carry an `etsy` block (paper and framed only), each with an `etsy_products` entry for both. Etsy prices match `gelato.etsy_prices` everywhere (0 mismatches).
- For every Etsy material, the sizes match the sizes offered on Shopify for that print.
- Etsy prices are deliberately higher than Shopify: paper by $4 to $24 and framed by $14 to $40, depending on size (for example 8x12 framed is $129 on Etsy and $115 on Shopify). Fine if intended to cover Etsy fees. A buyer who compares both will see the gap; Logan may want to confirm he is happy with it.
- Etsy offers only paper and framed print. Framed canvas, wood and acrylic exist on Shopify only, and Shopify still carries the framed-canvas margin leaders. No fix needed; just don't describe Etsy as the full range.
- `etsy_prices.framed` includes 24x36 at $355, but the Etsy listings recorded so far come from the small-file prints, so confirm 24x36 is only listed where the file supports it.

## Method
Shopify Admin GraphQL (read-only queries): product counts by status and publication, all ACTIVE products with min and max price, handle lookups for the four flagged legacy products, order and discount lookups, plus ShopifyQL sales queries (figures withheld from this file). Catalog checks ran locally in Python against `prints/catalog.json`.
