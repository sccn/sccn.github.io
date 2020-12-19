---
layout: default
title: 10. Group analysis
parent: Tutorials
has_children: true
has_toc: false
nav_order: 10
---

Multiple Subject processing
===============================
In this tutorial, the user is introduced to more advanced elements of EEGLAB focused around the STUDY
framework used for processing multiple subjects as once. These topics
are recommended for the user to successfully analyse large scale
experiments which go beyond single subject. 

In addition to the tutorial sections below, you may want to watch this short video on multiple subjects processing
 in EEGLAB (hosted on Youtube):

<a href="https://www.youtube.com/watch?v=kofJh7biGsE"><img align="center" width="400" height="400" src= "{{ site.baseurl }}/assets/images/yt_multiple_subjects.png"></a>

The most common steps you might take for group analysis of channel data and of ICA component are outlined here:

### Start by getting all your datasets within a STUDY data structure:

- [Create a STUDY](/tutorials/multi-subject/study-creation.html)
- [Specify your STUDY data analysis design](/tutorials/multi-subject/working-with-STUDY-designs.html)

### Then if you want to work on channel data:

- [Pre-compute channel data measures](/tutorials/multi-subject/STUDY-data-visualization-tools.html#precomputing-channel-measures)

### And if you want to work on the ICA component level:

- [Identify the components in each dataset to
    cluster](/tutorials/multi-subject/component-clustering-tools.html#Clustering_Methods "wikilink").
- [Specify and compute ("pre-clustering") measures to use in
    clustering](/tutorials/multi-subject/component-clustering-tools.html#Clustering_Methods "wikilink").
- [Perform component clustering using these
    measures](/tutorials/multi-subject/component-clustering-tools.html#Clustering_Methods "wikilink").
    
### Visualizing measures for either channel or component data:

- [View the scalp maps, dipole models, and activity measures of the
    component
    clusters](/tutorials/multi-subject/component-clustering-tools.html#Editing_clusters "wikilink").

### Finally perform statistical estimation on either channel data or components:
- [Perform signal processing and statistical estimation on the
    clusters](/tutorials/multi-subject/study-statistics-and-visualization-options.html).



