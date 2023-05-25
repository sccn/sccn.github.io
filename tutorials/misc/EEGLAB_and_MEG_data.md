---
layout: default
title: EEGLAB and MEG data
long_title: EEGLAB and MEG data
parent: Reference Topics
grand_parent: Tutorials
---
EEGLAB and MEG data
====================

EEGLAB supports reading most MEG data formats through the File-IO
extension. Therefore MEG data from all the major manufacturers may be imported (CTF, Neuromag, Neuroimaging 4-D, BTi). There is also a native *ctfimport* EEGLAB plugin to import CTF data, although we recommend using the File-IO extension first.

The [BIDS-matlab-tools](https://github.com/sccn/bids-matlab-tools) EEGLAB plugin also supports importing BIDS-formated MEG data. You may install this plugin from the EEGLAB plugin manager (menu item <span style="color: brown">File > Manage EEGLAB extensions</span>). 

Below, we show how to import and plot Neuromag MEG and CFT MEG data. For further processing, you should use the EEG tutorial. We recommend using the [clean_rawdata](https://github.com/sccn/clean_rawdata) EEGLAB plugin to clean data (find bad channels and bad portions of data). We also recommend using Independent Component Analysis (ICA) to remove artifacts. Unfortunately, artifactual ICA components need to be manually labeled. Automated methods such as [ICLabel](https://github.com/sccn/ICLabel) and [MARA](https://irenne.github.io/artifacts/) that automatically detect ICA artifacts do not apply to MEG data (they were trained with EEG data, and would need to be retrained with MEG data).

Importing Neuromag MEG data
---------------------------

For Neuromag data, as an example, we will use the popular "multisubject, multimodal face processing" [dataset](https://nemar.org/dataexplorer/detail?dataset_id=ds000117). Instead of downloading the entire dataset, you may download the file *sub-01_ses-meg_task-facerecognition_run-01_meg.fif* in the *sub-01/ses-meg/meg* folder. After starting EEGLAB, select menu item <span style="color: brown">File > Import data > Using the File-IO interface</span>. You are then asked if you want to import a file or a folder. Select the button to import a file and select the file above on your computer.

![Screen Shot 2022-12-22 at 11 47 49 PM](https://user-images.githubusercontent.com/1872705/209294989-34f958d5-6cc9-4639-9662-c96cf4217204.png)

Leave all the import options as default and press OK. Next, we will select the MEG channel we want to process and plot. Use menu item <span style="color: brown">Edit > Select data</span>. Click the button to browse channel types and select *megmag* to select the magnetometer channel type. Press OK and then OK again to select these channels and remove other channels.

![Screen Shot 2022-12-22 at 10 56 53 PM](https://user-images.githubusercontent.com/1872705/209293499-5f5a06c4-7cf4-45a8-8d89-e323e888cddc.png)

Let's now make a simple plot, for example, the MEG data spectrum. Use menu item <span style="color: brown">Plot > Channel spectra and maps</span>. Change the frequency to plot spectral power to 7 and 15 Hz. You may also change the option to plot the electrodes. Press OK, and the following spectrum appears. For further preprocessing, see the EEG tutorial. 

![Screen Shot 2022-12-22 at 11 42 39 PM](https://user-images.githubusercontent.com/1872705/209294152-ee22cc89-46d5-429d-a0de-31fa31a83d37.png)

Importing CTF MEG data
----------------------
For CTF, we will use a more challenging dataset than the one above. Some CTF datasets have sensor locations associated with them, but this is not always the case. We will use the [tutorial data](https://nemar.org/dataexplorer/detail?dataset_id=ds000246) for Brainstorm, which has the advantage of being small in size and easy to download. However, this dataset does not have sensor locations. 

First, download the data, and then let's first import the data. After starting EEGLAB, select menu item <span style="color: brown">File > Import data > Using the File-IO interface</span>. You are then asked to import a file or a folder. Select the button to import a folder and select the folder *sub-0001_task-AEF_run-01_meg.ds* located in the *sub-0001/meg* subfolder. We recommend you check the checkbox *Convert data trials to continuous data*. CTF data is sometimes stored as trials because it is large and may not all be processed in the computer memory. Storing the data as trials allows data to be loaded one trial at a time. This made sense one or two decades ago, but this limitation is obsolete since most computers can now load and process an entire dataset. MEG data trials are often contiguous, so we may convert the data trials back to continuous data. We recommend using that option since filtering data trials can lead to [a decrease in statistical power](https://www.biorxiv.org/content/10.1101/2022.12.03.518987v1). Press OK when done.

![Screen Shot 2022-12-23 at 12 26 48 PM](https://user-images.githubusercontent.com/1872705/209402761-fcce17a6-aac0-47cb-8bb6-a5b501edf7f0.png)

Let's then remove non-MEG channels. Unlike the Neuromag dataset, we cannot select channels by type in this dataset, so we will select channels by name (note that some CTF datasets have channel types, but this is not one of them). Use menu item <span style="color: brown">Edit > Select data</span>. Click the button to browse channels and select channels *MLC11-4408* to *MZP01-4408*. Press OK and then OK again to select these channels and remove other channels. You should be left with 274 channels.

![Screen Shot 2022-12-23 at 11 52 43 AM](https://user-images.githubusercontent.com/1872705/209402624-82ab9561-a4a7-4631-8b39-da69bb81d449.png)

Next, we need to assign sensor locations. To do so, call menu item <span style="color: brown">Edit > Channel locations</span>, then press the *Look up locs* button. Select the file *CTF275_helmet.mat*, a layout file for 2-D plotting (this type of file must not be used for 3-D plotting or source localization), and check the checkbox to import the file instead of looking up channel locations. Looking up channel locations would be fine except for the channels' names, which have the "-4480" postfix. To look up channel locations, we would first need to remove the postfix on the MATLAB command line, then EEGLAB would be able to look up the channel in the layout files. But let's instead import the layout file. So press OK to import the layout file.

![Screen Shot 2022-12-23 at 12 31 38 PM](https://user-images.githubusercontent.com/1872705/209403077-a3abcf6b-104a-43fe-aecc-7b19bf7b237c.png)

For some reason, the current dataset is missing channel MRT27, so we need to remove it from the layout. We also need to remove the last 2 channels, *COMNT* and *SCALE*, which are no longer in the dataset. Find channel MRT27, and press the *delete* button. Then find the last two channels and delete them as well. You should be left with 274 channels which is the number of data channels. If you do not have 274 channels, EEGLAB will complain and ignore the channel location you have imported (the number of channels having data must correspond to the number of channel locations).

![Screen Shot 2022-12-23 at 12 40 57 PM](https://user-images.githubusercontent.com/1872705/209403788-6ef250ea-ff64-416f-872c-5648fd6e1bd6.png)

Now use menu item <span style="color: brown">Plot > Channel spectra and maps</span> to plot the spectrum. Change the frequency at which to plot spectral power to 10 Hz. You may also change the option to plot the electrodes. Press OK, and the following spectrum appears.

![Screen Shot 2022-12-23 at 12 05 21 PM](https://user-images.githubusercontent.com/1872705/209403909-5cef619b-86db-481a-baad-f8a750f2bd25.png)

To perform source localization with this data, you would need to obtain the 3-D location from the sensor (instead of a 2-D layout). These may be obtained from other datasets recorded with the same system (for example, the [NIMH Intramural Healthy Volunteer Dataset](https://openneuro.org/datasets/ds004215/versions/1.0.1) has it; The [Mother of unification studies](https://data.donders.ru.nl/collections/di/dccn/DSC_3011020.09_236?0) dataset has them as well). Once you have imported these datasets, you may use menu item <span style="color: brown">Edit > Dataset info</span>, and for the channel locations, use the button *From other datasets*. You will need to check that the two datasets have the same number of data channels and the same channel labels.

EEGLAB will automatically detect that you are processing MEG data and adjust the topographic plots. However, if this is not the case, you may manually change the plotting settings on the MATLAB command line. To do so, type:

```matlab
EEG.chaninfo.topoplot = { 'headrad' 0.3 'conv' 'on'};
eeglab redraw
```

These commands change the size of the head and use a convex hull to determine the channel plotting limit. 

Source localization using MEG
-----------------------------
Unlike EEG, MEG source localization usually uses the subject anatomical MRI, and these are usually available. In this tutorial, we will use the popular [Henson-Wakeman dataset](https://nemar.org/dataexplorer/detail?dataset_id=ds000117). We will only use some files from the first subject, available [here](https://sccn.ucsd.edu/eeglab/download/ds000117_sub-01.zip). The MRI overlay plots shown below are from Fieldtrip. DIPFIT is an extension of EEGLAB that leverages Fieldtrip functions for equivalent dipole source model localization. This tutorial is very similar to [the one using EEG](../Source_09/Custom_head_model.md) on the same data.

## Aligning MRI with fiducials

We first import the data using menu item <span style="color:brown">*File > Import data > Using the File-IO interface*</span>, and select the *sub-01_ses-meg_task-facerecognition_run-01_meg.fif* file in the *ses-meg* folder. The fiducials are stored in the *sub-01_ses-meg_coordsystem.json*. EEGLAB will automatically detect this file and import the fiducials. When using other data formats, fiducials will usually be defined along with electrode locations. You may add the fiducials manually using menu item <span style="color:brown">*Edit > Channel locations*</span>.

Then we select MEG channels since this dataset contains both EEG and MEG data. Use menu item <span style="color:brown">Edit > Select data</span> and select all the *megplanar* channel type.

![Screen Shot 2022-12-23 at 3 37 38 PM](https://user-images.githubusercontent.com/1872705/209413866-4c6d647c-26da-465c-8527-db09ffc2e4ea.png)

Then call menu item <span style="color:brown">Tools > Source localization using DIPFIT > Create a head model from an MRI</span>. A window asks you to choose an MR head image, and the following GUI appears.

![Screen Shot 2022-12-11 at 3 35 19 PM](https://user-images.githubusercontent.com/1872705/206955411-513057c1-46e4-4f7c-ab77-c11493feedb0.png)

This will first pop up the fiducials. The fiducials are automatically aligned with the MR head image in this example. However, it is always good to check the alignment. We can see below that the fiducials are where we would expect them to be (the thin blue lines indicate their positions).

![Screen Shot 2022-12-11 at 3 37 03 PM](https://user-images.githubusercontent.com/1872705/206935920-b0f5e662-8571-40af-bba3-709eed80e306.png)

Then the MRI is segmented into the brain, skull, and scalp, and meshes are extracted. It is important to note that it is better to use Freesurfer to segment MRI and create meshes, as it is a more precise (albeit more time-consuming process). The [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) uses the "bemcp" method, a module external to Fieldtrip, to extract meshes. Again, this is the most cross-platform compatible solution but might not be the best one.

![Screen Shot 2022-12-11 at 7 39 20 PM](https://user-images.githubusercontent.com/1872705/206955695-e1522efe-793e-4fcc-a3ed-4b8573db67cf.png)

Once this is done, call menu item <span style="color:brown">Tools > Source localization using DIPFIT > Head model and settings</span>. We can see that the head model, MRI, and associated coordinate landmarks are blanked out. The graphic interface also shows that we are editing a custom head model in the Fieldtrip format.

![Screen Shot 2022-12-11 at 7 43 48 PM](https://user-images.githubusercontent.com/1872705/206956553-435a3f9f-48db-4bff-b714-4fddc37aa3f6.png)

Press the *Co-register* button, and then in the co-registration window, select *Align fiducials*, and press OK in the window, allowing you to select the pairs of channels. *Align fiducials* applies a rigid transformation, which is what we want because the fiducials in the MRI and the fiducials in channel space should not be stretched along any dimension (they are the same). The coregistration window will show a nonperfect alignment (left), which we can then adjust manually (right) by changing scaling and offsets. The electrodes should be above the scalp. The misalignment is due to uncertainty associated with [selecting fiducials](https://eeglab.org/tutorials/ConceptsGuide/coordinateSystem.html#eeglab-electrode-coordinate-systems). 

![Screen Shot 2022-12-11 at 11 06 22 PM](https://user-images.githubusercontent.com/1872705/206982193-92e59b82-90b9-43c5-8e7a-d551a90d66d1.png)

Press 'OK' to close the co-registration graphic interface and then 'OK' again to close the dipole settings graphic interface. We are now ready to localize some [ICA component scalp projection maps](DIPFIT.md) - or any other [EEG source projection maps](EEG_sources.md).



When the anatomical MRI is not available, not all is lost. For example, this [publicly available dataset](https://openneuro.org/datasets/ds004330/versions/1.0.0) does not contain MRI. What is important is to properly align the template head model with the subject head position in the MEG. This may be done with the fiducials but these are usually not sufficient. Using the fiducials, below we show alignment of the MEG sensors to the template head or to the subject's head extracted from the anatomical MRI. We can see a large difference between the two, even though the template head is stretched to match the subject's fiducial (this was not a rigid transformation). In other words, the fiducials capture the head position, but not the head geometry. If they did, we would expect the template head model to be stretched to match the subject's head.

![Screen Shot 2022-12-23 at 2 26 26 PM](https://user-images.githubusercontent.com/1872705/209410775-d9e51fab-6bff-44fd-a05c-6506e3fcbd18.png)

One way to fix this and use a template head model is to use the location of the EEG channels when they are available. EEG channels are usually scanned in the same coordinate space as the MEG sensors, so aligning and stretching the MEG head model to match the channel coordinates should be able to fix the problem above. A *headshape.pos* file is also sometimes available along with the MEG. It contains data points lying on the head of the subject and may be used to align the MEG sensor space to the anatomical MRI. However, this file may also be used to align and stretch the EEGLAB template MEG boundary element model to match the subject's head. To use this file, create a random data array on the MATLAB command line with the same number of scanned positions *a=rand(150, 1000);* and import it as a MATLAB array. Then, call the channel editor and import the *headshape.pos* file as an *SFP* file. You can then align the scanned position with the BEM head model. Write down the homogeneous transformation matrix and reuse it for the MEG model alignment.

Using templace head model for MEG
---------------------------------
Although it is preferable to use the subject's MRI, it is possible to use the template MNE head model with MEG data. The alignment between the head model and the sensors may be performed using Fiducials. EEG and MEG will use the same boundary element model. For MEG, only the inner surface of the model is being used. Model fitting is performed using FieldTrip.

Sensor vs model space for sources
----------------------------------
Unlike EEG, where source localization is performed in the model space (usually MNI), source localization of MEG is performed in the sensor space. This means that the model is projected to the sensor space. In practice, the EEG.dipfit structure will contain sources in the sensor instead of the model space. The reason for this choice is that it is the way FieldTrip handles MEG data. 

MEG pipeline
------------
We have demonstrated MEG pipelines for the PracticalMEEG workshop. The code for the pipeline is available [here](https://github.com/sccn/practical_MEEG). In all of the scripts, including source localization, users can toggle between using the EEG and MEG data.

Other MEG resources
--------------------
MEG source localization in EEGLAB leverage Fieldtrip capabilities. Any head model designed in Fieldtrip may be used for source localization in EEGLAB. We invite you to check the other MATLAB-based MEG software tools below, which may be used along with EEGLAB from the MATLAB command line.

-   <http://www.nitrc.org/projects/fieldtrip>
-   <http://www.nitrc.org/projects/cuda_sphere_fwd>
-   <http://www.nitrc.org/projects/bst>
-   <http://www.nitrc.org/projects/openmeeg>
-   <http://www.nitrc.org/projects/meg-tools>
-   <http://www.nitrc.org/projects/megsim>
