---
layout: default
title: I.10 Inspecting and removing ICA components
permalink: /tutorials/single-subject/inspecting-ica-comp.html
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
nav_order: 10
---




Inspecting ICA components
==========================
The component order returned by *runica/binica* is in decreasing order
of the EEG variance accounted for by each component. In other words, the
lower the order of a component, the more data (neural and/or
artifactual) it accounts for..



Plotting 2-D Component Scalp Maps
----------------------------------

To plot 2-D scalp component maps, select <span style="color: brown"> Plot → Component maps → In 2-D</span>. The interactive window (below) is then
produced by function [pop_topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_topoplot.m) . It is similar to the
window we used for plotting ERP scalp maps. Simply press *OK* to plot
all components.

*Note:* This may take several figures, depending on number of channels and
the *Plot geometry* field parameter. An alternative is to call this
functions several times for smaller groups of channels (e.g., *1:30* ,
*31:60* , etc.). Below we ask for the first 12 components (*1:12*) only,
and choosing to set 'electrodes', 'off'.



![475px]({{ site.baseurl }}/assets/images/I92pop_topoplot.jpg)



The following [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) window appears, showing the scalp
map projection of the selected components. Note that the scale in the
following plot uses arbitrary units. The scale of the component's
activity time course also uses arbitrary units. However, the component's
scalpmap values multiplied by the component activity time course is in
the same unit as the data. <em>\[Note, 09/18: The ICLabel plug-in of
Luca Pion-Tonachini now provides the best estimation of the type of each
of the independent components (brain, eye, muscle, line noise, etc.).
The included function viewprops() makes a display like that below, but
with component type labels -- and clicking on a component will pop up a
window with an expanded set of component property measures, as well as
the estimated probabilities of each component being of each type.
-SM\]</em>



![525px]({{ site.baseurl }}/assets/images/92ICA_topo.jpg)




### Plotting component headplots

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






<details>
  <summary>Note on ICA component projections and electrode montage plot </summary>
  

Note: From EEGLAB v4.32 on, if the electrode montage extends below the
horizontal plane of the head center, [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) plots them
as a 'skirt' (or halo) around the cartoon head that marks the
(arc_length = 0.5) head-center plane. (Note: Usually, the best-fitting
sphere is a cm or more above the plane of the nasion and ear canals). By
default, all channels with location arc_lengths \<= 1.0 (head bottom)
are used for interpolation and are shown in the plot. From the
commandline, [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) allows the user to specify the
interpolation and plotting radii (*intrad* and *plotrad*) as well as the
radius of the cartoon head (*headrad*). The *headrad* value should
normally be kept at its physiologically correct value (0.5). In 'skirt'
mode (see below), the cartoon head is plotted at its normal location
relative to the electrodes, the lower electrodes appearing in a 'skirt'
outside the head cartoon. If you have computed an equivalent dipole
model for the component map (using the [DIPFIT](/A5:_DIPFIT "wikilink")
plug-in) [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) can indicate the location of the
component equivalent current dipole(s). Note that the 'balls' of the
dipole(s) are located as if looking down from above on the transparent
head. The distance of the electrode positions from the vertex, however,
is proportional to their (great circle) distance on the scalp to the
vertex. This keeps the electrodes on the sides of the head from being
bunched together as they would be in a top-down view of their positions.
This great-circle projection spreads out the positions of the lower
electrodes. Thus, in the figure below, the (bottom) electrodes plotted
on the lower portion of the 'skirt' are actually located on the back of
the neck. In the plot, they appear spread out, whereas in reality they
are bunched on the relatively narrow neck surface. The combinations of
top-down and great-circle projections allows the full component
projection (or raw data scalp map) to be seen clearly, while allowing
the viewer to estimate the actual 3-D locations of plot features.




![275px]({{ site.baseurl }}/assets/images/Comp252.jpg)



The EEGLAB v4.32 [topoplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=topoplot.m) above shows an independent
component whose bilateral equivalent dipole model had only 2% residual
variance across all 252 electrode locations. This [binica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=binica.m)
decomposition used PCA to reduce the over 700,000 data points to 160
principal dimensions (a ratio of 28 time points per ICA weight).

</details>





### Studying and removing ICA components


