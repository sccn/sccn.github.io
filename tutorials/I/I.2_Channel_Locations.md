---
layout: default
title: I.2 Channel Locations
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 2
---


Importing channel location for the tutorial dataset
====================================================

To plot EEG scalp maps in either 2-D or 3-D format, or to estimate
source locations of data components, an EEGLAB dataset must contain
information about the scalp locations of the recording electrodes.

### Load channel location information

To load or edit channel location information contained in a dataset,
select <span style="color: brown>Edit \"> Channel locations</span>.

If you imported a binary data file in the Neuroscan or Biosemi
formats, channel labels will already be present in the dataset (in
EEGLAB v4.31 and later versions). When you call the channel editing
window, a dialog box (shown below) will appear, asking you if you want
to use standard channel locations based on the imported electrode
position labels (for example 'Fz') from a channel locations file using
an extended International 10-20 System.
>
>
>
![Image:Editchannelinfo_auto.png]({{ site.baseurl }}/assets/images/Editchannelinfo_auto.png)
>
>
>
You may choose between several templates. If you intend to perform
source localization, we strongly suggest that you select the second
option "Use MNI coordinates for the BEM Dipfit model" (the first set
of 'BESA' coordinates was designed for a spherical BESA head model,
now obsolete). For the sake of this tutorial, we will press the
*Cancel* button and load the channel location file associated with
this data manually.
>
>
>
![500px]({{ site.baseurl }}/assets/images/Gui_pop_chanedit.jpg)
>
>
>
To load a channel locations file, press the *Read Locations* button
and select the sample channel locations file *eeglab_chan32.locs*
(located in the *sample_data* sub-directory of the EEGLAB
distribution).




![Image:Loadchannellocation.png]({{ site.baseurl }}/assets/images/Loadchannellocation.png)


In the next pop-up window, simply press *OK*. If you do not specify
the file format, the [pop_chanedit.m]() function will attempt
to use the filename extension to assess its format. Press the button
*Read locs help* in the main channel graphic interface window to view
the supported formats.


![250px]({{ site.baseurl }}/assets/images/Chanedit_fileformat_gui.jpg)


Now the loaded channel labels and polar coordinates are displayed in
the [pop_chanedit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanedit.m) window.

We recommend using the default settings.
 
Electrodes plotted outside the head cartoon are electrodes located below the mid-head line (i.e.,
with a negative z (height) coordinate, 0 being the center of the
head). They are plotted outside the head cartoon by convention. 

To plot scalp maps only inside the head cartoon, enter 0.5 in the *Plot
radius* edit box. In this case, the two eye electrodes will not be
displayed nor taken into account when computing interpolated 2-D scalp
maps for display or (in some cases) further processing. 

These settings are used for all scalp topographies plotted in EEGLAB. 

If you do not see enough of the recorded field, set this dialogue box to 1.0 to
interpolate and show scalp maps including all possible scalp channel
locations, with parts of the head below the (0.5) head equator shown
in a 'skirt' or 'halo' region outside the cartoon head boundary (more
precise separate controls of which channel locations to plot are
available from the command line: see the 'Help' message for the scalp
map plotting function [topoplot.m]()).

In the window below, you may scroll through the channel field values
1-by-1 using the *\<* and *\>* buttons, or in steps of 10 using *\<\<*
and *\>\>*.


![500px]({{ site.baseurl }}/assets/images/Gui_pop_chanedit2.jpg)



### Viewing Channel Locations

Reopen <span style="color: brown>Edit \"> Channel locations</span> if you
closed it. 

To visualize the 2-D locations of the channels, press *Plot
2-D* above the *Read Locations* button. Else, at any time during an EEGLAB session you may refer to a plot showing the channel locations
by selecting <font color=brown>Plot → Channel location → By
name</font>. 
Either command pops up a window like that below. 

*Note*: In
this plot, click on any channel label to see its channel number.

<span style="color: red">WARNING</span>: Equating 'channel locations' with
(single) *electrode* locations only makes sense when all channels use
the same 'reference channel.' An EEG channel signal is always the
''difference' between voltages at two (or more) electrodes --
typically some electrode "referred to" a reference channel (or channel
combination. Equating the signal 'channel location' to the location of
one of the contributing electrodes is quite imprecise, as the channel
must be equally sensitive to potentials flowing to *either* of its two
(or more) contributing scalp electrodes.


![Image:Channellocationname.png]({{ site.baseurl }}/assets/images/Channellocationname.png)


The appendix [importing channel locations](/A03:_Importing_Channel_Locations "wikilink") contains
additional information.


