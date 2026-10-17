#!/usr/bin/env python3
"""
Draw simple framed-print mockups for listings that have no Gelato mockup yet,
in the style of Gelato's own (a frame on white): images/mockups/<slug>-<material>-<colour>.jpg,
recorded in the catalog's "previews" so the print page swaps to them.

    python3 scripts/make_mockups.py                 # framed listings without a preview
    python3 scripts/make_mockups.py --all           # every framed listing (replaces Gelato mockups)
    python3 scripts/make_mockups.py --clean DIR     # unwatermarked <slug>.jpg sources

The photo inside the frame carries the site watermark (same size, corner and
opacity as scripts/watermark.py), so a mockup never shows an unmarked print.
Sources, best first: --clean DIR, the Dropbox gelato-ready file, the site image.
"""
import json, random, sys
import watermark as wm
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
CAT_PATH = ROOT / "prints" / "catalog.json"
OUT = ROOT / "images" / "mockups"
# The unwatermarked print files (as Gelato's mockups use); the site image is a fallback.
READY = Path.home() / "Library/CloudStorage/Dropbox/Career/OxHollow/PrintMasters/gelato-ready"
ORDER = ["8x12", "12x12", "12x18", "16x16", "16x24", "20x20", "24x24", "24x36"]
WOOD = {"oak": (214, 188, 150), "walnut": (92, 62, 42)}
SOLID = {"black": (24, 24, 24), "white": (244, 243, 240)}
S = 1600  # square canvas, like Gelato's


def wood(size, base, seed):
    """Fine vertical-grain texture (rotated for horizontal rails)."""
    rnd = random.Random(seed)
    w, h = size
    im = Image.new("RGB", (w, h), base)
    d = ImageDraw.Draw(im)
    for x in range(w):
        k = rnd.uniform(-14, 10)
        d.line([(x, 0), (x, h)], fill=tuple(max(0, min(255, int(c + k))) for c in base))
    return im.filter(ImageFilter.GaussianBlur(0.6))


def frame_img(colour, size, seed):
    if colour in WOOD:
        return wood(size, WOOD[colour], seed)
    return Image.new("RGB", size, SOLID[colour])