Learning to recognize types of independent components may require
experience. 

The main criteria to determine if a component is 1)cognitively related 2) a muscle artifact or 3) some other type of
artifact are
 - first, the scalp map (as shown above), 
 - next the component
time course, 
- next the component activity power spectrum,
- finally
(given a dataset of event-related data epochs), the 
[erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m).

For example an expert eye would spot component 3 (above) as an eye
artifact component (see also component activity by calling menu
<span style="color: brown">Plot → Component activations (scroll)</span>). 

In the
window above, click on scalp map number 3 to pop up a window showing it
alone (as mentioned earlier, your decomposition and component ordering
might be slightly different).



![225px]({{ site.baseurl }}/assets/images/92ICA_eyecomp.jpg)


To study component properties and label components for rejection (i.e.
to identify components to subtract from the data), select
<span style="color: brown"> Tools → Reject data using ICA → Reject components by map</span>. 

The difference between the resulting figure(s) and the
previous 2-D scalp map plots is that one can here plot the properties of
each component by clicking on the rectangular button above each
component scalp map.


![450px]({{ site.baseurl }}/assets/images/94reject_ICAcomp.jpg)


For example, click on the button labeled *3*. This component can be
identified as an eye artifact for three reasons:

1.  The smoothly decreasing EEG spectrum (bottom panel) is typical of an
    eye artifact;
2.  The scalp map shows a strong far-frontal projection typical of eye
    artifacts; And,
3.  It is possible to see individual eye movements in the component 
[erpimage.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=erpimage.m) (top-right panel).

Eye artifacts are (nearly) always present in EEG datasets. 

They are usually in leading positions in the component array (because they tend
to be big) and their scalp topographies (if accounting for lateral eye
movements) look like component 3 or perhaps (if accounting for eye
blinks) like that of component 10 (above). 

Component property figures
can also be accessed directly by selecting 
<span style="color: brown"> Plot → Component properties</span>. (There is an equivalent menu item for
channels, <span style="color: brown"> Plot → Channel properties</span>).

Artifactual components are also relatively easy to identify by visual
inspection of component time course 
(menu <span style="color: brown">Plot → Component activations (scroll)</span> --- not shown here).


![325px]({{ site.baseurl }}/assets/images/I94component3_properties.jpg)



Since this component accounts for eye activity, we may wish to subtract
it from the data before further analysis and plotting. If so, click on
the bottom green <span style="color: green">*Accept* </span> button (above) to
toggle it into a red <span style="color: red"> *Reject*</span> button (note: at
this point, components are only marked for rejection; to subtract marked
components, see next section ['Subtracting ICA components from data'](/tutorials/single-subject/working-with-ICA-components)). 
Now press
*OK* to go back to the main component property window.

Another artifact example in our decomposition is component 32, which
appears to be typical muscle artifact component. This components is
spatially localized and show high power at high frequencies (20-50 Hz
and above) as shown below.


![325px]({{ site.baseurl }}/assets/images/I94component32_properties.jpg)


Artifactual components often encountered (but not present in this
decomposition) are single-channel (channel-pop) artifacts in which a
single channel goes 'off,' or line-noise artifacts such as 23. 
The ERP
image plot below shows that it picked up some noise line at 60 Hz
especially in trials 65 and on.



![325px]({{ site.baseurl }}/assets/images/I94component24_properties.jpg)



Many other components appear to be brain-related. Our sample
decomposition used in this tutorial is based on clean EEG data, and may
have fewer artifactual components than decompositions of some other
datasets. 

The main criteria for recognizing brain-related components
are that they have:

1.  Dipole-like scalp maps,
2.  Spectral peaks at typical EEG frequence is (i.e., 'EEG-like'
    spectra) and,
3.  Regular ERP-image plots (meaning that the component does not account
    for activity occurring in only a few trials).


The component below has a strong alpha band peak near 10 Hz and a scalp
map distribution compatible with a left occipital cortex brain source.

When we localize ICA sources using single-dipole or dipole-pair source
localization. Many of the 'EEG-like' components can be fit with very low
residual variance (e.g., under 5%). 

See the tutorial example for either
the EEGLAB plug-in [DIPFIT](/A5:_DIPFIT "wikilink") or for the
[BESA](/A7:_BESA_(outdated) "wikilink") plug-in for details.



