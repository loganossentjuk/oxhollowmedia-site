# Shop health check (2026-11-02)

Read-only review of Shopify (store sessjk-nj) against `prints/catalog.json`. Nothing in Shopify was changed. This file holds no sales figures and no customer data; those went to the manager in the reply.

## Result since 2026-10-14
- **Fixed since last check:** the four legacy listings Logan was asked to archive are gone from the active list (`mural-sundown-acrylic-1`, and the old combined `sun-on-the-water`, `marsh-at-dusk`, `cloudbreak-ridge`). No plain Canvas listing is active any more (all archived). Only the Paper and Framed Canvas listings remain for those prints.
- **Active vs published:** 325 products are ACTIVE, 0 are ACTIVE but unpublished. No DRAFT products.
- **Catalog links:** all 255 product IDs the catalog points at are ACTIVE. No catalog link goes to an archived product.
- **Duplicate titles:** none among the 250 products checked by title.
- **Titles:** every catalog-linked product is titled "<catalog title> - <material>".

## Price consistency vs `gelato.prices`
- Every catalog-linked product checked (250 of 255, by min and max variant price): 0 mismatches.
- The 70 newer Wood and Acrylic listings (below): all 145+ variants were checked one by one and match `gelato.prices` exactly (wood 80/125/160/225, acrylic 85/115/145/225).
- All of those variants have a Gelato unit cost set, and no price sits under its unit cost.

## Findings

### 1. 70 live Wood/Acrylic listings are not in the catalog (Medium, team fix, not Shopify)
Created 2026-10-29/30 (for example Blue Hour Ridge, Highland Hollow, Rainier Afterglow, Into the Unknown, Phase Shift, Divine Duality, Dawn Patrol, Valley in Violet; about 35 prints). They are live, priced correctly, and are not duplicates, but `prints/catalog.json` has no `wood`/`acrylic` entry for those prints, so the site never links to them. Until the catalog is updated they can be bought only by direct Shopify URL.
- Recommended fix: the team adds the wood and acrylic product IDs and variant IDs to the catalog, rebuilds the print pages, and re-runs the link QA. No Shopify change needed.

### 2. Automatic discount "Gelato quantity price breaks" (Low, Logan to confirm)
- It is an automatic app discount (ACTIVE since 2026-10-19, no end date, Product class). It has not been applied to any order yet.
- It cannot be combined with other product or order discounts, so it cannot stack with a code. It can combine with shipping discounts only.
- The Admin API shows no tier table or percentages (no metafields, and the function is not listed), so I cannot verify the discount stays above Gelato cost.
- Recommended fix: Logan opens the app in Shopify admin and checks that the largest quantity break leaves each print type above its "keep" figure in `team/BUSINESS.md`, and in particular above Gelato cost. For scale: Gelato's print cost is roughly 25 to 37% of the price for wood and acrylic (from `unitCost`), and the margin table shows 51 to 64% kept after shipping and fees. A break would need to be very large (roughly 40 to 50% off or more, before shipping) to push a sale to a loss, so a normal volume break should be safe, but that is an estimate until the tiers are checked.

### 3. Sample order used a code that sold at Gelato cost (Low, already closed)
- The only order on record used the OHM-SAMPLE one-use code and was priced exactly at Gelato's print cost, so after the card fee and free shipping it loses money. That was intended (Logan's own sample).
- The code is now status EXPIRED (used once, limit one). Nothing to do.
- The order has moved from "paid, waiting on Gelato" to fulfilled.
- No other code or order has gone under cost. Only that one code exists.

### 4. Catalog tidy-ups (team, no Shopify change)
- `petunia-blush` still lists `canvas` in `shopify` and `shopify_products` (the product is ARCHIVED). Remove it on the next catalog edit. (Same item as BACKLOG "Remove the archived Petunia Blush Canvas entry".)
- Before the Wind listings still use `autumn-flats-*` handles. Cart links work, so change them only if no URL has been shared.

## Fixes for Logan in Shopify
None are urgent this week. The archive tasks from 2026-10-14 are all done, so BACKLOG "Reminders for Logan" can drop the `mural-sundown-acrylic-1` / `sun-on-the-water` / `marsh-at-dusk` / `cloudbreak-ridge` / 26 Canvas line.
1. (Low) Check the tier table of the "Gelato quantity price breaks" app discount (finding 2).
2. (Optional) Nothing else. If you want the 70 unlinked listings off the shelf instead of in the catalog, archive them, but the better move is to link them (finding 1).

## Not covered this run
Market research and the holiday offer ideas were not requested this week, so they are not repeated here. Holiday gift deadline banner stays open in BACKLOG, pending Gelato's 2026 cut-off dates.