def stamp(pic, mark):
    """The site watermark on the visible photo (as scripts/watermark.py does)."""
    base = pic.convert("RGBA")
    w, h = base.size
    mw = int(w * (wm.WIDTH if w >= h else wm.WIDTH * 4 / 3))
    m = mark.resize((mw, max(1, int(mark.height * mw / mark.width))), Image.LANCZOS)
    alpha = m.split()[3].point(lambda v: int(v * wm.OPACITY))
    m.putalpha(alpha)
    halo = Image.new("RGBA", m.size, (0, 0, 0, 0))
    halo.putalpha(alpha.filter(ImageFilter.GaussianBlur(max(2, mw // 120))).point(lambda v: int(v * 0.45)))
    gap = int(min(w, h) * wm.MARGIN)
    xy = (w - m.width - gap, h - m.height - gap)
    base.alpha_composite(halo, xy)
    base.alpha_composite(m, xy)
    return base.convert("RGB")


def draw(photo, mat, colour, w_in, h_in, mark, mat_frac=0.11):
    canvas = Image.new("RGB", (S, S), "white")
    scale = 0.86 * S / max(w_in, h_in)
    fw, fh = int(w_in * scale), int(h_in * scale)
    x0, y0 = (S - fw) // 2, (S - fh) // 2
    # soft shadow
    sh = Image.new("L", (S, S), 0)
    ImageDraw.Draw(sh).rectangle([x0 + 10, y0 + 18, x0 + fw + 10, y0 + fh + 22], fill=110)
    canvas.paste((0, 0, 0), mask=sh.filter(ImageFilter.GaussianBlur(22)))
    t = int(0.035 * max(fw, fh)) if mat == "framed" else int(0.05 * max(fw, fh))
    # rails: vertical pieces use the texture as is, horizontal ones rotated
    side = frame_img(colour, (t, fh), 1)
    top = frame_img(colour, (fh, t), 2) if colour not in WOOD else wood((t, fw), WOOD[colour], 3).rotate(90, expand=True)
    canvas.paste(side, (x0, y0)); canvas.paste(side, (x0 + fw - t, y0))
    canvas.paste(top.resize((fw, t)), (x0, y0)); canvas.paste(top.resize((fw, t)), (x0, y0 + fh - t))
    d = ImageDraw.Draw(canvas)
    d.rectangle([x0, y0, x0 + fw - 1, y0 + fh - 1], outline=(0, 0, 0), width=1)
    ix0, iy0, ix1, iy1 = x0 + t, y0 + t, x0 + fw - t, y0 + fh - t
    d.rectangle([ix0, iy0, ix1, iy1], outline=(60, 60, 60), width=2)  # inner bevel line
    if mat == "framed":
        d.rectangle([ix0 + 2, iy0 + 2, ix1 - 2, iy1 - 2], fill=(248, 247, 243))  # mat
        m = int(mat_frac * (ix1 - ix0))   # per-print override: catalog "mockup_mat"
        bx0, by0, bx1, by1 = ix0 + m, iy0 + m, ix1 - m, iy1 - m
        pic = photo.copy(); pic.thumbnail((bx1 - bx0, by1 - by0), Image.LANCZOS)   # printed in full
        pic = stamp(pic, mark)
        px, py = bx0 + (bx1 - bx0 - pic.width) // 2, by0 + (by1 - by0 - pic.height) // 2
        canvas.paste(pic, (px, py))
        d.rectangle([px - 1, py - 1, px + pic.width, py + pic.height], outline=(205, 203, 197), width=1)
    else:
        gap = int(0.012 * fw)  # float gap between frame and canvas
        d.rectangle([ix0 + 2, iy0 + 2, ix1 - 2, iy1 - 2], fill=(18, 18, 18))
        bx0, by0, bx1, by1 = ix0 + gap, iy0 + gap, ix1 - gap, iy1 - gap
        bw, bh = bx1 - bx0, by1 - by0
        r = max(bw / photo.width, bh / photo.height)                                 # canvas is filled edge to edge
        pic = photo.resize((int(photo.width * r) + 1, int(photo.height * r) + 1), Image.LANCZOS)
        pic = pic.crop(((pic.width - bw) // 2, (pic.height - bh) // 2, (pic.width - bw) // 2 + bw, (pic.height - bh) // 2 + bh))
        canvas.paste(stamp(pic, mark), (bx0, by0))
    return canvas


def main():
    every = "--all" in sys.argv
    clean = Path(sys.argv[sys.argv.index("--clean") + 1]) if "--clean" in sys.argv else None
    mark = Image.open(wm.MARK).convert("RGBA")
    cat = json.loads(CAT_PATH.read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    made = 0
    for p in cat["prints"]:
        for mat in ("framed", "framed_canvas"):
            e = (p.get("shopify") or {}).get(mat)
            have = (p.get("previews") or {}).get(mat)
            if not e or (have and not every):
                continue
            k = min(e, key=lambda s: ORDER.index(s) if s in ORDER else 99)
            a, b = (int(x) for x in k.split("x"))
            land = p["width"] >= p["height"]
            w_in, h_in = (max(a, b), min(a, b)) if land else (min(a, b), max(a, b))
            src = next((c for c in ([clean / f"{p['slug']}.jpg"] if clean else []) + [READY / f"{p['slug']}.jpg"]
                        if c.exists()), ROOT / p["image"].lstrip("/"))
            photo = Image.open(src)
            photo.draft("RGB", (1600, 1600))
            photo = ImageOps.exif_transpose(photo).convert("RGB")
            photo.thumbnail((1600, 1600), Image.LANCZOS)
            urls = {}
            for colour in e[k]["frames"]:
                name = f"{p['slug']}-{mat.replace('_', '-')}-{colour}.jpg"
                draw(photo, mat, colour, w_in, h_in, mark, p.get("mockup_mat", 0.11)).resize((1200, 1200), Image.LANCZOS).save(OUT / name, quality=84, optimize=True)
                urls[colour] = f"/images/mockups/{name}"
                made += 1
            p.setdefault("previews", {})[mat] = urls
            print(f"  {p['slug']} {mat}: {', '.join(urls)}")
    CAT_PATH.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n")
    print(f"{made} mockup(s) drawn")


if __name__ == "__main__":
    main()
