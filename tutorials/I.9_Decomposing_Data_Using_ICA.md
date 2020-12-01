---
layout: default
title: I.9 Decomposing Data Using ICA
permalink: /tutorials/single-subject/decomposing-data-using-ICA
parent: I.Single subject data processing tutorial
grand_parent: Tutorials
---

{ {Backward_Forward\|Chapter_08:_Plotting_ERP_images\|(MT) Chapter 08:
Plotting ERP images\|Chapter_10:_Working_with_ICA_components\|(MT)
Chapter 10: Working with ICA components} }

Watch ICA presentations
-----------------------

There are 11 short presentations pertaining to ICA. Click on the image
below to access the playlist.


![300px\|link=<https://www.youtube.com/playlist?list=PLXc9qfVbMMN2uDadxZ_OEsHjzcRtlLNxc>]({{ site.baseurl }}/assets/images/Icapresentation2.png)




Independent Component Analysis of EEG data
------------------------------------------

Decomposing data by ICA (or any linear decomposition method, including
PCA and its derivatives) involves a linear *change of basis* from data
collected at single scalp channels to a spatially transformed "virtual
channel" basis. That is, instead of a collection of simultaneously
recorded single-channel data records, the data are transformed to a
collection of simultaneously recorded outputs of spatial filters applied
to the whole multi-channel data. These spatial filters may be designed
in many ways for many purposes.

In the original scalp channel data, each row of the data recording
matrix represents the time course of summed in voltage differences
between source projections to one data channel and one or more reference
channels (thus itself constituting a linear spatial filter). After ICA
decomposition, each row of the data activation matrix gives the time
course of the activity of one component process spatially filtered from
the channel data.

In the case of ICA decomposition, the independent component filters are
chosen to produce the maximally temporally independent signals available
in the channel data. These are, in effect, *information sources* in the
data whose mixtures, via volume conduction, have been recorded at the
scalp channels. The mixing process (for EEG, by volume conduction) is
passive, linear, and adds no information to the data. On the contrary,
it mixes and obscures the functionally distinct and independent source
contributions.

These information sources may represent synchronous or partialy
synchronous activity within one (or possibly more) cortical patch(es),
else activity from non-cortical sources (e.g., potentials induced by
eyeball movements or produced by single muscle activity, line noise,
etc.). The following example, from [Onton and
Makeig](http://sccn.ucsd.edu/papers/OntonMakeig_ICAERSP06.pdf) (2006),
shows the diversity of source information typically contained in EEG
data, and the striking ability of ICA to separate out these activities
from the recorded channel mixtures.




![300px]({{ site.baseurl }}/assets/images/Icaexample.jpg)




> **[View full-size version of this data
> image.](/Media:ICAexample_big.jpg "wikilink")** *Fifteen seconds of
> EEG data at 9 (of 100) scalp channels (top panel) with activities of 9
> (of 100) independent components (ICs, bottom panel). While nearby
> electrodes (upper panel) record highly similar mixtures of brain and
> non-brain activities, ICA component activities (lower panel) are
> temporally distinct (i.e. maximally independent over time), even when
> their scalp maps are overlapping. Compare, for example, IC1 and IC3,
> accounting for different phases of eye blink artifacts produced by
> this subject after each visual letter presentation (grey background)
> and ensuing auditory performance feedback signal (colored lines).
> Compare, also, IC4 and IC7, which account for overlapping frontal (4-8
> Hz) theta band activities appearing during a stretch of correct
> performance (seconds 7 through 15). Typical ECG and EMG artifact ICs
> are also shown, as well as overlapping posterior (8-12 Hz) alpha band
> bursts that appear when the subject waits for the next letter
> presentation (white background) For comparison, the repeated average
> visual evoked response of a bilateral occipital IC process (IC5) is
> shown (in red) on the same (relative) scale. Clearly the unaveraged
> activity dynamics of this IC process are not well summarized by its
> averaged response, a dramatic illustration of the independence of
> phase-locked and phase-incoherent activity.*

### Running ICA decompositions

<font color=green>KEY STEP 9:</font> Calculate ICA Components


To compute ICA components of a dataset of EEG epochs (or of a continuous
EEGLAB dataset), select <font color=brown>Tools \> Run ICA</font>. This
calls the function { {File\|pop_runica.m} }. To test this function,
simply press *OK*.


![575px]({{ site.baseurl }}/assets/images/Runica.gif)



We detail each entry of this GUI in detail below.

<u>ICA Algorithms:</u> Note (above) that EEGLAB allows users to try
different ICA decomposition algorithms. Only *runica*, which calls {
{File\|runica.m} } and *jader* which calls the function {
{File\|jader.m} } (from Jean-Francois Cardoso) are a part of the default
EEGLAB distribution. To use the *fastica* algorithm (Hyvarinen et al.),
one must install the [fastica
toolbox](http://www.cis.hut.fi/projects/ica/fastica/) and include it in
the Matlab path. Details of how these ICA algorithms work can be found
in the scientific papers of the teams that developed them. In general,
the physiological significance of any differences in the results or
different algorithms (or of different parameter choices in the various
algorithms) have not been tested -- neither by us nor, as far as we
know, by anyone else. Applied to simulated, relatively low dimensional
data sets for which all the assumptions of ICA are exactly fulfilled,
all three algorithms return near-equivalent components. We are satisfied
that Infomax ICA (runica/binica) gives stable decompositions with up to
hundreds of channels (assuming enough training data are given, see
below), and therefore we can recommend its use, particularly in its
faster binary form ({ {File\|binica.m} } - note that you will also need
to download the binary file at [this page](/Binica "wikilink") and edit
the EEGLAB file icadefs.m so that it points to the right binary). Note
about *jader*: this algorithm uses 4th-order moments (whereas Infomax
uses (implicitly) a combination of higher-order moments) but the storage
required for all the 4th-order moments become impractical for datasets
with more than \~50 channels. Note about *fastica*: Using default
parameters, this algorithm quickly computes individual components (one
by one). However, the order of the components it finds cannot be known
in advance, and performing a complete decomposition is not necessarily
faster than Infomax. Thus for practical purposes its name for it should
not be taken literally. Also, in our experience it may be less stable
than Infomax for high-dimensional data sets.

*Very important note:* We usually run ICA using many more trials that
the sample decomposition presented here. As a general rule, finding
*N*stable components (from N-channel data) typically requires *more
than* *kN^2* data sample points (at each channel), where N^2 is the
number of weights in the unmixing matrix that ICA is trying to learn and
*k* is a multiplier. In our experience, the value of *k* increases as
the number of channels increases. In our example using 32 channels, we
have 30800 data points, giving 30800/32^2 = 30 pts/weight points.
However, to find 256 components, it appears that even 30 points per
weight is not enough data. In general, it is important to give ICA as
much data as possible for successful training. Can you use too much
data? This would only occur when data from radically different EEG
states, from different electrode placements, or containing
non-stereotypic noise were concatenated, increasing the number of scalp
maps associated with independent time courses and forcing ICA to mixture
together dissimilar activations into the N output components. The bottom
line is: ICA works best when given a large amount of basically similar
and mostly clean data. When the number of channels (N) is large (\>\>32)
then a very large amount of data may be required to find N components.
When insufficient data are available, then using the 'pca' option to {
{File\|jader.m} } to find fewer than N components may be the only good
option.

<u>Supported Systems for binica:</u> To use the optional (and much
faster) *binica*, which calls { {File\|binica.m} } , the faster C
translation of { {File\|runica.m} }, you must make the location of the
executable ICA file known to Matlab and executable on your system. Note:
Edit the EEGLAB { {File\|icadefs.m} } Matlab script file to specify the
location of the { {File\|binica.m} } executable. The EEGLAB toolbox
includes three versions of the binary executable Informax ica routine,
for Linux (compiled under Redhat 2.4), *freebsd* (3.0) and *freebsd*
(4.0) (these are named, respectively *ica_linux2.4* , '' ica_bsd3.0''
and *ica_bsd4.0*). The executable file must also be accessible through
the Unix user path variable otherwise { {File\|binica.m} } won't work.
Windows and sun version (older version of binary ICA executable) are
available [here](http://www.sccn.ucsd.edu/eeglab/binica/) (copy them to
the EEGLAB directory). Please [contact us](mailto:eeglab@sccn.ucsd.edu)
to obtain the latest source code to compile it on your own system.

<u>Channel types:</u> It is possible to select specific channel types
(or even a list of channel numbers) to use for ICA decomposition. For
instance, if you have both EEG and EMG channels, you may want to run ICA
on EEG channels only, since any relationship between EEG and EMG signals
should involve propagation delays and ICA assumes an instantaneous
relationship (e.g., common volume conduction). Use the [channel
editor](/Chapter_02:_Channel_Locations "wikilink") to define channel
types.

Running *runica* produces the following text on the Matlab command line:

`Input data size [32,30720] = 32 channels, 30720 frames.`
`Finding 32 ICA components using logistic ICA.`
`Initial learning rate will be 0.001, block size 36.`
`Learning rate will be multiplied by 0.9 whenever angledelta >= 60 deg.`
`Training will end when wchange < 1e-06 or after 512 steps.`
`Online bias adjustment will be used.`
`Removing mean of each channel ...`
`Final training data range: -145.3 to 309.344`
`Computing the sphering matrix...`
`Starting weights are the identity matrix ...`
`Sphering the data ...`
`Beginning ICA training ...`
`step 1 - lrate 0.001000, wchange 1.105647`
`step 2 - lrate 0.001000, wchange 0.670896`
`step 3 - lrate 0.001000, wchange 0.385967, angledelta 66.5 deg`
`step 4 - lrate 0.000900, wchange 0.352572, angledelta 92.0 deg`
`step 5 - lrate 0.000810, wchange 0.253948, angledelta 95.8 deg`
`step 6 - lrate 0.000729, wchange 0.239778, angledelta 96.8 deg`
`...`
`step 55 - lrate 0.000005, wchange 0.000001, angledelta 65.4 deg`
`step 56 - lrate 0.000004, wchange 0.000001, angledelta 63.1 deg`
`Inverting negative activations: 1 -2 -3 4 -5 6 7 8 9 10 -11 -12 -13 -14 -15 -16 17 -18 -19 -20 -21 -22 -23 24 -25 -26 -27 -28 -29 -30 31 -32`
`Sorting components in descending order of mean projected variance ...`
`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32`


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

In the commandline printout, the *angledelta* is the angle between the
direction of the vector in weight space describing the current learning
step and the direction describing the previous step. An intuitive view
of the annealing angle (*angledelta*) threshold (see above) is as
follows: If the learning step takes the weight vector (in global weight
vector space) 'past' the true or best solution point, the following step
will have to 'back-track.' Therefore, the learning rate is too high (the
learning steps are too big) and should be reduced. If, on the other
hand, the learning rate were too low, the angle would be near 0 degrees,
learning would proceed in (small) steps in the same direction, and
learning would be slow. The default annealing threshold of 60 degrees
was arrived at heuristically, and might not be optimum.

Note: the *runica* Infomax function returns two matrices, a data
sphering matrix (which is used as a linear preprocessing to ICA) and the
ICA weight matrix. For more information, refer to ICA help pages (i.e.
<http://www.sccn.ucsd.edu/~arno/indexica.html>). If you wish, the
resulting decomposition (i.e., ICA weights and sphere matrices) can then
be applied to longer epochs drawn from the same data, e.g. for
time-frequency decompositions for which epochs of 3-sec or more may be
desirable.
The component order returned by *runica/binica* is in decreasing order
of the EEG variance accounted for by each component. In other words, the
lower the order of a component, the more data (neural and/or
artifactual) it accounts for. In contrast to PCA, for which the first
component may account for 50% of the data, the second 25%, etc..., ICA
component contributions are much more homogeneous, ranging from roughly
5% down to \~0%. This is because PCA specifically makes each successive
component account for as much as possible of the remaining activity not
accounted for by previously determined components -- while ICA seeks
*maximally independent* sources of activity.

PCA components are temporally or spatially orthogonal - smaller
component projections to scalp EEG data typically looking like checker
boards - while ICA components of EEG data are maximally temporally
independent, but spatially unconstrained -- and therefore able to find
maps representing the projection of a partially synchronized domain /
island / patch / region of cortex, no matter how much it may overlap the
projections of other (relatively independent) EEG sources. This is
useful since, apart from ideally (radially) oriented dipoles on the
cortical surface (i.e., on cortical gyri, not in sulci), simple
biophysics shows that the volume projection of each cortical domain must
project appreciably to much of the scalp.
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

### Plotting 2-D Component Scalp Maps

To plot 2-D scalp component maps, select <font color=brown> Plot \>
Component maps \> In 2-D</font>. The interactive window (below) is then
produced by function { {File\|pop_topoplot.m} } . It is similar to the
window we used for plotting ERP scalp maps. Simply press *OK* to plot
all components.

Note: This may take several figures, depending on number of channels and
the *Plot geometry* field parameter. An alternative is to call this
functions several times for smaller groups of channels (e.g., *1:30* ,
*31:60* , etc.). Below we ask for the first 12 components (*1:12*) only,
and choosing to set 'electrodes', 'off'.



![475px]({{ site.baseurl }}/assets/images/I92pop_topoplot.jpg)



The following { {File\|topoplot.m} } window appears, showing the scalp
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



![525px]({{ site.baseurl }}/assets/images/92ica_topo.jpg)



Learning to recognize types of independent components may require
experience. The main criteria to determine if a component is 1)
cognitively related 2) a muscle artifact or 3) some other type of
artifact are, first, the scalp map (as shown above), next the component
time course, next the component activity power spectrum and, finally
(given a dataset of event-related data epochs), the { {File\|erpimage.m}
}. For example an expert eye would spot component 3 (above) as an eye
artifact component (see also component activity by calling menu
<font color=brown>Plot \> Component activations (scroll)</font>). In the
window above, click on scalp map number 3 to pop up a window showing it
alone (as mentioned earlier, your decomposition and component ordering
might be slightly different).



![225px]({{ site.baseurl }}/assets/images/92ica_eyecomp.jpg)



Note: From EEGLAB v4.32 on, if the electrode montage extends below the
horizontal plane of the head center, { {File\|topoplot.m} } plots them
as a 'skirt' (or halo) around the cartoon head that marks the
(arc_length = 0.5) head-center plane. (Note: Usually, the best-fitting
sphere is a cm or more above the plane of the nasion and ear canals). By
default, all channels with location arc_lengths \<= 1.0 (head bottom)
are used for interpolation and are shown in the plot. From the
commandline, { {File\|topoplot.m} } allows the user to specify the
interpolation and plotting radii (*intrad* and *plotrad*) as well as the
radius of the cartoon head (*headrad*). The *headrad* value should
normally be kept at its physiologically correct value (0.5). In 'skirt'
mode (see below), the cartoon head is plotted at its normal location
relative to the electrodes, the lower electrodes appearing in a 'skirt'
outside the head cartoon. If you have computed an equivalent dipole
model for the component map (using the [DIPFIT](/A5:_DIPFIT "wikilink")
plug-in) { {File\|topoplot.m} } can indicate the location of the
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



The EEGLAB v4.32 { {File\|topoplot.m} } above shows an independent
component whose bilateral equivalent dipole model had only 2% residual
variance across all 252 electrode locations. This { {File\|binica.m} }
decomposition used PCA to reduce the over 700,000 data points to 160
principal dimensions (a ratio of 28 time points per ICA weight).

### Plotting component headplots

Using EEGLAB, you may also plot a 3-D head plot of a component
topography by selecting <font color=brown>Plot \> Component maps \> In
3-D</font>. This calls { {File\|pop_headplot.m} }. The function should
automatically use the spline file you have generated when plotting ERP
3-D scalp maps. Select one ore more components (below) and press *OK*.
For more information on this interface and how to perform
coregistration, see the [Plotting ERP Data in
3-D](/Chapter_06:_Data_Averaging#Plotting_ERP_data_as_a_series_of_3-D_maps "wikilink")
and the [DIPFIT](/A5:_DIPFIT "wikilink").


![575px]({{ site.baseurl }}/assets/images/3dcomponentedit.gif)


The { {File\|pop_headplot.m} } window below appears. You may use the
Matlab rotate 3-D option to rotate these headplots with the mouse. Else,
enter a different *view* angle in the window above.


![375px]({{ site.baseurl }}/assets/images/93ica_3d.jpg)


### Studying and removing ICA components

To study component properties and label components for rejection (i.e.
to identify components to subtract from the data), select
<font color=brown> Tools \> Reject data using ICA \> Reject components
by map</font>. The difference between the resulting figure(s) and the
previous 2-D scalp map plots is that one can here plot the properties of
each component by clicking on the rectangular button above each
component scalp map.


![450px]({{ site.baseurl }}/assets/images/94reject_icacomp.jpg)


For example, click on the button labeled *3*. This component can be
identified as an eye artifact for three reasons:

1.  The smoothly decreasing EEG spectrum (bottom panel) is typical of an
    eye artifact;
2.  The scalp map shows a strong far-frontal projection typical of eye
    artifacts; And,
3.  It is possible to see individual eye movements in the component {
    {File\|erpimage.m} } (top-right panel).

Eye artifacts are (nearly) always present in EEG datasets. They are
usually in leading positions in the component array (because they tend
to be big) and their scalp topographies (if accounting for lateral eye
movements) look like component 3 or perhaps (if accounting for eye
blinks) like that of component 10 (above). Component property figures
can also be accessed directly by selecting <font color=brown> Plot \>
Component properties</font>. (There is an equivalent menu item for
channels, <font color=brown> Plot \> Channel properties</font>).
Artifactual components are also relatively easy to identify by visual
inspection of component time course (menu <font color=brown>Plot \>
Component activations (scroll)</font> --- not shown here).


![325px]({{ site.baseurl }}/assets/images/I94component3_properties.jpg)



Since this component accounts for eye activity, we may wish to subtract
it from the data before further analysis and plotting. If so, click on
the bottom green <font color=green>*Accept* </font> button (above) to
toggle it into a red <font color=red> *Reject*</font> button (note: at
this point, components are only marked for rejection; to subtract marked
components, see next section ['Subtracting ICA components from
data'](/#Subtracting_ICA_xomponents_from_data "wikilink")). Now press
*OK* to go back to the main component property window.

Another artifact example in our decomposition is component 32, which
appears to be typical muscle artifact component. This components is
spatially localized and show high power at high frequencies (20-50 Hz
and above) as shown below.


![325px]({{ site.baseurl }}/assets/images/I94component32_properties.jpg)


Artifactual components often encountered (but not present in this
decomposition) are single-channel (channel-pop) artifacts in which a
single channel goes 'off,' or line-noise artifacts such as 23 (the ERP
image plot below shows that it picked up some noise line at 60 Hz
especially in trials 65 and on).



![325px]({{ site.baseurl }}/assets/images/I94component24_properties.jpg)



Many other components appear to be brain-related (Note: Our sample
decomposition used in this tutorial is based on clean EEG data, and may
have fewer artifactual components than decompositions of some other
datasets). The main criteria for recognizing brain-related components
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
residual variance (e.g., under 5%). See the tutorial example for either
the EEGLAB plug-in [DIPFIT](/A5:_DIPFIT "wikilink") or for the
[BESA](/A7:_BESA_(outdated) "wikilink") plug-in for details.



![325px]({{ site.baseurl }}/assets/images/I94component2_properties.jpg)


What if a component looks to be "half artifact, half brain-related"? In
this case, we may ignore it, or may try running ICA decomposition again
on a cleaner data subset or using other ICA training parameters. As a
rule of thumb, we have learned that removing artifactual epochs
containing one-of-a-kind artifacts is very useful for obtaining 'clean'
ICA components.
<u>Important note:</u> we believe an optimal strategy is to:

1.  Run ICA
2.  Reject bad epochs (see the functions we developed to detect
    artifactual epochs and channels, if any, in the [tutorial on
    artifact rejection](/Chapter_01:_Rejecting_Artifacts "wikilink")).
    In some cases, we do not hesitate to remove more than 10% of the
    trials, even from 'relatively clean' EEG datasets. We have learned
    that it is often better to run this first ICA composition on very
    short time windows.
3.  Run ICA a second time on the 'pruned' dataset.
4.  Apply the resulting ICA weights to the same dataset or to longer
    epochs drawn from the same original (continuous or epoched) dataset.
    For instance, to copy ICA weights and sphere information from
    dataset 1 to 2: First, call menu <font color=brown>Edit \> Dataset
    info</font> of dataset 2. Then enter *ALLEEG(1).icaweights* in the
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

### Subtracting ICA components from data

Typically we (at SCCN) don't actually subtract whole independent
component processes from our datasets because typically we study
individual component (rather than summed scalp channel) activities.
However, if and when we want to remove components, we use menu
<font color=brown>Tools \> Remove components</font>, which calls the {
{File\|pop_subcomp.m} } function. The component numbers present by
default in the resulting window (below) are those marked for rejection
in the previous <font color=brown>Tools \> Reject using ICA \> Reject
components by map</font> component rejection window (using the
*<font color=green>Accept</font>/<font color=red>Reject</font>*
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


Note that storing the new dataset in Matlab memory does not
automatically store it permanently on disk. To do this, select
<font color=brown>File \> Save current dataset</font>. Note that we will
pursue with all components, so you can appreciate the contribution of
artifactual components to the ERP. You may recover the previous dataset
using the <font color=brown>Dataset</font> top menu.

Note: If you try to run ICA on this new dataset, the number of
dimensions of the data will have been reduced by the number of
components subtracted. To run ICA on the reduced dataset, use the *pca*
option under the <font color=brown>Tools \> Run ICA</font> pop-up
window, type '' 'pca', '10' '' in the Commandline options box to reduce
the data dimensions to the number of remaining components (here 10),
before running ICA (see { {File\|runica.m} }. If the amount of data has
not changed, ICA will typically return the same (remaining) independent
components -- which were, after all, already found to be maximally
independent for these data. After running ICA (**not before**), we
suggest you again 'baseline-zero' the data; if it is epoched when some
components have been removed, channel data epoch-baseline means may
differ.

### Retaining multiple ICA weights in a dataset

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
tutorial](/Chapter_02:_Writing_EEGLAB_Scripts "wikilink") for more
information about writing Matlab scripts for EEGLAB.

### Scrolling through component activations

To scroll through component activations (time courses), select
<font color=brown>Plot \> Component activations (scroll)</font>.
Scrolling through the ICA activations, one may easily spot components
accounting for characteristic artifacts. For example, in the scrolling {
{File\|eegplot.m} } below, component 3 appears to account primarily for
blinks. Check these classifications using the complementary
visualization produced by <font color=brown>Plot \> Component
properties</font>.



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


There are 30 channels shown above; the time width is 5 sec. When the
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
<em>pop_runica()</em> function should detect it. However, rank
calculation in Matlab is imprecise, especially since raw EEG data is
stored at single precision. There are thus some cases in which the rank
reduction arising from use of average reference is not detected. In this
case, the user should reduce manually the number of components
decomposed. For example, when using 64 channels enter, in the option
edit box, "'pca', 63". If you do not do this, the activity of one of the
components that contributes the most to the data might be duplicated (as
shown above) and you will not be usable for your analysis. The activity
of other components does not seem much affected in our experience,
though as the figure above shows the component affected may also take on
noise.

[Category:I.Single subject data processing
tutorial](/Category:I.Single_subject_data_processing_tutorial "wikilink")
{ {Backward_Forward\|Chapter_08:_Plotting_ERP_images\|(MT) Chapter 08:
Plotting ERP images\|Chapter_10:_Working_with_ICA_components\|(MT)
Chapter 10: Working with ICA components} }
