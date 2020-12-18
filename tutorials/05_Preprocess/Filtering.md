---
layout: default
title: a. Filtering
categories: preproc
parent: 5. Preprocess data
grand_parent: Tutorials
---
Filtering the data
=======
To remove linear trends, it is often desirable to high-pass filter the
data. High-pass filtering the data at 1 Hz or 2 Hz is also recommended to obtain good quality ICA decompositions. Low-pass filtering high frequency noise is also sometimes necessary.

Load the sample EEGLAB dataset
-------------------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

Removing linear trends
-------------------

We recommend filtering continuous EEG data, before epoching or
artifact removal, although epoched data can also be filtered with this
function (each epoch being filtered separately). Filtering the
continuous data minimizes the introduction of filtering artifacts at
epoch boundaries.

Select <span style="color: brown">Tools → Filter the data → Basic FIR filter (new, default)</span>, enter *1* (Hz) as the *Lower edge* frequency,
and press *OK*.

![400px]({{ site.baseurl }}/assets/images/Pop_eegfiltnew_1hz.jpg)

A window will pop up to ask for the name of
the new dataset. We choose to modify the dataset name and to overwrite
the parent dataset by checking the *Overwrite parent* checkbox, then
pressing the *OK* button.

Note that if high-pass and low-pass cutoff frequencies are BOTH
selected, the filtering routine may have problem designing a suitable filter and infinite values might be returned. To avoid this problem,
we recommend first applying the low-pass filter and then, in a second
call, the high-pass filter (or vice versa).
 
If you apply filtering and continue to work with the updated data set,
check that the filter has been applied by selecting menu item
<span style="color: brown">Plot → Channel spectra and maps</span> to plot the
data spectra. 

You might notice that filtered-out frequency regions
might show 'ripples', unavoidable but hopefully acceptable filtering
artifacts. 

Note that removing data portions containing major artifacts (by visual inspection), such a large spikes in the data, before filtering can be preferable since filtering can “spread” the artifact out over “good” data, requiring more data to be rejected after filtering. When you remove major artifacts, and “boundary” event replaces the removed data. Filtering is only applied to continuous data segments, not across boundaries.

# Filtering for connectivity analysis

High pass filtering introduces dependencies in neighboring data sample and is often not recommended for connectivity analysis. In this case, it is usually better to apply piecewise detrending to remove data trends. Piecewise detrending is available in the SIFT EEGLAB plugin for example.

For causal analysis (assessing if one process causes another), call menu item <span style="color: brown">Tools → Filter the data → Basic FIR filter (legacy)</span> and check the checkbox *Use causal filter*. By default EEGLAB applies the filter forward and then again backward,
to ensure that phase delays introduced by the filter are nullified. When using this option, the filter is only applied forward, so phase delays might be introduced and not compensated for. However, causal relashionships are preserved. 

# Filtering without the signal processing toolbox

If the Matlab
Signal Processing Toolbox is present, EEGLAB uses the Matlab routine
*filtfilt()*. This applies the filter forward and then again backward,
to ensure that phase delays introduced by the filter are nullified. 

If the Matlab Signal Processing toobox is not present, EEGLAB may use a
simple filtering method involving the inverse fourrier transform. To do this call menu item <span style="color: brown">Tools → Filter the data → Basic FIR filter (legacy)</span> and check the checkbox *Use (sharper) FFT linear filter instead of FIR filtering*.

# Non-linear infinite impulse response filter and other filters

A infinite impulse response (IIR) filter plug-in is also distributed
as a plug-in to EEGLAB. Once the [iirfilt](https://github.com/sccn/iirfilt) plug-in is installed, it can be
accessed from the menu item <span style="color: brown">Tools → Filter the data → Short IIR filter </span>. This functionality uses the same
graphical interface as the FIR filtering option described above.
Although IIR filters usually introduce different phase delays at
different frequencies, this is compensated for by again applying
filtering in reverse using Matlab function *filtfilt()*. In practice,
infinite impulse response are shorter than FIR filters when used for high pass filtering (a few samples as compared thousands for FIR).

There is much more to be learned about filtering, and more filtering options available in Matlab itself. There is also no ideal filter for EEG data. In practice, we suggest you talk to your collegues about the pros and cons of using different filter solutions.

# Alternative to filtering for line noise removal

Another common use for bandpass filtering is to remove 50-Hz or 60-Hz line noise -- also known as notch filtering. However, to remove line noise, one may also use the [CleanLine](https://github.com/sccn/cleanline) EEGLAB plugin. This plugin adaptively estimates and removes sinusoidal (e.g. line) noise fusing multi-tapering and a Thompson F-statistic. Note that the version of CleanLine implemented in the PREP pipeline claims to have critical fixes [PREP](https://github.com/VisLab/EEG-Clean-Tools) although this claim has not been verified yet. As shown in the comparison figure below, when this method works (and it does not always work), the result can be spectacular.

![Image:cleanline.png](/assets/images/cleanline.png)
