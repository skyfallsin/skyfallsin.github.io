---
layout: default
title: all posts
---

<div class="post-list">
{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts %}
  <a href="{{ post.url }}" class="post-entry">
    <span class="post-date-col">
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if forloop.first and post.thumb %}<img src="{{ post.thumb }}" alt="" class="post-thumb theme-img-light" /><img src="{{ post.thumb_dark | default: post.thumb }}" alt="" class="post-thumb theme-img-dark" />{% endif %}
    </span>
    <span class="post-entry-title">{{ post.title }}</span>
  </a>
{% endfor %}
</div>
