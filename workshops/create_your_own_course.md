---
layout: default
title: Create your own course
long_title: Create your own course
parent: Workshops
nav_order: 1
---
# Create Your Own EEGLAB Course

This [repository](https://github.com/sccn/EEGLAB_course) contains materials for EEGLAB course sessions. This course was originally conducted at the [practical MEEG 2025 workshop](https://cuttingeeg.org/practicalmeeg2025/).

You may adapt the materials as needed for your own course, although please acknowledge the authors of the materials.

## Course Slides

Lecture slides for the course are available in two formats:

**PDF format:** Available in the [slides](slides/) folder of this repository. The following presentations are included:
- Introduction to the course
- Data preprocessing
- Event-Related Potentials (ERP) analysis
- Spectral and time-frequency analysis
- Source localization and ICA
- Connectivity analysis
- IC clustering
- LIMO statistics
- MVPA (Multivariate Pattern Analysis)

**PowerPoint format:** Editable PowerPoint versions of the slides are available at:
[Google Drive - Course Slides](https://drive.google.com/drive/folders/17EqHqypmM0aIQVuoaDMLbfSnMh8zB_GG?usp=drive_link)

## Prerequisites

### Step 1 – Download and install MATLAB

If you are organizing a course, you can usually obtain a [MATLAB trial version](https://www.mathworks.com/support/contact_us.html) for your participants by contacting the licensing department. Please have your participants install MATLAB in advance so you're ready to run EEGLAB during the course.

### Step 2 – Download the data

This course uses data from the multimodal face recognition BIDS dataset, a pruned version of the OpenNeuro dataset ds000117.

**Download the pruned single-subject dataset (ds000117_pruned):**
[https://zenodo.org/record/7410278](https://zenodo.org/record/7410278)

This dataset contains only one subject and is used in Sessions 1, 2, 3, and 5.

**For group-level analyses (Sessions 4 and 6), also download the preprocessed group dataset (ds002718):**
[https://zenodo.org/records/5528500](https://zenodo.org/records/5528500)

### Folder Structure Setup

The scripts expect the following folder structure:

```
parent_folder/
├── Data/
│   └── sub-01/                    (processed files for Session 4)
└── EEGLAB_course/
    ├── ds002718_5_Subjects/       (preprocessed group data for Session 6)
    ├── ds000117_pruned/           (raw data for Sessions 1, 2, 3, 5)
    │   └── derivatives/
    │       └── meg_derivatives/
    │           └── sub-01/
    │               └── ses-meg/
    │                   └── meg/
    └── (script files: Session_1_Import_Data.m, etc.)
```

**Setup instructions:**
1. Place the `ds000117_pruned` folder **inside** the `EEGLAB_course` folder (used by Sessions 1, 2, 3, 5)
2. Place the `ds002718_5_Subjects` folder **inside** the `EEGLAB_course` folder (used by Session 6)
3. Create a `Data` folder in the **parent** folder of `EEGLAB_course` and extract:
   - Processed single-subject files to `Data/sub-01/` (for Session 4)

**Note:** Sessions 1-3 generate processed files. Session 4 expects to find these in the parent `Data/sub-01/` folder, so you may need to copy output files from earlier sessions there.

### Step 3 – Download EEGLAB

Now it's time to clone the EEGLAB Git repository on your computer.

**Warning:** Do not download the ZIP file directly from GitHub, as it does not include EEGLAB submodules.

Instead, use the following command to clone the repository and pull its submodules:

```bash
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

Or download from the [EEGLAB website](https://sccn.ucsd.edu/eeglab/download.php).

### Step 4 – Check that EEGLAB runs

1. Start MATLAB
2. In MATLAB, navigate to the folder containing the EEGLAB repository
3. At the MATLAB command prompt (>>), type: `eeglab`
4. The EEGLAB main interface should appear

If it opens without errors, you're all set for the workshop!

### Step 5 – Download the course scripts

During the course, participants will follow along and do hands-on work using the EEGLAB graphical interface. However, they can also run the scripts provided in this repository.

Clone this repository:

```bash
git clone https://github.com/sccn/EEGLAB_course.git
```

Or download the ZIP on GitHub.

## Course Content Overview

The course materials are organized into several sessions, each focusing on different aspects of EEG/MEG data analysis using EEGLAB.

### Session 1: Preprocessing

For this presentation, we will first import the data with the [Session_1_Import_Data.m](Session_1_Import_Data.m) script. This script has 11 steps. 

* Step 1: Importing MEG data files with FileIO
* Step 2: Adding fiducials and rotating montage
* Step 3: Recomputing head center (for display only)
* Step 4: Re-import events from STI101 channel (the original ones are incorect)
* Step 5: Selecting EEG or MEG data 
* Step 6: Cleaning artefactual events (keep only valid event codes)
* Step 7: Fix button press info
* Step 8: Renaming button press events
* Step 9: Correcting event latencies (events have a shift of 34 ms as per the authors)
* Step 10: Replacing original imported channels
* Step 11: Creating folder to save data if does not exist yet

After importing the data, it is preprocessed using the [Session_1_Preprocess_Data.m](Session_1_Preprocess_Data.m) script. This script itself has several steps.

* Re-Reference the data
* Resampling the data (for speed)
* Filter the data
* Automatic rejection of bad channels
* Re-Reference again
* Repair bursts and reject bad portions of data
* run ICA to detect brain and artifactual components
* automatically classify Independent Components using IC Label
* Save dataset


### Session 2: Single sensor analysis (ERP/ERF)

For this presentation, we will use different vizualization techniques using the [Session_2_ERP_Analysis.m](Session_2_ERP_Analysis.m) script. The script first further process the data as follow.

* Extract data epochs for the famous, scrambled, and unfamiliar face stimuli
* Remove the baseline from -1000 ms to 0 pre-stimulus
* Apply a threshold methods to remove spurious epochs
* Resave the data

Then it plots the data using the following methods:

* Plot ERP butterfly plot and scalp distribution at different latencies
* Remove ICA artifactual components and replot
* Plot series of scalp topography at different latencies
* Plot conditions overlaid on each other
* Plot ERPimages

### Session 2: Time-frequency decomposition

For this presentation, we will the script [Session_2_Time_Frequency_Analysis.m](Session_2_Time_Frequency_Analysis.m). It performs the following steps.

* Spectral analysis for each of the conditions
* Time-frequency analysis for each of the conditions

### Session 3: Single and distributed sources

For this presentation, we will the script [Session_3_Source_Reconstruction.m](Session_3_Source_Reconstruction.m). It performs the following steps.

* Definition of head model and source model
* Localization of ICA components
* Plotting of ICA components overlaid on 3-D template MRI

### Session 4: ERP source analysis

The script [Session_4_ERP_Source_Analysis_TOEDIT.m](Session_4_ERP_Source_Analysis_TOEDIT.m) analyzes ERP component contributions and source-level analysis.

* Load preprocessed data from Session 1
* Extract epochs for Famous, Unfamiliar, and Scrambled face conditions
* Perform baseline correction (-1000 to 0 ms)
* Apply threshold-based epoch rejection
* Plot ERP scalp distributions for each condition
* Analyze ICA component contributions to ERPs using scalp envelope plots
* Demonstrate removal of artifact components
* Visualize component projections to ERPs

### Session 5: BIDS import and preprocessing workflows

This session demonstrates how to work with BIDS-formatted datasets using two scripts:

**Single-subject BIDS import** - [Session_5_6_bids_ds000117.m](Session_5_6_bids_ds000117.m):
* Import data using EEGLAB BIDS tools from ds000117_pruned
* Add fiducial coordinates and rotate montage
* Re-import events from STI101 channel
* Select EEG or MEG data type
* Clean artifactual events
* Merge multiple runs for each subject

**Group-level BIDS import** - [Session_5_6_bids_ds002718.m](Session_5_6_bids_ds002718.m):
* Import multiple subjects from ds002718 BIDS dataset
* Remove unwanted channels
* Apply common average reference
* Resample data to 100 Hz
* Apply high-pass (1 Hz) and low-pass (40 Hz) filters
* Prepare data for group-level analysis

### Session 6: Group-level analysis

The script [Session_6_Group_Analysis_STUDY.m](Session_6_Group_Analysis_STUDY.m) perform group analysis on a group of subjects.

* Removing components flagged for rejection using ICLabel
* Plotting grand average ERPs

## Advises on conducting the course

Give the lecture for the course and run the hands on exercises that accompany the PowerPoint slides. The scripts can support the demonstrations, although relying on them too heavily can overwhelm beginners. Most participants will follow the GUI more easily, so position the scripts as a reference rather than the primary workflow.

To continue to Session 2, participants must either run the script [Session_1_Import_Data.m](Session_1_Import_Data.m)  or manually reproduce all import steps in the GUI, which is impractical for this dataset. The raw files require several technical adjustments that are not beginner friendly. For Session 1, a practical compromise is to have users import the FIF file in the GUI, select the EEG channels, explore the raw data briefly, then execute the import script to complete the required preprocessing. The second script, [Session_1_Preprocess_Data.m](Session_1_Preprocess_Data.m), can be reproduced entirely with the GUI if students prefer to work interactively.

From Session 3 onward, the scripts function mainly as optional examples. All core operations can be performed in the GUI. Instructors can choose whether to demonstrate scripts to illustrate reproducible workflows, but this should not be required for participants to progress.

A few additional suggestions can improve the course experience. Clarify early that ICA may yield slightly different outcomes across computers and that this variability is normal. Finally, alternate between explanation and hands on exploration so participants stay engaged and do not fall behind. Have a teaching assistant present throughout the session so participants who get stuck can receive prompt one to one support without interrupting the flow of the course.
