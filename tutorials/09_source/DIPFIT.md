---
layout: default
title: Indep. Comp. sources
parent: 9. Source analysis
grand_parent: Tutorials
nav_order: 8
---
DIPFIT plug-in: Equivalent dipole source localization of independent components
================================================================================

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

A major obstacle to using EEG data to visualize macroscopic brain
dynamics is the underdetermined nature of the inverse problem: Given an
EEG scalp distribution of activity observed at given scalp electrodes,
any number of brain source activity distributions can be found that
would produce it. This is because there are any number of possible brain
source area pairs or etc. that, jointly, add (or subtract) nothing to
(from) the scalp data. Therefore, solving this 'EEG inverse' problem
uniquely requires making additional assumptions about the nature of the
source distributions. A computationally tractable approach is to find
some number of equivalent current dipoles (like vanishingly small
batteries) whose summed projections to the scalp most nearly resemble
the observed scalp distribution.
Unfortunately, the problem of finding the locations of more than one
simultaneously active equivalent dipoles also does not have a unique
solution, and "best fit" solutions will differ depending on the observed
scalp distribution(s) (or scalp 'map(s)') that are given to the source
inversion algorithm. For this reason, approaches to solving the EEG
inverse problem have tended to focus on fitting scalp maps in which a
single dipolar scalp map is expected to be active, for instance very
early peaks in ERP (or magnetic ERF) response averages indexing the
first arrival of sensory information in cortex. Others attempt to fit
multiple dipoles to longer portions of averaged ERP (or ERF) waveforms
based on "prior belief" (i.e., guesses) as to where the sources *should*
be located. This approach has often been criticized for not being based
wholly on the observed data and thus subject to bias or ignorance.
Using ICA to un-mix the continuous EEG data into brain and non-brain
effective source processes is a radically different approach. ICA
identifies temporally independent signal sources in multi-channel EEG
data as well as their patterns of projection to the scalp electrodes,
which are fixed for spatially stationary sources. These ICA 'component
maps' have been shown to be significantly more dipolar (i.e.,
"dipole-like") than either the raw EEG or any average ERP at nearly any
time point -- even though neither the locations of the electrodes nor
the biophysics of volume propagation are taken into account by ICA
([Delorme et al.,
2012](https://sccn.ucsd.edu/~scott/pdf/Delorme_Dipolar2012.pdf)). Many
independent EEG components have scalp maps that nearly perfectly match
the projection of a single equivalent brain dipole. This finding is
consistent with their presumed generation via partial synchrony of local
field potential (LFP) processes within a connected domain or patch of
cortex.
Fortunately, the problem of finding the location of a single equivalent
dipole generating a given dipolar scalp map is well posed, given a
sufficiently accurate electrical 'forward problem' head model that
specifies the resistance between each scalp electrode location and each
possible (brain) source location. Mathematically, coherent local field
potential (LFP) activity across a 'cortical patch' will have an
*equivalent* single infinitesimal oriented dipole model whose scalp
projection pattern matches the joint projection of the spatially
coherent activity across the patch. The location of the equivalent
dipole for such a patch will in general be quite near (\< 2 mm) but not
necessarily precisely at the center of the patch. In particular, if the
patch is radially oriented (e.g., on a cortical gyrus) and is thus
facing the supervening scalp surface, the equivalent dipole tends to be
slightly deeper than the cortical source patch. However, the location of
the equivalent dipole for an *effective source* of this type is
relatively easy to compute and easy to compare across conditions and
subjects. We use the term *effective source* since currents from a
spatially coherent (in-phase) signal across a cortical patch will make a
much larger contribution to the scalp EEG than spatially incoherent
(out-of-phase) activities from smaller domains within the same or any
similar cortical patch, because the out-of-phase contributions of the
smaller domains will tend to cancel each other out at the scalp
recording electrode (*phase cancellation*). Thus, even when the actual
LFP magnitudes in a smaller cortical domains are no less than in the
spatially coherent *effective source* patch, their net contribution to
the scalp EEG will be minimal compared to the spatially coherent
*effective source*.
<u>Component localization in EEGLAB:</u> EEGLAB now includes two
plug-ins for localizing equivalent dipole locations of independent
component scalp maps: (1) the DIPFIT plug-in calling Matlab routines of
Robert Oostenveld (F.C. Donders Centre, Netherlands); and (2) a BESAFIT
plug-in linking to older versions of the BESA program (Megis Software
GMBH, Germany) running outside of Matlab (see
[A7](/A7:_BESA_(outdated) "wikilink")). Use of the DIPFIT plug-in is
strongly recommended. An EEGLAB plug-in by Zeynep Akalin Acar, the
[Neuroelectromagnetic Forward modeling Toolbox
(NFT)](https://sccn.ucsd.edu/wiki/NFT) can also perform distributed
cortical source imaging as well as making the individual subject
electrical (forward) head model from an available subject MR head image
and sufficient EEG. Use of NFT is demonstrated [in its wiki
tutorial](https://sccn.ucsd.edu/wiki/NFT).
DIPFIT is an EEGLAB plug-in based on functions written and contributed
by Robert Oostenveld, and ported to EEGLAB by Robert in collaboration
with [Arnaud Delorme](http://sccn.ucsd.edu/~arno/). DIPFIT2, released
near the beginning of 2006 with EEGLAB v4.6, can perform source
localization by fitting an equivalent current dipole model using a
non-linear optimization technique using a 4-shell spherical model or by
using a standardized boundary element head model. DIPFIT2 makes use of
the FieldTrip toolbox, which requires a separate installation. DIPFIT3
released in 2019 adds support for eLoreta.


Dipole fitting with DIPFIT
--------

The scalp maps of many ICA components are compatible with their
generation in separate domains of partial synchrony in cortex. Because
local connections in cortex have a much higher density than longer range
connections, it is reasonable to assume that synchronous coupling of
neuronal activity, as isolated by ICA, usually occurs within a single
brain area. Some ICA component scalp maps do highly resemble the
projection of a single equivalent dipole (or in some cases a bilaterally
symmetric pair of dipoles). Residual scalp map variance of the
best-fitting single- or two-dipole component models is often
surprisingly low (see below), given the relative inaccuracy of the
(spherical) head model used to compute it. Such ICA components may thus
represent projection of activity from one (or two symmetric) patch(es)
of cortex.
To fit dipole models to ICA components in an EEGLAB dataset, you first
need to perform ICA decomposition and then select the components to be
fitted. To use DIPFIT to fit independent component maps for an EEGLAB
dataset, you must first build or load the dataset, import a channel
location file (see the EEGLAB tutorial on [Importing a Channel Location
File](/Chapter_02:_Channel_Locations "wikilink")) and compute an ICA
decomposition of your data (see [Performing Independent Component
Analysis of EEG
data](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink")).

To follow the dipole fitting example used in this tutorial, download a
69-channel sample dataset for DIPFIT and BESA dipole localization here:
[eeglab_dipole.set](ftp://sccn.ucsd.edu/pub/eeglab_dipole.set) (→1 MB).
This sample dataset contains a channel location file and pre-computed
ICA weights. Note: to save space, this dataset has been reduced to only
a single trial, after performing ICA on about 800 similar trials; You
should <u>not</u> try to apply ICA to this dataset, but should instead
use the pre-processed ICA weight matrix to test dipole localization.
Load the dataset into EEGLAB using menu item <font color=brown>File →
Load Existing Dataset</font>.

Next, you must select which component to fit. Independent component (IC)
5 of the sample dataset decomposition is a typical lateral posterior
alpha rhythm process. To plot component scalp map, use menu item
<span style="color: brown>Plot → Component maps \"> In 2-D</span>, enter *5* for
the component number and option '' 'electrodes', 'pointlabels' '' to
obtain the plot below. Note that the channel location file for this
subject has been scanned using the Polhemus system, so the electrode
locations are not exactly symmetrical.


![425px](/assets/images/A21component_maps.gif)



There are three steps required to create equivalent dipole models for
independent components:

-   Setting model and preferences: This involves choosing the model
    (spherical or boundary element) and excluding some channels from the
    fitting procedure (e.g., eye channels).
-   Grid scanning: This involves scanning possible positions in a coarse
    3-D grid to determine an acceptable starting point for fitting
    equivalent dipoles to each component.
-   Non-linear interactive fitting: This involves running an
    optimization algorithm to find the best position for each equivalent
    dipole.

Below we describe these three steps in detail. Note that the grid
scanning and non-linear optimization may also be performed automatically
for a group of selected components. This is described later in this
chapter.

### Setting up DIPFIT model and preferences

Before running DIPFIT, we must select some input parameters. Select the
EEGLAB menu item <font color=brown> Tools → Locate dipoles using DIPFIT
→ Head model and settings</font> to modify DIPFIT settings. This will
pop up the window below:



![750px](/assets/images/Pop_dipfit_settings.png)



The top edit box, *Model (click to select)*, specifies the type of head
model -- spherical or boundary element (BEM). By default, the spherical
head model uses four spherical surfaces (skin, skull, CSF, cortex) to
model the brain. The BEM model is composed of three 3-D surfaces (skin,
skull, cortex) extracted from the MNI (Montreal Neurological Institute)
canonical template brain also used in SPM. The BEM model is more
realistic than the four concentric spheres model, and will return more
accurate results. The spherical head model is kept for backward
compatibility purposes and should probably not be used any more for
publication. The spherical model returns results that are comparable
with the BESA tool ([below](/#DIPFIT_validation_study_using_the_spherical_head_model "wikilink")).
For this example, select *Boundary element model*.
Clicking on the model name updates the fields below. The entry *Head
model file* contains the head model parameters (surface information,
conductances, etc...). These are Matlab files and may be edited. See the
FieldTrip documentation for more information on the head model files.
The entry *Associated MRI file for plotting* contains the name of the
MRI image to plot dipoles within. You may enter a custom or individual
subject MR image file, assuming this file has first been normalized to
the MNI brain. See a tutorial page on [How to normalize an MR brain
image to the MNI brain template using
SPM2](/A08:_DIPFIT/Normalize "wikilink"). Note that the SPM2 software
directory must be in your Matlab path to use the resulting file in
DIPFIT.
The entry *Associated channel locations if any* contains the name of the
template channel location file associated with the head model. This
information is critical, as your dataset channel location file may be
different from the template. If so, a co-registration transform is
required to align your channel locations using the template locations
associated with the model.

Next is the coregistration which is explained in detail in the following
sections.

The last edit box *Channel to omit channels from dipole fitting*. By
pressing List, a list of channels appears that allows users to exclude
eye channels (or other, possibly non-head channels) from the dipole
fitting procedure. For example, non-scalp channels should be removed
prior to running dipole fitting.

Note: We advise to exclude peri-ocular channel values from inverse source
models because of poor conductance model geometry at the front of the head.

#### Avoiding co-registration by choosing appropriate channel locations

In case your channel location are the same as the one of the model. If
all your electrode locations are within the International 10-20 System,
you may use the standard channel coordinates associated with the head
model. In this case, no co-registration is required. To do this, press
the *No coreg* checkbox and close the DIPFIT settings window above (then
press *OK* to close that window). Then go to the channel editing window
(select menu item <span style="color: brownn">Edit → Channel location</span>).
The resulting channel editor window is shown below:

![600px\|border](/assets/images/Dipfit_pop_chanedit2.png)

Press the *Look up locs* to look up your channel locations (by matching
the channel labels) in the template channel location file.

![Image:Pop_chanedit_lookup.gif](/assets/images/Pop_chanedit_lookup.gif)

If you had wanted to use the template channel locations for the
spherical model, you would have selected the first option in the pop-up
menu *Use BESA file for four-shell DIPFIT spherical model*. If you want
to use the template channel locations for the BEM model, scroll down the
pop-up menu and click on the button labeled *Use MNI coordinate file for
the BEM DIPFIT model*, then press *OK*. At this point you may perform
coarse grid scanning and non-linear fine fitting as explained in the
next section.
<b>Important note:</b> If you change your channel locations, make sure
to go back to DIPFIT settings to update the coordinate transformation
settings.

#### Manual coregistration or fine tuning of coregistration

If you are using channel locations and/or labels *not* in the
International 10-20 System -- for example, scanned electrode positions,
or some commercial high-density electrode cap file -- you will need to
align or co-register your electrode locations with the selected head
model. DIPPLOT does not actually allow you to align your electrode
locations to the head model itself, but rather allows you to align your
electrode locations to matching template electrode locations associated
with the head model.

To try this, click on *Manual coreg.* in the DIPFIT settings window. The
following instruction window will first appear:



![Image:Coregister_warning.gif](/assets/images/Coregister_warning.gif)



If you have selected the spherical head model and pressed *OK*, the
following co-registration window will appear. Here, the electrode
locations are plotted on the sphere that represents the head. Note the
schematic nose on the lower right; this will rotate with the head
sphere. Each small red or green sphere indicates an electrode location,
with fiducial locations (conventionally, the nasion and ear canal
centers) drawn as bigger and darker spheres (more visible in the second
image below).



![Image:Coregister.gif](/assets/images/Coregister.gif)



If you have selected the BEM model, the following window will appear:



![Image:Coregister2.gif](/assets/images/Coregister2.gif)



Use the *Warp* button to align and scale your electrode locations file
so that it becomes best aligned with the template electrode file
associated with the head model.

If you have no channels with labels that are common to the labels in the
template montage, a channel correspondence window will pop up:



![Image:Pop_chancoresp.gif](/assets/images/Pop_chancoresp.gif)



The channel labels from your dataset electrode structure are shown in
the right column, while the left column shows channel labels from the
template channel file associated with the head model. Arrows in both
columns indicate electrodes with the same labels in the other column. If
your channels labels do not correspond to the International 10-20 System
labels used in the template montage, press the *Pair channels* button
and choose the nearest channel to each of your dataset channels in the
template montage.

When you press *OK*, the function will perform the optimal linear 3-D
warp (translation, rotation, and scaling) to align your channel montage
to the template montage associated with the head model. The warping
procedure uses the Fieldtrip toolbox which is installed by default with
EEGLAB. The result will be shown in the channel montage window (see
below). You may press the *Labels on* button to toggle display of the
channel labels for your channel structure (green) or the template
channel file associated with the head model (red). You may also restrict
the display to subsets of channels using the *Electrodes* buttons.
<u>Fine tuning:</u> To finely tune the alignment manually, repeatedly
edit the values in the edit boxes. Here:

-   *Yaw* means rotation in the horizontal plane around the z axis.
-   *Pitch* and *Roll* are rotations around the x and y axes.

The resulting co-registration window should look something like this:



![Image:Coregister3.gif](/assets/images/Coregister3.gif)



<u>Note about fiducials:</u> Your channel structure may contain standard
fiducial locations (nasion and pre-auricular points). If you import a
channel file with fiducial locations into the channel editor, in EEGLAB
v4.6- give them the standard 'fiducial' channel type *FID* and they will
be stored in the channel information structure, *EEG.chaninfo*. This
will also be done automatically if your fiducials have the standard
names, *Nz* (nasion), *LPA* (left pre-auricular point), and *RPA* (right
pre-auricular point ). There is also considerable confusion about
fiducials and we have created new fiducial labels in an attempt to
disambiguate fiducial exact location (see this
[slide](/media:fiducials.pdf "wikilink") extracted from the
[Get_chanlocs](/Get_chanlocs "wikilink") PDF user guide). Note that
fiducial locations are stored outside the standard channel location
structure, *EEG.chanlocs*, for compatibility with other EEGLAB plotting
functions.

Thereafter, fiducial locations will appear in the channel
co-registration window (above) and may be used (in place of
location-matched scalp channels) to align your electrode montage to the
template locations associated with the head model. Use the *Align
fiducials* button to do this. Press *OK* to update the DIPFIT settings
window. This will display the resulting talairach transformation matrix,
a vector comprised of nine fields named *\[shiftx shifty shiftz pitch
roll yaw scalex scaley scalez\]*. Then press *OK* in the DIPFIT settings
window and proceed to localization.

### Initial fitting - Scanning on a coarse-grained grid

Before you perform interactive dipole fitting, first allow DIPFIT to
scan for the best-fitting dipole locations on a coarse 3-D grid covering
the whole brain. The solutions of this grid search are not very accurate
yet, but they are acceptable as starting locations for the non-linear
optimalization. Starting from these best grid locations will speed up
finding the final best-fitting solution. (The next section, A4.4,
explains the fine tuning using the non-linear optimization). The
tutorial instructions below are valid for both the spherical head model
and the boundary element model. To scan dipoles on a coarse grid, select
menu item <font color = brown>Tools → Locate dipoles using DIPFIT →
Coarse fit (grid scan)</font>. If you use the sample dataset, the window
below will pop up:



![400px\|border](/assets/images/Pop_dipfit_batch2.png)



The first edit box *Component(s)* allows you to select a subset of
components to fit. Note: selecting only a few components does not
increase the speed of the computation, since the forward model still has
to be computed at each location on the grid. The *Grid in
X-direction*,*Grid in Y-direction*, and *Grid in Z-direction* edit boxes
allow you to specify the size and spacing of the coarse grid. By
default, DIPFIT uses 24 steps equally spaced between -radius and +radius
of the sphere that best matches the electrode positions. Since
equivalent dipoles are not likely to be in the lower hemisphere of the
model head, by default DIPFIT only scans through positive Z values. The
last edit box, *Rejection threshold RV(%)*, allows you to set a
threshold on the maximum residual variance that is accepted. Using this
threshold, components that do not resemble a dipolar field distribution
will not be assigned a dipole location.

Press *OK* and a bar will pop up to show the progress of the coarse grid
scanning. Note: during dipole localization, the electrode positions are
projected to the skin surface of the spherical or BEM head model, though
the electrode positions as saved in the dataset itself are *not*
altered. DIPFIT starts the grid scan by first excluding all 3-D grid
locations that are outside the head. It then computes the forward model
(dipole-to-electrode projections) at each remaining grid location and
compares it with all component topographies. The progress of this
process is shown in the text window. When the process is completed,
select menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Plot component dipoles</span> to call the window below:



![Image:Pop_dipplot2.gif](/assets/images/Pop_dipplot2.gif)



Simply press *OK*, to produce the figure below:



![Image:Dipplot_gridsearch.gif](/assets/images/Dipplot_gridsearch.gif)



Here, all the dipoles plotted had a residual variance (vis a vis their
component maps) below 40% (as we specified in the coarse grid search
interactive window). Note that some components end up having the same x,
y and z coordinates because of the coarseness of the grid. You may view
individual components by pressing the *Plot one* button. The component
index and its residual variance are then indicated in the top-left
corner (see the ['dipplot()' visualization
tutorial](/#Visualizing_dipole_models "wikilink") below for further
details).

### Interactive fine-grained fitting

To scan dipoles interactively, call menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT →Fine fit (iterative)</span>. The
following windows pop up. Enter a component index (here, 3) in the
*Component to fit* edit box.



![600px\|border](/assets/images/Pop_dipfit_nonlinear.gif)



Prior to fitting the component, press the *Plot map* button to show the
component scalp map. The following window pops up.



![600px\|border](/assets/images/A24comp4.png)



This component, showing a clear left-right symmetric activity, cannot be
accurately modeled using a single dipole. To fit this component using
two dipoles constrained to be located symmetrically across the (corpus
callosum) midline, set both dipole 1 and 2 to 'active' and 'fit' (by
checking the relevant checkboxes in the pop window). Then press the *Fit
selected dipole position(s)* button. If fitting fails, enter different
starting positions (e.g., \[-10 -68 17\] for first dipole and \[10 -68
17\] for the second dipole and refit). When fitting is done, note the
low residual variance for the two-dipole model on the top right corner
of the interactive interface (0.53 %). Then, press the *Plot dipole(s)*
button. The following plot pops up (see the['dipplot()' visualization
tutorial](/#Visualizing_dipole_models "wikilink") below).



![Image:Diplot_image2.gif](/assets/images/Diplot_image2.gif)



Note that the polarity of components is not fixed (but their orientation
is): the product of the component scalp map value and the component
activitation value (i.e., the back-projected contribution of the
component to the scalp data) is in the original data units (e.g.,
microvolts), but the polarities of the scalp map and of the activation
values are undetermined. For example, you may multiply both the scalp
map and the component activity by -1 while preserving the component
back-projection to the scalp (since the two negative factors cancel
out). As a result, you may choose to flip the visualized dipole
orientations (use the pop-up window for fitting, then press the *Flip
in\|out* button and then the *Plot dipole(s)* button to re-plot the
dipoles with indicated orientations reversed.

<u>Important note:</u> when you are done, press the *OK* button in the
interactive interface for dipole fitting. Do not press *Cancel* or close
the window -- if you do, all the dipole locations that you have computed
using this interface will be lost! Also, this DIPFIT menu is the only
one that does not generate EEGLAB history. The first menu item,
<font color=brown>Tools → Locate dipoles using DIPFIT → Autofit
component</font>, uses the same method for dipole fitting but also
generates an EEGLAB history command that can be re-used in batch
scripts.

### Automated dipole fitting

Automated dipole fitting performs the grid search and the non-linear
fitting on several component without human intervention. You still need
to select the model in the DIPFIT settings interactive window though. To
find a best-fitting equivalent dipole for the component above, select
the EEGLAB menu item <font color=brown>Tools → Locate dipoles using
DIPFIT → Autofit (coarse fit, fine fit, plot)</font> to automatically
fit selected ICA components. Set the *Component indices* to *5*, enter
*100* in the *rejection threshold* edit box so the iterative solution is
computed regardless of the residual variance for the coarse fit, and
check the *Plot resulting dipoles* checkbox to plot component dipoles at
the end of fitting. Then, press *OK*.



![Image:Pop_multifit.gif](/assets/images/Pop_multifit.gif)



The function starts by scanning a 3-D grid to determine acceptable
starting positions for each component. Then it uses the non-linear
optimization algorithm to find the exact dipole position for each
component. At the end of the procedure, the following window pops up.



![Image:Dipplot_multifit2.gif](/assets/images/Dipplot_multifit2.gif)



The residual variance *RV: 2.75%* is shown below the component number
*Comp: 5* on the right top corner indicates that the component beingplotted is component 5 and that the residual variance is 2.75%. The [dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipplot.m) function above allows you to rotate the head model

in 3-D with the mouse, plot MRI slices closest to the equivalent dipole,
etc... (See the ['dipplot()' visualization
tutorial](/#Visualizing_dipole_models "wikilink") below for more
details.)


### Visualizing dipole models

Use menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Plot component dipoles</span> and select component number 3 and 5 to
produce the plot shown below (assuming you performed the fit for both
components 3 and 5 as described above). Select all options except the
*Summary mode* and enter '' 'view', \[51 18\]'' in the *Additional
dipplot() options* text box to set the initial 3-D view; the function
will print the component indices.



![Image:Pop_dipplot.gif](/assets/images/Pop_dipplot.gif)



A plot pops-up. After 3D rotation it may look like the following plot.



![Image:A25_dipole_image.gif](/assets/images/A25_dipole_image.gif)



Press the *Plot one* button. You may scroll through the components by
pressing the *Next/Prev* buttons. Note that the closest MRI slices to
the dipole being currently plotted are shown. Note also that if you do
not select the option *Plot closest MRI slices* in the graphic
interface, and then press the *Tight view* button in the dipplot window,
you will be able to see the closest MRI slices at the location of the
plotted dipole as shown below. Try moving the 3-D perspective of the
tight view plot with the mouse, and/or selecting the three cardinal
viewing angles (sagittal, coronal, top) using the lower left control
buttons.



![Image:Dipole_tight.gif](/assets/images/Dipole_tight.gif)



Note that it is not yet possible to toggle the dipole "stems" or
"projection lines" on and off from within the graphic interface. You
need to use the EEGLAB menu again, unselecting the relevant checkboxes.
Also, it is not yet possible to use the subject's own anatomical MRI as
background (it will be possible in the future upon completion of a
EEG/MRI co-registration function as described below).

Finally, again call menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Plot component dipoles</span>. Select *Summary mode* and
press *OK*.



![Image:Dipole_summary.gif](/assets/images/Dipole_summary.gif)



For comparison, using the spherical model, the location of the dipoles
would have been as shown in the following picture. Notice the similarity
of the talairach coordinates for the two models. Notice also that the
BEM model does not overestimate dipole depth compare to the spherical
model (which is usually the case when the BEM model mesh is too coarse).
The MRI used to plot the spherical result is the average MNI brain (over
about 150 subjects) whereas the MRI used to plot the BEM is the average
MNI brain of a single subject (which was used to generate the model
leadfield matrix).



![Image:Dipole_summary2.gif](/assets/images/Dipole_summary2.gif)



The entry *Background image* contains the name of the MRI in which to
plot dipoles. You may enter a custom MRI file assuming this file has
been normalized to the MNI brain (see [How to normalize an MR brain
image to the MNI brain template using
SPM2](/A08:_DIPFIT/Normalize "wikilink"). Note that the SPM2 package
directory in your network must be in your Matlab path to be able to use
the resulting file in EEGLAB. This is true both for the spherical head
model (co-registered to the MNI brain) and the BEM model (based on the
MNI brain).

Note: Co-registration of the MNI average MR image with landmark
electrode positions for the spherical model. To plot dipole locations in
the average MR image (as in the [dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipplot.m) plots above), we
co-registered the MNI average brain MRI with landmark electrode
positions. For the average MRI image, we used a publicly available
average brain image (average of 152 T1-weighted stereotaxic volumes made
available by the ICBM project) from the MNI database (Montreal
Neurological Institute (MNI), Quebec). Co-registration of the MNI brain
and the standard EEG landmarks was accomplished automatically using
fiducials and the Cz (vertex) electrode position, then slightly adjusted
manually.

You may also see the co-registered model head sphere plotted over the
MNI brain in the [dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipplot.m) window by pressing the *Mesh on*
button in the BEM model below (here in 'tight view').



![Image:Dipole_mesh.gif](/assets/images/Dipole_mesh.gif)



Or, for the spherical model below (in summary mode). Note that the
sphere model is stretched in the visualization to the ellipsoid that
best matches the shape of the headsurface of the average MRI.



![Image:Dipole_mesh3.gif](/assets/images/Dipole_mesh3.gif)




#### Plotting dipole locations on scalp maps

Select menu item <span style="color: brown">Plot → Component maps → In 2-D</span>, enter *1:20* in the component index edit box. Note: The
sample dataset structure contains pre-computed component dipoles. If you
are processing another dataset, first select menu item
<span style="color: brown">Tools → Locate dipoles using DIPFIT → Autofit components</span> to fit ICA components from 1 to 20 automatically as
described in section A1.1. above. Check the *Plot dipole* checkbox (see
below) and press *OK*. Note: You may also enter additional dipole
fitting options in the last edit box; press the *Help* button for
details.



![Image:Pop_topoplot_gui.gif](/assets/images/Pop_topoplot_gui.gif)


The following plot will pop up.



![Image:A26topoplot_dipole.gif](/assets/images/A26topoplot_dipole.gif)




### Using DIPFIT to fit independent MEG components

Dipfit (v2.1) now supports source localization for MEG data acquired
using CTF (Vancouver, CA) systems. Note that a custom head model needs
to be used for MEG source localization since it is not possible to do
accurate source localization on a template head model from MEG data. The
main reason for this limitation is that, first, MEG sensor positions do
not follow any positioning standard. Each system may have its own
arrangement. Furthermore, unlike in EEG the sensors are not placed on an
elastic cap that automatically fits to the head of the subject. The MEG
sensor coils are located within a fixed helmet in which the majority of
subjects' heads fit loosely. The position of a given sensor relative to
a cortical structure could be quite different from subject to subject,
and even across different recordings from the same subject. For this
reason, the sensor's location is always reported relative to the center
and the orientation of the subject's head during the recording, which is
never exactly the same across recordings. Consequently, a head model
needs to be created for each recording using the CTF MRIViewer and
localSphere programs (see the CTF documentation). Then, in EEGLAB, call
menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Head model and settings</span>, and select the tab *CTF* in the upper
pop-window (note that the GUI below is an older version compared to the
one available in DIPFIT but the field remain fairly similar). Set up the
DIPFIT model and preferences as follows:

-   Select CTF as model.
-   The model file is the file *default.hdm* created by CTF localSphere,
    located in the *xxx.ds* folder.
-   The MRI head image should be the *xxx.mri* file used by MRIViewer to
    extract the cortical surface.
-   The channel file should be the *xxx.res4* file within the *xxx.ds*
    folder. This file also contains gradiometer-specific information,
    including sensor orientation, that is not in the EEG structure.




![800px](/assets/images/Dipole_settings_meg.gif)




As for EEG data, you first need to scan a relavely coarse grid, to find
an appropriate starting position for each dipole, by calling menu item
<span style="color: brown">Tools → Locate dipoles using DIPFIT → Coarse fit (grid scan)</span>. 

Note that CTF head models are in cm. Consequently,
the grid used for gridsearch needs to be specified in cm (this is done
automatically by pop_dipfit_gridsearch). Then as in EEG dipole fitting,
use menu item <span style="color: brown">Tools → Locate dipoles using DIPFIT → Fine fit (iterative)</span> to optimize dipole positions nonlinearly.


![Image:Dipole_grid_meg.gif](/assets/images/Dipole_grid_meg.gif)




Finally, you may plot dipoles on the subject MRI using menu item <font color=brown>Tools → Locate dipoles using DIPFIT → Plot component dipoles</font> as shown below. The corresponding scalp map is also shown
on the right. Because of co-registration issues, it is not possible to
plot the dipole positions on the scalp map as in EEG). It is strongly
advisable to normalize dipole lengths.


![850px](/assets/images/Dipole_plot_meg.gif)




You can also run DIPFIT for MEG data without a subject MR image if you
have extracted the subject head surface from another source, like a head
model acquired using a Polhemus 3-D location system. However, it would
then not be possible to visualise the dipole within EEGLAB. Any
comparison between or drawing of dipoles for different subjects requires
a thourough understanding of the MEG coordinate system, since that is
being used to express the dipole position. The default is in individual
subjects' head coordinates, and given that head sizes differ between
subject, the position of dipoles cannot be directly compared over
subjects. It is therefore advisable to coregister and spatially
normalize your subjects' MRIs to a common template (such as the MNI
template) and to apply the same coregistration and normalization to the
dipole positions before comparing them. These operations need to be
executed outside EEGLAB. A test set is available
[here](http://sccn.ucsd.edu/eeglab/dipfittut/testmeg.zip). Simply load
the test file and follow the instruction above. Thanks to Nicolas
Robitaille for his efforts to make this new feature work, in documenting
it, and providing test data.

DIPFIT structure and functions
--------

Like other EEGLAB functions, DIPFIT functions are standalone and may
also be called from the command line. Note that whenever you call the
DIPFIT menu from EEGLAB, a text command is stored in the EEGLAB history
as for any other EEGLAB command. Type *h* on the Matlab command line to
view the command history.

DIPFIT creates a *EEG.dipfit* sub-structure within the main *EEG*
dataset structure. This structure has several fields:

> |                            |                                                                                                                                                                                                                                                                                                         |
> |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
> | EEG.dipfit.chansel         | Array of selected channel indices to fit (for instance ECG or EYE channels might be excluded).                                                                                                                                                                                                          |
> | EEG.dipfit.current         | Index of the component currently being fitted.                                                                                                                                                                                                                                                          |
> | EEG.dipfit.hdmfile         | Model file name. Contains informatin about the geometry and the conductivity of the head. This is a standard Matlab file and may be edited as such; for the default spherical model the conductivities and radii are the same as in BESA.                                                               |
> | EEG.dipfit.mrifile         | Contains the MRI file used for plotting dipole locations.                                                                                                                                                                                                                                               |
> | EEG.dipfit.chanfile        | Contains the template channel location file associated with the current head model. This is used for electrode co-registration.                                                                                                                                                                         |
> | EEG.dipfit.coordformat     | Contains the coordinate format in the model structure. This is "spherical" for the spherical model or "MNI" for the BEM model.                                                                                                                                                                          |
> | EEG.dipfit.coord_transform | Contains the talairach transformation matrix to align the user dataset channel location structure (*EEG.chanlocs*) with the selected head model. This is a length-9 vector *\[shiftx shifty shiftz pitch roll yaw scalex scaley scalez\]*. Type *→→ help traditional* in Matlab for more information. |
> | EEG.dipfit.model           | A structure array containing dipole information.                                                                                                                                                                                                                                                        |
> | EEG.dipfit.model.posxyz    | Contains the 3-D position of the dipole(s). If a two-dipole model is used for a given component, each row of this array contains the location of one dipole.                                                                                                                                            |
> | EEG.dipfit.model.momxyz    | Contains 3-D moment of the dipole(s). If a two-dipole model is used for a given component, each row of this array contains the moment of one dipole.                                                                                                                                                    |
> | EEG.dipfit.model.rv        | Gives the relative residual variance between the dipole potential distribution and th ecomponent potential distribution, ranging from 0 to 1.                                                                                                                                                           |
> | EEG.dipfit.model.active    | Remembers which dipole was active when the component model was last fitted.                                                                                                                                                                                                                             |
> | EEG.dipfit.model.select    | Remembers which dipole was selected when the component model was last fitted.                             

The main DIPFIT functions are:
- [pop_dipfit_settings.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_settings.m): Specify DIPFIT parameters, i.e. head model details.                                                                                                                          
- [pop_dipfit_gridsearch.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_gridsearch.m): Perform initial coarse DIPFIT grid scan to find an acceptable starting positions for further fine fitting.                                                                    
- [pop_dipfit_nonlinear.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_nonlinear.m): Perform fine model fitting via an interactive interface using non-linear optimization. Note: This function cannot be called from the command line. For automated processing, use the function below.                                                                                                                    
- [pop_multifit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_multifit.m): Command the DIPFIT modeling process from a single function. This function allows the user to set parameters, initialize locations on a coarse grid, then perform non-linear optimization as in the separate functions above. This function can be used to automate batch fitting of components from one or more subjects.

Auxiliary DIPFIT functions used by the functions above:
- [dipfitdefs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipfitdefs.m): defines a set of default values used in DIPFIT.
- [dipfit_gridsearch.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipfit_gridsearch.m): same as [dipfit_gridsearch.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_batch.m) but does not use a pop-up window and assumes that the input data is an *EEG* dataset structure.
- [dipfit_nonlinear.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=dipfit_nonlinear.m): same as [dipfit_nonlinear.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_manual.m) but does not use a pop-up window and assumes that the input data is an *EEG* dataset structure.

<u>Note:</u> There is no auxiliary "dipfit_settings" function, since
selecting DIPFIT settings mostly involves copying default values to
*EEG.dipfit* fields.

DIPFIT validation study using the spherical head model
--------

We (AD) checked the results of fitting equivalent dipoles with DIPFIT
(spherical model) against results of BESA(3.0) for independent
components of data recorded in a working memory task in our laboratory.
There were 72 channels, of which 69 were used for dipole fitting. In
particular, we excluded tow EOG channels and the reference channel. We
performed ICA on data from three subjects and fit all 69 resulting
components with single dipoles using BESA (see the BESAFIT plug-in
Appendix) and DIPFIT. We then compared only those dipoles whose residual
variance was less than 15% (see plot below).


![Image:Comparedipfitbesa.gif](/assets/images/Comparedipfitbesa.gif)




Distances between equivalent dipole locations returned by DIPFIT1 and
BESA(3.0) were less than 3 mm (left panel) Note: The outliers were
infrequent failures to converge by either algorithm. Dipole angle
differences were below 2 degrees (middle panel). Residual variances
(mismatch between the component scalp map and the model pole projection)
were near equal (right panel). A few dipoles were localized with
residual variance below 15% by DIPFIT but not by BESA (4 of 213
components); a few others with residual variance below 15% by BESA but
not by DIPFIT (8 of 213 components). Optimization nonlinearities may
account for these small differences between the two algorithms, as the
solution models used in the two programs are theoretically identical.

The main advantage of using DIPFIT over BESA for localization of
equivalent dipoles for independent component scalp maps is that it is
integrated into Matlab and EEGLAB, and can be used in batch processing
scripts (see [Matlab
code](/#Using_DIPFIT_to_fit_EEG_or_ERP_scalp_maps "wikilink") and
[structures & functions](/#DIPFIT_structure_and_functions "wikilink")
above). BESA has additional capabilities not relevant to DIPFIT.
Succeeding versions of BESA did not allow a batch processing option.

### Spherical model error

The following article in Frontiers [Corrected Four-Sphere Head Model for
EEG
Signals](https://www.frontiersin.org/articles/10.3389/fnhum.2017.00490/full)
claim "errors in the formulas \[for the spherical model\] both in the
original paper and in the book”, and then refer to a 1998 paper and 2006
book. It seems to me that Srinivasan made an error in 1998 that was
copied in his contribution to Nunez’ book in 2006. However, the author
have not looked up the original original work, which as far as we know
is <https://www.ncbi.nlm.nih.gov/pubmed/95707> which is from 1979. And
note that in the 2nd half of the ’80s and certainly in the ‘90s the
4-concentric-sphere model was widely already (e.g. in BESA above). The
version of BESA we used to compare with Dipfit was BESA 3.0 which was
likely release before 1998 since it was released before BESA 99 (in
1999).

Our implementation in Dipfit (and Fieldtrip) was programmed by Robert
Oostenveld and is based on the Habilschrift (sort of advanced PhD thesis
that only exists in Germany) from Bernd Lutkenhoner from 1992. That
habilschrift is not available in pdf or online, but Robert Oostenveld
has a paper copy. The reason Robert Oostenveld used that description is
that it includes coordinate transformations for the dipole to be off
from the z-axis, i.e. at a arbitrary location in the brain. Right now,
until proven wrong, we don’t see a reason why the implementation in
Dipfit would be wrong, or that it would be based on an incorrect
published description.

There is another function to perform spherical source localization in
Brainstorm
<https://github.com/brainstorm-tools/brainstorm3/blob/master/toolbox/forward/bst_eeg_sph.m>
which is an approximation (Dipfit uses an exact computation, albeit a
series expansion that is truncated by default at order 60). It would be
worth to compare the results of this function with the result of Dipfit.

DIPFIT eLoreta
--------

Dipfit 3.0 also allows computing eLoreta solutions for ICA components
(in EEGLAB 14, this requires to update the Dipfit plugin in the EEGLAB
plugin manager). Model settings and coregistration with head model are
the same for eLoreta as for dipole source localization. eLoreta source
localization may be performed using menu item <font color=brown>File
→Locate component using eLoreta</font>. Result for a component is shown
below. eLoreta like other Dipfit function rely on Fieldtrip functions.
Refer to function ft_sourceanalysis for more information on eLoreta
source localization.


![750px](/assets/images/Dipfiteloreta.png)

Literature references
--------

M. Scherg, "Fundamentals of dipole source potential analysis". In:
"Auditory evoked magnetic fields and electric potentials" (eds. F.
Grandori, M. Hoke and G.L. Romani). Advances in Audiology, Vol. 6.
Karger, Basel, pp 40-69, 1990.

R. Kavanagh, T. M. Darcey, D. Lehmann, and D. H. Fender. "Evaluation of
methods for three-dimensional localization of electric sources in the
human brain." *IEEE Trans Biomed Eng,* 25:421-429, 1978.

T.F. Oostendorp and A. van Oosterom, "Source parameter estimation in
inhomogeneous volume conductors of arbitrary shape", IEEE Trans Biomed
Eng. 36:382-91, 1989.

R. Oostenveld and P. Praamstra. The five percent electrode system for
high-resolution EEG and ERP measurements. Clin Neurophysiol,
112:713-719, 2001.

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward\|A07:_Contributing_to_EEGLAB\|A07: Contributing to
EEGLAB\|A09:_Using custom MRI from individual subjects\|A09: Using
custom MRI from individual subjects} }
