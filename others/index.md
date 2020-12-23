---
layout: default
title: Other documents
has_children: true
has_toc: true
---
{% raw %}
~~~html
<ul>
{% for tag in site.tags %}
  {% assign name = tag | first %}
  {% assign posts = tag | last %}
  <li>{{ name | camelize | replace: "-", " " }} has {{posts | size}} posts</li>
{% endfor %}
</ul>
~~~
{% endraw %}