![325px]({{ site.baseurl }}/assets/images/I94component2_properties.jpg)


 
What if a component looks to be "half artifact, half brain-related"?
In this case, we may ignore it, or may try running ICA decomposition again
on a cleaner data subset or using other ICA training parameters. 


As a rule of thumb, we have learned that removing artifactual epochs
containing one-of-a-kind artifacts is very useful for obtaining 'clean'
ICA components.

*Note:* we believe an optimal strategy is to:

1.  Run ICA
2.  Reject bad epochs (see the functions we developed to detect
    artifactual epochs and channels, if any, in the [tutorial on
    artifact rejection](tutorials/advanced-topics/rejecting-artifacts.html)).
    In some cases, we do not hesitate to remove more than 10% of the
    trials, even from 'relatively clean' EEG datasets. We have learned
    that it is often better to run this first ICA composition on very
    short time windows.
3.  Run ICA a second time on the 'pruned' dataset.
4.  Apply the resulting ICA weights to the same dataset or to longer
    epochs drawn from the same original (continuous or epoched) dataset.
    For instance, to copy ICA weights and sphere information from
    dataset 1 to 2: First, call menu 
    <span style="color: brown">Edit → Dataset info</span> of dataset 2. 
    Then enter *ALLEEG(1).icaweights* in the
    *ICA weight array ...* edit box, *ALLEEG(1).icasphere* in the *ICA
    sphere array ...* edit box, and press *OK*.



### How to deal with "corrupted" ICA decompositions

When using Infomax ICA, which is the default in EEGLAB, it may happen
that the first two components' activity blows up. This happens because
the two components' activity compensate for each other. In this case,
both components are seen as having a large amount of noise. This is
illustrated below.


![px]({{ site.baseurl }}/assets/images/Corruped_ica.png)


The solution to this is not obvious. One solution is to use a different
ICA algorithm. Another solution we have been using is to experiment with
decreasing the number of dimension using PCA. For example, in one case
with 32 channels, decreasing the number of dimension to 10 eliminates
the problem (decreasing to 20 did not). Below is the same data but
decomposed with only 10 PCA components. The first two components clearly
isolates the blinks as they did before but do not appear as noisy. We
are not certain that removing the single blink component below is
preferable to removing the two very noisy component above since we have
not run any formal comparison. Our reasoning is that the two component
above tend to make other components noisy as well so the solution where
dimensions are reduced by PCA is preferable.


![px]({{ site.baseurl }}/assets/images/Corruped_ica2.png)


This is not to say that using PCA should be done systematically. In
general, PCA will slightly corrupt the data by adding non linearities so
it is better to use the full rank data matrix whenever possible.


Subtracting ICA components from data
--------------------------------------

Typically we (at SCCN) don't actually subtract whole independent
component processes from our datasets because typically we study
individual component (rather than summed scalp channel) activities.

However, if and when we want to remove components, we use menu
<span style="color: brown">Tools → Remove components</span>, which calls the 
[pop_subcomp.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_subcomp.m)
 function. 
 
 The component numbers present by
default in the resulting window (below) are those marked for rejection
in the previous <span style="color: brown">Tools → Reject using ICA → Reject components by map</span> 
component rejection window (using the *<span style="color: green">Accept</span> or <span style="color: red">Reject</span>*
buttons). Enter the component numbers you wish to reject and press
*OK*.


![px]({{ site.baseurl }}/assets/images/Pop_subcomp.jpg)


A window will pop up, plotting channel ERP before (in blue) and after
(in red) component(s) subtraction and asking you if you accept the new
ERP.


![475px]({{ site.baseurl }}/assets/images/Pop_subcomp2.gif)


Press *Yes*. A last window will pop up asking you if you want to rename
the new data set. Give it a name and again press *OK*.


![475px]({{ site.baseurl }}/assets/images/Pop_subcompnewdataset.gif)


Note that **storing the new dataset in Matlab memory does not
automatically store it permanently on disk**. 
To do this, select
<span style="color: brown">File → Save current dataset</span>. 

Note that we will
pursue with all components, so you can appreciate the contribution of
artifactual components to the ERP. 

You may recover the previous dataset
using the <span style="color: brown">Dataset</span> top menu.

