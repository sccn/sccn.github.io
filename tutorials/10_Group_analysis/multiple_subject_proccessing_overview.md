---
layout: default
title: a. Overview
parent: 10. Group analysis
grand_parent: Tutorials 
---

Multiple subject processing in EEGLAB - An Overview
=====================================================

This tutorial describes how to use the STUDY structure to manage and process data recorded from multiple subjects,
sessions, and/or conditions of an experimental study. 

EEGLAB uses studysets for performing statistical comparisons, for automated serial
(and in future parallel) computation, and for clustering of independent
signal components across subjects and sessions. It details the use of the 
set of EEGLAB component clustering functions that allow
exploratory definition and visualization of clusters of equivalent or
similar ICA data components across any number of subjects, subject
groups, experimental conditions, and/or sessions. 

Clustering functions
may be used to assess the consistency of ICA (or, other linearly
filtered) decompositions across subjects and conditions, and to evaluate
the separate contributions of identified clusters of these data
components to the recorded EEG dynamics.

EEGLAB STUDY structures and studysets:
---------------------------------------
EEGLAB v5.0 introduced a new basic concept and data structure, the
*STUDY*. 

Each *STUDY*, saved on disk as a *studyset* (*.std*) file, is a
structure containing a set of epoched *EEG* datasets from one or more
subjects, in one or more groups, recorded in one or more sessions, in
one or more task conditions -- plus additional (e.g., component
clustering) information. 

*STUDY* structures
and studysets are primary EEGLAB data processing objects. Operations carried out from the EEGLAB menu or the Matlab
command line on datasets are equally applicable to studysets
comprising any number of datasets.

### Use of STUDY structures to process single-trial channel data

EEGLAB studysets may be used to compute ERPs, spectrum,
ERSP and other measures onto single-trial channel data across dozens or
even hundreds of subjects. 

Missing data channels may be replaced if
necessary using spherical interpolation. 

Parametric or bootstrap
statistics may be used with correction for multiple comparisons to
compare a given measure in any n x m design. The channel data may also
be used to compute ICA component projections (see below).


Use of STUDY structures to cluster ICA components
----------------------------------

EEGLAB studysets may be used to cluster similar independent components
from multiple sessions and to evaluate the results of clustering. 

As ICA
component clustering is a powerful tool for electrophysiological data
analysis, and a necessary tool for applying ICA to experimental studies
involving planned comparisons between conditions, sessions, and/or
subject groups, the *STUDY* concept has been applied first to
independent component clustering. 

A small *studyset* of five datasets,
released with EEGLAB v5.0b for tutorial use and available
[here](ftp://sccn.ucsd.edu/pub/5subjects_reduced.zip), has been used to
create the example screens in this tutorial. 

We recommend that after following the
tutorial using this small example studyset, users next explore component
clustering by forming EEGLAB studies for one or more of their existing
experimental studies testing the component clustering functions more
fully on data they know well by repeating the steps outlined in the tutorial.

Upgrades to several standard EEGLAB plotting functions also allow them
to be applied simultaneously to whole studysets (either sequentially or
in parallel) rather than to single datasets, for example allowing users
to plot grand average channel data measures (ERPs, channel spectra,
etc.) across multiple subjects, sessions, and/or conditions from the
EEGLAB menu.

The dataset information contained in a *STUDY* structure allows
straightforward statistical comparisons of component activities and/or
source models for a variety of experimental designs. Currently, only a
few two-condition comparisons are directly supported. 

Currently we are
writing Matlab functions that will process information in more general
*STUDY* structures and the *EEG* data structures they contain,
potentially applying several types of statistical comparison (ANOVA,
permutation-based, etc.) to many types of data measures.

### Matlab toolboxes required for component clustering:

At the moment, two clustering methods are available: 'kmeans' and 'neural
network' clustering. 'Kmeans' clustering requires the Matlab Statistical
Toolbox, while 'neural network' clustering uses a function from the
Matlab Neural Network Toolbox. 

To learn whether these toolboxes are
installed, type *\>\> help* on the Matlab command line and see if the
line *toolbox/stats - Statistical toolbox* and/or the line *nnet/nnet -
Neural Network toolbox* are present. In future, we plan to explore the
possibility of providing alternate algorithms that do not require these
toolboxes, as well as options to cluster components using other methods.

This tutorial assumes that readers are already familiar with the
material covered in the [single subject EEGLAB tutorial](/tutorials/single-subject) and
also (for the later part of this chapter) in the [EEGLAB script writing tutorial](/tutorials/advanced-topics/writing-EEGLAB-scripts.html).

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



