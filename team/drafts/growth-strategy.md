# Growth strategy: ads and outreach (draft, 2026-10-13)

DRAFT FOR LOGAN. Nothing here has been launched, spent, posted or sent. No accounts were created. Every outside number has a source in the "Sources" section, with the date read. Numbers marked **(unverified)** were read only through a search-engine summary, not the original page. Treat them as rough and re-check them before spending.

Two plans follow. **Plan A** is event-photography leads and **Plan B** is gallery and print-shop sales. Pick one plan to lead with and one budget level (see "Decisions for Logan" at the end). Weekly marketing work then follows that plan.

---

> **Logan's decisions (2026-10-13):** Plan A leads, Plan B runs on free channels. Budget $0 to start, plus a small holiday ad test for prints (amount TBD by Logan; use the framed break-even numbers in the Shop analyst input as the ceiling per sale). Measurement fixes approved except email signup. Clients we may name in outreach: Semgrep, Bucket Brigade, Ocean Defenders Alliance, Conservation Made Simple, Illuminate Conservation. Verdigris and Copper and Teal are ready to sell. @oxhollowmedia is a Business account.

## 0. Before either plan: measurement gaps found in the repo

These cost nothing to fix, and without them we cannot tell whether any channel works.

1. **The site has no analytics tag in its HTML.** I found no Google Analytics, Cloudflare Web Analytics beacon, Meta Pixel or Pinterest tag. Cloudflare Web Analytics is "available on all plans" [S20]. Whether it is already switched on in the Cloudflare dashboard (it can run without a tag in the HTML) is a question for Logan. TODO(Logan): check Cloudflare dashboard > Web Analytics for oxhollowmedia.com.
2. **UTM tags stop at the Shopify cart.** A print page links straight to `sessjk-nj.myshopify.com/cart/<variantId>:1`, so any `utm_*` on the print page does not travel to the order. Shopify cart permalinks accept a `ref` parameter, which shows as a referral code on the order, and `attributes[...]`, which show in the order notes [S19]. Backlog idea: have `build_print_pages.py` copy the page's `utm_campaign` into `ref=` on the cart link. That is web-engineer work and needs approval.
3. **The contact form has no "How did you hear about me?" field.** Its fields are name, email, project, event date, budget and message. Adding one optional dropdown (Google, Instagram, LinkedIn, referral, venue, planner, other) is the cheapest way to attribute event leads, which close by email rather than on-site. Backlog idea, needs approval.
4. **The `/links` bio page sends `/store?utm_...` through a 301 to `/prints`.** This was already flagged in the 2026-10-09 report and is still open.

---

## Plan A: Event-photography leads

### A1. Who to target
- **In-house event and community teams at Bay Area tech companies.** Titles include event marketing, field marketing, developer relations, community, people/culture (offsites, all-hands, holiday parties) and recruiting. The site already shows "Trusted by Semgrep". That is the only client the site names, and we name no others.
- **Event production and experiential agencies** that staff photographers for client launches and conferences (for example TRADEMARK and Bash Creative, from the 2026-10-09 leads file).
- **Venue sales teams** that clients ask for vendor names. The venues the site already lists are Moscone Center, Fort Mason, The Midway, Pier 27 and YBCA. Not every venue keeps a list: one past client's review of Fort Mason says there was no approved-vendor list (secondhand, one review [S17]).
- **Conference organizers and sponsors.** Sponsors want photos of their booths and talks (for example QCon SF, Nov 16–20; see the leads file).
- What they buy, from `/work-with-me`: The Session (half day, from $1,000), The Day (from $2,000), The Production (multi-day, from $5,000), and the monthly content partner plan (from $2,500 a month). One booking is worth more than a whole month of the largest budget below, so a single lead can pay for the plan.

### A2. Channels ranked by expected return on a small budget
The ranking is my judgement from the costs below. None of it has been tested on this business yet.

