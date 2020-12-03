---
layout: default
title: I.8 Plotting ERP images
permalink: /tutorials/single-subject/plotting-erp-images
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 8
---

{
{Backward_Forward\|Chapter_07:_Selecting_Data_Epochs_and_Comparing\|(MT)
Chapter 07: Selecting Data
Epochs\|Chapter_09:_Decomposing_Data_Using_ICA\|(MT)Chapter09:
Decomposing Data Using ICA} }

Plotting ERP images
-------------------

The field of electrophysiological data analysis has been dominated by
analysis of 1-dimensional event-related potential (ERP) averages.
Various aspects of the individual EEG trials that make up an ERP may
produce nearly identical effects. For example, a large peak in an ERP
might be produced by a single bad trial, an across-the-board increase in
power at the same time point, or a coherence in phase across trials
without any noticeable significance within individual trials. In order
to better understand the causes of observed ERP effects, EEGLAB allows
many different *ERP image* trial-by-trial views of a set of data epochs.

ERP-image plots are a related, but more general 2-D (values at
times-by-epochs) view of the event-related data epochs. ERP-image plots
are 2-D transforms of epoched data expressed as 2-D images in which data
epochs are first sorted along some relevant dimension (for example,
subject reaction time, alpha-phase at stimulus onset, etc.), then
(optionally) smoothed (cross adjacent trials) and finally color-coded
and imaged. As opposed to the average ERP, which exists in only one
form, the number of possible ERP-image plots of a set of single trials
is nearly infinite -- the trial data can be sorted and imaged in any
order -- corresponding to epochs encountered traveling in any path
through the 'space of trials'. However, not all sorting orders will give
equal insights into the brain dynamics expressed in the data. It is up
to the user to decide which ERP-image plots to study. By default, trials
are sorted in the order of appearance in the experiment.

It is also easy to misinterpret or over-interpret an ERP-image plot. For
example, using phase-sorting at one frequency (demonstrated below) may
blind the user to the presence of other oscillatory phenomena at
different frequencies in the same data. Again, it is the responsibility
of the user to correctly weight and interpret the evidence that a 2-D
ERP-image plot presents, in light of to the hypothesis of interest --
just as it is the user's responsibility to correctly interpret 1-D ERP
time series.

### Selecting a channel to plot

To plot an ERP image of activity at one data channel in the single
trials of our dataset, we must first choose a channel to plot. Let us,
for example, choose a channel with high alpha band power (near 10 Hz).
[Previously](/Chapter_03:_Plotting_Channel_Spectra_and_Maps "wikilink")
in the tutorial we obtained the { {File\|spectopo.m} } plot reproduced
below.


![425px]({{ site.baseurl }}/assets/images/Channelspectra.gif)


The plot above shows that alpha band power (e.g., at 10 Hz) is
concentrated over the central occipital scalp.

<font color=green>Exploratory Step</font>: Locating Electrodes.

