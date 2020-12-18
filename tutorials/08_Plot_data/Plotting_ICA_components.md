---
layout: default
title: e. ICA components
parent: 8. Plot data
grand_parent: Tutorials
---
Working with ICA components
================================



Plotting component spectra and maps
-----------------------------------

It is of interest to see which components contribute most strongly to
which frequencies in the data. To do so, select <span style="color: brown">Plot → Component spectra and maps</span>. 
This calls [pop_spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_spectopo.m). 

Its first input is the epoch time range to
consider, the fourth is the percentage of the data to sample at random
(smaller percentages speeding the computation, larger percentages being
more definitive). 

Since our EEG dataset is fairly small, we choose to
change this value to *100* (= all of the data). 

We will then visualize
which components contribute the most at 10 Hz, entering *10* in the
*Scalp map frequency* text box. 

We simply scan all components, the
default in *Components to consider*. Press *OK*.



![525px]({{ site.baseurl }}/assets/images/Channelspectraedit.gif)



The [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) window (below) appears.




![425px]({{ site.baseurl }}/assets/images/Spectopocomps.gif)



In the previous window, we plotted the spectra of each component.
 
A more
accurate strategy is to plot the data signal
minus the component activity and estimate the decrease in power in
comparison to the original signal at one channel - it is also possible to
do this at all channel but it requires to compute the spectrum of the
projection of each component at each channel which is computationally
intensive. 

To do so, go back to the previous interactive window:
 - choose explicitly to plot component's contribution at channel *27* (POz) where
power appears to be maximum at *10* Hz using the *Electrode number to
analyze ...:* field, 
- uncheck the checkbox *\[checked\] compute component
spectra...*. 
- set percent to *100* as before.
- display *6*
component maps instead of 5 (default) (note that all component spectra
will be shown) 
- set the maximum frequency to be plotted at
*30* Hz using the *Plotting frequency range* option in the bottom panel
(below). 
- Press *OK* when done.


![525px]({{ site.baseurl }}/assets/images/Channelspectraedit1.gif)



The [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) figure appears (as below).


![425px]({{ site.baseurl }}/assets/images/I102spectopo.jpg)




The following text is displayed

    Component 1 percent variance accounted for: 3.07
    Component 2 percent variance accounted for: 3.60
    Component 3 percent variance accounted for: -0.05
    Component 4 percent variance accounted for: 5.97
    Component 5 percent variance accounted for: 28.24
    Component 6 percent variance accounted for: 6.15
    Component 7 percent variance accounted for: 12.68
    Component 8 percent variance accounted for: -0.03
    Component 9 percent variance accounted for: 5.04
    Component 10 percent variance accounted for: 52.08
    Component 11 percent variance accounted for: 0.79
    ....


*"Percent variance acounted for"* (pvaf) compares the variance of the data
MINUS the (back-projected) component to the variance of the whole data.

Thus, if one component accounts for all the data, the data minus the
component back-projection will be 0, and pvaf will be 100%.
 
 If the
component has zero variance, it accounts for none of the data and pvaf =
0%. 

