# Etsy launch plan: Ox Hollow Media prints (draft for Logan)

Prepared by shop-manager, 2026-10-23. Read-only work: nothing in Shopify, Gelato, Etsy, prices or the catalog was changed. The shop is https://oxhollowmediashop.etsy.com (empty at time of writing).

Logan's decisions this plan follows: **Etsy is a discovery channel and the site stays home base. Etsy prices sit about 10–15% above the site to cover fees.**

Companion file: `team/drafts/etsy-listings.csv` (slug, title, tags, description, price for the first 20 listings).

Sources were read on 2026-10-23. Several Etsy and Gelato pages return 403 to automated fetches. Where a fact comes from a search-result summary of an official page rather than the page itself, it's marked **(summary)**. Where it comes from a third-party page only, it's marked **(third-party)**.

---

## 1. Connecting Gelato to Etsy and listing every print

### 1a. What Logan has to do himself (the team can't do any of this)

1. **Finish Etsy shop setup in Shop Manager.** Gelato says you must finish Shop Manager setup and create at least one listing before connecting, or the shop won't open ([Gelato: connect Etsy](https://support.gelato.com/en/articles/8996451)). Shop setup includes:
   - **Payments:** bank account and tax ID (SSN or EIN) for Etsy Payments. This is a credential step: Logan only.
   - **Billing:** a card on file for Etsy fees.
   - **Shop policies:** a return policy is required on every physical listing for sellers outside the EU, even "no returns", and listings with no return policy may rank lower ([Etsy: return policies](https://help.etsy.com/hc/en-us/articles/7869401615255-How-do-I-Set-Return-Policies-on-My-Listings) (summary)). Recommended: mirror the site. Print-on-demand items are made to order, so: no returns for change of mind; free replacement if it arrives damaged or wrong, photo within 14 days (same wording as the site's print pages).
   - **About section and shop banner:** reuse the /about mission line and a Galápagos or Sierra image.
2. **Add Gelato as a production partner.** Shop Manager → Settings → Production partners → Add a new production partner. Name, location and a short description of how you work together. The name can be hidden from buyers behind a generic label such as "Print studio" ([Etsy: production partners](https://help.etsy.com/hc/articles/360000336547) (summary)). Gelato asks for this before connecting ([Gelato: connect Etsy](https://support.gelato.com/en/articles/8996451)).
3. **Connect the store in Gelato.** Gelato dashboard → Stores → Connect → Etsy, then approve Gelato's access to the Etsy account (OAuth; Logan only) ([Gelato: connect Etsy](https://support.gelato.com/en/articles/8996451)).
4. **Copy the new Etsy store's Gelato store ID** from the store page URL in the Gelato dashboard ([Gelato API from template](https://support.gelato.com/en/articles/8996064-creating-products-via-api-from-template), [Gelato developer guide](https://dashboard.gelato.com/docs/guides/create-product-from-template/) (summary)). It is a Gelato UUID, not the Etsy shop ID, and it is different from the Shopify store ID in the catalog (`e55c0c9f-…`).
5. **Make one Etsy shipping profile and one processing profile** before publishing. Etsy needs a shipping profile with an estimated delivery date to save a listing, plus a processing time ("Made to order") ([Etsy: processing times](https://help.etsy.com/hc/en-us/articles/115015588087-How-to-Set-Processing-Times-Processing-Profiles-and-Ship-By-Dates) (summary), [Etsy: create a listing](https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing) (summary)). Gelato puts a product on a free-shipping profile when "Free Shipping" is switched on ([Gelato: add products to Etsy](https://support.gelato.com/en/articles/8996452)). Recommended: free US shipping, matching the site, with the Gelato cost already inside the price.

### 1b. What Etsy requires on every listing

| Field | What to set | Source |
|---|---|---|
| Who made it / what is it | "I did", "A finished product", and production partner = Gelato. Etsy's Creativity Standards put this under **Designed by a seller**: an original design produced with a production partner, which must be disclosed | [Etsy Creativity Standards](https://www.etsy.com/legal/creativity) (summary); [Etsy: production partners](https://help.etsy.com/hc/articles/360000336547) (summary) |
| When was it made | "Made to order" | [Etsy: create a listing](https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing) (summary) |
| Category | Art & Collectibles → Photography → Color (attributes: subject, room, orientation, framing) | Etsy listing form (verify in the form) |
| Title | ≤140 characters; shoppers see only the first few words in search, so put the keyword first; Etsy suggests under about 15 words | [Etsy: listing anatomy](https://www.etsy.com/seller-handbook/article/1347574487014) (summary); [Etsy: create a listing](https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing) (summary) |
| Tags | 13 tags, each ≤20 characters; letters, numbers, spaces, with ' and - allowed inside a tag | [Etsy: tags](https://help.etsy.com/hc/en-us/articles/360000336307-How-to-Use-Tags-to-Get-Found-in-Search) (summary) |
| Materials | e.g. "archival matte paper, wood frame, plexiglass" (from the catalog's framed blurb) | `scripts/gelato_publish.py` BLURB |
| Photos | Gelato mockups plus the real photo. Gelato allows up to 20 mockups per Etsy listing; its dashboard guide also cites 10. Use 5–10 in practice | [Gelato: Etsy limits](https://support.gelato.com/en/articles/8996461); [Gelato: add products](https://support.gelato.com/en/articles/8996452) |
| Shipping profile, processing profile, return policy | See 1a, items 1 and 5 | as above |
| Variations | Max **2** variation types, ≤70 values each, ≤400 combinations; attribute names ≤20 characters; SKUs ≤32 characters and **must not be edited** on Etsy once Gelato is connected | [Gelato: Etsy limits](https://support.gelato.com/en/articles/8996461); [Gelato: connect individual listings](https://support.gelato.com/en/articles/8996473-how-do-i-connect-individual-etsy-listings-to-gelato) |
| Price | $0.20–$50,000 per variant | [Gelato: Etsy limits](https://support.gelato.com/en/articles/8996461) |

Etsy's Creativity Standards allow photography printed by a partner, as long as the photograph is the seller's own and the partner is disclosed. Sources say undeclared partners are what get listings removed, not using one ([FinerWorks](https://support.finerworks.com/news/understanding-etsys-rules-for-print-on-demand-sellers/) (third-party)).

### 1c. Three ways to get the prints onto Etsy

| Route | How it works | Work for 65 prints | Verdict |
|---|---|---|---|
| **A. Gelato dashboard, one at a time** | Stores → Etsy store → Add product → pick product, variants, design. Products are saved as Etsy **drafts** (no $0.20 fee until published) ([Gelato](https://support.gelato.com/en/articles/8996452)) | ~65 × 2 listings by hand. Days | Only for the 2–3 "collection" listings (below) |
| **B. Gelato Bulk Operations: "Create Products from Template"** | Build one template product in the Etsy store (variants, mockups, pricing), export the CSV, fill one row per print (title, description, product UID, print-file URL), upload. Option to publish to the external store. "Cannot be undone" ([Gelato bulk templates](https://support.gelato.com/en/articles/10506835-how-to-create-products-in-bulk-using-templates)) | One template product per material × orientation, then one CSV. Hours | **Good fallback**, but it needs a public URL for every print file, and Logan doesn't keep full-res files public (the script uses a temporary tunnel instead). The article doesn't confirm Etsy support or say whether Gelato+ is required; check on the Bulk Operations page |
| **C. `gelato_publish.py` against the Etsy store ID** | The same `POST /stores/{storeId}/products:create-from-template` call the script uses for Shopify, with the Etsy store's ID. The guide says the storeId comes from the dashboard URL of whichever store you connect ([Gelato developer guide](https://dashboard.gelato.com/docs/guides/create-product-from-template/) (summary)) | One command per batch, about the same 5–60 min per listing as Shopify | **Recommended**, after a one-print test and the script change below |

**Can the existing templates be reused?** The nine "OHM … – Landscape/Portrait/Square" templates are account-level Gelato templates, and the script finds them by name. The create call only takes a `templateId` plus the store in the URL, so the same templates should work for the Etsy store. **Unverified:** Gelato's API docs returned 403. Test with one print first.

**Do not run the script as it is with the Etsy ID swapped in.** I read `scripts/gelato_publish.py`, and it is built for Shopify in ways that would break things:

1. **It writes into the site's cart data.** `record()` saves every created variant's `externalId` into `p["shopify"]` and moves the old ID to `retired_products`. With the Etsy store ID and `--replace`, it would overwrite the Shopify variant IDs the print pages link to, and the site's cart links would break.
2. **It would do nothing without `--replace`.** `todo()` skips any print that already has Shopify entries for every material, which is all 65.
3. **The listing text is Shopify-shaped.** Titles are "<Title> - Framed Print", tags are `["print", mat, category]`, and the description is HTML. Etsy needs the SEO titles, 13 tags and plain-text description from the CSV.
4. **Prices.** The script notes that "API ignores template prices", so listings are created hidden (on Etsy: drafts) at Gelato's default price. That's fine (no listing fee until published), but every variant then needs the Etsy price from section 2, set with Etsy's bulk price editor or the Gelato dashboard's pricing step, before publishing.

**Recommended change (web-engineer; Logan runs it):** add a `--store etsy` mode that:
- reads `gelato.etsy_store_id`;
- writes results to `p["etsy"]` / `p["etsy_products"]`, never `shopify`;
- decides what's to do by the `etsy` key;
- takes title, tags and description from `team/drafts/etsy-listings.csv`, with `isVisibleInTheOnlineStore: false`;
- defaults to `--materials framed,paper`.

Whether Gelato passes `tags` through to Etsy's 13 tag slots is **unverified**. If it doesn't, paste the tags with Etsy's bulk editor (Listings → select → Editing options).

**Production partner on API-made listings:** Printify's help centre says its listings default to "Made by seller" unless the partner already exists in the Etsy account ([Printify](https://help.printify.com/hc/en-us/articles/4578896595345) (third-party)). Gelato may behave the same way. After each batch, select the new listings in Shop Manager → Editing options → **Change production partners** → Gelato ([Etsy: production partners](https://help.etsy.com/hc/articles/360000336547) (summary)).

### 1d. The realistic plan

1. Logan does 1a (about 1–2 hours): payments, policies, production partner, Gelato connect, shipping and processing profiles.
2. Web-engineer adds `--store etsy` to the script (small, reviewable PR). Logan stores `etsy_store_id`.
3. **Test:** `python3 scripts/gelato_publish.py --store etsy --only international-orange --dry-run`, then the same without `--dry-run`. Check the Etsy draft for title, tags, variants, mockups and production partner, then set prices and publish.
4. **Batch 1 (the 20 in section 3), framed + paper only:** run, set prices with the bulk editor, assign the production partner in bulk, publish. 40 listings × $0.20 = **$8**.
5. **Collection listings** (Galápagos, Salt and Stone, Embers), made by hand in Etsy and connected variation by variation with "Connect to Gelato" ([Gelato](https://support.gelato.com/en/articles/8996473-how-do-i-connect-individual-etsy-listings-to-gelato)).
6. **Batches 2–3:** the other 45 prints, framed + paper. Framed canvas later, only if Etsy views justify it. Hold wood and acrylic: their Gelato cost isn't in the repo, so the Etsy margin can't be checked.

---

## 2. Pricing: site → Etsy

**Rule:** site price × 1.12, rounded to the nearest number ending in 5 or 9 that lands between +10% and +15%. Where nothing ending in 5 or 9 fits that band, the next one above +10% is used: paper 12x18 and 16x16 land at +10% ($55), and paper 16x24 at +18% ($65; the other option, $59, is only +7%).

**Etsy fees (US seller):**

| Fee | Rate | Source |
|---|---|---|
| Listing | $0.20 per listing, charged again on each auto-renew (after a sale or every 4 months) | [Etsy sell page](https://www.etsy.com/sell) (summary); [Craftybase 2026](https://app.craftybase.com/blog/the-complete-guide-to-etsy-fees) (third-party) |
| Transaction | 6.5% of item price + shipping + gift wrap | [Etsy: fees and taxes](https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy) (summary) |
| Payment processing (US bank) | 3% + $0.25 per order | [Etsy sell page](https://www.etsy.com/sell) (summary) |
| Offsite Ads | 15% of an attributed order if the shop made under $10k in the last 365 days (can opt out); 12% at or above $10k (mandatory). Capped at $100 per order | [Etsy: Offsite Ads](https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work) (summary) |
| Share & Save | **Minus** 4% back as a fee credit on orders that come through Logan's own shared links (Instagram, site), within 30 days of the click | [Etsy: Share & Save](https://help.etsy.com/hc/en-us/articles/16981332744087-How-to-Save-on-Etsy-Fees-with-the-Share-Save-Program) (summary) |

The current fees policy page (etsy.com/legal/fees) returned 403. The rates above match across Etsy's help pages and 2026 third-party guides. Sales tax is collected by Etsy as marketplace facilitator and isn't modelled here.

**Assumptions:**
- Free shipping on Etsy, as on the site, so the fees apply to the price alone.
- Gelato cost ≈ site price ÷ 2.5. That's the `--quote` rule from `team/drafts/growth-shop-input.md`, so it's an upper-bound estimate, and it includes Gelato's shipping. Gelato is assumed to charge the same for Etsy orders as for Shopify ones.
- Etsy fees = 9.5% × price + $0.45 (6.5% + 3% + $0.25 + $0.20 renewal).
- Site net = site price − cost − Shopify card fee (2.9% + $0.30).
- Wood and acrylic: price only. Their Gelato cost isn't in the repo.
- Plain canvas is retired on the site and isn't listed.

| Material | Size | Site | **Etsy** | Markup | Est. Gelato cost | Etsy fees | **Etsy net** | Site net | Offsite Ads fee (15%) | Etsy net if ad-attributed |
|---|---|---|---|---|---|---|---|---|---|---|
| paper | 8x12 | $35 | $39 | +11% | $14.00 | $4.16 | $20.84 | $19.68 | $5.85 | $14.99 |
| paper | 12x18 | $50 | $55 | +10% | $20.00 | $5.67 | $29.33 | $28.25 | $8.25 | $21.08 |
| paper | 16x24 | $55 | $65 | +18% | $22.00 | $6.63 | $36.38 | $31.11 | $9.75 | $26.62 |
| paper | 24x36 | $70 | $79 | +13% | $28.00 | $7.96 | $43.05 | $39.67 | $11.85 | $31.20 |
| paper | 12x12 | $40 | $45 | +12% | $16.00 | $4.73 | $24.27 | $22.54 | $6.75 | $17.52 |
| paper | 16x16 | $50 | $55 | +10% | $20.00 | $5.67 | $29.33 | $28.25 | $8.25 | $21.08 |
| paper | 20x20 | $60 | $69 | +15% | $24.00 | $7.00 | $37.99 | $33.96 | $10.35 | $27.64 |
| framed | 8x12 | $115 | $129 | +12% | $46.00 | $12.70 | $70.30 | $65.36 | $19.35 | $50.95 |
| framed | 12x18 | $155 | $175 | +13% | $62.00 | $17.07 | $95.93 | $88.20 | $26.25 | $69.68 |
| framed | 16x24 | $205 | $229 | +12% | $82.00 | $22.20 | $124.80 | $116.75 | $34.35 | $90.45 |
| framed | 24x36 | $315 | $355 | +13% | $126.00 | $34.18 | $194.82 | $179.56 | $53.25 | $141.57 |
| framed | 12x12 | $140 | $155 | +11% | $56.00 | $15.18 | $83.82 | $79.64 | $23.25 | $60.57 |
| framed | 16x16 | $175 | $195 | +11% | $70.00 | $18.97 | $106.03 | $99.62 | $29.25 | $76.78 |
| framed | 20x20 | $205 | $229 | +12% | $82.00 | $22.20 | $124.80 | $116.75 | $34.35 | $90.45 |
| framed_canvas | 8x12 | $125 | $139 | +11% | $50.00 | $13.65 | $75.34 | $71.08 | $20.85 | $54.50 |
| framed_canvas | 12x18 | $150 | $169 | +13% | $60.00 | $16.50 | $92.50 | $85.35 | $25.35 | $67.15 |
| framed_canvas | 16x24 | $195 | $219 | +12% | $78.00 | $21.25 | $119.75 | $111.05 | $32.85 | $86.90 |
| framed_canvas | 24x36 | $330 | $369 | +12% | $132.00 | $35.51 | $201.50 | $188.13 | $55.35 | $146.15 |
| framed_canvas | 12x12 | $130 | $145 | +12% | $52.00 | $14.22 | $78.78 | $73.93 | $21.75 | $57.03 |
| framed_canvas | 24x24 | $260 | $289 | +11% | $104.00 | $27.90 | $157.10 | $148.16 | $43.35 | $113.75 |
| wood | 8x12 | $80 | $89 | +11% | n/a | $8.90 | n/a | n/a | $13.35 | n/a |
| wood | 12x18 | $125 | $139 | +11% | n/a | $13.65 | n/a | n/a | $20.85 | n/a |
| wood | 16x24 | $160 | $179 | +12% | n/a | $17.45 | n/a | n/a | $26.85 | n/a |
| wood | 24x36 | $225 | $255 | +13% | n/a | $24.67 | n/a | n/a | $38.25 | n/a |
| wood | 12x12 | $105 | $119 | +13% | n/a | $11.75 | n/a | n/a | $17.85 | n/a |
| wood | 16x16 | $125 | $139 | +11% | n/a | $13.65 | n/a | n/a | $20.85 | n/a |
| wood | 20x20 | $165 | $185 | +12% | n/a | $18.02 | n/a | n/a | $27.75 | n/a |
| acrylic | 8x12 | $75 | $85 | +13% | n/a | $8.52 | n/a | n/a | $12.75 | n/a |
| acrylic | 12x18 | $100 | $115 | +15% | n/a | $11.38 | n/a | n/a | $17.25 | n/a |
| acrylic | 16x24 | $130 | $145 | +12% | n/a | $14.22 | n/a | n/a | $21.75 | n/a |
| acrylic | 24x36 | $210 | $235 | +12% | n/a | $22.77 | n/a | n/a | $35.25 | n/a |
| acrylic | 12x12 | $80 | $89 | +11% | n/a | $8.90 | n/a | n/a | $13.35 | n/a |
| acrylic | 16x16 | $100 | $115 | +15% | n/a | $11.38 | n/a | n/a | $17.25 | n/a |
| acrylic | 20x20 | $130 | $145 | +12% | n/a | $14.22 | n/a | n/a | $21.75 | n/a |

**What it shows:**
- **At +12%, an organic Etsy sale nets slightly more than a site sale.** Framed 12x18: $95.93 on Etsy vs $88.20 on the site. So Etsy is margin-neutral as a discovery channel.
- **An Offsite-Ads-attributed sale nets about 20–25% less than a site sale.** It's still profitable at every size: the worst case, paper 8x12, nets $14.99. Recommendation: **stay opted in** to Offsite Ads while under $10k. It's free reach, paid only on a sale, which fits the $0 ad budget. Revisit if most orders turn out to be attributed.
- **Paper 8x12 at $39** is the thinnest line ($20.84 net) but is the cheapest entry point in search. Keep it as a variant, not a hero.

---

## 3. What to launch first, and how to structure listings

### Structure

- **One listing per print per material: "Framed print" and "Paper print".**
  - Gelato templates are one material each, so the script produces exactly this.
  - Two listings per print also doubles the search entry points for $0.20.
- **Framed listing:**
  - Variation 1 **Size** (8x12 / 12x18 / 16x24 / 24x36, or the squares).
  - Variation 2 **Frame** (Black / White / Oak).
  - Price varies by size. 4 × 3 = 12 combinations, well under Etsy's 2-type, 70-value, 400-combination limits ([Gelato: Etsy limits](https://support.gelato.com/en/articles/8996461)).
- **Paper listing:** one variation, Size.
- Merging framed and unframed into one listing (Frame = Black / White / Oak / Unframed) is possible with Gelato's Expand Product tool or by connecting variations by hand ([Gelato: multiple products](https://support.gelato.com/en/articles/8996339-how-to-publish-multiple-products-with-your-design)), but it means manual work per print. Not worth it for launch.
- **Collections as shop sections.** Shop sections: Galápagos · Salt and Stone · Eastern Sierra · Pacific Northwest · Golden Gate & Bay · Embers · Botanical · Urban. These mirror the gallery's Collections menu.
- **Collections as "choose your print" listings (3, built by hand in Etsy, each variation connected to Gelato):**

| Listing | Variation 1 | Variation 2 | Combinations |
|---|---|---|---|
| Galápagos Wildlife Prints | Print (5) | Frame: Black / White / Oak / Unframed (all are 8x12-only files) | 20 |
| Salt and Stone, Oahu Abstracts | Print (3) | Size + frame, e.g. "12x18 Oak" (3 × 3 = 9 values) | 27 |
| Embers Campfire Series | Print (3) | Size + frame (4 × 3 = 12 values) | 36 |

Price varies by variation 2 only, which keeps pricing simple.

### Batch 1: the first 20 prints (framed + paper = 40 listings)

Chosen for Etsy search fit (a named place, landmark or species that people actually type), a full size ladder where possible, and the confirmed places in `team/BUSINESS.md`:

| # | Print | Why on Etsy | Sizes |
|---|---|---|---|
| 1 | International Orange | "golden gate bridge print" is a deep Etsy search; SF gift | to 16x24 |
| 2 | Paddler at the Gate | Second Golden Gate image; SUP niche | 8x12 |
| 3 | Dawn Patrol | Surf decor; 12000 px hero | to 24x36 |
| 4 | Valley in Violet | Eastern Sierra; full ladder | to 24x36 |
| 5 | Sierra Snowline | Sierra snow, ski-cabin gifts in winter | to 24x36 |
| 6 | Into the Unknown | Bishop, CA (confirmed) | to 16x24 |
| 7 | Drift and Timber | PNW foggy forest: a strong Etsy decor style; 12000 px | to 24x36 |
| 8 | Misty Ridgeline | PNW layered mountains | to 24x36 |
| 9 | Rainier Afterglow | "mount rainier print": named peak | 8x12 |
| 10 | Aspen and Cobalt | Colorado aspen, fall | to 24x36 |
| 11 | Obsidian Palace | Hawaii / Oahu; Salt and Stone lead | to 16x24 |
| 12 | Phase Shift | Salt and Stone | to 16x24 |
| 13 | Divine Duality | Salt and Stone; "teal and copper" decor | to 16x24 |
| 14 | Salt and Scales | Marine iguana; 8064 px, the only Galápagos print that reaches 24x36 | to 24x36 |
| 15 | Leviathan's Leap | Humpback whale: a big Etsy niche | 8x12 |
| 16 | Blue-Footed Display | Blue-footed booby: giftable, funny-bird niche | 8x12 |
| 17 | Shark Shadow | Shark / diver gifts | 8x12 |
| 18 | Tidal Twilight | Cape Cod (from the lede); New England coastal | to 24x36 |
| 19 | Embers, Flame | Cabin / fireplace decor, winter | to 24x36 |
| 20 | Hydrangea, Deep Blue | Botanical: Etsy's floral wall-art demand | to 24x36 |

- **Batch 2:** Sun on the Tide, Sea Lion Siesta, Embers Flicker/Scatter, River to the Range, Scrub and Snow, Mountain Majesty, Pastel Harbor (square), Autumn Flare, Autumn Against Blue, Forest Fungus, Turquoise Shallows, Petunia Blush, Geranium White, Glass Spire.
- **Batch 3:** the rest.
- **Hold:** none of the 20 is blocked. Batch 2/3 needs a check on any print whose place isn't confirmed (Highland Hollow: BUSINESS.md lists "Highland River" under Seattle, but the 2026-10-16 entry says Scotland).

---

## 4. Etsy SEO kit: first 20 prints

All 20 are also in `team/drafts/etsy-listings.csv`. Each description there ends with the same product line: "Printed in full on archival matte paper, never cropped, in a black, white or oak frame or unframed. Made to order."

Checks on the kit:
- Every title is ≤140 characters (93–111).
- Every listing has exactly 13 tags, each ≤20 characters.
- Openers use only catalog alt text and ledes plus the places in BUSINESS.md.
- "Galapagos" is written without the accent in titles and tags, which is how buyers type it. Descriptions keep "Galápagos".
- For the paper listing, swap "Framed" in the title for "Unframed" or "Art Print", and swap the "framed photo print" tag for "unframed art print".

TODO(Logan) before publishing:
- **Dawn Patrol:** the alt text says "sunset sky". Titles and tags avoid both "sunrise" and "sunset".
- **Shark Shadow:** BUSINESS.md and the catalog say Galápagos **2019**, but commit `a42c554` says 2021. The kit uses 2019.
- **Rainier Afterglow, Paddler at the Gate, Hydrangea:** the places are from alt text (Rainier, Golden Gate) or left out (Hydrangea). Correct anything that's wrong.

**1. `international-orange`**  
Title: Golden Gate Bridge Print, International Orange, San Francisco Wall Art, Framed Fine Art Photography  
Tags: golden gate bridge, san francisco art, sf wall art, golden gate print, bay area gift, california wall art, bridge photography, fog photography, framed photo print, sf housewarming, fine art photo, san francisco print, karl the fog  
Opener: The Golden Gate Bridge rising into fog, shot from the water's edge. I'm a San Francisco Bay Area photographer, and this is my home water.

**2. `paddler-at-the-gate`**  
Title: Golden Gate Bridge Paddleboard Print, San Francisco Bay Wall Art, Framed Photography, Paddler at the Gate  
Tags: golden gate bridge, paddleboard art, sup wall art, san francisco print, sf bay photo, bay area gift, golden gate print, paddler gift, ocean wall art, framed photo print, california coast, water sports art, sf housewarming  
Opener: A paddleboarder crossing beneath the Golden Gate Bridge. One person, one board, and the whole bridge overhead.

**3. `dawn-patrol`**  
Title: Surfer Silhouette Print, Longboard Surf Wall Art, Dawn Patrol, Framed Ocean Photography, Beach House Decor  
Tags: surf wall art, surfer silhouette, longboard print, surf photography, beach house decor, ocean wall art, surfer gift, coastal wall art, framed surf print, golden hour surf, large surf print, surf decor, beach photo print  
Opener: A surfer holding a longboard at the water's edge, silhouetted against the sky. Dawn patrol is what surfers call the first session of the day.

**4. `valley-in-violet`**  
Title: Eastern Sierra Mountain Print, Valley in Violet, California Landscape Wall Art, Framed Fine Art Photography  
Tags: eastern sierra, sierra nevada print, mountain wall art, california mountain, mammoth lakes art, bishop california, landscape print, purple mountains, framed photo print, mountain photography, braided river, large wall art, hiker gift  
Opener: Violet light across the Eastern Sierra, with a braided river running below the range. I shot it in the Bishop and Mammoth Lakes country.

**5. `sierra-snowline`**  
Title: Sierra Nevada Snow Print, Sierra Snowline, Eastern Sierra Mountain Wall Art, Framed Landscape Photography  
Tags: sierra nevada print, eastern sierra, snowy mountain art, mountain wall art, california mountain, mammoth lakes art, winter mountain, ski cabin decor, landscape print, framed photo print, mountain photography, snow peak print, cabin wall art  
Opener: Fresh snow along a high ridgeline in the Eastern Sierra, California. I shot it in the Bishop and Mammoth Lakes country.

**6. `into-the-unknown`**  
Title: Bishop California Print, Eastern Sierra River Wall Art, Into the Unknown, Framed Mountain Landscape Photography  
Tags: bishop california, eastern sierra, sierra nevada print, river wall art, mountain wall art, california mountain, landscape print, framed photo print, owens valley, mountain photography, snowmelt river, hiker gift, large wall art  
Opener: Snowmelt finding its way through the valley near Bishop, California, with the range still holding onto winter. I shot it early, before the wind came up and put texture on the water.

**7. `drift-and-timber`**  
Title: Foggy Forest Print, Pacific Northwest Wall Art, Drift and Timber, Framed Misty Conifer Photography, Large  
Tags: foggy forest print, pacific northwest, pnw wall art, misty forest art, conifer forest, washington state, forest photography, moody forest decor, seattle wall art, framed photo print, evergreen print, cabin wall art, large forest print  
Opener: Fog drifting through tall conifer forest outside Seattle, Washington. Just the trees, the fog and the light coming through.

**8. `misty-ridgeline`**  
Title: Misty Mountain Print, Pacific Northwest Ridgeline, Blue Mountains Wall Art, Framed Landscape Photography  
Tags: misty mountain print, pacific northwest, pnw wall art, blue mountain art, washington state, seattle wall art, mountain wall art, moody landscape, layered mountains, framed photo print, mountain photography, cabin wall art, large wall art  
Opener: A forested ridgeline fading into blue evening mist, shot around Seattle, Washington. Each ridge a shade lighter than the one in front of it.

**9. `rainier-afterglow`**  
Title: Mount Rainier Print, Rainier Afterglow, Pacific Northwest Wall Art, Framed Mountain Photography, Washington  
Tags: mount rainier, mt rainier print, rainier wall art, pacific northwest, pnw wall art, washington state, seattle wall art, mountain wall art, pink sky print, framed photo print, mountain photography, national park art, volcano print  
Opener: Mount Rainier in silhouette against a pink and violet afterglow, shot from around Seattle.

**10. `aspen-and-cobalt`**  
Title: Colorado Aspen Print, Aspen and Cobalt, Fall Aspen Trees Wall Art, Framed Rocky Mountain Photography  
Tags: colorado aspen, aspen tree print, fall foliage art, rocky mountains, colorado wall art, autumn wall art, yellow aspen, mountain cabin art, landscape print, framed photo print, tree photography, fall decor print, colorado gift  
Opener: Yellow aspen and dark pine against a cobalt sky in the Colorado Rockies. Gold, green and blue, and nothing else in the frame.

**11. `obsidian-palace`**  
Title: Hawaii Tidepool Print, Obsidian Palace, Oahu Abstract Ocean Wall Art, Framed Lava Rock Photography  
Tags: hawaii wall art, oahu print, tidepool print, lava rock art, abstract ocean art, aquamarine wall art, hawaiian decor, ocean photography, volcanic rock, framed photo print, teal wall art, beach house decor, salt and stone  
Opener: Aquamarine water held in dark volcanic rock at the Mermaid's Pools on Oahu, Hawaii. I shot this from inside a cave as the waves crashed in.

**12. `phase-shift`**  
Title: Abstract Ocean Print, Phase Shift, Oahu Hawaii Water and Rock Wall Art, Framed Green Abstract Photography  
Tags: abstract ocean art, hawaii wall art, oahu print, green abstract art, water photography, lava rock art, hawaiian decor, copper green art, modern wall art, framed photo print, ocean photography, sea cave, salt and stone  
Opener: Green and white water sliding over dark rock, the color of weathered copper. Shot alongside Obsidian Palace at the Mermaid's Pools on Oahu, from inside a sea cave as the waves came in.

**13. `divine-duality`**  
Title: Teal and Copper Abstract Print, Divine Duality, Oahu Hawaii Ocean Wall Art, Framed Abstract Photography  
Tags: teal and copper, abstract ocean art, hawaii wall art, oahu print, red rock art, teal wall art, hawaiian decor, modern wall art, water photography, framed photo print, lava rock art, sea cave, salt and stone  
Opener: Teal water against oxidized copper-red rock at the Mermaid's Pools on Oahu, Hawaii. Shot from inside a sea cave as the waves came in.

**14. `salt-and-scales`**  
Title: Marine Iguana Print, Galapagos Wildlife Wall Art, Salt and Scales, Framed Nature Photography, Large  
Tags: marine iguana, galapagos print, galapagos wildlife, iguana wall art, wildlife photography, reptile art, nature wall art, ecuador travel art, biology gift, framed photo print, large wall art, island wildlife, naturalist gift  
Opener: A marine iguana resting on sun-bleached rock in the Galápagos Islands. I shot it on a trip there in 2019.

**15. `leviathans-leap`**  
Title: Humpback Whale Print, Breaching Whale Wall Art, Leviathan's Leap, Galapagos Framed Ocean Photography  
Tags: humpback whale, whale breach print, whale wall art, galapagos print, ocean wildlife, marine life art, whale photography, ocean wall art, whale lover gift, framed photo print, nautical wall art, sea life print, beach house decor  
Opener: A humpback whale breaching in open blue water off the Galápagos Islands, 2019. I shot it on a trip there that year.

**16. `blue-footed-display`**  
Title: Blue Footed Booby Print, Galapagos Bird Wall Art, Blue-Footed Display, Framed Wildlife Photography  
Tags: blue footed booby, booby bird print, galapagos print, galapagos wildlife, bird wall art, bird photography, seabird print, birder gift, wildlife photography, framed photo print, funny bird art, ecuador travel art, nursery wall art  
Opener: A blue-footed booby mid-display in the Galápagos Islands, 2019. The feet really are that blue.

**17. `shark-shadow`**  
Title: Shark Print, Galapagos Underwater Wall Art, Shark Shadow, Framed Ocean Photography, Reef Wall  
Tags: shark print, shark wall art, galapagos print, underwater photo, reef wall art, ocean wildlife, marine life art, shark lover gift, scuba diver gift, framed photo print, blue ocean art, sea life print, beach house decor  
Opener: A shark gliding past a reef wall in the Galápagos Islands, 2019. Hazy blue water, a dark wall, and one shape moving through.

**18. `tidal-twilight`**  
Title: Cape Cod Marsh Print, Tidal Twilight, New England Coastal Wall Art, Framed Dusk Landscape Photography  
Tags: cape cod print, cape cod wall art, tidal marsh, new england art, coastal wall art, marsh photography, dusk landscape, beach house decor, massachusetts art, framed photo print, salt marsh print, coastal decor, large wall art  
Opener: Tidal marsh and still water under a warm dusk sky on Cape Cod. Still water, warm light, nothing moving.

**19. `embers-flame`**  
Title: Campfire Flame Print, Embers Series, Fire Photography Wall Art, Framed Dark Moody Cabin Decor  
Tags: campfire print, fire photography, flame wall art, cabin wall art, moody wall art, dark wall art, camping gift, fireplace decor, embers print, framed photo print, outdoorsman gift, abstract fire, lodge decor  
Opener: A single tongue of campfire flame rising against the dark. One campfire, three ways: this is the flame, between the wood and the sparks.

**20. `hydrangea-deep-blue`**  
Title: Blue Hydrangea Print, Hydrangea Deep Blue, Botanical Flower Wall Art, Framed Floral Photography, Large  
Tags: blue hydrangea, hydrangea print, botanical wall art, flower photography, floral wall art, blue flower print, garden wall art, cottage decor, mothers day gift, framed photo print, large floral print, flower close up, nature wall art  
Opener: Deep blue hydrangea blooms against lit green leaves. Close work, from the quiet end of my collection.

---

## 5. Strategy: where Etsy fits

**Roles:**
- **Site (home base):** best margin; the story pages; events and films live here; Instagram and Pinterest link here.
- **Etsy (discovery):** people searching "golden gate bridge print" or "galapagos wall art" who have never heard of Ox Hollow. Etsy's search weighs title, tags, attributes, description, first photo and reviews together ([Etsy: listing anatomy](https://www.etsy.com/seller-handbook/article/1347574487014) (summary)).
- **Instagram:** keep linking to the site. When a post is about a print that's on Etsy, a Share & Save link earns 4% back on fees ([Etsy](https://help.etsy.com/hc/en-us/articles/16981332744087-How-to-Save-on-Etsy-Fees-with-the-Share-Save-Program) (summary)), but site sales net more. Use Etsy links only for "find me on Etsy" stories.
- **Pinterest:** pin from the site. Etsy gets its own search traffic.
- **Reviews:** Etsy reviews are the trust signal the site lacks. After the first Etsy reviews arrive, Logan can decide whether to quote them on the site. They are real buyer reviews, but quoting needs his OK under the "never invent" rule.
- **Holiday:** Etsy has seasonal gift traffic. Etsy's 2026 shipping cutoffs and **Gelato's 2026 holiday order deadlines were not published** in anything I could find (as of 2026-10-23). A third-party guide gives carrier last-ship dates of USPS Ground Advantage Dec 17 and Priority Dec 19 ([shippinglabel.co](https://shippinglabel.co/seasonal/etsy-holiday-shipping) (third-party)). Gelato produces before handing over to the carrier, so its date will be earlier. Logan should check the Gelato dashboard in mid-November and set an Etsy shop announcement with the date.

**Competitive note:** Etsy Golden Gate photo listings show prices from about $30 (paper) and framed or canvas from about $48–$116 at unstated sizes ([Etsy market page](https://www.etsy.com/market/golden_gate_bridge_wall_art); individual listings captured 46–498 days ago, prices unverified). Our $129 framed 8x12 sits above the marketplace floor. That fits the "fine art, framed, free shipping" position, but expect paper to convert first.

### 30-day launch checklist

| When | Who | Task |
|---|---|---|
| Days 1–3 | Logan | Etsy payments, tax and billing; shop policies (returns as on the site); About and banner; production partner = Gelato; shipping profile (free US) and processing profile (made to order); connect Gelato (OAuth) |
| Days 1–3 | Logan | Approve Etsy prices (section 2) and this SEO kit |
| Days 3–5 | Web-engineer, then Logan | `--store etsy` mode in `gelato_publish.py` (PR); Logan runs a one-print test |
| Days 5–10 | Logan | Batch 1: 40 listings. Bulk-set prices, assign the production partner, publish ($8 in listing fees) |
| Days 5–10 | Logan | Shop sections; 3 collection listings by hand; shop announcement |
| Days 10–14 | Logan | Join Share & Save; put the Etsy shop link in the Linktree/bio as a secondary link; Offsite Ads: stay opted in |
| Days 14–21 | Logan | Batch 2 (about 18 prints). Rewrite titles on any listing with views but no favorites |
| Day 21 | Shop-manager | First Etsy review in the weekly report: views and favorites per listing; recommend title and tag swaps |
| Days 21–30 | Logan | Batch 3. Add the holiday cut-off to the announcement as soon as Gelato publishes it. Consider an Etsy sale for Cyber Week (Logan's call; not needed on price) |

### What to track weekly

| Metric | Where | Why |
|---|---|---|
| Visits and listing views (total and top 10 listings) | Etsy Stats ([Etsy: stats](https://help.etsy.com/hc/en-us/articles/115015774268-How-to-Use-Etsy-Stats-for-Your-Shop) (summary)) | Discovery is the point of the channel |
| Favorites per listing | Stats / listing | An early demand signal before orders |
| Orders, revenue, average order value | Stats; Orders CSV | Same aggregate-only rule as Shopify: no buyer names |
| Conversion rate (orders ÷ visits) | Stats | Etsy defines it per visit ([Etsy: stats glossary](https://help.etsy.com/hc/en-us/articles/115015628207-Shop-Stats-Glossary) (summary)) |
| Traffic sources (Etsy search vs social vs direct) | Stats | Shows whether Etsy is bringing new people |
| Search terms that brought visits | Stats | Feeds tag and title rewrites |
| Offsite Ads-attributed orders and fees | Stats / Payments CSV | Shows the margin effect |

**How the weekly report gets it:** there's no Etsy connector in this setup.
- **Option 1 (preferred):** Logan opens Shop Manager → Stats for the last 7 days and screenshots or copies the overview and top listings.
- **Option 2:** the manager reads Logan's open Stats page through Claude in Chrome. That's read-only, and only with Logan's OK each time, since it is his signed-in account.
- **For order and revenue numbers:** Shop Manager → Settings → Options → Download Data. Orders, listings and payments CSVs are available ([Etsy: download data](https://help.etsy.com/hc/en-us/articles/360035753053-How-Do-I-Download-My-Etsy-Data) (summary)). Stats (views, visits, conversion) are **not** in any CSV, so they come from the dashboard.
- Numbers stay out of committed files, as with Shopify.

---

## Sources (all read or searched 2026-10-23)

**Gelato (opened directly):**
- https://support.gelato.com/en/articles/8996451 (connect Etsy)
- https://support.gelato.com/en/articles/8996452 (add products to Etsy: drafts, free-shipping profile, mockups)
- https://support.gelato.com/en/articles/8996461 (Etsy limits: 2 variation types, 70 values, 400 variants, SKU 32 characters, $0.20–$50,000)
- https://support.gelato.com/en/articles/10506835-how-to-create-products-in-bulk-using-templates
- https://support.gelato.com/en/articles/8996064-creating-products-via-api-from-template

**Gelato (search summary only):**
- https://support.gelato.com/en/articles/8996473-how-do-i-connect-individual-etsy-listings-to-gelato
- https://support.gelato.com/en/articles/8996339-how-to-publish-multiple-products-with-your-design
- https://dashboard.gelato.com/docs/guides/create-product-from-template/ (403)

**Etsy (search summaries; pages return 403 to fetch):**
- https://www.etsy.com/legal/creativity
- https://help.etsy.com/hc/articles/360000336547 (production partners)
- https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy
- https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work
- https://www.etsy.com/sell
- https://help.etsy.com/hc/en-us/articles/16981332744087-How-to-Save-on-Etsy-Fees-with-the-Share-Save-Program
- https://help.etsy.com/hc/en-us/articles/360000336307-How-to-Use-Tags-to-Get-Found-in-Search
- https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing
- https://www.etsy.com/seller-handbook/article/1347574487014
- https://help.etsy.com/hc/en-us/articles/115015588087-How-to-Set-Processing-Times-Processing-Profiles-and-Ship-By-Dates
- https://help.etsy.com/hc/en-us/articles/7869401615255-How-do-I-Set-Return-Policies-on-My-Listings
- https://help.etsy.com/hc/en-us/articles/115015774268-How-to-Use-Etsy-Stats-for-Your-Shop
- https://help.etsy.com/hc/en-us/articles/115015628207-Shop-Stats-Glossary
- https://help.etsy.com/hc/en-us/articles/360035753053-How-Do-I-Download-My-Etsy-Data
- https://www.etsy.com/market/golden_gate_bridge_wall_art

**Third-party:**
- https://app.craftybase.com/blog/the-complete-guide-to-etsy-fees (2026 fee confirmation)
- https://support.finerworks.com/news/understanding-etsys-rules-for-print-on-demand-sellers/
- https://help.printify.com/hc/en-us/articles/4578896595345
- https://shippinglabel.co/seasonal/etsy-holiday-shipping
