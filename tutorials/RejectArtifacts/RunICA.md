---
layout: default
title: c. Indep. Comp. Analysis
categories: artifact
parent: 6. Reject artifacts
grand_parent: Tutorials
has_toc: false
---
Independent Component Analysis (ICA) may be used to remove/subtract artifacts embeded in the data (muscle, eye blinks or eye movements) <i>without</i> removing the affected data portions. ICA may also be used to find brain sources and we will come back to this topic in subsequent sections of the tutorial. For more theory and background 
information on ICA you can also refer to the [Appendix](/tutorials/IV.Appendix/ICA_background.html). This is a long section, so we have included a table of contents below.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Watch ICA presentations
-----------------------

You can watch below eleven short presentations on EEG independent component analysis (ICA) which are part of our online tutorial.

<a href="https://www.youtube.com/playlist?list=PLXc9qfVbMMN2uDadxZ_OEsHjzcRtlLNxc"><img align="center" width="400" height="400" src= "{{ site.baseurl }}/assets/images/ICApresentation2.png"></a>

Running ICA decompositions
---------------------------

### Load the sample EEGLAB dataset

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set" which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png]({{ site.baseurl }}/assets/images/Pop_loadset.png)

In theory, you should go through rejecting bad channels and bad portions of data before running ICA. However, the tutorial dataset is clean enough for running ICA without prior artifact rejection.

### Run ICA

To compute ICA components of a dataset of EEG epochs (or of a continuous
EEGLAB dataset), select <span style="color: brown">Tools →  Run ICA</span>. 
This
calls the function [pop_runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_runica.m). To test this function,
simply press *OK*.


![575px]({{ site.baseurl }}/assets/images/Runica.gif)



We detail each entry of this GUI in detail below.

### Which ICA Algorithm?

EEGLAB allows users to try
different ICA decomposition algorithms. Only *runica*, which calls [runica.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=runica.m)
and *jader* which calls the function [jader.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=jader.m) (from Jean-Francois Cardoso) are a part of the default
EEGLAB distribution. 

