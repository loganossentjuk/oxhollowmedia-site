# Revenue engine (set up 2026-10-20)

Goal: grow revenue evenly across **events, prints and films**, with $0 ad spend for now and about **1–2 hours a week of Logan's time** (approving, sending, calls). The team does the research, writing, drafting and scheduling.

## Logan's rules (2026-10-20)
- **Outreach:** 10 new contacts a week. The team drafts them into Gmail (oxhollowmedia@gmail.com); **Logan approves and sends**. One follow-up draft after 7 days with no reply.
- **Instagram:** a weekly batch of 3–4 posts, ready Sunday. **Logan approves once**, then the team schedules them in Metricool. Nothing posts without that approval.
- **Leads:** when an enquiry or a reply comes in, the team **drafts Logan's reply** (booking-kit templates, quote from work-with-me prices) within a few hours. Logan sends.
- **Ads:** allowed in principle, but the budget is **$0** for now. No spending.
- **Reporting:** a weekly email to oxhollowmedia@gmail.com plus a summary in the Manager team chat.
- Always: no invented facts (team/BUSINESS.md); ask before changing visible site copy; preview before live.

## The weekly machine
| When (Pacific) | What | Where it runs |
|---|---|---|
| Mon 8:00 | **Outreach batch:** 10 researched contacts → Gmail drafts, plus 7-day follow-up drafts | local scheduled task `ox-weekly-outreach` |
| Mon 9:30 | **Weekly report:** Shopify orders/revenue, enquiries and replies, Instagram numbers (Metricool), what's waiting on Logan → email + chat | local scheduled task `ox-weekly-report` |
| Weekdays 9:00 / 13:00 / 17:00 | **Lead watch:** new enquiries and replies in Gmail → reply drafts | local scheduled task `ox-leads-inbox` |
| Sun 17:00 | **Instagram batch:** next week's 3–4 posts (images/Reels + captions) → Dropbox `Instagram Drafts/<date> Week batch/` + chat summary for approval | local scheduled task `ox-instagram-batch` |
| Every other day | **Team run:** site, SEO, QA, shop health, content (team/MANAGER.md) | cloud routine |

## Outreach mix (10 a week, rotate)
- **4 events:** in-house event/community/marketing leads at Bay Area tech companies, event agencies, venue sales teams. Hooks: Q4 holiday parties, January kickoffs, conferences on the SF calendar. Pitch the $2,500/mo content-partner retainer to past clients and warm leads.
- **3 prints:** interior designers and stagers, boutique hotels/cafés/offices that hang art, local gift-guide editors (SF Standard, Time Out SF and similar), corporate gifting buyers. Lead with Salt and Stone, Galápagos and the framed range; free US shipping; made to order.
- **3 films:** conservation nonprofits, outdoor and sustainability brands, foundations. Proof: Ocean Defenders (pro bono client work, never "commissioned"), Brushstrokes For Survival.
- Only public business contacts, cited. Never guess emails. Contact-form-only targets: draft the text with the form link.
- Keep a running log: `team/outreach-log.md` (date, org, channel, status: drafted / sent / replied / booked / no reply). Don't re-contact anyone within 60 days.

## Revenue levers in order
1. **Retainers and repeat corporate clients** (one retainer ≈ $30k/yr).
2. **Event bookings from outreach and referrals:** referral asks to the five named clients, then planners and venues.
3. **Holiday print season:** Salt and Stone, Galápagos and framed gifts; the gift-deadline line once Gelato's dates are known; Pinterest (free app); gift-guide pitches.
4. **Films:** one pitch-ready "conservation story" offer for nonprofits and brands.
5. **Free visibility:** Google Business Profile (Logan to create), reviews from past clients, Instagram series.

## Needs Logan once (unblocks automation)
- [ ] Formspree: set the contact-form notification email to **oxhollowmedia@gmail.com**. As of September it went to oxhollowbooking@gmail.com; if it still does, lead watch can't see new enquiries.
- [ ] Google Business Profile (about 30 min), then send the review link to past clients.
- [ ] Pinterest app for Shopify (free).
- [ ] Gelato 2026 holiday order cut-off dates.
