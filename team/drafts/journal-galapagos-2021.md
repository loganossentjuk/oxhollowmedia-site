# Journal entry 1: The Galápagos, 2021

Status: DRAFT for Logan. Not published. Nothing here is on the site yet.

How this was written: the repo confirms only that five prints were made in the Galápagos Islands in 2021, plus each print's title and alt text. Everything personal (how I got there, who with, what I used, what happened) is a `TODO(Logan)`. I kept the prose short on purpose, so your answers can slot in. Delete any sentence that does not sound like you.

Suggested meta title: The Galápagos, 2021 | Ox Hollow Media Journal
Suggested meta description: The story behind five wildlife prints made in the Galápagos Islands in 2021.

---

## The Galápagos, 2021

In 2021 I went to the Galápagos Islands. TODO(Logan): how long, which islands, what month.

I came home with five photographs I wanted to print. A bird, a sea lion pup, an iguana, a shark along a reef, and a whale in the air. This is the story behind each one.

TODO(Logan): one or two sentences on why you went and what you hoped to photograph. (Keep it plain: the reason, not the pitch.)

### How I worked there

TODO(Logan): how you got around (boat, day trips, on foot). Say only what is true.
TODO(Logan): the rules you worked under. Research note: the Galápagos National Park Directorate asks visitors to keep about two metres from wildlife, stay on marked trails, go with a licensed guide and use no flash on animals. If you want to say "I kept my distance", confirm it is true for these five frames.
TODO(Logan): the gear you carried, if you want to name it. Skip it if not.

### Blue-footed Booby

A blue-footed booby displaying in the Galápagos. The photograph is a 3:2 frame.

TODO(Logan): which island and what time of day.
TODO(Logan): what the bird was doing in the seconds before the frame. What did you wait for?
TODO(Logan): how close you were, in your own words.

Print: [Blue-Footed Booby](/prints/blue-footed-booby)

### Sea Lion Pup

A sea lion pup resting on the sand.

TODO(Logan): where this was and what time of day.
TODO(Logan): what the pup and the other animals around it were doing. Were you sitting, crouching, lying down?
TODO(Logan): one concrete detail you remember (sound, smell, the sand, the light).

Print: [Sea Lion Pup](/prints/sea-lion-pup)

### Marine Iguana

A marine iguana resting on sun-bleached rock. This one is a wide 2:1 crop, which suits a long, low animal on a flat stone.

TODO(Logan): where and when.
TODO(Logan): why you chose the wide crop, or whether the scene was already wide.
TODO(Logan): what the iguana did while you were there.

Print: [Marine Iguana](/prints/marine-iguana)

### Reef Passage

A shark gliding through hazy blue water beside a reef wall.

TODO(Logan): did you photograph this while snorkelling or diving? Which site? (Do not guess. I have not claimed either.)
TODO(Logan): what kind of shark, if you know.
TODO(Logan): how long it was in view, and what the water was like.

Print: [Reef Passage](/prints/reef-passage)

### Humpback Breach

A humpback whale breaching in open blue water.

TODO(Logan): was this shot from a boat, and what was the sea like?
TODO(Logan): how long you waited, and whether you knew it was coming.
TODO(Logan): the month, if you know it.

Print: [Humpback Breach](/prints/humpback-breach)

### What I took from it

TODO(Logan): two or three sentences, in your voice, on what the trip changed or confirmed about how you photograph. Optional: connect to the film work (/films), but only if true.

---

Closing links (no changes needed):
- See all five prints in the [gallery](/gallery).
- Each print page has framed, canvas and paper options. Prices stay on the print pages; none are quoted in this entry.

---

## Questions for Logan (short list)

1. Dates: which month(s) in 2021, and how many days?
2. Islands or sites for each of the five frames?
3. How did you get around: boat, tour, on foot? Anyone with you you want to name (or not)?
4. Gear: name it, or leave it out?
5. Booby: what was it doing, and how close were you?
6. Sea lion pup: what were you doing when you took it, and one detail you remember?
7. Marine iguana: why the wide 2:1 crop?
8. Reef Passage: snorkelling or diving? Species of shark?
9. Humpback: from what, and how long did you wait?
10. Why the Galápagos, and what did you take from it?

## Facts used from the repo

- Galápagos Islands, 2021, five prints: BUSINESS.md.
- Titles, slugs, alt text and aspect ratios: `prints/catalog.json` (`blue-footed-booby`, `sea-lion-pup`, `marine-iguana`, `reef-passage`, `humpback-breach`).
- Catalog `lede` and `story` fields are empty for all five. Once you answer, the same text can fill them (then run `python3 scripts/build_print_pages.py`; not done here).

## Proposed /journal page design (structure only, for review)

Purpose: a quiet home for stories behind the prints and guides for event clients. No new look. It reuses the existing site header, footer and type.

**/journal (index)**
- H1: "Journal". One-line intro in your voice, for example "Stories behind the prints, and notes for people hiring me."
- Two filter links above the list: "Stories" and "For event clients". Plain links, no script needed.
- List of entries, newest first. Each row: small image (the lead print, from `images/portfolio`), title (H2), date, one-sentence summary, "Read" link.
- Entry 1 sits first: The Galápagos, 2021. The event-brief guide follows once drafted.

**/journal/galapagos-2021 (entry page)**
- H1: entry title. Date line under it. TODO(Logan): publication date.
- Lead image: Humpback Breach or the booby (your pick), with alt text.
- Body in short paragraphs. One H2 per print, each with a small image, alt text and a link to the print page.
- Closing block: "See these prints" with five thumbnail links, then a link to the gallery.
- Previous / next entry links at the bottom.

**Technical notes for the web engineer / SEO specialist (not for Logan to decide)**
- Static HTML files like the rest of the site. Add to the sitemap and the main nav only after Logan approves.
- Article JSON-LD on entry pages (headline, datePublished, author = Logan Ossentjuk, image).
- Each print page could get a "Read the story" link back to its entry (via the catalog `story` field or a new field). That needs a catalog or script change, so it is a request to the manager, not done here.

## Sources (read 2026-10-12)

- https://www.galapagos.org/travel/park-rules/ : Galápagos National Park Directorate rules (distance from wildlife, marked trails, licensed guide, no flash). Used only to prompt the "how I worked" question. Nothing from it is stated as fact in the entry. Search summary also drew on tour-operator pages (Ecoventura, Intrepid); I did not use them, and some of their rules are operator-specific.
- https://etbtravelphotography.com/how-to-keep-a-travel-journal-that-tells-a-story/ : advice to build an entry around specific moments and one theme. Used for structure only.
- https://www.ilexinstant.com/photo-back-story-blogs/ : photo back-story posts, one image per section. Used for the one-H2-per-print structure.
- Search results only; I did not open the full pages for the last two.
