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

The [BIDS-matlab-tools](https://github.com/sccn/bids-matlab-tools) EEGLAB plugin also supports importing BIDS-formated MEG data. You may install this plugin from the EEGLAB plugin manager (menu item <span style="color: brown">File > Manage EEGLAB extensions</font>). 

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
For MEG source localization, you can use a custom model in DIPFIT within
EEGLAB (there is a specific entry for MEG custom leadfield matrix as explained [here](/tutorials/09_source/DIPFIT.html#using-dipfit-to-fit-independent-meg-components)). EEGLAB is still a solution of choice if you are using
Independent Component Analysis to extract brain sources from MEG data.

However, EEGLAB is not primarily designed to process MEG data and
perform MEG source localization. For advanced MEG source processing that
does not involve ICA, a large number of MEG users directly use specialized MEG
 software. For MEG source localization, some of the most
popular tools include Fieldtrip, Brainstorm, MEG-tools, MEGSIM, NUTMEG,
OpenMEG, MNE suite, or Curry. Some of the links on the popular NITRC
platform are listed shown

-   <http://www.nitrc.org/projects/fieldtrip>
-   <http://www.nitrc.org/projects/cuda_sphere_fwd>
-   <http://www.nitrc.org/projects/bst>
-   <http://www.nitrc.org/projects/openmeeg>
-   <http://www.nitrc.org/projects/meg-tools>
-   <http://www.nitrc.org/projects/megsim>
