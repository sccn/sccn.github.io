---
layout: default
title: I.7 Selecting Data Epochs and Comparing
permalink: /tutorials/single-subject/selecting-data-epochs-and-comparing
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 7
---


Selecting data epochs and Comparing 2 conditions
=================================================

Selecting events and epochs for two conditions
-----------------------------------------------
To compare event-related EEG dynamics for a subject in two or more
conditions from the same experiment, it is first necessary to [create
datasets containing epochs for each condition](/tutorials/single-subject/extracting-data-epochs). In the experiment of our
sample dataset, half the targets appeared at position 1 and the other
half at position 2 (see [sample experiment
description](/tutorials/single-subject/loading-data-in-EEGLAB.html#sample-experiment-description)
).

**Selecting events and epochs for two conditions**

Select <span style="color: brown">Edit → Select epochs or events</span>.
The { {File\|pop_selectevent.m} } window (below) will appear. 

Enter "1" in the textbox next to *position*, which will select all epochs in which the target appeared in position 1.

![px](/assets/images/Pop_selectevent1.jpg)


Press *Yes* in the resulting query window (below):


![300px](/assets/images/Query.gif)


Now a { {File\|pop_newset.m} } window for saving the new dataset pops up. We name this new dataset "Square, Position 1" and press *OK*.


![575px](/assets/images/Pop_newset2.gif)


Now, repeat the process to create a second dataset consisting of epochs in which the target appeared at position 2. 

First, go back to the previous dataset by selecting menu item <span style="color: brown> Datasets \> Continuous EEG Data</font>. Make sure you work on the original continuous dataset or you will be able to extract data epochs at position 2. Next select <font color=brown> Edit \"> Select epoch/events</span>. 

In the resulting { {File\|pop_selectevent.m} } window, enter "2" in the text box to the right of the *position* field. Press *OK*, then name the new dataset "Square, Position 2".


![5px](/assets/images/Pop_selectevent2.jpg)


See the event tutorial, ["selecting
events",](/tutorials/advanced-topics/event-processing#Selecting_events) for
more details on this topic.

**Select a subset of data epochs**

Another function that can be useful for selecting a dataset subset is the function { {File\|pop_select.m} } called by selecting <span style="color: brown>Edit \"> Select data</span>. The example below would select data sub-epochs with the epoch time range from -500 ms to 1000 ms. It would, further, remove dataset epochs 2, 3 and 4 and remove channel 31 completely.


![525px](/assets/images/Pop_select.gif)


Computing Grand Mean ERPs
---------------------------

Normally, ERP researchers report results on grand mean ERPs averaged
across subjects. As an example, we will use EEGLAB functions to compute
the ERP grand average of the two condition ERPs above.


Select <span style="color: brown>Plot → Sum/Compare ERPs</span>. In the top text-entry boxes of the resulting { {File\|pop_comperp.m} } window (below), enter the indices of datasets ‘3’ and ‘4’. On the first row, click the *avg.* box to display grand average, the *std.* box to display standard deviation, and the *all ERPs* box to display ERP averages for each dataset. Finally *0.05* for the t-test significance probability (p) threshold. Then press *OK*.

![575px](/assets/images/I72pop_comperp().gif)


The plot below appears.


![450px](/assets/images/Pop_comperp3.gif)


Now, click on the traces at electrode position *FPz*, calling up the image below. You may remove the legend by deselecting it under the <span style="color: brown>Insert \"> Legend</span> menu.


![450px](/assets/images/Pop_comperp4.gif)

*Note*: If you prefer to use positive up view for the y-axis scale, type
*ydir', 1* in the *Plottopo options* field. This can be set as a global
or project default in *icadefs.m*. See the [Options tutorial](/A3:_Maximizing_Memory "wikilink").

The ERPs for datasets 3 and 4 are shown in blue and red. 

The grand
average ERP for the two conditions is shown in bold black, and the
standard deviation of the two ERPs in dotted black.
 
Regions
significantly different from 0 are highlighted based on a two-tailed
t-test at each time point. 

This test compares the current ERP value
distribution with a distribution having the same variance and a 0 mean.

Note that this t-test has not been corrected for multiple comparisons.
The p values at each time point can be obtained from a command line call
to the function { {File\|pop_comperp.m} }.

Finding ERP peak latencies
--------------------------------

Although EEGLAB currently does not have tools for automatically finding
ERP peak amplitudes and latencies, one can use the convenient Matlab
zoom facility to visually determine the exact amplitude and latency of a
peak in any Matlab figure.

For example, in the figure above select the magnifying-glass icon having the **+** sign. Then, zoom in on the main peak of the red curve as shown below (click on the left mouse button to zoom in and on the right button to zoom out). Read the peak latency and amplitude to any desired precision from the axis scale.


![475px](/assets/images/Pop_comperp5.gif)



*Note*: It may be desirable to first use the low pass filtering edit box
of the { {File\|pop_comperp.m} } interface to smooth average data peaks
before measuring latency peaks.

Comparing ERPs in two conditions
---------------------------------

To compare ERP averages for the two conditions (targets presented in positions 1 and 2):
 - select <span style="color: brown">Plot → Sum/Compare ERPs</span> 
 - in the top text-entry box of the resulting { {File\|pop_comperp.m} } window (below), enter the indices of the
  datasets to compare. 
 - click all boxes in the *avg.* column. 
 - enter *30* for the low pass frequency and '' 'title', 'Position 1-2' '' in the { {File\|topoplot.m} } option edit box. 
 - then press *OK*.


![500px](/assets/images/Pop_comperp6.gif)


The { {File\|plottopo.m} } figure (below) appears.


![475px](/assets/images/Pop_comperp7.gif)


Again, individual electrode traces can be plotted in separate windows by clicking on electrode locations of interest in the figure (above). 

Note that here, since the two conditions are similar (only the position of the stimulus on the screen changes), the ERP difference is close to 0.


![475px](/assets/images/Pop_comperp8.gif)


Working with multiple datasets
-------------------------------
When working with multiple datasets, EEGLAB uses the STUDY data structure to aggregate and process datasets from multiple subjects,
sessions, and/or conditions. You can learn more about STUDY and multiple subject processing in [part II](/tutorials/multi-subject/overview.html) 
of this tutorial. 

Next step 
-----------

In the following sections, we will be working from the dataset 2
only, and will not use datasets 3 and 4. Return dataset 2
using the <span style="color: brown">Datasets</span> top menu, and optionally
delete datasets numbers 3 and 4 using <span style="color: brown">File → Clear dataset(s)</span>.

Data averaging collapses the dynamic information in the data, ignoring
inter-trial differences which are large and may be crucial for
understanding how the brain operates *in real time*. In the next
section, we show how to use EEGLAB to make 2-D ERP-image plots of
collections of single trials, sorted by any of many possibly relevant
variables. 
