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
module. Therefore all the major manufacturers may be imported (CTF,
Neuromag, Neuroimaging 4-D, BTi). There is also the native *ctfimport* EEGLAB plugin to import CTF data.

The BIDS-matlab-tools EEGLAB plugin also support importing BIDS formated MEG data. You may install this plugin from the EEGLAB plugin manager (menu item File > Manage EEGLAB extensions). 

MEG data may be processed as EEG data, although there is added complexity
for some data formats. For example, EEGLAB does not differentiate
between gradiometers and magnetometers for Neuromag data. For
plotting purposes, you should only keep one type of data.

Here we show how to import and plot Neuromag MEG and CFT data. 

Importing Neuromag MEG data
---------------------------

For Neuromag data, you may use the popular "multisubject, multimodal face processing" dataset ds000117. Instead of downloading the entire dataset, you may download the file *sub-01_ses-meg_task-facerecognition_run-01_meg.fif* in the *sub-01/ses-meg/meg* folder. After starting EEGLAB, select menu item <span style="color: brown">File > Import data > Using the File-IO interface</span>. You are then asked if you want to import a file or a folder. Select the button to import a file and select the file above.

![Screen Shot 2022-12-22 at 11 47 49 PM](https://user-images.githubusercontent.com/1872705/209294989-34f958d5-6cc9-4639-9662-c96cf4217204.png)

Leave all the import options as default and press OK. Next use menu item <span style="color: brown">Edit > Select data</span>. Click the button to browse channel types and select *megmag* to select the magnetometer channels. Press OK and then OK again to select these channels and remove other channels.

![Screen Shot 2022-12-22 at 10 56 53 PM](https://user-images.githubusercontent.com/1872705/209293499-5f5a06c4-7cf4-45a8-8d89-e323e888cddc.png)

Let's now plot the data spectrum. Use menu item <span style="color: brown">Plot > Channel spectra and maps</span>. Change the frequency at which to plot spectral power to 7 and 15 Hz. You may also change the option to plot the electrodes. Press OK, and the following spectrum appears.

![Screen Shot 2022-12-22 at 11 42 39 PM](https://user-images.githubusercontent.com/1872705/209294152-ee22cc89-46d5-429d-a0de-31fa31a83d37.png)

Importing CTF MEG data
----------------------



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
