---
layout: default
title: d. Custom head model
long_title: d. Using a custom head model
parent: 9. Source analysis
grand_parent: Tutorials
---
Use scanned electrode locations
===========================
The use of a custom head model can improve source localization. For
EEG, scanned electrode positions contain information about the subject's head geometry
and may be used to deform/adapt a template head model. This is not as accurate as co-registering
the measured electrode locations to an individual MR head image - when available - but
is more accurate than fitting template electrode positions to a template head model [Akalin Acar & Makeig, 2013](https://pubmed.ncbi.nlm.nih.gov/23355112/).
Building an electrical forward model for each subject based on their individual MR head image also allows inverse more accurate and meaningful source modeling to the individual convoluted cortical surface. This is not possible using a template forward model as each participant's cortical convolutions cannot be well determined by knowing their skull shape (e.g., based on measured electrode positions).

Even without having the participant's MR head image, having measured 3D positions of the scalp electrodes
will significantly improve the accuracy of source localization, because we may deform the template head model to adapt to the subject head geometry.
Template electrode locations (even for montages based on The International 10-20 System) may differ greatly between manufacturers. 
But scanning the actual 3D positions (relative to head landmarks and one another) has become easy and inexpensive. 
For this we may use modern smartphones that include 3-D scanners
(iPhone 13 pro, Samsung Galaxy S20 Ultra, etc...), or relatively cheap 3D-camera attachments (Structure.io) to standard computer tablets.  

We are further developing the EEGLAB function to assist in recording 3D electrode positions acquired by a 3D camera. 
The [get_chanlocs plug-in](https://github.com/sccn/get_chanlocs/wiki),  based on functions
implemented in [Fieldtrip](https://www.fieldtriptoolbox.org/tutorial/electrode/), assists the data analyst in ascertaining 3D electrode positions from a 3D scanned head image, thus relieving experiment participants of the need to sit through a long period of waiting while technicians use a magnetic or other stylus to record the electrode positions one by one, as was formerly necessary with the Polhemus system for example. 

After 3-D scanning, you may use the [get_chanlocs](https://github.com/sccn/get_chanlocs/wiki) EEGLAB plugin to measure the same electrode positions (one by one) in the scanned head image. This requires a few minutes, and can be further reduced by first saving and thereafter reusing a montage template. It should be possible to use machine vision methods to further automate this process, a feature we hope to introduce during 2023.

![Screen Shot 2022-12-10 at 12 26 58 PM](https://user-images.githubusercontent.com/1872705/206874056-8a2e646e-aff5-4a8b-b342-292725f6ae88.png)

If you have scanned electrode positions and wish to use them for source localization, you may follow the [DIPFIT settings](Model_Settings.md) tutorial. If you also have an MR head image for each participant, you may use EEGLAB's [Neuroelectromagnetic Forward head modeling Toolbox (NFT)](https://github.com/sccn/NFT) to create individual electrical head models that you can either import into DIPFIT or use NFT to fit either equivalent dipole or distributed cortical surface models of effective EEG sources identified in your data by independent component analysis (ICA). In this tutorial, however, we will use the Fieldtrip-related tools to build head models from MR head images.

Custom head models
=================
If you have the scanned 3D electrode positions and also have subject MR head images, then you may build a custom electrical head model for each subject. This model specifies how potentials generated anywhere in the brain volume (by one or more theoretical 'tiny battery' current dipoles) are propagated by volume conduction to the scalp. Often, researchers remove the face of the subject from shared MR head images for privacy purposes. It is preferable to use the non-defaced MRI for electrical head modeling. First, it may not be possible to precisely measure the skull fiducial points in the MRI, as the nasion is often missing. Even if the position of the nasion is available, the structure of the upper face and facial bones of the subject influences volume conduction to the frontal scalp, so it is important to have it when extracting the scalp and skull surfaces. Nevertheless, we will use a defaced MRI in this tutorial -- here with the positions of the nasion and other fiducials provided separately by the data authors.

In this tutorial, we will use the popular [Henson-Wakeman dataset](https://nemar.org/dataexplorer/detail?dataset_id=ds000117). We will only use some files from the first subject, available [here](https://sccn.ucsd.edu/eeglab/download/ds000117_sub-01.zip). The MRI overlay plots shown below are from Fieldtrip. DIPFIT is an extension of EEGLAB that leverages Fieldtrip functions for equivalent dipole source model localization.

## Aligning MRI with fiducials

We first import the data using menu item <span style="color:brown">*File > Import data > Using the File-IO interface*</span>, and select the *sub-01_ses-meg_task-facerecognition_run-01_meg.fif* file in the *ses-meg* folder. The fiducials are stored in the *sub-01_ses-meg_coordsystem.json*. EEGLAB will automatically detect this file and import the fiducials. When using other data formats, fiducials will usually be defined along with electrode locations. You may add the fiducials manually using menu item <span style="color:brown">*Edit > Channel locations*</span>.

Then we select EEG channels since this dataset contains both EEG and MEG data. Use menu item <span style="color:brown">Edit > Select data</span> and select all the channels whose channel labels begin with 'EEG'. Note that you may omit channels 367 to 370 (labels EEG061 to EEG064) which are EOG and ECG channels, and should not be included in EEG-related analyses.

![Screen Shot 2022-12-12 at 9 50 23 AM](https://user-images.githubusercontent.com/1872705/207117594-941ad9e9-5599-4208-89a7-48a93e41bcdc.png)

Then call menu item <span style="color:brown">Tools > Source localization using DIPFIT > Create a head model from an MRI</span>. A window asks you to choose an MR head image, and the following GUI appears.

![Screen Shot 2022-12-11 at 3 35 19 PM](https://user-images.githubusercontent.com/1872705/206955411-513057c1-46e4-4f7c-ab77-c11493feedb0.png)

This will first pop up the fiducials. The fiducials are automatically aligned with the MR head image in this example. However, it is always good to check the alignment. We can see below that the fiducials are where we would expect them to be (the thin blue lines indicate their positions).

![Screen Shot 2022-12-11 at 3 37 03 PM](https://user-images.githubusercontent.com/1872705/206935920-b0f5e662-8571-40af-bba3-709eed80e306.png)

Then the MRI is segmented into the brain, skull, and scalp, and meshes are extracted. It is important to note that it is better to use Freesurfer to segment MRI and create meshes, as it is a more precise (albeit more time-consuming process). The other added advantage is that various Atlases are defined, which may be used with the EEGLAB [ROIconnect](https://github.com/arnodelorme/roiconnect) plug-in. The [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) uses the "bemcp" method, a module external to Fieldtrip, to extract meshes. Again, this might not be the best solution -- the default in Fieldtrip is to the "dipoli" method, although currently this only works on Linux and Windows. You may change these settings by changing the parameter of the [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) function when calling it from the command line.

![Screen Shot 2022-12-11 at 7 39 20 PM](https://user-images.githubusercontent.com/1872705/206955695-e1522efe-793e-4fcc-a3ed-4b8573db67cf.png)

Once this is done, call menu item <span style="color:brown">Tools > Source localization using DIPFIT > Head model and settings</span>. We can see that the head model, MRI, and associated coordinate landmarks are blanked out. The graphic interface also shows that we are editing a custom head model in the Fieldtrip format.

![Screen Shot 2022-12-11 at 7 43 48 PM](https://user-images.githubusercontent.com/1872705/206956553-435a3f9f-48db-4bff-b714-4fddc37aa3f6.png)

Press the *Co-register* button, and then in the co-registration window, select *Align fiducials*, and press OK in the window, allowing you to select the pairs of channels. *Align fiducials* applies a rigid transformation, which is what we want because the fiducials in the MRI and the fiducials in channel space should not be stretched along any dimension (they are the same). The coregistration window will show a nonperfect alignment (left), which we can then adjust manually (right) by changing scaling and offsets. The electrodes should be above the scalp. The misalignment is due to uncertainty associated with [selecting fiducials](https://eeglab.org/tutorials/ConceptsGuide/coordinateSystem.html#eeglab-electrode-coordinate-systems). 

![Screen Shot 2022-12-11 at 11 06 22 PM](https://user-images.githubusercontent.com/1872705/206982193-92e59b82-90b9-43c5-8e7a-d551a90d66d1.png)

Press 'OK' to close the co-registration graphic interface and then 'OK' again to close the dipole settings graphic interface. We are now ready to localize some [ICA component scalp projection maps](DIPFIT.md) - or any other [EEG source projection maps](EEG_sources.md).

## Scripting it

<button onclick="showModal(this)" data-command="eeglabp = fileparts(which('eeglab.m')); open(fullfile(eeglabp, 'tutorial_scripts', 'source_reconstruction_custom_mri.m'));">Show MATLAB command</button>

The script in this section assumes that you have installed the following plug-ins from the EEGLAB plug-in manager: *File-IO*, *Fieldtrip*, *Picard*, and *bids-matlab-tools*. We first assume you have defined the following file names for the raw data and anatomical MRI.

```matlab
dataPath = 'xxx/sub-01';
filenameEEG = fullfile( dataPath, 'ses-meg','meg','sub-01_ses-meg_task-facerecognition_run-01_meg.fif');
filenameMRI = fullfile( dataPath, 'ses-mri','anat','sub-01_ses-mri_acq-mprage_T1w.nii.gz');
```

The first step is to import the data. In the script below, we assume that you select EEG channels. However, you may select MEG channels as well as shown in the tutorial script. Source localization will work with both EEG and MEG channels, although not simultaneously. The coordinates of the fiducials are stored in the *coordsystem* JSON file and are automatically detected and imported. However, if you use another file format, they may be included in your data file. 

```matlab
EEG = pop_fileio(filenameEEG); % import data
EEG = pop_select(EEG, 'chantype', 'eeg'); % select EEG channels
EEG = pop_select(EEG, 'rmchannel', { 'EEG061' 'EEG062' 'EEG063' 'EEG064' }); % remove EOG and EKG channels
```

Then we preprocess the data to generate some ICA components which may be used for source localization. This involves resampling the data, filtering it, re-referencing it, and running ICA. Note that we have not performed proper artifact rejection here. Our tutorial goal is only to quickly obtain some ICA components to demonstrate the equivalent dipole source localization process - this subject's EEG data have sufficiently low noise to allow the ICA decomposition to find component scalp maps that truly resemble the projection of a single equivalent dipole (an oriented model dipole whose scalp projection is 'equivalent' to that of synchronous local field activity across a suitably located and oriented cortical patch). Also, to speed the tutorial process we reduce the dimension of the data to only 20 using PCA, a practice we advise against using unless the data rank is less than the number of channels (*EEG.nbchan*) [see Artoni et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29526744/).

```matlab
% Preprocess and run ICA (so one may be localized)
EEG = pop_resample(EEG, 100);
EEG = pop_eegfiltnew(EEG, 1, 0);
EEG = pop_reref(EEG, []);
% EEG = [IMPORTANT: In actual practice, remove any artifcatual data portions here!]
EEG = pop_runica( EEG , 'picard', 'maxiter', 500, 'pca', 20); % NOTE: In practice, PCA dimension reduction prior to ICA decomposition is NOT recommended
```

Finally, we import the MRI and the associated file with the coordinates of the fiducials in MRI space (the file containing fiducials is automatically detected and imported). Alternatively, [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) will accept fiducials. If you have the subject's MR head image and have not selected the fiducials, you may use the Fieldtrip function *ft_volumerealign.m* interactive method to provide estimates of their positions relative to the head image, and then provide them as input to the [pop_dipfit_headmodel.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_headmodel.m) function.

```matlab
EEG = pop_dipfit_headmodel( EEG, filenameMRI, 'plotmesh', 'scalp');
EEG = pop_dipfit_settings( EEG, 'coord_transform', 'alignfiducials');
EEG = pop_multifit(EEG, 1:10,'threshold', 100, 'dipplot','off'); 
pop_dipplot(EEG, [], 'normlen', 'on');
```

The first command creates the head model from the MRI, segmenting it using Fieldtrip functions, which itself uses SPM functions. The second command aligns EEG or MEG electrodes with the head model and MRI. This is based on aligning fiducials which are both defined for the MRI and for the sensors. The alignment is performed automatically above, but it is always a good idea to check that the alignnment is correct. You may use the *plotalignment* option of the [pop_dipfit_settings.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipfit_settings.m) to check the alignemnt.

Now the hard part of aligning all head model and electrodes has been accomplished. Next, we perform dipole search as in regular DIPFIT by calling the [pop_multifit.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_multifit.m) and plot them using the [pop_dipplot.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_dipplot.m). It is also possible to define a source model to perform eLoreta or LCMV Beamforming, as described [here](https://eeglab.org/tutorials/09_source/EEG_sources.html). A biologically plausible ICA component is shown below.

## Other head models

The EEGLAB functions interface Fieldtrip, so you may also use Fieldtrip and place a file containing the head model, the MR head image, and the fiducials (associated with the MR image) in the respective DIPFIT structures. Note that the file containing the fiducials must have their coordinates transformed to match the MRI-modified coordinate frame. Any data format for the electrode locations that the [readlocs.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=readlocs.m) function can read is acceptable. The Fieldtrip tutorials used for this section are available here for [EEG](https://www.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/), here for [MEG](https://www.fieldtriptoolbox.org/tutorial/headmodel_meg/). Another [MEG tutorial](https://www.fieldtriptoolbox.org/workshop/practicalmeeg2022/handson_anatomy/) uses the same data as in this tutorial.

```matlab
EEG.dipfit.hdmfile = 'headmodel.mat';
EEG.dipfit.mrifile = 'mrifile.mat';
EEG.dipfit.chanfile = 'fiducials.sfp';
EEG.dipfit.coordformat = ''; % may be MNI, this field may be left blank as well
EEG = pop_dipfit_settings(EEG, 'coord_transform', 'alignfiducials'); % align MEEG fiducials with the MRI fiducials. Use EEG = pop_dipfit_settings(EEG) to  perform manual alignment
```

To update the EEGLAB graphic user interface (menu), use the following command sequence.

```
EEG.saved = 'no';
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG);
eeglab redraw;
```