| Rank | Channel | Cost | Why this rank |
|---|---|---|---|
| 1 | **Referral asks to past clients, plus direct outreach to planners, agencies and venues** (email or LinkedIn message, sent by Logan) | $0, Logan's time | The highest-intent people, and nothing to buy. The site's "replies within one business day" promise helps. Templates are in Appendix C. |
| 2 | **Google Business Profile** (service-area business, address hidden) | Free [S6] | Google says a service-area business with no storefront gets one profile and should hide a home address [S5]. It shows in local map results for "event photographer" searches. Category names must be checked in the live profile ("Photographer" as primary is the usual advice; secondhand [S18]). |
| 3 | **Google Search Ads** (exact and phrase match on local queries such as "event photographer san francisco" and "corporate event photographer bay area") | National average CPC $5.42, CPL $66.69; Business Services CPC $5.87, conversion rate 4.85%, CPL $93.69 [S1] | This catches people who are searching right now. Search volume for these exact queries is unknown: TODO(Logan) or team, once an Ads account exists, read the figures in the free Keyword Planner (it needs account setup and billing details [S3]). These are national averages; I found no San Francisco figure. Google can spend up to 2x the daily budget on a given day, but never more than 30.4x the daily budget in a month [S4]. |
| 4 | **LinkedIn**: organic posts from Logan's profile, plus a later small Sponsored Content test aimed at event and field-marketing titles at Bay Area companies | Organic $0. Ads: $10/day minimum, $25/day suggested start for new advertisers [S7]. CPC estimates range from $2 to $12+ **(unverified)** [S8] | The exact audience, but costly. The $10 minimum is about $300 a month, more than all of the $250 level. Organic posting comes first. |
| 5 | **Directories and marketplaces** (The Vendry, Peerspace vendor lists, Thumbtack) | The Vendry's vendor terms were not found (it shows "Request Pricing" profiles, and some are unclaimed [S16]). Thumbtack is pay-per-lead, about $20–75 per photographer lead, third-party estimate **(unverified)** [S15] | Low intent, and price shoppers on Thumbtack. Claiming a free profile on The Vendry, which is corporate-events focused, is worth an hour. Paid lead marketplaces are not recommended yet. |
| also | **Tech meetup and community sponsorship** (photographing a meetup for free in exchange for credit and a short intro) | $0 cash, one evening | Builds a portfolio of tech events and gets introductions to DevRel and community people. Prices for sponsorship slots were not researched; offer the service, not money. |

### A3. 90-day calendar (week of 2026-10-19 to week of 2027-01-11)
Holiday-party season (late Nov to mid Dec) is the near-term booking window. January is when 2027 conference and offsite budgets get planned, so Q1 outreach is the bigger prize.

| Week of | Plan A actions |
|---|---|
| Oct 19 | Set up measurement (section 0). Create and verify Google Business Profile. Send referral asks to past clients (Template C3). Cloudflare Connect is at Moscone this week; the 2026-10-09 leads file treats it as a lead for 2027. |
| Oct 26 | Send 5 planner and agency notes (C1). Claim The Vendry profile if it is free. Instagram: event Reel (see Section "Instagram as the hub"). |
| Nov 2 | Send 3 venue notes (C2): The Midway, Fort Mason, Pier 27. Post GBP photos (10 event images from `images/portfolio/events/` the client has cleared). Election Day Nov 3: no promotion. |
| Nov 9 | If budget level ≥ $250: launch Google Search test (Appendix A) at a 4-week length. LinkedIn post 1 ("how I cover a keynote", a guide-style post). |
| Nov 16 | QCon SF week (Nov 16–20, per leads file): no pitching that week, but note sponsors for 2027. Follow up on any unanswered notes from Oct 26 (one follow-up only). |
| Nov 23 | Thanksgiving week. No outreach. Check Google Ads search-terms report and add negative keywords. |
| Nov 30 | Holiday-party last-minute window: an Instagram Reel on holiday parties plus a GBP post. 24-hour rush add-on ($200) is already a stated service. |
| Dec 7 | Second wave of 5 planner and agency notes, framed as "planning Q1 offsites and kickoffs". LinkedIn post 2. |
| Dec 14 | Review Google test: clicks, form leads, cost per lead. Keep, pause or move budget. Ask each December client for a referral and a GBP review (ask, never write one). |
| Dec 21 | Quiet week. Draft the January list: 2027 conferences in SF (research task for marketing-lead). |
| Dec 28 | Quiet week. |
| Jan 4 | Q1 outreach: 10 notes to companies with public 2027 SF events (the marketing-lead researches them, Logan sends). |
| Jan 11 | 90-day review: leads by source, bookings, cost per booking. Decide whether LinkedIn Ads is worth a $300 test. |

