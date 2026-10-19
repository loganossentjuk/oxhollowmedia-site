# Booking kit: invoice, agreement, emails, print sales tax

Draft for Logan, 2026-10-13. Nothing here has been sent or published.

Facts used come from `team/BUSINESS.md` and `work-with-me.html`. Anything not confirmed is marked `TODO(Logan)`. The invoice review is based on Logan's existing invoices in Dropbox; no client names, addresses or amounts are copied here.

---

## 1. Invoice improvements

### What the current invoices look like
- Word doc exported to PDF. Header: "Ox Hollow Media LLC" and "oxhollowmedia.com".
- Fields: Invoice #, Invoice Date, Payment Terms (Net 30), Bill To (company, attention line, company website).
- Line items: one line per shoot (date, venue, start and end time) at an hourly rate, then one line per rideshare trip as a travel expense.
- Subtotal, Tax ($0.00), Total Due.
- Footer: payable to Ox Hollow Media LLC, preferred payment ACH through the client's vendor system, and a thank-you line.

The basics are there and the arithmetic checks out. These are the fixes worth making.

### Fixes, in priority order
1. **Fix the numbering and dates.** Invoice numbers use "2025" for work done in 2026, at least one invoice date is printed as 2025 for 2026 shoots, and the file and folder numbers don't match the invoice number inside them. An AP team may bounce an invoice dated before the work happened. Use `OHM-YYYY-NNN`, where YYYY is the year the invoice is issued and NNN is a running count that never resets mid-year or repeats. Name the file the same as the number: `OHM-2026-004_ClientName.pdf`.
2. **Add a due date, not just "Net 30".** Print the actual date (invoice date + 30 days). AP teams pay to the date on the page.
3. **Add Ox Hollow contact details.** There is no email, phone or mailing address for the business on the invoice. Add at least the business email and a mailing address. `TODO(Logan): which email goes on invoices (hello@oxhollowmedia.com or oxhollowmedia@gmail.com) and which mailing address.`
4. **Give more than one way to pay.** ACH through the client's vendor platform works for one client, but new clients will ask how to pay. List ACH (details on request or on a W-9 / vendor form) plus one card or online option. `TODO(Logan): which methods you accept (ACH, check, Zelle, card via Stripe or another processor). Card fees are usually 2.9% or more; decide whether to absorb them.`
5. **Itemise the add-ons the site promises.** Use separate lines for the package (The Session / The Day / The Production or hourly), overtime ($250/hour), rush ($200), second shooter (+50% of the package), and travel days outside the Bay Area ($500/day plus costs). This matches the site and makes approvals faster.
6. **Rethink the travel lines.** Each rideshare trip is its own line and says "Home". That reveals a personal address pattern and adds clutter. Either roll them into one line ("Local travel, rideshare, receipts attached") or drop local travel. The site says rates are for Bay Area bookings and only travel outside the Bay Area is quoted separately. `TODO(Logan): do you want to bill local rideshare inside the Bay Area?`
7. **Add a usage-rights line.** One sentence: the client may use the delivered photos however they like; Logan keeps copyright and may show the work in the Ox Hollow portfolio (unless an NDA says otherwise). It answers the question legal or marketing will ask later.
8. **Add a late-payment line and a reference field.** A short, polite line: "Invoices unpaid 15 days after the due date may incur a 1.5% monthly late fee." Also add a "PO / Reference" field, since many tech companies require a PO number. `TODO(Logan): do you want a late fee at all, and at what rate? Confirm any rate is allowed under California law before using it.`

Smaller tidy-ups: put "$" on every amount with two decimals; close all parentheses; make every shoot line the same format (date, venue, time); keep "Tax: $0.00" since the work is a service. `TODO(Logan): confirm with your accountant that event photography with digital delivery isn't taxable in CA.`

Also worth deciding: the hourly rate on past invoices is lower than the rates now on `/work-with-me`. `TODO(Logan): will existing clients keep their old rate, or move to the published packages?`

### Invoice template

