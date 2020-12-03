---
layout: default
title: EEGLAB 2011 Mallorca
permalink: /workshops/EEGLAB_2011_Mallorca.html
nav_exclude: true
---

![300px\|thumb\|left\|upright=2]({{ site.baseurl }}/assets/images/Mallorca2.jpg)

Fourteenth EEGLAB Workshop
==========================



[Mallorca](http://en.wikipedia.org/Mallorca), Spain, Sept. 22-25, 2011 preceding
[ICON](http://www.icon11mallorca.org/)

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




2\. Friday, Sept. 23 through noon on Sunday, Sept. 25, the first
<b>Advanced EEGLAB Workshop</b> introduced and demonstrate dthe use of
EEGLAB-linked tools for performing advanced analyses of EEG and related
data, with detailed method expositions and practical exercises.




3\. Sunday afternoon, Sept. 25, there was a (free) <b>Open Discussion
Session</b> of evolving directions in EEG/ECoG research and free / open
source data analysis, collection, and archival software. All interested
were welcome to attend or participate in this discussion.


Workshop Agendas
----------------

Key: <span style="color: purple">Lecture</span>,
<span style="color: darkblue">Practicum</span>,
<span style="color: green">Break</span>

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
• Data import and preprocessing options

• Basic independent component analysis (ICA) theory and application

• Methods for imaging IC activations (ERPs, time/frequency, coherence)

• Equivalent dipole source localization of independent components

• Introduction to Matlab scripting using EEGLAB structure

Note: Because of time limitations, the Novice workshop will NOT
include:
• New, more advanced toolboxes (NFT, SIFT, BCILAB, MPT)

• Mathematical derivations of the algorithms discussed

These topics will be covered in the Advanced EEGLAB workshop (described
below).

<span style="color: blue><b>Program</b"></span>

<span style="color: purple">08:30 -- 09:15am -- Mining event-related brain dynamics (Scott Makeig) [(PDF)](https://sccn.ucsd.edu/githubwiki/files/makeig_eeglab_mallorca_i.pdf)</span>
<!-- -->


<span style="color: red">09:15 -- 10:15am -- Introduction and getting started with EEGLAB (Julie Onton) [(PDF)](https://sccn.ucsd.edu/githubwiki/files/1_gettingstarted_eeglab.pdf)</span>


<span style="color: darkblue">Data import - Preprocessing tools and pipeline - Running ICA decomposition </span>

<!-- -->


<span style="color: green">10:15 -- 10:30 BREAK</span>

<!-- -->


<span style="color: red">10:30 -- 11:15 -- Evaluating ICA components (ICs) [(PDF)](https://sccn.ucsd.edu/githubwiki/files/2_evaluatingics.pdf)</span>


<span style="color: darkblue">Apply ICA weights - IC scalp map interpretation - Basic IC evaluation - Identify artifact ICs</span>

<!-- -->


<span style="color: red">11:15 -- 12:15 -- IC analysis tools [(PDF)](https://sccn.ucsd.edu/githubwiki/files/3_ic_analysis_tools.pdf)</span>


<span style="color: darkblue">Removing ICs and back-projection - IC ERP envelope - IC ERP images - Time-frequency analysis - IC Event-related spectral perturbations (ERSPs) - IC Cross coherence</span>

<!-- -->


<span style="color: green">12:15 -- 13:30 LUNCH</span>

<!-- -->


<span style="color: red">13:30 -- 14:30 -- EEGLAB 'EEG' structure and basic Matlab scripting [(PDF)](https://sccn.ucsd.edu/githubwiki/files/4_basic_scripting.pdf)</span>


<span style="color: darkblue">‘EEG’ structure overview - ‘EEG’ structure overview - Search EEG.event structure - Matlab functions - Converting from ‘pop’ functions to output functions</span>

<!-- -->


<span style="color: red">14:30 -- 15:15 – Equivalent dipole modeling [(PDF)](https://sccn.ucsd.edu/githubwiki/files/5_dipolemodeling.pdf)</span>


<span style="color: darkblue">Co-registration of electrodes with head model - Dipole fitting using Fieldtrip's dipfit function - Co-registration for 3D headplots</span>

<!-- -->


<span style="color: green">15:15 -- 15:30 BREAK</span>

<!-- -->


<span style="color: red">15:30 -- 16:30 -- Introduction to EEGLAB STUDY structure [(PDF)](https://sccn.ucsd.edu/githubwiki/files/6_study_intro.pdf)</span>


<span style="color: darkblue">Build a STUDY - Precompute, precluster, and cluster ICs across subjects - Plot and edit STUDY clusters</span>

<!-- -->


<span style="color: red">15:30 -- 17:30 -- Advanced STUDY scripting [(PDF)](https://sccn.ucsd.edu/githubwiki/files/7_study_scripting.pdf)</span>


<span style="color: darkblue">Build a STUDY from the command line - STUDY structure overview - Cluster ERP image - Accessing raw STUDY data measures</span>

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
• Performing ICA decompositions and evaluating ICA component

• Obtaining equivalent dipole models of independent components using
DIPFIT

• Performing time-frequency transforms and coherence analysis in EEGLAB

• Building an EEGLAB data STUDY

Advanced workshop topics will include:
• Applying adaptive-mixture ICA (Amica) to non-stationary EEG source
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

<span style="color: blue><b>Preliminary Program -- Friday, Sept. 23</b"></span>


<span style="color: purple">08:30 – 09:00 -- Welcome, introductions and brief overview (Scott Makeig)</span>

<!-- -->


<b>Session A – Adaptive mixture independent component analysis (AMICA) decomposition (Jason Palmer)</b>

<!-- -->



This session will motivate, derive simply, and demonstrate the Adaptive
Mixture ICA (Amica) algorithm of (Palmer et al., 2007) that finds more
physiologically interpretable component processes in high-density EEG
(or related) data and, further, detects and models changes in the
spatial EEG source structure. Use of a set of tools and measures for
interpreting the results of Amica decomposition will be demonstrated.

<!-- -->



<span style="color: purple">09:00 -- 09:45 ICA methods overview, with motivation for and derivation of Amica [(PDF)](https://sccn.ucsd.edu/githubwiki/files/ica_mallorca.pdf)</span>

<span style="color: darkblue">09:45 -- 10:45 Amica toolbox practicum</span>


<span style="color: green">10:45 -- 11:00 BREAK</span>

<!-- -->


<b>Session B -- Improving EEG source estimation using the Neuroelectromagnetic Forward Head Modeling Toolbox (NFT) (Zeynep Akalin Acar)</b>

<!-- -->



<!-- -->



[Both PDFs, supplementary functions and data for
NFT](ftp://sccn.ucsd.edu/pub/julie/extra2.zip)

[Supplementary functions and data ONLY, for
practicum](ftp://sccn.ucsd.edu/pub/julie/extra.zip)

<!-- -->



<span style="color: purple">11:00 -- 12:00 -- Forward head modeling overview [(PDF)](https://sccn.ucsd.edu/githubwiki/files/akalin_acar_forward_problem_of_eeg.pdf)</span>
<!-- -->



<span style="color: green">12:00 -- 13:30 LUNCH</span>

<!-- -->



<span style="color: darkblue">13:30 -- 14:30 -- NFT head modeling toolbox practicum [(PDF)](https://sccn.ucsd.edu/githubwiki/files/akalin_acar_nft_practicum.pdf)</span>
<!-- -->


<b>Session C -- Comparing EEG dynamics across subjects using the Measure Projection Analysis (MPA) toolbox (Nima Bigdely Shamlo)</b>

<!-- -->


<!-- -->



<span style="color: purple">14:30 – 15:30 – Measure projection analysis theory [(PDF)](https://sccn.ucsd.edu/githubwiki/files/measure_projection_eeglab_11_mallorca.pdf)</span>
<!-- -->



<span style="color: green">15:30 -- 15:45 BREAK</span>

<!-- -->



<span style="color: darkblue">15:45 -- 17:30 -- Measure projection analysis practicum [(PDF)](https://sccn.ucsd.edu/githubwiki/files/practicum_of_measure_projection_eeglab_11_mallorca.pdf)</span>

<span style="color: blue><b>Preliminary Program -- Saturday, Sept.24</b"></span>


<b>Session D -- Analyzing oscillatory EEG/ECoG source dynamics and interactions using the Source Information Flow Toolbox (SIFT) (Tim Mullen)</b>


<span style="color: purple">8:30 -- 10:00 am -- Analyzing Oscillatory Dynamics and Effective Connectivity </span> [(PDF)](https://sccn.ucsd.edu/githubwiki/files/eeglab_icon_mullen_sift.pdf)



<span style="color: green">10:00 -- 10:30 BREAK</span>

<!-- -->



<span style="color: darkblue">10:30 --12:00 -- Using the Source Information Flow Toolbox: practicum</span> [(PDF)](http://sccn.ucsd.edu/mediawiki/images/d/d2/SIFT_manual_0.1a.pdf)






<span style="color: green">12:00 -- 13:30 LUNCH</span>

<!-- -->


<b>Session E -- Statistical Learning Theory and Brain-Machine Interface Design (Christian Kothe)</b>

<!-- -->



<!-- -->



[Slides from Christian's lecture.](ftp://sccn.ucsd.edu/pub/bcilab/mallorca/Workshop2011-Theory.pdf)

<!-- -->



<span style="color: purple">13:30 -- 15:00 -- Statistical machine learning and Brain-Computer Interface design </span>



<span style="color: green">115:00 -- 15:30 BREAK</span>

<!-- -->



<span style="color: darkblue">15:30 -- 17:30 -- Using BCILAB to design and run BCI, cognitive monitoring, and neurofeedback experiments / applications </span> [(PDF)](https://sccn.ucsd.edu/githubwiki/files/workshop_2011_-_practicum.pdf)



<span style="color: blue><b>Preliminary Program -- Sunday, Sept. 25</b></span>


<b>Session F - Workshop Review, Results, and Discussion</b>

<!-- -->



<span style="color: purple">09:00 -- 10:00 -- EEG Research: Current and Future Directions (Scott Makeig)</span>

<!-- -->



<span style="color: darkblue">10:00 -- 10:30 -- Group practica results preparation</span>

<!-- -->



<span style="color: green">10:30 -- 10:45 BREAK</span>

<!-- -->



<span style="color: darkblue">10:45 -- 12:00 -- Group practica results presentations and general discussion</span>

III. EEGLAB Workshop Open Discussion Session -- Sunday, Sept. 25, 13:30 - 16:30
-------------------------------------------------------------------------------


<span style="color: purple">13:30-16:30 -- Evolving Methods and Tools for EEG/ECoG Research (preliminary agenda)</span>




<span style="color: darkblue">1. Introduction -- Framing remarks and EEGLAB overview (Scott Makeig)</span>






<span style="color: darkblue">2. Advanced EEGLAB-compatible tools and directions (Panel)</span>


