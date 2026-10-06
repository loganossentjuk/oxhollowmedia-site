# Framed prints: switching the shop to framed (Shopify + Gelato)

Every print is sold through Shopify, with Gelato printing and shipping:

| Tab on the print page | Gelato product | Choices |
|---|---|---|
| Framed print | Framed poster, archival matte paper, **no mat** | Black · White · Oak · **No frame** (Print Only) |
| Framed canvas | Canvas in a floating frame | Black · White · Oak |
| Wood | (already live) | |
| Acrylic | (already live) | |

Plain canvas and the Stripe paper links are retired: archived and turned off,
not deleted, and only for a print whose framed listings are live.

Sizes stay as they are: 8×12, 12×18, 16×24, 24×36 (squares 12×12, 16×16,
20×20), capped by each file's resolution (long side × 150 ppi).

## 1. Make the templates in Gelato (you, about 20 minutes)

The script finds templates **by exact name**, so copy the names below exactly.
Make 9 templates: 3 products × 3 orientations.

In the Gelato dashboard, go to **Templates → Create template**. For each one:

1. **Product:**
   - *Framed Print*: Framed posters, **wooden frame**, **archival (or premium) matte paper**, **no passe-partout/mat**.
   - *Framed Canvas*: Framed canvas (canvas in a floating frame).
   - *Print Only*: Posters, **archival matte paper** (the same paper the Stripe prints used).
2. **Orientation:** landscape, portrait or square.
3. **Frame colours** (both framed products): **Black, White, Natural wood**. The site shows Natural wood as "Oak".
4. **Sizes in inches:** tick **8×12, 12×18, 16×24, 24×36**, or **12×12, 16×16, 20×20** for square. Untick any Gelato doesn't offer for that product. Sizes must be in inches: cm-only sizes are ignored.
5. Upload any photo as the design (it gets replaced per print) and save with the name:

```
OHM Framed Print - Landscape     OHM Framed Canvas - Landscape     OHM Print Only - Landscape
OHM Framed Print - Portrait      OHM Framed Canvas - Portrait      OHM Print Only - Portrait
OHM Framed Print - Square        OHM Framed Canvas - Square        OHM Print Only - Square
```

6. Copy each template's ID (Templates page → ⋯ → **Copy Template ID**) and send all 9 IDs over.

## 2. Price them (one command, then you approve)

Wait until the current Gelato run has finished, then:

```bash
python3 scripts/gelato_publish.py --quote --templates ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9
```

This finds the templates by name, saves their IDs in `prints/catalog.json`,
and prints Gelato's US cost (item + cheapest shipping) per size, with a
suggested price at about 2.5×, rounded up to $5. Nothing is created. Approve
the prices and they go into `gelato.prices` in the catalog.

## 3. Create the listings

```bash
python3 scripts/gelato_publish.py --dry-run     # check the list first
python3 scripts/gelato_publish.py               # framed print, print only, framed canvas
```

Wood and acrylic that already exist are skipped. Gelato takes 5–60 minutes per
listing, so the run goes in batches, best sellers first. With no sales on
record yet, "best" means gallery-wall order (top of the wall first). Run
`--dry-run` before each batch, and do step 4 after each one:

```bash
# Batch 1
python3 scripts/gelato_publish.py --only dawn-patrol,sierra-river-bend,autumn-flats,blue-footed-booby,petunia-blush,humpback-breach,cloudbreak-ridge,fitz-roy-alpenglow,hydrangea-deep-blue,fog-forest
# Batch 2
python3 scripts/gelato_publish.py --only geranium-white,blue-hour-ridge,sea-lion-pup,geranium-coral,aspen-and-cobalt,golden-gate-fog,highland-river,petunia-crimson,petunia-veined,shorebreak-boulders
# Batch 3
python3 scripts/gelato_publish.py --only turquoise-shallows,the-wax-ritual,the-flower-market,driftwood-shore,marsh-at-dusk,sun-on-the-water,amber-glass,misty-ridgeline
# Batch 4
python3 scripts/gelato_publish.py --only cocktails,paddler-at-the-gate,wall-of-names,art-will-save-you,reef-passage,glass-spire,rainier-afterglow,dusk-waterfowl,mural-sundown,harbour-pastel
# Batch 5
python3 scripts/gelato_publish.py --only marine-iguana,turquoise-harbor,dusk-branches,tidepool-lava
# Held until their print files are re-made (their canvas/wood/acrylic are hidden for the same reason)
python3 scripts/gelato_publish.py --only verdigris,copper-and-teal
```

Prints whose file is 2000 px
(Blue-footed Booby, Humpback Breach, Fitz Roy, Blue Hour Ridge, Sea Lion Pup,
Highland River, Paddler, Reef Passage, Rainier) only reach 8×12, so they get a
framed 8×12 and nothing larger.

## 4. After each batch (Claude can do this with the Shopify connector)

1. Set the Shopify prices from `gelato.prices`, as was done for canvas/wood/acrylic.
2. Record each framed listing's mockup image per frame colour into the print's
   `"previews"` in the catalog (`{"framed": {"black": url, ...}, "framed_canvas": {...}}`).
   The print page swaps to the mockup when a frame is picked.
3. Archive (don't delete) the print's plain **Canvas** listing in Shopify.
4. `python3 scripts/build_print_pages.py`: framed prints switch to the framed layout.
5. `python3 scripts/make_stripe_links.py`: turns off the Stripe paper links for
   framed prints.

A print with no framed listing yet keeps its current page, so the switch can
happen one print at a time.

## Later

- **Mat (passe-partout):** off for now, to review later. It would mean a new set
  of framed-print templates with a mat, and new prices.
