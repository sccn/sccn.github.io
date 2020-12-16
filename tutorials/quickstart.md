---
layout: default
title: 2. Quickstart
categories: tutorial
parent: Tutorials
---

Opening an existing dataset
---------------------------

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

To learn how to create EEGLAB datasets from your own data, see the
tutorial on [Importing data and data
events](/A01:_Importing_Continuous_Epoched_Data "wikilink").

Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

When the dataset is loaded by EEGLAB, the main EEGLAB window shows
relevant information about it -- its number of channels, sampling rate,
etc.



![350px]({{ site.baseurl }}/assets/images/Eeglab_window_continuous_data.jpg)




Exploring event values
----------------------

In the tutorial dataset, the EEG.event structure fields *type*,
*position*, and *latency* are specified for each of the 154 events
marked in the dataset.

### Editing Event Values

Select menu <span style="color: brown">Edit → Event Values</span> to call up a
window where we can read and edit these values:


![Image:Figure pop editeventvals3.png]({{ site.baseurl }}/assets/images/Figure_pop_editeventvals3.png)



Scroll through each event by pressing the *\<* and *\>* buttons, or in steps of 10 using *\<\<*
and *\>\>*.


We will now briefly describe the experiment that produced the sample
dataset to motivate the analysis steps we demonstrate in the rest of the
tutorial.

Sample experiment description
-----------------------------

In this experiment, there were two types of events "square" and "rt";
"square" events correspond to the appearance of a filled disk in a green
colored square in the display and "rt" to subject's button press. 

The disk could be presented in any of the five squares on the screen, one
with green outline and the others blue, distributed along the horizontal
axis. Here we only considered presentation on the left, i.e. position 1
and 2 as indicated by the *position* field (at about 5.5 degree and 2.7
degree of horizontal visual angle respectively). 

In this experiment, the
subject covertly attended to a selected location on the computer screen
(the green square) and responded with a quick thumb button press only
when the disk was presented at this location. They were to ignore
circles presented at the unattended locations (the blue squares). 

To
reduce the amount of data required to download and process, this dataset
contains only targets (i.e., "square") stimuli presented at the two
left-visual-field attended locations for a single subject. For more
details about the experiment see [Makeig, et al., Science, 2002,
295:690-694](http://sccn.ucsd.edu/science2002.html).

When using events in an EEGLAB dataset, there are two required event
fields: *type* and *latency*, plus any number of additional user-defined
information fields. It is important to understand here that the names of
the fields were defined by the user creating the dataset, and that it is
possible to create, save, and load as many event fields as desired.

Note also that *type* and *latency* (lowercase) are two keywords
explicitly recognized by EEGLAB and that these fields *must* be defined
by the user unless importing epoch event information (Note: If only
field *latency* is defined, then EEGLAB will create field *type* with a
constant default value of 1 for each event). Unless these two fields are
defined, EEGLAB will not be able to handle events appropriately to
extract epochs, plot reaction times, etc. The [ INSERT LINK ON Importing
data TUTORIAL]() tutorial explains how
to import event information and define fields.

[//]: # (TODO: insert proper link for reference to future tutorial pages)

About this dataset
------------------

Here we describe how to edit and view the text field which describes the
current dataset, and is stored as a part of that dataset.

**Editing the Dataset Description**

Select <span style="color: brown">Edit → About this dataset</span>. A
text-editing window pops up which allows the user to edit a
description of the current dataset. For the sample data, we entered
the following description of the task. Press *SAVE* when done.


![Image:I15about_this_dataset.png]({{ site.baseurl }}/assets/images/I15about_this_dataset.png)

Scrolling through the data
--------------------------

Here we learn how to visualize and to reject selected portions of
continuous EEG channel data.

**Scrolling data**

To scroll through the channel data of the current dataset, select
<span style="color: brown">Plot → Channel data (scroll)</span>. This pops up
the [eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m)
the scrolling data display window below.

![Image:Scrollchannelactivities1.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities1.png)
