---
layout: default
title: ERP images 
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



