---
layout: default
title: SIFT
long_title: SIFT
parent: SIFT
grand_parent: Plugins
---
Mapping the structural and active functional properties of brain
networks is a key goal of basic and clinical neuroscience and medicine.
The novelty and importance of this transformative research was recently
emphasized by the U.S. National Institute of Health in their 2010
announcement for the Human Connectome Project:

> *Knowledge of human brain connectivity will transform human
> neuroscience by providing not only a qualitatively novel class of
> data, but also by providing the basic framework necessary to
> synthesize diverse data and, ultimately, elucidate how our brains work
> in health, illness, youth, and old age.*

The study of human brain connectivity generally falls under one or more
of three categories: *structural*, *functional*, and *effective*
(Bullmore and Sporns, 2009).

*Structural connectivity* denotes networks of anatomical (e.g., axonal)
links. Here the primary goal is to understand what brain structures are
*capable* of influencing each other via direct or indirect axonal
connections. This might be studied *in vivo* using invasive axonal
labeling techniques or noninvasive MRI-based diffusion weighted imaging
(DWI/DTI) methods.

*Functional connectivity* denotes (symmetrical) correlations in activity
between brain regions during information processing. Here the primary
goal is to understand what regions are functionally related through
correlations in their activity, as measured by some imaging technique. A
popular form of functional connectivity analysis using functional
magnetic resonance imaging (fMRI) has been to compute the pairwise
correlation (or partial correlation) in BOLD activity for a large number
of voxels or regions of interest within the brain volume.

In contrast to the symmetric nature of functional connectivity,
*effective connectivity* denotes asymmetric or causal dependencies
between brain regions. Here the primary goal is to identify which brain
structures in a functional network are (causally) influencing other
elements of the network during some stage or form of information
processing. Often the term “information flow” is used to indicate
directionally specific (although not necessarily causal) effective
connectivity between neuronal structures. Popular effective connectivity
methods, applied to fMRI and/or electrophysiological (EEG, iEEG, MEG)
imaging data, include dynamic causal modeling, structural equation
modeling, transfer entropy, and Granger-causal methods.

Contemporary research on building a human ‘connectome’ (complete map of
human brain connectivity) has typically focused on structural
connectivity using MRI and diffusion-weighted imaging (DWI) and/or on
functional connectivity using fMRI. However, the brain is a highly
dynamic system, with networks constantly adapting and responding to
environmental influences so as to best suit the needs of the individual.
A complete description of the human connectome necessarily requires
accurate mapping and modeling of transient directed information flow or
causal dynamics within distributed anatomical networks. Efforts to
examine transient dynamics of effective connectivity (causality or
directed information flow) using fMRI are complicated by low temporal
resolution, assumptions regarding the spatial stationarity of the
hemodynamic response, and smoothing transforms introduced in standard
fMRI signal processing (Deshpande et al., 2009a; Deshpande et al.,
2009b). While electro- and magneto-encephalography (EEG/MEG) affords
high temporal resolution, the traditional approach of estimating
connectivity between EEG electrode channels (or MEG sensors) suffers
from a high risk of false positives from volume conduction and non-brain
artifacts. Furthermore, severe limitations in spatial resolution when
using surface sensors further limits the physiological interpretability
of observed connectivity. Although precisely identifying the anatomical
locations of sources of observed electrical activity (the inverse
problem) is mathematically ill-posed, recent improvements in source
separation and localization techniques may allow approximate
identification of such anatomical coordinates with sufficient accuracy
to yield anatomical insight invaluable to a wide range of cognitive
neuroscience and neuroengineering applications (Michel et al., 2004). In
limited circumstances it is also possible to obtain human
intracranially-recorded EEG (ICE, ECoG, iEEG) that, although highly
invasive, affords high spatiotemporal resolution and (often) reduced
susceptibility to non-brain artifacts.

Once activity in specific brain areas have been identified using source
separation and localization, it is possible to look for transient
changes in dependence between these different brain source processes.
Advanced methods for non-invasively detecting and modeling distributed
network events contained in high-density EEG data are highly desirable
for basic and clinical studies of distributed brain activity supporting
behavior and experience. In recent years, Granger Causality (GC) and its
extensions have increasingly been used to explore ‘effective’
connectivity (directed information flow, or causality) in the brain
based on analysis of prediction errors of autoregressive models fit to
channel (or source) waveforms. GC has enjoyed substantial recent success
in the neuroscience community, with over 1200 citations in the last
decade (Google Scholar). This is in part due to the relative simplicity
and interpretability of GC – it is a data-driven approach based on
linear regressive models requiring only a few basic *a priori*
assumptions regarding the generating statistics of the data. However, it
is also a powerful technique for system identification and causal
analysis. While many landmark studies have applied GC to invasively
recorded local field potentials and spike trains, a growing number of
studies have successfully applied GC to non-invasively recorded human
EEG and MEG data (as reviewed in (Bressler and Seth, 2010)). Application
of these methods in the EEG source domain is also being seen in an
increasing number of studies (Hui and Leahy, 2006; Supp et al., 2007;
Astolfi et al., 2007; Haufe et al., 2010).

