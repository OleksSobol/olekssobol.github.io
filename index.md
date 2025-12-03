---
layout: single
permalink: /
author_profile: true
title: ""
header:
  overlay_color: "#0d0d0d"
  overlay_filter: "0.7"
classes: wide
---

# Building systems at 2 AM. Breaking things until they work.

Backend engineer specializing in automation that turns manual chaos into efficient systems.

<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0;">
  <span class="tech-badge">Python</span>
  <span class="tech-badge">Go</span>
  <span class="tech-badge">FastAPI</span>
  <span class="tech-badge">Docker</span>
  <span class="tech-badge">REST APIs</span>
  <span class="tech-badge">MySQL</span>
  <span class="tech-badge">Linux</span>
</div>

---

## Featured Projects

<div style="display: grid; gap: 1rem; margin: 2rem 0;">

<a href="https://github.com/OleksSobol/Utopia-Account-Creation---UAC" class="project-card" target="_blank" rel="noopener">
  <div class="project-title">Utopia Account Creation (UAC)</div>
  <div class="project-desc">Production automation serving 4000+ clients. Reduced onboarding from 20 minutes to under 1 minute. 90% reduction in manual errors.</div>
</a>

<a href="https://github.com/OleksSobol/DHCP-LEASE-RUNNER---DLR" class="project-card" target="_blank" rel="noopener">
  <div class="project-title">DHCP Lease Runner (DLR)</div>
  <div class="project-desc">ISP equipment management automation. Multi-threaded processing saves 15+ hours weekly.</div>
</a>

<a href="https://github.com/OleksSobol/expenses-tracker" class="project-card" target="_blank" rel="noopener">
  <div class="project-title">Expense Tracker</div>
  <div class="project-desc">Cross-platform Flutter app for personal finance with visual analytics and smart categorization.</div>
</a>

</div>

[View All Projects →](/projects/){: .btn .btn--primary}

---

## Recent Posts

{% if site.posts.size > 0 %}
<div style="margin: 1.5rem 0;">
{% for post in site.posts limit:3 %}
  <div class="archive__item" style="margin-bottom: 1rem;">
    <h3 class="archive__item-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="archive__item-excerpt">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    <p style="color: #6a6a6a; font-size: 0.85rem;">{{ post.date | date: "%B %d, %Y" }}</p>
  </div>
{% endfor %}
</div>

[Read More →](/blog/){: .btn .btn--primary}
{% else %}
<p style="color: #b0b0b0;">Posts coming soon. Technical deep dives and lessons learned from production systems.</p>
{% endif %}

---

## Playground

Random experiments, automation scripts, and tools I build for fun. Sometimes useful. Always educational.

[Explore the Chaos →](/playground/){: .btn .btn--primary}

---

<div class="highlight-box">

<p><strong>Currently Learning:</strong></p>
<ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
  <li>Boot.dev — Backend development & algorithms</li>
  <li>Harvard CS50x — Computer Science fundamentals</li>
  <li>Harvard CS50 Cybersecurity — Security principles</li>
</ul>

<img src="https://api.boot.dev/v1/users/public/0ad99ed2-be60-4b3b-8396-3c130c314deb/thumbnail" alt="Boot.dev Progress" style="margin-top: 1rem; max-width: 100%;" loading="lazy">

</div>

<div class="text-center mt-4">
  <a href="/about/" class="btn btn--primary">About Me</a>
  <a href="/assets/resume.pdf" class="btn btn--primary">Resume</a>
</div>
<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: 67
- XP Today: -2905
- Total XP: 2126
<!--BOOTDEV_STATS_END-->