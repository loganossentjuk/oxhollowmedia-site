# Plugins playbook: Small Business, Brand Voice, Marketing (2026-11-04)

Reviewed by the manager against `Dropbox/Career/OxHollow/` and the repo. Rule: a plugin is used only where it saves Logan time *and* can be fed from something we already built. Nothing here is set up yet; each row says what it needs.

## What already exists (and must be reused, not rebuilt)
| Asset | Where | Reuse by |
|---|---|---|
| Brand voice: banned/preferred words, visual don'ts, tone | `Instagram Drafts/Zeely Brand DNA fields.md`, `Zeely brief.md` | Folded into `.claude/brand-voice-guidelines.md` (done today) |
| Brand look: colours, fonts, moon lockup, profile marks | `Logos/`, `brand/logos/` in repo, memory brand-spec | `small-business:brand-style` input; never re-derive |
| Business cards, email signature | `BusinessCards/` | brand-style; outreach-composer signature block |
| Invoices 001–003 (Semgrep), expense reports | `Invoices/`, `ExpenseReports/` | `proposal-builder` template + historical pricing; `invoice-chase` once a ledger exists |
| Etsy launch plan + 20 listings | `etsy-launch.md`, `etsy-listings.csv` | `marketing:content-creation` for listing copy; shop-manager owns |
| Photo competitions calendar | `Photo competitions 2026-27.md` | Calendar entries (small-business google-calendar) once Logan picks entries |
| Instagram content bank (15 captions, Aug 2026) | `StoreLaunch/OxHollow_Instagram_Content.md` | Mine for science hooks; strip employer-adjacent posts (Nautilus, NOAA trainings) per guidelines |
| Fable review of that bank | `StoreLaunch/OxHollow_FableReview.md` | Its fixes are now rules: vary CTAs, no closing-question-every-post, Reels scripts, bio defined |
| Digital Income Roadmap + Coastal Communicator's Toolkit | `StoreLaunch/` | **Parked.** Different business line (environmental-practitioner templates), leans on day-job credibility. Conflicts with the no-employer rule and the prints/events/films focus. Revisit only if Logan reopens it. |
| Second brain, post plan, formats, experiments | `team/brain/` | Source of truth for all social plugins |
| Print catalog, prices | `prints/catalog.json` | Only price source for any plugin output |

## Brand Voice plugin
| Skill | Use | Needs |
|---|---|---|
| `enforce-voice` | Every caption, pin, outreach draft, shop description before it reaches Logan. Manager rule in MANAGER.md. | Guidelines file (exists) |
| `generate-guidelines` | Re-run in Feb 2027 with 10 sent outreach emails + best captions | Logan's sent mail |
| `discover-brand` | Skip; materials are not scattered | — |
| QA agent | Weekly batch check before approval | — |

## Marketing plugin
| Skill | Use | Needs |
|---|---|---|
| `brand-review` | Second check on the weekly Instagram batch and Etsy listings | Guidelines |
| `content-creation` / `draft-content` | Etsy listing copy, print-page stories, newsletter | catalog.json, guidelines |
| `campaign-plan` | One use: holiday gift window (Gelato cut-offs → Dec), $0 ads | Gelato cut-off dates |
| `email-sequence` | Event-client follow-up (quote → booking → delivery → referral), 4 emails, drafts only | A first real client thread |
| `seo-audit` | Overlaps seo-specialist; use only for the keyword-gap piece quarterly | — |
| `performance-report` | Feeds the weekly report; replaces hand-built numbers section | Metricool + Shopify analytics (connected) |
| `competitive-brief` | Once: 5 Bay Area event photographers' positioning, for outreach angles | — |
| Canva, Klaviyo, Ahrefs, Similarweb connectors | Not authorised; not needed now | OAuth from Logan if ever |

## Small Business plugin
| Skill | Use | Needs |
|---|---|---|
| `brand-style` | Set once from site URL so every plugin output matches the brand | Logan runs it once (asks for his output preference) |
| `proposal-builder` | Event quotes from Semgrep invoice structure + real rates; routes to DocuSign if connected | Logan's rate card (the client-quote blocker) |
| `invoice-chase` | Overdue Semgrep-style invoices | A ledger (QuickBooks/Xero): none connected. Shopify + Stripe cover prints only |
| `cash-flow-snapshot`, `month-end-prep`, `tax-prep` | Useful once there's a ledger; CSV upload works now | Ledger or CSV export |
| `inbox-manager` | hello@ triage each Monday: leads vs bills vs noise, replies drafted | Gmail connected (yes) |
| `speed-to-lead` | Draft reply within the hour to inquiry-form emails | Gmail; Formspree → Gmail already routes |
| `crm-autopilot` | Spreadsheet CRM for event leads (no HubSpot) | Google Drive connected |
| `lead-finder` / `outreach-composer` / `grow-pipeline` | Bay Area tech event contacts; drafts only, Logan sends | Voice profile from sent mail |
| `social-content-engine`, `canva-creator` | Overlap with brain + Metricool pipeline; skip | — |
| `ad-manager` | $0 ads policy; skip until Etsy Ads data exists | — |
| `inventory-planner`, `payroll-prep`, `hiring-*`, `grant-rfp-writer` | Not applicable (print-on-demand, solo). Exception: `grant-rfp-writer` for Nat Geo early-career grant, if Logan wants that climb | — |

## First three to switch on (recommendation)
1. **`small-business:brand-style`** once, from oxhollowmedia.com, so every report and doc the plugins produce is on-brand. 5 minutes of Logan's time.
2. **`inbox-manager` + `speed-to-lead`** on hello@, Monday run + inquiry alerts. Gmail is already connected; this is where event revenue starts.
3. **`proposal-builder`** seeded with the Semgrep invoices, as soon as Logan sets his rate card. Unblocks the client-quote item that has sat in the backlog since October.

Everything else stays off until the thing it needs exists.
