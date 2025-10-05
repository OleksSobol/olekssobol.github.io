---
layout: single
permalink: /
title: "Oleks’ Hacker Lair 👾"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/code-bg.jpg
  actions:
    - label: "About Me"
      url: "/about/"
    - label: "Projects"
      url: "/projects/"
    - label: "Latest Commits"
      url: "/commits/"
excerpt: >
  Welcome to my digital playground — projects, experiments, and late-night hacks.
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

<p><a href="/blog/">See all posts →</a></p>
{% else %}
<p>No posts yet. Stay tuned.</p>
{% endif %}

<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: 62
- XP Today: 132
- Total XP: 860
<!--BOOTDEV_STATS_END-->

<p align="left">
  <img src="https://api.boot.dev/v1/users/public/0ad99ed2-be60-4b3b-8396-3c130c314deb/thumbnail" >
</p>
