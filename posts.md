---
layout: default
title: all posts
---

<div class="post-list">
{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts %}
  <a href="{{ post.url }}" class="post-entry">
    <span class="post-entry-title">{{ post.title }}</span>
    <time class="post-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
  </a>
{% endfor %}
</div>
