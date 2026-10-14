# Instagram plan for @oxhollowmedia (draft, 2026-10-13)

DRAFT FOR LOGAN. Nothing has been posted, scheduled or sent. The Metricool tools were used read-only.

- **Goal:** post regularly and grow followers.
- **Order of priority:** event leads come first (Plan A). Prints run on free channels (Plan B).
- **Times:** all times are Pacific.

## 0. Baseline: not available yet (needs Logan)

Metricool has no Instagram account connected to it yet. When we queried it on 2026-10-13, its brand settings returned "This brand doesn't have any social network connected yet". Followers, reach and the best-time heatmap all came back as zeros.

TODO(Logan): connect @oxhollowmedia at https://app.metricool.com/brands/connections?blogId=7413270. After that, the next weekly run can pull the 30 to 90 day baseline and Metricool's own best times. Until then:

- **Posting times:** taken from the two 2026 studies in Sources [S3][S4].
- **Baseline:** Instagram's in-app Insights > Account overview has the same numbers. Note them privately if you want them tracked. They stay out of the repo.

## 1. Aesthetic rules (match the website)

**Palette.** Cream #F3EFE4 and #E5DEC8, plus card green #294132. Use them for:
- text-card backgrounds
- carousel end cards
- Story backgrounds
- the "frame" around mockups

**Type.** Any text overlay is Cormorant Garamond 500, uppercase or small caps, with letter-spacing 0.12em (about +120 tracking in the Instagram editor or Canva).
- **Size and colour:** keep it small. Use cream text over a photo or ink/green text over cream.
- **Length:** one line, at most two.
- **No extras:** no outlines, drop shadows or neon.

**Photos.**
- **Crops:** crop clean, with no visible watermark. Export the crop from your originals, not from `images/portfolio/`, because those copies carry the Ox Hollow mark.
- **Grid sizes:** feed posts are 4:5. Reels are 9:16, with the subject inside the center 4:5 so the grid crop still works.

**Prints** are shown as a framed mockup (black, white or oak frame) on a cream wall, with lots of empty wall. The print title goes in small Cormorant beneath.

**Restraint.**
- No loud stickers, emoji walls, arrows, "link in bio!!!" banners or trending text effects.
- At most one emoji per caption, and usually none.

**Grid look.** Calm and airy. Deep ocean blues and Sierra violets sit beside warm event candids, broken up every few tiles by a cream or green card.

- **Rhythm:** about one text card or framed mockup per row of three, so the grid breathes.
- **Mix:** events never sit three in a row, so a planner sees both range and consistency.
- **Pinned posts:** pin 3 to the top. Suggested: the events Reel, a framed-print carousel, and the Ocean Defenders post.

**Build note.**
- **Reel script:** `scripts/make_reel.py` currently draws text in Georgia/FreeSerif with a drop shadow, not Cormorant (backlog item below). Until it is changed, add text overlays in the Instagram editor instead, or use the Reels from the script without text.
- **Machine:** ffmpeg is not installed on this Mac, so the 3 Reels below were not built yet. To build them, run the commands in section 6 on a machine with ffmpeg, or after `brew install ffmpeg`. That is Logan's call.

## 2. Cadence (sustainable, 4 feed posts a week)

| Format | Per week | Why |
|---|---|---|
| Reels | 3 (Mon, Wed, Thu) | Reels reach non-followers. Meta's Trial Reels lets you show a Reel to non-followers first and then share it to followers [S5]. Use Trial on print Reels to test hooks. |
| Carousel | 1 (Tue) | Third-party 2026 guidance says carousels drive saves and shares. It suggests about 3-4 Reels and 1-2 carousels a week [S2]. |
| Stories | 1-3 on most weekdays | Stories help community and conversation more than reach [S2]. Use them for BTS, polls and resharing the day's post. |

- **Why this pace:** Adam Mosseri, head of Instagram, has said there is no single right frequency, and that the right schedule is one you can sustain [S2] (secondhand report). Four feed posts a week is above the 2026 median of about 3.7 posts a week reported via Rival IQ [S2], and is realistic for one person.
- **Hashtags:** use 3-5 per post. Instagram's @creators account announced a 5-hashtag cap on feed posts and Reels on 2025-12-18 [S1]. Treat hashtags as topic labels, not reach drivers.

