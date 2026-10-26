# Pinterest and TikTok: should Ox Hollow be there?

Knowledge base. Researched by the marketing lead on 2026-10-25/26; sources were read on **2026-10-25** unless noted.
Draft only: no accounts were created, nothing was pinned or posted.

**Status (coordinator, 2026-10-26):**
- Logan is creating the **Pinterest Business** and **TikTok** accounts himself, to connect to Metricool.
- The Etsy shop URL is now **https://oxhollowmediaprints.etsy.com**. The old oxhollowmediashop URL in `REVENUE-ENGINE.md` and `etsy-launch.md` needs updating; that's a backlog item.

**Citation tags:** [P] = primary source (platform or vendor's own page), [S] = secondary, **UNVERIFIED** = weak or conflicting sources.

## Recommendation in one line

| Platform | Verdict | Why |
|---|---|---|
| **Pinterest** | **Yes, now.** It's the #2 channel after Instagram for prints. | People use it to plan rooms and search for decor. Pins keep sending traffic for months. The site already has the product markup Rich Pins need, so it costs about 15 minutes a week once set up. |
| **TikTok** | **Mirror only, review on day 45.** | Reposting the same clean MP4 costs nothing. Making TikTok-native content doesn't fit 1–2 hours a week, and TikTok Shop isn't worth it for $115+ framed prints yet. |

---

## Pinterest

### Why it fits wall art
- **Decor is Pinterest's biggest category.** Secondary compilations citing Pinterest Newsroom put home decor as the most popular category, with 23B+ Pins and 682M boards, and about 275M weekly users [S1][S2]. **UNVERIFIED** against Pinterest's own page: business.pinterest.com returned 404 for the retail page.
- **People plan purchases there.** A roundup citing Pinterest's 2025 brand study says 67% of Pinners say it inspires purchases they wouldn't otherwise have made [S3]. **UNVERIFIED** (attributed, not seen on a Pinterest page).
- **Searches lean on room and style words.** Pinterest Predicts 2026 home trends were framed as room and style searches ("afrobohemian home decor", "Neo Deco") [S4]. Buyers search "coastal living room wall art", not "Ox Hollow".
- **Pins last.** Unlike Instagram's 48-hour life, a pin keeps surfacing in search. Third-party guides warn it takes **3–6 months** to build meaningful organic traffic [S5], so starting before the holiday season matters even if this year's lift is small.

### Pin types in 2026
- **Standard image pins (2:3, 1000×1500)** remain the workhorse. Tailwind's 2025 study of over 1M pins found **89% of the most viral pins were image pins** and 8% video [S6]. Tailwind advises judging static pins on outbound clicks and video pins on views and saves [S6].
- **Video pins:** Metricool schedules MP4s of **4–15 seconds** to Pinterest [P1]. The Reels are 12–20 s, so trim them to 15 s, or use 4–5 frames.
- **Idea Pins** (the old multi-page format) don't support external links, per Metricool [P1]. Whether Pinterest has fully folded them into standard pins is **UNVERIFIED** in this run. Don't plan around them.
- **Rich Pins (product)** show live price and availability on the pin. Pinterest pulls them from Open Graph or Schema.org markup in the page `<head>`. Pins from Etsy listings get product data automatically within 24 hours, with no markup needed [P2].
  - **Checked 2026-10-26:** the generated print pages (e.g. `prints/amber-glass.html`) already carry `og:type="product"` and Schema.org `Product` JSON-LD. So oxhollowmedia.com print pins should qualify once the site is claimed.
- **Product Pins via catalog** need a Business account, a claimed website, the Pinterest tag installed, merchant basics (contact details, shipping and refund policy) and a data feed. They also unlock shopping ads later [P3]. The **Shopify Pinterest app** (already a Logan to-do in `REVENUE-ENGINE.md`) is the usual way to get the tag and feed.
  - **Caveat:** the site's cart is Shopify but the pages are static HTML on Cloudflare. TODO(team): check whether the Shopify app's feed links to the Shopify product pages or can point to oxhollowmedia.com/prints/<slug>. If it can only link to Shopify, prefer Rich Pins from the site and skip the catalog for now.

### Etsy link-outs
- Rich Pins from Etsy work automatically [P2]. Guides say you connect Pinterest from Etsy's Marketing tab [S7].
- Whether you can still **claim** an Etsy shop on Pinterest is contested. One 2026 guide says connect it under "Claimed accounts"; another says the feature is gone; a March 2026 community thread reports claim failures [S7][S8]. **UNVERIFIED.** Logan can try it once; it doesn't block anything.
- **Link rule:** pin to **oxhollowmedia.com/prints/<slug>** by default, because the site nets the most (BUSINESS.md margins). Pin Etsy listings only on an "Etsy picks" board. An organic Etsy sale nets about the same (`etsy-launch.md`), and Etsy pins carry their own rich data.
- Use UTMs on site links: `?utm_source=pinterest&utm_medium=organic&utm_campaign=<board-slug>`.

### Boards to create (8 to start)
Pinterest boards work best when named the way people search. Board names are visible copy on a new channel, so Logan approves them.

| Board | Pins from |
|---|---|
| Coastal Wall Art | Ocean prints, Galápagos, Salt and Stone |
| Abstract Ocean Photography: Salt and Stone | Obsidian Palace, Phase Shift, Divine Duality |
| Mountain Wall Art: Eastern Sierra | Sierra River Bend, Cloudbreak Ridge, Valley in Violet… |
| Pacific Northwest Forest Prints | Fog Forest, Misty Ridgeline, Rainier Afterglow… |
| Galápagos Wildlife Prints | Blue-footed Booby, Sea Lion Pup, Marine Iguana, Shark Shadow… |
| Living Room Wall Art Ideas | Framed mockups on cream walls (room-based) |
| Office Wall Art (calm, nature) | Mockups. Also a quiet nod to tech-company buyers |
| Gift Ideas for Nature Lovers | 8x12 and 12x18 framed gift sizes (BUSINESS.md strategy) |

**Group boards:** low value in 2026. Pinterest-community and Tailwind posts say fresh pins on your own boards now beat group boards [S9]. Skip them. Join one only if a relevant, active one invites Logan.

### How many pins a week
- **Pinterest's own word:** a Pinterest community staff reply suggested up to 5 fresh pins a day, and warned that too many pins to one URL can trigger spam flags [S10]. Tailwind cites Pinterest saying quality and relevance matter more than frequency [S10].
- **Avoid:** saving the same pin to more than about 10 boards [S10].
- **Plan:** **10 fresh pins a week** (2 a day on weekdays), scheduled once a week in Metricool.
  - A "fresh pin" is a new image or crop. The same print can get several fresh pins: the full photo, a framed mockup, a detail crop, a room mockup [S10].
  - Don't send more than 2 pins to the same URL on the same day.
- Metricool can auto-publish image and video pins, pick or create boards, and the **free plan covers 50 scheduled pieces a month** [P1]. 10 pins a week plus Instagram may exceed 50 a month. TODO(team): count it once the accounts are connected (see the workflow below).

---

## TikTok

### Does reposting Reels work?
- TikTok's guidelines say content is **ineligible for the For You feed if it includes "unoriginal or reused material without anything new"** [P4].
- That rule targets other people's work. Logan's own MP4 from `make_reel.py` is original and has no Instagram watermark, so it's fine.
  - The widely repeated "watermarked content is penalised" claim is only in vendor blogs [S11]. **UNVERIFIED**, but the fix is free: always upload the clean source MP4, never a download from Instagram.
- TikTok expects in-app sound. Add a TikTok sound when posting; music can't go in the file (same licensing rule as Instagram).
- **Metricool can auto-publish to TikTok.** Some posts fall back to a phone notification for manual publishing: music outside the Top 100 trending songs, effects, filters [S12]. Expect Logan to tap "publish" on some posts.

### Formats that suit a photographer on TikTok
- **Photo Mode carousels** (stills with music) exist since 2022. TikTok has pushed photo posts since 2024–25, with a photo-only feed reported in early 2025 [S13]. Claims that carousels out-reach video (3% to 35%) come from vendor blogs [S13]: **UNVERIFIED**.
- Photographer niches that tend to travel (observation, not a sourced study): process/BTS ("how I got this shot"), before/after edits, "one place, four seasons", and ocean and wildlife moments. All overlap with the Instagram plan, so there's no new production.

### TikTok Shop for prints?
- Gelato markets a TikTok Shop integration and names framed wall art as a starter product [S14]. Some of Gelato's figures are wrong (it gives a 2026 launch date for TikTok Shop, which launched in 2023), so treat the post as marketing.
- **Not now:**
  1. It's a fourth storefront to keep in sync (site, Shopify, Etsy, TikTok).
  2. TikTok Shop runs on affiliate creators and low price points. Logan's framed range starts at $115.
  3. There's no audience on the account yet.
- **Revisit** if TikTok passes about 1,000 followers or a print video gets real comments asking "where can I buy this".

---

## Minimal weekly workflow (reuses existing assets)

| When | Who | What | Time |
|---|---|---|---|
| Sunday batch (existing `ox-instagram-batch`) | Team | Next week's 3 Reels + 1 carousel (already made). **Add:** 10 Pinterest pins (2:3 crops and framed mockups from the same prints, with keyword titles and descriptions, a UTM link and a board) and the 3 Reel MP4s queued for TikTok (trimmed to 15 s if also used as video pins). All go into the same Dropbox batch and Metricool **drafts** | 0 for Logan |
| Sunday/Monday | Logan | Approve the one batch (IG + Pinterest + TikTok) in one pass | +5 min |
| Weekdays | Metricool | Auto-publish Pinterest and TikTok, plus IG as now | 0 |
| When notified | Logan | Tap "publish" on any TikTok post Metricool can't auto-post (sound/effects) [S12] | ~5 min/wk |
| Monday report | Team | Pinterest impressions, saves, outbound clicks; TikTok views and followers; UTM sessions per source | 0 |

**Logan's extra time:** about 10 minutes a week on top of Instagram.

**Setup, once (Logan, about 45 min total):**
1. Pinterest Business account (in progress).
2. Claim oxhollowmedia.com: meta tag or DNS. DNS is a Cloudflare change, so Logan does it; the team can add the meta tag on the weekly branch with approval.
3. Connect Etsy from Etsy's Marketing tab.
4. Install the Shopify Pinterest app.
5. Create the 8 boards.
6. TikTok account (in progress): Business account, bio matching Instagram, link to oxhollowmedia.com.
7. Connect both to Metricool.

**Kill/keep rule:**
- **Day 45 (about 2026-12-10):** if TikTok averages under 200 views a post, stop TikTok and keep Pinterest.
- **Day 90:** judge Pinterest on outbound clicks (target: 100 a month). Give it the full 90 days because of its 3–6 month ramp.

---

## Sources

**Primary**
- [P1] Metricool, "How to Schedule Pinterest Pins" (published 2025-07-10): https://metricool.com/schedule-pinterest-metricool/
- [P2] Pinterest Help, Rich Pins: https://help.pinterest.com/en/business/article/rich-pins
- [P3] Pinterest Help, "Before you get started with catalogs": https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs
- [P4] TikTok Community Guidelines, Integrity and Authenticity: https://www.tiktok.com/community-guidelines/en/integrity-authenticity (the FYF standards overview, https://www.tiktok.com/community-guidelines/en/fyf-standards, only links to sections)

**Secondary**
- [S1] Printful, Pinterest statistics: https://www.printful.com/blog/pinterest-statistics
- [S2] Charle Agency, Pinterest statistics: https://www.charleagency.com/articles/pinterest-statistics/
- [S3] Searchlab, Pinterest statistics 2026: https://searchlab.nl/en/statistics/pinterest-statistics-2026
- [S4] Axios on Pinterest Predicts 2026 (2025-12-09): https://axios.com/2025/12/09/2026-pinterest-trend-report ; Apartment Therapy: https://www.apartmenttherapy.com/pinterest-predicts-2026-37522611
- [S5] Alura, Etsy listings to Pinterest: https://www.alura.io/blog/how-to-automatically-post-etsy-listings-to-pinterest-and-skyrocket-your-traffic
- [S6] Tailwind, "Video Pins vs Static Pins": https://www.tailwindapp.com/blog/video-pins-vs-static-pins
- [S7] eCommerce Fastlane, Pinterest for Etsy 2026: https://ecommercefastlane.com/how-to-use-pinterest-for-etsy-a-practical-guide-for-2026/ ; Printful: https://www.printful.com/blog/how-to-use-pinterest-for-etsy ; LitCommerce: https://litcommerce.com/blog/how-to-use-pinterest-for-etsy/
- [S8] Pinterest Business Community, "Can not make Rich Pin from Etsy": https://community.pinterest.biz/t/can-not-make-rich-pin-from-etsy/43654
- [S9] Pinterest Business Community, boards in 2026: https://community.pinterest.biz/t/the-pinterest-boards-that-will-matter-most-in-2026-and-quietly-help-you-sell/41299 ; Tailwind, group boards: https://www.tailwindapp.com/blog/pinterest-group-boards-create-join-leave/
- [S10] Pinterest Business Community staff reply on fresh pins: https://community.pinterest.biz/t5/connect-and-share-with-other-creators/quot-fresh-quot-pins/m-p/57937 ; Tailwind, posting frequency: https://www.tailwindapp.com/blog/pinterest-posting-frequency ; Tailwind FAQ (10-board guidance): https://support.tailwindapp.com/en/articles/3702827-pinterest-best-practices-faq
- [S11] Socialkit, Instagram to TikTok: https://socialk.it/en/cross-post/instagram-to-tiktok ; Kapwing: https://www.kapwing.com/resources/how-to-repost-on-tiktok/
- [S12] Metricool, scheduling TikTok: https://metricool.com/tiktok-carousels
- [S13] Lindsey Gamble, TikTok Photo Mode: https://lindseygamble.com/blog/tiktok-photo-mode ; Stack Influence: https://stackinfluence.com/tiktoks-photo-post-comeback/
- [S14] Gelato, "Getting started on TikTok Shop": https://www.gelato.com/blog/getting-started-on-tiktok-shop
