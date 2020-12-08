---
layout: default
title: I.10 Working with ICA components
permalink: /tutorials/single-subject/working-with-ICA-components
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 10
---

{ {Backward_Forward\|Chapter_09:_Decomposing_Data_Using_ICA\|(MT)
Chapter 09: Decomposing Data Using
ICA\|Chapter_11:_Timefrequency_decomposition\|(MT) Chapter 11:
Timefrequency decomposition} }

Rejecting data epochs by inspection using ICA
---------------------------------------------

To reject data by visual inspection of its ICA component activations,
select <font color=brown>Tools \> Reject data using ICA \> Reject by
inspection</font> (calling [pop_eegplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_eegplot.m). Note that marked
epochs can be kept in memory before being actually rejected (if the
option *Reject marked trials (checked=yes)* below is not set). Thus it
is possible to mark trials for rejection and then to come back and
update the marked trials. The first option (*Add to previously marked
rejections (checked=yes)*) allows us to include previous trial markings
in the scrolling data window or to ignore/discard them. Since it is the
first time we have used this function on this dataset, the option to
plot previously marked trials won't have any effect. Check the checkbox
to reject marked trials, so that the marked trials will be immediately
rejected when the scrolling window is closed. Press *OK*.


![275px]({{ site.baseurl }}/assets/images/Inspectionpop.gif)


First, adjust the scale by entering *10* in the scale text edit box
(lower right). Now, click on the data epochs you want to mark for
rejection. For this exercise, highlight two epochs. You can then
deselect the rejected epochs by clicking again on them. Press the
*Reject* button when finished and enter a name for the new dataset (the
same dataset minus the rejected epochs), or press the *Cancel* button to
cancel the operation.


![575px]({{ site.baseurl }}/assets/images/Inspectionhighlight.gif)



At this point, you may spend some time trying out the advanced rejection
functions we developed to select and mark artifactual epochs based on
ICA component maps and activations. For directions, see the [Data
rejection tutorial](/Chapter_01:_Rejecting_Artifacts "wikilink"). Then,
after rejecting 'bad' epochs, run ICA decomposition again. Hopefully, by
doing this you may obtain a 'cleaner' decomposition.

<u>Important note:</u>what do we mean by a cleaner ICA decomposition?
ICA takes all its training data into consideration. When too many types
(i.e., scalp distributions) of 'noise' - complex movement artifacts,
electrode 'pops', etc -- are left in the training data, these
unique/irreplicable data features will 'draw the attention' of ICA,
producing a set of component maps including many single-channel or
'noisy'-appearing components. The number of components (degrees of
freedom) devoted to decomposition of brain EEG alone will be
correspondingly reduced. Therefore, presenting ICA with as much 'clean'
EEG data as possible is the best strategy (note that blink and other
stereotyped EEG artifacts do not necessarily have to be removed since
they are likely to be isolated as single ICA components). Here 'clean'
EEG data means data after removing noisy time segments (does not apply
to removed ICA components).
For this tutorial, we decide to accept our initial ICA decomposition of
our data and proceed to study the nature and behavior(s) of its
independent components. First, we review a series of functions whose
purpose is to help us determine which components to study and how to
study them.

Plotting component spectra and maps
-----------------------------------

It is of interest to see which components contribute most strongly to
which frequencies in the data. To do so, select <font color=brown>Plot
\> Component spectra and maps</font>. This calls {
{File\|pop_spectopo.m} }. Its first input is the epoch time range to
consider, the forth is the percentage of the data to sample at random
(smaller percentages speeding the computation, larger percentages being
more definitive). Since our EEG dataset is fairly small, we choose to
change this value to *100* (= all of the data). We will then visualize
which components contribute the most at 10 Hz, entering *10* in the
*Scalp map frequency* text box. We simply scan all components, the
default in *Components to consider*. Press *OK*.



![525px]({{ site.baseurl }}/assets/images/Channelspectraedit.gif)



The [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) window (below) appears.




![425px]({{ site.baseurl }}/assets/images/Spectopocomps.gif)



In the previous window, we plotted the spectra of each component. A more
accurate strategy (for technical reasons) is to plot the data signal
minus the component activity and estimate the decrease in power in
comparison to the original signal at one channel (it is also possible to
do it at all channel but it requires to compute the spectrum of the
projection of each component at each channel which is computationally
intensive). To do so, go back to the previous interactive window, choose
explicitly to plot component's contribution at channel *27* (POz) where
power appears to be maximum at *10* Hz using the *Electrode number to
analyze ...:* field, uncheck the checkbox *\[checked\] compute component
spectra...*. Set percent to *100* as before. Finally we will display *6*
component maps instead of 5 (default) (note that all component spectra
will be shown) and we will set the maximum frequency to be plotted at
*30* Hz using the *Plotting frequency range* option in the bottom panel
(below). Press *OK* when done.


![525px]({{ site.baseurl }}/assets/images/Channelspectraedit1.gif)



The [spectopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=spectopo.m) figure appears (as below).


![425px]({{ site.baseurl }}/assets/images/I102spectopo.jpg)




The following text is displayed

> Component 1 percent variance accounted for: 3.07
> Component 2 percent variance accounted for: 3.60
> Component 3 percent variance accounted for: -0.05
> Component 4 percent variance accounted for: 5.97
> Component 5 percent variance accounted for: 28.24
> Component 6 percent variance accounted for: 6.15
> Component 7 percent variance accounted for: 12.68
> Component 8 percent variance accounted for: -0.03
> Component 9 percent variance accounted for: 5.04
> Component 10 percent variance accounted for: 52.08
> Component 11 percent variance accounted for: 0.79
> ....


"Percent variance acounted for" (pvaf) compares the variance of the data
MINUS the (back-projected) component to the variance of the whole data.
Thus, if one component accounts for all the data, the data minus the
component back-projection will be 0, and pvaf will be 100%; If the
component has zero variance, it accounts for none of the data and pvaf =
0%. If a component somehow accounts for the NEGATIVE of the data,
however, pvaf will be larger than 100% (meaning: "If you remove this
component, the data actually get larger, not smaller!"). According to
the variance accounted for output above, component 10 accounts for more
than 50% of power at 10 Hz for channel POz. (Note: A channel number has
to be entered otherwise component contributions are not computed).

Plotting component ERPs
-----------------------

After seeing which components contribute to frequency bands of interest,
it is interesting to look at which components contribute the most to the
ERP. A first step is to view the component ERPs. To Plot component ERPs,
select <font color=brown>Plot \> Component ERPs \> In rectangular
array</font>, which calls function [pop_plotdata.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_plotdata.m). Then
press *OK*.


![325px]({{ site.baseurl }}/assets/images/Rectarrayedit.gif)



The [plotdata.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=plotdata.m) window below pops up, showing the average ERP
for all 31 components.


![425px]({{ site.baseurl }}/assets/images/I103pop_plotdata.jpg)



Click on the component-1 trace (above) to plot this trace in new window
(as below).


![425px]({{ site.baseurl }}/assets/images/I103single_plotdata.jpg)



As for electrodes, use menu <font color=brown>Plot \> Sum/Compare comp.
ERPs</font> to plot component ERP differences accross multiple
datasets.

Plotting component ERP contributions
------------------------------------

To plot the contribution of component ERPs to the data ERP, select
<font color=brown>Plot \> Component ERPs \> with component maps</font>,
which calls [pop_envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_envtopo.m). Simply press *OK* to plot the 7
components that contribute the most to the average ERP of the dataset.
Note artifactual components can be subtracted from the data prior to
plot the ERP using the *Indices of component to subtract ...* edit
box.


![475]({{ site.baseurl }}/assets/images/Pop_envtopo.gif)




In the [envtopo.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=envtopo.m) plot (below), the black thick line
indicates the data envelope (i.e. minimum and maximum of all channel at
every time point) and the colored show the component ERPs.


![375]({{ site.baseurl }}/assets/images/Envtopo.gif)



The picture above looks messy, so again call the { {File\|pop_envtopo.m}
} window and zoom in on time range from *200* ms to *500* ms
post-stimulus, as indicated below.


![475]({{ site.baseurl }}/assets/images/Pop_envtopo2.gif)



We can see (below) that near 400 ms component 1 contributes most
strongly to the ERP.


![375]({{ site.baseurl }}/assets/images/Envtopo2.gif)




On the command line, the function also returns the percent variance
accounted for by each component:

> IC4 pvaf: 31.10%
> IC2 pvaf: 25.02%
> IC3 pvaf: 16.92%
> ...



Component ERP-image plotting
----------------------------

To plot ERP-image figures for component activations, select
<font color=brown>Plot \> Component ERP image</font> (calling {
{File\|pop_erpimage.m} }. This function works exactly as the one we used
for plotting channel ERP images, but instead of visualizing activity at
one electrode, the function here plots the activation of one component.
Enter the following parameters in the interactive window to sort trials
by phase at 10 Hz and 0 ms, to image reaction time, power and
Inter-Trial Coherence (see the [ERP-image
tutorial](/Chapter_08:_Plotting_ERP_images "wikilink") for more
information).


![525px]({{ site.baseurl }}/assets/images/Componenterpedit.gif)




For component 6 (below) we observe in the [erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) figure
that phase at the analysis frequency (9Hz to 11Hz) is evenly distributed
in the time window -300 to 0 ms (as indicated by the bottom trace
showing the inter-trial coherence (ITC) or phase-locking factor). This
component accounts for much of the EEG power at 10 Hz, but for little if
any of the average ERP. Overall, mean power at the analysis frequency
does not change across the epoch (middle blue trace) and phase at the
analysis frequency is not reset by the stimulus (bottom blue trace).
Here again, the red lines show the bootstrap significance limits (for
this number of trials).


![375px]({{ site.baseurl }}/assets/images/I105erpimage.jpg)



Note: As scale and polarity information is distributed in the ICA
decomposition (*not* lost!) between the projection weights (column of
the inverse weight matrix, *EEG.icawinv*) and rows of the component
activations matrix (*EEG.icaact*), the absolute amplitude and polarity
of component activations are meaningless and the activations have no
unit of measure (through they are *proportional to* microvolt). To
recover the absolute value and polarity of activity accounted for by one
or more components at an electrode, image the back-projection of the
component activation(s) at that channel. Go back to the previous
ERP-image window, use the same parameters and set *Project to channel
\#* to 27. Note that the ERP is reversed in polarity and that absolute
unit for power has changed.


![375px]({{ site.baseurl }}/assets/images/I105erpimage2.jpg)


In the next tutorial, we show how to use EEGLAB to perform and visualize
time/frequency decompositions of channel activities or independent
component activations.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")

{ {Backward_Forward\|Chapter_09:_Decomposing_Data_Using_ICA\|(MT)
Chapter 09: Decomposing Data Using
ICA\|Chapter_11:_Timefrequency_decomposition\|(MT) Chapter 11:
Timefrequency decomposition} }