**Posting times** (Pacific; re-check against Metricool once it is connected):
- **Mon 2:00 pm (Reel):** Sprout's Monday window is 2-4 pm [S3].
- **Tue 1:00 pm (carousel):** Sprout's Tuesday window is 1-7 pm [S3].
- **Wed 12:00 pm (Reel):** this is in Buffer's top 3 slots [S4] and inside Sprout's Wednesday window [S3].
- **Thu 9:00 am (Reel):** this is Buffer's #1 slot [S4].
- **Avoid weekends and early mornings.** Both studies rank weekends lowest [S3][S4].

## 3. Content pillars

| Pillar | Share | Posts in 4 weeks | Links to |
|---|---|---|---|
| Events and behind the scenes (Plan A) | about 40% | 6 | `/events` or `/work-with-me` |
| Print stories (Plan B) | about 35% | 6 | `/prints/<slug>` or `/gallery` |
| Conservation films | about 15% | 2 | `/films` |
| Place (SF, Sierra) | about 10% | 2 | a print page |

- **Client OK for event photos:** every event photo needs the client's OK before it goes on Instagram (growth strategy, "Instagram as the hub"). TODO(Logan): confirm that the event images below are cleared for social. They are already public on /events.
- **UTM format:** every link uses `?utm_source=instagram&utm_medium=social&utm_campaign=<slug>`. Put it on the `/links` bio page, or use Instagram's link sticker in Stories.

## 4. Four-week calendar (from Mon 2026-10-19)

**How to read the entries:**
- **Paths:** photo paths are under `images/portfolio/`.
- **Captions:** in your voice. Edit freely.
- **Audio:** add music in the Instagram app only. Pick from the in-app trending list on the day, and use "slow ambient" or "acoustic" as the fallback mood. Never put music in the file.

### Week 1

**Mon 10/19, 2:00 pm, Reel: events.** File: `team/drafts/reels/2026-10-19-1.mp4` (to build, see section 6).
- **Photos:** `events/02-keynote.jpg`, `events/10-tech-talk.jpg`, `events/11-stage-qa.jpg`, `events/04-industry-mingle.jpg`, `events/05-evening-reception.jpg`, `events/14-team-portrait.jpg`
- **Hook (first clip):** WHAT A DAY OF COVERAGE LOOKS LIKE. **Last clip:** HIGHLIGHTS WITHIN THE WEEK
- **Caption:** Keynote in the morning, Q&A after lunch, the reception once the light goes warm. I shoot company events around the Bay Area quietly and candidly. You get a highlight set the same week and the full gallery in five business days.
- **Hashtags:** #eventphotography #sanfranciscoevents #bayareaphotographer #techevents
- **Cover:** the keynote frame
- **CTA:** "Booking winter dates. Link in bio." `https://oxhollowmedia.com/events?utm_source=instagram&utm_medium=social&utm_campaign=events-coverage`

**Tue 10/20, 1:00 pm, Carousel: print stories.**
- **Slides:** 1) cream card reading TWO NEW PRINTS; 2) `ocean/15-copper-and-teal.jpg`; 3) a framed mockup of Copper and Teal; 4) `ocean/14-green-water.jpg` (Verdigris); 5) a framed mockup of Verdigris
- **Hook:** TWO NEW PRINTS
- **Caption:** Copper and Teal, and Verdigris. Both are in the shop now as framed prints, canvas, paper, wood and acrylic. TODO(Logan): one line on where and when you made them.
- **Hashtags:** #fineartprints #oceanphotography #wallart #homedecor
- **CTA:** `https://oxhollowmedia.com/prints/copper-and-teal?utm_source=instagram&utm_medium=social&utm_campaign=copper-and-teal`