```
OX HOLLOW MEDIA LLC
oxhollowmedia.com  |  [business email]  |  [mailing address]

INVOICE

Invoice #:        OHM-[YYYY]-[NNN]
Invoice date:     [Month D, YYYY]
Due date:         [Month D, YYYY]   (Net 30)
PO / Reference:   [PO number or "n/a"]

Bill to:
[Company name]
Attn: [Name], [AP email]
[Billing address]

Event: [Event name], [date(s)], [venue]

DESCRIPTION                                         RATE        QTY    AMOUNT
[The Session / The Day / The Production]
  [date], [venue], [start] to [end]                 $[x,xxx.00]  1     $[x,xxx.00]
  -- or, for hourly work --
Event photography, [date], [venue],
  [start] to [end]                                  $[xxx.00]/hr [h]   $[xxx.00]
Overtime, [date]                                    $250.00/hr   [h]   $[xxx.00]
Second shooter (+50% of package)                    $[xxx.00]    1     $[xxx.00]
Rush delivery                                       $200.00      1     $200.00
Travel day outside the Bay Area                     $500.00/day  [d]   $[xxx.00]
Travel costs, at cost (receipts attached)           $[xxx.00]    1     $[xxx.00]

                                                    Subtotal          $[x,xxx.00]
                                                    Tax               $0.00
                                                    TOTAL DUE         $[x,xxx.00]

Payment
Payable to: Ox Hollow Media LLC
ACH: [bank details, or "details provided on your vendor form"]
[Second method: e.g. card payment link / check to mailing address]

Usage
Once delivered, you may use these photos however you like. Ox Hollow Media
keeps the copyright and may show the work in its portfolio unless we agreed
otherwise in writing.

Invoices unpaid 15 days after the due date may incur a [x]% monthly late fee.

Thank you for having me at [event]. Questions about this invoice: [email].
```

---

## 2. Booking agreement template

> **Template, not legal advice; have a lawyer review.** It has not been checked against California law. Logan has no liability insurance yet, so the liability section matters more than usual. Never describe Ox Hollow as insured.

```
EVENT PHOTOGRAPHY AGREEMENT

This agreement is between Ox Hollow Media LLC ("I", "me", "Ox Hollow")
and [Client legal name] ("you", "Client"), on [date].

1. THE EVENT
Event:              [name]
Date(s):            [date(s)]
Venue / address:    [venue]
On-site contact:    [name, mobile]
Coverage:           [start time] to [end time], up to [4 / 8 / x] hours
Package:            [The Session / The Day / The Production / hourly]
Fee:                $[amount]
Add-ons:            [second shooter / rush / travel / none]

2. WHAT I DELIVER
- About 100 edited photos per hour of coverage. You get my selected
  edits, not every frame.
- A color-graded, full-resolution gallery, in high resolution and web
  sizes, within 5 business days of the event.
- On The Day, a same-week highlight set for social.
- RAW files only if you ask for them in writing before the event.
- Galleries stay online for [TODO(Logan): how long, e.g. 90 days].
  Please download your copy.

3. HOW YOU CAN USE THE PHOTOS
Once the gallery is delivered and the invoice is paid, you may use the
photos however you like: website, social, press, ads, internal channels.
I keep the copyright. I may show a selection in my portfolio and on
social media, unless you ask me not to in writing or an NDA covers the
event.
[DECISION FOR LOGAN: this keeps copyright and portfolio rights with you
and gives the client unlimited use. Alternatives: (a) transfer copyright
fully for a higher fee, or (b) limit use to non-paid channels and license
ads separately. The site currently promises "however you like", so this
version matches it.]

4. PAYMENT
- No deposit is required to book.
- I'll send an invoice after the event. Payment is due within 30 days
  of the invoice date by ACH or [other methods].
- Overtime, rush and any travel costs are added to that invoice.
- Unpaid invoices after [15] days past due may incur a [x]% monthly
  late fee. [TODO(Logan): keep or remove.]

[OPTIONAL CLAUSE, OFF BY DEFAULT. Turn on for multi-day work, travel
bookings, or new clients with no track record:
"To hold the date, a booking fee of [25]% of the fee is due when you
sign. It is credited to the final invoice and is non-refundable if you
cancel within [14] days of the event."
RISK NOTE: with no deposit, a late cancellation leaves the date empty
and unpaid. The cancellation fees in section 5 are the main protection;
they only help if the client pays them. The site says "no deposit", so
switching this on means updating the site or calling it something
else for specific jobs only.]

5. CANCELLING OR MOVING THE DATE
- More than [14] days before the event: no charge.
- [14] days or fewer: [50]% of the fee.
- [48 hours] or fewer: [100]% of the fee.
- Moving the date: free once if I'm available on the new date. If I'm
  not, it's treated as a cancellation.
- If I can't attend because of illness or an emergency, I'll try to
  find a qualified replacement you approve. If I can't, I'll refund
  anything you've paid and that is the end of my obligation.
[TODO(Logan): set the windows and percentages.]

6. ADD-ON RATES
- Overtime: $250 per extra hour, billed in [30-minute] blocks. I'll
  check with the on-site contact before staying past the end time.
- Rush delivery: $200. Please book at least 24 hours ahead if you can.
- Second shooter: +50% of the package rate (+$500 on The Session,
  +$1,000 on The Day). Included in The Production.
- Travel outside the Bay Area: $500 per travel day, plus travel costs
  (flights, lodging, car) at cost.

7. PEOPLE IN THE PHOTOS
You're responsible for letting attendees know the event is being
photographed (for example, a note on registration and signs at the
door) and for collecting any consent or model releases you need. Tell
me before the event about anyone who shouldn't be photographed, and
point them out on the day if you can. I'll do my best to avoid them.

8. CONFIDENTIALITY
I'll keep anything confidential I see or hear at your event private.
I'm happy to sign your NDA; if its terms conflict with this agreement,
the NDA wins on confidentiality and portfolio use.

9. WHAT I'M RESPONSIBLE FOR
- I bring professional, backed-up equipment and keep copies of the
  files until the gallery is delivered and for [TODO(Logan): x days]
  after.
- If files are lost or damaged through no fault of yours, or I can't
  deliver, my total responsibility is limited to refunding the fees
  you paid under this agreement.
- I'm not responsible for missed shots caused by venue rules, schedule
  changes, guests, lighting or access I couldn't control.
- I don't carry liability insurance. [TODO(Logan): update this line
  once you have a policy. Some venues and companies require a COI; ask
  early.]

10. GENERAL
This agreement, plus any NDA you send, is the whole agreement. Changes
need to be in writing (email counts). California law applies.

SIGNED
Ox Hollow Media LLC                     [Client legal name]
Name: Logan Ossentjuk                   Name: [ ]
Signature: _______________              Signature: _______________
Date: [ ]                               Title: [ ]   Date: [ ]
```

