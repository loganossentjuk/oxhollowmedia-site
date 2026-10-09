# The Ox Hollow team

An AI team that works on the business every week and hands Logan one pull request to approve.

```
Logan (owner: approves and merges)
  └── Manager (weekly Claude routine, team/MANAGER.md)
        ├── SEO specialist     .claude/agents/seo-specialist.md
        ├── Content expert     .claude/agents/content-writer.md
        ├── Web engineer / QA  .claude/agents/web-engineer.md
        ├── Shop analyst       .claude/agents/shop-manager.md
        └── Marketing lead     .claude/agents/marketing-lead.md
```

## How it works
- **When it runs:** every Monday morning (Pacific), a scheduled Claude routine starts a fresh session on this repo and follows `team/MANAGER.md`.
- **The manager:** plans the week from `team/BACKLOG.md`, sends the specialists out in parallel, and reviews everything they did. Each specialist researches before working and cites sources.
- **What Logan gets:**
  - A pull request "Team week of …" with:
    - the site changes
    - `team/reports/<date>.md`, with a summary and a "Needs you" checklist
    - drafts in `team/drafts/`: Instagram posts, outreach notes, newsletter
  - Cloudflare builds a preview of the branch. Merge the PR to publish, or close it to throw the week away.

## What the team can't do (on purpose)
- merge, or push to the live site
- change prices or Shopify, Gelato, Stripe or DNS
- post, email or message anyone
- spend money

Full rules: `team/BUSINESS.md`.

## Steering the team
- **Priorities:** edit `team/BACKLOG.md` (move things up, add ideas, mark approvals). Or leave a comment on the weekly PR; the next run reads open PRs.
- **Facts:** answer `TODO(Logan)` questions by adding the facts to `team/BUSINESS.md`, so every member learns them.
- **Schedule:** change it or pause it in claude.ai → Routines ("Ox Hollow weekly team").
