---
layout: default
title: a. Head model
long_title: a. Head model settings
parent: 9. Source analysis
grand_parent: Tutorials
---
Back to the basics
==================

To perform source localization, one needs
* A **head model** describing how electrical or magnetic fields behave
** It may be a simple model made of spheres having different conductances
** It may be a more complex model made of geometrical 3-D mesh describing the cortex surface, skull, skin, as well as change in conductance at the interface of these surfaces.
** It may be a volumetric model (Finite Element Model) describing how the current flow in each voxel. These are in theory more precise although they require more computation.
* A **source model** describing the position of the source generating these fields
** It may be a single dipole. 
** It may be dipoles distributed in a 3-D grid (volumetric source model for distributed source localization such as in eLoreta)
** It may be dipoles distributed on a surface. For example, we may force dipoles to be on the cortical surface
* The position of the EEG or MEG **sensors** and a way to align them with both the head model and source model

Once we have all of that, we need an algorithm to find where sources are. Unfortunately, there is an infinite number of solution that can generate the observed activity at the surface of the scalp, so we need to impose constraints on the sources. The constraints may be:
* Force to model the scalp activity with a single dipole. In this way, there is usually a unique optimal solution.
* Force sources to be smooth so the activity of the neighboring sources are correlated. This is the eLoreta solution.
* Force the activity of neighboring sources to be uncorrelated using linearly constrained minimum variance (LCMV) also known as Beamforming.

The figure below illustrates the process described above. After aligning electrodes, head model and source model, we feed that information along with some EEG data to the source reconstruction algorithm (single dipole, eLoreta, Beamforming, etc...). Based on the electrode positions, head model and source model, often, a transformation matrix is computed. This matrix indicates how a given source (described in the source model) influence the activity of individual EEG channels. Its size is source x EEG channels, and it is called the Leadfield matrix. Once we have this matrix, we can ignore the electrode position, head model and source model. The same Leadfield matrix may be used for single dipole, eLoreta, and Beamforming source reconstruction.

