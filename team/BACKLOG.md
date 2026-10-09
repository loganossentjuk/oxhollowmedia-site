# Team backlog

The manager picks from the top of each section and keeps the list ranked. Ideas need Logan's approval when marked **(Logan)**.

## Standing (every week)
- [ ] web-engineer: full QA run (desktop and phone, every page, every print page's pickers and cart links)
- [ ] shop-manager: sales snapshot, listing health, price consistency against `gelato.prices`
- [ ] marketing-lead: 3 Instagram drafts, 5 researched event-photography leads, content calendar

## SEO
- [x] Audit titles and descriptions on all top-level pages (length, uniqueness, target query per page)
- [x] Product + Offer JSON-LD on every print page, generated from the catalog; framed price range from `gelato.prices`
- [ ] LocalBusiness/ProfessionalService JSON-LD: check it is complete and consistent on the home, events and work-with-me pages
- [ ] VideoObject JSON-LD for films
- [ ] Internal links: print pages ↔ gallery; events ↔ work-with-me ↔ contact
- [ ] Image alt-text pass across the gallery and print pages
- [ ] (Logan) Google Search Console and Google Business Profile: check they're set up; the team can only prepare instructions

## Content
- [x] FAQ section on work-with-me for tech event planners (only facts already on the site; the rest as TODO(Logan))
- [ ] Print stories: a 2–3 sentence story per print in the catalog (place, light, moment); start with the gallery-wall top 10
- [ ] (Logan) Approve a Journal/blog section. First draft idea: "Where the light is: 5 Bay Area spots I photograph" in `team/drafts/`

## Website and bugs
- [ ] Image weight: find the largest images and propose or serve responsive sizes
- [ ] Accessibility pass (contrast, focus states, labels) on nav, print pickers and forms
- [x] 404 page links back to prints and gallery

## Shop
- [ ] Batch 2 framed listings (10 prints) were created hidden at Gelato default prices; they need pricing and publishing by Logan or the Gelato cloud session. Track until done.
- [ ] Verdigris and Copper & Teal are held until their print files are re-made **(Logan)**
- [ ] Holiday gift-deadline banner idea, using Gelato's published shipping cut-offs **(Logan)**

## Marketing
- [ ] Monthly newsletter draft (first run of each month)
- [ ] Instagram bio link page (`/links`): check its UTM links point at live pages (`/store` exists?)

## New ideas (2026-10-09, ranked)
- [ ] Home page: short distinct H1/intro with "San Francisco event photography"
- [ ] Internal-link pass: events <-> work-with-me <-> contact, print pages -> gallery
- [ ] `/links`: add h1; point Shop button at `/prints`; bump CSS version to ?v=53
- [ ] Focus-visible outlines, skip link, axe contrast audit
- [ ] BreadcrumbList JSON-LD on print pages; VideoObject for films (fix placeholder uploadDate)
- [ ] Generator: stop rewriting sitemap lastmod on every build
- [ ] Print stories top 10 (needs Logan's notes); "How to brief an event photographer" page
- [ ] Shop: finish batch 2 framed switch, then holiday banner and gift-sized picks
- [ ] Weekly QA script in scripts/ (Node Playwright)
