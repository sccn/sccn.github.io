---
layout: default
title: I.11 Time-Frequency decomposition
permalink: /tutorials/single-subject/time-frequency-decomposition
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
---

{ {Backward_Forward\|Chapter_10:_Working_with_ICA_components\|(MT)
Chapter 10: Working with ICA
components\|Chapter_12:_Multiple_Datasets\|(MT) Chapter 12: Multiple
Datasets} }

Time/frequency decomposition
----------------------------

Time/frequency analysis characterizes changes or perturbations in the
spectral content of the data considered as a sum of windowed sinusoidal
functions (i.e. sinusoidal wavelets). There is a long history and much
recent development of methods for time/frequency decomposition. The
methods used in the basic EEGLAB functions are straightforward. Their
mathematical details are given in a reference paper [(Delorme and
Makeig, 2004)](http://sccn.ucsd.edu/eeglab/download/eeglab_jnm03.pdf).

#### Decomposing channel data

<font color=green>KEY STEP 10:</font> ERSP and ITC

> To detect transient *event-related spectral perturbation,* or ERSP,
> [(Makeig, 1993)](http://sccn.ucsd.edu/~scott/ersp93.html)
> (event-related shifts in the power spectrum) and inter-trial coherence
> (ITC) (event-related phase-locking) events in epoched EEGLAB datasets,
> select <font color=brown>Plot \> Time frequency transforms \> Channel
> time-frequency</font> (calling { {File\|pop_timef.m} }. Below, we
> enter *14* (Cz) for the *Channel number*, *.01* for the *Bootstrap
> significance level*, and set the optional parameter *padratio* to *16*
> as below (a <em>very high</em> over-sampling factor for frequencies,
> giving a smooth looking plot at quite some unnecessary computational
> cost). We let the other defaults remain.
>
> Note the default "Wavelet cycles" entry of <b>3 0.5</b>. As explained
> in the help message for the <em>newtimef()</em> function, this means
> that the wavelet used to measure the amount and phase of the data in
> each successive, overlapping time window will begin with a 3-cycle
> wavelet (with a Hanning-tapered window applied). The '0.5' here means
> that the number of cycles in the wavelets used for higher frequencies
> will continue to expand slowly, reaching half (0.5) the number of
> cycles in the equivalent FFT window at its highest frequency. This
> controls the shapes of the individual time/frequency windows measured
> by the function, and their shapes in the resulting time/frequency
> panes. Note: This information does not set the lowest frequency to be
> analyzed. By current default, the lowest frequency window is about 0.5
> seconds long. Three cycles in 0.5 sec sets the lowest frequency
> analyzed to about 6 Hz. To make this lowest frequency near 3 Hz, we
> would need to add the Optional newtimef() argument <b>'winlen',
> xxx</b> where xxx is the sampling rate of the data (EEG.srate, also
> shown on the blue EEGLAB menu window). This would specify that the
> window length ('winlen') at the lowest frequency should be xxx samples
> long (i.e., 1 sec long), meaning the lowest analysis frequency would
> be 3 cycles n 1 sec, i.e. 1 Hz. We press *OK*.


![px]({{ site.baseurl }}/assets/images/Pop_newtimef()_gui.jpg)


> The { {File\|timef.m} } window below appears. The ''top image '' shows
> mean event-related changes in spectral power (from pre-stimulus
> baseline) at each time during the epoch and at each frequency (\< 50
> Hz). To inspect these changes more closely, click on the color image.
> A new window will pop up. Enabling Matlab zoom allows zooming in to
> any desired time/frequency window. The ERSP image shows a brief but
> significant decrease in power at about 370 ms at 8 Hz (click on the
> image to zoom in and determine the exact frequency), a power increase
> centered at 13.5 Hz and starting at 300 ms. More spectral changes
> occur at 20-28 Hz. Note that the method used to asses significance is
> based on random data shuffling, so the exact significance limits of
> these features may appear slightly different.
>
> The *upper left panel* shows the baseline mean power spectrum, and the
> lower part of the upper panel, the ERSP envelope (low and high mean dB
> values, relative to baseline, at each time in the epoch).
>
> The *lower image* shows is the Inter-Trial coherence (ITC) at all
> frequencies. We previously encountered the ITC when we explained the {
> {File\|ERP_image_plotting.m} } function. A significant ITC indicates
> that the EEG activity at a given time and frequency in single trials
> becomes phase-locked (not phase-random with respect to the
> time-locking experimental event). Here, a significant ITC appears
> briefly at about 10 Hz (at about the same time as the power increase
> in the *upper panel*), but this effect might well become insignificant
> using a more rigorous significance threshold. Note that the
> time/frequency points showing significant ITC and ERSP are not
> necessarily identical. In this plot, ITC hardly reaches significance
> and cannot be interpreted. The help message for the { {File\|timef.m}
> } function contains information about all its parameters, the images
> and curve plotted, and their meanings.


![375px]({{ site.baseurl }}/assets/images/Timef.gif)


#### Computing component time/frequency transforms

It is more interesting to look at time-frequency decompositions of
component activations than of separate channel activities, since
independent components may directly index the activity of one brain EEG
source, whereas channel activities sum potentials volume-conducted from
different parts of the brain.

To plot a component time-frequency transform, we select
<font color=brown>Plot \> Time/frequency transforms \> Component
time-frequency</font> (calling { {File\|pop_timef.m} }. Enter *10* for
the *Component number* to plot, *\[-500 1000\]* for the "Epoch time
range", (FFT) for *Wavelet cycles*, and *.01* for the *Bootstrap
significance level*. Note that Morlet wavelets are used by default
although it is also possible to use sinusoidal wavelets. We change
*padratio* to *16* and add the optional argument '' 'maxfreq', '30' ''
to visualize only frequencies up to 30 Hz. Again, we press *OK*.


Note: { {File\|pop_timef.m} } decompositions using FFTs allow
computation of lower frequencies than wavelets, since they compute as
low as one cycle per window, whereas the wavelet method uses a fixed
number of cycles (default 3) for each frequency.


![px]({{ site.baseurl }}/assets/images/Component_tf_transform_gui.jpg)



The following { {File\|timef.m} } window appears. The ITC image (*lower
panel*) shows strong synchronization between the component activity and
stimulus appearance, first near 15 Hz then near 4 Hz. The ERSP image
(*upper panel*) shows that the 15-Hz phase-locking is followed by a
15-Hz power increase, and that the 4-Hz phase-locking event is
accompanied by, but outlasts, a 4-Hz power increase. Note that the
appearance of oscillatory activity in the ERP (*trace under bottom ITC
image*) before and after the stimulus is not significant according to
ITC.


![425px]({{ site.baseurl }}/assets/images/Componenttimefreq.gif)


#### Computing component cross-coherences

To determine the degree of synchronization between the activations of
two components, we may plot their event-related cross-coherence (a
concept first demonstrated for EEG analysis by Rappelsberger). Even
though independent components are (maximally) independent over the whole
time range of the training data, they may become transiently (partially)
synchronized in specific frequency bands. To plot component
cross-coherence, select <font color = brown>Plot \> Time-frequency
transforms \> Component cross-coherence</font>, which calls {
{File\|pop_crossf.m} }. Below, we enter components *4* and *9* (Use any
components in your decomposition), *Bootstrap significance level* to
*0.01*, set *padratio* to *16*. We again press *OK*.


![px]({{ site.baseurl }}/assets/images/Component_cross-coherence_gui.jpg)



In the { {File\|crossf.m} } window below, the two components become
synchronized (*top panel*) around 11.5 Hz (click on the image to zoom
in). The *upper panel* shows the coherence magnitude (between 0 and 1, 1
representing two perfectly synchronized signals). The *lower panel*
indicates the phase difference between the two signals at time/frequency
points where cross-coherence magnitude (in the *top panel*) is
significant. In this example, the two components are synchronized with a
phase offset of about -120 degrees (this phase difference can also be
plotted as latency delay in ms, using the minimum-phase assumption. See
{ {File\|crossf.m} } help for more details about the function parameters
and the plotted variables).


![425px]({{ site.baseurl }}/assets/images/Crossf.gif)



One can also use <font color = brown>Plot \> Time-frequency transforms
\> Channel cross-coherence</font> to plot event-related cross-coherence
between a pair of scalp channels, but here relatively distant electrode
channels may appear synchronized only because a large EEG source
projects to both of them. Other source confounds may also affect channel
coherences in unintuitive ways. Computing cross-coherences on
independent data components may index transient synchronization between
particular cortical domains.

#### Plotting ERSP time course and topography

Recall that spectral perturbations at a single-analysis frequency and
channel or component in the single epochs (sorted by some relevant
value) can be imaged using { {File\|erpimage.m} } or by selecting
<font color=brown>Plot \> Component\|Channel ERP image</font>.

Called from the command line (see [EEGLAB script
writing](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink")), the {
{File\|timef.m} } and { {File\|crossf.m} } routines can return the data
for each part of their figures as a Matlab variable. Accumulating the
ERSP and ITC images (plus the ERSP baseline and significance-level
information) for all channels (e.g., via an [EEGLAB
script](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink")) allows use of
another toolbox routine, { {File\|tftopo.m} } (currently not available
from the EEGLAB menu).

In the next tutorial, we show more about how to import data and events
into EEGLAB datasets.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")
{ {Backward_Forward\|Chapter_10:_Working_with_ICA_components\|(MT)
Chapter 10: Working with ICA
components\|Chapter_12:_Multiple_Datasets\|(MT) Chapter 12: Multiple
Datasets} }
