---
layout: default
title: a. Channel Locations
parent: 4. Import data
grand_parent: Tutorials
---
Importing channel location for the tutorial dataset
====================================================

To plot EEG scalp maps in either 2-D or 3-D format, or to estimate
source locations of data components, an EEGLAB dataset must contain
information about the scalp locations of the recording electrodes.

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>.

In the rest of the tutorial, we will use the convention:
<span style="color: brown">Menu_item → Submenu_item</span> to refer to a menu
selection (e.g., here select submenu item <font color=brown>Load
existing dataset</font> under the top-level
<span style="color: brown">File</span> submenu).

In Unix, the following window will pop up (the aspect ratio of this
window may differ in Windows and MacOS):

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

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

### Why are electrodes plotted outside of the head limits
  
In the previous image, electrode EOG1 and EOG2 are plotted beyong the head limit because they extends below the
horizontal plane of the head center. <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m">topoplot.m</a> plots them
as a 'skirt' (or halo) around the cartoon head that marks the
(arc_length = 0.5) head-center plane. (Note: Usually, the best-fitting
sphere is a cm or more above the plane of the nasion and ear canals). By
default, all channels with location arc_lengths \<= 1.0 (head bottom)
are used for interpolation and are shown in the plot. From the
commandline, <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m">topoplot.m</a> allows the user to specify the
interpolation and plotting radii (*intrad* and *plotrad*) as well as the
radius of the cartoon head (*headrad*). The *headrad* value should
normally be kept at its physiologically correct value (0.5). In 'skirt'
mode (see below), the cartoon head is plotted at its normal location
relative to the electrodes, the lower electrodes appearing in a 'skirt'
outside the head cartoon. 

The distance of the electrode positions from the vertex, however,
is proportional to their (great circle) distance on the scalp to the
vertex. This keeps the electrodes on the sides of the head from being
bunched together as they would be in a top-down view of their positions.
This great-circle projection spreads out the positions of the lower
electrodes. Thus, in the figure below, the (bottom) electrodes plotted
on the lower portion of the 'skirt' are actually located on the back of
the neck. In the plot, they appear spread out, whereas in reality they
are bunched on the relatively narrow neck surface. The combinations of
top-down and great-circle projections allows the full component
projection (or raw data scalp map) to be seen clearly, while allowing
the viewer to estimate the actual 3-D locations of plot features.


<img src="https://sccn.github.io/assets/images/Comp252.jpg">



The EEGLAB v4.32 <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m">topoplot.m</a> above shows an independent
component whose bilateral equivalent dipole model had only 2% residual
variance across all 252 electrode locations. This <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m">binica.m</a>
decomposition used PCA to reduce the over 700,000 data points to 160
principal dimensions (a ratio of 28 time points per ICA weight).
If you have computed an equivalent dipole
model for the component map (using the <a href="https://sccn.github.io/tutorials/IV.Appendix/DIPFIT.html">DIPFIT plug-in</a>), <a href="http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m">topoplot.m</a> can indicate the location of the
component equivalent current dipole(s). Note that the 'balls' of the
dipole(s) are located as if looking down from above on the transparent
head. 

