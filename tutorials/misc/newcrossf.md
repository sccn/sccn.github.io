---
layout: default
title: sample dataset description
parent: Miscellaneous
grand_parent: Tutorials
---
### Computing component cross-coherences

To determine the degree of synchronization between the activations of
two components, we may plot their event-related cross-coherence (a
concept first demonstrated for EEG analysis by Rappelsberger). Even
though independent components are (maximally) independent over the whole
time range of the training data, they may become transiently (partially)
synchronized in specific frequency bands. To plot component
cross-coherence, select <span style="color: brown">Plot → Time-frequency transforms → Component cross-coherence</span>, 
which calls [pop_crossf.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_crossf.m).
Below, we enter:
 - components *4* and *9* (Use any
components in your decomposition), 
- *Bootstrap significance level* to
*0.01*, 
- set *padratio* to *16*. 

We again press *OK*.


![px]({{ site.baseurl }}/assets/images/Component_cross-coherence_gui.jpg)



In the [crossf.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=crossf.m) window below, the two components become
synchronized (*top panel*) around 11.5 Hz (click on the image to zoom
in). The *upper panel* shows the coherence magnitude (between 0 and 1, 1
representing two perfectly synchronized signals). The *lower panel*
indicates the phase difference between the two signals at time/frequency
points where cross-coherence magnitude (in the *top panel*) is
significant. In this example, the two components are synchronized with a
phase offset of about -120 degrees (this phase difference can also be
plotted as latency delay in ms, using the minimum-phase assumption. See
[crossf.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=crossf.m) help for more details about the function parameters
and the plotted variables).


![425px]({{ site.baseurl }}/assets/images/Crossf.gif)



One can also use <span style="color: brown">Plot → Time-frequency transforms → Channel cross-coherence</span> 
to plot event-related cross-coherence
between a pair of scalp channels, but here relatively distant electrode
channels may appear synchronized only because a large EEG source
projects to both of them. Other source confounds may also affect channel
coherences in unintuitive ways. 

Computing cross-coherences on
independent data components may index transient synchronization between
particular cortical domains.