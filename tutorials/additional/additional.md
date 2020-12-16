---
layout: default
title: z. additional
parent: Tutorials
has_children: true
has_toc: false
---

This section of the tutorial deals with rejecting artifacts

{% for page in site.pages %}
{% if page.categories contains "artifact"  %}
<li><a href="/{{ category }}/{{ page.title }}">{{ page.title }}</a></li>
{% endif %}
{% endfor %}