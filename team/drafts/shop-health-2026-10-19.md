# Shop health: weekly check (2026-10-19)

Read-only review of Shopify (store sessjk-nj) against `prints/catalog.json`. Nothing was changed. No sales figures, order numbers or customer data are in this file.

## Result
- **Active products:** 255, all published (a check for ACTIVE-but-unpublished products returns none). There are no draft products.
- **Catalog match:** the catalog links to 255 distinct products and Shopify has 255 active. The count matches. I did not compare product IDs one by one this week.
- **Prices:** every active product's variant prices fall on a price in `gelato.prices`. I checked this by searching for any active variant priced between the catalog's price points, below the lowest or above the highest. All 30 searches returned zero. This is a screen, not a per-size check. The full per-variant check was done on 2026-10-14 (0 mismatches), and the product price ranges I sampled today still match.
- **Stray and legacy listings:** the four items flagged on 2026-10-14 are now ARCHIVED: `mural-sundown-acrylic-1`, `sun-on-the-water`, `marsh-at-dusk`, `cloudbreak-ridge`. The Gelato-default-price risk is gone.
- **Plain Canvas listings:** none are active now (they were 26 last week). Framed Canvas has 65 active listings.
- **Recent activity:** the newest edits to active products were on 2026-10-18 and are Framed Print listings. They look like a publish run, and I saw nothing wrong with them.

## Sample order
The International Orange acrylic sample order is paid and its fulfillment status is "in progress" (Gelato is producing it). Nothing to do until it ships. The sample discount code no longer turns up in a discount search, so there is nothing left to deactivate.

## Issues for Logan
None urgent. Two carry-overs:
1. **Low, catalog (team):** `petunia-blush` still lists `canvas` in `shopify` and `shopify_products`. That product is archived. Remove the entry on the next catalog edit (also in BACKLOG).
2. **Low, Logan's call:** the Before the Wind listings still use `autumn-flats-*` handles. Cart links work. Change them only if no URL has been shared.

## Not done this week
- **Market research:** none. No sources are cited because I made no outside claims.
- **Holiday ship cut-offs:** not looked up this run. The banner idea in BACKLOG still needs Gelato's published dates.
- **Per-product ID comparison and the publication check:** the connector lacks the `read_product_listings` scope, so I could not read publication status per product. The unpublished-product search is the only check available.
