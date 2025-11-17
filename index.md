---
layout: single
permalink: /
title: "Oleksandr Sobol"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/code-bg.jpg
  actions:
    - label: "About Me"
      url: "/about/"
    - label: "Projects"
      url: "/projects/"
    - label: "Contact"
      url: "/contact/"
excerpt: >
  Backend Software Developer | Building scalable automation systems and APIs with Python
---

## About

I'm a Backend Software Developer with experience building automation pipelines and scalable systems. 

**Current Focus:** Cybersecurity, backend automation, API development, system scalability, and cloud infrastructure

---

## Featured Projects

Check out my [projects page](/projects/) to see what I've built:
- **Utopia Account Creation (UAC)** - Customer onboarding automation with API integration from Utopia, Powercodem CRM.
- **DHCP Lease Runner (DLR)** - Equipment management automation for ISP operations using Mikrotik and Powercode CRM.
- **Expense Tracker** - Cross-platform mobile app built with Flutter
- And more on my [GitHub profile](https://github.com/OleksSobol)

---

## Latest Posts

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
<p>Posts coming soon.</p>
{% endif %}

---

## Continuous Learning

Actively expanding my backend development and security skills through:
- **Boot.dev** - Backend development
- **Harvard CS50x** - Introduction to Computer Science
- **Harvard CS50 Cybersecurity** - Security fundamentals and best practices


<p align="left">
  <img src="https://api.boot.dev/v1/users/public/0ad99ed2-be60-4b3b-8396-3c130c314deb/thumbnail" alt="Boot.dev Progress">
</p>

---

**Also explore:** [Drone aerial footage](/videos/) | [Download Resume](/assets/resume.pdf)
<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: 64
- XP Today: 0
- Total XP: 143
<!--BOOTDEV_STATS_END-->