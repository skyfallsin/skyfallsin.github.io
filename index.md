---
layout: default
title: pradeep
---

## RECENT WRITING

<ul class="post-list post-list--home">
{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts limit:5 %}
  <li>
    <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

{% if published_posts.size > 5 %}
<a href="/posts" class="more-link">more →</a>
{% endif %}

## PHONE PICS

<div class="instagram-grid-wrapper" id="instagram-wrapper">
  <div class="instagram-grid" id="instagram-grid"></div>
  <div class="show-more" onclick="document.getElementById('instagram-wrapper').classList.add('expanded')">show more ↓</div>
</div>

<script>
(function() {
  const images = [
    {id: 'DK6OJfyOsAl', file: '01.jpg'},
    {id: 'DBNaowMv-aT', file: '02.jpg'},
    {id: 'C7cZQYOPrWj', file: '03.jpg'},
    {id: 'CiTZunsPk3d', file: '04.jpg'},
    {id: 'CeQBNwsrVli', file: '05.jpg'},
    {id: 'CdvyTVbp5op', file: '06.jpg'},
    {id: 'CdZvNIvrwqL', file: '07.jpg'},
    {id: 'CdCwY6uLX1G', file: '08.jpg'},
    {id: 'Ccrf1_ZrJ9L', file: '09.jpg'},
    {id: 'CcmaGWWLxa2', file: '10.jpg'},
    {id: 'Cbbp--eOpHF', file: '11.jpg'},
    {id: 'CbVTfkFJDZx', file: '12.jpg'},
    {id: 'CbTMZWevxMs', file: '13.jpg'},
    {id: 'Ca6Q2BhLFVI', file: '14.jpg'},
    {id: 'Ca1D00gLt2L', file: '15.jpg'},
    {id: 'Cad9t2Vr9i2', file: '16.jpg'},
    {id: 'CW2HdBvLKx8', file: '17.jpg'},
    {id: 'CVLc6o2vpUq', file: '18.jpg'},
    {id: 'CVLEkcglj7h', file: '19.jpg'},
    {id: 'CUKrT7UlRo5', file: '20.jpg'},
    {id: 'COrYRzap1oL', file: '21.jpg'},
    {id: 'COamjwHJWM4', file: '22.jpg'},
    {id: 'COYEBhxJk0p', file: '23.jpg'},
    {id: 'COWQn_WJIUE', file: '24.jpg'}
  ];
  
  for (let i = images.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [images[i], images[j]] = [images[j], images[i]];
  }
  
  const grid = document.getElementById('instagram-grid');
  
  images.forEach(({id, file}) => {
    const a = document.createElement('a');
    a.href = `https://www.instagram.com/p/${id}/`;
    a.target = '_blank';
    a.className = 'instagram-thumb';
    const img = document.createElement('img');
    img.src = `/images/instagram/${file}`;
    img.alt = '';
    img.loading = 'lazy';
    a.appendChild(img);
    grid.appendChild(a);
  });
})();
</script>