### A4. First 3 actions Logan can take this week
1. **Create the Google Business Profile** as a service-area business (SF Bay Area), address hidden, primary category Photographer, with services matching `/work-with-me`. It is free [S5][S6]. The team cannot create accounts; Logan does it.
2. **Send a referral ask (Template C3) to 3–5 past event clients** whose events you would happily shoot again. TODO(Logan): we do not know who these are; the site names only Semgrep.
3. **Pick your 5 outreach targets from `team/drafts/leads-2026-10-09.md`**, adapt Template C1 or C2, and send them yourself. Mark in a simple sheet: date sent, channel, reply.

### A5. What to measure
- **Contact-form leads by source.** Formspree submissions, tagged by the new "How did you hear" field (section 0.3) and by UTM landing page (for example `/events?utm_source=google&utm_medium=cpc&utm_campaign=event-sf`).
- **Leads → quotes → bookings**, and the booking value. A spreadsheet is enough. One booking at $1,000+ versus spend is the number that decides.
- **Google Ads:** clicks, CTR, CPC, search terms, and form submissions. Conversion tracking needs a tag on `/thank-you` (Formspree redirect). That is web-engineer work, after approval.
- **GBP:** calls, website clicks and direction requests in the Performance view (as GBP reports them).
- **Outreach:** notes sent, replies, meetings and bookings.
- UTM convention for every Plan A link: `utm_source=<google|linkedin|instagram|email|gbp>&utm_medium=<cpc|social|reel|outreach|profile>&utm_campaign=<event-sf-q4|referral|venue>`.

### A6. Starter budget
The cost-per-lead arithmetic below uses national averages for illustration [S1]. It is not a forecast for SF.

| Level | What it buys |
|---|---|
| **$0 / mo** | GBP, referral asks, 10–15 outreach notes a month (Appendix C), LinkedIn organic posts, a free The Vendry profile if available, one free community or meetup shoot. Logan's time is about 3 hours a week. |
| **$250 / mo** | Everything at $0, plus a Google Search test at about $8/day. At the Business Services average CPC of $5.87, that is about 40 clicks a month; at the 4.85% conversion rate, about 2 form leads (CPL average $93.69 → about 2.7 leads) [S1]. Small numbers, so give it 2 months before judging. |
| **$750 / mo** | Everything at $0, plus Google Search at about $20/day (about $600, about 100 clicks and about 5–6 leads at those averages [S1]) plus about $150 for Instagram Reel boosts of event work to Bay Area adults (CPC average $0.60 for traffic campaigns, all industries [S2]). LinkedIn Ads is held back: its $10/day minimum is about $300 a month and LinkedIn suggests $25/day to start [S7]. Test it in month 3 only if Google works. |

---

## Plan B: Gallery and print-shop sales

### B1. Who to target
- **Gift buyers, Oct–Dec**: people buying for someone who loves the Sierra, the Galápagos, the Pacific Northwest or Colorado. The story and place of each print is the hook (facts in `team/BUSINESS.md`).
- **People decorating their own home** who care about a place they have been: Eastern Sierra, Seattle, Rockies, Galápagos, Bay Area coast.
- **Interior designers and home stagers in the Bay Area** who need framed art in volume.
- **Offices** (the same tech companies as Plan A): lobby, meeting-room and new-office art. This joins Plan A to Plan B: an event client is a possible office-art client.
- Pricing points stay general here: framed prints run $115–$330 and paper $35–$70 (from `team/BUSINESS.md`).

