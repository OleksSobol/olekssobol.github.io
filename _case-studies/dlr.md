---
layout: single
title: "Automating ISP Equipment Management: 15+ Hours Saved Per Week"
excerpt: "Multi-threaded DHCP lease processing for ISP operations"
toc: true
toc_sticky: true
---

## The Problem

Field technicians at a regional ISP spent over 15 hours per week manually tracking DHCP leases across network infrastructure. Every service call required looking up equipment status, cross-referencing lease data, and verifying connectivity — all through manual processes spread across multiple systems.

There was no centralized view. Technicians queried devices one at a time, waited for responses, and manually compiled the information they needed. During outages, this bottleneck meant slower diagnosis and longer customer downtime.

## Constraints

- **Performance-critical** — technicians waited on results during live service calls. Slow meant unacceptable.
- **Many devices, concurrent queries** — the network had hundreds of devices. Sequential processing was too slow.
- **Must integrate with existing ISP infrastructure** — no greenfield deployment. The tool had to work with what was already in place.
- **Reliability** — partial failures (unreachable devices, timeouts) needed to degrade gracefully, not crash the entire run.

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Operator   │────▶│     DLR      │────▶│   Network    │
│  (Trigger)   │     │  (Python)    │     │   Devices    │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                     ┌──────┴───────┐
                     │  Thread Pool │
                     │  (Parallel)  │
                     └──────┬───────┘
                            │
                            ▼
                     ┌──────────────┐
                     │   Reports    │
                     │  (Output)    │
                     └──────────────┘
```

**Core:** Python application with thread pool for concurrent device queries
**Input:** Network device inventory
**Output:** Consolidated lease reports with equipment status

## Key Technical Decisions

### Decision 1: Multi-threading Over Async

**Context:** Needed to query hundreds of network devices concurrently. Both threading and async I/O were options.

**Choice:** Thread pool with `concurrent.futures.ThreadPoolExecutor`.

**Reasoning:** The workload is I/O-bound (waiting on network device responses), which threading handles well. The processing per device is straightforward — no complex state sharing between threads. `ThreadPoolExecutor` provides clean worker management, automatic thread reuse, and simple error handling. Async would have required restructuring all the device communication code for marginal benefit at this scale.

### Decision 2: Direct Lease File Parsing

**Context:** Could either poll devices via SNMP or parse lease files directly.

**Choice:** Direct parsing of DHCP lease files.

**Reasoning:** Faster and more reliable than SNMP polling. Lease files contain the authoritative state. SNMP adds a network round-trip and another failure point. Parsing is deterministic — the same file always produces the same result.

### Decision 3: Graceful Degradation

**Context:** Network devices go offline. Queries time out. A single unreachable device shouldn't break the entire report.

**Choice:** Per-device error handling with timeout limits. Failed devices are logged and skipped, not fatal.

**Reasoning:** In a network environment, some percentage of devices will always be unreachable. The report is most valuable when it shows "here's everything we could reach, and here's what we couldn't." Partial results beat no results.

## Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Weekly time spent on lease management | 15+ hours | < 1 hour | **93% reduction** |
| Device query speed | Sequential (minutes) | Parallel (seconds) | **Orders of magnitude faster** |
| Equipment visibility | Per-device manual lookup | Centralized report | **Single source of truth** |
| Failure handling | Manual retries | Automatic skip + log | **Hands-off resilience** |

## What I Learned

**Threading is underrated for I/O-bound network tools.** The async ecosystem gets more attention, but for "query N devices and collect results," a thread pool is simpler, easier to debug, and just as fast in practice. The right tool depends on the workload, not the trend.

**Network tools need to expect failure.** Designing for the happy path is easy. Designing for "30% of devices are unreachable and we still need useful output" is where the real engineering happens.

---

*Built with: Python, concurrent.futures, DHCP lease parsing, network automation*

<div class="text-center mt-4">
  <a href="/contact/" class="btn btn--primary">Have a Similar Problem? Let's Talk</a>
  <a href="/case-studies/" class="btn">More Case Studies</a>
</div>
