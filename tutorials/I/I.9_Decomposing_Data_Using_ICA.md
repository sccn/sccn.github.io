---
layout: default
title: I.9 Decomposing Data Using ICA
permalink: /tutorials/single-subject/decomposing-data-using-ICA
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 9
---

Using EEGLAB to run ICA decomposition 
======================================
 
For more theory and background 
information on ICA you can also refer to the [Appendix](/tutorials/IV.Appendix/ICA_background.html).


Watch ICA presentations
-----------------------

You can watch [here](https://www.youtube.com/playlist?list=PLXc9qfVbMMN2uDadxZ_OEsHjzcRtlLNxc) 11 short 
presentations on EEG independent component analysis (ICA).

<img align="center" width="200" height="200" src= "{{ site.baseurl }}/assets/images/ICApresentation2.png">


Running ICA decompositions
---------------------------


To compute ICA components of a dataset of EEG epochs (or of a continuous
EEGLAB dataset), select <span style="color: brown">Tools →  Run ICA</span>. 
This
calls the function [pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m). To test this function,
simply press *OK*.


![575px]({{ site.baseurl }}/assets/images/Runica.gif)



We detail each entry of this GUI in detail below.

**ICA Algorithms**

EEGLAB allows users to try
different ICA decomposition algorithms. Only *runica*, which calls [runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=runica.m)
and *jader* which calls the function [jader.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=jader.m) (from Jean-Francois Cardoso) are a part of the default
EEGLAB distribution. 

To use the *fastica* algorithm (Hyvarinen et al.),
one must install the [fastica
toolbox](http://www.cis.hut.fi/projects/ica/fastica/) and include it in
the Matlab path. 

Details of how these ICA algorithms work can be found
in the scientific papers of the teams that developed them. 

Refer to the [Appendix](/tutorials/IV.Appendix/ICA_background.html#note-on-ica-algorithms) for further information on 
the different ICA algorithms.


*Important note* 

We usually run ICA using many more trials that
the sample decomposition presented here. 
ICA works best when given a large amount of basically similar
and mostly clean data. When the number of channels (N) is large (\>\>32)
then a very large amount of data may be required to find N components.
When insufficient data are available, then using the 'pca' option to [jader.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=jader.m) to find fewer than N components may be the only good
option. In general, it is important to give ICA as
much data as possible for successful training. 
Refer to [this Appendix section](/tutorials/IV.Appendix/ICA_background.html#how-many-data-points-do-i-need-to-run-an-ica) for more details.




**Channel types** 

It is possible to select specific channel types
(or even a list of channel numbers) to use for ICA decomposition. For
instance, if you have both EEG and EMG channels, you may want to run ICA
on EEG channels only, since any relationship between EEG and EMG signals
should involve propagation delays and ICA assumes an instantaneous
relationship (e.g., common volume conduction). Use the [channel
editor]( /tutorials/single-subject/channel-locations) to define channel
types.

Pressing *OK* will run the ICA algorithm.


### Running ICA


Running *runica* produces the following text on the Matlab command line:

        Input data size [32,30720] = 32 channels, 30720 frames.
        Finding 32 ICA components using logistic ICA.
        Initial learning rate will be 0.001, block size 36.
        Learning rate will be multiplied by 0.9 whenever angledelta >= 60 deg.
        Training will end when wchange < 1e-06 or after 512 steps.
        Online bias adjustment will be used.
        Removing mean of each channel ...
        Final training data range: -145.3 to 309.344
        Computing the sphering matrix...
        Starting weights are the identity matrix ...
        Sphering the data ...
        Beginning ICA training ...
        step 1 - lrate 0.001000, wchange 1.105647
        step 2 - lrate 0.001000, wchange 0.670896
        step 3 - lrate 0.001000, wchange 0.385967, angledelta 66.5 deg
        step 4 - lrate 0.000900, wchange 0.352572, angledelta 92.0 deg
        step 5 - lrate 0.000810, wchange 0.253948, angledelta 95.8 deg
        step 6 - lrate 0.000729, wchange 0.239778, angledelta 96.8 deg
        ...
        step 55 - lrate 0.000005, wchange 0.000001, angledelta 65.4 deg
        step 56 - lrate 0.000004, wchange 0.000001, angledelta 63.1 deg
        Inverting negative activations: 1 -2 -3 4 -5 6 7 8 9 10 -11 -12 -13 -14 -15 -16 17 -18 -19 -20 -21 -22 -23 24 -25 -26 -27 -28 -29 -30 31 -32
        Sorting components in descending order of mean projected variance ...
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32




Note: the *runica* Infomax algorithm can only select for components with
a supergaussian activity distribution (i.e., more highly peaked than a
Gaussian, something like an inverted T). If there is strong line noise
in the data, it is preferable to enter the option '' 'extended', 1'' in
the command line option box, so the algorithm can also detect
subgaussian sources of activity, such as line current and/or slow
activity.

Another option we often use is the stop option: try '' 'stop', 1E-7'' to
lower the criterion for stopping learning, thereby lengthening ICA
training but possibly returning cleaner decompositions, particularly of
high-density array data. We also recommend the use of collections of
short epochs that have been carefully pruned of noisy epochs (see
[Rejecting artifacts](/Chapter_01:_Rejecting_Artifacts "wikilink") with
EEGLAB).


*Important note:* Run twice on the same data, ICA decompositions under
*runica/binica* will differ slightly. That is, the ordering, scalp
topography and activity time courses of best-matching components may
appear slightly different. This is because ICA decomposition starts with
a random weight matrix (and randomly shuffles the data order in each
training step), so the convergence is slightly different every time. Is
this a problem? At the least, features of the decomposition that do not
remain stable across decompositions of the same data should not be
interpreted except as irresolvable ICA uncertainty.

Differences between decompositions trained on somewhat different data
subsets may have several causes. We have not yet performed such repeated
decompositions and assessed their common features - though this would
seem a sound approach. Instead, in our recent work we have looked for
commonalities between components resulting from decompositions from
different subjects


