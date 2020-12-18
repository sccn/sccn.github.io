---
layout: default
title: ERICA
parent: Other documents
---

A concurrent project is developing an integrated software framework
(ERICA) for Experimental Recording, Interactive Control and Analysis of
EEG and multimodal experiments, particularly those incorporating
interactive data-adaptive stimulus and feedback control (BCI,
neurofeedback, cognitive monitoring, videogame-like protocols, social
neuroscience experiments, etc.) - an evolving imaging modality we refer
to as [Mobile Brain/body Imaging or
MOBI](http://sccn.ucsd.edu/%7Escott/pdf/). In particular, the Lab
Streaming Layer (LSL), a software by Christian Kothe is available for
synchronous recording of data from multiple sources (EEG, motion
capture, eye tracking, video, audio, etc.). A [video web tutorial on
LSL](http://youtu.be/Y1at7yrcFW0) is also available. To learn more about
the ERICA environment, write to <eeglab@sccn.ucsd.edu>. A Matlab
environment for reviewing and analyzing ERICA data
[Mobilab_software](/Mobilab_software "wikilink") is under construction.

The ERICA (Experimental Real-time Interactive Control and Analysis)
framework is composed of five complementary software environments:

-   A [Lab Streaming Layer](http://code/google/com/p/labstreaminglayer)
    (LSL) framework synchronizes data collection, processing, and
    storage across multiple devices.
-   A SNAP environment linked to LSL coordinates stimulus presentation
    in simple or complex experimental designs.
-   A [MatRiver](/MatRiver "wikilink") LSL client environment that
    allows direct read/write access to LSL data streams from Matlab.
-   An [Enactor](/Enactor "wikilink") Matlab environment interacting
    with LSL and/or MatRiver to maintain and perform online computation
    on a 3-D model of the experimental space and subject actions within
    it.
-   A MatSound MaxMSP patch toolbox, an LSL client coordinating sound
    production from SNAP and/or MatRiver/Enactor.