> **Shop analyst input** (full detail in `team/drafts/growth-shop-input.md`)
> - **Lead with framed, not paper.** Break-even cost per purchase is about $65 (framed 8x12, $115), $88 (12x18), $117 (16x24) and $180 (24x36), against $20–40 for paper. Paid ads should only send traffic to framed and framed-canvas sizes.
> - **Prints to feature:** Dawn Patrol, Valley in Violet and Snowline in ads; Fog Forest and Aspen and Cobalt on Pinterest (portrait); Golden Gate, Fog for Bay Area gift guides; the Galápagos trio as the $115 gift, tied to the journal; the Embers set as a bundle. Verdigris and Copper and Teal are confirmed ready to sell (2026-10-13).
> - **Price position:** below independent nature photographers (Carly Tabak framed 8x12 is $375; ours is $115) and close to marketplace prices. No discount is needed. The message is "framed, ready to hang, shipped free".
> - **Offers that change no prices (Logan approves each):** a gift-deadline banner (after G-day), a multi-print Embers cart link, gift cards (Shopify Basic supports them), and a gift guide by price point.
> - **Fix before sending traffic:** `shipping-returns.html` still says the receipt comes from Stripe, but checkout is now Shopify.
>
> _[slot reserved]_

### B2. Channels ranked by expected return on a small budget

| Rank | Channel | Cost | Why this rank |
|---|---|---|---|
| 1 | **Instagram Reels (organic) → print pages, with a UTM bio link** | $0 | Reels reach non-followers; the print and its story are the content. See "Instagram as the hub". |
| 2 | **Email list capture with Shopify Messaging** (formerly Shopify Email) | First 10,000 emails a month free, then from $1 per 1,000 [S10] | The list is ours, not a platform's. A short holiday sequence (gift guide, deadline reminder) costs nothing at this size. Needs a signup form on the site; the static site has none (backlog idea). |
| 3 | **Pinterest (organic first, then ads)** via the Pinterest app for Shopify | App free; ads only when bought [S11]. Pinterest says 41% of its audience starts gift lists as early as October [S12]. Home décor CPC is often cited at $0.50–$1.50 **(unverified)** [S13] | Wall art is a search-and-save habit on Pinterest. The app syncs the catalog into Product Pins and adds the Pinterest tag [S11]. Some reviews in the listing mention unexpected ad charges; set budgets by hand. |
| 4 | **Meta/Instagram ads**: Reel boosts now; retargeting site visitors later | Traffic-campaign CPC averages $0.60 overall, $0.59 Shopping/Collectibles & Gifts, $0.64 Furniture [S2]. Boost minimum about $1–$5/day by source **(unverified)** [S14] | Cheap reach. Retargeting needs the Meta Pixel on the site [S9] (not installed) and a minimum audience size Meta does not publish [S9]; third parties say about 100 people **(unverified)**. So retargeting is a month-2+ step. |
| 5 | **Local gift guides, makers markets, designers and offices** (Logan pitches by email) | $0 except any market booth fee | SF outlets that run local gift guides include the SF Standard and Time Out [S21]. SFMOMA's Holiday Makers Market is Dec 6, 2026 with 20 Bay Area makers; the application route was not found [S22]. Offices and designers are slow but high-value (Shop analyst input on terms). |
| not now | **Google Shopping/Search for prints** | Shopping, Collectibles & Gifts CPC $4.14, CPL $49.40 [S1] | Costly per click compared with Meta and Pinterest for a product people do not search for by name. Revisit after Christmas. |

### B3. 90-day calendar (week of 2026-10-19 to week of 2027-01-11)
**Holiday cut-offs.** USPS's 2026 recommended send-by dates for the lower 48 are Ground Advantage Dec 17, Priority Mail Dec 18 and Priority Mail Express Dec 19 [S23]. Gelato prints and frames before it ships, so its last-order dates will be earlier. Gelato's order-deadlines page showed only 2025 and UK rows when we checked (2025 UK economy wall-type products: Dec 17, 2025 **(unverified)** [S24]). **TODO(Logan): read the 2026 US framed-print dates in your Gelato dashboard.** Every "gift deadline" item below hangs on that date, written as **G-day**.

