# create_post.py
import datetime
import os

title = input("Title: ")
categories = input("Categories (comma-separated): ")
filename_title = title.lower().replace(" ", "-")
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S -0700")

filename = f"_posts/{datetime.datetime.now().strftime('%Y-%m-%d')}-{filename_title}.md"

content = input("Write your post content:\n")

with open(filename, "w") as f:
    f.write(f"""---
layout: single
title: "{title}"
date: {date}
categories: {categories}
---

{content}
""")

print(f"Post created: {filename}")
