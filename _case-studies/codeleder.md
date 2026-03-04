---
layout: single
title: "CodeLedger: An Offline-First Time Tracking & Invoicing App for Freelance Developers"
excerpt: "Built a Flutter mobile app from scratch to solve my own freelance billing problem — offline-first, encrypted backups, GitHub-integrated time tracking."
toc: true
toc_sticky: true
---

## The Problem

As a freelance developer, I needed a way to track billable hours and send professional invoices — without cloud lock-in, subscriptions, or tools that weren't built for developers.

Existing apps were either too bloated, required accounts, stored data on someone else's server, or had no concept of GitHub issues and repos as context for time entries. I wanted something that worked offline, kept data on my device, and produced invoices I'd actually be proud to send.

So I built it.

---

## Constraints

- **Offline-first** — must work with no internet connection; backup is opt-in, not required
- **No backend** — all data lives locally on device (SQLite); no server to maintain
- **Developer-specific** — needs GitHub issue/repo context on time entries, a "Modern Developer" invoice template
- **Solo project** — no team, no QA, no dedicated design; everything had to be simple and maintainable
- **Cross-platform target** — Flutter to support Android now, with iOS/web possible later without rewriting

---

## Architecture

```
┌─────────────────────────────────────────────┐
│                 Flutter App                 │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  Timer   │  │ Invoices │  │ Clients  │  │
│  │ Screen   │  │ Screen   │  │ Screen   │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │              │        │
│  ┌────▼──────────────▼──────────────▼─────┐ │
│  │           SQLite (local DB)            │ │
│  └────────────────────┬───────────────────┘ │
│                        │ (opt-in)            │
│  ┌─────────────────────▼───────────────────┐│
│  │     Google Drive Backup (AES-256-GCM)   ││
│  └─────────────────────────────────────────┘│
└─────────────────────────────────────────────┘
```

**Stack:** Flutter · Dart · SQLite · AES-256-GCM · Google Drive API · PDF generation

---

## Key Technical Decisions

### Decision 1: Local SQLite Over Any Cloud DB

**Context:** Needed persistent storage that worked offline and didn't require user accounts.

**Choice:** SQLite via `sqflite`, all data on device.

**Reasoning:** A cloud DB would introduce latency, require auth, and create a server dependency I'd have to maintain. SQLite is fast, proven, and gives users full ownership of their data. Backup becomes an explicit, user-controlled action rather than an automatic assumption.

### Decision 2: Encrypted Google Drive Backup Over a Custom Backup Server

**Context:** Users need a way to not lose their data if their phone dies.

**Choice:** Encrypt locally with AES-256-GCM + PBKDF2-HMAC-SHA256, then upload the encrypted blob to the user's own Google Drive.

**Reasoning:** I don't want to run a backup server, and users don't want their invoice data sitting on my infrastructure. With this approach, the backup goes into *their* Drive account — I never see it. Only they hold the decryption key (a password they choose).

### Decision 3: Manual Entry Alongside Timer

**Context:** Developers don't always remember to clock in before starting work.

**Choice:** Both a live timer *and* manual start/end time entry for every time log.

**Reasoning:** A timer-only app fails the moment you forget to start it. Supporting manual entry makes the app actually usable in real workflows, even if it's a bit more UI surface area.

### Decision 4: Editable Invoices

**Context:** Invoices sometimes need adjustments after generation — a rate change, a line item correction, a note.

**Choice:** Invoices remain editable after creation until explicitly sent/paid.

**Reasoning:** Locking invoices immediately after creation creates friction and frustration. Freelancers often draft, review, and revise before sending. The status workflow (Draft → Sent → Paid) signals intent without enforcing immutability too early.

---

## Results

| Metric | Outcome |
|---|---|
| Time to log a billable entry | < 5 seconds |
| Internet required for core use | None |
| Invoice templates | 3 (Minimal, Detailed, Modern Developer) |
| Data ownership | 100% on-device |
| Subscription cost | $0 |
| Lines of backend infrastructure | 0 |

---

## What I Learned

**Build for your own workflow first.** Every feature in CodeLedger exists because I personally ran into the problem it solves — the manual entry, the editable invoices, the GitHub refs. Building something you use yourself is the fastest feedback loop.

**Offline-first is a design constraint, not a feature.** Deciding early that there would be no required internet connection shaped every subsequent decision: local DB, opt-in backup, no auth system. It simplified the architecture significantly.

**Encryption UX is hard.** AES-256 is easy to implement. Explaining to a user that their backup password cannot be recovered — and that losing it means losing their data — requires careful copy and UI design, not just correct crypto.

---

*Built with: Flutter · Dart · SQLite · AES-256-GCM · Google Drive API*

[View Live Site](https://codeledger.osobol.com){: .btn .btn--primary}
[View on GitHub](https://github.com/OleksSobol/-CodeLedger-){: .btn}
[← Back to Case Studies](/case-studies/){: .btn}
