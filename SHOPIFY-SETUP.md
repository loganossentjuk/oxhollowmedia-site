# Shopify Store Setup — Ox Hollow Media

Goal: ship-to-order fine-art prints. Buyers click "Order this print" on
oxhollowmedia.com/store → land on your Shopify product page → check out →
a print partner prints and ships automatically. You never touch a package.

**Stack: Shopify Basic ($29/mo, usually $1/mo for the first 3 months) +
Prodigi (free Shopify app — fine-art print specialist: giclée, canvas,
framed; they print & ship each order automatically).**

Total setup ~45 minutes. Steps marked 🧑 need you (account/payment); steps
marked 🤖 Claude does once you're past the account wall.

---

## 1. 🧑 Create the store (~10 min)
1. Go to <https://www.shopify.com> → Start free trial.
2. Sign up with **oxhollowbooking@gmail.com**; store name **Ox Hollow Media**
   (URL will be something like `oxhollow-media.myshopify.com`).
3. Skip the questionnaire, pick the **Basic** plan when prompted
   (take the intro offer), add your payout bank details under
   **Settings → Payments** (Shopify Payments).

## 2. 🧑 Import the products (~5 min)
1. Admin → **Products → Import** → upload `shopify-products.csv`
   (in the repo root; all 20 products: 18 prints + the 2 mirror sets,
   images pull automatically from oxhollowmedia.com).
2. They import as **drafts** with price 0.00 — that's intentional;
   pricing comes after Prodigi is connected (step 3) so you can price
   above cost.

## 3. 🧑 Install Prodigi + map products (~20 min)
1. Admin → Apps → search **"Prodigi Print on Demand"** → Install (free).
2. In Prodigi, for each product choose the print type (their **Fine Art
   Prints / Giclée** range) and sizes you want to offer — Prodigi shows
   you the cost per size; set your retail price above it.
3. Prodigi asks for the print file per product: upload your full-res
   originals (Dropbox → Career/OxHollow, or ask Claude to stage the
   2000px web versions if you want to start immediately — full-res is
   better for large prints).
4. Set each product to **Active**.

## 4. 🤖 Wire the site (Claude, ~5 min)
Tell Claude the store is live and the `.myshopify.com` domain (or your
products' URLs). Claude fills `BUY_LINKS` in `store.html` so every
"Order this print" button opens the matching Shopify product page, and
deploys.

## 5. Optional polish (later)
- **Custom domain:** point `shop.oxhollowmedia.com` at Shopify
  (Settings → Domains; Claude can add the CNAME in Cloudflare).
- **Branding:** Claude can theme the Shopify checkout/product pages to
  match the site (Cormorant Garamond, ink/green palette).
- **Google Merchant Center:** free product listings on Google Shopping.

---

### Why not the alternatives
- **Fine Art America** (free) was the earlier recommendation and is still
  the zero-cost option, but its product pages are heavily FAA-branded and
  it can't live on your domain. Shopify + Prodigi costs $29/mo but the
  brand, customer relationship, and margins are yours.
- **Printful** does prints too but its catalog skews apparel; Prodigi is
  the art-print specialist (this is their core product).
