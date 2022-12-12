---
layout: default
title: d. Custom head model
long_title: d. Using a custom head model
parent: 9. Source analysis
grand_parent: Tutorials
---
Better electrode locations
===========================
The use of a custom head model may improve source localization. It is most important for MEG because 
MEG can usually not adapt a custom head model to match the individual subject head geometry. By contrast with
EEG, if we have scanned electrode position, these contain information about the subject's head geometry
and may be used to deform/adapt a template head model.

Therefore one should consider first to scan EEG electrode positions. Even without the subject's MRI, this
will greatly improve the accuracy of source localization because:
- We may deform the template head model to adapt to the subject head geometry
- The template electrode location (in the 10-20 system) differ greatly between manufacturers. My Fz may not be your Fz.
- Scanning electrode position has become easy and innexpensive with modern smartphone that contains 3-D scanners
(iPhone 13 pro, Samsung Galaxy S20 Ultra, etc...).  

We are actively developping solution to assist in 3-D scanning of electrode position, and improve our 
[get_chanlocs plugin](https://github.com/sccn/get_chanlocs/wiki), itself based on a solution 
developped in [Fieldtrip](https://www.fieldtriptoolbox.org/tutorial/electrode/). Our goal is to provide
automated alignment solutions to simplify the identification of electrodes in 3-D scans.

![Screen Shot 2022-12-10 at 12 26 58 PM](https://user-images.githubusercontent.com/1872705/206874056-8a2e646e-aff5-4a8b-b342-292725f6ae88.png)

If you have scanned electrode position and wish to use them for source localization, you may follow the [DIPFIT settings](Model_Settings.md) tutorial.

Custom head model
=================
If you have the scanned electrode positions, and also happen to have the subjects' MRI, then you may build a custom head model. It is important to use the non-defaced MRI. Sometimes, the face of the subject will be removed from the MRI for privacy purposes. Such MRI may not be used to build a head model. The first reason is that it will not be possible to precisely select fiducials in the MRI as the nazion is often missing. The second reason is that you will not be able to extrac the surface for the face of the subject. These surfaces influence volume conduction. 

In this tutorial, we will use the popular Henson Wakeman dataset. The dataset is available [here](https://nemar.org/dataexplorer/detail?dataset_id=ds000117). We will only use some files from the first subject which are available [here](https://sccn.ucsd.edu/eeglab/download/ds000117_sub-01.zip). Some MRI overlay plots shown below are from Fieldtrip. DIPFIT is an extension of EEGLAB that leverage Fieldtrip for source localization.

## Aligning MRI with fiducials

Let's first import the data using menu item <span style="color: brown">File > Import data > Using the File-IO interface</span>, and select the *sub-01_ses-meg_task-facerecognition_run-01_meg.fif* file in the *ses-meg* folder. The fiducials are stored in the *sub-01_ses-meg_coordsystem.json*. EEGLAB will automatically detect this file and import the fiducials. When using other data formats, fiducials will usually be defined along with electrode locations. You may add the fiducials manually using menu item <span style="color: brown">Edit > Channel locations</span>.

Then let's select EEG channels since this dataset contains both EEG and MEG data. Use menu item <span style="color: brown">Edit > Select data</span> and select all the channels starting with EEG. 

The fiducials are automatically aligned with the MRI in this example. However, it is always good to check the alignment. Call menu item <span style="color: brown">Tools > Source localization using DIPFIT > Create head model from MRI</span>. A windows pop up asking you to choose an MRI, and then the following GUI appears.

![Screen Shot 2022-12-11 at 3 35 19 PM](https://user-images.githubusercontent.com/1872705/206955411-513057c1-46e4-4f7c-ab77-c11493feedb0.png)

This will first pop up the fiducials. We can see below that the fiducials are where we would expect them to be.

![Screen Shot 2022-12-11 at 3 37 03 PM](https://user-images.githubusercontent.com/1872705/206935920-b0f5e662-8571-40af-bba3-709eed80e306.png)

Then the MRI is segmented into brain, skull, and scalp, and mesh are extracted. It is important to note that it is better to use Freesurfer to segment MRI and create mesh, as it is a more precise (albeit more time consuming process). The added advantage is that various Atlases are defined which may be used with the EEGLAB [ROIconnect](https://github.com/arnodelorme/roiconnect) plugin. The [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) uses the 'bemcp' method, which is an external module to Fieldtrip to extract mesh. Again, this might not be the best solution -- the default in Fieldtrip is to the "dipoli" method although it only works on Linux and Windows. You may change these settings while calling the [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) function.

![Screen Shot 2022-12-11 at 7 39 20 PM](https://user-images.githubusercontent.com/1872705/206955695-e1522efe-793e-4fcc-a3ed-4b8573db67cf.png)

Once, this is done, call menu item <span style="color: brown">Tools > Source localization using DIPFIT > Head model and settings</span>. We can see that the head model, MRI and associated coordinate landmarks are blanked out. The graphic interface also show that we are editing a custom head model in the Fieldtrip format.

![Screen Shot 2022-12-11 at 7 43 48 PM](https://user-images.githubusercontent.com/1872705/206956553-435a3f9f-48db-4bff-b714-4fddc37aa3f6.png)

Press the Co-register button, and then in the co-registration windown, select *Align fiducials*, and press OK in the window allowing you to select the pairs of channels. Align fiducials apply a rigid transformation, which is what we want because the fiducial in the MRI and the fiducials in channel space should not need to be stretched along any dimension (they are the same). The coregistration window will show a non perfect alignment, which we can then adjust manually. The electrodes should be above the scalp. The misalignemnt are due to uncertainty associated with selecting fiducials. 


Press OK to close the co-registration graphic interface, and then OK to close the dipole settings graphic interface. We are now ready to localize some ICA components.

## Scripting it

<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'source_reconstruction_custom_mri.m'));">Show MATLAB command</button>

The script in this section assume that you have installed the following plugins from the EEGLAB plugin manager: File-IO, Fieldtrip, Picard, and bids-matlab-tools. We first assume you have defined the following file names for the (1) raw data, (2) associated fiducials, and (3) anatomical MRI.

```matlab
dataPath = '/System/Volumes/Data/data/practicalMEEG/Data/ds000117_run1/sub-01';
filenameEEG = fullfile( dataPath, 'ses-meg','meg','sub-01_ses-meg_task-facerecognition_run-01_meg.fif');
filenameFID = fullfile( dataPath, 'ses-meg','meg','sub-01_ses-meg_coordsystem.json');
filenameMRI = fullfile( dataPath, 'ses-mri','anat','sub-01_ses-mri_acq-mprage_T1w.nii.gz');
```

The first step is to import the data. In the script below, we assume that you select EEG channels. However, you may select MEG channels as well as show in the tutorial script. Source localization will work with both EEG and MEG channel, although not simultaneously. The coordinate of the fiducials are stored in the coordsystem JSON file in this case, and is automatically detected and imported. However, they may be included in your data file if you use another file format. 

```matlab
EEG = pop_fileio(filenameEEG); % import data
EEG = pop_select(EEG, 'chantype', 'eeg'); % select EEG channels
```

Then let's preprocess the data to generate some ICA component which may be used for source localization. This involve resampling the data, filtering it, rereferencing it, and running ICA. Note that we have not done proper artifact rejection here. The goal is only to quickly obtain some ICA components for source localization purpose.

```matlab
% Preprocess and run ICA (so one may be localized)
EEG = pop_resample(EEG, 100);
EEG = pop_eegfiltnew(EEG, 1, 0);
EEG = pop_reref(EEG, []);
EEG = pop_runica( EEG , 'picard', 'maxiter', 500, 'pca', 20); % PCA not recommended if you have enough data
```

Finally we import the MIR and the associated file with the coordinates of the fiducials in MRI space (the file is automatically detected. Alternatively [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) will accept fiducials. If you have an MRI and have not selected the fiducials, you may use the Fieldtrip function *ft_volumerealign.m* interactive method to do so, and then provide them as input to the [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) function.

```matlab
EEG = pop_dipfit_headmodel( EEG, filenameMRI, 'plotmesh', 'scalp');
EEG = pop_dipfit_settings( EEG, 'coord_transform', 'alignfiducials');
EEG = pop_multifit(EEG, 1:10,'threshold', 100, 'dipplot','off'); 
pop_dipplot(EEG, [], 'normlen', 'on');
```

The first command creates the head model from the MRI, segmenting it using Fieldtrip functions, which itself uses SPM functions. It is important to note that it is better to use Freesurfer to segment MRI and create mesh, as it is a more precise (albeit more time consuming process). The added advantage is that various Atlases are defined which may be used with the EEGLAB [ROIconnect](https://github.com/arnodelorme/roiconnect) plugin. The [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) uses the 'bemcp' method, which is an external module to Fieldtrip to extract mesh. Again, this might not be the best solution -- the default in Fieldtrip is to the "dipoli" method although it only works on Linux and Windows. You may change these settings while calling the [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) function.

The second command align EEG or MEG electrodes with the head model and MRI. This is based on aligning fiducials which are both defined for the MRI and for the sensors. The alignment is performed automatically above, but it is always a good idea to check that the alignnment is correct. You may use the *plotalignment* option of the [pop_dipfit_settings.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_settings.m) to check the alignemnt.

The hard part has been done of aligning all head model and electrodes. Next, we can perform dipole search as in regular DIPFIT. It is also possible to define a source model to perform eLoreta or LCMV Beamforming as describe [here](https://eeglab.org/tutorials/09_source/EEG_sources.html).

## Other head models

The EEGLAB functions interface Fieldtrip, so you may also use Fieldtrip and place a file containing the head model, the MRI and the fiducials (associated with the MRI) in the respective DIPFIT structures. Note that the file containing the fiducials must have their coordinate transformed to match the MRI modified coordinate frame. Any data format for the electrode that may be read by the [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) function is acceptable. The Fieldtrip tutorials used for this section are available here for [EEG](https://www.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/), here for [MEG](https://www.fieldtriptoolbox.org/tutorial/headmodel_meg/). Another [MEG tutorial](https://www.fieldtriptoolbox.org/workshop/practicalmeeg2022/handson_anatomy/) uses the same data.

```matlab
EEG.dipfit.hdmfile = 'headmodel.mat';
EEG.dipfit.mrifile = 'mrifile.mat';
EEG.dipfit.chanfile = 'fiducials.sfp';
EEG.dipfit.coordformat = 'MNI';
EEG = pop_dipfit_settings(EEG, 'coord_transform', 'alignfiducials'); % align MEEG fiducials with the MRI fiducials. Use EEG = pop_dipfit_settings(EEG) to  perform manual alignment
```

If you are using the EEGLAB graphic interface, you can update it using the following commands.

```
EEG.saved = 'no';
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG);
eeglab redraw;
```


The use of a custom head model may improve source localization. It is most important for MEG because 
MEG can usually not adapt a custom head model to match the individual subject head geometry. By contrast with
EEG, if we have scanned electrode position, these contain information about the subject's head geometry
and may be used to deform/adapt a template head model.

Therefore one should consider first to scan EEG electrode positions. Even without the subject's MRI, this
will greatly improve the accuracy of source localization because:
- We may deform the template head model to adapt to the subject head geometry
- The template electrode location (in the 10-20 system) differ greatly between manufacturers. My Fz may not be your Fz.
- Scanning electrode position has become easy and innexpensive with modern smartphone that contains 3-D scanners
(iPhone 13 pro, Samsung Galaxy S20 Ultra, etc...).  

We are actively developping solution to assist in 3-D scanning of electrode position, and improve our 
[get_chanlocs plugin](https://github.com/sccn/get_chanlocs/wiki), itself based on a solution 
developped in [Fieldtrip](https://www.fieldtriptoolbox.org/tutorial/electrode/). Our goal is to provide
automated alignment solutions to simplify the identification of electrodes in 3-D scans.
