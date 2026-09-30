#!/usr/bin/env python3
"""
Create a Stripe Payment Link for every print x size on the site.

Reads prints/catalog.json, the same file scripts/build_print_pages.py builds
the shop from, so the links always match the print pages. Writes
stripe-links.json, mapping "<slug>|<size>" -> checkout URL; js/print-buy.js
(print pages) and js/gallery.js (gallery viewer) read it.

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
CATALOG = json.loads((ROOT / "prints" / "catalog.json").read_text())
SIZES = [(z["key"], z["label"], z["price"] * 100) for z in CATALOG["sizes"]]

DRY = "--dry-run" in sys.argv
KEY = os.environ.get("STRIPE_SECRET_KEY", "")
if not KEY and not DRY:
    sys.exit("STRIPE_SECRET_KEY is not set. Export it first, or pass --dry-run.")


def catalogue():
    """Every print in the shop: slug, title, absolute image URL."""
    return [{"slug": p["slug"], "title": p["title"], "image": SITE + p["image"]}
            for p in CATALOG["prints"]]


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
    print(f"  ... and {total - 3 * len(SIZES)} more. Re-run without --dry-run to create them.")
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
            "name": f"{p['title']}, {label} archival print",
            "metadata[slug]": p["slug"], "metadata[size]": key,
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
            "after_completion[redirect][url]": f"{SITE}/thank-you",
            "phone_number_collection[enabled]": "true",
        })
        links[ident] = link["url"]
        made += 1
        print(f"  ok {ident}  {link['url']}")
        out_file.write_text(json.dumps(links, indent=2))   # save as we go

print(f"\ncreated {made}, skipped {skipped} already present -> stripe-links.json")
