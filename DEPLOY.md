# Deploying Ox Hollow Media

The site is a static site (HTML/CSS/JS) — no build step. It's hosted on
**Cloudflare Pages**, which deploys automatically every time you push to GitHub.

There are three one-time setup tasks. Steps 1–2 get the site live; step 3 makes
the contact form work.

---

## 1. Connect the repo to Cloudflare Pages

1. Create a free account at <https://dash.cloudflare.com/sign-up>.
2. In the dashboard, go to **Workers & Pages → Create → Pages → Connect to Git**.
3. Authorize GitHub and pick the **`oxhollowmedia-site`** repo.
4. Configure the build:
   - **Production branch:** `main`
   - **Framework preset:** `None`
   - **Build command:** *(leave blank)*
   - **Build output directory:** `/`  (the repo root)
5. Click **Save and Deploy**. In ~30 seconds you'll get a live URL like
   `oxhollowmedia-site.pages.dev`. Open it — the site should look exactly like local.

> From now on, every `git push` to `main` auto-deploys. Pushes to other branches
> get their own preview URL.

---

## 2. Point oxhollowmedia.com at the site

You own the domain, so we just add it to the Pages project.

1. In your Pages project → **Custom domains → Set up a custom domain**.
2. Enter `oxhollowmedia.com`, then also add `www.oxhollowmedia.com`.
3. Cloudflare will show DNS records to add. Two paths:
   - **Easiest (recommended):** move the domain's nameservers to Cloudflare
     (Cloudflare walks you through this — you paste two nameservers into your
     current registrar). DNS + SSL then "just work."
   - **Or keep your current registrar's DNS** and add the CNAME records
     Cloudflare gives you.
4. Wait for DNS to propagate (usually minutes, up to a few hours). Cloudflare
   issues the HTTPS certificate automatically.

Done — `https://oxhollowmedia.com` is live.

---

## 3. Make the contact form work (Formspree)

The form currently shows "Form not configured yet" until you do this:

1. Sign up free at <https://formspree.io> using **hello@oxhollowmedia.com**.
2. Create a new form; Formspree gives you an endpoint like
   `https://formspree.io/f/abcdwxyz`.
3. In `index.html`, find `YOUR_FORM_ID` (one spot, flagged with a ⚠️ comment)
   and replace it with your ID.
4. Commit + push. The form now emails you on every submission.

---

## 4. (Optional) Get email at hello@oxhollowmedia.com

The site links to `hello@oxhollowmedia.com`. To actually receive mail there for
free, use **Cloudflare Email Routing** (in your domain's dashboard → Email):
forward `hello@oxhollowmedia.com` → your personal Gmail. No mailbox to manage.

---

## Everyday workflow after setup

```
# make changes, then:
git add -A
git commit -m "describe your change"
git push
```

Cloudflare redeploys automatically. That's it.
