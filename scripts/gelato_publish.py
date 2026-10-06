#!/usr/bin/env python3
"""
Put prints on canvas, wood and acrylic: create the Gelato products (which
Gelato publishes to the Shopify store and fulfils), then record the Shopify
variant IDs in prints/catalog.json so the print pages get the material picker.

    python3 scripts/gelato_publish.py --only driftwood-shore   # one print
    python3 scripts/gelato_publish.py                          # every ready print
    python3 scripts/gelato_publish.py --dry-run                # just list them

A print is "ready" when Dropbox/Career/OxHollow/PrintMasters/gelato-ready/
<slug>.jpg exists and the catalog has no Shopify entry for it yet. Only
landscape prints are handled until portrait/square templates exist.

How the image gets to Gelato: Gelato downloads each file from a URL. The
script serves the gelato-ready folder from this Mac through a temporary
Cloudflare quick tunnel (brew install cloudflared) at a random one-time
address, and stops it when the run ends, so the full-res files are never
left anywhere public.

Each print becomes three Shopify listings ("<Title> - Canvas", "- Wood",
"- Acrylic") because a Gelato template holds one material. The website's
picker links straight to each variant's checkout, so that is invisible there.

Key: GELATO_API_KEY in the environment, or paste it at the hidden prompt.
Standard library + Pillow (already used by the scan scripts).
"""
import getpass, html, http.server, json, os, re, secrets, shutil, socketserver, subprocess
import sys, tempfile, threading, time, urllib.error, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
CAT_PATH = ROOT / "prints" / "catalog.json"
READY = Path.home() / "Dropbox/Career/OxHollow/PrintMasters/gelato-ready"
API = "https://ecommerce.gelatoapis.com/v1"
PPI = 150          # same rule as the paper sizes: long side x 150 must fit the file
MATERIALS = ["canvas", "wood", "acrylic"]
LABEL = {"canvas": "Canvas", "wood": "Wood", "acrylic": "Acrylic"}
BLURB = {
    "canvas": "Gallery-wrapped canvas with mirrored edges, ready to hang.",
    "wood": "Printed on FSC-certified birch, so the natural grain shows through the lightest areas.",
    "acrylic": "Glossy acrylic with a glass-like finish and vivid color.",
}

DRY = "--dry-run" in sys.argv
ONLY = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
cat = json.loads(CAT_PATH.read_text())
cfg = cat["gelato"]


def save():
    # Merge into the file on disk rather than overwrite it, so a second run (or a
    # hand edit) made while this one is going isn't lost: only this run's Shopify
    # entries and the Gelato template IDs are written back.
    disk = json.loads(CAT_PATH.read_text())
    mine = {p["slug"]: p for p in cat["prints"]}
    for p in disk["prints"]:
        q = mine.get(p["slug"])
        for k in ("shopify", "shopify_products"):
            if q and q.get(k):
                p.setdefault(k, {}).update(q[k])
    g = disk.setdefault("gelato", {})
    for o, mats in cfg.get("templates", {}).items():
        g.setdefault("templates", {}).setdefault(o, {}).update(mats)
    if cfg.get("_candidates_done"):
        g.pop("template_candidates", None)
    CAT_PATH.write_text(json.dumps(disk, indent=2, ensure_ascii=False) + "\n")


def orientation(path):
    w, h = ImageOps.exif_transpose(Image.open(path)).size
    return "landscape" if w > h * 1.05 else "portrait" if h > w * 1.05 else "square"


def todo():
    out = []
    for p in cat["prints"]:
        f = READY / f"{p['slug']}.jpg"
        if ONLY and p["slug"] not in ONLY:
            continue
        if not f.exists() or all(m in (p.get("shopify") or {}) for m in MATERIALS):
            continue
        o = orientation(f)
        if o not in cfg["templates"]:
            print(f"  skip {p['slug']}: {o} (no {o} templates yet)")
            continue
        out.append((p, f, o))
    return out


