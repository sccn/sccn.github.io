---
layout: default
title: III.1 Rejecting Artifacts
permalink: /tutorials/advanced-topics/rejecting-artifacts.html
parent: III.Advanced topics
grand_parent: Tutorials
---
<font color=red>In EEGLAB 2019.1, make sure to select the option "Show
all menus from previous versions of EEGLAB" in EEGLAB menu item **File
\> Preference** to be able to use the tools on this page.</font>

Rejecting artifacts in continuous and epoched data
--------------------------------------------------

Strategy: The approach used in EEGLAB for artifact rejection is to use
'statistical' thresholding to 'suggest' epochs to reject from analysis.
Current computers are fast enough to allow easy confirmation and
adjustment of suggested rejections by visual inspection, which our {
{File\|eegplot.m} } tool makes convenient. We therefore favor
*semi-automated rejection* coupled with visual inspection, as detailed
below. In practice, we favor applying EEGLAB rejection methods to
*independent components* of the data, using a seven-stage method
outlined
[below](/#Rejection_based_on_independent_data_components "wikilink").

Examples: In all this section, we illustrate EEGLAB methods for artifact
rejection using the same sample EEG dataset we used in the [single
subject data analysis
tutorial](/I.Single_subject_data_processing_tutorial "wikilink"). These
data are not perfectly suited for illustrating artifact rejection since
they have relatively few artifacts! Nevertheless, by setting low
thresholds for artifact detection it is possible to find and mark
outlier trials. Though these may not necessarily be artifact related, we
use them here to illustrate how the EEGLAB data rejection functions
work. We encourage users to make their own determinations as to which
data to reject and to analyze using the set of EEGLAB rejection tools.

### Rejecting artifacts in continuous data

##### Rejecting data by visual inspection

Rejecting portions of continuous data can be performed visually using
function { {File\|pop_eegplot.m} }. Select <font color=brown>Tools \>
Reject continuous data</font>. This will open a warning message window,
simply press *Continue*. Select data for rejection by dragging the mouse
over a data region. After marking some portions of the data for
rejection, press *REJECT* and a new data set will be created with the
rejected data omitted. EEGLAB will adjust the *EEG.event* structure
fields and will insert *boundary* events where data has been rejected,
with a duration field holding the duration of the data portion that was
rejected. The *boundary* events will appear in the new dataset, marked
in red (see the second image below). Thus, rejection on continuous data
must be performed 'before' separating it into data epochs. Note: To
*deselect* a portion of the data, simply click on the selected region.
This allows re-inspection of the data portions marked for rejection in
two or more passes, e.g., after the user has developed a more consistent
rejection strategy or threshold. See the section on [Visualizing EEG
data](/Chapter_01:_Loading_Data_in_EEGLAB "wikilink") under the main
tutorial for more information about how to use this interactive
window.



![575px](/assets/images/Iii1eegplot.jpg)

![575px](/assets/images/Iii1eegplot1.jpg)



Note: To select portions of data that extend out of the plotting window,
simply drag the mouse over the new region and connect it to a previously
marked region. For instance, in the following plotting window which
already had the time interval 2.1 seconds to 3.4 seconds selected (as
shown above), drag the mouse from 6.9 seconds back to 4.7.



![575px](/assets/images/Iii1eegplot2.jpg)


##### Rejecting data channels based on channel statistics

Channel statistics may help determine whether to remove a channel or
not. To compute and plot one channel statistical characteristics, use
menu <font color=brown>Plot \> Data statistics \> channel
statistics</font>. In the pop-up window below enter the channel number.
The parameter "Trim percentage" (default is 5%) is used for computing
the trimmed statistics (recomputing statistics after removing tails of
the distribution). If P is this percentage, then data values below the P
percentile and above the 1-P percentile are excluded for computing
trimmed statistics.



![225px](/assets/images/Pop_signalstat1.jpg)



Pressing *OK* will open the image below.



![575px](/assets/images/Ch10_signalstat.jpg)



Some estimated variables of the statistics are printed as text in the
lower panel to facilitate graphical analysis and interpretation. These
variables are the signal mean, standard deviation, skewness, and
kurtosis (technically called the 4 first cumulants of the distribution)
as well as the median. The last text output displays the
Kolmogorov-Smirnov test result (estimating whether the data distribution
is Gaussian or not) at a significance level of p=0.05.

The upper left panel shows the data histogram (blue bars), a vertical
red line indicating the data mean, a fitted normal distribution (light
blue curve) and a normal distribution fitted to the trimmed data (yellow
curve). The P and 1-P percentile points are marked with yellow ticks on
the X axis. A horizontal notched-box plot with whiskers is drawn below
the histogram. The box has lines at the lower quartile
(25th-percentile), median, and upper quartile (75th-percentile) values.
The whiskers are lines extending from each end of the box to show the
extent of the rest of the data. The whisker extends to the most extreme
data value within 1.5 times the width of the box. Outliers ('+') are
data with values beyond the ends of the whiskers.

The upper right panel shows the empirical quantile-quantile plot
(QQ-plot). Plotted are the quantiles of the data versus the quantiles of
a Standard Normal (i.e., Gaussian) distribution. The QQ-plot visually
helps to determine whether the data sample is drawn from a Normal
distribution. If the data samples do come from a Normal distribution
(same shape), even if the distribution is shifted and re-scaled from the
standard normal distribution (different location and scale parameters),
the plot will be linear.

Empirically, 'bad' channels have distributions of potential values that
are further away from a Gaussian distribution than other scalp channels.
For example, plotting the statistics of periocular (eye) Channel 1
below, we can see that it is further away from a normal distribution
than Channel 10 above. (However, Channel 1 should not itself be
considered a 'bad' channel since ICA can extract the eye movement
artifacts from it, making the remained data from this channel usable for
futher analysis of neural EEG sources that project to the face). The
function plotting data statistics may provide an objective measure for
removing a data channel. Select menu item <font color=brown>Edit \>
Select data</font> to remove one or more data channels. It is also
possible to plot event statistics from the EEGLAB menu -- see the
[EEGLAB event tutorial](/Chapter_03:_Event_Processing "wikilink") for
details.



![575px](/assets/images/Ch1_signalstat.jpg)



Note that the function above may also be used to detect bad channels in
non-continuous (epoched) data.

### Rejecting artifacts in epoched data

In contrast to continuous EEG data, we have developed several functions
to find and mark for rejection those data epochs that appear to contain
artifacts using their statistical distributions. Since we want to work
with epoched dataset, you should either load an earlier saved epoched
dataset, or using the downloaded dataset (better loaded with channel
locations info), use the following Matlab script code:

``` matlab
EEG = pop_eegfilt( EEG, 1, 0, [], [0]); % Highpass filter cutoff freq. 1Hz.
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'Continuous EEG Data'); % Save as new dataset.
EEG = pop_reref( EEG, [], 'refstate',0); % Re-reference the data
EEG = pop_epoch( EEG, { 'square' }, [-1 2], 'newname', 'Continuous EEG Data epochs', 'epochinfo', 'yes'); % Epoch dataset using 'square' events.
EEG = pop_rmbase( EEG, [-1000 0]); % remove baseline
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET, 'setname', 'Continuous EEG Data epochs', 'overwrite', 'on');
% save dataset

[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % store dataset
eeglab redraw % redraw eeglab to show the new epoched dataset
```


After having an epoched dataset, call the main window for epoched data
rejection, select <font color=brown>Tools \> Reject data epochs \>
Reject data (all methods)</font>. The window below will pop up. We will
describe the fields of this window in top-to-bottom order. First, change
the bottom multiple choice button reading <font color=brown>Show all
trials marked for rejection by the measure selected above or checked
below</font> to the first option: <font color=brown>Show only the new
trials marked for rejection by the measure selected above</font>. We
will come back to the default option at the end.


![675px](/assets/images/Iii2pop_rejmenu.jpg)




##### Rejecting epochs by visual inspection

As with continuous data it is possible to use EEGLAB to reject epoched
data simply by visual inspection. To do so, press the *Scroll data*
button on the top of the interactive window. A scrolling window will pop
up. Chage the scale to '79'. Epochs are shown delimited by blue dashed
lines and can be selected/deselected for rejection simply by clinking on
them. Rejecting parts of an epoch is not possible.


![575px](/assets/images/Iii21eegplot.jpg)


##### Rejecting extreme values

During 'threshold rejection', the user sets up bounding values the data
should not exceed. If the data (at the selected electrodes) exceeds the
given limits during a trial, the trial is marked for rejection. Enter
the following values under *find abnormal values* (which calls function
{ {File\|pop_eegthresh.m} }), and press *CALC/PLOT*. The parameters
entered below tell EEGLAB that EEG values should not exceed +/-*75* µV
in any of the 32 channels (*1:32* ) at any time within the epoch
(''-1000 ''to *2000* ms).


![575px](/assets/images/Iii22find_abnormal_val.jpg)


Marked trials are highlighted in the { {File\|eegplot.m} } window
(below) that then pops up. Now epochs marked for rejection may be
un-marked manually simply by clicking on them. Note that the activity at
some electrodes is shown in red, indicating the electrodes in which the
outlier values were found. Press *Update Marks* to confirm the epoch
markings.


![575px](/assets/images/Iii22eegplot.jpg)




At this point, a warning will pop up indicating that the marked epochs
have not yet been rejected and are simply marked for rejection. When
seeing this warning, press *OK* to return to main rejection window.


![275px](/assets/images/Iii22warning.jpg)



Also note that several thresholds may be entered along with separate
applicable time windows. In the following case, in addition to the
preceding rejection, additional epochs in which EEG potentials went
above *25* µV or below *-25* µV during the *-500* to ms interval will be
marked for rejection.


![575px](/assets/images/Rawyellowmultiple.gif)


##### Rejecting abnormal trends

Artifactual currents may cause linear drift to occur at some electrodes.
To detect such drifts, we designed a function that fits the data to a
straight line and marks the trial for rejection if the slope exceeds a
given threshold. The slope is expressed in microvolt over the whole
epoch (50, for instance, would correspond to an epoch in which the
straight-line fit value might be 0 µv at the beginning of the trial and
50 µ v at the end). The minimal fit between the EEG data and a line of
minimal slope is determined using a standard R-square measure. To test
this, in the main rejection window enter the following data under *find
abnormal trends* (which calls function { {File\|pop_rejtrend.m} }, and
press *CALC/PLOT*.


![575px](/assets/images/Rawgreen.gif)



The following window will pop up. Note that in our example the values we
entered are clearly too low (otherwise we could not detect any linear
drifts in in this clean EEG dataset). Electrodes triggering the
rejection are again indicated in red. To deselect epochs for rejection,
click on them. To close the scrolling window, press the *Update marks*
button.


![575px](/assets/images/Iii23eegplot.jpg)



Note: Calling function { {File\|pop_rejtrend.m} } either directly from
the command line, or by selecting <font color=brown>Tools \> Reject data
epochs \> Reject flat line data</font>, allows specifying additional
parameters.

##### Rejecting improbable data

By determining the probability distribution of values across the data
epochs, one can compute the probability of occurrence of each trial.
Trials containing artifacts are (hopefully) improbable events and thus
may be detected using a function that measures the probability of
occurrence of trials. Here, thresholds are expressed in terms of
standard deviations of the mean probability distribution. Note that the
probability measure is applied both to single electrodes and the
collection of all electrodes. In the main rejection window, enter the
following parameters under *find improbable data* press *Calculate*
(which calls function { {File\|pop_jointprob.m} }), and then press
*PLOT*.


![575px](/assets/images/Iii24find_improbable_data.jpg)



The first time this function is run on a dataset, its computation may
take some time. However the trial probability distributions will be
stored for future calls. The following display shows the probability
measure value for every trial and electrode (each number at the bottom
shows an electrode, the blue traces the trial values). On the right, the
panel containing the green lines shows the probability measure over all
the electrodes. Rejection is carried out using both single- and
all-channel thresholds. To disable one of these, simply raise its limit
(e.g. to 15 std.). The probability limits may be changed in the window
below (for example, to 3 standard deviations). The horizontal red lines
shift as limit values are then modified. Note that if you change the
threshold in the window below the edit boxes in the main window will be
automatically updated (after pressing the *UPDATE* button).


![375px](/assets/images/Iii24rejecttrials.jpg)



It is also possible to look in detail at the trial probability measure
for each electrode by clicking on its sub-axis plot in the above window.
For instance, by clicking on electrode number two on the plot, the
following window would pop up (from left to right, the first plot is the
[ERPimage](/Chapter_08:_Plotting_ERP_images "wikilink") of the square
values of EEG data for each trial, the second plot indicates which
trials were labeled for rejection (all electrodes combined) and the last
plot is the original probability measure plot for this electrode with
limits indicated in red).


![375px](/assets/images/Iii24elctrode2.jpg)



Close this window and press the *UPDATE* button in the probability plot
window to add to the list of trials marked for rejection.

Now press the *'Scroll data* button to obtain the standard scrolling
data window. Inspect the trials marked for rejection, make any
adjustments manually, then close the window by pressing *UPDATE
MARKS*.


![625px](/assets/images/Iii24eegplot.jpg)


##### Rejecting abnormally distributed data

Artifactual data epochs sometimes have very 'peaky' activity value
distributions. For instance, if a discontinuity occurs in the activity
of data epoch for a given electrode, the activity will be either close
to one value or the other. To detect these distributions, a statistical
measure called kurtosis is useful. Kurtosis is also known as the fourth
cumulant of the distribution (the skewness, variance and mean being the
first three). A high positive kurtosis value indicates an abnormally
'peaky' distribution of activity in a data epoch, while a high negative
kurtosis value indicates abnormally flat activity distribution. Once
more, single- and all-channel thresholds are defined in terms of
standard deviations from mean kurtosis value. For example, enter the
following parameters under ''find abnormal distribution '' press
*Calculate* (which calls function { {File\|pop_rejkurt.m} }), then press
*PLOT*.


![575px](/assets/images/Iii25find_abnormal_dist.jpg)



In the main rejection window note that the *Currently marked trials*
field have changed to 5. In the plot figure all trials above the
threshold (red line) are marked for rejection, note that there are more
than 5 such lines. The figure presents all channels, and the same trial
can exceed the threshold several times in different channles, and
therefore there are more lines than marked trials.


![500px](/assets/images/Iii25rejecttrials.jpg)



As with probability rejection, these limits may be updated in the pop-up
window below, and pressing *Scroll data* in the main rejection window
(above) brings up the standard data scrolling window display which may
be used to manually adjust the list of epochs marked for rejection.

##### Rejecting abnormal spectra

According to our analysis (Delorme, A., Makeig, S., Jung, T.P.,
Sejnowski, T.J. (2001), "[Automatic rejection of event-related potential
trials and components using independent component
analysis](http://www.cnl.salk.edu/%7Earno/abstracts/2001sfn.html)"),
rejecting data epochs using spectral estimates may be the most effective
method for selecting data epochs to reject for analysis. In this case,
thresholds are expressed in terms of amplitude changes relative to
baseline in dB. To specify that the spectrum should not deviate from
baseline by *+/-50* dB in the '' 0-2'' Hz frequency window, enter the
following parameters under '' find abnormal spectra'' (which calls
function { {File\|pop_rejspec.m} }), then press *CALC/PLOT*.


![575px](/assets/images/Iii26find_abnormal_spectra.jpg)



Computing the data spectrum for every data epoch and channel may take a
while. We use a frequency decomposition based on the slepian multitaper
(Matlab pmtm() function) to obtain more accurate spectra than using
standard Fourier transforms. After computing the trial spectra, the
function removes the average power spectrum from each trial spectrum and
tests whether the remaining spectral differences exceed the selected
thresholds. Here, two windows pop up (as below), the top window being
slaved to the bottom. The top window shows the data epochs and the
bottom window the power spectra of the same epochs. When scrolling
through the trial spectra, the user may use the top window to check what
caused a data trial to be labeled as a spectral outlier. After further
updating the list of marked trials, close both windows by pressing
*UPDATE MARKS* in the bottom window.


![575px](/assets/images/Iii26eegplotup.jpg)

![575px](/assets/images/Iii26eegplotdown.jpg)


As with standard rejection of extreme values, several frequency
thresholding windows may be defined. In the window below, we specify
that the trial spectra should again not deviate from the mean by *+/-50*
dB in the *0-2* Hz frequency window (good for catching eye movements)
and should not deviate by *+25* or *-100* dB in the *20-40* Hz frequency
window (useful for detecting muscle activity).


![575px](/assets/images/Iii26find_abnormal_spectra2.jpg)




##### Inspecting current versus previously proposed rejections

To compare the effects of two different rejection thresholds, the user
can plot the currently and previously marked data epochs in different
colors. To do this, change the option in the long rectangular tab under
*Plotting options* (at the buttom of the figure). Select
<font color=brown>Show previous and new trials marked for rejection by
this measure selected above</font>. For instance, using '' abnormal
distribution'', enter the following parameters and press *Scroll
data*.


![575px](/assets/images/Iii27find_abnormal_dist.jpg)



The scrolling window appears and now shows that at trials 11 & 12 the
blue window is actually divided into two, with dark blue on the top and
light blue on the bottom. Dark blue indicates that the trial is
currently marked as rejected. The light blue indicates that the trial
was already rejected using the previous rejection threshold.


![575px](/assets/images/Iii27eegplot.jpg)



Note: Pressing *UPDATE MARKS* only updates the currently rejected trials
and optional visual adjustments. Previously rejected trials are ignored
and can not be removed manually in the plot window.

##### Inspecting results of all rejection measures

To visually inspect data epochs marked for rejection by different
rejection measures, select <font color=brown>Show all trials marked for
rejection measures by the measure selected above or checked below</font>
in the long rectangular tab under '' Plotting options''. Then press
*CALC/PLOT* under *Find abnormal spectra*. Rejected windows are divided
into several colored patches, each color corresponding to a specific
rejection measure. Channels colored red are those marked for rejection
by any method.


![575px](/assets/images/Iii28eegplot.jpg)



When visually modifying the set of trials labeled for rejection in the
window above, all the *current rejection measure* are affected and are
reflected in the main rejection window after you press the *UPDATE
MARKS* button.

##### Notes and strategy

-   The approach we take to artifact rejection is to use statistical
    thresholding to suggest epochs to reject from analysis. Current
    computers are fast enough to allow easy confirmation and adjustment
    of suggested rejections by visual inspection. We therefore favor
    *semi-automated rejection* coupled with visual inspection.
-   All the functions presented here can also be called individually
    through <font color=brown>Plot \> Reject data epochs</font> or from
    the Matlab command line.
-   After labeling trials for rejection, it is advisable to *save* the
    dataset before actually rejecting the marked trials (marks will be
    saved along with the dataset). This gives one the ability go back to
    the original dataset and recall which trials were rejected.
-   To actually reject the marked trials either use the option *Reject
    marked trials* at the buttom of the main rejection window, or use
    the main eeglab window options <font color=brown>Tools \> Reject
    data epochs \> Reject marked epochs</font>.
-   All these rejection measures are useful, but if one does not know
    how to use them they may be inefficient. Because of this, we have
    not provided standard rejection thresholds for all the measures. In
    the future we may include such information in this tutorial. The
    user should *begin* by visually rejecting epochs from some test
    data, then adjust parameters for one or more of the rejection
    measures, comparing the visually selected epochs with the results of
    the rejection measure. All the measures can capture both simulated
    and real data artifacts. In our experience, the most efficient
    measures seem to be frequency threshold and linear trend detection.
-   We typically apply semi-automated rejection to the *independent
    component activations* instead of to the raw channel data, as
    described below.

Rejection based on independent data components
----------------------------------------------

We usually apply the measures described above to the activations of the
independent components of the data. As independent components tend to
concentrate artifacts, we have found that bad epochs can be more easily
detected using independent component activities. The functions described
above work exactly the same when applied to data components as when they
are applied to the raw channel data. Select <font color=brown>Tools \>
Reject data using ICA \> Reject data (all methods)</font>. We suggest
that the analysis be done iteratively in the following seven steps:

1.  Visually reject unsuitable (e.g. paroxysmal) portions of the
    continuous data.
2.  Separate the data into suitable short data epochs.
3.  Perform ICA on these epochs to derive their independent components.
4.  Perform semi-automated and visual-inspection based rejection of data
    epochs on the derived components. (\*)
5.  Visually inspect and select data epochs for rejection.
6.  Reject the selected data epochs.
7.  Perform ICA a second time on the pruned collection of short data
    epochs -- This may improve the quality of the ICA decomposition,
    revealing more independent components accounting for neural, as
    opposed to mixed artifactual activity. If desired, the ICA unmixing
    and sphere matrices may then be applied to (longer) data epochs from
    the same continuous data. Longer data epochs are useful for
    time/frequency analysis, and may be desirable for tracking other
    slow dynamic features.
8.  Inspect and reject the components. Note that components should NOT
    be rejected before the second ICA, but after.

(\*) After closing the main ICA rejection window, select
<font color=brown>Tools \> Reject data using ICA \> Export marks to data
rejection</font> and then <font color=brown>Tools \> Reject data epochs
\> Reject by inspection</font> to visualize data epochs marked for
rejection using ICA component activities.
