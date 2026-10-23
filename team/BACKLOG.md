# Team backlog

The manager picks from the top of each section and keeps the list ranked. Ideas need Logan's approval when marked **(Logan)**.

## Standing (every week)
- [ ] web-engineer: full QA run (desktop and phone, every page, every print page's pickers and cart links)
- [ ] shop-manager: sales snapshot, listing health, price consistency against `gelato.prices`
- [ ] marketing-lead: 3 Instagram drafts, 5 researched event-photography leads, content calendar

## SEO
- [x] Audit titles and descriptions on all top-level pages (length, uniqueness, target query per page)
- [x] Product + Offer JSON-LD on every print page, generated from the catalog; framed price range from `gelato.prices`
- [x] LocalBusiness/ProfessionalService JSON-LD: check it is complete and consistent on the home, events and work-with-me pages
- [x] VideoObject JSON-LD for films (Ocean Defenders only; other dates TODO(Logan))
- [ ] Internal links: print pages ↔ gallery; events ↔ work-with-me ↔ contact
- [ ] Image alt-text pass across the gallery and print pages
- [ ] (Logan) Google Search Console and Google Business Profile: check they're set up; the team can only prepare instructions

## Content
- [x] FAQ section on work-with-me for tech event planners (only facts already on the site; the rest as TODO(Logan))
- [ ] Print stories: a 2–3 sentence story per print in the catalog (place, light, moment); start with the gallery-wall top 10
- [ ] **Top priority.** Journal entry 1: "The Galápagos, 2019", the story behind Blue-footed Booby, Sea Lion Pup, Marine Iguana, Reef Passage and Humpback Breach. Link each print page.
  - Draft it in `team/drafts/`.
  - List the personal details needed from Logan as short questions.
  - Propose a simple `/journal` page design for review. The journal is approved as print stories plus guides for event clients.
- [ ] Journal entry 2 (event clients): "How to brief your event photographer"
- [ ] Shelved: "Where the light is: 5 Bay Area spots". Logan's nature work is mostly outside the Bay Area.

## Photo review (Logan)
- [ ] **(Logan)** Review the 55 BestWork picks not yet on the site: `Dropbox/Career/OxHollow/BestWork picks (review)/` (numbered; `_contact-sheet.jpg` shows all). Pick which go to the gallery and which to the print shop. 16, 39, 40 and 29 are too small to print; 46–55 are portraits of real people and need their OK. Added 2026-10-09.
- [ ] **(Logan)** Review the blue-tagged photos and decide which go on the site. Added 2026-10-09.

## Website and bugs
- [ ] Links/canonical use `/prints` but Pages serves `/prints/` (308 hop on 221 nav links, sitemap, canonical): switch to `/prints/` (SEO + web-engineer)
- [ ] Add `<main>` landmarks to about, contact, events, films, filmmaking, gallery, index, privacy, shipping-returns, 404
- [ ] **Next run, approved by Logan 2026-10-14 (web-engineer):** resize ALL web photos in images/portfolio (not the Dropbox print masters): 1600px WebP ~q75 (aim <350KB) + an 800px version via srcset/sizes on every page and in build_print_pages.py; keep JPG fallbacks; keep higher quality where detail suffers; watermark is already baked in. Preview before live.
- [ ] Catalog `location` field so print descriptions name the place (e.g. Galápagos) — generator line ~215
- [ ] Remove the archived Petunia Blush Canvas entry from the catalog
- [x] Measurement (approved 2026-10-13): cart `ref=` code from UTMs, "How did you hear" field, /links → /prints, shipping-returns Stripe wording
- [x] Cloudflare Web Analytics: already on since 2026-07-14 (auto-install); GA4 G-8BE3SQGCQG live 2026-10-13 with begin_checkout/generate_lead, /privacy page
- [ ] Email signup form (not yet approved)
- [ ] Image weight: find the largest images and propose or serve responsive sizes
- [ ] Accessibility pass (contrast, focus states, labels) on nav, print pickers and forms
- [x] 404 page links back to prints and gallery

## Reminders for Logan
- [ ] **(Logan)** Client logos for the About page (Semgrep, Bucket Brigade, Ocean Defenders Alliance, Conservation Made Simple, Illuminate Conservation): get files + OK to show them
- [ ] **(Logan)** Client quote for the About/events pages (in progress)
- [ ] **(Logan)** Send the other abstracts (like Obsidian Palace) for the series (repeat in every report's Needs-you list until ticked)
- [ ] **(Logan)** Shopify: archive `mural-sundown-acrylic-1` (live at Gelato default prices), old combined `sun-on-the-water`, `marsh-at-dusk`, `cloudbreak-ridge`; decide on the 26 plain Canvas listings
- [ ] **(Logan)** Look into general liability insurance. Venues often ask for a certificate of insurance; quotes run about $350/yr for $1M. Started 2026-10-09.

## Shop
- [x] Batch 2 framed listings priced and published (2026-10-09)
- [x] Verdigris and Copper & Teal: files re-made, ready to sell (Logan, 2026-10-13)
- [ ] Holiday gift-deadline banner idea, using Gelato's published shipping cut-offs **(Logan)**

## Marketing
- [x] **Growth strategy drafted 2026-10-13** (`team/drafts/growth-strategy.md`). Logan chose: events lead + prints organic, $0 budget plus a small holiday print-ad test. Weekly marketing work now follows it.
- [ ] ~~Original brief:~~ Growth strategy: ads and outreach. Deliver `team/drafts/growth-strategy.md` with two plans: event-photography leads, and gallery/print-shop sales.
  - **Research first and cite sources:**
    - realistic costs and results for Google Ads (local "event photographer San Francisco" searches), Meta/Instagram ads (Reels boosts, retargeting site visitors), LinkedIn (tech event planners), and Pinterest (wall art)
    - free channels: Google Business Profile, event-venue preferred-vendor lists, planner and agency partnerships, tech meetup and community sponsorships, referral asks to past clients, directory listings
    - print-shop tactics: gift guides, interior designers and offices, holiday timing using Gelato's cut-offs, email list capture
    - **use the margin table in `team/BUSINESS.md`:** promote framed print and framed canvas first, and size any ad budget against profit per sale (about $67–$188 framed) rather than price
  - **For each plan:**
    - who to target
    - 3–5 channels ranked by expected return for a small budget
    - a 90-day calendar
    - the first 3 concrete actions Logan can take this week
    - what to measure: UTM links, Shopify sales, contact-form leads
    - a starter budget at three levels ($0, $250 a month, $750 a month), with what each buys
  - **Draft-only extras:** ad copy and audiences, plus 3 cold-outreach templates for event planners in Logan's voice. Nothing gets launched, spent or sent.
  - **Return** the plan for Logan to choose. After that, each week's marketing work follows the chosen plan.
- [ ] Monthly newsletter draft (first run of each month)
- [x] Instagram bio link page (`/links`): Shop now points at /prints with UTMs (2026-10-13)

## New ideas (2026-10-09, ranked)
- [x] Home page: short distinct H1/intro with "San Francisco event photography"
- [ ] Internal-link pass: events <-> work-with-me <-> contact, print pages -> gallery
- [ ] `/links`: add h1 (Shop button → /prints done 2026-10-13)
- [ ] Focus-visible outlines, skip link, axe contrast audit
- [ ] BreadcrumbList JSON-LD on print pages; VideoObject for films (fix placeholder uploadDate)
- [ ] Generator: stop rewriting sitemap lastmod on every build
- [ ] Print stories top 10 (needs Logan's notes); "How to brief an event photographer" page
- [ ] Shop: finish batch 2 framed switch, then holiday banner and gift-sized picks
- [ ] Weekly QA script in scripts/ (Node Playwright)

## New ideas (2026-10-12, ranked)
- [ ] Journal entry 1 is a scaffold: needs Logan's answers (team/drafts/journal-galapagos-2021.md), then fill catalog `story` fields
- [ ] Catalog: drop archived canvas entry for `petunia-blush`; add framed entries for Verdigris, Copper & Teal; add Rising Flame and Sparks (needs Logan OK)
- [ ] Decide canonical set for duplicate "-1"/"-2" Shopify products (24x36 added), then repoint catalog
- [ ] Hidden UTM/source field on /contact form; Pinterest pins; email capture; holiday banner (blocked on Gelato 2026 dates)
- [ ] Axe contrast audit and skip link; BreadcrumbList on print pages
- [ ] VideoObject for Brushstrokes For Survival and Fluid Frontier once Vimeo dates are confirmed

## New ideas (2026-10-23, ranked)
- [ ] Generator: only bump sitemap lastmod when a page changes
- [ ] Fix "Galápagos 2021" to 2019 in `team/drafts/instagram-2026-10-12.md`
- [ ] Shop: research Gelato 2026 holiday cut-off dates for the banner
- [ ] Verify PyBay, SF Tech Week and Cloudflare Connect dates, and the Exploratorium and Palace of Fine Arts rental pages
- [ ] Before the Wind listings still use `autumn-flats-*` handles (catalog)
