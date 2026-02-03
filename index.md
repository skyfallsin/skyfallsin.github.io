---
layout: default
title: pradeep
---

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url }}">{{ post.title }}{% unless post.published == true or post.published == nil %} <span class="unpublished-badge">[unpublished]</span>{% endunless %}</a>
  </li>
{% endfor %}
</ul>
