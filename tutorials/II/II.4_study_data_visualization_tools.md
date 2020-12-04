---
layout: default
title: II.4 STUDY Data Visualization Tools
permalink: /tutorials/multi-subject/STUDY-data-visualization-tools.html
parent: II.Multiple subject processing tutorial
grand_parent: Tutorials 
---

{ {Backward_Forward\|Chapter 03: Working with STUDY designs\|Chapter 03:
Working with STUDY designs\|Chapter 05: Component Clustering
Tools\|Chapter 05: Component Clustering Tools\|} }

<u>Description of experiment for this part of the tutorial:</u> These
data were acquired by Arnaud Delorme and colleagues from fourteen
subjects. Subjects were presented with pictures that either contained or
did not contain animal image. Subjects respond with a button press
whenever the picture presented contained an animal. These data are
available for download [here](ftp://sccn.ucsd.edu/pub/animal_study.zip)
(380 Mb). A complete description of the task, the raw data (4Gb), and
some Matlab files to process it, are all available
[here](http://www.sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html).

We have used these data in the following two sections since the released
cluster tutorial data used in previous sections are too sparse to allow
computing statistical significance. However, for initial training, you
might better use that much smaller example STUDY.

__TOC__

### Precomputing channel measures

Before plotting the component distance measures, you must precompute
them using the <font color=brown>Study \> Precompute measures</font>
menu item as shown below.


![px](/assets/images/Pop_precomp.jpg)



It is highly recommended that for visualizing and computing statistics
on data channels you first interpolate missing channels. Automated
interpolation in EEGLAB is based on channel names. If datasets have
different channel locations (for instance if the locations of the
channels were scanned), you must interpolate missing channels for each
dataset from the command line using { {File\|eeg_interp.m} }. Select all
the measures above, or just one if you want to experiment. The channel
ERPs have been included in the tutorial dataset; if you select ERPs,
they will not be recomputed -- unless you also check the box ''
Recompute even if present on disk''.

Each measure to precompute is explained in detail in the component
clustering part (where the same exact measures may be computed).

### Plotting channel measures

After precomputing the channel measures, you may now plot them, using
menu item <font color=brown>Study \> Plot channel measures</font>.


![600px](/assets/images/Pop_chanplot.gif)\]



Here we only illustrate the behavior of { {File\|pop_chanplot.m} } for
plotting ERPs. Spectral and time/frequency (ERSP/ITC) measure data for
scalp channels may be plotted in a similar manner, as shown in the
previous section on component clustering. To plot data for a single
scalp channel ERP, press the *Plot ERPs* pushbutton on the left column.
A plot like the one below should appear:



![\![image not found](/assets/images/Erp1.gif)\]



You may plot all subjects ERPs by pressing the *Plot ERPs* pushbutton in
the left columns, obtaining a figure similar to the one below.



![\![image not found](/assets/images/Erp2.gif)\]



Finally, you may also plot all scalp channels simultaneously. To do
this, simply click the push button *Sel. all* to select all data
channels. Then again press the *Plot ERPs* button in the right column.



![\![image not found](/assets/images/Erp3.gif)\]



Clicking on individual ERPs will make a window plotting the selected
channel ERP pop up. Many other plotting options are available in the
central column of the { {File\|pop_chanplot.m} } gui. These will be
described in the next section.
More complex plotting options are demonstrated in the section dealing
with [visualization and
statistics](/Chapter_06:_Study_Statistics_and_Visualization_Options "wikilink").
