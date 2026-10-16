#!/usr/bin/env python3
"""
Render an Instagram carousel (1080x1350) that reads like a photobook you page through:
closed cloth cover -> title spread -> one photo per spread (or a pair) -> back page colophon.

    python3 scripts/make_photobook.py book.json OUT_DIR

book.json:
{
  "title": "GALÁPAGOS · 2019",            # cover, tracked caps
  "title_page": ["GALÁPAGOS", "2019"],     # big lines on the title page
  "title_note": "Five photographs from the islands",   # italic line under them (optional)
  "colophon_line": "Galápagos Islands, 2019",          # trip / series line on the back page
  "pages": [
    {"layout": "spread", "image": "images/portfolio/ocean/04-blue-footed-booby.jpg",
     "title": "Blue-Footed Display", "detail": "a blue-footed booby, displaying"},
    {"layout": "pair", "left": {...same keys...}, "right": {...}}
  ]
}

Web images in images/portfolio carry the Ox Hollow watermark bottom-right (scripts/watermark.py);
crop_watermark() trims that strip off before the photo is mounted, so no mark shows on the page.
Fonts, colours and the lockup come from make_reel.py. Italic captions use
scripts/fonts/CormorantGaramond-Italic.ttf if present, else a sheared Medium.
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_reel import font, tracked, CREAM, CREAM2, GREEN, LOGO, ROOT  # noqa: E402

W, H = 1080, 1350
INK = (58, 60, 52)
MOON = ROOT / "brand/watermark/watermark-moon-white.png"
ITALIC = ROOT / "scripts/fonts/CormorantGaramond-Italic.ttf"
WM_WIDTH, WM_MARGIN, WM_RATIO = 0.24, 0.03, 434 / 2811   # mirrors scripts/watermark.py

# open-book geometry
BX0, BX1, BY0, BY1 = 44, 1036, 250, 1100
GX = (BX0 + BX1) // 2
MARGIN = 54


# ---------- materials (pure Pillow) ----------
def noise(size, sigma):
    """Gaussian grain as an L image centred on 128."""
    return Image.effect_noise(size, sigma)


def tint(lum, base, k=1.0):
    """Colour an L 'deviation from 128' map around a base RGB."""
    return Image.merge("RGB", [lum.point(lambda v, c=c: int(max(0, min(255, c + (v - 128) * k)))) for c in base])


def table():
    """Cream backdrop with a faint grain and a soft light falloff."""
    c = tint(noise((W, H), 2.2), CREAM2)
    fall = Image.radial_gradient("L").resize((W, round(H * 1.25))).crop((0, round(H * 0.06), W, round(H * 0.06) + H))
    c.paste((60, 56, 44), (0, 0), fall.point(lambda v: int(v * 0.16)))
    return c


def linen(size, base=GREEN):
    """Book cloth: per-row and per-column thread variation plus fine grain."""
    w, h = size
    rows = noise((1, h), 3.5).resize((w, h), Image.NEAREST)
    cols = noise((w, 1), 3.5).resize((w, h), Image.NEAREST)
    lum = ImageChops.add(ImageChops.add(rows, cols, 1, -128), noise((w, h), 5), 1, -128)
    return tint(lum.filter(ImageFilter.GaussianBlur(0.6)), base, 0.9)


def paper(size):
    return tint(noise(size, 1.6), CREAM)


def shadow(canvas, box, blur=26, offset=(0, 16), alpha=110, radius=8):
    m = Image.new("L", canvas.size, 0)
    x0, y0, x1, y1 = box
    ImageDraw.Draw(m).rounded_rectangle((x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]), radius, fill=alpha)
    m = m.filter(ImageFilter.GaussianBlur(blur))
    canvas.paste((30, 34, 28), (0, 0), m)


def recolour(path, width, colour):
    mask = Image.open(path).convert("RGBA").getchannel("A")
    mask = mask.crop(mask.getbbox())
    mask = mask.resize((width, round(mask.height * width / mask.width)), Image.LANCZOS)
    return Image.new("RGB", mask.size, colour), mask


# ---------- type ----------
def italic_font(size):
    if ITALIC.exists():
        return ImageFont.truetype(str(ITALIC), size), False
    return font(size), True


def italic(canvas, xy, text, size, fill, anchor="l"):
    """Draw one italic line; anchor l/c/r on x. Faux-italic by shearing if no italic face."""
    f, fake = italic_font(size)
    d = ImageDraw.Draw(canvas)
    tw = d.textlength(text, font=f)
    asc, desc = f.getmetrics()
    h = asc + desc
    shear = 0.2 if fake else 0
    lw = int(tw + shear * h + 8)
    layer = Image.new("L", (lw, h), 0)
    ImageDraw.Draw(layer).text((2, 0), text, font=f, fill=255)
    if shear:
        layer = layer.transform(layer.size, Image.AFFINE, (1, shear, -shear * h, 0, 1, 0), Image.BICUBIC)
    x, y = xy
    x = {"l": x, "c": x - tw / 2, "r": x - tw}[anchor]
    canvas.paste(Image.new("RGB", layer.size, fill), (round(x), round(y)), layer)
    return tw


def fit_italic_size(text, size, maxw):
    while size > 20:
        f, _ = italic_font(size)
        if ImageDraw.Draw(Image.new("L", (1, 1))).textlength(text, font=f) <= maxw:
            return size
        size -= 1
    return size


def tracked_width(text, f, track):
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    return sum(d.textlength(c, font=f) for c in text) + f.size * track * (len(text) - 1)


def tracked_at(d, x, y, text, f, fill, track, anchor="l"):
    w = tracked_width(text, f, track)
    cx = {"l": x + w / 2, "c": x, "r": x - w / 2}[anchor]
    tracked(d, cx, y, text, f, fill, track)


# ---------- photos ----------
def crop_watermark(im):
    """Trim the bottom strip that holds the corner watermark (see scripts/watermark.py)."""
    w, h = im.size
    mw = w * (WM_WIDTH if w >= h else WM_WIDTH * 4 / 3)
    cut = int(min(w, h) * WM_MARGIN + mw * WM_RATIO + min(w, h) * 0.02)
    return im.crop((0, 0, w, h - cut))


def mount(canvas, src, box, border=10):
    """Fit the photo inside box (keeping its shape), white border, soft contact shadow."""
    im = crop_watermark(Image.open(ROOT / src).convert("RGB"))
    bx0, by0, bx1, by1 = box
    s = min((bx1 - bx0 - 2 * border) / im.width, (by1 - by0 - 2 * border) / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    fw, fh = im.width + 2 * border, im.height + 2 * border
    x = bx0 + (bx1 - bx0 - fw) // 2
    y = by0 + (by1 - by0 - fh) // 2
    shadow(canvas, (x, y, x + fw, y + fh), blur=7, offset=(0, 4), alpha=70, radius=1)
    canvas.paste((252, 251, 247), (x, y, x + fw, y + fh))
    canvas.paste(im, (x + border, y + border))
    return x, y, x + fw, y + fh


# ---------- the book ----------
def open_book(pages=(True, True)):
    """Table, cloth rim, page-block edges and paper for an open spread (or one right page)."""
    c = table()
    lx = BX0 if pages[0] else GX
    rim = (lx - 14, BY0 - 12, BX1 + 14, BY1 + 16)
    shadow(c, rim, blur=30, offset=(0, 20), alpha=120)
    cl = linen((rim[2] - rim[0], rim[3] - rim[1]))
    m = Image.new("L", cl.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, cl.width - 1, cl.height - 1), 7, fill=255)
    c.paste(cl, rim[:2], m)
    d = ImageDraw.Draw(c)
    # page-block edges: thin stacked leaves at the outer sides and the foot
    for i in range(5, 0, -1):
        o = i * 2
        tone = tuple(v - 10 - i * 3 for v in CREAM)
        line = tuple(v - 40 for v in CREAM)
        if pages[0]:
            d.rectangle((BX0 - o, BY0 + o // 2, GX, BY1 + o), fill=tone, outline=line)
        d.rectangle((GX, BY0 + o // 2, BX1 + o, BY1 + o), fill=tone, outline=line)
    c.paste(paper((BX1 - lx, BY1 - BY0)), (lx, BY0))
    if pages[0]:   # the fold itself, drawn under any mounted photo
        ImageDraw.Draw(c).line((GX, BY0, GX, BY1), fill=tuple(v - 46 for v in CREAM), width=1)
    return c


def gutter(c, pages=(True, True)):
    """Soft fold shadow at the spine and a faint darkening at the outer edges."""
    import math
    lx = BX0 if pages[0] else GX
    row = []
    for x in range(lx, BX1):
        dist = abs(x - GX)
        if pages[0]:
            v = 0.16 * math.exp(-dist / 22) + 0.07 * math.exp(-dist / 120) + 0.05 * math.exp(-abs(x - BX0) / 30)
        else:
            v = 0.12 * math.exp(-(x - GX) / 18) + 0.06 * math.exp(-(x - GX) / 120)
        v += 0.05 * math.exp(-abs(x - BX1) / 30)
        row.append(int(min(255, v * 255)))
    m = Image.new("L", (BX1 - lx, 1))
    m.putdata(row)
    c.paste((40, 36, 28), (lx, BY0), m.resize((BX1 - lx, BY1 - BY0)))


def folios(c, left, right):
    d = ImageDraw.Draw(c)
    f = font(24)
    y = BY1 - 52
    if left:
        tracked_at(d, BX0 + MARGIN, y, str(left), f, INK, 0.12, "l")
    if right:
        tracked_at(d, BX1 - MARGIN, y, str(right), f, INK, 0.12, "r")


def caption_row(c, y, x0, x1, title, detail):
    """One caption line split across the fold: title (tracked caps) left, detail (italic) right."""
    d = ImageDraw.Draw(c)
    f = font(23)
    tracked_at(d, x0, y + 6, title.upper(), f, GREEN, 0.14, "l")
    size = fit_italic_size(detail, 31, x1 - GX - 28)
    italic(c, (x1, y), detail, size, INK, "r")


# ---------- slides ----------
def cover(book, out):
    c = table()
    bw, bh = 760, 980
    x0, y0 = (W - bw) // 2, (H - bh) // 2 - 10
    # page block peeking at the fore-edge and foot
    d = ImageDraw.Draw(c)
    shadow(c, (x0, y0, x0 + bw, y0 + bh), blur=34, offset=(10, 26), alpha=140)
    d.rectangle((x0 + 6, y0 + 8, x0 + bw + 5, y0 + bh + 6), fill=tuple(v - 18 for v in CREAM), outline=tuple(v - 48 for v in CREAM))
    for i in (2, 4):
        d.line((x0 + bw + i, y0 + 10, x0 + bw + i, y0 + bh + 4), fill=tuple(v - 38 for v in CREAM))
    cl = linen((bw, bh))
    m = Image.new("L", cl.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, bw - 1, bh - 1), 8, fill=255)
    c.paste(cl, (x0, y0), m)
    # hinge groove + light bevel
    over = Image.new("L", (bw, bh), 0)
    od = ImageDraw.Draw(over)
    od.rectangle((44, 0, 50, bh), fill=60)
    over = over.filter(ImageFilter.GaussianBlur(3))
    c.paste((14, 24, 18), (x0, y0), over)
    hl = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(hl).rectangle((51, 0, 54, bh), fill=26)
    c.paste((255, 255, 255), (x0, y0), hl.filter(ImageFilter.GaussianBlur(1.5)))
    d = ImageDraw.Draw(c)
    cx = x0 + 25 + bw / 2
    size = 60
    while tracked_width(book["title"], font(size), 0.12) > bw * 0.72:
        size -= 2
    tracked(d, cx, y0 + bh * 0.40, book["title"], font(size), CREAM, 0.12)
    col, mk = recolour(MOON, 62, CREAM)
    c.paste(col, (round(cx - mk.width / 2), round(y0 + bh * 0.40 - 120)), mk)
    d.line((cx - 40, y0 + bh * 0.40 + size + 40, cx + 40, y0 + bh * 0.40 + size + 40), fill=CREAM, width=1)
    c.save(out, quality=92)


def title_spread(book, out):
    c = open_book()
    gutter(c)
    d = ImageDraw.Draw(c)
    cx = (GX + BX1) / 2
    col, mk = recolour(MOON, 46, GREEN)
    c.paste(col, (round(cx - mk.width / 2), 520), mk)
    y = 610
    for i, line in enumerate(book["title_page"]):
        f = font(58 if i == 0 else 40)
        tracked(d, cx, y, line, f, GREEN, 0.12)
        y += f.size * 1.35
    if book.get("title_note"):
        size = fit_italic_size(book["title_note"], 30, BX1 - GX - 2 * MARGIN)
        italic(c, (cx, y + 26), book["title_note"], size, INK, "c")
    c.save(out, quality=92)


def spread(page, n, out):
    c = open_book()
    box = (BX0 + MARGIN, BY0 + 70, BX1 - MARGIN, BY1 - 190)
    x0, y0, x1, y1 = mount(c, page["image"], box)
    gutter(c)
    caption_row(c, y1 + 30, x0, x1, page["title"], page["detail"])
    folios(c, n, n + 1)
    c.save(out, quality=92)


def pair(page, n, out):
    c = open_book()
    for side, (px0, px1) in (("left", (BX0 + MARGIN, GX - MARGIN // 2 - 10)), ("right", (GX + MARGIN // 2 + 10, BX1 - MARGIN))):
        p = page[side]
        x0, y0, x1, y1 = mount(c, p["image"], (px0, BY0 + 150, px1, BY1 - 300))
        d = ImageDraw.Draw(c)
        tracked_at(d, x0, y1 + 30, p["title"].upper(), font(21), GREEN, 0.14, "l")
        size = fit_italic_size(p["detail"], 28, x1 - x0)
        italic(c, (x0, y1 + 64), p["detail"], size, INK, "l")
    gutter(c)
    folios(c, n, n + 1)
    c.save(out, quality=92)


def back_page(book, out):
    c = open_book(pages=(False, True))
    gutter(c, pages=(False, True))
    d = ImageDraw.Draw(c)
    cx = (GX + BX1) / 2
    col, mk = recolour(LOGO, 330, GREEN)
    c.paste(col, (round(cx - mk.width / 2), 430), mk)
    y = 430 + mk.height + 70
    d.line((cx - 30, y, cx + 30, y), fill=GREEN, width=1)
    tracked(d, cx, y + 40, "PRINTS FROM THIS BOOK", font(24), GREEN, 0.14)
    tracked(d, cx, y + 82, "oxhollowmedia.com/prints", font(30), INK, 0.04)
    size = fit_italic_size(book["colophon_line"], 30, BX1 - GX - 2 * MARGIN)
    italic(c, (cx, y + 170), book["colophon_line"], size, INK, "c")
    # centre the lone page (with its rim and shadow) on the slide
    box = (GX - 14, BY0 - 12, BX1 + 14, BY1 + 16)
    page = c.crop(box)
    bg = table()
    x = (W - page.width) // 2
    shadow(bg, (x, box[1], x + page.width, box[3]), blur=30, offset=(0, 20), alpha=120)
    m = Image.new("L", page.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, page.width - 1, page.height - 1), 7, fill=255)
    bg.paste(page, (x, box[1]), m)
    bg.save(out, quality=92)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    book = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    i = 1
    cover(book, out / f"{i}-cover.jpg"); i += 1
    title_spread(book, out / f"{i}-title.jpg"); i += 1
    folio = 4
    for p in book["pages"]:
        name = (p.get("image") or p["left"]["image"]).split("/")[-1].split(".")[0].lstrip("0123456789-")
        (spread if p["layout"] == "spread" else pair)(p, folio, out / f"{i}-{name}.jpg")
        i += 1
        folio += 2
    back_page(book, out / f"{i}-back.jpg")
    print(f"{i} slides -> {out}")


if __name__ == "__main__":
    main()