> We will use the dataset as it was after the last Key Step, [Key Step
> 8](/Chapter_05:_Extracting_Data_Epochs#Removing_baseline_values "wikilink").
>
> To find which electrodes are located in this region, we can simply
> plot the electrode names and locations by selecting
> <font color=brown>Plot \> Channel locations \> By name</font>,
> producing the figure below. We see that electrode POz is the channel
> at which alpha power is largest. Click on the *POz* channel label
> (below) to display its number (27).


![425px]({{ site.baseurl }}/assets/images/Channellocationname.gif)


Note: It is also possible to plot electrode locations in the spectral
graph by entering '' 'electrodes', 'on' '' in the lowest text box
(*Scalp map options*) of the interactive { {File\|pop_spectopo.m} }
window.

### Plotting ERP images using pop_erpimage()

Now that we know the number of the channel whose activity we want to
study, we can view its activity in single trials in the form of an
ERP-image plot.

<font color=green>Exploratory Step: </font> Viewing a Channel ERP.

> Select <font color=brown>Plot \> Channel ERP image</font> . This
> brings up the { {File\|pop_erpimage.m} } window (below). Enter the
> channel number (27), a trial-smoothing value of *1*, and press *OK*.


![500px]({{ site.baseurl }}/assets/images/I82pop_erpimage.jpg)


> An ERP image is a rectangular colored image in which every horizontal
> line represents activity occurring in a single experimental trial (or
> a vertical moving average of adjacent single trials). The figure below
> (not an ERP image) explains the process of constructing ERP-image
> plots. Instead of plotting activity in single trials such as
> left-to-right traces in which potential is encoded by the height of
> the trace, we color-code their values in left-to-right straight lines,
> the changing color value indicating the potential value at each time
> point in the trial. For example, in the following image, three
> different single-trial epochs (blue traces) would be coded as three
> different colored lines (below).


![225px]({{ site.baseurl }}/assets/images/Erpimagedemo.jpg)


> By stacking above each other the color-sequence lines for all trials
> in a dataset, we produce an ERP image. In the standard {
> {File\|erpimage.m} } output figure (below), the trace below the ERP
> image shows the average of the single-trial activity, i.e. the ERP
> average of the imaged data epochs. The head plot (top left) containing
> a red dot indicates the position of the selected channel in the
> montage.
>
> Note: Both of these plotting features (as well as several others) can
> be turned off in the { {File\|pop_erpimage.m} } pop-up window (above).
> See check-boxes *plot ERP* and *plot scalp map*.


![400px]({{ site.baseurl }}/assets/images/1erpimagesmooth.gif)


> Since activity in single trials contains many variations, it may be
> useful to smooth the activity (vertically) across neighboring trials
> using a rectangular (boxcar) moving average.

<font color=green>Exploratory Step:</font> Plotting a Smoothed ERP.

> Again call up the { {File\|pop_erpimage.m} } interactive window and
> set the smoothing width to *10* instead of *1*. Now (see below) it is
> easier to see the dominant alpha-band oscillations in single trials.
>
> Note: Because of the large number of available options, parameters
> from the last call (if any) are recalled as defaults (though optional
> arguments entered via the text box are not). If you experience a
> problem with this feature, you may type *\>\>eegh(0)* on the Matlab
> command line to clear the history.


![475px]({{ site.baseurl }}/assets/images/1erpimage27.gif)


> When plotting a large number of trials, it is not necessary to plot
> each (smoothed) trial as a horizontal line. (The screen and/or printer
> resolution may be insufficient to display them all). To reduce the
> imaging delay (and to decrease the saved plot file size), one can
> decimate some of the (smoothed) ERP-image lines. Entering *4* in the
> *Downsampling* box of the { {File\|pop_erpimage.m} } window would
> decimate (reduce) the number of lines in the ERP image by a factor of
> *4*. If the *Smoothing* width is (in this case) greater than *2\*4 =
> 8*, no information will be lost from the smoothed image.
>
> Note: To image our sample dataset, it is not necessary to decimate,
> since we have relatively few (80) trials.

### Sorting trials in ERP images

In the ERP-image figures above, trials were imaged in (bottom-to-top)
order of their occurrence during the experiment. It is also possible to
sort them in order of any other variable that is coded as an event field
belonging to each trial in the dataset. Below, we demonstrate sorting
the same trials in order of response time event latency (reaction time).

<font color=green>Exploratory Step: </font> Sorting Trials in an ERP
Image.

> In the { {File\|pop_erpimage.m} } window again, first press the button
> *Epoch-sorting field*, and select *Latency*. Next, press the button
> *Event type*, and select *rt*. In the resulting ERP image, trials will
> be sorted by the *latency* of *rt* events (our sample data has one
> *rt* event per epoch. If this were not the case,{ {File\|erpimage.m} }
> would only have plotted epochs with rt events). Enter *Event time
> range* of *-200 800* ms to plot activity immediately following
> stimulus onsets.


![575px]({{ site.baseurl }}/assets/images/Erpimagelatency.gif)


> Note: In this and some other interactive pop-windows, holding the
> mouse cursor over the label above a text-entry box for a few seconds
> pops up an explanatory comment.
>
> Now, the { {File\|erpimage.m} } figure below appears. The curved black
> line corresponds to the latency time of the event (rt) we are sorting
> by.


![425px]({{ site.baseurl }}/assets/images/1erpimagelatency.gif)


> In general, the user can sort on any event field value.
>
> For example, call back the { {File\|pop_erpimage.m} } window, press
> the *Epoch-sorting Field* button, and select *position* instead of
> *latency*. Remove *rt* from the *Event type* box. Finally enter *yes*
> under the *Rescale* box. Press *OK*. In the resulting {
> {File\|erpimage.m} } plot, trials are sorted by stimulus position (1
> or 2, automatically normalized values to fit the post-stimulus space
> for display). Note that the smoothing width (10) is applied to both
> the single-trial data and to the sorting variable. This explains the
> oblique line connecting the low (1) and high (2) sorting variable
> regions.
>
> Note: One can also enter a Matlab expression to normalize the sorting
> variable explicitly (see { {File\|erpimage.m} } help).


![425px]({{ site.baseurl }}/assets/images/1erpimageposition.gif)


> Now, reselect the *latency* of the *rt* events as the trial-sorting
> variable (press the *Epoch-sorting field* button to select *latency*
> and press the *Event type* button to select *rt*). Enter *no* under
> *Rescale* (else, reaction times would be automatically normalized).
>
> Use the *Align* input to re-align the single-trial data based on the
> sorting variable (here the reaction time) and the change time limits.
> The latency value given in *Align* will be used for specifying time
> 0.
>
> To select the median of the trial-sorting values (here, median
> reaction time) for specifying the new time 0 (which will be at the
> response time minus the median reaction time), our convention is to
> use *Inf* the Matlab symbol for infinity in this box (as below). If
> you want to set a different value (for instance, while plotting an
> ERPimage for one subject, you might want to use the median reaction
> time you computed for all your subjects), simply enter the value in ms
> in the *Align* input box.
>
> Note: Temporal realignment of data epochs, relative to one another,
> will result in missing data at the lower-left and upper-right corners
> of the ERP image. The ERP-image function shows these as green (0) and
> returns these values as *NaN*s (Matlab not-a-number).


![575px]({{ site.baseurl }}/assets/images/1erpimageinfedit.gif)


> The ERP image figure (below) will be created. Here, the straight
> vertical line at time about 400 ms indicates the moment of the subject
> response, and the curving vertical line, the time at which the
> stimulus was presented in each trial. Compare the figure below with
> the previous non-aligned, RT-sorted ERP image.


![425px]({{ site.baseurl }}/assets/images/1erpimageinf.gif)


### Plotting ERP images with spectral options

Next, we will experiment with sorting trials by their EEG phase value in
a specified time/frequency window. Though *rt* values can be shown in
phase-sorted ERP-image figures, we will omit them for simplicity.

<font color=green>Exploratory Step:</font> Sorting Trials in an ERP by
Phase Value

> To do this, return to the { {File\|pop_erpimage.m} } window from the
> menu. Clear the contents of the ''Epoch-sorting field', *Event type*
> and *Align* inputs. Then, in the *Sort trials by phase* section, enter
> *10* (Hz) under \<*Frequency* and *0*(ms) under *Center window*. Enter
> *-200 800* next to *Time limits (ms)* to zoom in on the period near
> stimulus onset, this option appear at the top of the pop window.


![575px]({{ site.baseurl }}/assets/images/I84pop_erpimage.jpg)


> We then obtain the ERP-image figure below.


![475px]({{ site.baseurl }}/assets/images/1erpimage10.gif)


> Note just before the stimulus onset the red oblique stripe: this is
> produced by phase sorting: the phase (i.e., the latency of the wave
> peaks) is uniformly distributed across the re-sorted trials.
>
> In this computation, a 3-cycle 10 Hz wavelet was applied to a window
> in each trial centered at time 0. The width of the wavelet was 300 ms
> (i.e., three 10-Hz cycles of 100 ms). Therefore, it extended from -150
> ms to 150 ms. After the wavelet was applied to each trial, the
> function sorted the trials in order of the phase values (-pi to pi)
> and displayed an ERP image of the trials in this (bottom-to-top)
> order. The dominance of circa 10-Hz activity in the trials, together
> with the 10-trial smoothing we applied makes the phase coherence
> between adjacent trials obvious in this view.
>
> We could have applied phase-sorting of trials using any time/frequency
> window. The results would depend on the strength of the selected
> frequency in the data, particularly on its degree of momentum (i.e.,
> did the data exhibit long bursts at this frequency), and its
> phase-locking (or not) to experimental events. Phase-sorted ERP images
> using different time and frequency windows represent different paths
> to fly through complex (single-channel) EEG data. (Note: Use keyword
> 'showwin' to image the time window used in sorting the data for any
> type of data-based sorting (e.g., by phase, amplitude, or mean
> value).
>
> To see the phase sorting more clearly, keep the same settings, but
> this time enter *50* under *percent low-amp. trials to ignore*. Here,
> the 50% of trials with smallest 10-Hz (alpha) power in the selected
> time window will be rejected; only the (40) others (larger-alpha 50%)
> will be imaged. Here (below), we can better see how the alpha wave
> seems to resynchronize following the stimulus. Before time 0, alpha
> phase is more or less random (uniformly distributed) and there is
> little activity in the average ERP. At about 200 ms, alpha activity
> seems to (partially) synchronize with the stimulus and an N300 and
> P400 ERP appears.


![475px]({{ site.baseurl }}/assets/images/1erpimage1050.gif)


Our interpretation (above) of these trials as representing phase
synchronization need not be based on visual impression alone. To
statistically assess whether alpha activity is partially resynchronized
by (i.e., is partly phase-reset by) the stimuli, we need to plot the
phase coherence (or phase-locking factor) between the stimulus sequence
and the post-stimulus data. This measure, the *Inter-Trial Coherence
(ITC)* our terminology, takes values between 0 and 1. A value of 1 for
the time frequency window of interest indicates that alpha phase (in
this latency window) is constant in every trial. A value of 0 occurs
when the phase values in all trials are uniformly distributed around the
unit circle. In practice, values somewhat larger than 0 are expected for
any finite number of randomly phase-distributed trials.
<font color=green>Exploratory Step:</font> Inter-Trial Coherence.

> To plot the ITC in our ERP-image figure, we choose to enter the
> following parameters in the { {File\|pop_erpimage.m} } window: we omit
> the *Percent low-amp. of Trials to ignore* value (or enter ). Under
> <font color=brown>Sort trials by phase\>Frequency</font> enter *9 11*
> and also enter *9 11* in the <font color=brown>Inter-Trial
> Coherence\>Frequency</font> box. Enter *0.01* under *Signif. level*
> and press *OK*.
>
> Note that these two entries must be equal (the window actually
> prevents the user from entering different values). Entering a
> frequency range instead of one frequency (e.g., *10* as before) tells
> { {File\|erpimage.m} } to find the data frequency with maximum power
> in the input data (here between 9 and 11 Hz).


![475px]({{ site.baseurl }}/assets/images/I84pop_erpimage2.jpg)


> The following window is created.


![375px]({{ site.baseurl }}/assets/images/I84coher_freq.jpg)


> Two additional plot panels appear below the ERP panel (uV). The middle
> panel, labeled *ERSP* for Event Related Spectral Power, shows mean
> changes in power across the epochs in dB. The blue region indicates 1%
> confidence limits according to surrogate data drawn from random
> windows in the baseline. Here, power at the selected frequency (10.12
> Hz) shows no significant variations across the epoch. The number
> *25.93 dB* in the baseline of this panel indicates the absolute
> baseline power level.
>
> Note: To compare results, it is sometimes useful to set this value
> manually in the main ERP-image pop-window.
>
> The bottom plot panel shows the event-related Inter-Trial Coherence
> (ITC), which indexes the degree of phase synchronization of trials
> relative to stimulus presentation. The value *10.12 Hz* here indicates
> the analysis frequency selected. Phase synchronization becomes
> stronger than our specified p=0.01 significance cutoff at about 300
> ms.
>
> Note: The ITC significance level is typically lower when based on more
> trials. Moreover, ITC is usually not related to power changes.

##### Discussion Point: Does the ERP here arise through partial phase synchronization or reset following stimulus onset?

In a 'pure' case of (partial) phase synchronization:

-   EEG power (at the relevant frequencies) remains constant in the
    post-stimulus interval.
-   The ITC value is significant during the ERP, but less than 1
    (complete phase locking).

In our case, the figure (above) shows a significant post-stimulus
increase in alpha ITC accompanied by a small (though non-significant)
increase in alpha power. In general, an ERP could arise from partial
phase synchronization of ongoing activity combined with a
stimulus-related increase (or decrease) in EEG power.

It is important not to over interpret the results of phase sorting in
ERP-image plots. For example, the following calls from the Matlab
command line simulate 256 1-s data epochs using Gaussian white noise,
low-pass filters this below (simulated) 12 Hz, and draw the following
10-Hz phase sorted ERP-image plot of the resulting data. The figure
appears to identify temporally coherent 10-Hz activity in the (actual)
noise. The (middle) amplitude panel below the ERP-image plot shows,
however, that amplitude at (simulated) 10 Hz does not change
significantly through the (simulated) epochs, and the lowest panel shows
that inter-trial coherence is also nowhere significant (as confirmed
visually by the straight diagonal 10-Hz wave fronts in the center of the
ERP image).

``` matlab
% Simulate 256 1-s epochs with Gaussian noise
% at 256-Hz sampling rate; lowpass < 12 Hz
>> data = eegfilt(randn(1,256*256),256,0,15);

% Plot ERP image, phase sorted at 10 Hz
>> figure;
>> erpimage(data,zeros(1,256),1:256,'Phase-sorted Noise',1,1,...
 'phasesort',[128 0 10],'srate',256,...
 'coher',[10 10 .01], 'erp','caxis',0.9);
```


![475px]({{ site.baseurl }}/assets/images/Noisesort.jpg)


Taking epochs of white noise (as above) and adding a strictly
time-locked 'ERP-like' transient to each trial will give a phase-sorted
ERP-image plot showing a sigmoidal, not a straight diagonal wavefront
signature. How can we differentiate between the two interpretations of
the same data (random EEG plus ERP versus partially phase reset EEG)?
For simulated one-channel data, there is no way to do so, since both are
equally valid ways of looking at the same (simulated) data - no matter
how it was created. After all, the simulated data themselves do not
retain any impression of how they were created - even if such an
impression remains in the mind of the experimenter!

For real data, we must use convergent evidence to bias our
interpretation towards one or the other (or both) interpretations. The
partial phase resetting model begins with the concept that the physical
sources of the EEG (partial synchronized local fields) may ALSO be the
sources of or contributors to average-ERP features. This supposition may
be strengthened or weakened by examination of the spatial scalp
distributions of the ERP features and of the EEG activity. However, here
again, a simple test may not suffice since many cortical sources are
likely to contribute to both EEG and averaged ERPs recorded at a single
electrode (pair). An ERP feature may result from partial phase resetting
of only one of the EEG sources, or it may have many contributions
including truly 'ERP-like' excursions with fixed latency and polarity
across trials, monopolar 'ERP-like' excursions whose latency varies
across trials, and/or partial phase resetting of many EEG processes.
Detailed spatiotemporal modeling of the collection of single-trial data
is required to parcel out these possibilities. For further discussion of
the question in the context of an actual data set, see [Makeig et al.
(2002)](http://sccn.ucsd.edu/science2002.html). In that paper, phase
resetting at alpha and theta frequencies was indicated to be the
predominant cause of the recorded ERP (at least at the indicated scalp
site, POz). How does the ERP in the figure above differ?

The [Makeig et al. paper](http://sccn.ucsd.edu/science2002.html) dealt
with non-target stimuli, whereas for the sample EEGLAB dataset we used
epochs time locked to target stimuli from one subject (same experiment).
The phase synchronization might be different for the two types of
stimuli. Also, the analysis in the paper was carried out over 15
subjects and thousands of trials, whereas here we analyze only 80 trials
from one subject. (The sample data we show here are used for tutorial
purposes. We are now preparing a full report on the target responses in
these experiments.)


<u>Note:</u> Altogether, there are five trial sorting methods available
in *erpimage()* -\>
\* Sort by the sorting variable (default) - Sorts input data trials
(epochs) by the *sortvar*, sorting variable (for example, RT) input for
each epoch of the input data.

-   Sort by value (*valsort*)- Here, trials are sorted in order of their
    mean value in a given time window. Use this option to sort by ERP
    size (option not available yet in the interactive window).
-   Sort by amplitude (*ampsort*)-- Trials are sorted in order of
    spectral amplitude or power at a specified frequency and time
    window. Use this option to display, for example, P300 responses
    sorted by alpha amplitude (option not available yet in the
    interactive window).
-   Sort by phase (*phasesort*)-- Trials are sorted in order of spectral
    phase in a specified time/frequency window. </font>
-   Do not sort (*nosort*)-- Display input trials in the same order they
    are input.

### Plotting spectral amplitude in single trials and additional options

There are several other { {File\|erpimage.m} } options that we will
briefly illustrate in the following example. The *Image amps* entry on
the { {File\|pop_erpimage.m} } window allows us to image amplitude of
the signal (at the frequency of interest) in the single trials, instead
of the raw signals themselves. Check this box. The ''Plot spectrum
(minHz maxHz) '' entry adds a small power spectrum plot to the top right
of the figure. Enter *2 50* to specify the frequency limits for this
graph.

Change the *Epoch-sorting field* box back to *latency* and *Event
type</font>* back to *rt*. Then enter *500* under *Mark times* to plot a
vertical mark at 500 ms (here for illustrative purpose only). Finally
enter *-500 1500* under *Time limits* to zoom in on a specific time
window, and *-3 3* under *Amplitude limits (dB)*.



![575px]({{ site.baseurl }}/assets/images/I85pop_erpimage.jpg)


The { {File\|erpimage.m} } figure below appears.



![425px]({{ site.baseurl }}/assets/images/I85erpimage.jpg)



In the next tutorial, we show how to use EEGLAB to perform and evaluate
ICA decomposition of EEG datasets.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")
{
{Backward_Forward\|Chapter_07:_Selecting_Data_Epochs_and_Comparing\|(MT)
Chapter 07: Selecting Data
Epochs\|Chapter_09:_Decomposing_Data_Using_ICA\|(MT)Chapter09:
Decomposing Data Using ICA} }
