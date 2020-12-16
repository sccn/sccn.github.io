---
layout: default
title: b. Re-referencing
parent: 5. Preprocess data
categories: preproc
grand_parent: Tutorials
---
Re-referencing the data
-------------------------
For detailed background theory on re-referencing EEG data please refer to the [Appendix](/tutorials/IV.Appendix/rereferencing_background.html)

We describe below how to specify the reference electrode(s) in EEGLAB
and to (optionally) re-reference the data

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

### Re-reference the Data

Select <span style="color: brown">Tools → Re-reference the data</span> to
convert the dataset to average reference by calling the [pop_reref.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_reref.m) function. When you call this menu item for the
first time for a given dataset, the following window pops up.


![400px]({{ site.baseurl }}/assets/images/Figure43_pop_rerefgui.jpg)


The (sample) data above were recorded using a mastoid reference. Since
we do not wish to include this reference channel (neither in the data
nor in the average reference), we do not click the *Add current
reference channel in data* check-box. (Do click this check-box when
the recording reference was on the scalp itself). 

The box *Data are
referenced to one site (default)* should remain checked.

Now, press the *OK* button: the re-referencing window below appears.


![400px]({{ site.baseurl }}/assets/images/Figure42_pop_newset.jpg)


Press the *OK* button to compute the average reference. This step will
then be recorded in the main EEGLAB window (not shown). As in the
previous step, a dialogue box will appear asking for the name of the
new dataset. Save the re-referenced data to a new dataset or hit
cancel, as the new reference is not used in the following sections.

After the data have been average referenced, calling the
<span style="color: brown">Tools → Re-reference the data</span> menu still
allows re-referencing the data to any channel or group of channels (or
undoing an average reference transform -- as long as you chose to
include the initial reference channel in the data when you transformed
to average reference).

Note that the re-referencing function also re-references the stored
ICA weights and scalp maps, if they exist.

Re-referencing data can be more complicated. For instance, if you
recorded data referenced to Cz and want to re-reference the data to
linked mastoid. Now you want to add Cz back to your data under the
average reference assumption (the assumption that the average of all
electrode is 0). The first step is to compute average reference and
declare Cz as the reference in the channel editor. In the channel
editor, references are placed after all the data channels (note that
for reference the checkbox "data channel" is unchecked since these are
not actual data channels).
 
To declare a reference, go to the last
channel and press the *Append* button. An empty channel is created.



![Image:Pop_reref4.png]({{ site.baseurl }}/assets/images/Pop_reref4.png)



Fill up the channel label (enter "Cz" in the "Channel label" edit box)
and enter the position of the channel if you have it. For instance,
you may enter the X, Y, Z locations and press the *XYZ -→ Polar &
Sph.* to convert the 3-D Cartesian coordinates to polar and spherical
coordinates. 

If you do not have the electrode location, you may simply
press the *Look up locs* button to automatically look it up based on
the 10-20 channel label (note that this will look up location for all
electrodes).



![Image:Pop_reref3.png]({{ site.baseurl }}/assets/images/Pop_reref3.png)



Then press the *Set reference* pushbutton to set the reference to all
channels to Cz (Cz need to be typed into the checkbox and the channel
range needs to be entered manually as well).



![Image:Pop_reref5.png]({{ site.baseurl }}/assets/images/Pop_reref5.png)



Press OK to validate your new reference channel, and go back to the
re-referencing interface. Now click on the *Retain old reference*
button.



![Image:Pop_reref6.png]({{ site.baseurl }}/assets/images/Pop_reref6.png)


You may now select electrode "Cz" and press OK.



![Image:Pop_reref7.png]({{ site.baseurl }}/assets/images/Pop_reref7.png)



Then press *OK* to actually re-reference your data. This is the first
step. If you actually want to re-reference your data to linked
mastoid, you will need to call the re-referencing interface once more
and select both mastoids as your new reference.
The reason for this overly complex procedure is that the reference
channel can have a location and that this location needs to be
declared in the channel editor so it can be plotted along with other
channels.

The next tutorial section deals with extracting data epochs from
continuous or epoched datasets.

### Re-referencing to multiple channels

Say you collected data with reference M1 (mastoid) and want to process
your data using linked mastoid (M1 and M2) as reference. The process is
as follow:

-   Specify M1 as reference as described in the previous section and
    compute average reference *while keeping electrode M1* (how to
    keep the reference channel is also described in the previous
    section)
-   Re-reference a second time the data selecting both electrodes M1 and
    M2 as reference (you may then either select to keep the reference
    channels or have them deleted)
