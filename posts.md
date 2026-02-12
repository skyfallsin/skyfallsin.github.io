---
layout: default
title: all posts
---

<div class="post-list">
{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts %}
  {% if post.image %}
  <a href="{{ post.url }}" class="post-entry post-entry--img">
    <img src="{{ post.image }}" alt="" class="post-thumb" />
    <span class="post-entry-text">
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <span class="post-entry-title">{{ post.title }}</span>
    </span>
  </a>
  {% else %}
  <a href="{{ post.url }}" class="post-entry">
    <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    <span class="post-entry-title">{{ post.title }}</span>
  </a>
  {% endif %}
{% endfor %}
</div>