---

## 3. Email templates

Plain text. Swap the [brackets]. No em dashes.

### 3a. Enquiry reply with quote

```
Subject: [Event name] on [date]: availability and quote

Hi [Name],

Thanks for reaching out about [event]. I'm free on [date].

Here's what I'd suggest:

The [Session / Day], [start] to [end] at [venue]: $[fee]
[Second shooter: +$[x]]
[Travel day outside the Bay Area: $500, plus travel costs]

That includes a color-graded, full-resolution gallery within 5 business
days. Expect about 100 edited photos per hour of coverage. [On The Day,
you'll also get a same-week highlight set for social.] Once delivered,
you can use the photos however you like.

No deposit to hold the date. I invoice after the event, Net 30.

A rough shot plan:
- [Arrivals and venue details]
- [Keynote / speakers]
- [Candid networking]
- [Group or team photo at a set time]

If that works, reply and I'll send a short agreement. Happy to adjust
the hours or the plan.

Logan
Ox Hollow Media
oxhollowmedia.com
```

### 3b. Booking confirmation

```
Subject: Confirmed: [event] on [date]

Hi [Name],

You're on my calendar for [date], [start] to [end] at [venue].

Attached is a short agreement covering hours, delivery, usage and
cancellation. Sign and send it back when you can. If you have an NDA or
a vendor form for your finance team, send it over and I'll fill it in.
[If they need a PO number on the invoice, let me know.]

I'll check in two or three days before the event to confirm the
schedule and who to find on site.

Thanks for booking,
Logan
```

### 3c. Pre-event check-in (2 to 3 days before)

```
Subject: [Event] on [day]: a few quick details

Hi [Name],

Looking forward to [day]. A few things so the day runs smoothly:

1. Run-of-show: is the latest version the one you sent, or is there an
   update?
2. On-site contact: who should I find when I arrive, and their mobile?
3. Arrival: I'll be there at [time], 15 minutes before coverage starts.
   Where should I check in, and is there parking or a loading spot?
4. Must-have shots: any speakers, sponsors, execs or a group photo I
   shouldn't miss?
5. Anyone who shouldn't be photographed?
6. Attendee notice: a line on registration or a sign at the door
   saying the event is being photographed helps.

My mobile on the day: [number].

Logan
```

