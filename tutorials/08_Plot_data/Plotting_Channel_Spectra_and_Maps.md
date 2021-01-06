---
layout: default
title: c. Spectra
longtitle:
parent: 8. Plot data
grand_parent: Tutorials
---
Plotting channel spectra and maps
=====================
In addition to reading the tutorial sections below, you may want to watch the short video on computing spectra in EEGLAB (hosted on Youtube) below. In particular, we recommend video 1 and 2 describing the Welch method used in this section, and video 5, describing the EEGLAB functions used in this section

<a href="https://www.youtube.com/playlist?list=PLXc9qfVbMMN2TAoLHVW5NvNmJtwiHurzw"><img align="center" width="400" src= "/assets/images/yt_spectopo2.png"></a>

Load the sample EEGLAB dataset
-----------------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png](/assets/images/Pop_loadset.png)

Plot Channel Spectra and Maps
-----------------

To plot the channel spectra and associated topographical maps, select
<span style="color: brown">Plot → Channel spectra and maps</span>. This will pop up the [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m) window (below). 
Leave the default settings and press *OK*.

![](/assets/images/spectopo1gui.png)

The function should return a [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) plot (below).
Since we only sampled 50% of the data (via the *Percent data...* edit
box above), results should differ slightly on each call. (Naturally,
this will not occur if you enter 100% in the edit box).

![](/assets/images/spectopo1plot.png)

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

On the Matlab command line, the parameter for the calculating the spectrum using
the Welch method are exposed (a window size of 128 sample with no overlap between
windows). We can change these parameters. Select menu item <span style="color: brown">Plot → Channel spectra and maps</span> and in the *Spectral and scalp map options* edit box, enter
" *'winsize', 256, 'overlap', 128* ". 

![](/assets/images/spectopo2gui.png)

This will result in a smoother spectrum with higher frequency
resolution as shown below.

![](/assets/images/spectopo2plot.png)


Note that functions [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo) and [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) also work with epoched data.

Another menu item, <span style="color: brown">Plot → Channel properties</span>, plots the scalp location of a selected channel, its
activity spectrum, and an [ERP-image
plot](/Chapter_08:_Plotting_ERP_images "wikilink") of its activity in
single-epochs.

*Note*: The Matlab Signal Processing Toolbox should to be in your Matlab path to use these functions. EEGLAB has replacement functions in case the signal processing toolbox is not present, but their capabilities are limited. 

*Note*: It is also possible to plot electrode locations in the spectral
graph by entering '' 'electrodes', 'on' '' in the lowest text box
(*Scalp map options*) of the interactive [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m)
window.