*Note*: If you try to run ICA on this new dataset, the number of
dimensions of the data will have been reduced by the number of
components subtracted. To run ICA on the reduced dataset, use the *pca*
option under the <span style="color: brown">Tools  → Run ICA</span> pop-up
window, type '' 'pca', '10' '' in the Commandline options box to reduce
the data dimensions to the number of remaining components (here 10),
before running ICA (see [runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=runica.m). 

If the amount of data has
not changed, ICA will typically return the same (remaining) independent
components -- which were, after all, already found to be maximally
independent for these data. 

After running ICA (**not before**), we
suggest you again 'baseline-zero' the data; if it is epoched when some
components have been removed, channel data epoch-baseline means may
differ.

Retaining multiple ICA weights in a dataset
---------------------------------------------

To retain multiple copies of ICA weights (e.g. EEG.weights and
EEG.sphere), use the extendibility property of Matlab structures. On the
Matlab command line, simply define new weight and sphere variables to
retain previous decomposition weights. For example,

``` matlab
>> EEG.icaweights2 = EEG.icaweights; % Store existing ICA weights matrix
>> EEG.icasphere2 = EEG.icasphere; % Store existing ICA sphere matrix
>> [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % copy to EEGLAB memory
>> EEG = pop_runica(EEG);  % Compute ICA weights and sphere again using
% binica() or runica(). Overwrites new weights/sphere matrices
% into EEG.icaweights, EEG.icasphere
>> [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET); % copy to EEGLAB memory
```


Both sets of weights will then be saved when the dataset is saved, and
reloaded when it is reloaded. See the [script
tutorial](/tutorials/advanced-topics/writing-EEGLAB-scripts.html) for more
information about writing Matlab scripts for EEGLAB.

Scrolling through component activations
-----------------------------------------
To scroll through component activations (time courses), select
<span style="color: brown">Plot → Component activations (scroll)</span>.
Scrolling through the ICA activations, one may easily spot components
accounting for characteristic artifacts. For example, in the scrolling 
[eegplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) below, component 3 appears to account primarily for
blinks.
 
 Check these classifications using the complementary visualization produced by 
 <span style="color: brown">Plot → Component properties</span>.



![px]({{ site.baseurl }}/assets/images/Scrollcomponentact2.png)



In the next tutorial, we show more ways to use EEGLAB to study ICA
components of the data.

### Issue: ICA returns near-identical components with opposite polarities

When computing average reference on n-channel data, the rank of the data
is reduced to n-1. Why? Because the sum of the potential is 0 at all
time points, the last channel activity is equal to minus the sum of the
others. ICA does not behave well in this (**rank-deficient**) condition.

Below, we show an ICA solution computed on data which was average
referenced and in which two of the returned components are almost
identical with opposite polarities (data collected with EGI amplifier,
courtesy of the Institute of Noetic Sciences).


![px]({{ site.baseurl }}/assets/images/Comp_identical1.gif)


There are 30 channels shown above; the time width is 5 sec. 

When the
same <em>runica()</em> or <em>binica()</em> (or from the gui,
<em>pop_runica()</em>) decomposition is run using the option "'pca',
29", then a single similar (but not quite identical) component is
returned, and here exhibits quite well defined alpha activity. Not only
does this component account for both component activities above, but the
noise in their activitations disappears (i.e., is more properly assigned
by ICA to other component processes). The noise above is most likely due
to instability in the ICA decomposition algorithm, which is here forced
to create two components compensating for each others activity.


![px]({{ site.baseurl }}/assets/images/Comp_identical2.gif)


If the rank of the data is lower than the number of channels, the EEGLAB
<em>pop_runica()</em> function should detect it. 

However, rank
calculation in Matlab is imprecise, especially since raw EEG data is
stored at single precision. There are thus some cases in which the rank
reduction arising from use of average reference is not detected. In this
case, the user should reduce manually the number of components
decomposed. 

For example, when using 64 channels enter, in the option
edit box, "'pca', 63". If you do not do this, the activity of one of the
components that contributes the most to the data might be duplicated (as
shown above) and you will not be usable for your analysis. The activity
of other components does not seem much affected in our experience,
though as the figure above shows the component affected may also take on
noise.
