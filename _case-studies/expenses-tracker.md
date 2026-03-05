---
layout: single
title: "Expenses Tracker: A Privacy-First Personal Finance App"
excerpt: "Built an offline-first Flutter app to track personal income, expenses, and recurring bills — no accounts, no cloud, no subscriptions."
toc: true
toc_sticky: true
---

## The Problem

Most personal finance apps require an account, sync your data to the cloud, and charge a monthly subscription. For something as sensitive as financial data, that's a big ask.

I wanted a simple app to log transactions, track recurring bills, and visualize spending — with zero data leaving the device and zero ongoing cost. Nothing I found hit all three requirements without trade-offs I wasn't willing to make.

So I built it.

---

## Constraints

- **Fully offline** — no network calls, no accounts, no backend to maintain
- **Privacy-first** — all data stays in SQLite on-device; no analytics, no tracking
- **Free, no subscriptions** — distributed as a free APK; the business model is "just use it"
- **Solo project** — no dedicated QA; simplicity and correctness had to be built in from the start
- **Android target** — Flutter for cross-platform potential without rewriting later

---

## Architecture

```
┌──────────────────────────────────────────────┐
│                Flutter App                   │
│                                              │
│  ┌──────────┐ ┌──────────┐ ┌─────────────┐  │
│  │   Home   │ │  Bills   │ │   Reports   │  │
│  │ Dashboard│ │ Screen   │ │   Screen    │  │
│  └────┬─────┘ └────┬─────┘ └──────┬──────┘  │
│       │             │              │          │
│  ┌────▼─────────────▼──────────────▼───────┐ │
│  │         SQLite (expenses_tracker.db)    │ │
│  │   transactions · bills · categories    │ │
│  └────────────────────┬────────────────────┘ │
│                        │                      │
│  ┌─────────────────────▼───────────────────┐ │
│  │   Local Notifications (bill reminders)  │ │
│  └─────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Stack:** Flutter · Dart · SQLite · fl_chart · Google ML Kit · flutter_local_notifications

---

## Key Technical Decisions

### Decision 1: SQLite Over SharedPreferences for Transactions

**Context:** Needed structured, queryable storage for transactions, bills, and categories with relationships between them.

**Choice:** SQLite via `sqflite` with a proper relational schema.

**Reasoning:** SharedPreferences is key-value only — not suitable for filtering, joining, or aggregating financial data. SQLite gives full SQL query power for reports (sum by category, filter by date range) without network dependency.

### Decision 2: Receipt Scanning via On-Device OCR

**Context:** Manual amount entry is the friction point that kills daily usage of finance apps.

**Choice:** Google ML Kit text recognition running entirely on-device.

**Reasoning:** No data leaves the device — consistent with the privacy-first promise. ML Kit handles recognition locally without API keys or network calls. Users can point the camera at a receipt and have the amount and notes pre-filled.

### Decision 3: Local Notifications for Bill Reminders

**Context:** Recurring bills are the most common source of late fees and missed payments.

**Choice:** `flutter_local_notifications` with per-bill scheduled notifications and auto-calculated next due dates.

**Reasoning:** A bill tracker without reminders is just a list. Scheduling notifications locally (no push notification server needed) keeps the app fully self-contained while delivering real utility — the app tells you when rent is due, not just when you remember to check.

### Decision 4: Custom Categories with Icon + Color Pickers

**Context:** Default categories never fit everyone's spending patterns.

**Choice:** Full custom category creation with icon picker (Material icon set) and color picker.

**Reasoning:** A finance app that forces you into rigid categories gets abandoned. Letting users model their own spending vocabulary makes the data more meaningful and the app more likely to stay in daily use.

---

## Results

| Metric | Outcome |
|---|---|
| Internet required | None |
| Account required | None |
| Subscription cost | $0 |
| Data leaves device | Never |
| Receipt entry time | ~3 seconds (OCR) vs ~15s (manual) |
| Supported frequencies | Daily / Weekly / Monthly / Yearly |
| Export formats | CSV |

---

## What I Learned

**Privacy is a feature, not a constraint.** Designing around "no network calls" actually simplified the architecture significantly — no auth, no sync conflicts, no API rate limits, no backend maintenance. The constraint produced a cleaner system.

**OCR is only useful if it's fast.** Receipt scanning had to feel instant or users wouldn't bother. On-device ML Kit processes in under a second on modern devices, which clears the bar. If it had required a round-trip to a server, the UX would have been worse than just typing.

**Recurring logic is harder than it looks.** Calculating the next due date correctly across DST transitions, month-end edge cases (what's "monthly" from Jan 31?), and leap years took more care than expected. Getting this wrong destroys user trust in a bill tracker.

---

*Built with: Flutter · Dart · SQLite · Google ML Kit · fl_chart · flutter_local_notifications*

[View Live Site](https://expenses-tracker.osobol.com){: .btn .btn--primary}
[← Back to Case Studies](/case-studies/){: .btn}
