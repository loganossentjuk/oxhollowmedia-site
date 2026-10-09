# Ox Hollow Media: business brief (every team member reads this first)

## What the business is
Ox Hollow Media is Logan Ossentjuk's one-person studio in the San Francisco Bay Area. It earns money three ways:

1. **Event photography and brand films**, mostly for tech companies in SF and the Bay Area. This is the biggest earner per job. The money pages are `/work-with-me`, `/events` and `/contact`.
2. **Fine-art prints** of ocean, mountains and wildlife, sold through Shopify and printed and shipped by Gelato:
   - framed print (black, white or oak), framed canvas (black, oak or walnut), unframed paper, wood and acrylic
   - one page per print at `/prints/<slug>`; the gallery is `/gallery`
   - prices live in `prints/catalog.json` under `gelato.prices`; framed prints run $115–$330 and paper $35–$70
3. **Documentary and conservation films**: `/films` and `/filmmaking`. These build the brand and bring in commissions.

The name: Logan means "little hollow" and Ossentjuk means "oxen yoke". Tagline: "Dare to see."
Instagram: @oxhollowmedia. Email: oxhollowmedia@gmail.com. Site: https://oxhollowmedia.com

## How the site works
- **Hosting:** a static site (HTML/CSS/JS) on Cloudflare Pages. A push to `main` deploys to production. Any other branch gets a preview URL. There's no build step for most pages.
- **Print pages:**
  - Generated from `prints/catalog.json` by `python3 scripts/build_print_pages.py`.
  - Never hand-edit `prints/*.html`. Change the catalog or the script, then rebuild.
- **Checkout:** print pages link to the Shopify cart (`https://sessjk-nj.myshopify.com/cart/<variantId>:1`).
- **Product scripts:**
  - `scripts/gelato_publish.py` creates Gelato/Shopify products. It runs on Logan's Mac only and the team never runs it.
  - `scripts/make_stripe_links.py` manages the old Stripe links. The team never runs it either.
- **Local preview:** `python3 -m http.server 8090` from the repo root.
  - Playwright and Chromium are preinstalled in cloud sessions (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`).
  - Cloud sessions usually can't load oxhollowmedia.com itself (proxy). Test the local copy.
- **Background docs:** `DEPLOY.md`, `SHOPIFY-SETUP.md`, `GELATO-FRAMED.md`.

## Voice
- Quiet, observant, outdoorsy, confident. Write in the first person ("I"), as Logan.
- Short sentences. Concrete places and light, not hype.
- No exclamation-mark marketing and no "stunning/breathtaking/elevate".
- Speak to tech-company event planners the way you'd speak to a professional peer.

## Hard rules (no exceptions)
- **Never invent facts:**
  - no fake clients, testimonials, awards, publications, numbers, gear or locations
  - if a fact isn't in this repo or confirmed by Logan, leave a `TODO(Logan): …` and list it in the report
- **Never change:**
  - prices
  - Shopify products (create, edit, publish, archive or delete)
  - Gelato templates
  - Stripe
  - DNS or Cloudflare settings
- **Shopify is read-only for the team:**
  - reading orders, products and analytics is fine
  - customer personal data never leaves Shopify and never goes into the repo or a report
- **Never post, email or message anyone outside the team.** Social posts, newsletters and outreach are drafts in `team/drafts/` for Logan to send.
- **Never push to `main` or merge.** All work goes on the weekly branch and into one pull request that Logan approves.
- **Never spend money or sign up for services.**
- **Research is required:**
  - Every recommendation that relies on outside knowledge (SEO practice, competitor pricing, trends, platform rules) cites its sources (URL + date read).
  - Prefer primary sources: Google Search Central, schema.org, MDN, web.dev, platform help centers.
- **Keep changes small and reviewable:** a few strong changes beat many weak ones.
