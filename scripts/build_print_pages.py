#!/usr/bin/env python3
"""
Build the print shop from prints/catalog.json:

  - prints/<slug>.html   one buy page per print (image, sizes, Stripe buttons)
  - prints/index.html    the shop grid, regenerated between the SHOP markers
  - sitemap.xml          one <url> per print page, between the PRINTS markers

    python3 scripts/build_print_pages.py

A print sold framed (its catalog "shopify" entry has "framed") is sold only
through Shopify/Gelato: framed print, framed canvas, wood and acrylic, with
the frames in black, white or oak. Until then, paper buy buttons start as
enquiry links and switch to Stripe checkout at runtime once stripe-links.json
has an entry for "<slug>|<size>" (js/print-buy.js).
Pages for prints removed from the catalogue are deleted, so the folder never
serves a print the shop no longer lists.

Standard library only.
"""
import html, json, re
from datetime import date
from pathlib import Path
from urllib.parse import quote

SITE = "https://oxhollowmedia.com"
ROOT = Path(__file__).resolve().parent.parent
PRINTS = ROOT / "prints"
CAT = json.loads((PRINTS / "catalog.json").read_text())
SIZES, PAPER = CAT["sizes"], CAT["paper"]
PPI = 150   # minimum resolution for a sharp print


def sizes(p):
    """Standard sizes this print's file can support: long side x PPI must fit in source_px."""
    return [z for z in SIZES
            if max(int(n) for n in z["key"].split("x")) * PPI <= p["source_px"]]
CSS_VER = re.search(r'styles\.css\?v=(\d+)', (ROOT / "index.html").read_text()).group(1)

e = lambda s: html.escape(s, quote=True)

# Nav and footer are copied from the shop page so every print page matches it.
index_html = (PRINTS / "index.html").read_text()
NAV = re.search(r'  <!-- ── Navigation ── -->.*?<div class="drawer-overlay" id="overlay"></div>\n',
                index_html, re.S).group(0)
FOOTER = re.search(r'  <!-- ── Footer ── -->.*?</footer>\n', index_html, re.S).group(0)


FRAMES = CAT["gelato"].get("frames", {})
FRAMED = ("framed", "framed_canvas")


def framed(p):
    return bool((p.get("shopify") or {}).get("framed"))


def label(key):
    return key.replace("x", "×") + "″"


def by_size(d):
    return sorted(d.items(), key=lambda kv: int(kv[0].split("x")[0]))


def offers_of(p):
    """(name, price) for every size a print sells: framed prints from Shopify, others on paper."""
    if framed(p):
        return [(f"{label(k)} framed print", v["price"]) for k, v in by_size(p["shopify"]["framed"])]
    return [(f"{s['label']} archival print", s["price"]) for s in sizes(p)]


def spec_line(p):
    if framed(p):
        return "Framed · black, white or oak · " + " · ".join(
            f"{label(k)} ${v['price']}" for k, v in by_size(p["shopify"]["framed"]))
    return "Archival matte paper · " + " · ".join(f"{s['label']} ${s['price']}" for s in sizes(p))


def fit(p):
    """3:2 photos fill the standard (2:3) paper; anything else prints whole with a border."""
    return "printed edge to edge" if p["shape"] == "3:2" else "printed in full with a white border, never cropped"


def lede(p):
    return p["lede"] or p["alt"].rstrip(".") + "."


def product_ld(p):
    url = f"{SITE}/prints/{p['slug']}"
    offers = [{
        "@type": "Offer", "name": name, "price": str(price),
        "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": url,
        "shippingDetails": {"@type": "OfferShippingDetails",
                            "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "USD"},
                            "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"}},
    } for name, price in offers_of(p)]
    return json.dumps({"@context": "https://schema.org", "@type": "Product", "name": p["title"],
                       "description": lede(p), "image": SITE + p["image"],
                       "brand": {"@type": "Brand", "name": "Ox Hollow Media"}, "offers": offers},
                      ensure_ascii=False)


def picture(p, extra=""):
    return (f'<picture><source type="image/webp" srcset="{p["webp"]}"><img src="{p["image"]}" '
            f'width="{p["width"]}" height="{p["height"]}" decoding="async" alt="{e(p["alt"])}"{extra}></picture>')


def more_prints(p):
    same = [q for q in CAT["prints"] if q["category"] == p["category"]]
    i = same.index(p)
    picks = [same[(i + k) % len(same)] for k in range(1, len(same))][:3]
    cards = "".join(f'''
        <div class="print-card">
          <a class="print-mat" href="/prints/{q['slug']}">
            {picture(q, ' loading="lazy"')}
          </a>
          <h3>{e(q['title'])}</h3>
        </div>''' for q in picks)
    return cards


