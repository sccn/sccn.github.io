---
layout: default
title: I.3 Plotting Channel Spectra and Maps
permalink: /tutorials/single-subject/plotting-channel-spectra-and-maps
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 3
---

{ {Backward_Forward\|I.2:_Channel_Locations\|(MT) I.2: Channel
Locations\|I.4:_Preprocessing_Tools\|(MT) I.4: Preprocessing Tools} }

Plotting channel spectra and maps
---------------------------------

To begin processing the data, we recommend first scrolling the data as
shown before rejecting clearly 'bad' data stretches or data epochs, then
studying their power spectra to be sure that the loaded data are
suitable for further analysis. Note that the Matlab Signal Processing
Toolbox needs to be in your Matlab path to use these functions.

<font color=green>Exploratory Step</font>: Plot Channel Spectra and
Maps.

> To plot the channel spectra and associated topographical maps, select
> <font color=brown>Plot \> Channel spectra and maps</font>. This will
> pop up the { {File\|pop_spectopo.m} } window (below). Leave the
> default settings and press *OK*.


![Image:Pop_spectopo.png]({{ site.baseurl }}/assets/images/Pop_spectopo.png)


> The function should return a { {File\|spectopo.m} } plot (below).
> Since we only sampled 15% of the data (via the *Percent data...* edit
> box above), results should differ slightly on each call. (Naturally,
> this will not occur if you enter 100% in the edit box).


![500px]({{ site.baseurl }}/assets/images/Channel_spectra_spectopo.jpg)


> Each colored trace represents the spectrum of the activity of one data
> channel. The leftmost scalp map shows the scalp distribution of power
> at 6 Hz, which in these data is concentrated on the frontal midline.
> The other scalp maps indicate the distribution of power at 10 Hz and
> 22 Hz.
>
> The { {File\|pop_spectopo.m} } window menu (above) allows the user to
> compute and plot spectra in specific time windows in the data. The
> *Percent data...* value can be used to speed the computation (by
> entering a number close to 0) or to return more definitive measures
> (by entering a number closer to 100).
>
> Note that functions { {File\|pop_spectopo.m} } and {
> {File\|spectopo.m} } also work with epoched data.
>
> Another menu item, <font color=brown>Plot \> Channel
> properties</font>, plots the scalp location of a selected channel, its
> activity spectrum, and an [ERP-image
> plot](/Chapter_08:_Plotting_ERP_images "wikilink") of its activity in
> single-epochs.

The next section deals with some data preprocessing options available
via the EEGLAB menu.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")

{ {Backward_Forward\|I.2:_Channel_Locations\|(MT) I.2: Channel
Locations\|I.4:_Preprocessing_Tools\|(MT) I.4: Preprocessing Tools} }