**Wed 10/21, 12:00 pm, Reel: print stories.** File: `team/drafts/reels/2026-10-21-2.mp4`. Turn on Trial [S5].
- **Photos:** `ocean/04-blue-footed-booby.jpg`, `ocean/03-sea-lion-pup.jpg`, `ocean/12-marine-iguana.jpg`, `ocean/02-shark-silhouette.jpg` (Reef Passage), `ocean/01-humpback-breach.jpg`
- **Hook:** GALÁPAGOS, 2021. **Last clip:** FIVE PRINTS FROM ONE TRIP
- **Caption:** One trip to the Galápagos in 2021. A booby, a sea lion pup, an iguana, a reef, a whale. All five are prints now. TODO(Logan): one personal detail from the trip.
- **Hashtags:** #galapagos #wildlifephotography #fineartprints #oceanlife
- **Cover:** the blue-footed booby
- **CTA:** `https://oxhollowmedia.com/prints/blue-footed-booby?utm_source=instagram&utm_medium=social&utm_campaign=galapagos-2021`

**Thu 10/22, 9:00 am, Reel: place.** File: `team/drafts/reels/2026-10-22-3.mp4`.
- **Photos:** `mountains/16-cloudbreak-ridge.jpg`, `mountains/14-sierra-river-bend.jpg`, `mountains/15-valley-in-violet.jpg`, `mountains/17-snowline.jpg`, `mountains/18-the-long-valley.jpg`, `mountains/19-range-and-scrub.jpg`
- **Hook:** EASTERN SIERRA. **Last clip:** BISHOP TO MAMMOTH LAKES
- **Caption:** The Eastern Sierra, between Bishop and Mammoth Lakes. Cloud on the ridges, violet in the valley, and snow coming down to meet the scrub.
- **Hashtags:** #easternsierra #mammothlakes #bishopca #landscapephotography
- **Location tag:** Mammoth Lakes, California
- **CTA:** `https://oxhollowmedia.com/prints/cloudbreak-ridge?utm_source=instagram&utm_medium=social&utm_campaign=eastern-sierra`

### Week 2

**Mon 10/26, 2:00 pm, Reel: events (offsites).**
- **Photos:** `events/06-offsite-group-photo.jpg`, `events/20-offsite-smile.jpg`, `events/03-team-celebration.jpg`, `events/08-ping-pong-serve.jpg`, `events/09-garden-party-toast.jpg`, `events/18-garden-twirl.jpg`
- **Hook:** OFFSITES, IN BETWEEN THE AGENDA
- **Caption:** The group photo matters. So does the ping-pong serve and the toast after. Offsite coverage starts with The Session (half day).
- **Hashtags:** #teamoffsite #corporateevents #bayareaevents #eventphotography
- **CTA:** `https://oxhollowmedia.com/work-with-me?utm_source=instagram&utm_medium=social&utm_campaign=offsites`

**Tue 10/27, 1:00 pm, Carousel: conservation films.**
- **Slides:** 4-5 stills you export from Ocean Defenders (TODO(Logan)), then a green end card reading WATCH ON OXHOLLOWMEDIA.COM/FILMS
- **Hook:** LOST GEAR, FOUND PARTNERS
- **Caption:** Ocean Defenders follows Kurt Lieber, founder of Ocean Defenders Alliance, working with fishermen in Southern California to recover lost fishing gear and return it to its owners. The film is on my site.
- **Collab:** invite @[Ocean Defenders Alliance handle] as a collaborator (see section 5).
- **Hashtags:** #oceanconservation #documentary #ghostgear #conservationfilm
- **CTA:** `https://oxhollowmedia.com/films?utm_source=instagram&utm_medium=social&utm_campaign=ocean-defenders`

**Wed 10/28, 12:00 pm, Reel: print stories (Seattle).**
- **Photos:** `mountains/04-fog-forest.jpg`, `mountains/02-highland-river.jpg`, `mountains/03-misty-ridgeline.jpg`, `mountains/12-forest-fungus.jpg`, `mountains/06-winter-bark.jpg`, `mountains/10-rainier-afterglow.jpg`
- **Hook:** FOG, MOSS, THEN RAINIER
- **Caption:** Around Seattle the light stays soft for days. Fog in the forest, a river through the highlands, and one evening when Rainier held the last of it.
- **Hashtags:** #pacificnorthwest #mountrainier #landscapephotography #fineartprints
- **CTA:** `https://oxhollowmedia.com/prints/rainier-afterglow?utm_source=instagram&utm_medium=social&utm_campaign=seattle`

