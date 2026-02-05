---
layout: default
title: all posts
---

<ul class="post-list">
{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts %}
  <li>
    <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
