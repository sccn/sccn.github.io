---
layout: default
title: EEGLAB and MEG data
parent: Reference Topics
grand_parent: Tutorials
---
EEGLAB and MEG data <span style="color: green"> - Done</span>
====================

EEGLAB supports reading most MEG data formats through the File-IO
module. Therefore all the major manufacturers may be imported (CTF,
Neuromag, Neuroimaging 4-D, BTi). There is also the native *ctfimport* EEGLAB plugin to import CTF data.

MEG data may be processed as EEG data, although there is added complexity
for some data formats. For example, EEGLAB does not differentiate
between gradiometers and magnetometers for Neuromag data. For
plotting purposes, you have to tweak the topoplot function to plot
either one or the other.

Also, EEGLAB does not support MEG gradient correction, so you need
to do that outside of EEGLAB before processing the MEG data in EEGLAB.

For MEG source localization, you can use a custom model in DIPFIT within
EEGLAB (there is a specific entry for MEG custom leadfield matrix as explained [here](/tutorials/09_source/DIPFIT.html#using-dipfit-to-fit-independent-meg-components)). EEGLAB is still a solution of choice if you are using
Independent Component Analysis to extract brain sources from MEG data.

However, EEGLAB is not primarily designed to process MEG data and
perform MEG source localization. For advanced MEG source processing that
does not involve ICA, a large number of MEG users directly use MEG
specialized software. For MEG source localization, some of the most
popular tools include Fieldtrip, Brainstorm, MEG-tools, MEGSIM, NUTMEG,
OpenMEG, MNE suite, or Curry. Some of the links on the popular NITRC
platform are listed shown

-   <http://www.nitrc.org/projects/fieldtrip>
-   <http://www.nitrc.org/projects/cuda_sphere_fwd>
-   <http://www.nitrc.org/projects/bst>
-   <http://www.nitrc.org/projects/openmeeg>
-   <http://www.nitrc.org/projects/meg-tools>
-   <http://www.nitrc.org/projects/megsim>