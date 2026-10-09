#!/usr/bin/env python3
"""
Stamp the Ox Hollow watermark (moon + OX HOLLOW, bottom-right) on the site's
display images in images/portfolio/.

Print files come from Dropbox (scripts/gelato_publish.py), never from here,
so prints are never watermarked. The unmarked originals stay in git history.

    python3 scripts/watermark.py            # stamp anything not yet stamped
    python3 scripts/watermark.py --dry-run  # list what would be stamped

Safe to re-run: stamped files are recorded in images/portfolio/.watermarked.json
by content hash, so nothing is stamped twice. Add new photos, run it again.
"""
import hashlib, json, sys
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / "images" / "portfolio"
MARK = ROOT / "brand" / "watermark" / "watermark-horizontal-white.png"
LEDGER = PORTFOLIO / ".watermarked.json"
WIDTH = 0.24      # mark width as a share of image width (0.32 on portrait images)
MARGIN = 0.03     # gap from the edges, share of the shorter side
OPACITY = 0.85


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp(path, mark):
    im = Image.open(path)
    im.load()
    fmt = im.format
    base = im.convert("RGBA")
    w, h = base.size
    short = min(w, h)
    mw = int(w * (WIDTH if w >= h else WIDTH * 4 / 3))
    m = mark.resize((mw, max(1, int(mark.height * mw / mark.width))), Image.LANCZOS)
    alpha = m.split()[3].point(lambda v: int(v * OPACITY))
    m.putalpha(alpha)
    # soft dark halo so the mark reads on bright skies and snow
    halo = Image.new("RGBA", m.size, (0, 0, 0, 0))
    halo.putalpha(alpha.filter(ImageFilter.GaussianBlur(max(2, mw // 120))).point(lambda v: int(v * 0.45)))
    gap = int(short * MARGIN)
    xy = (w - m.width - gap, h - m.height - gap)
    base.alpha_composite(halo, xy)
    base.alpha_composite(m, xy)
    out = base.convert("RGB")
    if fmt == "WEBP":
        out.save(path, "WEBP", quality=82, method=6)
    else:
        out.save(path, "JPEG", quality=86, optimize=True, progressive=True)


def main():
    dry = "--dry-run" in sys.argv
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    mark = Image.open(MARK).convert("RGBA")
    todo = [p for p in sorted(PORTFOLIO.rglob("*")) if p.suffix.lower() in (".jpg", ".jpeg", ".webp")
            and ledger.get(str(p.relative_to(ROOT))) != sha(p)]
    for p in todo:
        rel = str(p.relative_to(ROOT))
        print(("would stamp " if dry else "stamped ") + rel)
        if not dry:
            stamp(p, mark)
            ledger[rel] = sha(p)
    if not dry:
        LEDGER.write_text(json.dumps(ledger, indent=1, sort_keys=True) + "\n")
    print(f"{len(todo)} image(s) {'to stamp' if dry else 'stamped'}")


if __name__ == "__main__":
    main()
