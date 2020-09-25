---
layout: default
title: I.4 Preprocessing Tools
permalink: /tutorials/single-subject/I.4_Preprocessing_Tools
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
---

{ {Backward_Forward\|I.3:_Plotting_Channel_Spectra_and_Maps\|(MT) I.3:
Plotting Channel Spectra\|I.5:_Extracting_Data_Epochs\|(MT) I.5:
Extracting Data Epochs} }

Preprocessing tools
-------------------

The upper portion of the <font color=brown>Tools</font> menu may be used
to call three data preprocessing routines:

#### Changing the data sampling rate

The most common use for <font color=brown>Tools \> Change sampling
rate</font> is to reduce the sampling rate to save memory and disk
storage. A { {File\|pop_resample.m} } window pops up, asking for the new
sampling rate. The function uses Matlab *resample()* (in the Signal
Processing toolbox-- if you do not have this toolbox, it will use the
slow Matlab function *griddata*). Do not use this function here, since
the tutorial EEG dataset is already at an acceptable sampling rate.

#### Filtering the data

To remove linear trends, it is often desirable to high-pass filter the
data.

<font color=green>KEY STEP 6</font>: Remove linear trends.

> We recommend filtering continuous EEG data, before epoching or
> artifact removal, although epoched data can also be filtered with this
> function (each epoch being filtered separately). Filtering the
> continuous data minimizes the introduction of filtering artifacts at
> epoch boundaries.
>
> Select <font color=brown>Tools \> Filter the data \> Basic FIR filter
> (new, default)</font>, enter *1* (Hz) as the *Lower edge* frequency,
> and press *OK*.


![400px]({{ site.baseurl }}/assets/images/Pop_eegfiltnew_1hz.jpg)


> A { {File\|pop_newset.m} } window will pop up to ask for the name of
> the new dataset. We choose to modify the dataset name and to overwrite
> the parent dataset by checking the *Overwrite parent* checkbox, then
> pressing the *OK* button.


![400px]({{ site.baseurl }}/assets/images/Figure42_pop_newset.jpg)


