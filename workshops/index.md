---
layout: default
title: Workshops
has_children: true
has_toc: false
nav_order: 4
---
![Mugs from the 17th EEGLAB workshop](/assets/images/EEGLAB-mug-shot.png)
# EEGLAB Workshops

## Current workshops
- [<b>The Online EEGLAB Workshop</b>](/workshops/Online_EEGLAB_Workshop) - Includes online videos, slides, and tutorial materials!
- [Future EEGLAB Workshops](/workshops/Future_workshops.html)

<h2>List of past EEGLAB workshops</h2>
{%- assign children_list = site.pages | where: "parent", "Past workshops" -%}
{% include toc_nav.html nav=children_list %}
