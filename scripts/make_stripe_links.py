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
# Each print's sizes come from its shape, so every size matches the photo.
SIZE_SETS = {shape: [(z["key"], z["label"], z["price"] * 100) for z in zs]
             for shape, zs in CATALOG["size_sets"].items()}

API_VERSION = "2026-06-24.dahlia"
TAX_CODE = "txcd_99999999"   # general tangible goods; used once Stripe Tax is on

DRY = "--dry-run" in sys.argv
KEY = os.environ.get("STRIPE_API_KEY") or os.environ.get("STRIPE_SECRET_KEY", "")
# The example from the docs ("rk_test_..." / "...yourActualKeyHere") is not a key.
if KEY and (KEY.endswith(("...", "Here")) or len(KEY) < 30):
    KEY = ""
if not KEY and not DRY:
    if not sys.stdin.isatty():
        sys.exit("No Stripe key found. Run: export STRIPE_API_KEY=<your rk_test_ key>, or pass --dry-run.")
    import getpass
    print("Copy your restricted key from Stripe (Developers > API keys > print-shop-links, copy icon).")
    KEY = getpass.getpass("Paste it here and press Enter (it won't show on screen): ").strip()
    if not KEY:
        sys.exit("No key entered.")
if KEY and not KEY.startswith(("rk_", "sk_")):
    sys.exit("That doesn't look like a Stripe API key (expected rk_... or sk_...).")
MODE = "live" if "_live_" in KEY else "test"


def catalogue():
    """Every print in the shop: slug, title, absolute image URL."""
    return [{"slug": p["slug"], "title": p["title"], "image": SITE + p["image"],
             "sizes": SIZE_SETS[p["shape"]]} for p in CATALOG["prints"]]


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


def stripe_list(path, query):
    """Every object from a list endpoint, following pagination."""
    out, after = [], None
    while True:
        q = dict(query, limit="100", **({"starting_after": after} if after else {}))
        req = urllib.request.Request(
            f"https://api.stripe.com/v1/{path}?" + urllib.parse.urlencode(q),
            headers={"Authorization": "Bearer " + KEY, "Stripe-Version": API_VERSION})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                page = json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit(f"Stripe {path} failed: {e.code}\n{e.read().decode()[:400]}")
        out += page["data"]
        if not page.get("has_more"):
            return out
        after = page["data"][-1]["id"]


prints = catalogue()
wanted = {f"{p['slug']}|{k}" for p in prints for k, _, _ in p["sizes"]}
out_file = ROOT / "stripe-links.json"
links = json.loads(out_file.read_text()) if out_file.exists() else {}
stale = sorted(set(links) - wanted)
todo = sorted(wanted - set(links))
print(f"{len(prints)} prints, {len(wanted)} payment links: {len(todo)} to create, "
      f"{len(stale)} to retire" + ("" if DRY else f" ({MODE} mode)"))

if DRY:
    for p in prints:
        for key, label, cents in p["sizes"]:
            if f"{p['slug']}|{key}" in todo:
                print(f"  would create: {p['title']} - {label}  ${cents/100:.2f}")
    for ident in stale:
        print(f"  would retire:  {ident}")
    sys.exit(0)

made = skipped = 0

for p in prints:
    for key, label, cents in p["sizes"]:
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

# Retire links for sizes a print no longer offers: deactivate them in Stripe
# so an old URL can't take an order, then drop them from the file.
retired = 0
if stale:
    by_ident = {f"{l['metadata'].get('slug')}|{l['metadata'].get('size')}": l
                for l in stripe_list("payment_links", {"active": "true"})}
    for ident in stale:
        l = by_ident.get(ident)
        if l:
            stripe(f"payment_links/{l['id']}", {"active": "false"}, f"retire-{l['id']}")
        links.pop(ident)
        retired += 1
        print(f"  retired {ident}" + ("" if l else " (not active in Stripe)"))
    out_file.write_text(json.dumps(links, indent=2))

print(f"\ncreated {made}, skipped {skipped} already present, retired {retired} -> stripe-links.json")
