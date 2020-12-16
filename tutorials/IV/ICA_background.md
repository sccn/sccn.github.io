---
layout: default
title: ICA background
permalink: /tutorials/IV.Appendix/ICA_background.html
parent: IV.Appendix
grand_parent: Tutorials
---

Some background information on EEG Independent Component Analysis
=================================================================

This appendix gives background information and more details on ICA in general as well as on ICA algorithms available using EEGLAB.
For practical information on how to run ICA using EEGLAB please refer to the [tutorial]( /tutorials/single-subject/decomposing-data-using-ICA).



Independent Component Analysis of EEG data
------------------------------------------

Decomposing data by ICA (or any linear decomposition method, including
PCA and its derivatives) involves a linear *change of basis* from data
collected at single scalp channels to a spatially transformed "virtual
channel" basis. 

That is, instead of a collection of simultaneously
recorded single-channel data records, the data are transformed to a
collection of simultaneously recorded outputs of spatial filters applied
to the whole multi-channel data. These spatial filters may be designed
in many ways for many purposes.

In the original scalp channel data, each row of the data recording
matrix represents the time course of summed in voltage differences
between source projections to one data channel and one or more reference
channels (thus itself constituting a linear spatial filter). After ICA
decomposition, each row of the data activation matrix gives the time
course of the activity of one component process spatially filtered from
the channel data.

In the case of ICA decomposition, the independent component filters are
chosen to produce the maximally temporally independent signals available
in the channel data. These are, in effect, *information sources* in the
data whose mixtures, via volume conduction, have been recorded at the
scalp channels. The mixing process (for EEG, by volume conduction) is
passive, linear, and adds no information to the data. On the contrary,
it mixes and obscures the functionally distinct and independent source
contributions.

