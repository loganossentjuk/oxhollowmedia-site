# Stripe setup — selling prints from oxhollowmedia.com

The print pages take payment through **Stripe Payment Links**: one hosted
checkout URL per size. No server, no monthly platform fee, nothing to
maintain. Stripe's cut is 2.9% + 30¢ per sale and that's it.

Right now **one print is live as a full product page**:
`/prints/sierra-river-bend`. Its four buttons fall back to the enquiry form
until you paste in Stripe links — so nothing is ever broken for a visitor.

---

## The price ladder

| Size   | Price |
|--------|-------|
| 8×12″  | $55   |
| 12×18″ | $100  |
| 16×24″ | $175  |
| 24×36″ | $320  |

Free US shipping — the cost is baked into these prices, so don't add a
shipping charge at checkout.

---

## 1. 🧑 Create the Stripe account (~10 min)

1. <https://dashboard.stripe.com/register> — sign up with
   **oxhollowbooking@gmail.com**.
2. Business type: **Individual / sole proprietor** unless you've actually
   registered an LLC.
3. Add your bank details for payouts. Stripe will ask for SSN/EIN — that's
   standard for US payment processing and goes directly to Stripe.
4. Stay in **Test mode** (toggle, top right) until step 4 below.

## 2. 🧑 Create four Payment Links (~10 min for the first print)

For each row of the table above:

1. Dashboard → **Payment links** → **+ New**.
2. **Product:** "Sierra River Bend — 8×12″ archival print" (etc.)
3. **Price:** from the table. One-off, USD.
4. **Image:** upload the photo — it shows in checkout and matters.
5. Under **Options**:
   - ✅ **Collect customers' shipping addresses** → United States only
   - ❌ Do *not* add a shipping rate (shipping is already in the price)
   - ✅ Collect phone number (optional, useful for delivery issues)
6. **After payment** → redirect to `https://oxhollowmedia.com/thank-you`
   *(or leave Stripe's default confirmation for now)*
7. Copy the resulting `https://buy.stripe.com/...` URL.

## 3. 🤖 Paste the links in

Open `prints/sierra-river-bend.html`, find `STRIPE_LINKS` near the bottom,
and fill in the four URLs:

```js
const STRIPE_LINKS = {
  "8x12":  "https://buy.stripe.com/...",
  "12x18": "https://buy.stripe.com/...",
  "16x24": "https://buy.stripe.com/...",
  "24x36": "https://buy.stripe.com/..."
};
```

Any size left as `""` keeps falling back to the enquiry form. Send the URLs
to Claude and this gets done and deployed in a minute.

## 4. 🧑 Test it, then go live

1. In **Test mode**, buy your own print with card `4242 4242 4242 4242`,
   any future expiry, any CVC.
2. Confirm the order email arrives and the shipping address is captured.
3. Flip Stripe to **Live mode** and recreate the four links — *test-mode
   links do not work in live mode*. Paste the live URLs in.

---

## Fulfilling an order

You chose print-on-demand, so the loop is:

1. Stripe emails you: print, size, buyer's shipping address.
2. Open the master TIFF from
   `Dropbox/Career/OxHollow/PrintMasters/<category>/`.
3. Upload to your lab (Prodigi, WHCC, Bay Photo) and enter the buyer's
   address as the ship-to. They print and ship direct.
4. Stripe payout lands on its normal schedule.

Two or three minutes per order. When volume justifies it, this can be
automated with a Cloudflare Worker on a Stripe webhook that submits the
order to the lab's API — no manual step at all.

**Check your margin before going live.** Get a real quote from your lab for
a 24×36 giclée. If their cost plus shipping is more than about $120, the
$320 price is too thin and we should raise it.

---

## Scaling to the rest of the catalogue

43 prints × 4 sizes = **172 Payment Links**, which is unreasonable by hand.
`scripts/make-stripe-links.mjs` creates them all from the site's own product
data.

```bash
export STRIPE_SECRET_KEY=sk_live_...   # never commit this
node scripts/make-stripe-links.mjs --dry-run   # preview
node scripts/make-stripe-links.mjs             # create for real
```

It writes `stripe-links.json`, which Claude can then wire into every print
page at once.

**Run it yourself.** Your secret key controls your money — it should never be
pasted into a chat, and Claude never needs to see it.
