---
layout: default
title: Plugins
has_children: true
has_toc: true
nav_order: 7
---
{%- assign children_list = site.pages | where: "parent", "Plugins" -%}
{% include toc_nav.html nav=children_list %}