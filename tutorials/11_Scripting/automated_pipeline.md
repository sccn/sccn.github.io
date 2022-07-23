---
layout: default
title: c. Group level
title: c. Group-level analysis
parent: 11. Write scripts
grand_parent: Tutorials 
---
Group-level analyses using EEGLAB scripts
=====
{: .no_toc }

Building a *STUDY* from the graphic interface (as described in previous
sections) calls eponymous MATLAB functions that may also be called
directly by users. Below we briefly describe these functions. See their
MATLAB help messages for more information. Functions whose names begin
with *std_* take *STUDY* and/or *EEG* structures as arguments and
perform signal processing and/or plotting directly on channel or cluster
activities. Whenever relevant, feel free to look up documentation in the part of the tutorial describing [the STUDY structure](/tutorials/ConceptsGuide/Data_Structures.html#the-study-structure).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'study_script.m'));">Show MATLAB command</button>

Creating a STUDY
-----------------