These information sources may represent synchronous or partialy
synchronous activity within one (or possibly more) cortical patch(es),
else activity from non-cortical sources (e.g., potentials induced by
eyeball movements or produced by single muscle activity, line noise,
etc.). The following example, from [Onton and
Makeig](http://sccn.ucsd.edu/papers/OntonMakeig_ICAERSP06.pdf) (2006),
shows the diversity of source information typically contained in EEG
data, and the striking ability of ICA to separate out these activities
from the recorded channel mixtures.




![500px]({{ site.baseurl }}/assets/images/ICAexample.jpg)




**[View full-size version of this data
image.](/Media:ICAexample_big.jpg "wikilink")** *Fifteen seconds of
EEG data at 9 (of 100) scalp channels (top panel) with activities of 9
(of 100) independent components (ICs, bottom panel). While nearby
electrodes (upper panel) record highly similar mixtures of brain and
non-brain activities, ICA component activities (lower panel) are
temporally distinct (i.e. maximally independent over time), even when
their scalp maps are overlapping. Compare, for example, IC1 and IC3,
accounting for different phases of eye blink artifacts produced by
this subject after each visual letter presentation (grey background)
and ensuing auditory performance feedback signal (colored lines).
Compare, also, IC4 and IC7, which account for overlapping frontal (4-8
Hz) theta band activities appearing during a stretch of correct
performance (seconds 7 through 15). Typical ECG and EMG artifact ICs
are also shown, as well as overlapping posterior (8-12 Hz) alpha band
bursts that appear when the subject waits for the next letter
presentation (white background) For comparison, the repeated average
visual evoked response of a bilateral occipital IC process (IC5) is
shown (in red) on the same (relative) scale. Clearly the unaveraged
activity dynamics of this IC process are not well summarized by its
averaged response, a dramatic illustration of the independence of
phase-locked and phase-incoherent activity.*


Note on ICA algorithms
-----------------------
In general,
the physiological significance of any differences in the results or
different algorithms (or of different parameter choices in the various
algorithms) have not been tested -- neither by us nor, as far as we
know, by anyone else. Applied to simulated, relatively low dimensional
data sets for which all the assumptions of ICA are exactly fulfilled,
all three algorithms return near-equivalent components. We are satisfied
that Infomax ICA (runica/binica) gives stable decompositions with up to
hundreds of channels (assuming enough training data are given, see
below), and therefore we can recommend its use, particularly in its
faster binary form ([binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m) - note that you will also need
to download the binary file at [this page](/Binica "wikilink") and edit
the EEGLAB file icadefs.m so that it points to the right binary).
 
 *Note about jader*: 
 
 this algorithm uses 4th-order moments (whereas Infomax
uses (implicitly) a combination of higher-order moments) but the storage
required for all the 4th-order moments become impractical for datasets
with more than \~50 channels. 

*Note about fastica*: 

Using default
parameters, this algorithm quickly computes individual components (one
by one). However, the order of the components it finds cannot be known
in advance, and performing a complete decomposition is not necessarily
faster than Infomax. Thus for practical purposes its name for it should
not be taken literally. Also, in our experience it may be less stable
than Infomax for high-dimensional data sets.


*Supported Systems for binica:*
 
To use the optional (and much
faster) *binica*, which calls [binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m) , the faster C
translation of [runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=runica.m), you must make the location of the
executable ICA file known to Matlab and executable on your system. Note:
Edit the EEGLAB [icadefs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=icadefs.m) Matlab script file to specify the
location of the [binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m) executable. The EEGLAB toolbox
includes three versions of the binary executable Informax ica routine,
for Linux (compiled under Redhat 2.4), *freebsd* (3.0) and *freebsd*
(4.0) (these are named, respectively *ica_linux2.4* , '' ica_bsd3.0''
and *ica_bsd4.0*). The executable file must also be accessible through
the Unix user path variable otherwise [binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m) won't work.
Windows and sun version (older version of binary ICA executable) are
available [here](http://www.sccn.ucsd.edu/eeglab/binica/) (copy them to
the EEGLAB directory). Please [contact us](mailto:eeglab@sccn.ucsd.edu)
to obtain the latest source code to compile it on your own system.





### How many data points do I need to run an ICA?  
As a general rule, finding
*N*stable components (from N-channel data) typically requires *more
than* *kN^2* data sample points (at each channel), where N^2 is the
number of weights in the unmixing matrix that ICA is trying to learn and
*k* is a multiplier. In our experience, the value of *k* increases as
the number of channels increases. In our example using 32 channels, we
have 30800 data points, giving 30800/32^2 = 30 pts/weight points.
However, to find 256 components, it appears that even 30 points per
weight is not enough data. 



Can you use too much
data? This would only occur when data from radically different EEG
states, from different electrode placements, or containing
non-stereotypic noise were concatenated, increasing the number of scalp
maps associated with independent time courses and forcing ICA to mixture
together dissimilar activations into the N output components. 



ICA weights
------------

In the commandline printout [here](/tutorials/single-subject/decomposing-data-using-ICA#running-ica), 
the *angledelta* is the angle between the
direction of the vector in weight space describing the current learning
step and the direction describing the previous step. An intuitive view
of the annealing angle (*angledelta*) threshold (see above) is as
follows: If the learning step takes the weight vector (in global weight
vector space) 'past' the true or best solution point, the following step
will have to 'back-track.' Therefore, the learning rate is too high (the
learning steps are too big) and should be reduced. If, on the other
hand, the learning rate were too low, the angle would be near 0 degrees,
learning would proceed in (small) steps in the same direction, and
learning would be slow. The default annealing threshold of 60 degrees
was arrived at heuristically, and might not be optimum.


The *runica* Infomax function returns two matrices, a data
sphering matrix (which is used as a linear preprocessing to ICA) and the
ICA weight matrix. For more information, refer to ICA help pages (i.e.
<http://www.sccn.ucsd.edu/~arno/indexica.html>). If you wish, the
resulting decomposition (i.e., ICA weights and sphere matrices) can then
be applied to longer epochs drawn from the same data, e.g. for
time-frequency decompositions for which epochs of 3-sec or more may be
desirable.

Differences between ICA and PCA
---------------------------------

The component order returned by *runica/binica* is in decreasing order
of the EEG variance accounted for by each component. In other words, the
lower the order of a component, the more data (neural and/or
artifactual) it accounts for. In contrast to PCA, for which the first
component may account for 50% of the data, the second 25%, etc..., ICA
component contributions are much more homogeneous, ranging from roughly
5% down to \~0%. This is because PCA specifically makes each successive
component account for as much as possible of the remaining activity not
accounted for by previously determined components -- while ICA seeks
*maximally independent* sources of activity.

PCA components are temporally or spatially orthogonal - smaller
component projections to scalp EEG data typically looking like checker
boards - while ICA components of EEG data are maximally temporally
independent, but spatially unconstrained -- and therefore able to find
maps representing the projection of a partially synchronized domain /
island / patch / region of cortex, no matter how much it may overlap the
projections of other (relatively independent) EEG sources. This is
useful since, apart from ideally (radially) oriented dipoles on the
cortical surface (i.e., on cortical gyri, not in sulci), simple
biophysics shows that the volume projection of each cortical domain must
project appreciably to much of the scalp.