> Note that if high-pass and low-pass cutoff frequencies are BOTH
> selected, the filtering routine may not work. To avoid this problem,
> we recommend first applying the low-pass filter and then, in a second
> call, the high-pass filter (or vice versa).
>
> Another common use for bandpass filtering is to remove 50-Hz or 60-Hz
> line noise. The filtering option in EEGLAB, { {File\|eegfilt.m} },
> uses linear finite impulse response (FIR) filtering. If the Matlab
> Signal Processing Toolbox is present, it uses the Matlab routine
> *filtfilt()*. This applies the filter forward and then again backward,
> to ensure that phase delays introduced by the filter are nullified. If
> the Matlab Signal Processing toobox is not present, EEGLAB uses a
> simple filtering method involving the inverse fourrier transform.
>
> A infinite impulse response (IIR) filter plug-in is also distributed
> as a plug-in to EEGLAB. Once the plug-in is installed ( [see how to
> install a plug-in
> here](https://sccn.ucsd.edu/wiki/EEGLAB_Extensions#)), it can be
> accessed from the menu item <font color=brown>Tools \> Filter the data
> \> Short IIR filter </font>. This functionality uses the same
> graphical interface as the FIR filtering option described above.
> Although IIR filters usually introduce different phase delays at
> different frequencies, this is compensated for by again applying
> filtering in reverse using Matlab function *filtfilt()*. In practice,
> we suggest you test the use of this IIR filter, as it is stronger (and
> shorter) than FIR filters.
>
> If you apply filtering and continue to work with the updated data set,
> check that the filter has been applied by selecting menu item
> <font color=brown>Plot \> Channel spectra and maps</font> to plot the
> data spectra. You might notice that filtered-out frequency regions
> might show 'ripples', unavoidable but hopefully acceptable filtering
> artifacts. (Note: There is much more to be learned about filtering,
> and more filtering options available in Matlab itself).

#### Re-referencing the data

##### What is re-referencing and why re-reference

The reference electrode used in recording EEG data is usually termed the
'common' reference for the data -- if all the channels use this same
reference. Typical recording references in EEG recording are one mastoid
(for example, TP10 in the 10-20 System, the electrode colored red in the
picture below), linked mastoids (usually, digitally-linked mastoids,
computed *post hoc*, the vertex electrode (Cz), single or linked
earlobes, or the nose tip. Systems with active electrodes (e.g. BIOSEMI
Active Two), may record data reference-free. In this case, a reference
be must be chosen *post hoc* during data import. Failing to do so will
leave 40 dB of unnecessary noise in the data!

There is no 'best' common reference site. Some researchers claim that
non-scalp references (earlobes, nose) introduce more noise than a scalp
channel reference though this has not been proven to our knowledge. If
the data have been recorded with a given reference, they can usually be
re-referenced (inside or outside EEGLAB) to any other reference channel
or channel combination.


![400px]({{ site.baseurl }}/assets/images/Reref.jpg)


Converting data, before analysis, from fixed or common reference (for
example, from a common earlobe or other channel reference) to 'average
reference' is advocated by some researchers, particularly when the
electrode montage covers nearly the whole head (as for some high-density
recording systems). The advantage of average reference rests on the fact
that outward positive and negative currents, summed across an entire
(electrically isolated) sphere, will sum to 0 (by Ohm's law). For
example, in the figure below a tangentially-oriented electrical source
is associated with a positive inward current to the left (here, blue)
and an opposing outward negative current to the right (red). If the
current passing through the base of the skull to the neck and body is
assumed to be negligible (for instance, because of low conductance of
the skull at the base of the brain), one may assume that the sum of the
electric field values recorded at all (sufficiently dense and evenly
distributed) scalp electrodes is always 0 (the average reference
assumption).

The problem with this assumption is that true average reference data
would require the distribution of electrodes to be even over the head.
This is not usually the case, as researchers typically place more
electrodes over certain scalp areas, and fewer (if any) on the lower
half of the head surface. As a consequence, an average reference result
using one montage may not be directly comparable to an average reference
result obtained using another montage.



![Image:Averef.gif]({{ site.baseurl }}/assets/images/Averef.gif)



Below, we detail the process of transforming data to 'average
reference'. Note that in this process, the implied activity time course
at the former reference electrode may be calculated from the rest of the
data (so the data acquires an additional channel - though not an
additional degree of freedom!). Also note that if the data were recorded
using nose tip or ear lobe electrodes, you should not include these
reference electrodes when computing the average reference in (1)
(below), Thus, in the example below the dividing factor (in (2)) would
be 64 instead of 65. Note that in localizing sources using the EEGLAB
DIPFIT plug-in, 'average reference' will be used internally (without
user input).

The choice of data reference does color (literally) the plotted results
of the data analysis. For example, plots of mean alpha power over the
scalp must have a minimum at the reference channel, even if there are in
fact alpha sources just below and oriented toward the reference channel!
However, no (valid) reference can said to be wrong - rather, each
reference can be said to give another view of the data. However, the
nature of the reference needs to be taken into account when evaluating
(or, particularly, comparing) EEG results.


![Image:Reref2.gif]({{ site.baseurl }}/assets/images/Reref2.gif)



For ICA decomposition (covered later in the tutorial), the selection of
reference is not so important. This is because changing the reference
only amounts to making a linear transformation of the data (in
mathematical terms, multiplying it by a fixed re-referencing matrix), a
transformation to which ICA should be insensitive. In practice, we have
obtained results of similar quality from data recorded and analyzed with
mastoid, vertex, or nose tip reference.

We advise recording eye channels (conventionally four channels, two for
vertical eye movement detection and two for horizontal eye movement
detection) using the same reference as other channels, instead of using
bipolar montages. One can always recover the bipolar montage activity by
subtracting the activities of the electrode pairs. We term these
channels 'peri-ocular EEG' channels since what they record is not
exclusively electro-oculographic (EOG) signals, but also includes e.g.
prefrontal EEG activities.

ICA can be used to decompose data from either average reference, common
reference, or bipolar reference channels -- or from more than one of
these types at once. However, plotting single scalp maps requires that
all channels use either the same common reference or the same average
reference. Robert Oostenveld advises that peri-ocular channel values,
even in ICA component maps, may best be omitted from inverse source
modeling using simple head models, since these are apt to poorly model
the conductance geometry at the front of the head.

##### Specify reference and re-reference the data

We will now describe how to specify the reference electrode(s) in EEGLAB
and to (optionally) re-reference the data

<font color=green>Exploratory Step</font>: Re-reference the Data.

> Select <font color=brown>Tools \> Re-reference the data</font> to
> convert the dataset to average reference by calling the {
> {File\|pop_reref.m} } function. When you call this menu item for the
> first time for a given dataset, the following window pops up.


![400px]({{ site.baseurl }}/assets/images/Figure43_pop_rerefgui.jpg)


> The (sample) data above were recorded using a mastoid reference. Since
> we do not wish to include this reference channel (neither in the data
> nor in the average reference), we do not click the *Add current
> reference channel in data* check-box. (Do click this check-box when
> the recording reference was on the scalp itself). The box *Data are
> referenced to one site (default)* should remain checked.
>
> Now, press the *OK* button: the re-referencing window below appears.


![400px]({{ site.baseurl }}/assets/images/Figure42_pop_newset.jpg)


> Press the *OK* button to compute the average reference. This step will
> then be recorded in the main EEGLAB window (not shown). As in the
> previous step, a dialogue box will appear asking for the name of the
> new dataset. Save the re-referenced data to a new dataset or hit
> cancel, as the new reference is not used in the following sections.
>
> After the data have been average referenced, calling the
> <font color=brown>Tools \> Re-reference the data</font> menu still
> allows re-referencing the data to any channel or group of channels (or
> undoing an average reference transform -- as long as you chose to
> include the initial reference channel in the data when you transformed
> to average reference).
>
> Note that the re-referencing function also re-references the stored
> ICA weights and scalp maps, if they exist.
>
> Re-referencing data can be more complicated. For instance, if you
> recorded data referenced to Cz and want to re-reference the data to
> linked mastoid. Now you want to add Cz back to your data under the
> average reference assumption (the assumption that the average of all
> electrode is 0). The first step is to compute average reference and
> declare Cz as the reference in the channel editor. In the channel
> editor, references are placed after all the data channels (note that
> for reference the checkbox "data channel" is unchecked since these are
> not actual data channels). To declare a reference, go to the last
> channel and press the *Append* button. An empty channel is created.
>
>
>
> ![Image:Pop_reref4.png]({{ site.baseurl }}/assets/images/Pop_reref4.png)
>
>
>
> Fill up the channel label (enter "Cz" in the "Channel label" edit box)
> and enter the position of the channel if you have it. For instance,
> you may enter the X, Y, Z locations and press the *XYZ -\> Polar &
> Sph.* to convert the 3-D Cartesian coordinates to polar and spherical
> coordinates. If you do not have the electrode location, you may simply
> press the *Look up locs* button to automatically look it up based on
> the 10-20 channel label (note that this will look up location for all
> electrodes).
>
>
>
> ![Image:Pop_reref3.png]({{ site.baseurl }}/assets/images/Pop_reref3.png)
>
>
>
> Then press the *Set reference* pushbutton to set the reference to all
> channels to Cz (Cz need to be typed into the checkbox and the channel
> range needs to be entered manually as well).
>
>
>
> ![Image:Pop_reref5.png]({{ site.baseurl }}/assets/images/Pop_reref5.png)
>
>
>
> Press OK to validate your new reference channel, and go back to the
> re-referencing interface. Now click on the *Retain old reference*
> button.
>
>
>
> ![Image:Pop_reref6.png]({{ site.baseurl }}/assets/images/Pop_reref6.png)
>
>
> You may now select electrode "Cz" and press OK.
>
>
>
> ![Image:Pop_reref7.png]({{ site.baseurl }}/assets/images/Pop_reref7.png)
>
>
>
> Then press *OK* to actually re-reference your data. This is the first
> step. If you actually want to re-reference your data to linked
> mastoid, you will need to call the re-referencing interface once more
> and select both mastoids as your new reference.
> The reason for this overly complex procedure is that the reference
> channel can have a location and that this location needs to be
> declared in the channel editor so it can be plotted along with other
> channels.
>
> The next tutorial section deals with extracting data epochs from
> continuous or epoched datasets.

##### Re-reference to multiple channels

Say you collected data with reference M1 (mastoid) and want to process
your data using linked mastoid (M1 and M2) as reference. The process is
as follow:

-   Specify M1 as reference as described in the previous section and
    compute average reference **while keeping electrode M1** (how to
    keep the reference channel is also described in the previous
    section)
-   Re-reference a second time the data selecting both electrodes M1 and
    M2 as reference (you may then either select to keep the reference
    channels or have them deleted)

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")

{ {Backward_Forward\|I.3:_Plotting_Channel_Spectra_and_Maps\|(MT) I.3:
Plotting Channel Spectra and Maps\|I.5:_Extracting_Data_Epochs\|(MT)
I.5: Extracting Data Epochs} }