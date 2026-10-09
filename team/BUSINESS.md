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

## Facts from Logan (2026-10-09). Use these and don't re-ask.
**Event services**
- **Usage:** once delivered, clients may use the photos however they like.
- **No deposit.** Don't mention one anywhere.
- **Overtime:** $250 per extra hour.
- **Rush jobs:** a $200 add-on. Ask clients to book at least 24 hours ahead if they can.
- **Travel outside the Bay Area:** $500 per travel day, plus travel costs.
- **Photo count:** about 100 edited photos per hour of coverage.
- **What's delivered:** select edits by default. RAW files only on request.
- **NDAs:** Logan will sign them.
- **Insurance:** Logan has no liability insurance yet and is looking into it. Never claim to be insured.
- **Second shooter:** +50% of the package rate (+$500 Session, +$1,000 Day). Already included in The Production.

**Pricing and contact**
- **Price tier:** "$$". Logan wants to be affordable.
- **Phone number:** not in structured data.
- **Location:** central San Francisco is fine for the business address and geo.

**Films**
- Ocean Defenders was published 2023-06-03.

**Where the prints were made**
- **Eastern Sierra, Bishop / Mammoth Lakes area, California:** Sierra River Bend, Cloudbreak Ridge, Blue Hour Ridge, Valley in Violet, Snowline, The Long Valley, Range and Scrub, Fog on the Flats, Golden Brush.
- **Around Seattle, Washington:** Fog Forest, Highland River, Misty Ridgeline, Rainier Afterglow, Forest Fungus, Winter Bark.
- **Rocky Mountains, Colorado:** Aspen and Cobalt, Sunflare Oak, Autumn Against Blue, Still Pond.
- **Galápagos Islands, 2021:** Blue-footed Booby, Sea Lion Pup, Marine Iguana, Reef Passage, Humpback Breach.

**Journal**
- Approved, as "stories behind the prints" plus guides for event clients.
- The first entry is the Galápagos (2021). The content writer drafts it from the facts above and asks Logan only for the personal details it can't know.

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
- **Never post, email or message anyone outside the team.**
  - Social posts, newsletters and outreach are drafts in `team/drafts/` for Logan to send.
  - The one exception: the manager emails the weekly report to oxhollowmedia@gmail.com.
- **Never push to `main` or merge.** All work goes on the weekly branch and into one pull request that Logan approves.
- **Never spend money or sign up for services.**
- **Research is required:**
  - Every recommendation that relies on outside knowledge (SEO practice, competitor pricing, trends, platform rules) cites its sources (URL + date read).
  - Prefer primary sources: Google Search Central, schema.org, MDN, web.dev, platform help centers.
- **Keep changes small and reviewable:** a few strong changes beat many weak ones.