jobs = todo()
print(f"{len(jobs)} print(s) to set up: " + ", ".join(p["slug"] for p, _, _ in jobs))
if DRY or not jobs:
    sys.exit(0)

KEY = os.environ.get("GELATO_API_KEY", "")
if not KEY:
    print("Copy your Gelato API key (Gelato dashboard > Developer > API keys).")
    KEY = getpass.getpass("Paste it here and press Enter (it won't show on screen): ").strip()
if not KEY:
    sys.exit("No key entered.")
if re.fullmatch(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}", KEY):
    sys.exit("That looks like a template or product ID, not an API key (keys have a ':' in them). Copy the key again.")


def gelato(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"X-API-KEY": KEY, "Content-Type": "application/json", "Accept": "application/json",
                                          # Gelato's Cloudflare blocks the default Python-urllib agent (error 1010)
                                          "User-Agent": "OxHollowMedia-PrintShop/1.0 (+https://oxhollowmedia.com)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Gelato rejected the key (401). Copy it again from Developer > API keys and re-run.")
        raise RuntimeError(f"Gelato {method} {path} -> {e.code}: {e.read().decode()[:400]}")


templates = {}

# Template IDs are found once by name ("OHM Canvas - Landscape" ...) among
# candidate IDs (Templates page > ... > Copy Template ID), then kept in the catalog.
if cfg.get("template_candidates"):
    names = {f"OHM {LABEL[m]} - {o.title()}": (o, m) for o in ("landscape", "portrait", "square") for m in MATERIALS}
    for tid in cfg["template_candidates"]:
        try:
            t = gelato("GET", f"/templates/{tid}")
        except RuntimeError as e:
            print(f"  (not a template: {tid} {str(e)[:120]})")
            continue
        print(f"  template {tid}: {t.get('templateName')}")
        if t.get("templateName") in names:
            o, m = names[t["templateName"]]
            cfg["templates"].setdefault(o, {})[m] = tid
            templates[tid] = t
    cfg.pop("template_candidates")
    cfg["_candidates_done"] = True
    save()
    print("templates: " + json.dumps(cfg["templates"]))


def template(orient, mat):
    tid = cfg["templates"].get(orient, {}).get(mat)
    if not tid:
        raise RuntimeError(f"no Gelato template 'OHM {LABEL[mat]} - {orient.title()}' found")
    if tid not in templates:
        templates[tid] = gelato("GET", f"/templates/{tid}")
    return templates[tid]


missing = sorted({f"OHM {LABEL[m]} - {o.title()}" for _, _, o in jobs for m in MATERIALS
                  if not cfg["templates"].get(o, {}).get(m)})
if missing:
    sys.exit("Gelato templates not found: " + ", ".join(missing))


# ── Serve upright copies of the files through a temporary tunnel ──
stage = Path(tempfile.mkdtemp(prefix="gelato-"))
token = secrets.token_urlsafe(16)                     # unguessable path prefix
(stage / token).mkdir()
for p, f, _ in jobs:
    # Bake in EXIF rotation so Gelato sees the photo the right way up.
    ImageOps.exif_transpose(Image.open(f)).convert("RGB").save(stage / token / f.name, quality=95)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(stage), **k)

    def list_directory(self, path):                    # never list the folder
        self.send_error(404)

    def log_message(self, *a):
        pass


httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), Quiet)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
port = httpd.server_address[1]
tunnel = subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--url", f"http://127.0.0.1:{port}"],
                          stderr=subprocess.PIPE, text=True)
base = None
t0 = time.time()
while time.time() - t0 < 60 and not base:
    m = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", tunnel.stderr.readline())
    base = m.group(0) if m else None
if not base:
    tunnel.kill()
    sys.exit("Couldn't start the cloudflared tunnel.")
threading.Thread(target=lambda: [None for _ in tunnel.stderr], daemon=True).start()   # drain logs


