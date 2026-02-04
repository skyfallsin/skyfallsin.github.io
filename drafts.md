---
layout: default
title: Drafts
published: false
---

# Drafts

<ul class="post-list">
{% for post in site.posts %}
  {% if post.published == false %}
  <li>
    <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endif %}
{% endfor %}
</ul>
