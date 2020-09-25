---
layout: default
title: I.7 Selecting Data Epochs and Comparing
permalink: /tutorials/single-subject/I.7_Selecting_Data_Epochs_and_Comparing
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
---

{ {Backward_Forward\|I.6:_Data_Averaging\|(MT) I.6: Data
Averaging\|I.8:_Plotting_ERP_images\|(MT) I.8: Plotting ERP images} }

Selecting data epochs and plotting data averages
------------------------------------------------

#### Selecting events and epochs for two conditions

To compare event-related EEG dynamics for a subject in two or more
conditions from the same experiment, it is first necessary to create
datasets containing epochs for each condition. In the experiment of our
sample dataset, half the targets appeared at position 1 and the other
half at position 2 (see [sample experiment
description](/I.1:_Loading_Data_in_EEGLAB#Sample_experiment_description "wikilink")
).

<font color=green>Exploratory Step: </font>Selecting Events and Epochs
for Two Conditions.

> Select <font color=brown>Edit \> Select epochs or events</font>. The {
> {File\|pop_selectevent.m} } window (below) will appear. Enter "1" in
> the textbox next to *position*, which will select all epochs in which
> the target appeared in position 1.


![750px]({{ site.baseurl }}/assets/images/Pop_selectevent1_i7.jpg)


> Now a { {File\|pop_newset.m} } window for saving the new dataset pops
> up. We name this new dataset "Square, Position 1" and press *OK*.


![575px]({{ site.baseurl }}/assets/images/Pop_newset_i7.jpg)


> Now, repeat the process to create a second dataset consisting of
> epochs in which the target appeared at position 2. First, go back to
> the previous dataset by selecting menu item <font color=brown>
> Datasets \> Continuous EEG Data</font>. Make sure you work on the
> original continuous dataset or you will be able to extract data epochs
> at position 2. Next select <font color=brown> Edit \> Select
> epoch/events</font>. In the resulting { {File\|pop_selectevent.m} }
> window, enter "2" in the text box to the right of the *position*
> field. Press *OK*, then name the new dataset "Square, Position 2".


![750px]({{ site.baseurl }}/assets/images/Pop_selectevent2_i7.jpg)


> See the event tutorial, ["selecting
> events",](/I.03:_Event_Processing#Selecting_events "wikilink") for
> more details on this topic.
>
> Another function that can be useful for selecting a dataset subset is
> the function { {File\|pop_select.m} } called by selecting
> <font color=brown>Edit \> Select data</font>. The example below would
> select data sub-epochs with the epoch time range from -500 ms to 1000
> ms. It would, further, remove dataset epochs 2, 3 and 4 and remove
> channel 31 completely.


![525px]({{ site.baseurl }}/assets/images/Pop_select_i7.jpg)

