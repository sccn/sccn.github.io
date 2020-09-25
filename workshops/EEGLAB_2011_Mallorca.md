---
layout: default
title: EEGLAB 2011 Mallorca
permalink: /workshops/EEGLAB_2011_Mallorca.html
parent: Workshops
---

![300px\|thumb\|left\|upright=2]({{ site.baseurl }}/assets/images/Mallorca2.jpg)

Fourteenth EEGLAB Workshop
==========================



<font color=blue>[Mallorca](http://en.wikipedia.org/Mallorca), Spain,
Sept. 22-25, 2011 preceding
[ICON](http://www.icon11mallorca.org/)</font>

Overview
--------

The 14th EEGLAB Workshop took place from Thursday, September 22 through
Sunday, September 25, 2011 on the Spanish island of Mallorca preceding
ICON XI. Participants in the first two parts of the Workshop were
expected to bring laptops with Matlab installed so as to be able to
participate in the practical sessions. The workshops consisted of three
parts:


1\. On Thursday, Sept. 22 there was a full-day <b>Novice EEGLAB
Workshop</b> for those interested in learning the basics of using EEGLAB
and independent component analysis (ICA) to analyze their EEG (or
related) data.

<!-- -->


2\. Friday, Sept. 23 through noon on Sunday, Sept. 25, the first
<b>Advanced EEGLAB Workshop</b> introduced and demonstrate dthe use of
EEGLAB-linked tools for performing advanced analyses of EEG and related
data, with detailed method expositions and practical exercises.

<!-- -->


3\. Sunday afternoon, Sept. 25, there was a (free) <b>Open Discussion
Session</b> of evolving directions in EEG/ECoG research and free / open
source data analysis, collection, and archival software. All interested
were welcome to attend or participate in this discussion.

Costs and Registration
----------------------

To reimburse travel expenses of Workshop faculty and facilities rental,
costs for the workshop were as follows:



Part 1 - Novice EEGLAB Workshop (Sept. 22) 120€

Part 2 - Advanced EEGLAB Workshop (Sept. 23-25) 240€

Parts 1 & 2 - Novice & Advanced workshops (Sept. 22-25) 300€

Part 3 -- Open Discussion Session: Current directions in EEG research
and open source software (no charge)

<font color=red>Registration is currently <b>closed</b></font>.

Relevant preparation in Matlab
------------------------------

The EEGLAB graphic interface is built on and provides easy ways to use
the powerful Matlab scripting language. Exploiting the capabilities of
EEGLAB for building macro commands and performing custom and automated
processing requires the ability to manipulate EEGLAB data structures in
Matlab. Because of time constrains, we will NOT provide an introduction
to the Matlab language. Instead, users need to familiarize themselves
with Matlab prior to the workshop.

Users of Matlab 7: we recommend running the following demos and reading
the following help sections. After opening the Matlab desktop, select
menu item "Help Demos" and run the following demos. Note that while the
demo is running, you can retype the text (or copy it) to the main Matlab
window:



Mathematics - Basic Matrix Operations

Mathematics - Matrix manipulations

Graphics - 2-D Plots

Programming - Manipulating Multidimentional arrays

Programming - Structures

In the Help Content, read and practice at least the following sections:



Getting Started - Matrices and Arrays - Matrices and Magic squares

Getting Started - Matrices and Arrays - Expressions

Getting Started - Matrices and Arrays - Working with Matrices

Getting Started - Graphics - Basic plotting functions

Getting Started - Programming - Flow Control

Getting Started - Programming - Other data structures

Getting Started - Programming - Scripts and Functions

Each section or demo (if read thoroughly) should take about 10 minutes.
We encourage you to watch these demos and read these sections over
several days. If you do not have access to the Matlab demos,
[here](http://sccn.ucsd.edu/eeglab/matlaboverview.html) is a short
online introduction to Matlab (recommended pages, 1 to 12)

*IMPORTANT NOTE:* Advanced tools and methods require script writing to
perform analysis customized to your data and analysis goals. Script
writing in Matlab is simple; the workshops will assume that you know at
least the basics.

*EEGLAB WIKI:* refer to the [EEGLAB wiki](/EEGLAB "wikilink") for
additional help.

Some papers describing EEGLAB processing
----------------------------------------

Delorme, A., Makeig, S. [EEGLAB: an open source toolbox for analysis of
single-trial EEG dynamics including independent component
analysis]({{ site.baseurl }}/assets/pdfs/EEGLAB_published.pdf). J Neurosci Methods.2004; Mar 15; 134(1):9-21.

Makeig, S., Debener, S., Onton, J., Delorme, A. [Mining event-related
brain dynamics]({{ site.baseurl }}/assets/pdfs/TICSreview_published.pdf). TrendsCogn Sci. 2004; May; 8(5):204-10.

Jung, TP, Makeig, S, Westerfield, M, Townsend, J, Courchesne, E,
Sejnowski, TJ. [Analysis and visualizaion of single-trial event-related
potentials]({{ site.baseurl }}/assets/pdfs/Jung_HBM01.pdf). Human Brain Mapping.2001; 14(3), 166-185.

Delorme, A., Sejnowski, T., Makeig, S. [Improved rejection of artifacts
from EEG data using high-order statistics and independent component
analysis]({{ site.baseurl }}/assets/pdfs/neuroimage2007_reformated.pdf). Neuroimage.2007; 34, 1443-1449.

Delorme, A., Palmer, J. Oostenveld, R., Onton, J., Makeig, S. [Comparing
results of algorithms implementing blind source separation of EEG
data]({{ site.baseurl }}/assets/pdfs/delorme_unpub.pdf). unpublished manuscript.
Onton J, Delorme, A., Makeig, S. [Frontal midline EEG dynamics during
working memory]({{ site.baseurl }}/assets/pdfs/Onton_FMtheta_published.pdf).NeuroImage. 2005;27, 341-356

Workshop Agendas
----------------

Key: <font color = purple>Lecture</font>,
<font color = darkblue>Practicum</font>,
<font color = green>Break</font>

I. Novice EEGLAB Workshop -- Thursday, Sept. 22
-----------------------------------------------

This workshop is designed for researchers who would like to learn how to
process their EEG or related datasets using the ICA, time/frequency, and
other tools provided in the EEGLAB software environment for Matlab
(http://sccn.ucsd.edu/eeglab). The workshop instructor will be Julie
Onton, Ph.D., long-time EEGLAB user and SCCN laboratory member. Scott
Makeig, Director of the Swartz Center for Computational Neuroscience,
UCSD, and originator of EEGLAB methods will give an introductory talk on
evolving methods for analyzing EEG dynamics.

Novice workshop topics will include:
::• Data import and preprocessing options



• Basic independent component analysis (ICA) theory and application

• Methods for imaging IC activations (ERPs, time/frequency, coherence)

• Equivalent dipole source localization of independent components

• Introduction to Matlab scripting using EEGLAB structure

Note: Because of time limitations, the Novice workshop will NOT
include:
::• New, more advanced toolboxes (NFT, SIFT, BCILAB, MPT)



• Mathematical derivations of the algorithms discussed

These topics will be covered in the Advanced EEGLAB workshop (described
below).

<font color=blue><b>Program</b></font>


<font color = purple>08:30 -- 09:15am -- Mining event-related brain
dynamics (Scott
Makeig)[(PDF)]({{ site.baseurl }}/assets/pdfs/Makeig_EEGLAB_Mallorca_I.pdf)</font>
<!-- -->


<font color = red>09:15 -- 10:15am -- Introduction and getting started
with EEGLAB (Julie Onton)
[(PDF)]({{ site.baseurl }}/assets/pdfs/1_GettingStarted_EEGLAB.pdf)</font>


<font color = darkblue>Data import - Preprocessing tools and pipeline -
Running ICA decomposition </font>

<!-- -->


<font color = green>10:15 -- 10:30 BREAK</font>

<!-- -->


<font color = red>10:30 -- 11:15 -- Evaluating ICA components (ICs)
[(PDF)]({{ site.baseurl }}/assets/pdfs/2_EvaluatingICs.pdf)</font>


<font color = darkblue>Apply ICA weights - IC scalp map interpretation -
Basic IC evaluation - Identify artifact ICs</font>

<!-- -->


<font color = red>11:15 -- 12:15 -- IC analysis tools
[(PDF)]({{ site.baseurl }}/assets/pdfs/3_IC_Analysis_Tools.pdf)</font>


<font color = darkblue>Removing ICs and back-projection - IC ERP
envelope - IC ERP images - Time-frequency analysis - IC Event-related
spectral perturbations (ERSPs) - IC Cross coherence</font>

<!-- -->


<font color = green>12:15 -- 13:30 LUNCH</font>

<!-- -->


<font color = red>13:30 -- 14:30 -- EEGLAB 'EEG' structure and basic
Matlab scripting [(PDF)]({{ site.baseurl }}/assets/pdfs/4_Basic_Scripting.pdf)</font>


<font color = darkblue>‘EEG’ structure overview - ‘EEG’ structure
overview - Search EEG.event structure - Matlab functions - Converting
from ‘pop’ functions to output functions</font>

<!-- -->


<font color = red>14:30 -- 15:15 – Equivalent dipole modeling
[(PDF)]({{ site.baseurl }}/assets/pdfs/5_DipoleModeling.pdf)</font>


<font color = darkblue>Co-registration of electrodes with head model -
Dipole fitting using Fieldtrip's dipfit function - Co-registration for
3D headplots</font>

<!-- -->


<font color = green>15:15 -- 15:30 BREAK</font>

<!-- -->


<font color = red>15:30 -- 16:30 -- Introduction to EEGLAB STUDY
structure [(PDF)]({{ site.baseurl }}/assets/pdfs/6_STUDY_Intro.pdf)</font>


<font color = darkblue>Build a STUDY - Precompute, precluster, and
cluster ICs across subjects - Plot and edit STUDY clusters</font>

<!-- -->


<font color = red>15:30 -- 17:30 -- Advanced STUDY scripting
[(PDF)]({{ site.baseurl }}/assets/pdfs/7_STUDY_Scripting.pdf)</font>


<font color = darkblue>Build a STUDY from the command line - STUDY
structure overview - Cluster ERP image - Accessing raw STUDY data
measures</font>

<hr>

II. Advanced EEGLAB Workshop -- Friday-Sunday, Sept. 23-25
----------------------------------------------------------

This 2.5-day workshop will focus on emerging computational methods for
EEG/ECoG analysis that have recently been made available within the
EEGLAB environment as plug-in toolboxes. The lectures and practica will
be more technically advanced than previous EEGLAB workshops.
Participants will be expected to have at least passing familiarity with
concepts such as linear regression, matrix inversion and other basic
linear algebraic operations, Fourier transforms, and basic probability
theory.

In addition, participants should be comfortable with using Matlab
including performing the following operations using EEGLAB:
::• Performing ICA decompositions and evaluating ICA component



• Obtaining equivalent dipole models of independent components using
DIPFIT

• Performing time-frequency transforms and coherence analysis in EEGLAB

• Building an EEGLAB data STUDY

Interested participants who do not have the above background are
strongly encouraged to study the relevant parts of the extensive
<b>Online EEGLAB Tutorial</b>(http://sccn.ucsd.edu/wiki/EEGLAB), to go
through the relevant video/slide lectures and practica in the <b>Online
EEGLAB Workshop</b> (http://sccn.ucsd.edu/wiki/Online_EEGLAB_Workshop),
and to consider attending the <b>Novice EEGLAB Workshop</b> (described
above).

Advanced workshop topics will include:
::• Applying adaptive-mixture ICA (Amica) to non-stationary EEG source
dynamics



• Using Measure Projection analysis of multi-subject ICA-resolved EEG
dynamics

• Applying statistical machine learning to EEG data analysis and
Brain-Computer Interface design

• Analysis of oscillatory source network dynamics including Granger
causality

• Forward and inverse modeling for EEG/ECoG source localization

Participants are expected to bring a laptop with Matlab and EEGLAB
installed to work on (detailed instructions will be sent out before the
workshop). Pairs of participants may also choose to share a laptop.

<font color = blue><b>Preliminary Program -- Friday, Sept. 23</b></font>


<font color = purple>08:30 – 09:00 -- Welcome, introductions and brief
overview (Scott Makeig)</font>

<!-- -->


<b>Session A – Adaptive mixture independent component analysis (AMICA)
decomposition (Jason Palmer)</b>

<!-- -->



This session will motivate, derive simply, and demonstrate the Adaptive
Mixture ICA (Amica) algorithm of (Palmer et al., 2007) that finds more
physiologically interpretable component processes in high-density EEG
(or related) data and, further, detects and models changes in the
spatial EEG source structure. Use of a set of tools and measures for
interpreting the results of Amica decomposition will be demonstrated.

<!-- -->



<font color = purple>09:00 -- 09:45 ICA methods overview, with
motivation for and derivation of Amica
[(PDF)]({{ site.baseurl }}/assets/pdfs/ICA_Mallorca.pdf)</font>
<font color = darkblue>09:45 -- 10:45 Amica toolbox practicum</font>


Please see wiki pages:

[Linear_Representations_and_Basis_Vectors](/Linear_Representations_and_Basis_Vectors "wikilink")

[Random_Variables_and_Probability_Density_Functions](/Random_Variables_and_Probability_Density_Functions "wikilink")

[Amica](/Amica "wikilink")

[Amica_Download](/Amica_Download "wikilink")

<!-- -->



<font color = green>10:45 -- 11:00 BREAK</font>

<!-- -->


<b>Session B -- Improving EEG source estimation using the
Neuroelectromagnetic Forward Head Modeling Toolbox (NFT) (Zeynep Akalin
Acar)</b>

<!-- -->



This session will give an overview of the forward head modeling problem
and its approaches, followed by a demonstration of using NFT tools
(http://sccn.ucsd.edu/wiki/NFT) to derive forward head models from
subject MR images and/or recorded electrode positions, and using such
models to estimate source locations.

<!-- -->



[Both PDFs, supplementary functions and data for
NFT](ftp://sccn.ucsd.edu/pub/julie/extra2.zip)

[Supplementary functions and data ONLY, for
practicum](ftp://sccn.ucsd.edu/pub/julie/extra.zip)

<!-- -->



<font color = purple>11:00 -- 12:00 -- Forward head modeling
overview[(PDF)]({{ site.baseurl }}/assets/pdfs/Akalin_Acar_Forward_Problem_of_EEG.pdf)</font>
<!-- -->



<font color = green>12:00 -- 13:30 LUNCH</font>

<!-- -->



<font color = darkblue>13:30 -- 14:30 -- NFT head modeling toolbox
practicum[(PDF)]({{ site.baseurl }}/assets/pdfs/Akalin_Acar_NFT_practicum.pdf)</font>
<!-- -->


<b>Session C -- Comparing EEG dynamics across subjects using the Measure
Projection Analysis (MPA) toolbox (Nima Bigdely Shamlo)</b>

<!-- -->



This session will address multi-subject EEG source analysis and will
introduce a novel probabilistic method, Measure Projection Analysis
(MPA, [wiki is located here](http://sccn.ucsd.edu/wiki/MPT)), to study
and visualize the consistency of independent component localization and
activities across subjects, groups, and/or conditions.

<!-- -->



<font color = purple>14:30 – 15:30 – Measure projection analysis theory
[(PDF)]({{ site.baseurl }}/assets/pdfs/Measure_Projection_EEGLAB_11_Mallorca.pdf)</font>
<!-- -->



<font color = green>15:30 -- 15:45 BREAK</font>

<!-- -->



<font color = darkblue>15:45 -- 17:30 -- Measure projection analysis
practicum
[(PDF)]({{ site.baseurl }}/assets/pdfs/Practicum_of_Measure_Projection_EEGLAB_11_Mallorca.pdf)</font>
<font color = blue><b>Preliminary Program -- Saturday, Sept.
24</b></font>


<b>Session D -- Analyzing oscillatory EEG/ECoG source dynamics and
interactions using the Source Information Flow Toolbox (SIFT) (Tim
Mullen)</b>

<!-- -->



This session will survey contemporary computational approaches for
analyzing oscillatory dynamics and synchronization/information flow in
electrophysiological data. Topics will include the basic theory and
practical issues surrounding estimation of Granger causality, Partial
Directed Coherence and related information flow measures, phase-locking
value, and phase-amplitude coupling. Participants will gain hands-on
expertise in modeling and visualizing effective connectivity and
synchronization between quasi-independent sources of EEG activity using
the Source Information Flow Toolbox (SIFT)
(http://sccn.ucsd.edu/wiki/SIFT).

<!-- -->



<font color = purple>8:30 -- 10:00 am -- Analyzing Oscillatory Dynamics
and Effective Connectivity
[(PDF)]({{ site.baseurl }}/assets/pdfs/EEGLAB_ICON_Mullen_SIFT.pdf)


Phase-amplitude coupling

Phase-locking value

Adaptive vector autoregressive models

Granger-causality, Partial Directed Coherence

Directed Transfer Functions, and related effective connectivity
measures</font>

<!-- -->



<font color = green>10:00 -- 10:30 BREAK</font>

<!-- -->



<font color = darkblue>10:30 --12:00 -- Using the Source Information
Flow Toolbox: practicum [\|
(PDF)](http://sccn.ucsd.edu/mediawiki/images/d/d2/SIFT_manual_0.1a.pdf)



Getting started with SIFT

Vector Autoregressive Model Fitting and Validation

Connectivity Analysis (Granger Causality, Partial Coherence, Directed
Transfer)

Computing reliability of network activity

Visualizing source connectivity across time, frequency and space

Group analysis using causal projection and other techniques</font>

<!-- -->



<font color = green>12:00 -- 13:30 LUNCH</font>

<!-- -->


<b>Session E -- Statistical Learning Theory and Brain-Machine Interface
Design (Christian Kothe)</b>

<!-- -->



This session will introduce the research areas of Brain-Computer
Interface (or brain-machine interface) design and cognitive monitoring.
Central concepts and challenges will be reviewed, and a selection of
existing and emerging computational approaches will be examined. The
presentation will focus on the use of oscillatory processes, with less
focus on ERP-like phenomena. An introduction to creating BCILAB scripts
and extensions will be included. In the practicum, participants will
gain hands-on experience in designing, constructing, evaluating,
visualizing and running BCI models using the open-source BCILAB software
(http://sccn.ucsd.edu/wiki/BCILAB).

<!-- -->



[Slides from Christian's
lecture.](ftp://sccn.ucsd.edu/pub/bcilab/mallorca/Workshop2011-Theory.pdf)

<!-- -->



<font color = purple>13:30 -- 15:00 -- Statistical machine learning and
Brain-Computer Interface design



Construction, learning and testing of predictive models (signal
processing, machine learning, cross-validation)

Spatial filters for spectral BCI measures (CSP, ICA, DAL)

Capturing spectral structure (DFT, time-frequency representations)

Complexity control and regularization (sparsity norms, priors, nested
cross-val)

Imposing prior knowledge in space, time and frequency (Talairach,
DIPFIT, etc.)

Scaling to large / heterogenous data sources (across sessions, subjects,
and/or task conditions).</font>

<!-- -->



<font color = green>115:00 -- 15:30 BREAK</font>

<!-- -->



<font color = darkblue>15:30 -- 17:30 -- Using BCILAB to design and run
BCI, cognitive monitoring, and neurofeedback experiments / applications
[(Download the PDF slide
instructions)]({{ site.baseurl }}/assets/pdfs/Workshop_2011_-_Practicum.pdf‎)


Getting started with BCILAB

Learning, evaluating and visualizing spectral models: from simple to
advanced

Offline and online data processing

BCILAB scripting, customization, and plug-in authoring</font>

<font color = blue><b>Preliminary Program -- Sunday, Sept. 25</b></font>


<b>Session F - Workshop Review, Results, and Discussion</b>

<!-- -->



<font color = purple>09:00 -- 10:00 -- EEG Research: Current and Future
Directions (Scott Makeig)</font>

<!-- -->



<font color = darkblue>10:00 -- 10:30 -- Group practica results
preparation</font>

<!-- -->



<font color = green>10:30 -- 10:45 BREAK</font>

<!-- -->



<font color = darkblue>10:45 -- 12:00 -- Group practica results
presentations and general discussion</font>

<hr>

III. EEGLAB Workshop Open Discussion Session -- Sunday, Sept. 25, 13:30 - 16:30
-------------------------------------------------------------------------------

This will be a topic-focused discussion bringing together EEGLAB tool
developers, advanced users, and computationally-inclined members of the
cognitive neuroscience community as well as others interested to discuss
the current state and future development of open-source EEG/ECoG
analysis software within or connecting to the EEGLAB framework. This
discussion will be open to all ICON participants -- any and all are
welcome to attend and participate.

<font color = red> This discussion will take place at the Hotel Palas
Atenea (second floor hall, by the pool) </font>


<font color = purple>13:30-16:30 -- Evolving Methods and Tools for
EEG/ECoG Research (preliminary agenda)</font>

<font color = purple>



<font color=darkblue>1. Introduction -- Framing remarks and EEGLAB
overview (Scott Makeig)</font>



Designed EEGLAB uses and architecture

Use of the Matlab platform

Extending the EEGLAB plug-in mechanism

Building an online user community and collaborative network

Bridging to other open source tools and data collection systems

Multimodal data collection software -- ERICA and other efforts

Data and tools archive development -- HeadIT and other efforts

<!-- -->



<font color=darkblue>2. Advanced EEGLAB-compatible tools and directions
(Panel)</font>



Spatial source decomposition tools (Jason Palmer & TBN)

Forward and inverse head modeling tools (TBN)

Subject group analysis tools (Nima Bigdeley Shamlo)

Oscillatory dynamics analysis tools (Tim Mullen & TBN)

Information flow, synchronization, and causal network tools (Tim Mullen)

Brain-computer interface tools and directions (Christian Kothe)

</font>

<hr>

Survey
------

Please help us by answering [workshop survey
questions](http://www.surveymonkey.com/s/5CMLJFH)

[Category:Workshops](/Category:Workshops "wikilink")