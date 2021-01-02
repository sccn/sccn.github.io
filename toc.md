---
layout: default
title: Table of contents
nav_order: 4
---
<h1><a href="/tutorials">Tutorials</a></h1>
{%- assign children_list = site.pages | where: "parent", "Tutorials" -%}
{% include toc_nav.html nav=children_list %}
<h1><a href="/workshops">Workshops</a></h1>
{%- assign children_list = site.pages | where: "parent", "Workshops" -%}
{% include toc_nav.html nav=children_list %}
<h1><a href="/others">Other documents</a></h1>
{%- assign children_list = site.pages | where: "parent", "Other documents" -%}
{% include toc_nav.html nav=children_list %}
