#!/usr/bin/env python3
"""
Pull Gelato's own product mockups for the wood and acrylic listings into
images/mockups/<slug>-<material>.jpg and record them in the catalog's "previews",
so the print page swaps to them when that material is picked.

    python3 scripts/gelato_previews.py              # wood + acrylic
    python3 scripts/gelato_previews.py --list SLUG  # print the image URLs Gelato has for one print
    python3 scripts/gelato_previews.py --pick N     # use Gelato's Nth image (default 0, the main preview)

Each Gelato store product is matched to the catalog through its variants'
externalId (the Shopify variant ID the website's buy buttons use). Gelato's
mockups show the print unmarked, so the site watermark is stamped on the print
itself in the saved copy (its bottom right corner, same mark and opacity as
scripts/watermark.py). Old combined listings (one Gelato product holding wood
and acrylic together) are skipped: their images don't show a single material.

Key: GELATO_API_KEY in the environment, else the macOS Keychain item
"ohm-gelato-api-key", else paste it at the hidden prompt.
"""
import getpass, io, json, os, shutil, subprocess, sys, urllib.request
from pathlib import Path
from PIL import Image, ImageChops, ImageOps
import watermark as wm
from make_mockups import stamp

ROOT = Path(__file__).resolve().parent.parent
CAT_PATH = ROOT / "prints" / "catalog.json"
OUT = ROOT / "images" / "mockups"
API = "https://ecommerce.gelatoapis.com/v1"
MATS = ("wood", "acrylic")
UA = "OxHollowMedia-PrintShop/1.0 (+https://oxhollowmedia.com)"

KEY = os.environ.get("GELATO_API_KEY", "")
if not KEY and shutil.which("security"):
    r = subprocess.run(["security", "find-generic-password", "-s", "ohm-gelato-api-key", "-w"],
                       capture_output=True, text=True)
    KEY = r.stdout.strip() if r.returncode == 0 else ""
if not KEY:
    KEY = getpass.getpass("Paste your Gelato API key and press Enter (it won't show): ").strip()
if not KEY:
    sys.exit("No key.")


def get(path):
    req = urllib.request.Request(API + path, headers={"X-API-KEY": KEY, "Accept": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
        return r.read()


def images(prod):
    """Every mockup URL Gelato gives for a product, main preview first."""
    urls = [prod.get("previewUrl")] + [i.get("fileUrl") for i in prod.get("productImages") or []]
    seen = []
    for u in urls:
        if u and u not in seen:
            seen.append(u)
    return seen


def mark_print(im, mark):
    """Stamp the watermark on the print, not the white backdrop: find the print as
    the area that differs from the corner colour and stamp inside it."""
    bg = Image.new("RGB", im.size, im.getpixel((2, 2)))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 30 else 0).getbbox()
    if not box:
        return stamp(im, mark)
    out = im.copy()
    out.paste(stamp(im.crop(box), mark), box[:2])
    return out


def main():
    cat = json.loads(CAT_PATH.read_text())
    store = cat["gelato"]["store_id"]
    pick = int(sys.argv[sys.argv.index("--pick") + 1]) if "--pick" in sys.argv else 0
    only = sys.argv[sys.argv.index("--list") + 1] if "--list" in sys.argv else None
    # Shopify variant ID -> (print, material)
    want = {}
    for p in cat["prints"]:
        for m in MATS:
            for v in ((p.get("shopify") or {}).get(m) or {}).values():
                want[str(v["variant"])] = (p, m)
    found, offset = {}, 0
    while True:
        page = get(f"/stores/{store}/products?limit=100&offset={offset}")
        prods = page.get("products") or []
        for pr in prods:
            ids = {str(v.get("externalId")) for v in pr.get("variants") or []}
            hits = [want[i] for i in ids if i in want]
            if len({m for _, m in hits}) > 1:        # old combined listing
                continue
            hit = hits[0] if hits else None
            if hit:
                found.setdefault((hit[0]["slug"], hit[1]), (hit[0], pr["id"]))
        if len(prods) < 100:
            break
        offset += 100
    print(f"{len(found)} wood/acrylic product(s) matched in Gelato")
    OUT.mkdir(parents=True, exist_ok=True)
    mark = Image.open(wm.MARK).convert("RGBA")
    missing = sorted({(p["slug"], m) for p, m in want.values()} - set(found))
    for (slug, m), (p, gid) in sorted(found.items()):
        if only and slug != only:
            continue
        urls = images(get(f"/stores/{store}/products/{gid}"))
        if only:
            print(f"{slug} {m}:"); [print(f"  [{i}] {u}") for i, u in enumerate(urls)]
            continue
        if not urls:
            print(f"  ! {slug} {m}: Gelato has no preview image"); continue
        im = ImageOps.exif_transpose(Image.open(io.BytesIO(fetch(urls[min(pick, len(urls) - 1)])))).convert("RGB")
        im.thumbnail((1200, 1200), Image.LANCZOS)
        name = f"{slug}-{m}.jpg"
        mark_print(im, mark).save(OUT / name, quality=84, optimize=True)
        p.setdefault("previews", {})[m] = f"/images/mockups/{name}"
        print(f"  {slug} {m}: {len(urls)} image(s), saved [{min(pick, len(urls) - 1)}]")
    if missing:
        print("not found in Gelato: " + ", ".join(f"{s} {m}" for s, m in missing))
    if not only:
        CAT_PATH.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
