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

## ABOUT

Hacker since 2000. Grew up in Chennai, moved to Maryland for high school and college, then the Bay Area to run startups.

I build teams that ship joyful consumer products (usually from scratch). I work with like-minded folk who prize quality, skill, speed and courage.

My businesses usually blend advanced engineering, delightful design, digital storytelling and aggressive BD. I'm very interested in products that have the unit economic structures to improve the quality of life for every person in the world. I keep co-founding with [Kevin Li](https://x.com/liveink) like it's a family tradition.

<div class="startup-entry">
<a href="https://askjo.ai" class="startup-logo"><img src="/images/logos/jo.png" alt="jo"></a>
<div class="startup-text"><strong><a href="https://askjo.ai">jo</a></strong> (YC W24) — After six months talking to LLMs for hours a day, I started building an AI that lives on your computer. Nascent.</div>
</div>

<div class="startup-entry">
<a href="https://techcrunch.com/2018/12/06/farmstead-is-an-ambitious-grocery-delivery-startup-with-plans-to-defeat-instacart/" class="startup-logo"><img src="/images/logos/farmstead.png" alt="Farmstead"></a>
<div class="startup-text"><strong><a href="https://techcrunch.com/2018/12/06/farmstead-is-an-ambitious-grocery-delivery-startup-with-plans-to-defeat-instacart/">Farmstead</a></strong> (YC S16) — My daughter turned two and started drinking a lot of milk. I found myself at the grocery store 3-4x a week. Posted on Nextdoor asking if anyone wanted milk, eggs, and bread delivered—200 people said yes in two days. Built an AI grocer that cut food waste from ~30% to 1.5%. Grew to 5 markets, double-digit millions in revenue, and a 200-person team of technologists, operators, drivers, and warehouse staff.</div>
</div>

<div class="startup-entry">
<a href="https://techcrunch.com/2012/12/04/kicksend-target-cvs/" class="startup-logo"><img src="/images/logos/kicksend.png" alt="Kicksend"></a>
<div class="startup-text"><strong><a href="https://techcrunch.com/2012/12/04/kicksend-target-cvs/">Kicksend</a></strong> (YC S11) — Co-founded with <a href="https://x.com/brendanlim">Brendan Lim</a>. Photo prints delivered to your door. Featured on the <a href="https://www.today.com/video/today/52066329">Today Show</a>. Millions of users, millions in revenue, and partnerships with CVS, Target, Walgreens, Walmart. Acquired by Lyft.</div>
</div>

<div class="startup-entry">
<a href="https://www.lyft.com" class="startup-logo"><img src="/images/logos/lyft.png" alt="Lyft"></a>
<div class="startup-text"><strong>Lyft</strong> — Stayed on after acquisition. Driver growth, unlocking conversion in major markets.</div>
</div>

I solo backpack, make landscape photos, and read a lot of fiction. Based in Silicon Valley.

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
  
  const masks = [
    '50%',
    '12px',
    '9999px'
  ];
  
  images.forEach(({id, file}) => {
    const a = document.createElement('a');
    a.href = `https://www.instagram.com/p/${id}/`;
    a.target = '_blank';
    a.className = 'instagram-thumb';
    const img = document.createElement('img');
    img.src = `/images/instagram/${file}`;
    img.alt = '';
    img.loading = 'lazy';
    img.style.borderRadius = masks[Math.floor(Math.random() * masks.length)];
    a.appendChild(img);
    grid.appendChild(a);
  });
})();
</script>
