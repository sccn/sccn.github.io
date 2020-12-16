---
layout: default
title: a. Manual rejection
categories: artifact
parent: 6. Reject artifacts
grand_parent: Tutorials
---
Scrolling and rejecting data 
--------------------------

Here we learn how to visualize and to reject selected portions of
continuous EEG channel data.

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

### Scrolling data

To scroll through the channel data of the current dataset, select
<span style="color: brown">Plot → Channel data (scroll)</span>. This pops up
the [eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m)
the scrolling data display window below.

Note that this sample data file contains as-if-continuous EEG data. To
reduce (your) download time, this "pseudo-continuous" EEG dataset was
actually constructed by concatenating eighty separate three-second
data epochs (which we will later separate again). This explains some
sudden jumps you may see in some data channels.


![Image:Scrollchannelactivities1.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities1.png)


To the right of the plot window is the vertical scale value (and its
unit, microvolts) that indicates the "amplitude" of the vertical scale
bar. In this case, that value is 80 (microvolts). The same value is
also shown in the lower right-hand edit box, where we can change it as
explained below.

### Voltage Scale

Change the "Scale" edit-text box value to about 50, either by
repeatedly clicking on the *"-"* button or by editing the text value
from the keyboard, and press the *Enter* key to update the scrolling
window.


![Image:Scrollchannelactivities2.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities2.png)


### Adjusting the width of the scrolling time window

To adjust the time range displayed (i.e., the horizontal scale),
select the [eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) menu
item <span style="color: brown">Settings → Time range to display</span>, and
set the desired window length to "10" seconds as shown below,


![Image:I16change_window_length.png]({{ site.baseurl }}/assets/images/I16change_window_length.png)




Then press *OK* to make the indicated change take effect.


![Image:Scrollchannelactivities3.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities3.png)



### Number of Channels to Display

To adjust the number of channels displayed, select
[eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) menu
item <font color=brown>Settings → Number of channels to
display</font> and enter the desired number of channels to display in
the screen (for instance "16").


![Image:I16chan_to_display.png]({{ site.baseurl }}/assets/images/I16chan_to_display.png)


Reducing the number of channels shown will return a scrolling
[eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) window
with a vertical channel-set slider to the left of the plot. Use it to
scroll the display (vertically) through all the channels.


![Image:Scrollchannelactivities4.png]({{ site.baseurl }}/assets/images/Scrollchannelactivities4.png)



### Zoom on data

To zoom in on a particular area of a data window, select
[eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) menu
item <span style="color: brown>Settings → Zoom off/on \"> Zoom on</span>. Now
using your mouse, drag a rectangle around an area of the data to zoom
in on it. The scrolling window may now look similar to the one below.
Click the right button on the mouse to zoom out again. Use menu item
<span style="color: brown>Setting → Zoom off/on \"> Zoom off</span> to turn
off the zoom option.


![Image:I16scroll_zoom.png]({{ site.baseurl }}/assets/images/I16scroll_zoom.png)



### Grid Lines

To display horizontal (x) and vertical (y) grid lines on the data,
select <span style="color: brown>Display → Grid \"> X grid on</span> or
<span style="color: brown>Display → Grid \"> Y grid on</span>. Repeat this
process to turn off either set of grid lines.


![800px]({{ site.baseurl }}/assets/images/I16grid_scroll.png)


The [eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m)
window also allows you to reject (erase) arbitrary portions of the
continuous data. The function
[eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) can be
called from both menu items <font color=brown>Plot → Scroll
data</font> and <font color=brown>Tools → Reject continuous
data</font> using the *REJECT* button on the bottom right corner.


### Rejecting Data

Close the current
[eegplot()](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) window
and select item <font color=brown>Tools → Reject Continuous Data by
eye</font> in the main EEGLAB window. A warning message appears; click
on continue. 

To erase a selected portion of the data, first drag the
mouse (holding down the left mouse button) horizontally across the
time region of interest to mark it for rejection. If you like, mark
multiple regions for rejection in this way. To undo a rejection mark,
click once on the marked region. 

![800px]({{ site.baseurl }}/assets/images/I16reject_scroll.png)

Note: Zooming must be disabled to select a portion of the data.

Note: To select portions of data that extend out of the plotting window,
simply drag the mouse over the new region and connect it to a previously
marked region. For instance, in the following plotting window which
already had the time interval 2.1 seconds to 3.4 seconds selected (as
shown above), drag the mouse from 6.9 seconds back to 4.7.

Note: To *deselect* a portion of the data, simply click on the selected region.
This allows re-inspection of the data portions marked for rejection in
two or more passes, e.g., after the user has developed a more consistent
rejection strategy or threshold. 

![575px](/assets/images/Iii1eegplot2.jpg)

After marking some portions of the data for
rejection, press *REJECT* and a new data set will be created with the
rejected data omitted. A new dataset will be created with the marked
regions removed. 

Click *OK* (below) to create the new dataset with the marked data
portions removed.

![Image:I16pop_newset_after_reject.png]({{ site.baseurl }}/assets/images/I16pop_newset_after_reject.png)

Press *OK* to create the new dataset. The EEGLAB main window now looks
like:

![Image:I16change_datasets_2.png]({{ site.baseurl }}/assets/images/I16change_datasets_2.png)


EEGLAB adjust the *EEG.event* structure
fields and insert *boundary* events where data has been rejected,
with a duration field holding the duration of the data portion that was
rejected. EEGLAB will also link these events in a backup copy of the experiment
event record contained in the *EEG.urevent* structure. Rejection
boundary events insure that subsequent epoch selections do not cross
non-contiguous rejection boundaries. Thus, rejection on continuous data
must be performed 'before' separating it into data epochs. To plot the data with the *boundary* event use menu item <span style="color: brown">Plot → Channel data (scroll)</span> on the new dataset as shown below (the thick red event mark is a boundary event).

![575px](/assets/images/Iii1eegplot1.jpg)

Since we only performed this rejection for illustrative purposes,
you may switch back to the original dataset by selecting main window menu item
<span style="color: brown">Datasets → Dataset 1: Continous EEG data</span>.

##### Rejecting data by visual inspection







