# Shop health: post-rename check (2026-10-14)

Read-only review of Shopify (store sessjk-nj) against `prints/catalog.json`, after the 29-print rename and the International Orange rename. Nothing was changed. No sales figures or customer data are in this file.

## Result
- 279 products are ACTIVE and every one is published to the Online Store. No ACTIVE-but-unpublished products remain (the batch 2 framed listings and stray `-paper` duplicates flagged on 2026-10-09 are gone or fixed).
- **Titles:** every product the catalog links to (275 of 276) is titled exactly "<catalog title> - <material>". The rename landed everywhere the catalog points.
- **Prices:** all 1,615 variant IDs in the catalog were checked against the live store. 1,612 carry exactly the `gelato.prices` price; 0 mismatches. The other 3 are the archived Petunia Blush Canvas (below). Catalog prices are themselves consistent with `gelato.prices`.
- **Duplicate titles:** none.
- **Sample order:** Logan's International Orange acrylic 16x24 sample order exists, is paid and unfulfilled (it was placed today, so that is expected while Gelato produces it). The one-use code OHM-SAMPLE-7Q4K has a usage limit of 1 and has been used once, so Shopify will not accept it again. The code still shows status Active until it expires on 2026-10-21.

## Issues for Logan to fix in Shopify
1. **"Mural, Sundown - Acrylic" (handle `mural-sundown-acrylic-1`): High.** It is live, still has the old name, is not in the catalog, and sits at Gelato default prices ($50.06 to $143.61, well under the $75 to $210 catalog price). The correct listing is "Sundown Silhouette - Acrylic" (`mural-sundown-acrylic-2`). Fix: archive `mural-sundown-acrylic-1`.
2. **Legacy combined products "Sun on the Water" and "Marsh at Dusk" (handles `sun-on-the-water`, `marsh-at-dusk`): Medium.** Both are live under their old names and are not in the catalog. Each holds acrylic, canvas and wood variants at catalog prices, so nobody is overcharged. They duplicate the new "Sun on the Tide" and "Tidal Twilight" listings. Fix: archive both.
3. **Legacy combined "Cloudbreak Ridge" (handle `cloudbreak-ridge`): Low.** It is live and no longer in the catalog (the site now links the Cloudbreak Ridge paper and framed listings only). Prices are correct. Fix: archive it.
4. **Plain Canvas listings for prints that now have Framed Canvas: Low, Logan's call.** 26 prints (for example Drift and Timber, Misty Ridgeline, International Orange) still have a live plain Canvas listing. The site hides plain canvas when framed canvas exists, so these are only reachable from Shopify itself. Per GELATO-FRAMED.md step 4 they can be archived once framed is live. Petunia Blush Canvas has already been archived.
5. **Discount code OHM-SAMPLE-7Q4K: Low.** It is used up and can't be redeemed again. Optional: deactivate it now rather than waiting for the 2026-10-21 expiry, to keep the discounts list clean.

## Catalog tidy-up (for the team, not Shopify)
- `petunia-blush` still lists `canvas` in `shopify` and `shopify_products` (product 15418512212210, now ARCHIVED). The built page doesn't show it because framed canvas exists, but the entry is stale and should be removed on the next catalog edit.
- Carried over from 2026-10-09: the Before the Wind listings still use `autumn-flats-*` handles. Cart links work. Change them only if no URL has been shared.