![Screen Shot 2022-12-10 at 11 29 37 AM](https://user-images.githubusercontent.com/1872705/206872175-f0224ffc-dc7e-49e6-b74d-e2068a589a29.png)

Selecting a head model
=========================

There are several steps required for source localization. First, choosing a head model, which defines different regions of conductivities. Second, choosing a source model: The source model is the type of source you will use. This may be a single dipole, which position you optimize. This could also be 
a distributed model, with one dipole per brain voxel, such as when using Loreta. The source model is independent of the head model. Third, you will perform inverse source localization and plot the source results.

This section deals with the first step only of choosing a head model and aligning it with your electrode locations. Other steps are described in
subsequent sections of the tutorial.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Setting up DIPFIT head model
----
In this section, we use the tutorial dataset after [extracting data epochs](/tutorials/07_Extract_epochs/Extracting_Data_Epochs.html). Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data_epochs_ica.set" located in the "sample_data" folder of EEGLAB. Then press *Open*.

Before running DIPFIT, we must select some input parameters. Select the
EEGLAB menu item <span style="color: brown"> Tools → Locate dipoles using DIPFIT
→ Head model and settings</span> to modify DIPFIT settings. This will
pop up the window below:

![](/assets/images/dipfit_settings_besa.png)

The top edit box, *Model (click to select)*, specifies the type of head
model -- spherical model, template boundary element model (BEM), or custom model. 

The **template Spherical Four-Shell (BESA)** uses four spherical surfaces (skin, skull, CSF, cortex) to
model the head. The spherical head model is kept for backward
compatibility purposes and should not be used for
publication. The spherical model has been tested against versions of the BESA software and shown to return similar results.

The **template boundary element model** is composed of three 3-D surfaces (skin,
skull, cortex) extracted from the MNI (Montreal Neurological Institute)
canonical template brain is also used in Statistical Parametric Mapping (SPM). The BEM model is more
realistic than the four concentric spheres model and will return more
accurate results. The description of how the BEM model was generated is available [here](https://pubmed.ncbi.nlm.nih.gov/11222970/). Although it was first made available in DIPFIT, this standard BEM model is the same as the one in Fieldtrip when you type *ft_read_headmodel('standard_bem.mat');*. From the original [paper](https://pubmed.ncbi.nlm.nih.gov/11222970/): "This template consists of a high-quality anatomical MRI of a single representative subject,
with a voxel size of 1 x 1 x 1 mm, created by the McConnell Brain Imaging Centre of the Montre¬al Neurological
Institute. It was created by registering 27 T1-weighted
scans of the same individual in stereotaxic space, where they
were subsampled, and intensity averaged. After the generation of this averaged MRI, an expert-guided semi-automatic
segmentation was performed to identify the tissue type of
each voxel. This segmentation of the averaged brain was
used for the construction of a noiseless MRI of the brain
using an MR simulator. This noiseless MRI is used in this
paper for visualizing the results; the segmentation of the
original MRI was used to create the realistically shaped
volume conduction model of the head.
The motivation for using this specific MRI was that it
forms the template brain of the Statistical Parametric
Mapping package (SPM, 1999)."

The **custom model and MRI files from Fieldtrip** allow users to take advantage of custom head models designed in Fieldtrip. How to create a boundary head model from a subject MRI is described [here](https://www.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/). Once you have created a model, the electrode alignment may be performed in EEGLAB, so the second part of the Fieldtrip tutorial may be skipped.

For this example, select *Boundary element model*.
Clicking on the model name updates some of the fields below the dropdown menu: 
- The entry *Head
model file* contains the head model parameters (surface information,
conductances, etc...). These are MATLAB files and may be edited. See the
FieldTrip documentation for more information on the head model files. 
- The
edit box *Matrix to align chan. locs with head model* is automatically updated to align the current electrode coordinates with the current head model. We co-registered the MNI average brain MRI with landmark electrode
positions. For the average MRI image, we used a publicly available
average brain image (average of 152 T1-weighted stereotaxic volumes made
available by the ICBM project) from the MNI database (Montreal
Neurological Institute (MNI), Quebec). Co-registration of the MNI brain
and the standard EEG landmarks was accomplished automatically using
fiducials and the Cz (vertex) electrode position, then slightly adjusted
manually.  In our case, it is not ideal, as it is better to use electrode locations compatible with the head model (see next section).
The automatic update of the transformation matrix is not always performed, and sometimes you may need to align electrode coordinates and the head model manually, as explained in a later section.
- The entry *Associated MRI file for plotting* contains the name of the
MRI image to use for plotting. You may enter a custom or individual
subject MR image file, assuming this file has first been normalized to
the MNI brain. The [SPM software](https://www.fil.ion.ucl.ac.uk/spm/) will
take a raw subject MRI as input and normalize it to the MNI brain template.
- The entry *Associated channel locations if any* contains the name of the
template channel location file associated with the head model. This
information is critical, as your dataset channel location file may be
different from the template. If so, a co-registration transform is
required to align your channel locations using the template locations
associated with the model.
- Edit box *Channel to omit channels from dipole fitting*. By
pressing "*...*", a list of channels appears that allows users to exclude
eye channels (or other, possibly non-head channels) from the dipole
fitting procedure. For example, non-scalp channels should be removed
prior to running dipole fitting. We advise excluding peri-ocular channel values from inverse source
models because of poor conductance model geometry at the front of the head.

Next is the coregistration, which is explained in detail in the following
sections.

### The default headmodels

The first default head model for Fieldtrip is a spherical head model. This is the 

### Avoiding co-registration by choosing appropriate channel locations

It is ideal if your channel locations are the same as the ones associated with the head model. 
In the dataset we are using here, the channel locations are in the spherical
coordinate system, while we want to use a BEM head model. 
If all your electrode locations are within the International 10-20 System (which is the case here),
you may use the standard channel coordinates associated with the head
model. Close the current head model settings window and go to the channel editing window
(select menu item <span style="color: brownn">Edit → Channel location</span>).
The resulting channel editor window is shown below:

![600px\|border](/assets/images/Dipfit_pop_chanedit2.png)

Press the *Look up locs* to look up your channel locations (by matching
the channel labels) in the template channel location file. Select *Use MNI coordinate file for
the BEM DIPFIT model*.

![](/assets/images/chanlocs_bem.png)

Press *Ok* on the window above and the channel editor window. Then go back to the head model settings using the <span style="color: brown"> Tools → Locate dipoles using DIPFIT
→ Head model and settings</span> menu item. The window below will pop up. You can see that
the matrix to align the electrode coordinate to the head model (edit box *Matrix to align chan. locs with head model*) mainly contains -pi/2 (-1.5708), which correspond to a 90-degree rotation in the axial plane (also known as
the transverse or horizontal plane). This is because EEGLAB assumes that the nose direction is
along a specific axis, while the head model uses a different convention. The Talairach transformation matrix,
a vector comprised of nine fields *\[shiftx shifty shiftz pitch roll yaw scalex scaley scalez\]*, is organized as follow:
- The first 3 numbers *\[shiftx shifty shiftz\]* are the offset (in millimeters) along the x, y, and z axes. When equal to 0, no shift is applied.
- The next 3 numbers *\[pitch roll yaw\]* are rotations along different planes in radian. *Yaw* means rotation in the horizontal plane around the z axis. *Pitch* and *Roll* are rotations around the x and y axes, respectively. When equal to 0, no rotation is applied.
- The last 3 numbers *\[scalex scaley scalez\]* are scaling factors along the x, y, and z axes. When equal to 1, no scaling is applied.

In this case, the only alignment required is a 90-degree rotation between the electrode coordinates and the coordinate system of the head model. In case no co-registration/alignment is required, you may also select the *No coreg* checkbox.

![](/assets/images/dipfit_settings_bem.png)

*Important note:* If you change your channel locations, make sure
to go back to DIPFIT settings to update the coordinate transformation
settings.

### Manual coregistration or fine-tuning of coregistration

If you are using channel locations and/or labels *not* in the
International 10-20 System -- for example, scanned electrode positions
or some commercial high-density electrode cap file -- you will need to
align or co-register your electrode locations with the selected head
model. The coregistration interface does not automatically allow you to align your electrode
locations to the head model. Instead, it allows you to automatically align your
electrode locations to matching template electrode locations associated
with the head model.

Again, use the <span style="color: brown"> Tools → Locate dipoles using DIPFIT
→ Head model and settings</span> menu item. Click on *Manual coreg.* in the DIPFIT settings window. A window appears. Change the *resize* values to 1.5 for all axes to see the electrodes (we are undoing the alignment for illustrative purposes).

![](/assets/images/coregister_new1.png)

Here, the electrode
locations are plotted on the head model. Each small red or green sphere indicates an electrode location,
with fiducial locations (conventionally, the nasion and ear canal
centers) drawn as slightly bigger and darker spheres.

Use the *Warp* button to align and scale your electrode locations (green)
so that it becomes best aligned with the template electrode locations (brown) associated with the head model.

A channel correspondence window will pop up:

![Image:Pop_chancoresp.gif](/assets/images/Pop_chancoresp.gif)

The channel labels from your dataset electrode structure are shown in
the right column, while the left column shows channel labels from the
template channel file associated with the head model. Arrows in both
columns indicate electrodes with the same labels in the other column. If
your channels' labels do not correspond to the International 10-20 System
labels used in the template montage, press the *Pair channels* button
and choose the nearest channel to each of your dataset channels in the
template montage.

When you press *Ok*, the function will perform the optimal linear 3-D
warp (translation, rotation, and scaling) to align your channel montage
to the template montage associated with the head model. The result will be shown in the channel montage window (see
below). You may press the *Labels on* button to toggle the display of your
channels' label (green) or the template
channels associated with the head model (red). You may also restrict
the display to subsets of channels using the *Electrodes* buttons.

<u>Manual fine-tuning:</u> To finely tune the alignment manually, repeatedly edit the values in the edit boxes, which correspond to the *\[shiftx shifty shiftz pitch roll yaw scalex scaley scalez\]* transformation mentioned previously. The resulting co-registration window should look something like this:

![Image:coregister_new2.png](/assets/images/coregister_new2.png)

If you want to retain your modifications, press *Ok* to update the DIPFIT settings
window. This will display the resulting Talairach transformation matrix in the edit box *Matrix to align chan. locs with head model*. In this specific case, you may press the *Cancel* button in the coregistration interface since no further alignment was necessary (we performed coregistration for illustrative purposes on a dataset that did not require further alignment). Then press *Ok* in the DIPFIT settings
window and proceed to localization in the next section of the tutorial.

<u>Note about fiducials:</u> Your channel structure may contain standard
fiducial locations (nasion and pre-auricular points). If you import a
channel file with fiducial locations into the channel editor, give them the standard *fiducial* channel type *FID*, and they will
be stored in the channel information structure, *EEG.chaninfo*. This
will also be done automatically if your fiducials have the standard
names, *Nz* (nasion), *LPA* (left pre-auricular point), and *RPA* (right
pre-auricular point ). There is also considerable confusion about
fiducials, and we have created new fiducial labels in an attempt to
disambiguate exact fiducial locations (see this
[slide](https://sccn.ucsd.edu/eeglab/download/Fiducials.pdf)). Note that
fiducial locations are stored outside the standard channel location
structure, *EEG.chanlocs*, for compatibility with other EEGLAB plotting
functions.

Thereafter, fiducial locations will appear in the channel
co-registration window (above) and may be used (in place of
location-matched scalp channels) to align your electrode montage to the
template locations associated with the head model. Use the *Align
fiducials* button to do this.

Head model and custom MRI
-----

When plotting dipole sources in the next [section of the tutorial](/tutorials/09_source/DIPFIT.html), you may plot the head model head surface and the MRI. 

![Image:model_align.png](/assets/images/head_mesh.png)

In this case, we are using the tutorial data and the standard BEM model described in the previous sections. The BEM head model mesh was extracted from the average MRI used for plotting, so the alignment is perfect. When using participants' MRI and transformed them to MNI space (for example, using SPM), this allows checking the alignment between the MRI and the head model. 

It is also possible to compute extract 3-D meshes from your participants' MRI and use them to create head models as described in this [Fieldtrip tutorial](http://www.fieldtriptoolbox.org/workshop/baci2017/forwardproblem/). If you have a custom head model, use the dropdown menu *Custom model files from other template or individual subject* in the head model settings. A custom head model for MEG is also possible and described in the next section of the tutorial.