def wait_reachable(url):
    # A new tunnel's hostname takes a few seconds to exist; asking too early
    # gets "no such host" cached by macOS, so wait before the first try.
    time.sleep(10)
    err = None
    for _ in range(40):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=10) as r:
                if r.status == 200:
                    return
        except Exception as e:
            err = e
        time.sleep(4)
    raise RuntimeError(f"tunnel not reachable ({err}): {url}")


def size_key(title):
    m = re.search(r"(\d+)x(\d+)\s*[″\"]", title)
    return f"{m.group(1)}x{m.group(2)}" if m else None


def description(p, mat):
    lede = p.get("lede") or p["alt"].rstrip(".") + "."
    return (f"<p>{html.escape(lede)} Photographed by Logan Ossentjuk of Ox Hollow Media.</p>"
            f"<p>{BLURB[mat]} Printed edge to edge, so the image is trimmed slightly to fill each size. "
            f"Made to order and shipped free in the US.</p>")


try:
    for p, f, orient in jobs:
        url = f"{base}/{token}/{f.name}"
        wait_reachable(url)
        # Square photos use their own sizes (gelato.square_sizes); the rest use the paper sizes.
        keys = cfg.get("square_sizes", []) if orient == "square" else [z["key"] for z in cat["sizes"]]
        allowed = [k for k in keys if max(map(int, k.split("x"))) * PPI <= p["source_px"]]
        p.setdefault("shopify", {})
        for mat in MATERIALS:
            if mat in p["shopify"]:
                continue
            t = template(orient, mat)
            variants = [v for v in t["variants"] if size_key(v["title"]) in allowed]
            body = {
                "templateId": t["id"],
                "title": f"{p['title']} - {LABEL[mat]}",
                "description": description(p, mat),
                "isVisibleInTheOnlineStore": True,
                "salesChannels": ["web"],
                "tags": ["print", mat, p["category"]],
                "vendor": "Ox Hollow Media",
                "productType": f"{LABEL[mat]} Print",
                "variants": [{"templateVariantId": v["id"],
                              "imagePlaceholders": [{"name": ph["name"], "fileUrl": url, "fitMethod": "slice"}
                                                    for ph in v["imagePlaceholders"]]} for v in variants],
            }
            prod = gelato("POST", f"/stores/{cfg['store_id']}/products:create-from-template", body)
            print(f"  {p['slug']} {mat}: created {prod['id']}, publishing", end="", flush=True)
            # Gelato can take 30+ minutes, and its status sometimes stays
            # "created" after the Shopify product exists, so also accept a
            # product whose variants all carry Shopify IDs.
            deadline = time.time() + 60 * 60
            while time.time() < deadline:
                time.sleep(20)
                try:
                    prod = gelato("GET", f"/stores/{cfg['store_id']}/products/{prod['id']}")
                except (RuntimeError, OSError) as e:      # transient network/API hiccup: keep waiting
                    print("!", end="", flush=True)
                    continue
                print(".", end="", flush=True)
                linked = prod.get("variants") and all(v.get("externalId") for v in prod["variants"])
                if prod["status"] in ("active", "publishing_error") or (linked and prod.get("externalId")):
                    break
            print(" " + prod["status"])
            if not (prod.get("externalId") and prod.get("variants")
                    and all(v.get("externalId") for v in prod["variants"])):
                raise RuntimeError(f"{p['slug']} {mat}: {prod['status']} {prod.get('publishingErrorCode')}")
            price = cfg["prices"][mat]
            p["shopify"][mat] = {
                size_key(v["title"]): {"variant": v["externalId"], "price": price[size_key(v["title"])]}
                for v in prod["variants"] if v.get("externalId") and size_key(v["title"])}
            p.setdefault("shopify_products", {})[mat] = prod["externalId"]
            save()                                     # keep progress if a later step fails
finally:
    tunnel.terminate()
    httpd.shutdown()
    shutil.rmtree(stage, ignore_errors=True)

print("\ndone. Next: prices/shipping check in Shopify, then python3 scripts/build_print_pages.py")
