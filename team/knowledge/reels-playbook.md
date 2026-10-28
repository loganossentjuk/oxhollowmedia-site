# Reels playbook (weekly, automated, Logan approves only)

Sources: `research-tech-events-and-reels.md` §4 and `instagram-growth.md` (2026-10). Logan's choice is **approve only**: the team builds everything from the library, and Logan adds a trending sound in Instagram/Edits and posts or approves scheduling.

## What Instagram rewards
- **Ranking signals:** watch time, sends (DM shares) and likes are the top three. Sends matter most for reaching non-followers, which is nearly all our reach at ~70 followers.
- **Hook:** it lands in the first 1–2 s as on-screen text and motion.
- **Originality:** since about 2026-04-30, accounts that mostly post reused content aren't recommended. Always export clean masters, never a TikTok-watermarked file.
- **Trial Reels:** test 2–3 hook variants with non-followers, then promote the winner.

## Formats the team builds by script (pick 5–7 a week, rotate)
| # | Format | Length | Built from | Script status |
|---|---|---|---|---|
| 1 | One-photo seamless loop (slow push, loops cleanly, rewatch bait) | 5–8 s | one still | extend `make_reel.py` (`--loop`) |
| 2 | Original → edited reveal (wipe or cut on the beat) | 8–12 s | original + edited pair | needs pairs; the original-vs-edited job finds them |
| 3 | Before/after slider | 8–10 s | pair | new: `make_reel.py --wipe` |
| 4 | "Where is this?" tight crop → full frame + place name | 8–12 s | one still | new: crop-zoom-out |
| 5 | Map zoom-in intro → photo | 10–15 s | map tile + still | later |
| 6 | "POV: you…" text hook over a sequence | 10–15 s | 3–5 stills | `make_reel.py` today |
| 7 | "1, 2 or 3?" vote (drives comments) | 8–12 s | 3 stills | `make_reel.py` today |
| 8 | 3D parallax ("photo comes alive") | 6–10 s | one still + depth map (DepthFlow) | new; check edges by eye |
| 9 | Beat-synced photo dump of a place or trip | 15–30 s | 8–15 stills | `make_reel.py` + tempo tag for Logan's sound |
| 10 | Settings overlay ("1/1000 · f/8 · 200mm") | 8–12 s | still + EXIF | new: read EXIF, overlay |
| 11 | Salt and Stone "what am I looking at?" (abstract → reveal) | 8–12 s | abstract + wider frame | `make_reel.py` |
| 12 | Ambient clip with real ocean sound, no music | 8–15 s | existing video | ffmpeg trim |
| 13 | Event recap as an Instagram Collab with the organiser | 20–40 s | event photos (OK'd faces only) | `make_reel.py`; Logan sends the Collab invite |

**Needs Logan, rarely:** a story-time voice memo (30 s on the phone), a Lightroom screen recording, and a behind-the-scenes clip from a shoot.

## Every Reel ships with
- The hook text in the first frame.
- A cover frame.
- A caption: place and subject in plain words in the first line, then one line of story, then the CTA (save, send to someone, or the print link with a UTM), then 3–5 specific hashtags and a location tag.
- A **mood and tempo tag** for the sound, e.g. "slow ambient, 70–90 bpm", plus 2 trending-sound suggestions found that week (Instagram Reels trends / Edits Inspirations; TikTok Creative Center for TikTok).
- Silent MP4 masters only, since music can't be licensed into the file.

## Weekly loop
1. **Sunday batch job:**
   - Read last week's numbers in Metricool: reach, % non-follower, sends, saves, watch time.
   - Pick the formats with the best sends per reach.
   - Render 5–7 Reels plus 1 carousel into `Dropbox/…/Instagram Drafts/<date> Week batch/`.
   - For the 2 strongest ideas, include 2 hook variants as Trial Reels.
2. **Logan approves.** He adds a sound in Instagram/Edits and posts, or approves and Metricool schedules.
3. **Monday report:** which format won and why. Keep doing what wins.
