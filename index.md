---
layout: single
permalink: /
title: "Oleks Sobol"
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
  Software Engineer | Building scalable web applications and exploring AI/ML solutions
---

## About

I'm a software engineer passionate about full-stack development and artificial intelligence. I document my journey from network engineering to software development, sharing insights on practical coding challenges and solutions.

**Current Focus:** Python, JavaScript, AI agents, and modern web development

---

## Featured Projects

Check out my [projects page](/projects/) to see what I've been building, including:
- AI-powered applications
- Full-stack web development
- Automation tools and scripts

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

## Professional Development

Currently completing Boot.dev's computer science curriculum, focusing on backend development and algorithmic thinking.

<p align="left">
  <img src="https://api.boot.dev/v1/users/public/0ad99ed2-be60-4b3b-8396-3c130c314deb/thumbnail" alt="Boot.dev Progress">
</p>

---

**Also check out:** [Drone aerial footage](/videos/) | [GitHub](https://github.com/yourusername)