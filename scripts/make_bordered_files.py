#!/usr/bin/env python3
"""
Print files for the framed prints with a white border inside the frame.

Gelato's framed poster has no mat: the paper fills the frame. So the border is
built into the file: white paper, the photo centred on it. One file per print
and paper shape it is sold on:

    A4   21 x 29.7 cm   the 8x12" size
    3x2  2:3 paper      12x18, 16x24, 24x36
    sq   square paper   12x12, 16x16, 20x20

Border: 12% of the paper's short side on every side. If the photo is close to
the shape of the space inside the border (centre-cropping it would take 10% of
the photo or less), it is cropped to fit and the border is even all round.
Otherwise the whole photo is kept and the two looser sides get a wider border.

    python3 scripts/make_bordered_files.py                 # every framed print
    python3 scripts/make_bordered_files.py --only shark-shadow

Writes ~/.../PrintMasters/gelato-ready-bordered/<slug>-framed-<A4|3x2|sq>.jpg
(sRGB JPEG, never upscaled past the master, long side at most 10800 px) and
prints which prints got even borders and which got wider sides.
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None

ROOT = Path(__file__).resolve().parent.parent
CAT_PATH = ROOT / "prints" / "catalog.json"
PM = Path.home() / "Library/CloudStorage/Dropbox/Career/OxHollow/PrintMasters"
READY = PM / "gelato-ready"
OUT = PM / "gelato-ready-bordered"
BORDER = 0.12        # of the paper's short side
MAX_CROP = 0.10      # crop to even borders only up to this share of the photo
MAX_PX = 10800
PAPER = {"A4": (297, 210), "3x2": (3, 2), "sq": (1, 1)}   # long, short (ratio is what matters)


def shape_for(size):
    a, b = (int(x) for x in size.split("x"))
    return "sq" if a == b else "A4" if size == "8x12" else "3x2"


def source(p):
    m = p.get("master") or ""
    # the edited high-res TIF, else the gelato-ready JPG ("master" can also be a raw camera file)
    for f in ([PM.parent / m] if "HighResolution" in m else []) + [READY / "HighResolution" / f"{p['slug']}.tif",
                                                                 READY / f"{p['slug']}.jpg"]:
        if f.exists():
            return f
    sys.exit(f"no master for {p['slug']}")


def layout(pw, ph, iw, ih):
    """Paper w/h (any unit), photo w/h px -> (crop box in photo px, photo box on paper as fractions, even?)."""
    b = BORDER * min(pw, ph)
    bw, bh = pw - 2 * b, ph - 2 * b                      # space inside the border
    r_box, r_img = bw / bh, iw / ih
    if r_img > r_box:                                     # photo wider: crop the sides
        keep = r_box / r_img
        crop = (iw * (1 - keep) / 2, 0, iw - iw * (1 - keep) / 2, ih)
    else:                                                 # photo taller: crop top and bottom
        keep = r_img / r_box
        crop = (0, ih * (1 - keep) / 2, iw, ih - ih * (1 - keep) / 2)
    if 1 - keep <= MAX_CROP:
        return crop, (b / pw, b / ph, bw / pw, bh / ph), True
    # keep the whole photo: fit inside the border box, centred
    s = min(bw / iw, bh / ih)
    w, h = iw * s, ih * s
    return (0, 0, iw, ih), ((pw - w) / 2 / pw, (ph - h) / 2 / ph, w / pw, h / ph), False


def make(p, shape, photo):
    land = photo.width >= photo.height
    L, S = PAPER[shape]
    pw, ph = (L, S) if land else (S, L)
    crop, (fx, fy, fw, fh), even = layout(pw, ph, photo.width, photo.height)
    cw, ch = crop[2] - crop[0], crop[3] - crop[1]
    scale = min(1.0, MAX_PX / max(cw / fw, ch / fh))      # paper px from the photo's own resolution
    W, H = round(cw / fw * scale), round(ch / fh * scale)
    page = Image.new("RGB", (W, H), "white")
    pic = photo.crop(tuple(round(v) for v in crop)).resize((round(fw * W), round(fh * H)), Image.LANCZOS)
    page.paste(pic, (round(fx * W), round(fy * H)))
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{p['slug']}-framed-{shape}.jpg"
    page.save(out, quality=95, dpi=(300, 300), subsampling=0)
    return out, even, (1 - (cw * ch) / (photo.width * photo.height))


def main():
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    cat = json.loads(CAT_PATH.read_text())
    even, wide = [], []
    for p in cat["prints"]:
        f = (p.get("shopify") or {}).get("framed")
        if not f or (only and p["slug"] not in only):
            continue
        photo = ImageOps.exif_transpose(Image.open(source(p))).convert("RGB")
        for shape in sorted({shape_for(k) for k in f}):
            out, ok, cropped = make(p, shape, photo)
            (even if ok else wide).append(f"{p['title']} ({shape}{f', {cropped:.0%} cropped' if ok and cropped > 0.005 else ''})")
            print(f"  {out.name}: {'even' if ok else 'wider sides'}", flush=True)
    print(f"\neven border all round ({len(even)}): " + "; ".join(even))
    print(f"\nwhole photo, wider on two sides ({len(wide)}): " + "; ".join(wide))


if __name__ == "__main__":
    main()