| Week of | Plan B actions |
|---|---|
| Oct 19 | Set up measurement (section 0). Shop analyst input in. Install the Pinterest app for Shopify (Logan; free) and claim the website. Reel: one print story with UTM link. |
| Oct 26 | Gift-guide pitch emails to local outlets (Logan sends). Pinterest: 3 boards (Eastern Sierra, Galápagos, Pacific Northwest), pinned from print pages. |
| Nov 2 | Email signup form live on site (if approved) with a plain offer such as "gift deadlines and new prints, about once a month". Election Day Nov 3: no promotion. |
| Nov 9 | Reel: "gifts for someone who's been there" (Galápagos set). If budget ≥ $250: start Reel boosts. |
| Nov 16 | Pitch 5 interior designers or stagers and 3 offices (Plan A contacts with new offices). |
| Nov 23 | Thanksgiving (Nov 26), Black Friday (Nov 27), Small Business Saturday (Nov 28): "studio of one" Reel. Any discount is Logan's call (Shop analyst input). |
| Nov 30 | Cyber Monday (Nov 30), Giving Tuesday (Dec 1: conservation film Reel, link to /films). Email 1: holiday gift picks plus G-day. |
| Dec 7 | SFMOMA Holiday Makers Market is Dec 6 (as a visitor or future applicant). Reel: "last week to order framed for Christmas" if G-day falls here. Email 2: deadline reminder. |
| Dec 14 | After G-day: switch the message to paper prints if they ship faster (check), or to "a print for the new year". USPS Ground cut-off Dec 17. |
| Dec 21 | Quiet. No ads after G-day unless the delivery promise is clear. |
| Dec 28 | "New wall for a new year" Reel. Review holiday results. |
| Jan 4 | Pinterest ads test if budget allows (home refresh is a January theme; date assumption, not sourced). Email 3: the story behind one print. |
| Jan 11 | 90-day review: sessions, orders by source (see B5), list growth. |

### B4. First 3 actions Logan can take this week
1. **Read the 2026 US Gelato last-order dates** for framed prints, canvas and paper from the dashboard, and send them to the team. Every holiday item depends on them.
2. **Install the Pinterest app for Shopify** and connect a Pinterest business account. It is free; ads are paid only if bought [S11]. Do not create an ad campaign yet. Ad credits are offered on first campaign [S11], so wait for the plan.
3. **Turn on Shopify Messaging** (first 10,000 emails a month free [S10]) and decide where the signup lives: a form on the site, or a "join the list" link to a Shopify page. The team can build the form on approval.

### B5. What to measure
- **Shopify sales by source.** Shopify's analytics (read-only for the team). Add a `ref=<campaign>` code on cart links (section 0.2) so orders that started from a Reel, pin or email can be told apart. The numbers stay in the PR body, never in this public repo.
- **UTM traffic to print pages**, once an analytics tool is on (section 0.1). Convention: `utm_source=<instagram|pinterest|email|meta>&utm_medium=<reel|pin|newsletter|paid>&utm_campaign=<holiday-2026|print-slug>`.
- **Email:** signups per week, open and click rates, and orders with the email ref code.
- **Pinterest:** outbound clicks and saves per pin (in Pinterest Analytics), and orders if the tag is installed.
- **Meta:** CPC, landing-page views and cost per order (once the Pixel is on).
- Leading indicator to check monthly: print-page sessions → cart clicks (needs analytics).

### B6. Starter budget

| Level | What it buys |
|---|---|
| **$0 / mo** | 3 Reels a week in season (organic), Pinterest organic with catalog sync, Shopify Messaging (free tier) holiday emails, local gift-guide and designer/office pitches. |
| **$250 / mo** | Everything at $0, plus about $8/day boosting the best-performing print Reel to US adults interested in landscape photography and home décor, linking to a print page. At the $0.59–$0.64 traffic CPC averages that is roughly 400 clicks a month [S2]. That is a reach and traffic number, not a sales number: no conversion benchmark we found fits this shop. |
| **$750 / mo** | Everything at $0, plus Meta about $450 (Reel boosts plus a website-visitor retargeting set once the Pixel is on and the audience is big enough [S9]) and Pinterest about $300 ($10/day, a common "practical" daily figure from third-party guides **(unverified)** [S13]), aimed at wall-art and gift search terms. Stop all spend at G-day unless the delivery promise is clear. |

