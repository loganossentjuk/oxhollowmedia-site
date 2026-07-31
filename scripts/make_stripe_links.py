#!/usr/bin/env python3
"""
Create a Stripe Payment Link for every print x size on the site.

Reads the catalogue straight out of prints/index.html so it can never drift
from what's actually published. Writes stripe-links.json, mapping
"<slug>|<size>" -> checkout URL, ready to wire into the print pages.

    export STRIPE_SECRET_KEY=sk_live_...
    python3 scripts/make_stripe_links.py --dry-run
    python3 scripts/make_stripe_links.py

Safe to re-run: anything already in stripe-links.json is skipped, and the
file is saved after every link so an interruption never loses work.

Standard library only - no pip install needed.
"""
import json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path

SITE = "https://oxhollowmedia.com"
ROOT = Path(__file__).resolve().parent.parent
SIZES = [
    ("8x12",  "8×12″",  5500),
    ("12x18", "12×18″", 10000),
    ("16x24", "16×24″", 17500),
    ("24x36", "24×36″", 32000),
]

DRY = "--dry-run" in sys.argv
KEY = os.environ.get("STRIPE_SECRET_KEY", "")
if not KEY and not DRY:
    sys.exit("STRIPE_SECRET_KEY is not set. Export it first, or pass --dry-run.")


def catalogue():
    """Every print on the index: slug, title, image URL."""
    html = (ROOT / "prints" / "index.html").read_text()
    pat = re.compile(
        r'<a class="print-mat" href="([^"]+)">.*?<img src="([^"]+)".*?<h3>([^<]+)</h3>',
        re.S)
    out = []
    for href, img, title in pat.findall(html):
        title = title.strip()
        slug = (href[len("/prints/"):] if href.startswith("/prints/")
                else re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"))
        out.append({"slug": slug, "title": title, "image": SITE + img})
    return out


def stripe(path, params):
    data = urllib.parse.urlencode(params, doseq=True).encode()
    req = urllib.request.Request(
        "https://api.stripe.com/v1/" + path, data=data,
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Stripe {path} failed: {e.code}\n{e.read().decode()[:400]}")


prints = catalogue()
total = len(prints) * len(SIZES)
print(f"{len(prints)} prints x {len(SIZES)} sizes = {total} payment links")

if DRY:
    for p in prints[:3]:
        for _, label, cents in SIZES:
            print(f"  would create: {p['title']} - {label}  ${cents/100:.2f}")
    print(f"  ... and {total - 12} more. Re-run without --dry-run to create them.")
    sys.exit(0)

out_file = ROOT / "stripe-links.json"
links = json.loads(out_file.read_text()) if out_file.exists() else {}
made = skipped = 0

for p in prints:
    for key, label, cents in SIZES:
        ident = f"{p['slug']}|{key}"
        if ident in links:
            skipped += 1
            continue
        product = stripe("products", {
            "name": f"{p['title']} — {label} archival print",
            "description": "Archival matte fine-art print, made to order. Free US shipping.",
            "images[0]": p["image"],
        })
        price = stripe("prices", {
            "product": product["id"], "unit_amount": str(cents), "currency": "usd",
        })
        link = stripe("payment_links", {
            "line_items[0][price]": price["id"],
            "line_items[0][quantity]": "1",
            "shipping_address_collection[allowed_countries][0]": "US",
            "after_completion[type]": "redirect",
            "after_completion[redirect][url]": f"{SITE}/prints/{p['slug']}?ordered=1",
        })
        links[ident] = link["url"]
        made += 1
        print(f"  ok {ident}  {link['url']}")
        out_file.write_text(json.dumps(links, indent=2))   # save as we go

print(f"\ncreated {made}, skipped {skipped} already present -> stripe-links.json")
