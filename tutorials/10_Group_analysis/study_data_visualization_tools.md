---
layout: default
title: d. Data visualisation
parent: 10. Group analysis
grand_parent: Tutorials 
---

Visualizing channel data
========================


Load the sample EEGLAB STUDY set
---------------------------------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing study</span>. Select the tutorial file "n400clustedit.study" then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/pop_loadstudy.png)





#### Description of experiment for this part of the tutorial

These data were acquired by Arnaud Delorme and colleagues from fourteen
subjects. Subjects were presented with pictures that either contained or
did not contain animal images. Subjects respond with a button press
whenever the picture presented contained an animal. These data are
available for download [here](ftp://sccn.ucsd.edu/pub/animal_study.zip)
(380 Mb). A complete description of the task, the raw data (4Gb), and
some Matlab files to process it, are all available
[here](http://www.sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html).

We have used these data in the following two sections since the released
cluster tutorial data used in previous sections are too sparse to allow
computing statistical significance. However, for initial training, you
might better use that much smaller example STUDY.


Precomputing channel measures
------------------------------
Before plotting the channel measures, you must precompute
them using the <span style="color: brown">Study → Precompute measures</span>
menu item as shown below.


![px](/assets/images/pop_precomp.png)

This menu is in 2 parts: 
- **Precompute channel measures for STUDY ...**

Lets you specify behaviours that will then be applied to any channel 
  measure you precompute

It is highly recommended that for visualizing and computing statistics
on data channels you first interpolate missing channels.
 
Automated interpolation in EEGLAB is based on channel names. If datasets have
different channel locations (for instance if the locations of the
channels were scanned), you must interpolate missing channels for eachdataset from the command line using [eeg_interp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_interp.m). 


- **List of measures to precompute**

Tick the box and complete the parameters for the measure(s) you are interested in. 
 The channel ERPs have been included in the tutorial dataset; if you select ERPs,
they will not be recomputed -- unless you also check the box ''Overwrites files on disk''.
Here is the full list of measures you can compute:

- *ERPs:* computes mean event related potential for each condition and electrode. Specify the baseline you wish to use.

- *Power spectrum*: performs spectral decomposition for each condition and electrode. You can enter here specific parameters  for the  [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) function.

- *ERP-image*: computes the ERP-image. 
- *ERPs*/ *ITCs*:  
  The last two checkboxes allow computing
    event-related spectral perturbation in the form of
    event-related spectral power changes (ERSPs), and event-related
    phase consistencies (ITCs) for each condition. 
    To compute the ERSP and/or ITC measures, several time/frequency parameters are required.    To choose these values, you may enter the relevant [timefreq.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=timefreq.m) keywords and arguments in the text box. You may

    for instance enter '' 'alpha', 0.01'' for significance masking. See    the [timefreq.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=timefreq.m) help message for information about

    time/frequency parameters to select.  
    
    
Finally, the [pop_precomp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_precomp.m) gui allows you to choose to recompute the measures even if they already exist (overwrites

files on disk).



Visualizing channel data measures
-----------------------

After precomputing the channel measures, you may now plot them, using
menu item <span style="color: brown">Study → Plot channel measures</span>.


![600px](/assets/images/pop_chanplot.png)


All the measures described below, once computed, can be used
for channel data visualization.
In thecentral column of the [pop_chanplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanplot.m) gui, press *Params* next to the measure you wish to plot. 

Once you entered the desired parameters, press *OK* to exit the *Params* window then on the [pop_chanplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanplot.m) gui select the channel(s) (left handside) or subject(s) (right handside) you wish to plot

and press the corresponding "Plot XXX" measure.

-   **ERPs:** *ERP plotting options* lets you specify the time range and scale. 
*Multiple channels selection* gives you the choice of:
    - plotting individual channels
    - plotting the average topography over a time range (specified in the top box)
    - plotting the ERP measure averaged over a subset of channels
    - compute the root mean square (RMS) of the selected channels - this is equivalent to computing the 
    Globla Field Power (GFP)

-   **Spectra:** the menu is similar to the ERP's menu with the difference that
    the top box lets you specify the frequency range you wish to plot.     
    
- **ERPimage**: specifiy a time range and channel plotting options

- **ERSPs** / **ITCs** : these 2 measures share the same menu. You can specify and time and frequency range as well as power and ITC limits. 
 



Example - Plotting channel measures
----------------------------

Here we illustrate the behavior of [pop_chanplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_chanplot.m) for

plotting ERPs. Spectral and time/frequency (ERSP/ITC) measure data for
scalp channels may be plotted in a similar manner.

To plot data for a single
scalp channel ERP, press the *Plot ERPs* pushbutton on the left column.
A plot like the one below should appear:



![ERP](/assets/images/Erp1.gif)



You may plot all subjects ERPs by pressing the *Plot ERPs* pushbutton in
the left columns, obtaining a figure similar to the one below.



![ERP](/assets/images/Erp2.gif)



Finally, you may also plot all scalp channels simultaneously. To do
this, simply click the push button *Sel. all* to select all data
channels. Then again press the *Plot ERPs* button in the right column.



![ERP](/assets/images/Erp3.gif)



Clicking on individual ERPs will make a window plotting the selected
channel ERP pop up. 