---

## Instagram as the hub (@oxhollowmedia, Reels first)

Instagram is the one place both plans share. The same weekly Reels work for both:

- **Plan A:** one event Reel in three, showing coverage style and turnaround (a keynote, a booth, a holiday party). The client must OK each image. Link: `/events?utm_source=instagram&utm_medium=reel&utm_campaign=<name>`. Planners check a photographer's Instagram before replying to an outreach note, so the grid is also proof for Plan A's emails and LinkedIn messages.
- **Plan B:** two Reels in three tell a print's story (place, light, moment) and link `/prints/<slug>?utm_source=instagram&utm_medium=reel&utm_campaign=<name>`.
- **Paid:** a boost only ever goes on a Reel that already did well organically. It is the cheapest test in both plans [S2][S14].
- The bio link page `/links` carries both (fix the `/store` redirect first; section 0.4).

**If we later connect the account's insights** (Logan grants access; the team never logs in), what we would track weekly:
- Per Reel: views, reach, average watch time, saves, shares, likes, comments, reposts and skip rate. These are the Reel metrics in Meta's Instagram API [S25]; some are marked "in development".
- Per account: profile visits, follows and link taps on the bio. Profile visits are reported for feed and story media, not Reels, in the API [S25], so check them at account level.
- Ratios we would watch: shares and saves per 1,000 reach (which Reels to boost), watch time versus Reel length (hook quality), and bio link taps → UTM sessions → leads or orders.
- Account type: insights need a professional (Business or Creator) account [S25]. TODO(Logan): confirm @oxhollowmedia is one. Follower count and current reach are unknown to the team; we do not guess them.

---

## Appendix A: Draft ad copy and audiences, top paid channel per plan (NOT launched)

### A-1. Plan A: Google Search (responsive search ad draft)
- **Campaign:** Search only (Display and Search Partners off), location SF Bay Area (people *in* the area), schedule weekdays, budget per the chosen level.
- **Keywords (exact and phrase):** "event photographer san francisco", "corporate event photographer san francisco", "conference photographer san francisco", "event photographer bay area", "tech event photographer". Starter negatives: wedding, jobs, hiring, salary, course, free, cheap.
- **Final URL:** `https://oxhollowmedia.com/events?utm_source=google&utm_medium=cpc&utm_campaign=event-sf-q4`
- **Headlines (≤30 chars):** "SF Event Photographer" · "Conferences, Launches, Parties" · "Galleries in 5 Business Days" · "Half Day From $1,000" · "Bay Area Tech Events" · "Reply Within 1 Business Day" · "Candid Keynote Coverage" · "Book Holiday Party Coverage"
- **Descriptions (≤90 chars):** "Candid photos of conferences, launches and team events across the Bay Area." · "Full gallery in five business days. Clients may use the photos however they like." · "Tell me the date and venue. You'll hear back within one business day."
- Facts used: all from `/work-with-me` and `team/BUSINESS.md`. No insurance claim, no deposit mention.

### A-2. Plan B: Meta (Instagram Reels boost / Reels placement)
- **Creative:** the best organic print Reel of the week (12–20 s, silent, Logan adds audio in-app).
- **Audience 1 (prospecting):** US, 25–65, interests in landscape photography, national parks, hiking, interior design, home décor. Placement: Instagram Reels.
- **Audience 2 (retargeting, after Pixel):** visitors to `/prints/*` or `/gallery` in the last 30 days who did not buy.
- **Primary text:** "Eastern Sierra, early light, before the wind came up. Sierra River Bend, framed and ready to hang." (story text from the existing Oct 9 draft) · "Five prints from the Galápagos, 2021. Each one has a story." · "Order by [G-day] for Christmas." (only after Gelato dates are known)
- **Button:** Shop now → `https://oxhollowmedia.com/prints/sierra-river-bend?utm_source=meta&utm_medium=paid&utm_campaign=holiday-2026`
- No "stunning", no exclamation marks, no prices unless the Shop analyst input confirms them.

