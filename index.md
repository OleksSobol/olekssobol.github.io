---
layout: default
title: "Oleks' Lair"
---

# Welcome to Oleks’ Hacker Lair 👾

- [About](/about/)
- [Projects](/projects/)
- [Latest Commits](/commits/)

## Latest Posts
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}
