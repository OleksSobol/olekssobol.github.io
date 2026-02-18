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

# I build backend systems that eliminate manual work.

Production automation serving 4000+ clients. 95% faster onboarding. 99.9% uptime.

<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0;">
  <span class="tech-badge">Python</span>
  <span class="tech-badge">Go</span>
  <span class="tech-badge">Flask</span>
  <span class="tech-badge">FastAPI</span>
  <span class="tech-badge">Docker</span>
  <span class="tech-badge">REST APIs</span>
  <span class="tech-badge">MySQL</span>
  <span class="tech-badge">Linux</span>
</div>

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;">
  <a href="/case-studies/" class="btn btn--primary">See Case Studies</a>
  <a href="/assets/resume.pdf" class="btn">Download Resume</a>
</div>

---

## Impact by the Numbers

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div class="metric-card">
    <div class="metric-number">4000+</div>
    <div class="metric-label">Clients Served</div>
  </div>
  <div class="metric-card">
    <div class="metric-number">95%</div>
    <div class="metric-label">Faster Onboarding</div>
  </div>
  <div class="metric-card">
    <div class="metric-number">15+</div>
    <div class="metric-label">Hours Saved Weekly</div>
  </div>
  <div class="metric-card">
    <div class="metric-number">99.9%</div>
    <div class="metric-label">System Uptime</div>
  </div>
</div>

---

## Featured Work

<div style="display: grid; gap: 1rem; margin: 2rem 0;">

<a href="/case-studies/uac/" class="project-card">
  <div class="project-title">Utopia Account Creation (UAC)</div>
  <div class="project-desc">Production automation serving 4000+ clients. Reduced ISP customer onboarding from 20 minutes to under 1 minute. 90% reduction in manual errors.</div>
</a>

<a href="/case-studies/dlr/" class="project-card">
  <div class="project-title">DHCP Lease Runner (DLR)</div>
  <div class="project-desc">ISP equipment management automation. Multi-threaded processing saves 15+ hours per week per technician.</div>
</a>

</div>

[View All Case Studies](/case-studies/){: .btn .btn--primary}

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

[Read More](/blog/){: .btn .btn--primary}
{% else %}
<p style="color: #b0b0b0;">Technical deep dives coming soon — lessons from building production automation systems.</p>
{% endif %}

---

<div class="text-center mt-4">
  <a href="/services/" class="btn btn--primary">What I Build</a>
  <a href="/about/" class="btn">About Me</a>
</div>
