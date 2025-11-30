---
layout: single
permalink: /
title: "Oleksandr Sobol"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/code-bg.jpg
  actions:
    - label: "View Projects"
      url: "/projects/"
    - label: "About Me"
      url: "/about/"
    - label: "Get in Touch"
      url: "/contact/"
excerpt: >
  Backend Software Developer — Turning 20-minute processes into sub-1-minute automation | 4000+ clients served | 90% reduction in manual errors
---

<style>
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}
.metric-card {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  border: 1px solid #3a3a3a;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.2s, border-color 0.2s;
}
.metric-card:hover {
  transform: translateY(-4px);
  border-color: #52adc8;
}
.metric-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #52adc8;
  line-height: 1.2;
}
.metric-label {
  font-size: 0.9rem;
  color: #b0b0b0;
  margin-top: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.tech-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin: 1.5rem 0;
}
.tech-badge {
  background: #2d2d2d;
  border: 1px solid #3a3a3a;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  font-size: 0.85rem;
  color: #e0e0e0;
  font-weight: 500;
}
.highlight-box {
  background: linear-gradient(135deg, #1a2332 0%, #1a1a1a 100%);
  border-left: 4px solid #52adc8;
  padding: 1.5rem;
  border-radius: 4px;
  margin: 2rem 0;
}
.project-quick-link {
  display: block;
  background: #1a1a1a;
  border: 1px solid #3a3a3a;
  border-radius: 6px;
  padding: 1rem 1.2rem;
  margin: 0.8rem 0;
  text-decoration: none;
  transition: all 0.2s;
}
.project-quick-link:hover {
  border-color: #52adc8;
  background: #2d2d2d;
  transform: translateX(4px);
}
.project-title {
  font-weight: 600;
  color: #52adc8;
  font-size: 1.1rem;
}
.project-desc {
  color: #b0b0b0;
  font-size: 0.9rem;
  margin-top: 0.4rem;
}

/* Accessibility & keyboard focus improvements */
.project-quick-link {
  cursor: pointer;
}
.project-quick-link:focus {
  outline: 3px solid #52adc8;
  transform: none;
  box-shadow: 0 0 0 4px rgba(82,173,200,0.12);
}
</style>

<main role="main">

## Backend Developer | Automation Specialist

I build scalable automation systems and APIs that improve operational efficiency and remove repetitive manual work. With 4+ years of experience, I specialize in Python, Go, and cloud infrastructure.


<div class="tech-badges">
  <span class="tech-badge">Python</span>
  <span class="tech-badge">Go</span>
  <span class="tech-badge">Flask</span>
  <span class="tech-badge">FastAPI</span>
  <span class="tech-badge">Docker</span>
  <span class="tech-badge">AWS</span>
  <span class="tech-badge">REST APIs</span>
  <span class="tech-badge">MySQL</span>
  <span class="tech-badge">MongoDB</span>
  <span class="tech-badge">Linux</span>
</div>

---

## Featured Projects

<a href="/projects/#utopia-account-creation-uac" class="project-quick-link" aria-label="Utopia Account Creation (UAC) project">
  <div class="project-title">Utopia Account Creation (UAC)</div>
  <div class="project-desc">Production automation serving 4000+ clients — Reduced onboarding from 20 minutes to under 1 minute</div>
</a>

<a href="/projects/#dhcp-lease-runner-dlr" class="project-quick-link" aria-label="DHCP Lease Runner (DLR) project">
  <div class="project-title">DHCP Lease Runner (DLR)</div>
  <div class="project-desc">ISP equipment management automation — Saving 15+ hours weekly with multi-threaded processing</div>
</a>

<a href="/projects/#expense-tracker" class="project-quick-link" aria-label="Expense Tracker project">
  <div class="project-title">Expense Tracker</div>
  <div class="project-desc">Cross-platform mobile app built with Flutter — Personal finance management with visual analytics</div>
</a>

[View All Projects →](/projects/){: .btn .btn--primary}

---

## Latest from the Blog

{% if site.posts.size > 0 %}
<ul class="latest-posts">
  {% for post in site.posts limit:5 %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small> — {{ post.date | date: "%b %d, %Y" }}</small>
  </li>
  {% endfor %}
</ul>

<p><a href="/blog/">View all posts →</a></p>
{% else %}
<p>Posts coming soon — Check back for technical deep dives and lessons learned.</p>
{% endif %}

---

## Continuous Learning & Growth

<div class="highlight-box">
I'm committed to continuous improvement through structured learning programs:

- **Boot.dev** — Backend development & algorithms
- **Harvard CS50x** — Computer Science fundamentals
- **Harvard CS50 Cybersecurity** — Security principles & implementation

<p align="left" style="margin-top: 1rem;">
  <img src="https://api.boot.dev/v1/users/public/0ad99ed2-be60-4b3b-8396-3c130c314deb/thumbnail" alt="Boot.dev Progress" loading="lazy">
</p>
</div>

---

## Beyond Development

**FAA Part 107 Certified Pilot** — Check out my [aerial drone footage](/videos/) captured across Montana and Washington.

---

<div style="text-align: center; margin: 2rem 0;">
  <a href="/about/" class="btn btn--info" aria-label="Learn more about me">Learn More About Me</a>
  <a href="/playground/" class="btn btn--success" aria-label="Open the playground">Try the Playground</a>
  <a href="/assets/resume.pdf" class="btn btn--primary" aria-label="Download resume">Download Resume</a>
</div>

</main>
<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: 64
- XP Today: 1200
- Total XP: 5031
<!--BOOTDEV_STATS_END-->