In the last decade an increasing number of effective connectivity
measures, closely related to Granger’s definition of causality, have
been proposed. Like classic GC, these measures can be derived from
(multivariate) autoregressive models fit to observed data time-series.
These measures can describe different aspects of network dynamics and
thus comprise a complementary set of tools for effective connectivity or
causal analysis.

Several toolboxes affording various forms of Granger-causal (or related)
connectivity analysis are currently available in full or beta-release.
Table 1 provides a list of several of these toolboxes, along with the
website, release version, and license. Although these toolboxes provide
a number of well-written and useful functions, most lack integration
within a more comprehensive framework for EEG signal processing (the
exceptions being Fieldtrip's routines, and TSA, which integrates into
the Biosig EEG/MEG processing suite). Furthermore, many of these may
implement only one or two (often bivariate) connectivity measures, lack
tools for sophisticated visualization, or lack robust statistics or
multi-subject (group) analysis. Finally, to our knowledge, with the
exception of E-Connectome, none of these toolboxes directly support
analysis and visualization of connectivity in the EEG source domain.
These are all factors that our Source Information Flow Toolbox (SIFT),
combined with the EEGLAB software suite, hopes to address.




Table caption. A list of free Matlab-based toolboxes for granger-causal
connectivity analysis in neural data.




|                                                                  |                  |         |                                                             |
|------------------------------------------------------------------|------------------|---------|-------------------------------------------------------------|
| <b>Toolbox Name</b>                                                     | <b>Primary Author</b>   | <b>Website</b>                                                     | <b>License</b> |
| Granger Causality Connectivity Analysis (GCCA) Toolbox           | Anil Seth        | <https://www.sussex.ac.uk/research/centres/sussex-centre-for-consciousness-science/resources/connectivity> | GPL 3   |
| Time-Series Analysis (TSA) Toolbox                               | Alois Schloegl   | <https://sourceforge.net/p/octave/tsa/ci/default/tree/>                 | GPL 2   |
| E-Connectome                                                     | Bin He           | <https://www.nitrc.org/projects/econnectome>                               | GPL 3   |
| Fieldtrip                                                        | Robert Oosteveld |  <http://fieldtrip.fcdonders.nl/>                            | GPL 2   |
| Brain-System for Multivariate AutoRegressive Timeseries (BSMART) | Jie Cui          |  <http://www.brain-smart.org/>                               | --      |


SIFT is an open-source Matlab (The Mathworks, Inc.) toolbox for analysis
and visualization of multivariate information flow and causality,
primarily in EEG/iEEG/MEG datasets following source separation and
localization. The toolbox supports both command-line (scripting) and
graphical user interface (GUI) interaction and is integrated into the
widely used open-source EEGLAB software environment for
electrophysiological data analysis (sccn.ucsd.edu/eeglab). There are
currently four modules: data preprocessing, model fitting and
connectivity estimation, statistical analysis, and visualization. First methods implemented include a large number of
popular frequency-domain granger-causal and coherence measures, obtained
from adaptive multivariate autoregressive models, surrogate and analytic
statistics, and a suite of tools for interactive visualization of
information flow dynamics across time, frequency, and (standard or
personal MRI co-registered) anatomical source locations.

In this tutorial, we will outline the theory underlying multivariate
autoregressive modeling and granger-causal analysis. Practical
considerations, such as data length, parameter selection, and
non-stationarities are addressed throughout the text and useful tests
for estimating statistical significance are outlined. This theory
section is followed by a hands-on walkthrough of the use of the SIFT
toolbox for analyzing source information flow dynamics in an EEG
dataset. Here, we will walk through a typical data-processing pipeline
culminating with the demonstration of some of SIFT’s powerful tools for
interactive visualization of time- and frequency-dependent directed
information flow between localized EEG sources in an
anatomically-coregistered 3D space. Theory boxes throughout the chapter
will provide additional insight into various aspects of model fitting and
parameter selection.