**Thu 10/29, 9:00 am, Reel: events (what you receive).**
- **Photos:** `events/01-gala-conversation.jpg`, `events/12-awards-embrace.jpg`, `events/17-evening-toast.jpg`, `events/07-come-play-neon.jpg`, `events/05-evening-reception.jpg`
- **Hook:** ABOUT 100 EDITED PHOTOS PER HOUR
- **Caption:** About 100 edited photos for every hour of coverage. Highlights the same week, the full gallery in five business days, and the photos are yours to use however you like.
- **Hashtags:** #eventphotographer #sfevents #corporateevents #bayareaphotographer
- **CTA:** `https://oxhollowmedia.com/events?utm_source=instagram&utm_medium=social&utm_campaign=turnaround`

### Week 3

**Mon 11/2, 2:00 pm, Reel: events (details).**
- **Photos:** `events/13-ferry-building-tower.jpg`, `events/16-ferry-building-lunch.jpg`, `events/19-sushi-platter.jpg`, `events/15-through-the-leaves.jpg`, `events/14-team-portrait.jpg`
- **Hook:** THE DETAILS COUNT TOO
- **Caption:** The table, the room, the view out the window. Planners use these frames as much as the keynote.
- **Hashtags:** #eventdetails #sanfrancisco #eventphotography #ferrybuilding
- **Location tag:** Ferry Building (only if that is where the event was; TODO(Logan))
- **CTA:** `https://oxhollowmedia.com/events?utm_source=instagram&utm_medium=social&utm_campaign=details`

**Tue 11/3, 1:00 pm, Carousel: print stories (Colorado).**
- **Slides:** `mountains/24-aspen-and-cobalt.jpg`, `mountains/25-sunflare-oak.jpg`, `mountains/26-autumn-against-blue.jpg`, `mountains/27-still-pond.jpg`, then a framed mockup of Aspen and Cobalt
- **Hook:** AUTUMN IN THE ROCKIES
- **Caption:** Four from the Colorado Rockies. Aspen against a cobalt sky, oak in flare, and a pond that stayed still long enough.
- **Hashtags:** #coloradoautumn #rockymountains #aspens #fineartprints
- **CTA:** `https://oxhollowmedia.com/prints/aspen-and-cobalt?utm_source=instagram&utm_medium=social&utm_campaign=colorado-autumn`

**Wed 11/4, 12:00 pm, Reel: place (San Francisco).**
- **Photos:** `ocean/07-golden-gate-fog.jpg` (International Orange), `ocean/08-golden-gate-paddler.jpg`, `people/06-city-thunderheads.jpg`, `urban/04-glass-spire.jpg`, `urban/05-mural-sundown.jpg`
- **Hook:** HOME, IN THE FOG
- **Caption:** San Francisco, where I'm based. Fog through the Gate, a paddler under it, and the city when the weather turns.
- **Hashtags:** #sanfrancisco #goldengatebridge #karlthefog #bayarea
- **Location tag:** San Francisco
- **CTA:** `https://oxhollowmedia.com/prints/international-orange?utm_source=instagram&utm_medium=social&utm_campaign=sf-fog`

**Thu 11/5, 9:00 am, Reel: behind the scenes (new footage; shot list in section 7).**
- **Hook:** HOW I WORK A ROOM
- **Caption:** Quiet, out of the way, near the light. This is most of the job.
- **Hashtags:** #behindthescenes #eventphotographer #bayareaphotographer
- **CTA:** `https://oxhollowmedia.com/work-with-me?utm_source=instagram&utm_medium=social&utm_campaign=bts`

### Week 4

**Mon 11/9, 2:00 pm, Reel: events (holiday parties).**
- **Photos:** `events/17-evening-toast.jpg`, `events/07-come-play-neon.jpg`, `urban/01-cocktails-neon.jpg`, `events/03-team-celebration.jpg`, `events/12-awards-embrace.jpg`
- **Hook:** HOLIDAY PARTY SEASON
- **Caption:** Booking company holiday parties now. If your date is close, I offer a rush option. Booking at least 24 hours ahead helps.
- **Hashtags:** #holidayparty #companyparty #sfevents #eventphotography
- **CTA:** `https://oxhollowmedia.com/work-with-me?utm_source=instagram&utm_medium=social&utm_campaign=holiday-parties`

