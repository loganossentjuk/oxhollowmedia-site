# Stripe setup: selling prints from oxhollowmedia.com

Every print in the shop has its own page at `/prints/<name>` with four Buy
buttons. Payment runs through **Stripe Payment Links**: one hosted checkout
URL per print and size. There's no server and no monthly fee. Stripe takes
2.9% + 30¢ per sale.

Until Stripe links exist, each Buy button opens the enquiry form with the
print and size filled in, so no button is ever broken.

## How the pieces fit

| File | What it does |
|---|---|
| `prints/catalog.json` | The list of prints, sizes and prices. Edit this to add, remove or reorder prints. |
| `scripts/build_print_pages.py` | Builds every `/prints/<name>` page, the shop grid and the sitemap from the catalogue. |
| `scripts/make_stripe_links.py` | Creates a Stripe product, price and Payment Link for every print × size and writes `stripe-links.json`. |
| `stripe-links.json` | Public checkout URLs (no secrets). Once it's committed, every Buy button goes straight to checkout. |
| `js/print-buy.js` | Swaps each Buy button to its Stripe link when one exists. |

Changing the shop later:

```bash
python3 scripts/build_print_pages.py      # after editing prints/catalog.json
python3 scripts/make_stripe_links.py      # creates links only for new prints
```

## Prices

Every print is offered in four sizes that match its shape (sizes are short side × long side). The shape is set per print in `prints/catalog.json`.

| Shape | Prints | Sizes and prices |
|---|---|---|
| 3:2 | 15 | 8×12″ $55 · 12×18″ $100 · 16×24″ $175 · 24×36″ $320 |
| 16:9 | 12 | 9×16″ $75 · 12×21″ $115 · 18×32″ $235 · 20×36″ $275 |
| 4:3 | 6 | 9×12″ $60 · 12×16″ $90 · 18×24″ $190 · 24×32″ $290 |
| 5:4 | 4 | 8×10″ $45 · 12×15″ $85 · 16×20″ $145 · 24×30″ $275 |
| 2:1 | 4 | 6×12″ $40 · 9×18″ $80 · 12×24″ $130 · 18×36″ $255 |
| 1:1 | 1 | 10×10″ $55 · 12×12″ $75 · 20×20″ $180 · 30×30″ $330 |

Prices follow the original 3:2 ladder by print area, so a size costs about what a 3:2 print of the same area does. Free US shipping is built in. Don't add a shipping rate at checkout.

When sizes change, `make_stripe_links.py` creates links for the new sizes and turns off the old ones in Stripe, so an old checkout URL can't take an order.

---|---|
| 8×12″ | $55 |
| 12×18″ | $100 |
| 16×24″ | $175 |
| 24×36″ | $320 |

Free US shipping is built into these prices. Don't add a shipping rate at checkout.

---

## One-time setup (you do these steps; they need your identity and bank details)

### 1. Create and activate the account

1. Sign up at <https://dashboard.stripe.com/register>.
2. **Activate payments:** business type (individual/sole proprietor unless you have an LLC), your details, and the bank account for payouts.
   - Website: `https://oxhollowmedia.com/prints`
   - Product description: "Archival fine-art photography prints, made to order and shipped in the US."
   - Statement descriptor: `OX HOLLOW MEDIA`
3. Stripe checks that the site shows prices, contact details and a refund policy. All three are live: the print pages, the footer email and phone, and `/shipping-returns`.

### 2. Settings worth turning on

- **Settings → Customer emails:** turn on "Successful payments" so buyers get a receipt.
- **Settings → Branding:** upload the logo and set the brand color to `#294132` so checkout matches the site.
- **Settings → Notifications:** make sure you get an email for every successful payment. That email is your order ticket.
- **Sales tax:** physical prints are taxable in many states, including California. Every product is already tagged with the tax code for general physical goods, so Stripe Tax can be switched on later. Turning it on without first adding a tax registration (Tax → Registrations) collects nothing, and Stripe doesn't warn you. Decide with an accountant whether tax is added on top of the listed prices or included in them.

### Safety net

This repo has a commit check that blocks any Stripe key (`sk_`/`rk_`) from being committed. Turn it on once in any new copy of the repo with `git config core.hooksPath .githooks`.

### 3. Create the links in test mode

1. Switch the dashboard to **Test mode**.
2. **Developers → API keys → Create restricted key.** Name it `print-shop-links` and give it **Write** access to **Products**, **Prices** and **Payment Links** only. Leave everything else at None. Copy the key (`rk_test_...`).
   A restricted key can only do those three things, so it does far less harm if it ever leaks than the full secret key would.
3. In your own terminal (never paste the key into a chat, a file in this repo, or a commit):

   ```bash
   cd ~/projects/oxhollowmedia-site
   export STRIPE_API_KEY=rk_test_...
   python3 scripts/make_stripe_links.py --dry-run
   python3 scripts/make_stripe_links.py
   ```

   That creates every print × size link (168 for 42 prints) and writes `stripe-links.json`.
   If it stops partway, just run it again: finished links are skipped and nothing is duplicated.
4. Tell Claude it's done. Claude commits `stripe-links.json` to a preview so you can test before anything goes live.
5. On the preview, buy a print with card `4242 4242 4242 4242`, any future date, any CVC. Check that the receipt arrives, the shipping address is collected, and you land on `/thank-you`.

### 4. Go live

Test-mode links don't work for real payments. Once the test purchase works:

```bash
rm stripe-links.json
export STRIPE_API_KEY=rk_live_...
python3 scripts/make_stripe_links.py
```

Create the live restricted key the same way (Products, Prices, Payment Links: Write). When the links are made, you can delete or expire both restricted keys in the dashboard. The site itself never uses a key.

Then Claude commits the new file and publishes.

---

## Fulfilling an order

1. Stripe emails you the print, the size and the buyer's shipping address.
2. Open the master file for that print.
3. Order it from your print lab and enter the buyer's address as the ship-to.
4. Email the buyer when it ships.

**Check your margin before going live.** Get a real quote from your lab for
each size, especially 24×36″. If the lab's cost plus shipping is more than
about $120 for that size, $320 is too thin and the price should go up.

**Check the sizes with your lab.** Each print's sizes match its shape, but a
few are close rather than exact: 12×21″ and 20×36″ for 16:9 photos, the 2:1
sizes for Shorebreak Boulders (about 2.17:1) and the 5:4 sizes for Mural,
Sundown (about 1.21:1) trim a sliver off one edge. Confirm your lab offers
every size listed, or tell Claude which to swap.