To use the *fastica* algorithm (Hyvarinen et al.),
one must install the [fastica
toolbox](http://www.cis.hut.fi/projects/ica/fastica/) and include it in
the Matlab path. 

Details of how these ICA algorithms work can be found
in the scientific papers of the teams that developed them. 

Refer to the [Appendix](/tutorials/IV.Appendix/ICA_background.html#note-on-ica-algorithms) for further information on 
the different ICA algorithms.


*Important note* 

We usually run ICA using many more trials that
the sample decomposition presented here. 
ICA works best when given a large amount of basically similar
and mostly clean data. When the number of channels (N) is large (\>\>32)
then a very large amount of data may be required to find N components.
When insufficient data are available, then using the 'pca' option to [jader.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=jader.m) to find fewer than N components may be the only good
option. In general, it is important to give ICA as
much data as possible for successful training. 
Refer to [this Appendix section](/tutorials/IV.Appendix/ICA_background.html#how-many-data-points-do-i-need-to-run-an-ica) for more details.




### Selecting channel types 

It is possible to select specific channel types
(or even a list of channel numbers) to use for ICA decomposition. For
instance, if you have both EEG and EMG channels, you may want to run ICA
on EEG channels only, since any relationship between EEG and EMG signals
should involve propagation delays and ICA assumes an instantaneous
relationship (e.g., common volume conduction). Use the [channel
editor]( /tutorials/single-subject/channel-locations) to define channel
types.

Pressing *OK* will run the ICA algorithm.


### Command line output

Running *runica* produces the following text on the Matlab command line:

        Input data size [32,30720] = 32 channels, 30720 frames.
        Finding 32 ICA components using logistic ICA.
        Initial learning rate will be 0.001, block size 36.
        Learning rate will be multiplied by 0.9 whenever angledelta >= 60 deg.
        Training will end when wchange < 1e-06 or after 512 steps.
        Online bias adjustment will be used.
        Removing mean of each channel ...
        Final training data range: -145.3 to 309.344
        Computing the sphering matrix...
        Starting weights are the identity matrix ...
        Sphering the data ...
        Beginning ICA training ...
        step 1 - lrate 0.001000, wchange 1.105647
        step 2 - lrate 0.001000, wchange 0.670896
        step 3 - lrate 0.001000, wchange 0.385967, angledelta 66.5 deg
        step 4 - lrate 0.000900, wchange 0.352572, angledelta 92.0 deg
        step 5 - lrate 0.000810, wchange 0.253948, angledelta 95.8 deg
        step 6 - lrate 0.000729, wchange 0.239778, angledelta 96.8 deg
        ...
        step 55 - lrate 0.000005, wchange 0.000001, angledelta 65.4 deg
        step 56 - lrate 0.000004, wchange 0.000001, angledelta 63.1 deg
        Inverting negative activations: 1 -2 -3 4 -5 6 7 8 9 10 -11 -12 -13 -14 -15 -16 17 -18 -19 -20 -21 -22 -23 24 -25 -26 -27 -28 -29 -30 31 -32
        Sorting components in descending order of mean projected variance ...
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32


Note: the *runica* Infomax algorithm can only select for components with
a supergaussian activity distribution (i.e., more highly peaked than a
Gaussian, something like an inverted T). If there is strong line noise
in the data, it is preferable to enter the option '' 'extended', 1'' in
the command line option box, so the algorithm can also detect
subgaussian sources of activity, such as line current and/or slow
activity.

Another option we often use is the stop option: try '' 'stop', 1E-7'' to
lower the criterion for stopping learning, thereby lengthening ICA
training but possibly returning cleaner decompositions, particularly of
high-density array data. We also recommend the use of collections of
short epochs that have been carefully pruned of noisy epochs (see
[Rejecting artifacts](/Chapter_01:_Rejecting_Artifacts "wikilink") with
EEGLAB).

*Important note:* Run twice on the same data, ICA decompositions under
*runica/binica* will differ slightly. That is, the ordering, scalp
topography and activity time courses of best-matching components may
appear slightly different. This is because ICA decomposition starts with
a random weight matrix (and randomly shuffles the data order in each
training step), so the convergence is slightly different every time. Is
this a problem? At the least, features of the decomposition that do not
remain stable across decompositions of the same data should not be
interpreted except as irresolvable ICA uncertainty.

Differences between decompositions trained on somewhat different data
subsets may have several causes. We have not yet performed such repeated
decompositions and assessed their common features - though this would
seem a sound approach. Instead, in our recent work we have looked for
commonalities between components resulting from decompositions from
different subjects.

For this tutorial, we decide to accept our initial ICA decomposition of
our data and proceed to study the nature and behavior(s) of its
independent components. 

First, we review a series of functions whose
purpose is to help us determine which components to study and how to
study them.

Inspecting ICA components
==========================
The component order returned by *runica/binica* is in decreasing order
of the EEG variance accounted for by each component. In other words, the
lower the order of a component, the more data (neural and/or
artifactual) it accounts for..

Scrolling through component activations
-----------------------------------------
To scroll through component activations (time courses), select
<span style="color: brown">Plot → Component activations (scroll)</span>.
Scrolling through the ICA activations, one may easily spot components
accounting for characteristic artifacts. For example, in the scrolling 
[eegplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eegplot.m) below, component 3 appears to account primarily for
blinks (we will learn how to recognize them in this tutorial).

![px]({{ site.baseurl }}/assets/images/Scrollcomponentact2.png)

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

Check these classifications using the complementary visualization produced by <span style="color: brown">Plot → Component properties</span>.

Studying and flagging artifactual ICA components
----------------------------------

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

Many other components appear to be brain-related. A different section of the tutorial deal with using ICA component for brain source localization.
What if a component looks to be "half artifact, half brain-related"?
In this case, we may ignore it, or may try running ICA decomposition again
on a cleaner data subset or using other ICA training parameters. 

As a rule of thumb, we have learned that removing artifactual data regions
containing one-of-a-kind artifacts is very useful for obtaining 'clean'
ICA components.

Optimizing ICA decompositions' quality
==========================

What do we mean by a better ICA decomposition
---------------------------------------
ICA takes all its training data into consideration. When too many types
(i.e., scalp distributions) of 'noise' - complex movement artifacts,
electrode 'pops', etc -- are left in the training data, these
unique/irreplicable data features will 'draw the attention' of ICA,
producing a set of component maps including many single-channel or
'noisy'-appearing components. 

The number of components (degrees of
freedom) devoted to decomposition of brain EEG alone will be
correspondingly reduced. 

Therefore, presenting ICA with as much 'clean'
EEG data as possible is the best strategy. Note that blink and other
stereotyped EEG artifacts do not necessarily have to be removed since
they are likely to be isolated as single ICA components. 

Here 'clean'
EEG data means data after removing noisy time segments (does not apply
to removed ICA components).

How to deal with the agressive high pass filter applied before running ICA
---------------------------------------

ICA decomposition are notably of higher quality (less ambiguous components) when the data is high pass filtered above 1Hz or sometimes 2Hz. High pass filtering is the easiest solution to fix a bad quality ICA decompositions. However, for the purpose of processing EEG data (such as ERP analysis) high pass filtering at 2 Hz might not be optimal as it might remove important data. In this case, we believe an optimal strategy is to:

1.  Start with an unfiltered (or minimally filtered) dataset (dataset 1)
2.  Filter the data at 1Hz or 2Hz to obtain dataset 2
3.  Run ICA on dataset 2
4.  Apply the resulting ICA weights to original dataset 1. To copy ICA weights and sphere information from
    dataset 1 to 2: First, call menu <span style="color: brown">Edit → Dataset info</span> of dataset 1. Then enter *ALLEEG(2).icaweights* in the *ICA weight array ...* edit box, *ALLEEG(2).icasphere* in the *ICA sphere array ...* edit box, and press *OK*.

ICA components can be considered as spatial filters, and it is perfectly valid to use these spatial filters on the original unfiltered data. The only limitation is that if there are strong artifacts affecting frequency band below 1 Hz or 2 Hz (depending on the type of high pass filtered you have used), these may not be removed by ICA. In practice, we have never found this to be a problem, because artifactual processes that contaminate the data below 2 Hz also tend to contaminate the data above 2 Hz.

What to do with a low-quality ICA decomposition
---------------------------------------

With a low-quality ICA decomposition, you can try filtering the data as indicated in the previous section. Another strategy is to clean the data agreesively of artifact before running ICA as explained below:

1.  Start with an unfiltered (or minimally filtered) dataset (dataset 1)
2.  Agressively clean dataset either manually or using the automated tools provided in EEGLAB
3.  Run ICA on dataset 2
4.  Apply the resulting ICA weights to original dataset 1. To copy ICA weights and sphere information from
    dataset 1 to 2: First, call menu <span style="color: brown">Edit → Dataset info</span> of dataset 1. Then enter *ALLEEG(2).icaweights* in the *ICA weight array ...* edit box, *ALLEEG(2).icasphere* in the *ICA sphere array ...* edit box, and press *OK*.

As mentioned previously, ICA components can be considered as spatial filters, and it is perfectly valid to use these spatial filters on the original unfiltered data. One limitation of this approach is that the quality of ICA decompositions depends on the quantity of EEG data provided as input. Reducing the amount data could decrease the quality of ICA components.

How to deal with "corrupted" ICA decompositions
---------------------------------------

When using Infomax ICA, which is the default in EEGLAB, it may happen
that the first two components' activity blows up. This happens because
the two components' activity compensate for each other. Both components are almost
identical with opposite polarities (data collected with EGI amplifier,
courtesy of the Institute of Noetic Sciences). In this case,
both components are seen as having a large amount of noise. This is
illustrated below.

![px]({{ site.baseurl }}/assets/images/Comp_identical1.gif)

This may happen in case of rank deficiency (as explained in the next section). However, this may also happen in full ranked data. The solution to this is not obvious. One solution is to use a different
ICA algorithm. Another solution we have been using is to experiment with
decreasing the number of dimension using PCA. For example, in one case
with 32 channels, decreasing the number of dimension to 10 eliminates
the problem (decreasing to 20 did not). Below is the same data but
decomposed with only 10 PCA components (only the first component is shown). Not only
does this component account for both component activities above, but the
noise in its activitation disappears (i.e., is more properly assigned
by ICA to other component processes). The noise above is most likely due
to instability in the ICA decomposition algorithm, which is here forced
to create two components compensating for each others activity. We
are not certain that removing the single blink component below is
preferable to removing the two very noisy component above since we have
not run any formal comparison. Our reasoning is that the two component
above tend to make other components noisy as well so the solution where
dimensions are reduced by PCA is preferable.

![px]({{ site.baseurl }}/assets/images/Comp_identical2.gif)

This is not to say that using PCA should be done systematically. In
general, PCA will slightly corrupt the data by adding non linearities so
it is better to use the full rank data matrix whenever possible.

Issue with data rank deficiencies
---------------------------------------

When computing average reference on n-channel data, the rank of the data
is reduced to n-1. Why? Because the sum of the potential is 0 at all
time points, the last channel activity is equal to minus the sum of the
others. ICA does not behave well in this (**rank-deficient**) condition.

If the rank of the data is lower than the number of channels, the EEGLAB
<em>pop_runica()</em> function should detect it. 

However, rank
calculation in Matlab is imprecise, especially since raw EEG data is
stored at single precision. There are thus some cases in which the rank
reduction arising from use of average reference is not detected. In this
case, the user should reduce manually the number of components
decomposed. If the ICA decomposition does not look "right" (with the types of components shown on this page), check on the Matlab command line that EEGLAB reduced the number of dimension. If this is not the case, you can fix this manually.

For example, when using 64 channels enter, in the option
edit box, "'pca', 63". If you do not do this, the activity of one of the
components that contributes the most to the data might be duplicated (as
shown above) and you will not be usable for your analysis. The activity
of other components does not seem much affected in our experience,
though as the figure above shows the component affected may also take on
noise.

Issues associated with aggresive automated artifact removal before ICA
---------------------------------------

Automated artifact removal before ICA may remove data (such data portions containing blinks) which can easily be corrected by ICA. However, lowering the thresholds for automated artifact rejection might lead to retaining too many artifacts that ICA cannot remove. In this case we recommend the following procedure.

1.  Start with a dataset that has been minimally cleaned of artifacts (or where only bad channels have been removed)
2.  Run ICA on this dataset
3.  Identify bad ICA components and remove/subtract them from the data as explained in the next section
4.  Clean again the dataset using more aggressive threshold or strategy to remove remaining artifacts

Applying ICA to data epochs instead of continuous data
---------------------------------------

In general we recommend using ICA on continuous data, not data for which epochs have been extracted. First, extracting data epochs reduces the number of samples, and ICA component quality is usually higher when more data is present. Second, you are not tempted to remove the epochs' baseline. Removing the epoch baseline can have <a href="https://pubmed.ncbi.nlm.nih.gov/19162199/">dramatic considerences for ICA</a> because it may introduces random offsets in each channel, something ICA cannot model or compensate for. Note that it is possible to extract epochs and not remove the epoch baseline. Then after running ICA, the baseline may be removed.

However, applying ICA to data epochs is possible. ICA expects the data to be stationary, i.e. the same statistical model
is generating all time points. If you have enough data after epoching, then
epoched data may be preferable since it will increase stationary.  However, you may want to epoch on different events to produce
different datasets, with the same ICA decomposition for all conditions.
More data generally gives a better ICA decomposition, assuming all the data
is similar statistically. Longer epochs are preferable because they yield more data for
ICA (assuming stationarity holds.) However, if you are epoching before ICA,
you don’t want to give ICA overlapping epochs, since it will then have
duplicates of some data skewing the statistical model. So the epoch start
time should not be before the stop time of the previous epoch, and the stop
time should not be after the start time of the next epoch.

Automated detection of artifactual ICA components
==========================

<a href="https://github.com/sccn/ICLabel">ICLabel</a> is an EEGLAB plugin installed by default with EEGLAB. The ICLabel project's goal was to develop an EEG IC classifier which is reliable and accurate enough to use in large-scale studies. The current classifier implementation is trained on thousands of maually labeled ICs and hundreds of thousands of unlabeled ICs. More information may be found in the <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6592775/">ICLabel reference article</a>. The <a href="http://labeling.ucsd.edu/tutorial/about">ICLabel website</a>  also allows you to train to recognize components and compare your performance against experts. It can automatically find artifactual ICA components. Note that it is one of many such EEGLAB plugins. Other plugins or toolboxes worth checking for automatically labeling ICA components are MARA, FASTER, SASICA, ADUST and IC_MARK. 

Once you have run ICA, select menu item <span style="color: brown">Tools → Classify components using ICLabel → Label components</span>. Simply select the default and press OK.

![px]({{ site.baseurl }}/assets/images/iclabel1.png)

A second window will pop up and ask to plot components. Simply press OK. IC components will be plotted along with the category they most likely belong to along with the likelyhood of belonging to that category.

![px]({{ site.baseurl }}/assets/images/iclabel2.png)

Note that ICLabel assign a probability to belong to each component. There are 6 classes of components <i>Brain</i>, <i>Muscle</i>, <i>Eye</i>, <i>Heart</i>, <i>Line Noise</i>, <i>Channel Noise</i>, and <i>Other</i>. By typing the following command on the Matlab prompt you can see the probability for each of the first 10 components (rows) to belong to one of the component classes (columns):

``` matlab
>>  round(EEG.etc.ic_classification.ICLabel.classifications(1:10,:)*100)

ans =

  10×7 single matrix

    12     0     1     0    26     1    60
     4     0     0     0    95     0     0
    10     0     4     0    14     1    71
    20     0     0     1    28     1    50
     9     0    53     2     9     2    26
     5     0     0     1    80     0    14
    74     0     0     0    12     0    14
     1     0    85     0     8     2     4
     7     0     0     0    41     4    48
    23     0     0     0    21     0    56
```

Then you may select menu item <span style="color: brown">Tools → Classify components using ICLabel → Flag components as artifacts</span>. The default is to those components which have more than 90% probability of being in the muscle or eye artifacts (eye blinks and eye movements) category. When components are flagged using this function, the button will appear red in the interface for rejecting components manually (<span style="color: brown">Tools → Reject using ICA → Reject components by map</span>), so may edit which component are rejected.

![px]({{ site.baseurl }}/assets/images/iclabel3.png)

Subtracting ICA components from data
==========================

Typically we (at SCCN) do not actually subtract whole independent
component processes from our datasets because typically we study
individual component (rather than summed scalp channel) activities. Also, even you are only interested in removing ICA components, at the STUDY level (group analysis level), components you have flagged as artifacts, either manually or using an automated method, may be automatically subtracted from the data. Therefore, in most cases, there is no need to physically remove/subtract component from the EEG data.

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

In the rest of this tutorial, after running ICA, we pursue with all components, so you can appreciate the contribution of artifactual components to the ERP. 