def frame_panel(p, m, by_key):
    """Frame colour swatches (CSS-only radios), each with its own row of size buttons."""
    store, sid = CAT["shopify_store"], f'{p["slug"]}-{m}'
    colours = [c for c in FRAMES if any(c in v["frames"] for v in by_key.values())]
    radios = "".join(
        f'<input type="radio" name="frame-{sid}" id="frame-{sid}-{c}" class="frame-radio"{" checked" if i == 0 else ""}>'
        f'<label for="frame-{sid}-{c}" class="frame-tab"><span class="frame-swatch frame-{c}"></span>{e(FRAMES[c])}</label>'
        for i, c in enumerate(colours))
    panels = ""
    for c in colours:
        rows = "".join(f'''
                  <a class="buy-btn" href="https://{store}/cart/{v['frames'][c]}:1" rel="nofollow">
                    <span class="size">Buy {label(k)}</span><span class="price">${v['price']}</span>
                  </a>''' for k, v in by_size(by_key) if c in v["frames"])
        panels += f'''
                <div class="frame-panel" data-frame="{c}">{rows}
                </div>'''
    return f'''
              <div class="frame-pick"><span class="frame-label">Frame</span>{radios}{panels}
              </div>'''


def materials(p):
    """Framed print / framed canvas / wood / acrylic picker for prints sold through
    Shopify (Gelato fulfils). CSS-only tabs: one radio per material; each size links
    to Shopify checkout. Framed materials add a frame-colour picker inside their
    panel. Plain canvas is hidden once framed canvas replaces it."""
    mats = p.get("shopify")
    if not mats:
        return ""
    store, names = CAT["shopify_store"], CAT["materials"]
    order = [m for m in names if m in mats and not (m == "canvas" and "framed_canvas" in mats)]
    tabs = "".join(
        f'<input type="radio" name="mat-{p["slug"]}" id="mat-{p["slug"]}-{m}" class="mat-radio"{" checked" if i == 0 else ""}>'
        f'<label for="mat-{p["slug"]}-{m}" class="mat-tab">{e(names[m])}</label>'
        for i, m in enumerate(order))
    panels = ""
    for m in order:
        if m in FRAMED:
            panels += f'''
            <div class="mat-panel" data-mat="{m}">{frame_panel(p, m, mats[m])}
            </div>'''
            continue
        rows = "".join(f'''
              <a class="buy-btn" href="https://{store}/cart/{v['variant']}:1" rel="nofollow">
                <span class="size">Buy {key.replace("x", "×")}″</span><span class="price">${v['price']}</span>
              </a>''' for key, v in sorted(mats[m].items(), key=lambda kv: int(kv[0].split("x")[0])))
        panels += f'''
            <div class="mat-panel" data-mat="{m}">{rows}
            </div>'''
    intro = ("Framed and ready to hang, or on wood or acrylic · free US shipping" if framed(p)
             else "Also on canvas, wood or acrylic · printed edge to edge · free US shipping")
    return f'''
          <div class="materials{' is-primary' if framed(p) else ''}">
            <p class="detail-spec">{intro}</p>
            <div class="mat-tabs">{tabs}{panels}
            </div>
          </div>'''


def page(p):
    t, url = e(p["title"]), f"{SITE}/prints/{p['slug']}"
    desc = f"{p['title']}, {'a framed' if framed(p) else 'an archival'} fine-art print by Logan Ossentjuk. {lede(p)} Made to order, free US shipping."
    buttons = "".join(f'''
            <a class="buy-btn is-pending" data-slug="{p['slug']}" data-size="{s['key']}" href="/contact?print={quote(p['title'] + ' (' + s['label'].rstrip('″') + ')')}">
              <span class="size">Buy {s['label']}</span><span class="price">${s['price']}</span>
            </a>''' for s in sizes(p))
    story = f'\n          <p class="detail-story">{e(p["story"])}</p>' if p["story"] else ""
    if framed(p):
        # Framed only: no unframed paper buttons; the material picker is the buy block.
        buy = f'''
          <p class="detail-spec">{e(PAPER)}, framed in black, white or oak · made to order</p>{materials(p)}'''
        note = ("Each print is made to order and framed behind shatterproof plexiglass, ready to hang. "
                "Allow a few days for printing and framing plus transit.")
        ask = "Questions or other sizes?"
    else:
        buy = f'''
          <p class="detail-spec">{"Fine-art paper · " if p.get("shopify") else ""}{e(PAPER)} · {fit(p)} · made to order</p>
          <div class="buy-list">{buttons}
          </div>{materials(p)}'''
        note = "Each print is made to order on archival paper. Allow a few days for printing plus transit."
        ask = "Questions, other sizes, or framing?"
    kind = "Framed print" if framed(p) else "Archival print"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{e(desc)}" />
  <title>{t} | Fine-Art Print | Ox Hollow Media</title>

  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png" />
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" />

  <meta property="og:site_name" content="Ox Hollow Media" />
  <meta property="og:type" content="product" />
  <meta property="og:title" content="{t} | Fine-Art Print | Ox Hollow Media" />
  <meta property="og:description" content="{e(lede(p))} {kind}, made to order, free US shipping." />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}{p['image']}" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="canonical" href="{url}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/styles.css?v={CSS_VER}" />
  <script type="application/ld+json">{product_ld(p)}</script>
