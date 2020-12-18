---
layout: default
title: c. Spectra
parent: 8. Plot data
grand_parent: Tutorials
---
Plotting channel spectra and maps
-----------------------
### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data_epochs_ica.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*. You could also select the file "eeglab_data.set" although you would need to import or look up channel locations to plot spectra with scalp topographies.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

To begin processing the data, we recommend first scrolling the data as
shown before rejecting clearly 'bad' data stretches or data epochs, then
studying their power spectra to be sure that the loaded data are
suitable for further analysis. 

Note that the Matlab Signal Processing Toolbox should to be in your Matlab path to use these functions. EEGLAB has some replacement functions in case the signal processing toolbox is not present, but if this is an option, it is recommended to use the Matlab implementation. 

### Plot Channel Spectra and Maps

To plot the channel spectra and associated topographical maps, select
<span style="color: brown">Plot → Channel spectra and maps</span>. 

This will pop up the [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m) window (below). 

Leave the default settings and press *OK*.


![Image:Pop_spectopo.png]({{ site.baseurl }}/assets/images/Pop_spectopo.png)


The function should return a [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) plot (below).
Since we only sampled 15% of the data (via the *Percent data...* edit
box above), results should differ slightly on each call. (Naturally,
this will not occur if you enter 100% in the edit box).


![500px]({{ site.baseurl }}/assets/images/Channel_spectra_spectopo.jpg)


Each colored trace represents the spectrum of the activity of one data
channel. The leftmost scalp map shows the scalp distribution of power
at 6 Hz, which in these data is concentrated on the frontal midline.
The other scalp maps indicate the distribution of power at 10 Hz and
22 Hz.

The [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m) window menu (above) allows the user to
compute and plot spectra in specific time windows in the data. The
*Percent data...* value can be used to speed the computation (by
entering a number close to 0) or to return more definitive measures
(by entering a number closer to 100).

Note that functions [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo) and [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) also work with epoched data.

Another menu item, <font color=brown>Plot → Channel
properties</font>, plots the scalp location of a selected channel, its
activity spectrum, and an [ERP-image
plot](/Chapter_08:_Plotting_ERP_images "wikilink") of its activity in
single-epochs.