If a component somehow accounts for the NEGATIVE of the data,
however, pvaf will be larger than 100% (meaning: "If you remove this
component, the data actually get larger, not smaller!"). 

According to
the variance accounted for output above, component 10 accounts for more
than 50% of power at 10 Hz for channel POz. Note: A channel number has
to be entered otherwise component contributions are not computed.

Plotting component ERPs
-----------------------

After seeing which components contribute to frequency bands of interest,
it is interesting to look at which components contribute the most to the
ERP.
 
A first step is to view the component ERPs. To Plot component ERPs,
select <span style="color: brown">Plot → Component ERPs → In rectangular array</span>, which calls function [pop_plotdata.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file
=pop_plotdata.m). Then
press *OK*.


![325px]({{ site.baseurl }}/assets/images/Rectarrayedit.gif)



The [plotdata.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=plotdata.m) window below pops up, showing the average ERP
for all 31 components.


![425px]({{ site.baseurl }}/assets/images/I103pop_plotdata.jpg)



Click on the component-1 trace (above) to plot this trace in new window
(as below).


![425px]({{ site.baseurl }}/assets/images/I103single_plotdata.jpg)



As for electrodes, use menu <span style="color: brown">Plot → Sum/Compare comp. ERPs</span> to plot component ERP differences accross multiple
datasets.

Plotting component ERP contributions
------------------------------------

To plot the contribution of component ERPs to the data ERP, select
<span style="color: brown">Plot → Component ERPs → with component maps</span>,
which calls [pop_envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_envtopo.m). 

Simply press *OK* to plot the 7
components that contribute the most to the average ERP of the dataset.

Note that artifactual components can be subtracted from the data prior to
plot the ERP using the *Indices of component to subtract ...* edit
box.


![475]({{ site.baseurl }}/assets/images/Pop_envtopo.gif)




In the [envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=envtopo.m) plot (below), the black thick line
indicates the data envelope (i.e. minimum and maximum of all channel at
every time point) and the colored show the component ERPs.


![375]({{ site.baseurl }}/assets/images/Envtopo.gif)



The picture above looks messy, so again call the [envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=envtopo.m) 
window and zoom in on time range from *200* ms to *500* ms
post-stimulus, as indicated below.


![475]({{ site.baseurl }}/assets/images/Pop_envtopo2.gif)



We can see (below) that near 400 ms component 1 contributes most
strongly to the ERP.


![375]({{ site.baseurl }}/assets/images/Envtopo2.gif)




On the command line, the function also returns the percent variance
accounted for by each component:

    IC4 pvaf: 31.10%
    IC2 pvaf: 25.02%
    IC3 pvaf: 16.92%
    ...



Component ERP-image plotting
----------------------------

To plot ERP-image figures for component activations, select
<span style="color: brown">Plot → Component ERP image</span> 
(calling [pop_erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_erpimage.m)). 

This function works exactly as the one we used
for plotting channel ERP images, but instead of visualizing activity at
one electrode, the function here plots the activation of one component.

Enter the following parameters in the interactive window to sort trials
by phase at 10 Hz and 0 ms, to image reaction time, power and
Inter-Trial Coherence (see the [ERP-image tutorial](/tutorials/single-subject/plotting-erp-images) for more
information).


![525px]({{ site.baseurl }}/assets/images/Componenterpedit.gif)




For component 6 (below) we observe in the [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) figure
that phase at the analysis frequency (9Hz to 11Hz) is evenly distributed
in the time window -300 to 0 ms (as indicated by the bottom trace
showing the inter-trial coherence (ITC) or phase-locking factor). 

This
component accounts for much of the EEG power at 10 Hz, but for little if
any of the average ERP.
 
 Overall, mean power at the analysis frequency
does not change across the epoch (middle blue trace) and phase at the
analysis frequency is not reset by the stimulus (bottom blue trace).
Here again, the red lines show the bootstrap significance limits (for
this number of trials).


![375px]({{ site.baseurl }}/assets/images/I105erpimage.jpg)



*Note*: As scale and polarity information is distributed in the ICA
decomposition (*not* lost!) between the projection weights (column of
the inverse weight matrix, *EEG.icawinv*) and rows of the component
activations matrix (*EEG.icaact*), the absolute amplitude and polarity
of component activations are meaningless and the activations have no
unit of measure (though they are *proportional to* microvolt). 

To recover the absolute value and polarity of activity accounted for by one
or more components at an electrode, image the back-projection of the
component activation(s) at that channel: 
 - go back to the previous
ERP-image window
- use the same parameters 
- set *Project to channel \#* to 27. 

Note that the ERP is reversed in polarity and that absolute
unit for power has changed.


![375px]({{ site.baseurl }}/assets/images/I105erpimage2.jpg)


In the next tutorial, we show how to use EEGLAB to perform and visualize
time/frequency decompositions of channel activities or independent
component activations.

### Plotting channels and component headplots

Using EEGLAB, you may also plot a 3-D head plot of a component
topography by selecting <font color=brown>Plot \> Component maps \> In
3-D</font>. This calls [pop_headplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_headplot.m). The function should
automatically use the spline file you have generated when plotting ERP
3-D scalp maps. Select one ore more components (below) and press *OK*.
For more information on this interface and how to perform
coregistration, see the [Plotting ERP Data in
3-D](/Chapter_06:_Data_Averaging#Plotting_ERP_data_as_a_series_of_3-D_maps "wikilink")
and the [DIPFIT](/A5:_DIPFIT "wikilink").


![575px]({{ site.baseurl }}/assets/images/3Dcomponentedit.gif)


The [pop_headplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_headplot.m) window below appears. You may use the
Matlab rotate 3-D option to rotate these headplots with the mouse. Else,
enter a different *view* angle in the window above.


![375px]({{ site.baseurl }}/assets/images/93ICA_3D.jpg)


