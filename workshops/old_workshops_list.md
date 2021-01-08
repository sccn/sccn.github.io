---
layout: default
title: Old workshops
parent: Workshops
nav_order: 5
---
<h1>List of old workshops</h1>
{%- assign children_list = site.pages | where: "parent", "Workshops" | where: "nav_exclude", "true" -%}
{% include toc_nav.html nav=children_list %}