---

## Appendix B: Pinterest pin copy (organic, Plan B)
- Pin title: "Eastern Sierra wall art: Sierra River Bend, framed print" · Description: "River and snowmelt below the Sierra, early light. Framed in black, white or oak. Gift idea for someone who loves Mammoth and Bishop."
- Board names: "Eastern Sierra prints", "Galápagos wildlife prints", "Pacific Northwest fog and forest", "Colorado autumn".

---

## Appendix C: Cold-outreach templates for event planners (Logan's voice, drafts only)
Replace bracketed parts. Send yourself. Keep only claims that are true; TODO(Logan) marks what we can't verify.

**C1. To an in-house event or community lead at a tech company**
> Subject: Photos for [event name] in [month]
>
> Hi [first name], I'm Logan, an event photographer in San Francisco. I saw [event name] is coming up at [venue] and wanted to introduce myself. I shoot conferences, launches and team events in a candid style, with a full gallery in five business days. If you're still lining up coverage, I'd be glad to send a quote within a day. A few examples: oxhollowmedia.com/events

**C2. To a venue sales or events team**
> Subject: Photographer for your corporate clients
>
> Hi [venue] team, I'm Logan from Ox Hollow Media. I photograph company events around the Bay Area, [including at [venue] — TODO(Logan): keep only if true]. When clients ask you who to call for photos, I'd like to be an easy name to pass on. I reply within one business day and deliver within five. Happy to send work from your space if that helps.

**C3. Referral ask to a past client**
> Subject: A small favor
>
> Hi [first name], thanks again for having me at [event]. I'm booking for the winter and early next year. If you know an event, community or marketing lead who needs a photographer, I'd be grateful for an intro. And if you have a minute, a short Google review would help me a lot. [GBP review link, once the profile exists] No pressure either way.

(For agencies, adapt C1: "I'd like to be a reliable name on your photographer list for SF launches and conferences.")

---

## Questions for Logan (unknown facts; not guessed)
1. Is Cloudflare Web Analytics (or any analytics) switched on for oxhollowmedia.com?
2. Who are the past event clients we can ask for referrals, and may we name any besides Semgrep?
3. Which event photos have client OK for public use in ads, GBP and Reels?
4. Is @oxhollowmedia a professional (Business or Creator) account? Rough follower count, if you want it in plans (it stays out of the repo if you prefer).
5. Have you shot at The Midway, Fort Mason or Pier 27 specifically (for the venue notes)?
6. Gelato 2026 US last-order dates per product (G-day).
7. Would you consider a holiday offer for prints (Shop analyst input decides form)?

