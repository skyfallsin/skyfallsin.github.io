---
layout: default
title: pradeep
---

## RECENT WRITING <a href="/feed.xml" class="rss-icon" aria-label="RSS Feed"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="6.18" cy="17.82" r="2.18"/><path d="M4 4.44v2.83c7.03 0 12.73 5.7 12.73 12.73h2.83c0-8.59-6.97-15.56-15.56-15.56zm0 5.66v2.83c3.9 0 7.07 3.17 7.07 7.07h2.83c0-5.47-4.43-9.9-9.9-9.9z"/></svg></a>

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

My businesses usually blend engineering, design, storytelling & BD. I'm very interested in products that have the unit economic structures to improve the quality of life for every person in the world.

I solo backpack, make landscape photos, and read a lot of fiction. Based in Silicon Valley.

## PROJECTS

<div class="startup-entry">
<a href="https://askjo.ai" class="startup-logo"><img src="/images/logos/jo.png" alt="jo"></a>
<div class="startup-text"><strong><a href="https://askjo.ai">jo</a></strong> (YC W24) — Co-founded with <a href="https://x.com/liveink">Kevin Li</a>. After six months talking to LLMs for hours a day, I started building an AI that lives on your computer. Nascent.</div>
</div>

<div class="startup-entry">
<a href="https://techcrunch.com/2018/12/06/farmstead-is-an-ambitious-grocery-delivery-startup-with-plans-to-defeat-instacart/" class="startup-logo"><img src="/images/logos/farmstead.png" alt="Farmstead"></a>
<div class="startup-text"><strong><a href="https://techcrunch.com/2018/12/06/farmstead-is-an-ambitious-grocery-delivery-startup-with-plans-to-defeat-instacart/">Farmstead</a></strong> (YC S16) — Co-founded with <a href="https://x.com/liveink">Kevin Li</a>. My daughter turned two and started drinking a lot of milk. I found myself at the grocery store 3-4x a week. Posted on Nextdoor asking if anyone wanted milk, eggs, and bread delivered—200 people said yes in two days. Built a vertically integrated AI grocer that cut food waste from ~30% to 1.5%. Grew to 5 markets, double-digit millions in revenue, and a 200-person team of technologists, operators, drivers, and warehouse staff.</div>
</div>

<div class="startup-entry">
<a href="https://techcrunch.com/2012/12/04/kicksend-target-cvs/" class="startup-logo"><img src="/images/logos/kicksend.png" alt="Kicksend"></a>
<div class="startup-text"><strong><a href="https://techcrunch.com/2012/12/04/kicksend-target-cvs/">Kicksend</a></strong> (YC S11) — Co-founded with <a href="https://x.com/brendanlim">Brendan Lim</a>. Photo prints delivered to your door. Featured on the <a href="https://www.today.com/video/today/52066329">Today Show</a>. Millions of users, millions in revenue, and partnerships with CVS, Target, Walgreens, Walmart. Acquired by Lyft.</div>
</div>

<div class="startup-entry">
<a href="https://www.lyft.com" class="startup-logo"><img src="/images/logos/lyft.png" alt="Lyft"></a>
<div class="startup-text"><strong>Lyft</strong> — Stayed on after acquisition. Driver growth, unlocking conversion in major markets.</div>
</div>

## OPEN SOURCE

<div class="startup-entry">
<a href="https://github.com/jo-inc/camofox-browser" class="startup-logo"><img src="/images/logos/camofox.png" alt="camofox-browser" class="logo-padded"></a>
<div class="startup-text"><strong><a href="https://github.com/jo-inc/camofox-browser">camofox-browser</a></strong> — Anti-detection headless browser for AI agents. Wraps <a href="https://camoufox.com">Camoufox</a> (Firefox fork with C++ fingerprint spoofing) in a REST API. Powers <a href="https://askjo.ai">jo</a>'s web browsing. <a href="/2026/02/10/camofox-browser-deep-dive.html">Blog post</a>.</div>
</div>

<div class="startup-entry">
<a href="https://github.com/skyfallsin/pi-mem" class="startup-logo"><img src="/images/logos/pi-mem.png" alt="pi-mem" class="logo-padded theme-img-light"><img src="/images/logos/pi-mem-dark.png" alt="pi-mem" class="logo-padded theme-img-dark"></a>
<div class="startup-text"><strong><a href="https://github.com/skyfallsin/pi-mem">pi-mem</a></strong> — Plain-Markdown memory for the <a href="https://pi.dev/">pi</a> coding agent. Long-term facts, daily logs, and a scratchpad — just files on disk injected into context. <a href="/2026/02/11/pi-mem.html">Blog post</a>.</div>
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
