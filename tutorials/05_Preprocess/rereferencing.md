---
layout: default
title: b. Re-referencing
long_title: b. Re-referencing
parent: 5. Preprocess data
grand_parent: Tutorials
---
Re-referencing the data
======
For detailed background theory on re-referencing EEG data, please refer to the [Appendix](/tutorials/ConceptsGuide/rereferencing_background.html). We describe below how to specify the reference electrode(s) in EEGLAB and to (optionally) re-reference the data.

Load the sample EEGLAB dataset
-------------------------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" distributed with
the toolbox and located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png](/assets/images/Pop_loadset.png)

Calculating average reference
-------------------------

Calculating an average reference is recommended for source localization.

Select <span style="color: brown">Tools → Re-reference the data</span> to
convert the dataset to average reference by calling the [pop_reref.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_reref.m) function. When you call this menu item for the
first time for a given dataset, the following window pops up.


![](/assets/images/Figure43_pop_rerefgui.jpg)


The (sample) data above were recorded using a mastoid reference. Since
we do not wish to include this reference channel (neither in the data
nor in the average reference), we do not click the *Add current
reference channel in data* checkbox.

Press the *Ok* button to compute the average reference. This step will
then be recorded in the main EEGLAB window (not shown). As in the
previous step, a dialogue box will appear asking for the new dataset's name.

After the data have been average referenced, calling the
<span style="color: brown">Tools → Re-reference the data</span> menu still
allows re-referencing the data to any channel or group of channels (or
undoing an average reference transform -- as long as you chose to
include the initial reference channel in the data when you transformed
to average reference).

Note that the re-referencing function also re-references the stored
ICA weights and scalp maps, if they exist.

Retaining the reference channel
-------------------------

Re-referencing data can be more complicated. For instance, say you
recorded data referenced to Cz and wish to re-reference the data to
average reference. You may also want to add Cz back to your data under the
average reference assumption (the assumption that the average of all
electrodes is 0). The first step is to compute average reference and
declare Cz as the reference in the channel editor.

For this example, we will use the [TEST.CNT](http://sccn.ucsd.edu/eeglab/download/TEST.CNT) dataset. Save the file on your hard drive and import it in EEGLAB using menu item <span style="color: brown">File → Import data → Using EEGLAB functions and plugins → From Neuroscan .CNT file</span>.
 
To declare Cz as a reference, call the channel editor window using the <span style="color: brown">Edit → Channel location</span> menu item, go to the last
channel and press the *Append* button. An empty channel is created.
Fill up the channel label (enter "Cz" in the *Channel label* edit box)
and enter the position of the channel if you have it. You may enter the X, Y, Z locations and press the *XYZ -→ Polar &
Sph.* to convert the 3-D Cartesian coordinates to polar and spherical
coordinates. In the channel
editor, references are placed after all the data channels (note that
the checkbox *Channel in data array* is unchecked since these are
not actual data channels associated with this electrode location).

If you do not have the electrode location, you may simply
press the *Look up locs* button to automatically look it up based on
the 10-20 channel label (note that this will look up the location of all
electrodes).

![Image:Pop_reref3.png](/assets/images/Pop_reref3.png)

Then press the *Set reference* pushbutton to set the reference to all
channels to Cz ("Cz" needs to be typed into the checkbox and the channel
range needs to be entered manually).

![Image:Pop_reref5.png](/assets/images/Pop_reref5.png)

Press OK to validate your new reference channel, close the channel editor window.

Now go back to the re-referencing interface using menu item <span style="color: brown">Tools → Re-reference the data</span>. Now click on the *Retain old reference* button and select the Cz electrode.

![Image:Pop_reref6.png](/assets/images/Pop_reref6.png)

Press OK. The re-referencing interface should look like the one below.

![Image:Pop_reref7.png](/assets/images/Pop_reref7.png)

Then press *Ok* to actually re-reference your data. Your data is now average referenced and you have added back Cz (the original reference) to the data. The reason for this overly complex procedure is that the reference
channel can have a location and that this location needs to be
declared in the channel editor so it can be plotted along with other
channels.

If you wanted to further re-reference your data to another reference (linked mastoid, for example), you may call the <span style="color: brown">Tools → Re-reference the data</span>  menu item again. 

Re-referencing to multiple electrodes
-------------------------
Say you collected data with reference M1 (mastoid) and want to process
your data using linked mastoid (M1 and M2) as reference. The process is
as follow:
-   Specify M1 as a reference channel as described in the previous section and
    compute average reference *while keeping electrode M1* (how to
    keep the reference channel is also described in the previous
    section)
-   Re-reference a second time the data selecting both electrodes M1 and
    M2 as reference (you may then either select to keep the reference
    channels or have them deleted)a

Re-reference at infinity
-------------------------
REST (Reference Electrode Standardization Technique) is a re-reference technique for translating multichannel EEG to a new dataset with reference at Infinity where the potential is zero/constant. It is implemented in the [REST](https://github.com/sccn/REST) EEGLAB plugin available on the EEGLAB plugin manager using the <span style="color: brown">File → Manage EEGLAB extension</span> menu item.