**Tue 11/10, 1:00 pm, Carousel: print stories (gifts).**
- **Slides:** framed mockups of Humpback Breach, Sea Lion Pup, Rainier Afterglow, Cloudbreak Ridge and International Orange, then a cream end card
- **Hook:** PRINTS FOR THE HOLIDAYS
- **Caption:** Framed in black, white or oak, or as canvas, paper, wood or acrylic. Printed and shipped for you. TODO(Logan): add the last order date once the Gelato holiday cut-off is known.
- **Hashtags:** #giftideas #fineartprints #wallart #holidaygifts
- **CTA:** `https://oxhollowmedia.com/gallery?utm_source=instagram&utm_medium=social&utm_campaign=holiday-2026`

**Wed 11/11, 12:00 pm, Reel: conservation films.**
- **Clip:** a 15-20 second cut from Brushstrokes For Survival (TODO(Logan): your own footage, with the film's music muted)
- **Hook:** PAINT FOR STEELHEAD
- **Caption:** Brushstrokes For Survival follows Nate Irwin, a conservationist turned artist, painting with family to draw attention to critically endangered steelhead in the Santa Ynez River Valley.
- **Hashtags:** #steelhead #conservationfilm #santaynez #documentary
- **CTA:** `https://oxhollowmedia.com/films?utm_source=instagram&utm_medium=social&utm_campaign=brushstrokes`

**Thu 11/12, 9:00 am, Reel: print stories (Sierra light).**
- **Photos:** `mountains/21-blue-hour-ridge.jpg`, `mountains/22-fog-on-the-flats.jpg`, `mountains/23-golden-brush.jpg`, `mountains/20-autumn-flats.jpg`, `mountains/17-snowline.jpg`
- **Hook:** SAME RANGE, DIFFERENT HOUR
- **Caption:** Blue hour on the ridge, fog on the flats, then gold in the brush. One range in the Eastern Sierra, changing all day.
- **Hashtags:** #easternsierra #bluehour #landscapephotography #fineartprints
- **CTA:** `https://oxhollowmedia.com/prints/blue-hour-ridge?utm_source=instagram&utm_medium=social&utm_campaign=blue-hour`

## 5. Follower growth at $0, and a weekly 15-minute routine

**Tactics:**
- **Collab posts with past clients:** Ocean Defenders Alliance, Conservation Made Simple, Illuminate Conservation and Bucket Brigade are named clients. A collab shows the post on both profiles once the partner accepts [S6] (third-party; check in the app). Ask first, in the same message as the referral ask.
- **Trial Reels:** use them on print Reels to test hooks on non-followers without crowding your grid [S5].
- **Location tags:** use specific places only: San Francisco, Mammoth Lakes, Bishop, Galápagos. Event venues only when the client is fine with it.
- **Local event accounts:** follow and leave real comments on 5 accounts a week. Venues: The Midway, Fort Mason. Organizers: QCon SF. Also SF meetup and tech-event accounts. Write one specific sentence, never "great post".
- **Tag credits:** after every event, tag the venue and planner (with the client's OK). Their reshares reach exactly the planners you want.
- **Stories:** reshare every new post to Stories, and add a link sticker carrying the same UTM.
- **Profile:** keep the bio to one line plus /links. Pin 3 posts (see section 1).

**Weekly routine (15 min, Monday after posting):**
1. 3 min: reply to every comment and DM.
2. 5 min: comment on 5 local event or venue accounts and 2 conservation accounts.
3. 3 min: post 1-2 Stories (BTS or a poll) and reshare the day's Reel.
4. 2 min: note the numbers in section 8.
5. 2 min: check next week's drafts and pick the trending audio.

## 6. Reel build commands (not run: ffmpeg is missing)

```
P=images/portfolio
python3 scripts/make_reel.py team/drafts/reels/2026-10-19-1.mp4 $P/events/02-keynote.jpg "What a day of coverage looks like" $P/events/10-tech-talk.jpg "" $P/events/11-stage-qa.jpg "" $P/events/04-industry-mingle.jpg "" $P/events/05-evening-reception.jpg "" $P/events/14-team-portrait.jpg "Highlights within the week"
python3 scripts/make_reel.py team/drafts/reels/2026-10-21-2.mp4 $P/ocean/04-blue-footed-booby.jpg "Galápagos, 2021" $P/ocean/03-sea-lion-pup.jpg "" $P/ocean/12-marine-iguana.jpg "" $P/ocean/02-shark-silhouette.jpg "" $P/ocean/01-humpback-breach.jpg "Five prints from one trip"
python3 scripts/make_reel.py team/drafts/reels/2026-10-22-3.mp4 $P/mountains/16-cloudbreak-ridge.jpg "Eastern Sierra" $P/mountains/14-sierra-river-bend.jpg "" $P/mountains/15-valley-in-violet.jpg "" $P/mountains/17-snowline.jpg "" $P/mountains/18-the-long-valley.jpg "" $P/mountains/19-range-and-scrub.jpg "Bishop to Mammoth Lakes"
```

The portfolio copies carry the watermark. For watermark-free Reels, point these commands at your originals.

## 7. Footage to film (for the 11/5 behind-the-scenes Reel)

Film at your next event. Use 10-second clips, vertical, on a phone held by a friend or clipped to a stand:
1. Your hands changing a lens or card at the side of the room.
2. A wide shot of you shooting from a low angle near a window or the stage edge.
3. Over your shoulder: the back-of-camera screen as you take a candid.
4. You walking the room between sessions, slow and out of the way.
5. Laptop at the end of the night, culling. This is the "same-week highlights" moment.

Only film guests who have agreed to it. Keep client logos out unless the client OKs them.

## 8. What to track weekly

**Metricool** (once Instagram is connected; these field IDs exist in its API):
- **Followers:** IGEV01 (followers), IGEV43 / IGEV44 (gained / lost).
- **Reach and interactions:** IGEV06 (account reach), IGEV26 (Reels reach), IGEV39 / IGEV40 (Reels / posts shares), IGEV15 / IGEV29 (saves), IGEV42 (accounts engaged).
- **Per-Reel:** best time to post (re-run it every month), plus watch time and skip rate in the Reels connector [S7].

**GA4 or Cloudflare analytics:**
- **Traffic:** sessions where source is instagram and medium is social, by `utm_campaign`, landing on /events, /work-with-me and /prints/*.
- **Leads:** contact-form submits and the "How did you hear about me?" answer "Instagram", once that field ships.
- **Print sales:** orders whose cart `ref=` is instagram, once that ships.

**Two ratios to act on:**
- **Shares + saves per 1,000 reach:** a Reel that does well here is worth a repeat, or a boost later.
- **Bio link taps → /events sessions → inquiries:** this is the Plan A funnel.

## Sources (read 2026-10-13)
- [S1] Instagram 5-hashtag cap announced by @creators on 2025-12-18, per secondary reports: https://www.lilachbullock.com/instagram-hashtag-limit/ and https://later.com/blog/instagram-hashtags/ (the Help Center page itself could not be opened; re-check it in the app).
- [S2] Posting frequency: https://routenote.com/blog/how-often-you-should-post-on-instagram/ (Mosseri: no single right answer, sustainable schedule), https://www.kontentino.com/blog/how-often-to-post-on-instagram/ , https://www.socialcal.app/how-often-to-post-on-instagram (vendor benchmarks, including the Rival IQ 3.69 posts/week median). Third-party; there is no 2026 primary statement from Instagram.
- [S3] Sprout Social, "Best times to post on Instagram in 2026" (updated March 2026): https://sproutsocial.com/insights/best-times-to-post-on-instagram/
- [S4] Buffer, "Best Time to Post on Instagram in 2026" (9.6M posts, July 2026): https://buffer.com/resources/when-is-the-best-time-to-post-on-instagram
- [S5] Meta Newsroom, "Test content with non-followers using Trial Reels": https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first/
- [S6] Collab posts, how-to (third-party): https://help.planable.io/hc/en-us/articles/21715384533148-Instagram-Collabs-posts
- [S7] Metricool MCP, Instagram "evolution" metric list and brand settings (queried 2026-10-13); Meta Instagram Media Insights (Reel metrics): https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights/
- In-repo: `team/BUSINESS.md`, `team/drafts/growth-strategy.md`, `films.html` (film descriptions), `events.html` and `work-with-me.html` (turnaround, ~100 photos/hour, usage), `prints/catalog.json` (slugs), and the brand spec in Logan's memory notes.
