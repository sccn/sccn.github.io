---
layout: default
title: I.5 Extracting Data Epochs
permalink: /tutorials/single-subject/extracting-data-epochs
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 5
---
Data Epochs
========================

To study the event-related EEG dynamics of continuously recorded data,
we must extract data epochs time locked to events of interest (for
example, data epochs time locked to onsets of one class of experimental
stimuli) by selecting <span style="color: brown>Tools \"> Extract Epochs</span>
from the EEGLAB main user interface.


**Extracting data epochs**

![Image:I51pop_epoch.png]({{ site.baseurl }}/assets/images/I51pop_epoch.png)


Click on the upper right button, marked *"…"*, of the resulting {
{File\|pop_epoch.m} } window, which calls up a browser box listing the
available event types.


![Image:I51pop_epoch_event.png]({{ site.baseurl }}/assets/images/I51pop_epoch_event.png)


Here, choose event type *square* (onsets of square target stimuli in
this experiment), and press *OK*. You may also type in the selected
event type directly in the upper text box of the { {File\|pop_epoch.m}
} window.


![Image:I51pop_epoch2.png]({{ site.baseurl }}/assets/images/I51pop_epoch2.png)


Here, retain the default epoch limits (from 1 sec before to 2 sec
after the time-locking event). If you wish, add a descriptive name for
the new dataset. Then press *OK*. A new window will pop up offering
another chance to change the dataset name and/or save the dataset to a
disk file. At this point, it can be quite useful to edit the dataset
description -- to store the exact nature of the new dataset in the
dataset itself, for future reference. Do this by pressing
*Description*. Accept the defaults and enter *OK*.


![Image:I51pop_newset_feb10.jpg]({{ site.baseurl }}/assets/images/I51pop_newset_Feb10.jpg)


Another window will then pop up to facilitate removal of meaningless
epoch baseline offsets. This operation is discussed in the next
section.
In this example, the stimulus-locked windows are 3 seconds long. It is
often better to extract long data epochs, as here, to make
time-frequency decomposition possible at lower (\<\< 10 Hz)
frequencies.

**Removing baseline values**

Removing a mean baseline value from each epoch is useful when baseline
differences between data epochs (e.g., those arising from low frequency
drifts or artifacts) are present. These are not meaningfully
interpretable, but if left in the data could skew the data analysis.

After the data has been epoched, the following window will pop up
automatically. It is also possible to call it directly, by selecting
menu item <span style="color: brown">Tools → Remove baseline</span>.


![Image:Pop_removebase.png]({{ site.baseurl }}/assets/images/Pop_removebase.png)


Here we may specify the baseline period in each epoch (in ms) -- the
latency window in each epoch across which to compute the mean to
remove The original epoched dataset is by default overwritten by the
baseline-removed dataset. Note: There is no uniformly 'optimum' method
for selecting either the baseline period or the baseline value. Using
the mean value in the pre-stimulus period (the { {File\|pop_rmbase.m}
} default) is effective for many datasets, if the goal of the analysis
is to define transformations that occur in the data following the
time-locking events.
By default baseline removal will be performed on all channels data.
However, you can also choose specific channels by type (can be
specified while [editing channel
info](https://sccn.ucsd.edu/wiki/I.2:_Channel_Locations)), or manually
select them. Click on the '...' push buttons to see the list of
available types/channels for selection.
Press *OK* to subtract the baseline (or *Cancel* to not remove the
baseline).

**Save new dataset**

This is a good time to save the epoched and baseline-removed dataset
under a new name, as explained above, since we will be working
extensively with these data epochs. You should also preserve the
continuous dataset on the disk separately to allow later arbitrary
re-epoching for various analyses. To save the current dataset, select
<span style="color: brown> File \"> Save current dataset</span> or
<span style="color: brown> File \"> Save current dataset as</span> from the
EEGLAB menu. (In this case, these two menu items are equivalent, since
we have not yet saved this dataset).

The file-browser window below appears. Entering a name for the dataset
(which should end with the filename extension *.set*), and pressing
*SAVE* (below) and then *OK* (above) will save the dataset including
all its ancillary information re events, channel locations, processing
history, etc., plus any unique structure fields you may have added
yourself - see the [script writing tutorial]().


![Image:Saveepoch.png]({{ site.baseurl }}/assets/images/Saveepoch.png)


