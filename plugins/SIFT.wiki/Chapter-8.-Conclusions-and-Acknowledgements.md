---
layout: default
title: Chapter-8.-Conclusions-and-Acknowledgements
long_title: Chapter-8.-Conclusions-and-Acknowledgements
parent: SIFT
grand_parent: Plugins
---
In this tutorial, we have introduced a new, open-source (Matlab-based)
toolbox for electrophysiological information flow analysis, which
functions as a plugin for the EEGLAB environment. We sought to outline
the theoretical basis for vector autoregressive (VAR) model fitting of
electrophysiological data, as well as some VAR-based measures for
multivariate granger-causality and spectral analysis in the time and
frequency domain. We then demonstrated the applicability of these
approaches through simulations and, using the SIFT toolbox, the analysis
of EEG data from an individual performing an error-inducing cognitive
task.

## Acknowledgements

I (Tim Mullen) would like to first express my deep appreciation to Arnaud Delorme and
Christian Kothe who have helped in the development of this toolbox. Dr.
Delorme is the principal developer of EEGLAB and has helped
substantially with integrating the toolbox into the EEGLAB environment
as well as with modifications of his brainmovie3d.m and dipoledensity.m
functions on which the causal brainmovie and causal projection functions
have been based. Mr. Kothe contributed to many conversations regarding
the structure of the toolbox and contributed the function input/output
specification and PropertyGrid code, which is used in some of the
graphical user interfaces. Thanks also to Derrick Lock for significant
help in preparing the online wiki version of this manual.


I would also like to thank Scott Makeig for his constant encouragement
and intellectual contributions in developing this toolbox. Additionally,
I’d like to thank my undergraduate/postgraduate advisor Dr. Robert
Knight (UC Berkeley) who supported my development of the ECViz toolbox
on which the concept of SIFT was based.


Thanks also goes to Virginia De Sa and to Doug Nitz for serving as my
project committee members and for their constant patience throughout the
development of this project.


Finally, a big thanks goes to Nima Bigdely Shamlo, Julie Onton, Thorsten
Zander and others from SCCN and elsewhere who have contributed ideas,
datasets, visualization code, and other useful items to this project.


The author (Tim Mullen) was generously supported by a San Diego
Fellowship, a Glushko Fellowship (Dept. of Cognitive Science), and
endowments from the Swartz Foundation (Old Field, NY).


Parametric model-fitting in SIFT makes use of modified routines from
Alois Schloegl’s open-source TSA+NaN package and, if downloaded
separately, Tapio Schneider and Arnold Neumaier’s ARfit package.