## Decisions for Logan
1. **Which plan leads for the next 90 days**: A (event leads), B (print sales), or A with B running organic only in the background (my suggestion: A + organic B, because one booking outweighs a month of print traffic, and B's holiday window is short and hangs on the G-day date).
2. **Budget level per plan**: $0, $250 or $750 a month.
3. **Approve the measurement fixes** in section 0 for the web engineer: analytics tag, cart `ref` code, "How did you hear" field, email signup form. Nothing is changed until you say so.
4. **You do the account setups** (GBP, Pinterest app, Shopify Messaging, a Google Ads account if you choose a paid level). The team cannot create accounts or spend.
5. **Approve or edit the outreach templates** (Appendix C) and the first 5 targets.
6. **Holiday offer yes/no** for prints, after the Shop analyst input.
7. **LinkedIn Ads**: skip for now (my suggestion) or test at $300+ a month in January.

---

## Sources (read 2026-10-13 unless marked)
- [S1] LocaliQ, "Search Advertising Benchmarks" (labelled 2026, last updated June 1, 2026): https://localiq.com/blog/search-advertising-benchmarks/ (opened)
- [S2] LocaliQ, "Facebook Advertising Benchmarks" (last updated Sep 23, 2026): https://localiq.com/blog/facebook-advertising-benchmarks/ (opened)
- [S3] Google Ads Help, "Use Keyword Planner": https://support.google.com/google-ads/answer/7337243 (opened)
- [S4] Google Ads Help, "About average daily budgets": https://support.google.com/google-ads/answer/2375454 (opened)
- [S5] Google Business Profile Help, "Guidelines for representing your business on Google": https://support.google.com/business/answer/3038177 (opened)
- [S6] Google, Business Profile FAQ ("creating a Business Profile ... is free"): https://business.google.com/us/business-profile/ (opened)
- [S7] LinkedIn Business, "Maximize your budget": https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget (opened)
- [S8] LinkedIn CPC estimates, third-party (unverified, search summary): https://www.webfx.com/blog/marketing/linkedin-advertising-cost/ , https://nuoptima.com/linkedin-ads-cost , https://postiv.ai/blog/linkedin-advertising-costs
- [S9] Meta for Developers, "Website Custom Audiences" (Pixel-based; audience must reach "a certain size"): https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences (opened); the ~100-person figure is third-party (unverified): https://www.stackmatix.com/blog/meta-custom-audiences
- [S10] Shopify App Store, Shopify Messaging ("first 10,000 emails each month are free", then from $1/1,000): https://apps.shopify.com/shopify-email (opened)
- [S11] Shopify App Store, Pinterest app: https://apps.shopify.com/pinterest (opened)
- [S12] Pinterest Business, "Our 2025 holiday marketing guide is here" (41% gift lists as early as October): https://business.pinterest.com/uk/blog/announcing-2025-holiday-marketing-guide/ (opened)
- [S13] Pinterest CPC and budget, third-party (unverified, search summary): https://www.mbadv.agency/pinterest-ads/how-much-do-pinterest-ads-cost , https://aiadvantageagency.com/pinterest-ads-cost-for-ecommerce/ , https://trackbee.io/blog/pinterest-ads-cost
- [S14] Instagram boost minimums, third-party (unverified, search summary): https://blog.hootsuite.com/boost-instagram-reels/ , https://www.shopify.com/blog/how-to-boost-instagram-post , https://help.metricool.com/en/article/how-to-boost-your-posts-84jehj
- [S15] Thumbtack lead cost, third-party (unverified, search summary): https://leadcapture.io/blog/thumbtack-lead-cost/
- [S16] The Vendry SF photographer profiles (search summary): https://thevendry.com/pro/47329/lunch-break-headshots-san-francisco-ca
- [S17] Fort Mason vendor policy, one past client's review (search summary, unverified): https://theknot.com/marketplace/fort-mason-center-for-arts-and-culture-san-francisco-ca-2021541
- [S18] GBP category advice for photographers, third-party (search summary): https://filterpixel.com/blog/marketing-event-photography-business
- [S19] Shopify.dev, "Create cart permalinks" (`ref`, `attributes`, `note`): https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks (opened)
- [S20] Cloudflare Docs, Web Analytics ("Available on all plans"): https://developers.cloudflare.com/web-analytics/ (opened)
- [S21] Local gift guides (search summary): https://sfstandard.com/2025/12/14/san-francisco-gifts-christmas-last-minute , https://www.timeout.com/san-francisco/shopping/holiday-gift-guide
- [S22] SFMOMA Museum Store, "2026 SFMOMA Holiday Makers Market" (search summary): https://museumstore.sfmoma.org/blogs/news/2026-sfmoma-holiday-makers-market
- [S23] USPS 2026 holiday send-by dates (search summary of USPS page and Sep 23, 2026 news reports): https://www.usps.com/holiday/holiday-shipping-dates.htm , https://www.wsmv.com/2026/09/23/usps-announces-recommended-2026-holiday-mailing-shipping-deadlines/
- [S24] Gelato order deadlines (page blocked to direct fetch; search summary shows 2025 and UK rows only, unverified): https://www.gelato.com/order-deadlines
- [S25] Meta for Developers, "Instagram Media Insights" (Reel metrics list): https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights/ (opened)
- In-repo facts: `team/BUSINESS.md`, `work-with-me.html`, `events.html`, `contact.html`, `links.html`, `_redirects`, `team/drafts/leads-2026-10-09.md` (read 2026-10-13).
