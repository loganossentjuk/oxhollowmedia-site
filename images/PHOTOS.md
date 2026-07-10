# Photos — how to add your selects

This folder holds every image the site uses. Drop your ~30 portfolio selects into
the category folders below and the gallery (Phase 2) will pull them in.

## Folder layout

```
images/
├── portfolio/
│   ├── ocean/        ← ocean selects
│   ├── mountains/    ← mountain selects
│   └── people/       ← people selects
├── about/            ← 1 photo of you / behind-the-scenes for the About section
└── PHOTOS.md         ← this file
```

Aim for ~10 per category to hit your 30. It's fine to start with fewer.

## Naming

Use lowercase, hyphenated, descriptive names — no spaces. The filename becomes
part of the caption/alt text and the URL, so make it meaningful:

```
ocean/big-sur-dusk.jpg
mountains/cascade-ridgeline.jpg
people/harbor-fisherman-portrait.jpg
```

Optional: prefix with a number to control display order — `01-`, `02-`, …
(`ocean/01-big-sur-dusk.jpg`).

## File format & size

For **the website** (fast loading — NOT your full-res sell files):

| Setting        | Target                                                    |
|----------------|-----------------------------------------------------------|
| Format         | JPG (or WebP if your export tool supports it)             |
| Long edge      | ~2000 px                                                  |
| Quality        | 80–85%                                                    |
| File size      | under ~500 KB each                                        |
| Color profile  | sRGB (important — Adobe RGB looks dull/washed in browsers)|

> Keep your **full-resolution originals somewhere else** (Lightroom catalog /
> external drive). Those are what we'll send to the print lab and sell as digital
> downloads in later phases — never commit full-res sell files to this repo.

## Quick export presets

- **Lightroom:** Export → JPEG, Quality 80, Color Space sRGB, Resize to Long Edge
  2000 px.
- **Photoshop:** File → Export → Save for Web → JPEG High, convert to sRGB,
  fit to 2000 px.
- **No editor?** Tell me and I'll add a one-command image-optimizer script.

## When you're ready

Add your files, tell me they're in, and I'll build the real category-filtered
gallery in Phase 2.
