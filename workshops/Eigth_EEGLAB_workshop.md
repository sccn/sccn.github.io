---
layout: default
title: Eighth EEGLAB Workshop
permalink: /workshops/EEGLAB09ASPET.html
parent: Workshops
---

![300px\|thumb\|left]({{ site.baseurl }}/assets/images/Aspet.jpg)

Eighth EEGLAB Workshop
======================

<font color=blue>Aspet, France
June 7-10, 2009</font>



Material for download
---------------------

Please download the following programs

> [Latest EEGLAB development version (34
> Mb)](ftp://sccn.ucsd.edu/pub/eeglab6.1b.zip)
> [CORRMAP plugin (\< 1Mb)](https://sccn.ucsd.edu/githubwiki/files/Corrmap1.01.zip)> To install EEGLAB, follow [these
> instructions](/EEGLAB/I.Analyzing_Data_in_EEGLAB#Installing_EEGLAB_and_tutorial_files "wikilink").

Also download the following data and place all the in a dedicated folder

> [STUDY tutorial files Animal/non-animal task (630
> Mb)](ftp://sccn.ucsd.edu/pub/animal_study.zip)
> [STUDY tutorial files spatial attention task (650
> Mb)](ftp://sccn.ucsd.edu/pub/STUDY.zip)
> [Other tutorial Data sets (15 Mb)](https://sccn.ucsd.edu/githubwiki/files/Data.zip)
Tutorial scripts and questions

> [Tutorial scripts
> faces2.m](http://sccn.ucsd.edu/eeglab/workshop09/faces2.m)
> [Project questions](https://sccn.ucsd.edu/githubwiki/files/Projectquestions.pdf)
Soon... Group Research Questions

Relevant reading material:
--------------------------

EEGLAB graphic interface is built on top of the powerful Matlab
scripting language. Enjoying the full capabilities of EEGLAB for
building macro commands and performing custom and automated processing
requires the ability to manipulate EEGLAB data structures in Matlab.
Because of time constrains, we will NOT provide an introduction to the
Matlab language. Instead users need to familiarize themselves with
Matlab prior to the workshop. Users of Matlab 7: we recommend running
the following demos and reading the following help sections.

After opening the Matlab desktop, select menu item "Help Demos" and run
the following demos. Note that while the demo is running, you can retype
the text (or copy it) to the main Matlab window:



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

Each section or demo (if read thoroughly) should take you about 10
minutes, for a total here of about 2 hours. We encourage you to watch
these demos and read these sections over several days.

If you do not have access to the Matlab demos,
[here](http://sccn.ucsd.edu/eeglab/matlaboverview.html) is a short
online introduction to Matlab (recommended pages, 1 to 12)

*IMPORTANT NOTE:* A portion of the workshop will be dedicated to writing
EEGLAB scripts, so not being able to understand Matlab syntax will
result in you missing out on a large portion of the workshop.

*EEGLAB WIKI:* refer to the [EEGLAB wiki](/EEGLAB "wikilink") for
additional help.

Below are some seminal and important papers describing EEGLAB processing:
-------------------------------------------------------------------------

Delorme, A., Makeig, S. [EEGLAB: an open source toolbox for analysis of
single-trial EEG dynamics including independent component
analysis](https://sccn.ucsd.edu/githubwiki/files/Eeglab_published.pdf). J Neurosci Methods.2004; Mar 15; 134(1):9-21.

Makeig, S., Debener, S., Onton, J., Delorme, A. [Mining event-related
brain dynamics](https://sccn.ucsd.edu/githubwiki/files/Ticsreview_published.pdf). TrendsCogn Sci. 2004; May; 8(5):204-10.

Jung, TP, Makeig, S, Westerfield, M, Townsend, J, Courchesne, E,
Sejnowski, TJ. [Analysis and visualizaion of single-trial event-related
potentials](https://sccn.ucsd.edu/githubwiki/files/Jung_hbm01.pdf). Human Brain Mapping.2001; 14(3), 166-185.

Delorme, A., Sejnowski, T., Makeig, S. [Improved rejection of artifacts
from EEG data using high-order statistics and independent component
analysis](https://sccn.ucsd.edu/githubwiki/files/Neuroimage2007_reformated.pdf). Neuroimage.2007; 34, 1443-1449.

Delorme, A., Palmer, J. Oostenveld, R., Onton, J., Makeig, S. [Comparing
results of algorithms implementing blind source separation of EEG
data](https://sccn.ucsd.edu/githubwiki/files/Delorme_unpub.pdf). unpublished manuscript.
Onton J, Delorme, A., Makeig, S. [Frontal midline EEG dynamics during
working memory](https://sccn.ucsd.edu/githubwiki/files/Onton_fmtheta_published.pdf).NeuroImage. 2005;27, 341-356

Workshop Program (with corresponding PDFs)
------------------------------------------

<font color=purple>Purple lettering = lecture</font>
<font color=orange>Orange lettering = tutorial</font>

<u><font color=blue>Sunday, June 7</font></u>


16:00 -- train station shuttle pick up

16:30 -- shuttle aiport pick up

<font color = green>


19:00 -- diner (included in registration)</font>

<u><font color=blue>Monday, April 20</font></u>


<font color = green>7:00 - 8:00 Breakfast</font>

<!-- -->


**Overview and ICA Theory/Practice**

<font color = purple>



8:00 – 9:00 -- EEGLAB overview (Arnaud Delorme)
([PDF](https://sccn.ucsd.edu/githubwiki/files/Lecture_eeglaboverview2.pdf‎))
9:00 – 10:00 -- ICA theory (Arnaud Delorme)
([PDF](https://sccn.ucsd.edu/githubwiki/files/Lecture_ica.pdf))
</font>



<font color = green>-- Break--</font>


<font color = purple>10:20 – 11:00 -- Time-Frequency decomopositions
(Arnaud Delorme) ([PDF](https://sccn.ucsd.edu/githubwiki/files/Lecture_timefreq.pdf))</font>
<font color = orange>11:00 – 12:00 -- Time-Frequency practicum (Arnaud
Delorme) </font>

<!-- -->


<font color = green>12:00-13:30 Lunch --</font>

<!-- -->


**EEGLAB methods I – Data Preprocessing**

<font color=purple>



13:30 – 14:30 -- Mining event-related brain dynamics I (Scott
Makeig)</font>

<font color=orange>



14:30 – 15:30 -- Data import, Artifact rejection and running ICA (Filipa
Campo Viola)
[(PDF)](https://sccn.ucsd.edu/githubwiki/files/Practicum_1_data_import_artifreject.pdf)

<font color=green>-- Break –</font>

15:50 – 16:50 -- Evaluation of ICA components (Arnaud Delorme)
[(PDF)](https://sccn.ucsd.edu/githubwiki/files/Practicum_3_evaluateics2.pdf)
16:50 – 17:20 -- ICA automatic artifact detection plugin (Filipa Campo
Viola) [(PDF)](https://sccn.ucsd.edu/githubwiki/files/Automatic_detec_artifac_comps.pdf)
17:20 – 19:00 -- Data and workstation available

</font>


<font color = green>19:00 -- Dinner</font>

<u><font color=blue>Tuesday, June 9th</font></u>


<font color = green>7:00 - 8:00 Breakfast</font>

<!-- -->


**IC Analysis**


<font color = purple>8:00 – 9:00 -- Robust statistics (Robert
Oostenveld) ([PDF](https://sccn.ucsd.edu/githubwiki/files/Robust_statistics_aspet2009.pdf))
<font color=purple>9:00 – 10:00 -- Independent Component Clustering and
Study (Scott Makeig)
([PDF](https://sccn.ucsd.edu/githubwiki/files/Eeglab_aspet_clustering09.pdf))

<font color = green>-- Break--</font>

<font color = purple>10:20 – 11:20 -- Forward and inverse models (Robert
Oostenveld)
([PDF](https://sccn.ucsd.edu/githubwiki/files/Forward_and_inverse_models_aspet2009.pdf))</font>
<font color = orange>11:20 – 12:00 -- Basic scripting using EEGLAB
“history” (A.Delorme)</font>
[(PDF)](https://sccn.ucsd.edu/githubwiki/files/Practicum_4_basic_scripting.pdf)
<!-- -->


<font color=green>12:00-1:00 Lunch --</font>

<!-- -->


**EEGLAB methods II – Evaluating ICs**


<font color = orange>13:00 – 14:00 – Plotting and component clusterint
with studies (Arnaud
Delorme)</font>[(PDF)](https://sccn.ucsd.edu/githubwiki/files/Practicum_9_studyplotedit2.pdf)
<font color = orange>15:00 – 15:30 – Scripting with studies (Arnaud
Delorme) (included in previous PDF)</font>

<!-- -->


<font color = green>15:30-18:00-- Hiking in the pyrennees</font>

<!-- -->


<font color=green>19:00 -- Dinner --</font>

<u><font color=blue>Wednesday, June 10</font></u>


<font color=green>7:00-8:00 -- Breakfast</font>

<!-- -->



<font color=purple>8:00 – 9:00 -- Mining event-related brain dynamics II
(Scott Makeig)</font>

<font color=orange>9:00 – 9:20 -- EEGLAB plugins</font>
[(PDF)](https://sccn.ucsd.edu/githubwiki/files/Eeglab_plugins2.pdf)
<!-- -->



<font color=orange>9:20 – 11:30 -- Practicum, project available</font>

<font color=orange>11:30 – 12:00 -- Participant project presentation and
general discussion</font>

<!-- -->


<font color=green>12:00 -- Lunch</font>

<!-- -->


<font color=green>13:30 -- Airport/train station shuttle leaves</font>

[Category:Workshops](/Category:Workshops "wikilink")