</head>
<body class="light-nav">

{NAV}
  <!-- ── The print (generated from prints/catalog.json) ── -->
  <section id="print-detail">
    <div class="container">
      <p class="crumb"><a href="/prints">← All prints</a></p>
      <div class="detail-grid">
        <div class="detail-frame">
          {picture(p, ' fetchpriority="high"')}
        </div>
        <div class="detail-buy">
          <p class="section-label">{"Framed fine art print" if framed(p) else "Fine art print"}</p>
          <h1 class="detail-title">{t}</h1>
          <p class="detail-lede">{e(lede(p))}</p>{story}{buy}
          <p class="buy-note"><strong>Free US shipping.</strong> {note} Arrives damaged or wrong? Email a photo within 14 days and I'll send a free replacement. <a href="/shipping-returns">Shipping &amp; returns</a>. {ask} <a href="/contact?print={quote(p['title'])}">Get in touch</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── More prints ── -->
  <section id="more-prints">
    <div class="container">
      <p class="section-label">More prints</p>
      <div class="more-grid">{more_prints(p)}
      </div>
    </div>
  </section>

{FOOTER}
  <script src="/js/print-buy.js?v=1"></script>
  <script src="/js/main.js?v=3"></script>
  <script src="/js/motion.js?v=5"></script>
</body>
</html>
'''


def shop_sections():
    out = []
    for key, meta in CAT["categories"].items():
        items = [p for p in CAT["prints"] if p["category"] == key]
        if not items:
            continue
        cards = "".join(f'''
          <div class="print-card">
            <a class="print-mat" href="/prints/{p['slug']}">
              {picture(p, ' loading="lazy"')}
            </a>
            <h3>{e(p['title'])}</h3>
            <p class="print-spec">{e(spec_line(p))}</p>
            <a class="print-cta" href="/prints/{p['slug']}">→ View details &amp; buy</a>
          </div>''' for p in items)
        out.append(f'''  <!-- ── {e(meta['name'])} ── -->
  <section class="print-section" id="{key}">
    <div class="container">
      <div class="print-section-head">
        <h2>{e(meta['name'])}</h2>
        <p>{e(meta['intro'])}</p>
      </div>
      <div class="print-grid">{cards}
      </div>
    </div>
  </section>
''')
    return "\n".join(out)


# 1. print pages
live = set()
for p in CAT["prints"]:
    (PRINTS / f"{p['slug']}.html").write_text(page(p))
    live.add(f"{p['slug']}.html")
for f in PRINTS.glob("*.html"):
    if f.name != "index.html" and f.name not in live:
        f.unlink()
        print("removed", f.name)

# 2. shop grid
START, END = "  <!-- SHOP:START (generated by scripts/build_print_pages.py) -->\n", "  <!-- SHOP:END -->\n"
if START not in index_html:
    # First run: the grid is everything from the first subject section up to "How it works".
    a = index_html.index("  <!-- ── Mountains ── -->")
    b = index_html.index("  <!-- ── How it works / FAQ ── -->")
    index_html = index_html[:a] + START + END + "\n" + index_html[b:]
a, b = index_html.index(START) + len(START), index_html.index(END)
(PRINTS / "index.html").write_text(index_html[:a] + shop_sections() + index_html[b:])

# 3. sitemap
sm = (ROOT / "sitemap.xml").read_text()
S, E = "  <!-- PRINTS:START -->\n", "  <!-- PRINTS:END -->\n"
if S not in sm:
    sm = re.sub(r"  <url>\n    <loc>https://oxhollowmedia\.com/prints/[^<]+</loc>\n.*?</url>\n", "", sm, flags=re.S)
    sm = sm.replace("</urlset>", S + E + "</urlset>")
today = date.today().isoformat()
urls = "".join(f"  <url>\n    <loc>{SITE}/prints/{p['slug']}</loc>\n    <lastmod>{today}</lastmod>\n"
               f"    <image:image>\n      <image:loc>{SITE}{p['image']}</image:loc>\n"
               f"      <image:title>{e(p['title'])}</image:title>\n    </image:image>\n  </url>\n"
               for p in CAT["prints"])
a, b = sm.index(S) + len(S), sm.index(E)
(ROOT / "sitemap.xml").write_text(sm[:a] + urls + sm[b:])

print(f"built {len(CAT['prints'])} print pages, shop grid, sitemap")