### 3d. Gallery delivery

```
Subject: Your photos from [event]

Hi [Name],

Your gallery is ready: [link]

There are [number] edited photos in high resolution and web sizes. The
link stays up for [x days], so download a copy for your team.

Use them however you like: website, social, press, internal channels.
If you credit the photos, "Photo: Ox Hollow Media" is perfect.

Invoice [OHM-YYYY-NNN] is attached, due [date].

If anything looks off or you need a different crop, just reply.

Logan
```

### 3e. Review and referral ask (about a week after delivery)

```
Subject: One small favor

Hi [Name],

I hope the photos from [event] have been useful.

If you have two minutes, a short Google review helps me more than
anything else: [Google review link]

And if anyone on your team or at another company is planning an event,
I'd be glad to hear from them. They can reach me here or at
oxhollowmedia.com/contact.

Thanks again for having me.

Logan
```

`TODO(Logan): add your Google Business Profile review link.`

### 3f. Gentle overdue reminder

```
Subject: Invoice [OHM-YYYY-NNN] for [event]

Hi [Name],

A quick note that invoice [OHM-YYYY-NNN] for $[amount], due [date],
hasn't come through on my side yet. It's attached again here.

If it's already in process, thanks, and please ignore this. If it needs
to go to someone else in finance, or needs a PO number, let me know who
and I'll send it straight there.

Logan
```

Second reminder (if still unpaid two weeks later): same email, add "Could you let me know when I should expect payment?" and copy the AP address if you have one.

---

## 4. California sales tax checklist for print sales

> **Not tax advice.** Check with an accountant or CDTFA before you start collecting. Items marked UNVERIFIED need confirming.

1. **Get a California seller's permit from CDTFA.** One is required if you are engaged in business in California and sell tangible goods that are normally taxable at retail; physical prints and canvases count. Exceptions are narrow; "occasional sellers" make no more than two sales in 12 months. It is free to register online. Sources: https://cdtfa.ca.gov/taxes-and-fees/faqseller.htm and https://cdtfa.ca.gov/formspubs/pub107/ (read 2026-10-13).
2. **Register before the first order ships.** Logan is placing the first order now, so this is timely.
3. **Turn on CA collection in Shopify.** Go to Settings > Taxes and duties > United States, add California, and enter the seller's permit number. You can save it before the number arrives and fill it in later. Choose whether shipping is taxed under advanced options. UNVERIFIED: California generally doesn't tax separately stated delivery charges, so confirm the shipping setting with CDTFA or an accountant. Use Shopify's "Tax liability insights" page to see if any other state needs attention. Shopify calculates and collects the tax; it does not file or remit California sales tax for your own store, you do. Sources: https://help.shopify.com/en/manual/taxes/us/us-tax-setup and https://help.shopify.com/en/manual/taxes/us/us-tax-liability (read 2026-10-13).
4. **Give Gelato a resale certificate.** Gelato's help center says it needs a resale certificate on file to sell to you tax-exempt, and lists California among states where you must hold a state registration to claim that exemption. Once you have the CA permit, upload a CA resale certificate (CDTFA-230) in the Gelato dashboard so you aren't taxed twice. UNVERIFIED: whether Gelato is charging you tax on orders today. Check a Gelato invoice. Source: https://support.gelato.com/en/articles/8996142-sales-tax-exemption-instructions-for-marketplace-sellers (read 2026-10-13).
5. **File on the schedule CDTFA assigns.** CDTFA sets the frequency (yearly, quarterly or monthly) from your expected taxable sales. A small print shop will likely be yearly or quarterly (UNVERIFIED until assigned). You must file a return even if you had no sales. Quarterly returns are due Apr 30, Jul 31, Oct 31 and Jan 31; yearly returns are due Jan 31. Source: https://cdtfa.ca.gov/taxes-and-fees/sales-use-tax-returns-filing-dates.htm (read 2026-10-13).
6. **Out-of-state buyers.** You usually only need to collect in states where you have nexus (presence or a sales threshold). At current volume that is probably just California. Recheck Shopify's liability insights every quarter.
7. **Event work is separate.** Photography services delivered digitally are generally treated differently from physical prints. UNVERIFIED: confirm with your accountant so event invoices can keep showing $0.00 tax.
