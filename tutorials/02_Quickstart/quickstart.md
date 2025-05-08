---
layout: default
title: 2. Quickstart
long_title: 2. Quickstart
categories: tutorial
parent: Tutorials
nav_order: 2
---
Quickstart guide
================

This page lets you import and visualize an EEG dataset. It is a way  to get started quickly.

Load the sample EEGLAB dataset
---------------------------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>.

In the rest of the tutorial, we will use the convention:
<span style="color: brown">Menu_item → Submenu_item</span> to refer to a menu
selection (e.g., here select submenu item <span style="color: brown">Load
existing dataset</span> under the top-level
<span style="color: brown">File</span> submenu).

In Unix, the following window will pop up (the aspect ratio of this
window may differ in Windows and MacOS):

![Image:Pop_loadset.png](/assets/images/Pop_loadset.png)

To learn how to create EEGLAB datasets from your data, see the
tutorial on [Importing data and data
events](/tutorials/04_Import/Importing_Continuous_and_Epoched_Data.html).

Select the tutorial file "eeglab_data.set", which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

After EEGLAB loads the dataset, the main EEGLAB window shows
relevant information about it -- its number of channels, sampling rate,
etc.

![](/assets/images/Eeglab_window_continuous_data.jpg)

Exploring event values
----------------------

In the tutorial dataset, the EEG.event structure fields *type*,
*position*, and *latency* are specified for each of the 154 events
marked in the dataset.

Select menu <span style="color: brown">Edit → Event Values</span> to call up a
window where we can read and edit these values:


![Image:Figure pop editeventvals3.png](/assets/images/Figure_pop_editeventvals3.png)



Scroll through each event by pressing the *\<* and *\>* buttons, or in steps of 10 using *\<\<*
and *\>\>*.


We will now briefly describe the experiment that produced the sample
dataset to motivate the analysis steps we demonstrate in the rest of the
tutorial.

About this dataset
------------------

Here we describe how to edit and view the text field, which describes the
current dataset and is stored as a part of that dataset.

Select <span style="color: brown">Edit → About this dataset</span>. A
text-editing window pops up, which allows the user to edit a
description of the current dataset. For the sample data, we entered
the following description of the task. Press *SAVE* when done.


![Image:I15about_this_dataset.png](/assets/images/I15about_this_dataset.png)

Scrolling through the data
--------------------------

Here we learn how to visualize and to reject selected portions of
continuous EEG channel data.

To scroll through the channel data of the current dataset, select
<span style="color: brown">Plot → Channel data (scroll)</span>. This pops up
the [eegplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m)
the scrolling data display window below.

![Image:Scrollchannelactivities1.png](/assets/images/Scrollchannelactivities1.png)
