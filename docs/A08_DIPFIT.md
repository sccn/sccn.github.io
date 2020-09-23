---
layout: default
title: A08 DIPFIT
permalink: /docs/A08_DIPFIT
parent: Docs
---

{ {Backward_Forward|A07:_Contributing_to_EEGLAB|A07: Contributing to
EEGLAB|A09:_Using custom MRI from individual subjects|A09: Using custom
MRI from individual subjects} }

## DIPFIT plug-in: Equivalent dipole source localization of independent components

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
([Delorme et
al., 2012](https://sccn.ucsd.edu/~scott/pdf/Delorme_Dipolar2012.pdf)).
Many independent EEG components have scalp maps that nearly perfectly
match the projection of a single equivalent brain dipole. This finding
is consistent with their presumed generation via partial synchrony of
local field potential (LFP) processes within a connected domain or patch
of cortex.
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
[A7](/A7:_BESA_\(outdated\) "wikilink")). Use of the DIPFIT plug-in is
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


#### Dipole fitting with DIPFIT

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
[eeglab_dipole.set](ftp://sccn.ucsd.edu/pub/eeglab_dipole.set) (\>1
MB). This sample dataset contains a channel location file and
pre-computed ICA weights. Note: to save space, this dataset has been
reduced to only a single trial, after performing ICA on about 800
similar trials; You should <u>not</u> try to apply ICA to this dataset,
but should instead use the pre-processed ICA weight matrix to test
dipole localization. Load the dataset into EEGLAB using menu item
<font color=brown>File \> Load Existing Dataset</font>.

Next, you must select which component to fit. Independent component (IC)
5 of the sample dataset decomposition is a typical lateral posterior
alpha rhythm process. To plot component scalp map, use menu item
<font color=brown>Plot \> Component maps \> In 2-D</font>, enter *5* for
the component number and option '' 'electrodes', 'pointlabels' '' to
obtain the plot below. Note that the channel location file for this
subject has been scanned using the Polhemus system, so the electrode
locations are not exactly symmetrical.

<center>

![425px](/assets/images/A21component_maps.gif)

</center>


There are three steps required to create equivalent dipole models for
independent components:

  - Setting model and preferences: This involves choosing the model
    (spherical or boundary element) and excluding some channels from the
    fitting procedure (e.g., eye channels).
  - Grid scanning: This involves scanning possible positions in a coarse
    3-D grid to determine an acceptable starting point for fitting
    equivalent dipoles to each component.
  - Non-linear interactive fitting: This involves running an
    optimization algorithm to find the best position for each equivalent
    dipole.

Below we describe these three steps in detail. Note that the grid
scanning and non-linear optimization may also be performed automatically
for a group of selected components. This is described later in this
chapter.

#### Setting up DIPFIT model and preferences

Before running DIPFIT, we must select some input parameters. Select the
EEGLAB menu item <font color=brown> Tools \> Locate dipoles using DIPFIT
\> Head model and settings</font> to modify DIPFIT settings. This will
pop up the window below:


<center>

![750px](/assets/images/pop_dipfit_settings.png)

</center>


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
with the BESA tool
([below](/#DIPFIT_validation_study_using_the_spherical_head_model "wikilink")).
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
fitting procedure. For example, non scalp channels should be removed
prior to running dipole fitting.

##### Avoiding co-registration by choosing appropriate channel locations

In case your channel location are the same as the one of the model. If
all your electrode locations are within the International 10-20 System,
you may use the standard channel coordinates associated with the head
model. In this case, no co-registration is required. To do this, press
the *No coreg* checkbox and close the DIPFIT settings window above (then
press *OK* to close that window). Then go to the channel editing window
(select menu item <font color=brown>Edit \> Channel location</font>).
The resulting channel editor window is shown below:


<center>

![600px|border](/assets/images/Dipfit_pop_chanedit2.png)

</center>


Press the *Look up locs* to look up your channel locations (by matching
the channel labels) in the template channel location file.


<center>

![Image:pop_chanedit_lookup.gif](/assets/images/pop_chanedit_lookup.gif)

</center>


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

##### Manual coregistration or fine tuning of coregistration

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


<center>

![Image:coregister_warning.gif](/assets/images/coregister_warning.gif)

</center>


If you have selected the spherical head model and pressed *OK*, the
following co-registration window will appear. Here, the electrode
locations are plotted on the sphere that represents the head. Note the
schematic nose on the lower right; this will rotate with the head
sphere. Each small red or green sphere indicates an electrode location,
with fiducial locations (conventionally, the nasion and ear canal
centers) drawn as bigger and darker spheres (more visible in the second
image below).


<center>

![Image:coregister.gif](/assets/images/coregister.gif)

</center>


If you have selected the BEM model, the following window will appear:


<center>

![Image:coregister2.gif](/assets/images/coregister2.gif)

</center>


Use the *Warp* button to align and scale your electrode locations file
so that it becomes best aligned with the template electrode file
associated with the head model.

If you have no channels with labels that are common to the labels in the
template montage, a channel correspondence window will pop up:


<center>

![Image:pop_chancoresp.gif](/assets/images/pop_chancoresp.gif)

</center>


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

  - *Yaw* means rotation in the horizontal plane around the z axis.
  - *Pitch* and *Roll* are rotations around the x and y axes.

The resulting co-registration window should look something like this:


<center>

![Image:coregister3.gif](/assets/images/coregister3.gif)

</center>


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

#### Initial fitting - Scanning on a coarse-grained grid

Before you perform interactive dipole fitting, first allow DIPFIT to
scan for the best-fitting dipole locations on a coarse 3-D grid covering
the whole brain. The solutions of this grid search are not very accurate
yet, but they are acceptable as starting locations for the non-linear
optimalization. Starting from these best grid locations will speed up
finding the final best-fitting solution. (The next section, A4.4,
explains the fine tuning using the non-linear optimization). The
tutorial instructions below are valid for both the spherical head model
and the boundary element model. To scan dipoles on a coarse grid, select
menu item <font color = brown>Tools \> Locate dipoles using DIPFIT \>
Coarse fit (grid scan)</font>. If you use the sample dataset, the window
below will pop up:


<center>

![400px|border](/assets/images/pop_dipfit_batch2.png)

</center>


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
select menu item <font color=brown>Tools \> Locate dipoles using DIPFIT
\> Plot component dipoles</font> to call the window below:


<center>

![Image:pop_dipplot2.gif](/assets/images/pop_dipplot2.gif)

</center>


Simply press *OK*, to produce the figure below:


<center>

![Image:dipplot_gridsearch.gif](/assets/images/dipplot_gridsearch.gif)

</center>


Here, all the dipoles plotted had a residual variance (vis a vis their
component maps) below 40% (as we specified in the coarse grid search
interactive window). Note that some components end up having the same x,
y and z coordinates because of the coarseness of the grid. You may view
individual components by pressing the *Plot one* button. The component
index and its residual variance are then indicated in the top-left
corner (see the ['dipplot()' visualization
tutorial](/#Visualizing_dipole_models "wikilink") below for further
details).

#### Interactive fine-grained fitting

To scan dipoles interactively, call menu item <font color=brown>Tools \>
Locate dipoles using DIPFIT \> Fine fit (iterative)</font>. The
following windows pop up. Enter a component index (here, 3) in the
*Component to fit* edit box.


<center>

![600px|border](/assets/images/pop_dipfit_nonlinear.gif)

</center>


Prior to fitting the component, press the *Plot map* button to show the
component scalp map. The following window pops up.


<center>

![600px|border](/assets/images/A24comp4.png)

</center>


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


<center>

![Image:diplot_image2.gif](/assets/images/diplot_image2.gif)

</center>


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
in|out* button and then the *Plot dipole(s)* button to re-plot the
dipoles with indicated orientations reversed.

<u>Important note:</u> when you are done, press the *OK* button in the
interactive interface for dipole fitting. Do not press *Cancel* or close
the window -- if you do, all the dipole locations that you have computed
using this interface will be lost\! Also, this DIPFIT menu is the only
one that does not generate EEGLAB history. The first menu item,
<font color=brown>Tools \> Locate dipoles using DIPFIT \> Autofit
component</font>, uses the same method for dipole fitting but also
generates an EEGLAB history command that can be re-used in batch
scripts.

#### Automated dipole fitting

Automated dipole fitting performs the grid search and the non-linear
fitting on several component without human intervention. You still need
to select the model in the DIPFIT settings interactive window though. To
find a best-fitting equivalent dipole for the component above, select
the EEGLAB menu item <font color=brown>Tools \> Locate dipoles using
DIPFIT \> Autofit (coarse fit, fine fit, plot)</font> to automatically
fit selected ICA components. Set the *Component indices* to *5*, enter
*100* in the *rejection threshold* edit box so the iterative solution is
computed regardless of the residual variance for the coarse fit, and
check the *Plot resulting dipoles* checkbox to plot component dipoles at
the end of fitting. Then, press *OK*.


<center>

![Image:pop_multifit.gif](/assets/images/pop_multifit.gif)

</center>


The function starts by scanning a 3-D grid to determine acceptable
starting positions for each component. Then it uses the non-linear
optimization algorithm to find the exact dipole position for each
component. At the end of the procedure, the following window pops up.


<center>

![Image:dipplot_multifit2.gif](/assets/images/dipplot_multifit2.gif)

</center>


The residual variance *RV: 2.75%* is shown below the component number
*Comp: 5* on the right top corner indicates that the component being
plotted is component 5 and that the residual variance is 2.75%. The {
{File|dipplot.m} } function above allows you to rotate the head model in
3-D with the mouse, plot MRI slices closest to the equivalent dipole,
etc... (See the ['dipplot()' visualization
tutorial](/#Visualizing_dipole_models "wikilink") below for more
details.)


#### Visualizing dipole models

Use menu item <font color=brown>Tools \> Locate dipoles using DIPFIT \>
Plot component dipoles</font> and select component number 3 and 5 to
produce the plot shown below (assuming you performed the fit for both
components 3 and 5 as described above). Select all options except the
*Summary mode* and enter '' 'view', \[51 18\]'' in the *Additional
dipplot() options* text box to set the initial 3-D view; the function
will print the component indices.


<center>

![Image:pop_dipplot.gif](/assets/images/pop_dipplot.gif)

</center>


A plot pops-up. After 3D rotation it may look like the following plot.


<center>

![Image:A25_dipole_image.gif](/assets/images/A25_dipole_image.gif)

</center>


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


<center>

![Image:dipole_tight.gif](/assets/images/dipole_tight.gif)

</center>


Note that it is not yet possible to toggle the dipole "stems" or
"projection lines" on and off from within the graphic interface. You
need to use the EEGLAB menu again, unselecting the relevant checkboxes.
Also, it is not yet possible to use the subject's own anatomical MRI as
background (it will be possible in the future upon completion of a
EEG/MRI co-registration function as described below).

Finally, again call menu item <font color=brown>Tools \> Locate dipoles
using DIPFIT \> Plot component dipoles</font>. Select *Summary mode* and
press *OK*.


<center>

![Image:dipole_summary.gif](/assets/images/dipole_summary.gif)

</center>


For comparison, using the spherical model, the location of the dipoles
would have been as shown in the following picture. Notice the similarity
of the talairach coordinates for the two models. Notice also that the
BEM model does not overestimate dipole depth compare to the spherical
model (which is usually the case when the BEM model mesh is too coarse).
The MRI used to plot the spherical result is the average MNI brain (over
about 150 subjects) whereas the MRI used to plot the BEM is the average
MNI brain of a single subject (which was used to generate the model
leadfield matrix).


<center>

![Image:dipole_summary2.gif](/assets/images/dipole_summary2.gif)

</center>


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
the average MR image (as in the { {File|dipplot.m} } plots above), we
co-registered the MNI average brain MRI with landmark electrode
positions. For the average MRI image, we used a publicly available
average brain image (average of 152 T1-weighted stereotaxic volumes made
available by the ICBM project) from the MNI database (Montreal
Neurological Institute (MNI), Quebec). Co-registration of the MNI brain
and the standard EEG landmarks was accomplished automatically using
fiducials and the Cz (vertex) electrode position, then slightly adjusted
manually.

You may also see the co-registered model head sphere plotted over the
MNI brain in the { {File|dipplot.m} } window by pressing the *Mesh on*
button in the BEM model below (here in 'tight view').


<center>

![Image:dipole_mesh.gif](/assets/images/dipole_mesh.gif)

</center>


Or, for the spherical model below (in summary mode). Note that the
sphere model is stretched in the visualization to the ellipsoid that
best matches the shape of the headsurface of the average MRI.


<center>

![Image:dipole_mesh3.gif](/assets/images/dipole_mesh3.gif)

</center>



##### Plotting dipole locations on scalp maps

Select menu item <font color=brown>Plot \> Component maps \> In
2-D</font>, enter *1:20* in the component index edit box. Note: The
sample dataset structure contains pre-computed component dipoles. If you
are processing another dataset, first select menu item
<font color=brown>Tools \> Locate dipoles using DIPFIT \> Autofit
components</font> to fit ICA components from 1 to 20 automatically as
described in section A1.1. above. Check the *Plot dipole* checkbox (see
below) and press *OK*. Note: You may also enter additional dipole
fitting options in the last edit box; press the *Help* button for
details.


<center>

![Image:pop_topoplot_gui.gif](/assets/images/pop_topoplot_gui.gif)

</center>

The following plot will pop up.


<center>

![Image:A26topoplot_dipole.gif](/assets/images/A26topoplot_dipole.gif)

</center>



#### Using DIPFIT to fit independent MEG components

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
menu item <font color=brown>Tools \> Locate dipoles using DIPFIT \> Head
model and settings</font>, and select the tab *CTF* in the upper
pop-window (note that the GUI below is an older version compared to the
one available in DIPFIT but the field remain fairly similar). Set up the
DIPFIT model and preferences as follows:

  - Select CTF as model.
  - The model file is the file *default.hdm* created by CTF localSphere,
    located in the *xxx.ds* folder.
  - The MRI head image should be the *xxx.mri* file used by MRIViewer to
    extract the cortical surface.
  - The channel file should be the *xxx.res4* file within the *xxx.ds*
    folder. This file also contains gradiometer-specific information,
    including sensor orientation, that is not in the EEG structure.



<center>

![800px](/assets/images/dipole_settings_meg.gif)

</center>



As for EEG data, you first need to scan a relavely coarse grid, to find
an appropriate starting position for each dipole, by calling menu item
<font color=brown>Tools \> Locate dipoles using DIPFIT \> Coarse fit
(grid scan)</font>. Note that CTF head models are in cm. Consequently,
the grid used for gridsearch needs to be specified in cm (this is done
automatically by pop_dipfit_gridsearch). Then as in EEG dipole
fitting, use menu item <font color=brown>Tools \> Locate dipoles using
DIPFIT \> Fine fit (iterative)</font> to optimize dipole positions
nonlinearly.

<center>

![Image:dipole_grid_meg.gif](/assets/images/dipole_grid_meg.gif)

</center>



Finally, you may plot dipoles on the subject MRI using menu item
<font color=brown>Tools \> Locate dipoles using DIPFIT \> Plot component
dipoles</font> as shown below. The corresponding scalp map is also shown
on the right. Because of co-registration issues, it is not possible to
plot the dipole positions on the scalp map as in EEG). It is strongly
advisable to normalize dipole lengths.

<center>

![850px](/assets/images/dipole_plot_meg.gif)

</center>



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

#### Using DIPFIT to fit EEG or ERP scalp maps

Though the implementation of the DIPFIT plug-in has not been expressly
designed to fit dipoles to raw ERP or EEG scalp maps, EEGLAB provides a
command line function allowing DIPFIT to do so. Fitting can only be
performed at selected time points, not throughout a time window. First,
you must specify the DIPFIT settings on the selected dataset (see
section A4.2. Setting up DIPFIT model and preferences). Then, to fit a
time point at 100 ms in an average ERP waveform (for example) from the
main tutorial data set
([eeglab_data_epochs_ica.set](ftp://sccn.ucsd.edu/pub/eeglab_data_epochs_ica.set)),
use the following Matlab commands.

``` matlab
% Find the 100-ms latency data frame
latency = 0.100;
pt100 = round((latency-EEG.xmin)*EEG.srate);

% Find the best-fitting dipole for the ERP scalp map at this timepoint
erp = mean(EEG.data(:,:,:), 3);
EEG = pop_dipfit_settings(EEG); <font color="black">''% Follow GUI instructions to perform co-registration
[ dipole model TMPEEG] = dipfit_erpeeg(erp(:,pt100), EEG.chanlocs, 'settings', EEG.dipfit, 'threshold', 100);

% Show dipole information (spherical or MNI coordinate based on the model selected) dipole

% plot the dipole in 3-D
pop_dipplot(TMPEEG, 1, 'normlen', 'on');

% Plot the dipole plus the scalp map
figure; pop_topoplot(TMPEEG,0,1, [ 'ERP 100ms, fit with a single dipole (RV ' num2str(dipole.rv*100,2) '%)'], 0, 1);
```

Click [here](http://sccn.ucsd.edu/eeglab/dipfittut/dipfit_erpeegtest.m)
to download the script above.


#### DIPFIT structure and functions

Like other EEGLAB functions, DIPFIT functions are standalone and may
also be called from the command line. Note that whenever you call the
DIPFIT menu from EEGLAB, a text command is stored in the EEGLAB history
as for any other EEGLAB command. Type *h* on the Matlab command line to
view the command history.

DIPFIT creates a *EEG.dipfit* sub-structure within the main *EEG*
dataset structure. This structure has several fields:

>
>
> |                             |                                                                                                                                                                                                                                                                                                         |
> | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | EEG.dipfit.chansel          | Array of selected channel indices to fit (for instance ECG or EYE channels might be excluded).                                                                                                                                                                                                          |
> | EEG.dipfit.current          | Index of the component currently being fitted.                                                                                                                                                                                                                                                          |
> | EEG.dipfit.hdmfile          | Model file name. Contains informatin about the geometry and the conductivity of the head. This is a standard Matlab file and may be edited as such; for the default spherical model the conductivities and radii are the same as in BESA.                                                               |
> | EEG.dipfit.mrifile          | Contains the MRI file used for plotting dipole locations.                                                                                                                                                                                                                                               |
> | EEG.dipfit.chanfile         | Contains the template channel location file associated with the current head model. This is used for electrode co-registration.                                                                                                                                                                         |
> | EEG.dipfit.coordformat      | Contains the coordinate format in the model structure. This is "spherical" for the spherical model or "MNI" for the BEM model.                                                                                                                                                                          |
> | EEG.dipfit.coord_transform | Contains the talairach transformation matrix to align the user dataset channel location structure (*EEG.chanlocs*) with the selected head model. This is a length-9 vector *\[shiftx shifty shiftz pitch roll yaw scalex scaley scalez\]*. Type *\>\> help traditional* in Matlab for more information. |
> | EEG.dipfit.model            | A structure array containing dipole information.                                                                                                                                                                                                                                                        |
> | EEG.dipfit.model.posxyz     | Contains the 3-D position of the dipole(s). If a two-dipole model is used for a given component, each row of this array contains the location of one dipole.                                                                                                                                            |
> | EEG.dipfit.model.momxyz     | Contains 3-D moment of the dipole(s). If a two-dipole model is used for a given component, each row of this array contains the moment of one dipole.                                                                                                                                                    |
> | EEG.dipfit.model.rv         | Gives the relative residual variance between the dipole potential distribution and th ecomponent potential distribution, ranging from 0 to 1.                                                                                                                                                           |
> | EEG.dipfit.model.active     | Remembers which dipole was active when the component model was last fitted.                                                                                                                                                                                                                             |
> | EEG.dipfit.model.select     | Remembers which dipole was selected when the component model was last fitted.                                                                                                                                                                                                                           |
>

The main DIPFIT functions are:

> <font face="helvetica,ariel,sans-serif">
>
> |                                      |                                                                                                                                                                                                                                                                                                                           |
> | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | { {File|pop_dipfit_settings.m} }   | Specify DIPFIT parameters, i.e. head model details.                                                                                                                                                                                                                                                                       |
> | { {File|pop_dipfit_gridsearch.m} } | Perform initial coarse DIPFIT grid scan to find an acceptable starting positions for further fine fitting.                                                                                                                                                                                                                |
> | { {File|pop_dipfit_nonlinear.m} }  | Perform fine model fitting via an interactive interface using non-linear optimization. Note: This function cannot be called from the command line. For automated processing, use the function below.                                                                                                                      |
> | { {File|pop_multifit.m} }           | Command the DIPFIT modeling process from a single function. This function allows the user to set parameters, initialize locations on a coarse grid, then perform non-linear optimization as in the separate functions above. This function can be used to automate batch fitting of components from one or more subjects. |
>

> </font>

Auxiliary DIPFIT functions used by the functions above:

> <font face="helvetica,ariel,sans-serif">
>
> |                                 |                                                                                                                                          |
> | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
> | { {File|dipfitdefs.m} }         | defines a set of default values used in DIPFIT.                                                                                          |
> | { {File|dipfit_gridsearch.m} } | same as { {File|pop_dipfit_batch.m} } but does not use a pop-up window and assumes that the input data is an *EEG* dataset structure.  |
> | { {File|dipfit_nonlinear.m} }  | same as { {File|pop_dipfit_manual.m} } but does not use a pop-up window and assumes that the input data is an *EEG* dataset structure. |
>

> </font>

<u>Note:</u> There is no auxiliary "dipfit_settings" function, since
selecting DIPFIT settings mostly involves copying default values to
*EEG.dipfit* fields.


#### DIPFIT validation study using the spherical head model

We (AD) checked the results of fitting equivalent dipoles with DIPFIT
(spherical model) against results of BESA(3.0) for independent
components of data recorded in a working memory task in our laboratory.
There were 72 channels, of which 69 were used for dipole fitting. In
particular, we excluded tow EOG channels and the reference channel. We
performed ICA on data from three subjects and fit all 69 resulting
components with single dipoles using BESA (see the BESAFIT plug-in
Appendix) and DIPFIT. We then compared only those dipoles whose residual
variance was less than 15% (see plot below).

<center>

![Image:comparedipfitbesa.gif](/assets/images/comparedipfitbesa.gif)

</center>



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

#### Spherical model error

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

#### DIPFIT eLoreta

Dipfit 3.0 also allows computing eLoreta solutions for ICA components
(in EEGLAB 14, this requires to update the Dipfit plugin in the EEGLAB
plugin manager). Model settings and coregistration with head model are
the same for eLoreta as for dipole source localization. eLoreta source
localization may be performed using menu item <font color=brown>File
\>Locate component using eLoreta</font>. Result for a component is shown
below. eLoreta like other Dipfit function rely on Fieldtrip functions.
Refer to function ft_sourceanalysis for more information on eLoreta
source localization.

<center>

![750px](/assets/images/dipfiteloreta.png)

</center>




#### Advanced source reconstruction using DIPFIT/Fieldtrip

DIPFIT relies on Fieldtrip, though in fact DIPFIT was also an ancestor
of Fieldtrip: when Robert Oostenveld, the first Fieldtrip developer,
decided to release source imaging functions he had developed during his
dissertation work, he first packaged them in EEGLAB as DIPFIT. A few
years later, when he and his collaborators released Fieldtrip (also
running on MATLAB), we reworked DIPFIT so it would use the Fieldtrip
functions that Robert and colleagues planned to and have since
maintained for use in Fieldtrip. Below is a short tutorial on how to
perform source modeling using Fieldtrip applied to data in an EEGLAB
dataset.

To localize sources of EEG data, first use DIPFIT to align the electrode
locations with a head model of choice (menu item **Tools \> Locate
dipoles using DIPFIT \> Head model and settings**). The resulting DIPFIT
information may then be used to perform source localization in
Fieldtrip.

##### Performing source reconstruction in a volume

The first snippet of code below creates the leadfield matrix for a 3-D
grid (for use with eLoreta, for example).

``` matlab
% First load a dataset in EEGLAB.
% Then use EEGLAB menu item <em>Tools > Locate dipoles using DIPFIT > Head model and settings</em>
% to align electrode locations to a head model of choice
% The eeglab/fieldtrip code is shown below:

eeglab                        % start eeglab
eeglabPath = fileparts(which('eeglab'));                 % save its location
bemPath = fullfile(eeglabPath, 'plugins', 'dipfit', 'standard_BEM');    % load the dipfit plug-in
EEG = pop_loadset(fullfile(eeglabPath, 'sample_data', 'eeglab_data_epochs_ica.set'));   % load the sample eeglab epoched dataset
EEG = pop_dipfit_settings( EEG, 'hdmfile',fullfile(bemPath, 'standard_vol.mat'), ...
           'coordformat','MNI','mrifile',fullfile(bemPath, 'standard_mri.mat'), ...
           'chanfile',fullfile(bemPath, 'elec', 'standard_1005.elc'), ...
           'coord_transform',[0.83215 -15.6287 2.4114 0.081214 0.00093739 -1.5732 1.1742 1.0601 1.1485] , ...
           'chansel',[1:32] );
```

Then calculate a volumetric leadfield matrix using Fieldtrip function
**ft_prepare_leadfield**. Note that the head model is also used to
assess whether a given voxel is within or outside the brain.

``` matlab
dataPre = eeglab2fieldtrip(EEG, 'preprocessing', 'dipfit');   % convert the EEG data structure to fieldtrip

cfg = [];
cfg.channel = {'all', '-EOG1'};
cfg.reref = 'yes';
cfg.refchannel = {'all', '-EOG1'};
dataPre = ft_preprocessing(cfg, dataPre);

vol = load('-mat', EEG.dipfit.hdmfile);

cfg            = [];
cfg.elec       = dataPre.elec;
cfg.headmodel  = vol.vol;
cfg.resolution = 10;   % use a 3-D grid with a 1 cm resolution
cfg.unit       = 'mm';
cfg.channel    = { 'all' };
[sourcemodel] = ft_prepare_leadfield(cfg);
```

Then use the now generated leadfield matrix to perform source
reconstruction. Below, we provide a simple example, to model putative
sources of ERP features using eLoreta. Here, eLoreta may be replaced by
other approaches, such as Dynamical Imaging of Coherent Sources 'dics'
(see the [tutorial
page](http://www.fieldtriptoolbox.org/tutorial/beamformer) from which
this section is inspired for more information).

``` matlab
% Compute an ERP in Fieldtrip. Note that the covariance matrix needs to be calculated here for use in source estimation.
cfg                  = [];
cfg.covariance       = 'yes';
cfg.covariancewindow = [EEG.xmin 0]; % calculate the average of the covariance matrices
                                   % for each trial (but using the pre-event baseline  data only)
dataAvg = ft_timelockanalysis(cfg, dataPre);

% source reconstruction
cfg             = [];
cfg.method      = 'eloreta';
cfg.sourcemodel = sourcemodel;
cfg.headmodel   = vol.vol;
source          = ft_sourceanalysis(cfg, dataAvg);  % compute the source model
```

Then plot the solution using Fieldtrip functions. Note that the
solutions are generated in a low-resolution head volume. It is not
technically feasible to interpolate this volume onto a high-resolution
MRI in (near) real time -- online, it would require too many
computational resources, while offline, it would require too much memory
(one head volume at every latency. Unlike fMRI data, EEG data have high
temporal resolution, so the low-resolution head volume x latencies
matrix is already quite large - transforming it into a high-resolution
volume matrix is impractical). Note that you could then click on
different voxels and latencies to obtain a figure that looks like the
one below.

Note also that you can see discontinuities in the plotted volume. This
is because of sudden inversion of polarity of the dipole orientation in
the nearest voxels. This is normal. The product of voxel polarity by
temporal activity remains continuous in space and time, but because of
the projection method for the 3-D dipole orientation at the voxel level,
it is possible that neighboring voxels have opposite polarities (and, of
course, oppositely-signed time courses as well). An ideal solution has
not been found yet to avoid inversions in both space and time - having
all dipoles point outwards with respect to the head center - and
inverting associated source time courses accordingly - would be a
solution worth trying.

``` matlab
cfg = [];
cfg.projectmom = 'yes';
cfg.flipori = 'yes';
sourceProj = ft_sourcedescriptives(cfg, source);

cfg = [];
cfg.parameter = 'mom';
cfg.operation = 'abs';
sourceProj = ft_math(cfg, sourceProj);

cfg              = [];
cfg.method       = 'ortho';
cfg.funparameter = 'mom';
figure; ft_sourceplot(cfg, sourceProj);
```



<center>

![border|500px](/assets/images/dipfiteloreta3.png)

</center>


Once latencies of interest have been chosen, they may be projected into
a high-resolution MRI. head image. Below, we show global power on MRI
slices of a template brain.

``` matlab
% project sources on MRI and plot solution
mri = load('-mat', EEG.dipfit.mrifile);
mri = ft_volumereslice([], mri.mri);

cfg              = [];
cfg.downsample   = 2;
cfg.parameter    = 'pow';
source.oridimord = 'pos';
source.momdimord = 'pos';
sourceInt  = ft_sourceinterpolate(cfg, source , mri);

cfg              = [];
cfg.method       = 'slice';
cfg.funparameter = 'pow';
figure; ft_sourceplot(cfg, sourceInt);
```



<center>

![border|500px](/assets/images/dipfiteloreta4.png)

</center>



##### Performing source reconstruction on a surface

Alternatively, the code below generates a leadfield matrix for a
realistic 3-D mesh in MNI space. Note that this requires that you choose
the MNI BEM head model when selecting the head model in the DIPFIT
settings menu. Different mesh versions are available using different
resolutions. Refer to
<http://www.fieldtriptoolbox.org/template/sourcemodel/> for more
information . Note that the code below assumes that you have run the
code above.

``` matlab
[ftVer, ftPath] = ft_version;
sourcemodel = ft_read_headshape(fullfile(ftPath, 'template', 'sourcemodel', 'cortex_8196.surf.gii'));

cfg           = [];
cfg.grid      = sourcemodel;    % source points
cfg.headmodel = vol.vol;        % volume conduction model
leadfield = ft_prepare_leadfield(cfg, dataAvg);
```

The code in the previous section used eLoreta. In this section we will
use minimal norm estimate (MNE). Both MNE and eLoreta can perform source
reconstruction at each latency (assuming you are using an EEG time
series as input).

``` matlab
cfg               = [];
cfg.method        = 'mne';
cfg.grid          = leadfield;
cfg.headmodel     = vol.vol;
cfg.mne.lambda    = 3;
cfg.mne.scalesourcecov = 'yes';
source            = ft_sourceanalysis(cfg, dataAvg);
```

Now we will plot global power. Using the same approach, it is possible
to create movies in which the MNE source solutions evolves over time, as
described on [this
page](http://www.fieldtriptoolbox.org/tutorial/minimumnormestimate/).

``` matlab
cfg = [];
cfg.funparameter = 'pow';
cfg.maskparameter = 'pow';
cfg.method = 'surface';
cfg.latency = 0.4;
cfg.opacitylim = [0 200];
ft_sourceplot(cfg, source);
```



<center>

![border|500px](/assets/images/fieldtrip_surface_solution2.png)

</center>



You may also visually check the alignment of the source model mesh with
the BEM head model mesh by overlaying the BEM mesh on the image above,
as shown below

``` matlab
hold on; ft_plot_mesh(vol.vol.bnd(3), 'facecolor', 'red', 'facealpha', 0.05, 'edgecolor', 'none');
hold on; ft_plot_mesh(vol.vol.bnd(2), 'facecolor', 'red', 'facealpha', 0.05, 'edgecolor', 'none');
hold on; ft_plot_mesh(vol.vol.bnd(1), 'facecolor', 'red', 'facealpha', 0.05, 'edgecolor', 'none');
```



<center>

![border|500px](/assets/images/fieldtrip_surface_solution_with_bem2.png)

</center>




##### The most relevant Fieldtrip tutorials

  - [How to build a source
    model](http://www.fieldtriptoolbox.org/tutorial/sourcemodel/) and
    [available template source
    models](http://www.fieldtriptoolbox.org/template/sourcemodel/) (one
    of them is used above)

<!-- end list -->

  - [How to define the volume conduction
    model](http://www.fieldtriptoolbox.org/workshop/baci2017/forwardproblem/)

<!-- end list -->

  - [Beamformer
    methods](http://www.fieldtriptoolbox.org/tutorial/beamformer/) -
    note that you may replace 'dics' by 'eloreta' in this tutorial

<!-- end list -->

  - [Minimum norm
    estimates](http://www.fieldtriptoolbox.org/tutorial/minimumnormestimate/)
    for MEG, but can be adapted for EEG

This section was written by Arnaud Delorme with contributions and
feedback from Robert Oostenveld and Scott Makeig.

#### Literature references

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
{Backward_Forward|A07:_Contributing_to_EEGLAB|A07: Contributing to
EEGLAB|A09:_Using custom MRI from individual subjects|A09: Using custom
MRI from individual subjects} }