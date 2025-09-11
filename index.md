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
- Level: 56
- XP Today: 1368
- Total XP: 3940
<!--BOOTDEV_STATS_END-->