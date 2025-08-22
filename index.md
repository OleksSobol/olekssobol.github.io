---
layout: default
title: "Oleks' Lair"
---

Welcome to my hacker blog.  

- [About](/about/)  
- [Projects](/projects/)  

## Latest Posts
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}
