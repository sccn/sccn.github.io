---
layout: default
title: I.1 Loading Data in EEGLAB
permalink: /tutorials/single-subject/loading-data-in-EEGLAB
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
---

{ {Backward_Forward\|Getting_Started\|Introduction to
EEGLAB\|I.2:_Channel_Locations\|(MT) I.2: Channel Locations} }

Learning Matlab
---------------

The EEGLAB graphic interface is built on top of the powerful Matlab
scripting language. Enjoying the full capabilities of EEGLAB for
building macro commands and performing custom and automated processing
requires the ability to manipulate EEGLAB data structures in Matlab.
Because of time constraints, this wiki NOT provide an introduction to
the Matlab scripting language. Instead users need to familiarize
themselves with Matlab prior to the workshop. Users of Matlab 7: We
recommend running the following demos and reading the following help
sections.

In the Matlab help, you should perform the first 3 tutorials (Matlab
2018)

-   Getting Started with MATLAB
-   Language Fundamentals
-   Mathematics
-   Graphics (first section 2-D plot only)

Each section or demo (if read thoroughly) should take you about 40
minutes, for a total here of about 2 hours. We encourage you to read
these sections over several days.

Installing EEGLAB and tutorial files
------------------------------------

First download [EEGLAB (30MB)](http://sccn.ucsd.edu/eeglab/install.html)
which contains the tutorial dataset (also available [here
(4MB)](/Media:eeglab_data.set "wikilink") - *press the right mouse
button and select 'Save link as' if strange characters appear*).
When you uncompress EEGLAB you will obtain a folder named "eeglabxxxx"
(note: current version number 'xxxx' will vary). Under Windows, Matlab
usually recommends (although does not require) that you place toolboxes
in the *Application/MatlabRxxxx/toolbox/* folder (note: this name should
vary with the Matlab version 'xxxx'). In Linux, the Matlab toolbox
folder is typically located at */usr/local/pkgs/Matlab-rxxxx/toolbox/*
and in Mac in "/Application/MATLAB_Rxxxx". You may also place the folder
anywhere else on your path.

Starting Matlab and EEGLAB
--------------------------

Here we will start Matlab and EEGLAB. Note that paragraphs that begin
with <font color=green>KEY STEP</font> are necessary to what follows in
the tutorial. Paragraphs that begin with <font color=green>Exploratory
Step</font> are written to help you explore various EEGLAB features.

<font color=green>KEY STEP 1: </font>Start Matlab.

> WINDOWS: Go to Start, find Matlab and run it.
> Mac Option 1: Start from the Matlab icon in the dock or in the
> application folder.
> Linux: Open a terminal window and type "matlab" and hit enter.

<font color=green>KEY STEP 2:</font> Switch to the EEGLAB directory
(folder).

> You may browse for the directory by clicking on the button marked
> *"…"* in the upper right of the screen.


![800px]({{ site.baseurl }}/assets/images/Matlab_main_screen.png)


> This opens the window below. Double-click on a directory to enter it.
> Double-clicking on ".." in the folder list takes you up one level. Hit
> *OK* once you find the folder or directory you wish to be in.
> Alternatively, from the command line use "cd" (change directory) to
> get to the desired directory.

<font color=green>KEY STEP 3:</font> Start EEGLAB.

> Type "eeglab" at the Matlab command line and hit enter. EEGLAB will
> automatically add itself to the Matlab path.


![800px]({{ site.baseurl }}/assets/images/Matlab_command_line.png)


> The blue main EEGLAB window below should pop up, with its seven menu
> headings: <font color=brown>File, Edit, Tools, Plot, Study, Datasets,
> Help</font> arranged in typical (left-to-right) order of use.


![350px]({{ site.baseurl }}/assets/images/Eeglab20191.png)



<font color=green>Exploratory step (optional):</font> Add EEGLAB to the
Matlab path

> You may want to add the EEGLAB folder to the Matlab search path so the
> next time you start Matlab, you will be able able to open EEGLAB
> directly.
>
> If you started Matlab through its graphical interface, go to menu item
> <font color=brown>file</font> and select <font color=brown>set
> path</font>. This will open the following window.


[Image:Matlab set path
gui.png]({{ site.baseurl }}/assets/images/Matlab_set_path_gui.png)


>
> Or, if you are running Matlab from the command line, type "pathtool"
> and hit return; this will also call up this window.
>
> Click on the button marked *Add folder* and select the folder
> "eeglabxxxxx", then hit *OK* (EEGLAB will take care of adding its
> subfolder itself).
>
> Hit *save* in the pathtool window/ This will make the EEGLAB call-up
> function "eeglab" available in future Matlab sessions. Note that if
> you are installing a more recent version of EEGLAB, it is best to
> remove the old version from the Matlab path (select, then hit
> *Remove*) to avoid the possibility of calling up outdated routines. It
> is preferable NOT to add the "eeglab" path with its subfolder and let
> eeglab manage paths (when you start "eeglab", it automatically adds
> the path it needs.

Opening an existing dataset
---------------------------

<font color=green>KEY STEP 4:</font> Load the sample EEGLAB dataset.

> Select menu item <font color=brown>File</font> and press sub-menu item
> <font color=brown>Load existing dataset</font>.

In the rest of the tutorial, we will use the convention:
<font color=brown>Menu_item \> Submenu_item</font> to refer to a menu
selection (e.g., here select submenu item <font color=brown>Load
existing dataset</font> under the top-level
<font color=brown>File</font> submenu).

In Unix, the following window will pop up (the aspect ratio of this
window may differ in Windows and MacOS):




![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)



To learn how to create EEGLAB datasets from your own data, see the
tutorial on [Importing data and data
events](/A01:_Importing_Continuous_Epoched_Data "wikilink").

> Select the tutorial file "eeglab_data.set" which is distributed with
> the toolbox, located in the "sample_data" folder of EEGLAB (also
> available [here](/Media:eeglab_data.set "wikilink") - Press the right
> mouse button and select *Save link as" if strange characters
> appear*'). Then press *Open*.

When the dataset is loaded by EEGLAB, the main EEGLAB window shows
relevant information about it -- its number of channels, sampling rate,
etc...



![350px]({{ site.baseurl }}/assets/images/Eeglab_window_continuous_data.jpg)




Exploring event values
----------------------

In the tutorial dataset, the EEG.event structure fields *type*,
*position*, and *latency* are specified for each of the 154 events
marked in the dataset.

<font color=green>Exploratory Step:</font> Editing Event Values.

> Select menu <font color=brown>Edit \> Event Values</font> to call up a
> window where we can read and edit these values:


[Image:Figure pop
editeventvals3.png]({{ site.baseurl }}/assets/images/Figure_pop_editeventvals3.png)



Scroll through the events by pressing the **\>**, **\>\>**, **\<**, and
**\<\<** keys above.

We will now briefly describe the experiment that produced the sample
dataset to motivate the analysis steps we demonstrate in the rest of the
tutorial.

Sample experiment description
-----------------------------

In this experiment, there were two types of events "square" and "rt";
"square" events correspond to the appearance of a filled disk in a green
colored square in the display and "rt" to subject's button press. The
disk could be presented in any of the five squares on the screen, one
with green outline and the others blue, distributed along the horizontal
axis. Here we only considered presentation on the left, i.e. position 1
and 2 as indicated by the *position* field (at about 5.5 degree and 2.7
degree of horizontal visual angle respectively). In this experiment, the
subject covertly attended to a selected location on the computer screen
(the green square) and responded with a quick thumb button press only
when the disk was presented at this location. They were to ignore
circles presented at the unattended locations (the blue squares). To
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
extract epochs, plot reaction times, etc. The [Importing
data](/A02:_Importing_Event_Epoch_Info "wikilink") tutorial explains how
to import event information and define fields.

About this dataset
------------------

Here we describe how to edit and view the text field which describes the
current dataset, and is stored as a part of that dataset.

<font color=green>Exploratory Step:</font> Editing the Dataset
Description.

> Select <font color=brown>Edit \> About this dataset</font>. A
> text-editing window pops up which allows the user to edit a
> description of the current dataset. For the sample data, we entered
> the following description of the task. Press *SAVE* when done.


![Image:I15about_this_dataset.png]({{ site.baseurl }}/assets/images/I15about_this_dataset.png)




Scrolling through the data
--------------------------

Here we learn how to visualize and to reject selected portions of
continuous EEG channel data.

<font color=green>Exploratory Step:</font> Scrolling data.

> To scroll through the channel data of the current dataset, select
> <font color=brown>Plot \> Channel data (scroll)</font>. This pops up
> the [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m)
> the scrolling data display window below.
>
> Note that this sample data file contains as-if-continuous EEG data. To
> reduce (your) download time, this "pseudo-continuous" EEG dataset was
> actually constructed by concatenating eighty separate three-second
> data epochs (which we will later separate again). This explains some
> sudden jumps you may see in some data channels.


![Image:Scrollchannelactivities1.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities1.png)


> To the right of the plot window is the vertical scale value (and its
> unit, microvolts) that indicates the "amplitude" of the vertical scale
> bar. In this case, that value is 80 (microvolts). The same value is
> also shown in the lower right-hand edit box, where we can change it as
> explained below.

<font color=green>Exploratory Step:</font> Voltage Scale.

> Change the "Scale" edit-text box value to about 50, either by
> repeatedly clicking on the *"-"* button or by editing the text value
> from the keyboard, and press the *Enter* key to update the scrolling
> window.


![Image:Scrollchannelactivities2.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities2.png)


<font color=green>Exploratory Step:</font> Adjusting the width of the
scrolling time window.

> To adjust the time range displayed (i.e., the horizontal scale),
> select the
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) menu
> item <font color=brown>Settings \> Time range to display</font>, and
> set the desired window length to "10" seconds as shown below,


![Image:I16change_window_length.png]({{ site.baseurl }}/assets/images/I16change_window_length.png)




> Then press *OK* to make the indicated change take effect.


![Image:Scrollchannelactivities3.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities3.png)



<font color=green>Exploratory Step:</font> Number of Channels to
Display.

> To adjust the number of channels displayed, select
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) menu
> item <font color=brown>Settings \> Number of channels to
> display</font> and enter the desired number of channels to display in
> the screen (for instance "16").


![Image:I16chan_to_display.png]({{ site.baseurl }}/assets/images/I16chan_to_display.png)


> Reducing the number of channels shown will return a scrolling
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) window
> with a vertical channel-set slider to the left of the plot. Use it to
> scroll the display (vertically) through all the channels.


![Image:Scrollchannelactivities4.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities4.png)



<font color=green>Exploratory Step:</font> Zoom.

> To zoom in on a particular area of a data window, select
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) menu
> item <font color=brown>Settings \> Zoom off/on \> Zoom on</font>. Now
> using your mouse, drag a rectangle around an area of the data to zoom
> in on it. The scrolling window may now look similar to the one below.
> Click the right button on the mouse to zoom out again. Use menu item
> <font color=brown>Setting \> Zoom off/on \> Zoom off</font> to turn
> off the zoom option.


![Image:I16scroll_zoom.png]({{ site.baseurl }}/assets/images/I16scroll_zoom.png)



<font color=green>Exploratory Step:</font> Grid Lines.

> To display horizontal (x) and vertical (y) grid lines on the data,
> select <font color=brown>Display \> Grid \> X grid on</font> or
> <font color=brown>Display \> Grid \> Y grid on</font>. Repeat this
> process to turn off either set of grid lines.


![800px]({{ site.baseurl }}/assets/images/I16grid_scroll.png)


> The [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m)
> window also allows you to reject (erase) arbitrary portions of the
> continuous data. The function
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) can be
> called from both menu items <font color=brown>Plot \> Scroll
> data</font> and <font color=brown>Tools \> Reject continuous
> data</font> using the *REJECT* button on the bottom right corner.

<font color=green>Exploratory Step:</font> Rejecting Data.

> Close the current
> [eegplot()](http://sccn.ucsd.edu/eeglab/allfunctions/eegplot.m) window
> and select item <font color=brown>Tools \> Reject Continuous Data by
> eye</font> in the main EEGLAB window. A warning message appears; click
> on continue. To erase a selected portion of the data, first drag the
> mouse (holding down the left mouse button) horizontally across the
> time region of interest to mark it for rejection. If you like, mark
> multiple regions for rejection in this way. To undo a rejection mark,
> click once on the marked region.


![800px]({{ site.baseurl }}/assets/images/I16reject_scroll.png)


> Note: Zooming must be disabled to select a portion of the data.
>
> Now, to erase the marked data regions, click the (lower right)
> *REJECT* button (above). A new dataset will be created with the marked
> regions removed. Note: EEGLAB will also add new "rejection boundary"
> events to the new dataset event list and will link these events to
> added "rejection boundary" events in a backup copy of the experiment
> event record contained in the EEG.urevent structure. Rejection
> boundary events insure that subsequent epoch selections do not cross
> non-contiguous rejection boundaries. For more details about rejecting
> continuous data regions and data epochs, see the [data rejection
> tutorial](/Chapter_01:_Rejecting_Artifacts "wikilink").
>
> Click *OK* (below) to create the new dataset with the marked data
> portions removed.


![Image:I16pop_newset_after_reject.png]({{ site.baseurl }}/assets/images/I16pop_newset_after_reject.png)


> Press *OK* to create the new dataset. The EEGLAB main window now looks
> like:


![Image:I16change_datasets_2.png]({{ site.baseurl }}/assets/images/I16change_datasets_2.png)


> Since we only performed this rejection for illustrative purposes,
> switch back to the original dataset by selecting main window menu item
> <font color=brown>Datasets \> Dataset 1: Continous EEG data</font>.

<font color=green>Exploratory Step:</font> Deleting a Dataset from
Memory.

> To delete the newly created second dataset, select
> <font color=brown>File \> Clear dataset(s)</font> or
> <font color=brown>Edit \> Delete dataset(s)</font> and enter the
> dataset index, "2" as shown below, and press *OK*.


![Image:Delete.png]({{ site.baseurl }}/assets/images/Delete.png)


> The second dataset will now be removed from the EEGLAB/Matlab
> workspace. (Note: It is not necessary to switch back to the first
> dataset before deleting the second. It is also possible to delete
> several datasets at once from this window by entering their indices
> separated by spaces.)

{ {Backward_Forward\|Getting_Started\|Introduction to
EEGLAB\|I.2:_Channel_Locations\|(MT) I.2: Channel Locations} }
[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")
