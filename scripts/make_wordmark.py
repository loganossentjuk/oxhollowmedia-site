#!/usr/bin/env python3
"""
Draw the Ox Hollow wordmark as images: OX H◐LLOW, the moon mark standing in as
the first O of HOLLOW, set like the homepage (Cormorant Garamond Medium, capitals,
0.12em tracking, mark 0.74em wide with 0.02em / 0.12em either side).

    python3 scripts/make_wordmark.py

Writes
  brand/watermark/watermark-lockup-white.png   white on transparent, for watermark.py
  brand/logos/wordmark-<ink|green|cream>.png   for share images and documents
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "scripts" / "fonts" / "CormorantGaramond-Medium.ttf"
EM = 400                                   # drawing size; outputs are trimmed
TRACK, MARK_W, MARK_L, MARK_R = .12, .74, .02, .12
COLOURS = {"white": (255, 255, 255), "ink": (35, 33, 32), "green": (41, 65, 50), "cream": (244, 238, 226)}


def mark(size, colour, scale=4):
    """The brand mark (ring + left crescent) from its 100-unit SVG, drawn large then shrunk for clean edges."""
    S = size * scale
    im = Image.new("L", (S, S), 0)
    d = ImageDraw.Draw(im)
    k = S / 100
    r, w = 40 * k, 4.7 * k
    d.ellipse([50 * k - r - w / 2, 50 * k - r - w / 2, 50 * k + r + w / 2, 50 * k + r + w / 2], fill=255)
    d.ellipse([50 * k - r + w / 2, 50 * k - r + w / 2, 50 * k + r - w / 2, 50 * k + r - w / 2], fill=0)
    # crescent: the part of the disc left of the chord at x = 27.25
    disc = Image.new("L", (S, S), 0)
    ImageDraw.Draw(disc).ellipse([50 * k - r, 50 * k - r, 50 * k + r, 50 * k + r], fill=255)
    left = Image.new("L", (S, S), 0)
    ImageDraw.Draw(left).rectangle([0, 0, 27.25 * k, S], fill=255)
    im.paste(255, (0, 0), Image.composite(disc, Image.new("L", (S, S), 0), left))
    im = im.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), colour + (0,))
    out.putalpha(im)
    return out


def wordmark(colour):
    font = ImageFont.truetype(str(FONT), EM)
    track, mw = TRACK * EM, round(MARK_W * EM)
    left, right = "OX H", "LLOW"
    adv = lambda t: font.getlength(t)
    width = sum(adv(c) + track for c in left) + MARK_L * EM + mw + MARK_R * EM + sum(adv(c) + track for c in right)
    asc, desc = font.getmetrics()
    H = asc + desc
    im = Image.new("RGBA", (int(width) + 40, H + 40), colour + (0,))
    d = ImageDraw.Draw(im)
    x, base = 20, 20 + asc
    for c in left:
        d.text((x, base), c, font=font, fill=colour + (255,), anchor="ls"); x += adv(c) + track
    x += MARK_L * EM
    cap = font.getbbox("H", anchor="ls")                   # centre the mark on the capitals, like an O
    cy = base + (cap[1] + cap[3]) / 2
    im.alpha_composite(mark(mw, colour), (round(x), round(cy - mw / 2)))
    x += mw + MARK_R * EM
    for c in right:
        d.text((x, base), c, font=font, fill=colour + (255,), anchor="ls"); x += adv(c) + track
    return im.crop(im.getbbox())


def main():
    out = ROOT / "brand" / "watermark" / "watermark-lockup-white.png"
    wordmark(COLOURS["white"]).save(out)
    print("wrote", out.relative_to(ROOT))
    (ROOT / "brand" / "logos").mkdir(exist_ok=True)
    for name in ("ink", "green", "cream"):
        p = ROOT / "brand" / "logos" / f"wordmark-{name}.png"
        wordmark(COLOURS[name]).save(p)
        print("wrote", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
