---
layout: single
title: "How I Reduced ISP Customer Onboarding from 20 Minutes to Under 60 Seconds"
excerpt: "Production automation serving 4000+ clients with 99.9% uptime"
toc: true
toc_sticky: true
---

## The Problem

A regional ISP was onboarding every new fiber customer manually. Each account required data entry into two separate systems — PowerCode (billing and service management) and Utopia Fiber (network provisioning). The process took approximately 20 minutes per customer, required knowledge of both platforms, and was error-prone.

During peak sign-up periods, the backlog grew. Incorrect service tiers, missed billing codes, and data mismatches between systems created downstream support tickets. The manual process was the bottleneck.

## Constraints

- **Two external APIs** with different authentication models and data formats — both had to be orchestrated in a single workflow
- **Must not disrupt existing billing** — the system needed to integrate alongside current processes, not replace them overnight
- **Single developer** — I designed, built, deployed, and maintained this solo
- **Edge case handling** — partial failures (one API succeeds, the other fails) needed graceful recovery, not silent corruption
- **Config changes are frequent** — billing rules, service tiers, and portal settings change regularly and shouldn't require code deployments

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Browser    │────▶│  Flask App   │────▶│  PowerCode   │
│   (Staff)    │     │   (UAC)      │     │    API       │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │ Utopia Fiber │
                     │     API      │
                     └──────────────┘
```

**Runtime:** Flask + uWSGI behind Nginx on Linux

**Config layer:**
- `.env` — True secrets (API keys, admin credentials, service URLs). Loaded once at startup.
- `app_settings.json` — Operational config (email templates, service tags, SSL settings, portal passwords, ticket templates). Read fresh on every request.
- `billing_settings.json` — Billing rules and credit policies. Read fresh on every request.
- `users.json` — Application user accounts with bcrypt-hashed passwords.

## Key Technical Decisions

### Decision 1: JSON Config Files Over a Database

**Context:** Billing rules, email templates, and service tier mappings change frequently. The operations team needed to adjust these without developer intervention.

**Choice:** JSON files with a read-fresh-each-call pattern instead of a relational database.

**Reasoning:** The data is small (kilobytes), access patterns are simple (read whole file, update whole file), and the operations team is comfortable editing structured text. A database would have added deployment complexity (migrations, connection pooling, backup strategy) for a problem that didn't need relational queries. The JSON managers reload on every request, so config changes take effect immediately — no restart required.

### Decision 2: Read-Fresh-Each-Call Pattern

**Context:** Operational config changes shouldn't require service restarts. But caching introduces staleness risk.

**Choice:** Every API call reads the JSON config file from disk. No caching layer.

**Reasoning:** File reads at this scale (< 10 KB files, ~100 requests/day) are effectively free. The simplicity of "what's on disk is what's in use" eliminates an entire class of bugs around cache invalidation. The trade-off (microseconds of disk I/O per request) is irrelevant at this traffic volume.

### Decision 3: Flask Over FastAPI

**Context:** FastAPI was the trendier choice. Flask was mature and well-understood.

**Choice:** Flask with uWSGI.

**Reasoning:** The workflow is fundamentally sequential — create account in PowerCode, then provision in Utopia, then configure billing. Async would add complexity without benefit since each step depends on the previous one. Flask's synchronous model maps directly to the business logic. The team (me) had deep Flask experience. Ship speed mattered more than framework novelty.

### Decision 4: Role-Based User Management

**Context:** Multiple staff members needed access, but not all should change billing configuration.

**Choice:** Built-in user management with a `can_view_config` permission flag, bcrypt password hashing, and a web UI for user administration.

**Reasoning:** An external auth provider (OAuth, LDAP) would be overkill for a 5-person team. The built-in system keeps the deployment self-contained — no external dependencies that could fail independently.

## Implementation Highlights

All JSON config managers follow the same pattern — simple, consistent, easy to extend:

```python
class AppSettingsManager:
    """Read-fresh-each-call pattern for operational config.

    Every request reads from disk. No caching.
    Config changes take effect immediately without restart.
    """
    def __init__(self, path="app/data/app_settings.json"):
        self.path = path
        self._ensure_file_exists()

    def _load(self):
        with open(self.path) as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=2)

    def _ensure_file_exists(self):
        """Bootstrap from .env on first run."""
        if not os.path.exists(self.path):
            self._save(self._default_from_env())
```

The same `_load()/_save()/_ensure_file_exists()` pattern is used by `BillingManager` and `UserManager`. This consistency makes the codebase predictable — if you understand one manager, you understand all three.

## Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Time per account | ~20 minutes | < 1 minute | **95% reduction** |
| Manual errors | ~15/week | ~1/week | **93% reduction** |
| Clients served | Manual capacity limit | 4000+ | **Scaled to demand** |
| System uptime | N/A | 99.9% | **Production-grade** |
| Config change deployment | Service restart | Immediate | **Zero downtime** |

## What I Learned

The biggest lesson was that **infrastructure decisions should match the actual scale of the problem.** JSON files instead of a database, Flask instead of FastAPI, built-in auth instead of OAuth — each "simpler" choice saved weeks of development time and eliminated maintenance burden, with zero compromise on reliability at this scale.

The second lesson was that **config architecture matters more than code architecture** for operational systems. The team interacts with config 10x more often than they interact with the code. Making config changes safe, immediate, and restart-free was the single highest-ROI design decision.

---

*Built with: Python, Flask, uWSGI, REST APIs, PowerCode API, Utopia Fiber API*

<div class="text-center mt-4">
  <a href="/contact/" class="btn btn--primary">Have a Similar Problem? Let's Talk</a>
  <a href="/case-studies/" class="btn">More Case Studies</a>
</div>
