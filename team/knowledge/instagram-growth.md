# Instagram growth for a small photography account (2026)

Knowledge base for @oxhollowmedia. Researched by the marketing lead on **2026-10-25**; every source below was read that day unless noted.
Draft only: nothing was posted, scheduled, followed or messaged.

**Starting point (from the manager's brief, 2026-10-25):** about 67 followers, very low reach, Business account, Metricool connected, Reels built with `scripts/make_reel.py`, Obsidian Palace was the best post so far, $0 ads, Logan has 1–2 hours a week.

**How to read the citations**
- **[P]** = primary (Instagram, Meta or the creator's own page).
- **[S]** = secondary (news, vendor blog, study). Use it as a lead.
- **UNVERIFIED** = only one weak source, or the sources disagree. Check it in the app before relying on it.

---

## 1. What the algorithm rewards (the short version)

| Signal | What it means for Logan | Source |
|---|---|---|
| **Watch time** | The top signal for both followers and non-followers. The first 2 seconds decide it. Short (12–20 s) Reels that loop are easier to watch to the end than long ones. | Mosseri, as reported by [S1][S2] |
| **Sends per reach** (DM shares) | Weighs a little more than likes for **non-followers**. That's the reach Logan needs at 67 followers. A post people send to a friend ("we should go here", "this would look good in our hallway") travels. | [S1] |
| **Likes per reach** | Weighs a little more than sends for people who already follow. | [S1] |
| **Saves** | Carousels earn more saves than Reels. Reels earn more comments and shares. | Socialinsider data, via [S3] |
| **Originality** | Instagram ranks original posts over reposts, labels reposts, and stops recommending aggregator accounts. Secondary reports say this was extended from Reels to photos and carousels on **2026-04-30**. Logan's work is all his own, so this helps him. Never repost other people's work to fill the grid. | TechCrunch [S4]; Planoly [S5] (the April 2026 date is **UNVERIFIED** against an Instagram post) |
| **Human, not AI** | Mosseri's year-end note (Dec 2025) said Instagram would favour raw, real human content over AI-generated material in 2026. BTS and "how I made this" fit that. | Secondhand via [S1] (**UNVERIFIED** wording) |
| **Tiered testing** | New eligible posts go first to a small audience, followers or not, and widen if they do well. So one weak post doesn't hurt the account. Judge each Reel on its own numbers. | TechCrunch [S4] |

**Plain-language takeaway:** make posts people **watch to the end** and **send to someone**. Saves are the bonus.

### Tools Instagram gives small accounts

- **Trial Reels.** A Reel is shown to non-followers first. You can share it to followers by hand, or let it auto-share if it does well in the first 72 hours. Meta launched it to all professional accounts in Dec 2024 [P1].
  - **Eligibility is unclear in 2026.** One guide says 1,000 followers. Another, citing Instagram Help, says 200 for professional accounts. Both are **UNVERIFIED** [S6][S7].
  - At about 67 followers Logan may not see the "Trial" toggle yet. TODO(Logan): check the toggle on the next Reel's share screen and tell the team.
- **Collab posts.** One post appears on up to 5 profiles. It shares views and likes, and reaches each collaborator's audience. Collaborators must be professional accounts and accept the invite. Third-party guides agree on the 5 limit; Instagram's own Help page wasn't reachable [S8].
- **Hashtags are capped at 5** on posts and Reels. Instagram told creators this in Dec 2025, and asked for relevant tags, not generic ones like #reels or #explore [S9]. Treat them as labels, not a growth lever.
- **Keyword captions.** Instagram search reads captions and comments, and it analyses the image itself. Mosseri has called hashtags a categorisation tool, not a growth hack [S10] (secondary). Public posts from professional accounts can also show up in Google [S10] (**UNVERIFIED**; no primary Meta/Google note found).
  - **What it means for captions:** write the place and subject in plain words in the first line, e.g. "Mermaid's Pools, Oahu. Volcanic rock from inside a cave as the wave comes in."
- **Original audio in the app.** Instagram has said it favours original sound or music from its own library [S11] (secondary). Logan's MP4s are silent by design; add sound in the app.

---

## 2. Formats that work for photographers

Ranked by fit for Logan's 1–2 hours a week. Everything reuses photos already in `images/portfolio/`, except where noted.

| # | Format | Why it works | How to make it here | Effort |
|---|---|---|---|---|
| 1 | **Story Reel** (5–7 stills, 3 s each, one-line hook) | Reels reach non-followers more than any other format [S3]. A story (one trip, one place) gives people a reason to send it. | `make_reel.py` as now. The hook goes on frame 1, and the last frame names the print. | Team builds; Logan approves |
| 2 | **Series drops** ("Salt and Stone, 1 of 3") | Obsidian Palace was the best post. A series turns one hit into a habit, so people follow to see the next one. | Obsidian Palace → Phase Shift → Divine Duality, plus new abstracts as Logan adds them. | Team |
| 3 | **Original vs edited** (2-frame Reel or carousel) | Photographers' most-shared format is the before/after, because it shows skill without bragging. It also proves "human, not AI". | Needs Logan's unedited RAW export for 1–2 frames (the team doesn't have them). TODO(Logan): drop 3 RAW/edited pairs into Dropbox. | 10 min for Logan, once a month |
| 4 | **Location carousel** (4–8 photos + a map/text card) | Carousels earn saves [S3]. Location words in the caption feed search [S10]. | Eastern Sierra (Bishop → Mammoth), Seattle, Colorado, Galápagos 2019. | Team |
| 5 | **BTS clip** (10–15 s of Logan shooting, phone on a rock) | Raw and human, which Instagram favours. It's also the only format that shows Logan himself, and that builds trust for event clients. | Logan films on the next shoot (shot list in the weekly batch). | 10 min while shooting |
| 6 | **Print-in-room** (framed mockup on a cream wall) | It answers "what would it look like?" and is the bridge to a sale. | Mockups per `instagram-plan.md` §1. | Team |
| 7 | **Event highlight** (6 stills, with client OK) | Plan A is event leads. Planners judge range and consistency. | Only cleared images (BUSINESS.md: no recognisable people without OK). | Team; Logan clears faces |

**Hooks that fit Logan's voice** (quiet, concrete, no hype). The hook is the first 2 seconds of text:
- A place and a time: "GALÁPAGOS, 2019." / "BISHOP, BLUE HOUR."
- The surprising fact: "SHOT FROM INSIDE A CAVE." (Obsidian Palace)
- A question that answers itself on frame 2: "WHAT THE WAVE LOOKS LIKE FROM BEHIND."
- A process line: "STRAIGHT OUT OF CAMERA → FINISHED PRINT."
- Avoid: "You won't believe…", "Wait for it", countdowns, emojis in the overlay.

---

## 3. Cadence

- **3 Reels + 1 carousel a week**, already set in `team/drafts/instagram-plan.md` §2. Keep it.
  - Mosseri's line is that the right schedule is the one you can sustain [S12] (secondary).
  - The Rival IQ median is about 3.7 posts a week [S12].
- **Stories:** 2–3 a week, not daily. Reshare the day's Reel and use the link sticker to the print page. Stories carry clickable links, so they turn engaged followers into store visits [S13].
- **Times:** keep the Sprout/Buffer windows in `instagram-plan.md` (weekday midday). Once Metricool has 30+ days of data, switch to its own best-time heatmap (the team can read it with `getBestTimeToPostByNetwork`).
- **Don't** post more just to post. At 67 followers, one Reel that 300 non-followers watch to the end beats five that nobody finishes.

---

## 4. Captions, hashtags and SEO

**Caption template (Logan's voice):**
1. **Line 1:** place + subject in plain words, which feeds search. "Mermaid's Pools, Oahu."
2. **Line 2–3:** one concrete detail about the light or the moment, in the first person.
3. **Line 4:** a soft CTA, only on print posts. "It's a print now. Link in bio."
4. **Hashtags:** 3–5 specific ones (cap is 5 [S9]). Mix one place tag (#easternsierra), one subject tag (#oceanphotography), one buyer tag (#fineartprints) and one niche/community tag (#bayareaphotographer).
5. **Location tag** on every post with a real place.
6. **Alt text:** add a plain description in Advanced settings. It's good for accessibility, and Instagram uses it for search.

**Profile SEO:** the name field is searchable. Consider "Logan · Ox Hollow Media" or "Ox Hollow Media | SF photographer". TODO(Logan): visible-copy change, so it's your call. Today's bio (2026-10-14) is fine.

---

## 5. Collaborations (the fastest free reach)

Collab posts put one post on up to 5 profiles [S8]. Ideas, all drafts for Logan to propose himself:
- **Past clients we may name** (BUSINESS.md): Ocean Defenders Alliance, Conservation Made Simple, Illuminate Conservation, Bucket Brigade, Semgrep.
  - **The ask:** a collab Reel of work already delivered, e.g. Ocean Defenders stills, only with consent from anyone recognisable. They get content; Logan gets their audience.
- **Location partners:** a café, gallery or boutique hotel that hangs a print, as a collab post when it's installed. None exists yet, so this is for later.
- **Peer photographers** at similar size in the Bay Area (1k–10k): a "two views of the same place" collab, or a joint photo walk. Find them through the location tags Logan already uses.
- **Never** buy shoutouts, follow/unfollow, or join engagement pods. These go against Instagram's spam rules, and the reach they bring isn't real buyers.

---

## 6. Engagement routine: 10 minutes, 4 days a week (~40 min/week)

Sized to Logan's 1–2 hours a week. Do it from the phone, ideally within an hour after a Reel goes up.

1. **2 min:** reply to every comment and DM on the latest post. A reply with a question gets a second comment.
2. **4 min:** open 2 location tags Logan uses (#easternsierra, Mermaid's Pools, Point Reyes and so on) and leave **3 real comments** on recent posts by people with fewer than 10k followers. A specific line about their light or place, not "nice shot".
3. **2 min:** send one Reel to someone who'd genuinely want it (a past client, a friend at a venue). No pitch.
4. **2 min:** reshare the newest post to Stories with a link sticker on print posts.

That's all. Don't spend time on follower counts mid-week; the Monday report has them.

---

## 7. Teardown: 10 photography accounts

**What we could see:** follower counts are what each public Instagram profile showed on **2026-10-25** (logged-out view). Logged-out pages don't show post dates, post counts or Reel views for most accounts, so **cadence and hooks could not be verified for the large accounts**; where noted, they come from the profile bio, highlight titles or the photographer's own site. TODO(team): a logged-in look (Logan's phone, 10 min) would fill the cadence column.

| Account | Followers (seen 2026-10-25) | Niche | What's visible | How they sell prints | Lesson for Ox Hollow |
|---|---|---|---|---|---|
| **@paulnicklen** (Paul Nicklen) | 6.9M | Polar and ocean wildlife, conservation | Bio: "@SeaLegacy co-founder / @NatGeo contributor" [P2] | Site has "Limited Edition Prints" and a store; the site also asks for SeaLegacy donations [P3] | Mission and conservation framing sits **beside** print sales, not instead of them. That fits Logan's mission line. |
| **@chrisburkard** (Chris Burkard) | 3.7M | Adventure landscape (cold coasts, surf) | Bio: "Have Camera, Will Travel. Photographer•Speaker•Filmmaker"; link-in-bio with 4 links, the first a YouTube film [P4] | Not checked this run | Multiple income lines (speaking, films, photos), the same mix as Ox Hollow. The bio leads with a story (a film), not a shop. |
| **@clarklittle** (Clark Little) | 1.9M | Shorebreak waves (Hawaii) | Bio: "Shorebreak Photographer"; link to clarklittle.com [P5] | His site rate-limited us (429), so print details are **UNVERIFIED** | **A one-subject niche, said in two words.** It's the closest analogue to Salt and Stone (Oahu water and rock). Owning "Salt and Stone" as a series name is the move. |
| **@mitty** (Cristina Mittermeier) | 1.6M | Ocean conservation | Bio lists SeaLegacy, Nat Geo Explorer, "lens-based mixed media artist"; Linktree [P6] | Not checked | Calls herself an artist, not only a photographer, so the work is framed as collectible. |
| **@franslanting** (Frans Lanting) | 849K | Wildlife, conservation (Nat Geo) | Bio: "Nat Geo Photographer Author \| Public Speaker \| Creator of images, stories and events to inspire wonder and concern…"; lanting.com plus 4 links [P7] | lanting.com (not checked this run) | A California-based name (Bay Nature covers his Monterey Bay work [S14]). "Wonder and concern" is the same register as Logan's mission line. |
| **@benthouard** (Ben Thouard) | 372K | Ocean and waves from underwater | Bio: "Ocean photographer / Fine Art Prints & Books"; highlights titled Aqua Obscura, EXHIBITIONS, TURBULENCES, SURFACE [P8] | Bio points to benthouard.com for prints and books (site rate-limited, details **UNVERIFIED**) | **Highlights are named series**, so the profile reads like a gallery. Copy this: highlights for Salt and Stone, Galápagos 2019, Eastern Sierra, Events. |
| **@erinbabnik** (Erin Babnik) | 56.4K | Fine-art landscape (Sierra and beyond) | Bio: "Photographer, Speaker, Author, Creative Coach / @canonusa Explorer of Light"; erinbabnik.com [P9] | Site has a store and cart, workshops, and image licensing via the contact form [P10] | Mid-size accounts earn from **teaching and licensing** as well as prints. A later option for Logan, not now. |
| **@effiesnapsshots** (Effie Benjamin) | 2,120 | Freediving and ocean, film and digital, Monterey Bay | Bio: "Freediver with a camera • Film & digital / Monterey Bay CA // Missoula MT / Prints & projects ↓"; recent posts are a mix of photos, carousels and clips, with tags from local partner accounts [P11]; profiled by NOAA Monterey Bay [S15] | effiebenjamin.com ("Prints & projects") | A small regional account at Logan's size. The bio says **what, where and "prints"** in three lines. A conservation-agency profile gave her credibility. |
| **@kumigram** (Kumiko Iwashita) | 1,100 | Bay Area wildlife | Bio: "wildlife/ nature photography / SF Bay Area"; the bio link points to a Point Reyes National Seashore Association spotlight; posts dated Sep–Oct 2026 are singles and carousels [P12][S16] | No shop visible | **Local press beats a shop link at small sizes.** A Point Reyes or NOAA-style feature is a realistic, free credibility win. Ties into `photo-competitions.md` (BigPicture, BCDC). |
| *Gap:* a 10k–100k Bay Area ocean/landscape account | n/a | n/a | Two searches didn't surface one we could verify | n/a | TODO(team): next run, Logan names 2–3 Bay Area accounts he admires and the team reads them logged-in. |

**Patterns across all ten:**
1. **The niche is in two to four words** in the bio ("Shorebreak Photographer", "Ocean photographer", "Freediver with a camera").
2. **Prints are one line in the bio, not the headline.** The big accounts lead with mission, story or film.
3. **Conservation partners and press do the credibility work** (SeaLegacy, Nat Geo, NOAA, Point Reyes).
4. **Highlights are organised as series.**

---

## 8. What to do with this (for the weekly batch)

1. Lead every week with **one Salt and Stone or Galápagos story Reel**, since that's where the proof is (Obsidian Palace).
2. Write the first caption line as **place + subject**; use 3–5 hashtags plus a location tag.
3. Add **one "original vs edited"** a month, once Logan supplies RAW pairs.
4. **Rename the highlights** into series (Salt and Stone, Galápagos 2019, Eastern Sierra, Events). It's a visible change, so Logan approves it.
5. **Propose one collab a month** to a named past client (Logan sends).
6. **Check the Trial Reels toggle**; if it's there, use it on every print Reel.

---

## Sources (all read 2026-10-25)

**Primary**
- [P1] Meta Newsroom, Trial Reels (Dec 2024): https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first/ (cited in `instagram-plan.md`, read 2026-10-13)
- [P2] https://www.instagram.com/paulnicklen/
- [P3] https://www.paulnicklen.com/
- [P4] https://www.instagram.com/chrisburkard/
- [P5] https://www.instagram.com/clarklittle/
- [P6] https://www.instagram.com/mitty/
- [P7] https://www.instagram.com/franslanting/
- [P8] https://www.instagram.com/benthouard/ and /reels/
- [P9] https://www.instagram.com/erinbabnik/
- [P10] https://www.erinbabnik.com/
- [P11] https://www.instagram.com/effiesnapsshots/
- [P12] https://www.instagram.com/kumigram/
- Not reachable: Instagram Help Center Trial Reels page (https://help.instagram.com/1255328138850553 returned an empty shell).

**Secondary**
- [S1] eClincher, "How the Instagram Algorithm Works in 2026": https://www.eclincher.com/articles/how-the-instagram-algorithm-works-in-2026 ; Hootsuite: https://blog.hootsuite.com/instagram-algorithm/
- [S2] Dataslayer, Instagram algorithm guide: https://dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers
- [S3] Socialinsider 2026 Instagram benchmarks: https://www.socialinsider.io/instagram-benchmarks ; Contentdrips summary (Reels = comments/shares, carousels = saves): https://contentdrips.com/blog/2026/06/instagram-reels-vs-carousels-2026-guide/
- [S4] TechCrunch, Instagram favours original content and smaller creators: https://techcrunch.com/?p=2697938
- [S5] Planoly, "Instagram Updates its Original Content Policy": https://planoly.com/blog/instagram-updates-its-original-content-policy
- [S6] Storrito, Trial Reels 72 hours: https://storrito.com/resources/how-instagram-trial-reels-work-72-hours/
- [S7] Superprofile, Trial Reels eligibility: https://superprofile.bio/guides/instagram-trial-reels
- [S8] Sked Social, Collab guide 2026: https://skedsocial.com/blog/instagram-collaboration-feature.md ; Planable: https://help.planable.io/hc/en-us/articles/21715384533148-Instagram-Collabs-posts
- [S9] Social Media Today, 5-hashtag limit: https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ ; BetaNews (2025-12-19): https://betanews.com/2025/12/19/instagram-puts-a-limit-on-hashtag-usage/
- [S10] Kontentino, Instagram search SEO: https://www.kontentino.com/q-and-a/instagram-search-seo/ ; Corkboard Concepts, hashtags in 2026: https://corkboardconcepts.com/marketing-resources/blog/are-hashtags-still-relevant-in-2026/
- [S11] Rival IQ, Reels best practices: https://www.rivaliq.com/blog/best-practices-instagram-reels/
- [S12] RouteNote on posting frequency (Mosseri): https://routenote.com/blog/how-often-you-should-post-on-instagram/ (cited in `instagram-plan.md`)
- [S13] creativehub, selling prints on Instagram: https://creativehub.io/help/how-do-i-use-instagram-to-sell-art-prints/
- [S14] Bay Nature, Frans Lanting tag: https://baynature.org/tag/frans-lanting
- [S15] NOAA Monterey Bay, "She to Shining Sea": https://montereybay.noaa.gov/new/260805shetoshiningsea.html
- [S16] Point Reyes National Seashore Association, photographer spotlight: https://ptreyes.org/news/photographer-spotlight-kumiko-iwashita/
