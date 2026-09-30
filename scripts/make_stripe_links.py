#!/usr/bin/env python3
"""
Create a Stripe Payment Link for every print x size on the site.

Reads prints/catalog.json, the same file scripts/build_print_pages.py builds
the shop from, so the links always match the print pages. Writes
stripe-links.json, mapping "<slug>|<size>" -> checkout URL; js/print-buy.js
(print pages) and js/gallery.js (gallery viewer) read it.

    export STRIPE_API_KEY=rk_test_...
    python3 scripts/make_stripe_links.py --dry-run
    python3 scripts/make_stripe_links.py

Use a restricted key (rk_) with write access to Products, Prices and Payment
Links only. A full secret key (sk_) also works but can do far more if leaked.
Keep the key in your shell, never in a file in this repo.

Safe to re-run: anything already in stripe-links.json is skipped, every
create call carries an idempotency key so a retried request can't make a
duplicate, and the file is saved after every link so an interruption never
loses work.

Standard library only - no pip install needed.
"""
import json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path

SITE = "https://oxhollowmedia.com"
ROOT = Path(__file__).resolve().parent.parent
CATALOG = json.loads((ROOT / "prints" / "catalog.json").read_text())
SIZES = [(z["key"], z["label"], z["price"] * 100) for z in CATALOG["sizes"]]

API_VERSION = "2026-06-24.dahlia"
TAX_CODE = "txcd_99999999"   # general tangible goods; used once Stripe Tax is on

DRY = "--dry-run" in sys.argv
KEY = os.environ.get("STRIPE_API_KEY") or os.environ.get("STRIPE_SECRET_KEY", "")
if not KEY and not DRY:
    sys.exit("STRIPE_API_KEY is not set. Export a restricted key (rk_...) first, or pass --dry-run.")
if KEY and not KEY.startswith(("rk_", "sk_")):
    sys.exit("That doesn't look like a Stripe API key (expected rk_... or sk_...).")
MODE = "live" if "_live_" in KEY else "test"


def catalogue():
    """Every print in the shop: slug, title, absolute image URL."""
    return [{"slug": p["slug"], "title": p["title"], "image": SITE + p["image"]}
            for p in CATALOG["prints"]]


def stripe(path, params, idem):
    data = urllib.parse.urlencode(params, doseq=True).encode()
    req = urllib.request.Request(
        "https://api.stripe.com/v1/" + path, data=data,
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Stripe-Version": API_VERSION,
                 "Idempotency-Key": f"oxhollow-{MODE}-{idem}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Stripe {path} failed: {e.code}\n{e.read().decode()[:400]}")


prints = catalogue()
total = len(prints) * len(SIZES)
print(f"{len(prints)} prints x {len(SIZES)} sizes = {total} payment links" + ("" if DRY else f" ({MODE} mode)"))

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
            "tax_code": TAX_CODE,
        }, f"product-{ident}")
        price = stripe("prices", {
            "product": product["id"], "unit_amount": str(cents), "currency": "usd",
        }, f"price-{ident}")
        link = stripe("payment_links", {
            "metadata[slug]": p["slug"], "metadata[size]": key,
            "line_items[0][price]": price["id"],
            "line_items[0][quantity]": "1",
            "shipping_address_collection[allowed_countries][0]": "US",
            "after_completion[type]": "redirect",
            "after_completion[redirect][url]": f"{SITE}/thank-you",
            "phone_number_collection[enabled]": "true",
        }, f"link-{ident}")
        links[ident] = link["url"]
        made += 1
        print(f"  ok {ident}  {link['url']}")
        out_file.write_text(json.dumps(links, indent=2))   # save as we go

print(f"\ncreated {made}, skipped {skipped} already present -> stripe-links.json")
