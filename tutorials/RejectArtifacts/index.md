---
layout: default
title: 6. Reject artifacts
parent: Tutorials
has_children: true
---
This section of the tutorial contains the following sub-sections:

{% for page in site.pages %}
{% if page.categories contains "preproc"  %}
<li><a href="/{{ category }}/{{ page.title }}">{{ page.title }}</a></li>
{% endif %}
{% endfor %}
