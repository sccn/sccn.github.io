---
layout: default
title: a. Filtering
categories: preproc
parent: 5. Preprocess data
grand_parent: Tutorials
---
Filtering the data
-------------------
To remove linear trends, it is often desirable to high-pass filter the
data.

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

### Removing linear trends

We recommend filtering continuous EEG data, before epoching or
artifact removal, although epoched data can also be filtered with this
function (each epoch being filtered separately). 

Filtering the
continuous data minimizes the introduction of filtering artifacts at
epoch boundaries.

Select <span style="color: brown">Tools → Filter the data → Basic FIR filter (new, default)</span>, enter *1* (Hz) as the *Lower edge* frequency,
and press *OK*.


![400px]({{ site.baseurl }}/assets/images/Pop_eegfiltnew_1hz.jpg)


A [pop_newset.m]() window will pop up to ask for the name of
the new dataset. We choose to modify the dataset name and to overwrite
the parent dataset by checking the *Overwrite parent* checkbox, then
pressing the *OK* button.


![400px]({{ site.baseurl }}/assets/images/Figure42_pop_newset.jpg)


Note that if high-pass and low-pass cutoff frequencies are BOTH
selected, the filtering routine may not work. To avoid this problem,
we recommend first applying the low-pass filter and then, in a second
call, the high-pass filter (or vice versa).
 
 
Another common use for bandpass filtering is to remove 50-Hz or 60-Hz
line noise. The filtering option in EEGLAB, [eegfilt.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegfilt.m),
uses linear finite impulse response (FIR) filtering. 

If the Matlab
Signal Processing Toolbox is present, it uses the Matlab routine
*filtfilt()*. This applies the filter forward and then again backward,
to ensure that phase delays introduced by the filter are nullified. 

If the Matlab Signal Processing toobox is not present, EEGLAB uses a
simple filtering method involving the inverse fourrier transform.

A infinite impulse response (IIR) filter plug-in is also distributed
as a plug-in to EEGLAB. Once the plug-in is installed ([see how to
install a plug-in
here](https://sccn.ucsd.edu/wiki/EEGLAB_Extensions#)), it can be
accessed from the menu item <span style="color: brown">Tools → Filter the data → Short IIR filter </span>. This functionality uses the same
graphical interface as the FIR filtering option described above.
Although IIR filters usually introduce different phase delays at
different frequencies, this is compensated for by again applying
filtering in reverse using Matlab function *filtfilt()*. In practice,
we suggest you test the use of this IIR filter, as it is stronger (and
shorter) than FIR filters.

If you apply filtering and continue to work with the updated data set,
check that the filter has been applied by selecting menu item
<span style="color: brown">Plot → Channel spectra and maps</span> to plot the
data spectra. 

You might notice that filtered-out frequency regions
might show 'ripples', unavoidable but hopefully acceptable filtering
artifacts. 

Note that temoving major artifacts, such a large spikes in the data, before filtering can be preferable since filtering can “spread” the artifact out over “good” data, requiring more data to be rejected after filtering. When you remove major artifacts, and “boundary” event replaces the removed data. Filtering is only applied to continuous data segments, not across boundaries.

*Note:* There is much more to be learned about filtering,
and more filtering options available in Matlab itself.