---
layout: default
title: II.4 STUDY Channel Data Visualization Tools
parent: II.Multiple subject processing tutorial
grand_parent: Tutorials 
---

STUDY data visualization tools
================================

#### Description of experiment for this part of the tutorial

These data were acquired by Arnaud Delorme and colleagues from fourteen
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


Precomputing channel measures
------------------------------
Before plotting the channel measures, you must precompute
them using the <span style="color: brown">Study → Precompute measures</span>
menu item as shown below.


![px](/assets/images/pop_precomp.png)



It is highly recommended that for visualizing and computing statistics
on data channels you first interpolate missing channels.
 
 Automated
interpolation in EEGLAB is based on channel names. If datasets have
different channel locations (for instance if the locations of the
channels were scanned), you must interpolate missing channels for each
dataset from the command line using { {File\|eeg_interp.m} }. 

Select all
the measures above, or just one if you want to experiment. The channel
ERPs have been included in the tutorial dataset; if you select ERPs,
they will not be recomputed -- unless you also check the box ''
Recompute even if present on disk''.

Each measure to precompute is explained in detail in the [component
clustering part]( /tutorials/multi-subject/component-clustering-tools.html) (where the same exact measures may be computed).

// Work in progress !!

-   **Spectra:** The first checkbox in the middle right of the
    pre-clustering window (above) allows you to include the log mean
    power spectrum for each condition in the pre-clustering measures.
    Clicking on the checkbox allow you to enter power spectral
    parameters. In this case, a frequency range \[lo hi\] (in Hz) is
    required. 
    
    Note that for clustering purposes (but not for display),
    for each subject individually, the mean spectral value (averaged
    across all selected frequencies) is subtracted from all selected
    components, and the mean spectral value at each frequency (averaged
    across all selected components) is subtracted from all components.
    The reason is that some subjects have larger EEG power than others.
    If we did not subtract the (log) means, clusters might contain
    components from only one subject, or from one type of subject (e.g.,
    women, who often have thinner skulls and therefore larger EEG than
    men).
    
-   **ERPs:** The second checkbox computes mean ERPs for each condition.
    Here, an ERP latency window \[lo hi\] (in ms) is required.
    
-   **Dipole locations:** The third checkbox allows you to include component
    equivalent dipole locations in the pre-clustering process. Dipole
    locations (shown as \[x y z\]) automatically have three dimensions
    
    *Note:* It is not yet possible to cluster on dipole orientations. 
    
    As mentioned above, the equivalent dipole model for each component and
    dataset must already have been pre-computed. If one component is
    modeled using two symmetrical dipoles, { {File\|pop_preclust.m} }
    will use the average location of the two dipoles for clustering
    purposes (Note: this choice is not optimum).
    
-   **Scalp maps:** The fourth checkbox allows you to include scalp map
    information in the component 'cluster location'. You may choose to
    use raw component map values, their laplacians, or their spatial
    gradients. 
    
    *Note*: We have obtained fair results for main components
    using laplacian scalp maps, though there are still better reasons to
    use equivalent dipole locations instead of scalp maps. 
    
    You may also
    select whether or not to use only the absolute map values, their
    advantage being that they do not depend on (arbitrary) component map
    polarity. As explained in the { {File\|ICA_decomposition.m} }, ICA
    component scalp maps themselves have no absolute scalp map polarity.
    
-   **ERSPs and/or ITCs:** The last two checkboxes allow including
    event-related spectral perturbation information in the form of
    event-related spectral power changes (ERSPs), and event-related
    phase consistencies (ITCs) for each condition. 
    To compute the ERSP
    and/or ITC measures, several time/frequency parameters are required.
    To choose these values, you may enter the relevant {
    {File\|timefreq.m} } keywords and arguments in the text box. You may
    for instance enter '' 'alpha', 0.01'' for significance masking. See
    the { {File\|timefreq.m} } help message for information about
    time/frequency parameters to select.
    
-   **Final number of dimensions:** An additional checkbox at the bottom
    allows further reduction of the number of dimensions in the
    component distance measure used for clustering. Clustering
    algorithms may not work well with measures having more than 10 to 20
    dimensions. 
    
    For example, if you selected all the options above and
    retained all their dimensions, the accumulated distance measures
    would have a total of 53 dimensions. This number may be reduced
    (e.g., to a default 10) using the PCA decomposition invoked by this
    option. Note that, since this will distort the cluster location
    space (projecting it down to its smaller dimensional 'shadow'), it
    is preferable to use this option carefully. For instance, if you
    decide to use reduced-dimension scalp maps and dipole locations that
    together have 13 dimensions (13 = the requested 10 dimensions for
    the scalp maps plus 3 for the dipole locations), you might
    experiment with using fewer dimensions for the scalp maps (e.g., 7
    instead of 10), in place of the final dimension reduction option (13
    to 10).


- Finally, the { {File\|pop_preclust.m} } gui allows you to choose to save
the updated *STUDY* to disk.


In the { {File\|pop_preclust.m} } select all methods and leave all
default parameters (including the dipole residual variance filter at the
top of the window), then press *OK*. As explained below, for this
tutorial STUDY, measure values are already stored on disk with each
dataset, so they need not be recomputed, even if the requested
clustering limits (time, frequency, etc.) for these measured are
reduced.








Plotting channel measures
----------------------------
After precomputing the channel measures, you may now plot them, using
menu item <span style="color: brown">Study → Plot channel measures</span>.


![600px](/assets/images/pop_chanplot.png)



Here we only illustrate the behavior of { {File\|pop_chanplot.m} } for
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




Channel data measures
-----------------------
All the measures described below, once computed, can be used
for channel data visualization.
In the
central column of the { {File\|pop_chanplot.m} } gui, press *Params* next to the measure you wish to plot. 
Once you entered the desired parameters, press *OK* to exit the *Params* window then on the 
{ {File\|pop_chanplot.m} } gui select the channel(s) (left handside) or subject(s) (right handside) you wish to plot
and press the corresponding "Plot XXX" measure.

-   **ERPs:** *ERP plotting options* lets you specify the time range and scale. 
*Multiple channels selection* gives you the choice of:
- plotting individual channels
- plotting the average topography over a time range (specified in the top box)
- plotting the ERP measure averaged over a subset of channels
- compute the root mean square (RMS) of the selected channels     

-   **Spectra:** the menu is similar to the ERP's menu with the difference that
    the top box lets you specify the frequency range you wish to plot.     
    
- **ERPimage**

- **ERSPs**
- **ITCs** 
 

   


In the { {File\|pop_preclust.m} } select all methods and leave all
default parameters (including the dipole residual variance filter at the
top of the window), then press *OK*. As explained below, for this
tutorial STUDY, measure values are already stored on disk with each
dataset, so they need not be recomputed, even if the requested
clustering limits (time, frequency, etc.) for these measured are
reduced.








More complex plotting options are demonstrated in the section dealing
with [visualization and statistics](/tutorials/multi-subject/study-statistics-and-visualization-options.html).
