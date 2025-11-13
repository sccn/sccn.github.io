---
layout: default
title: Create your own course
long_title: Create your own course
parent: Workshops
nav_order: 1
---
# Create Your Own EEG Course

This [repository](https://github.com/sccn/EEGLAB_course) contains materials for EEGLAB course sessions. This course was originally conducted at the [practical MEEG 2025 workshop](https://cuttingeeg.org/practicalmeeg2025/). Although this course is centered on EEGLAB, 90% of the material is not EEGLAB-specific.

You may adapt the materials as needed for your own course, although please acknowledge the authors of the materials.

## Prerequisites

### Step 1 – Download and install MATLAB

If you are organizing a course, you can usually obtain a [MATLAB trial version](https://www.mathworks.com/support/contact_us.html) for your participants by contacting the licensing department. Please have your participants install MATLAB in advance so you're ready to run EEGLAB during the course.

### Step 2 – Download the course scripts

During the course, participants will follow along and do hands-on work using the EEGLAB graphical interface. However, they can also run the scripts provided in this repository.

Clone this repository:

```bash
git clone https://github.com/sccn/EEGLAB_course.git
```

Or download the ZIP on GitHub. Then run all the scripts one of by one starting with the first script.

### Step 3 – Download the data

This course uses data from the multimodal face recognition BIDS dataset, a pruned version of the OpenNeuro dataset ds000117.

**Download the pruned single-subject dataset (ds000117_pruned):**
[https://zenodo.org/record/7410278](https://zenodo.org/record/7410278)

This dataset contains only one subject and is used in Sessions 1, 2, 3, and 5.

**For group-level analyses, also download the BIDS dataset (ds002718):**
[https://nemar.org/dataexplorer/detail?dataset_id=ds002718](https://nemar.org/dataexplorer/detail?dataset_id=ds002718)
(download the ZIP file on that page)

### Folder Structure Setup

The scripts expect the following folder structure:

```
EEGLAB_course/
├── eeglab/                    (eeglab distribution with plugins installed)
├── ds002718/                  (raw BIDS data)
│   └── derivatives/           (processed data will be saved here)
├── ds000117_pruned/           (raw data for Sessions 1 of subject 1, not a valid BIDS dataset)
│   └── derivatives/
│       └── meg_derivatives/
│           └── sub-01/
│               └── ses-meg/
│                   └── meg/   (processed .set files saved here)
├── script_01_import_data.m
├── script_02_preprocess_data.m
├── script_03_epochs_and_erp.m
├── script_04_time_frequency.m
├── script_05_source_reconstruction.m
├── script_06_connectivity.m
└── ... (other scripts)
```

**Setup instructions:**
1. Clone or download this repository to create the `EEGLAB_course` folder
2. Download and extract the `ds000117_pruned` folder **inside** the `EEGLAB_course` folder
3. Download and extract the `ds002718` folder **inside** the `EEGLAB_course` folder

### Step 4 – Download EEGLAB

Now it's time to clone the EEGLAB Git repository on your computer.

**Warning:** Do not download the ZIP file directly from GitHub, as it does not include EEGLAB submodules.

Instead, use the following command to clone the repository and pull its submodules:

```bash
git clone --recurse-submodules https://github.com/sccn/eeglab.git
```

Or download from the [EEGLAB website](https://sccn.ucsd.edu/eeglab/download.php).

### Step 5 – Check that EEGLAB runs

1. Start MATLAB
2. In MATLAB, navigate to the folder containing the EEGLAB repository
3. At the MATLAB command prompt (>>), type: `eeglab`
4. The EEGLAB main interface should appear

If it opens without errors, you're all set for the workshop!

### Step 6 – Download EEGLAB plugins

This is step is critical or a lot of the excercises will not run. This is the list of plugins to downlaod:
* File-IO
* Fieldtrip-lite
* LIMO

It is best to use the EEGLAB plugin manager (EEGLAB menu item **File > Manage extension** and to select the plugins to install).

## Course Content Overview

The course materials are organized into several sessions, each focusing on different aspects of EEG/MEG data analysis using EEGLAB. Some sesisons are longer than others.

### Session_1.1_overview.pptx

The 18-slides presentation introduces EEGLAB, its history, capabilities, ecosystem, and practical setup steps. It also highlights preprocessing pipeline comparisons and key reference articles.

* EEGLAB origins and development timeline
* Usage statistics and ecosystem scale
* Plugin manager and plugin count
* MATLAB version and toolbox requirements
* Advantages and limitations of MATLAB based EEGLAB
* Operating system and compilation options
* Automated preprocessing pipeline comparison
* EEGLAB minor performance advantage explanation
* Links to tutorial videos and test data
* Key EEGLAB reference publications
* Installation instructions and datasets
* Git setup and cloning repositories

### Session_1.2_BIDS_and_NEMAR_data_repository.pptx

The 31 slides present the principles of open and FAIR data, the structure and purpose of BIDS, and the components of BIDS-EEG. They also introduce NEMAR resources, available tools, and computational infrastructure. This presentation is optional; however, since the data is in BIDS format, it is beneficial to introduce the format.

* Drivers of increased data sharing
* FAIR data principles and requirements
* BIDS purpose and scope
* Components of a BIDS-EEG dataset
* Examples of dataset organization
* Supported raw EEG formats
* Event and task description structure
* Tools for BIDS import and export
* NEMAR repository overview
* Manuscripts describing NEMAR tools
* Available GPU and CPU compute resources
* EEGDash platform introduction 

### Session_1.3_preprocessing.pptx

The 67 slides explain the full EEG preprocessing pipeline from raw data to analysis, including filtering, referencing, artifact handling, ICA, and evaluation of preprocessing choices. They also present evidence on how preprocessing steps influence statistical outcomes and describe practical EEGLAB workflows.

* Reasons for preprocessing EEG data
* Overview of the full preprocessing pipeline
* BIDS support in major MEEG toolboxes
* Event import and raw data inspection
* Hands on data loading and visualization
* HED tagging and NEMAR BIDS experiments
* Channel location scanning and alignment
* Influence of reference choice on ERPs
* Effects of downsampling decisions
* High pass filtering and ERP significance
* Artifact types and identification methods
* Bad channel detection via correlation
* Line noise handling and interpolation
* ASR performance and human rater comparison
* Automated rejection methods and limitations
* ICA decomposition and quality criteria
* ICLabel classification and component removal
* Clean_rawdata preprocessing workflow
* Baseline effects on ERP significance
* Comparison of automated preprocessing pipelines

### Session_2.1_ERP.pptx

The 48 slides introduce ERP analysis at the sensor level, covering conceptual foundations, visualization methods, preprocessing influences, and EEGLAB based workflows. They illustrate how ERPs arise, how to inspect them, and how ICA components contribute to ERP features.

* Historical context and ERP foundations
* ERP experiment structure and data flow
* Examples of ERP morphology
* ERP images and trial sorting
* Phase synchronization as ERP mechanism
* Time, frequency, and time frequency approaches
* Epoch extraction and baseline handling
* Artifact rejection and ICA influence on ERPs
* Scalp distribution and topographic visualization
* Three dimensional channel registration and warping
* Component level ERP envelopes and contributions
* Difference ERPs across conditions
* Hands on ERP analysis steps

### Session_2.2_TimeFrequencyAnalysis.pptx

The 55 slides present the theory and practice of time frequency analysis for biophysical signals, from Fourier methods to wavelets. They explain key trade offs, practical spectral estimation techniques, and EEGLAB based ERSP and ITC analysis.

* Biophysics of EEG and brain oscillations
* Stationary versus non stationary signals
* Fourier theorem and frequency decomposition
* Discrete Fourier Transform and FFT basics
* Zero padding and spectral interpolation limits
* Tapering, windowing, and Gibbs phenomenon
* Window trade offs and Welch spectral estimation
* Trial averaging and variance reduction in spectra
* Spectrograms and ERSP for non stationary activity
* Absolute versus relative power and normalization
* Time frequency uncertainty and Heisenberg limit
* Wavelet construction and Morlet convolution
* Time frequency trade off in wavelet families
* Comparing FFT based and wavelet approaches
* Phase resetting, induced versus evoked responses
* Inter trial coherence and phase visualization
* IC level ERSP and ITC plots in EEGLAB
* Hands on steps for channel time frequency analysis

### Session_3.1_Source_Localization_ICA.pptx

The 53 slides explain how ICA contributes to source estimation, covering the forward and inverse problems, ICA theory, and practical DIPFIT based localization. They describe how IC scalp projections relate to dipolar sources and how to fit anatomical models in EEGLAB.

* Forward and inverse modeling principles
* Ill posed nature of EEG source reconstruction
* Dipole and distributed inverse methods
* Role of ICA in separating cortical sources
* ICA versus PCA and key ICA algorithms
* Applications of ICA to biomedical data
* Two step workflow for IC source localization
* Dipole fitting and residual variance evaluation
* Co registration of electrodes and head models
* BEM models and transformation parameters
* Autofit options and dual dipole fitting
* Distributed localization with eLORETA and beamforming
* Leadfield computation and component modeling
* Hands on DIPFIT localization procedures

### Session_3.2_connectivity.pptx

The 54 slides introduce dynamic brain connectivity analysis in EEG, covering VAR modeling, Granger causality, non stationarity handling, ROI based source space connectivity, and SIFT workflows. They explain key pitfalls, model selection principles, and visualization of causal interactions, with an accompanying brain movie illustrating connectivity dynamics.

* Goals and challenges of EEG connectivity analysis
* Spurious connectivity and common input problems
* Granger causality principles and VAR modeling
* Model order selection and information criteria
* Handling non stationarity with sliding windows
* Connectivity during visually guided movement
* ICA based source space analysis and ROI extraction
* SIFT workflow and causal network reconstruction
* Influence of atlas choice and number of nodes
* Coherence and phase relationships between regions
* Channel versus source space considerations
* Hands on steps for ROI connectivity computation

(see also the associated brain movie: Session_3.2_connectivity_brain_movie.mov)

### Session4_IC_Clustering.pptx

The 51 slides describe how to cluster ICA components across subjects in EEGLAB, from STUDY setup and measure precomputation to K-means clustering and interpretation. They also show how clustering validates ICA solutions and helps identify functionally meaningful source groups.

* Steps of IC clustering workflow
* STUDY loading and dataset information editing
* Residual variance computation and IC selection
* Precomputation of spectra, ERSP, dipoles, and moments
* PCA based preclustering and singular value selection
* K means clustering in feature space of IC measures
* Choice of measures based on scientific question
* Examples of within subject and across subject clusters
* Validation of ICA dipolarity and algorithm reliability
* Visualization and manual editing of IC clusters
* Identification of frontal midline theta and occipital alpha clusters
* Hands on protocol for clustering and outlier removal

### Session_5.1_univariate_statistics.pptx

The 72 slides present robust statistical methods for EEG, covering parametric and nonparametric inference, bootstrap and permutation strategies, multiple comparison corrections, and GLM based analysis at single subject and group levels. They emphasize robust estimation, visualization, and principled control of false positives.

* Parametric and nonparametric hypothesis testing
* Power, effect size, and sample size considerations
* Robust central tendency and trimmed means
* Bootstrap confidence intervals and inference
* Bootstrap versus permutation logic
* Corrections for multiple comparisons
* Bonferroni, Holm, FDR, cluster, and TFCE methods
* Cluster based permutation for EEG time series
* Strengths and limitations of correction strategies
* Introduction to GLMs for EEG data
* Design matrices and modeling factors
* Level one and level two GLM analysis
* Mixed effects modeling and random effects
* Software implementations in MATLAB, Python, and R

### Session_5.2_univariate_statistics_practicum.pptx

The 23 slides give a hands on walkthrough of GLM based univariate statistics in EEGLAB/LIMO, using the ds002718 face dataset. They focus on STUDY design setup, single trial modeling, and running first and second level analyses with appropriate corrections.

* Overview of the ds002718 face repetition dataset
* Level one GLM and beta significance estimation
* Experimental factors and condition structure
* BIDS import, cleaning, ICA, and epoching steps
* STUDY creation and design specification
* Precomputation of single trial measures
* Standard EEGLAB statistics and corrections
* Exercises on ERP comparison across conditions
* LIMO plugin based model estimation
* Group level ANOVA and contrast interpretation
* Practical workflow for GLM based EEG statistics

(see also the associated movies referenced in the presentation: Session_5.2_movie_1.mp4 and Session_5.2_movie_2.mp4; distributed separately because of GitHub 100mb limit)

## Exercices

* **Session_1.1_overview.pptx** – No Exercice
* **Session_1.2_BIDS_and_NEMAR.pptx** – No Exercice
* **Session_1.3_preprocessing.pptx** – Load raw data, apply cleaning, run ICA with ICLabel, and compare preprocessing choices.
* **Session_2.1_ERP.pptx** – Create epochs, compute ERPs, visualize scalp maps and ERPimages, and examine ICA contributions.
* **Session_2.2_TimeFrequencyAnalysis.pptx** – Compute ERSP and ITC, compare baseline strategies, and study induced versus evoked activity.
* **Session_3.1_Source_Localization_ICA.pptx** – Fit ICA dipoles, assess residual variance, and perform distributed source localization.
* **Session_3.2_connectivity.pptx** – Compute ROI activity, estimate VAR based connectivity, and interpret connectivity dynamics.
* **Session_4_IC_Clustering.pptx** – Precompute IC measures, run PCA based preclustering, apply K means, and interpret IC clusters.
* **Session_5.1_univariate_statistics.pptx** – No Exercice
* **Session_5.2_univariate_statistics_practicum.pptx** – Perform full GLM analysis on a multi subject dataset, including model specification and correction.

## Scripts

The scripts accompany the presentations, although they are not required for students to complete the course. The material is aimed primarily at beginners who may not yet know how to script, so the presentations do not explicitly describe these files. The scripts nevertheless mirror the workflow shown in each session and can be used to reproduce the results demonstrated during the lectures. Students who wish to explore further can consult the help messages of the functions used in each script.

* **script_01_import_data.m** - Imports raw EEG or MEG data and events into EEGLAB. Refers to Session_1.3_preprocessing.
* **script_02_preprocess_data.m** - Runs filtering, bad channel detection, ASR, ICA and IC cleaning. Refers to Session_1.3_preprocessing.
* **script_03_epochs_and_erp.m** - Creates epochs, computes ERPs and prepares data for ERP analysis. Refers to Session_2.1_ERP.
* **script_04_time_frequency.m** - Computes ERSP, ITC and other time frequency measures. Refers to Session_2.2_TimeFrequencyAnalysis.
* **script_05_source_reconstruction.m** - Runs DIPFIT, computes dipoles and distributed source models. Refers to Session_3.1_Source_Localization_ICA.
* **script_06_connectivity.m** - Computes VAR models, Granger causality and ROI connectivity. Refers to Session_3.2_connectivity.
* **script_07_group_analysis_preprocess.m** - Prepares multi subject datasets and STUDY structures for group analysis. Refers to Session4_IC_Clustering and Session_5.x statistics.
* **script_08_group_analysis.m** - Runs group level STUDY measures including clustering and group ERPs. Refers to Session4_IC_Clustering.
* **script_09_ica_clustering.m** - Performs IC clustering across subjects using STUDY. Refers to Session4_IC_Clustering.
* **script_10_limo_erp.m** - Runs GLM based univariate statistics using LIMO EEG. Refers to Session_5.1 and Session_5.2 univariate statistics.

## Advises on conducting the course

Present the lectures for the course and run the hands on exercises that accompany the PowerPoint slides. The scripts can support the demonstrations, although relying on them too heavily can overwhelm beginners. Most participants will follow the GUI more easily, so position the scripts as a reference rather than the primary workflow.

As an intructer, we advise that you download and install the material. Then run all the scripts so the data is precomputed for participants (otherwise for session 3, participants must either run the script [script_01_import_data.m](script_01_import_data.m) and [script_02_preprocess_data.m](script_02_preprocess_data.m) or manually reproduce all import steps in the GUI, which is impractical for this dataset). The raw files require several technical adjustments made by the scripts that are not beginner friendly so it is better to have everything precomputed. Script [script_03_epochs_and_erp.m](script_03_epochs_and_erp.m) extract epoch and also need to be executed. Script 4 to 6 function mainly as optional examples. Script 7 needs to be run for the group and limo analysis. All core operations can be performed in the GUI. Instructors can choose whether to demonstrate scripts to illustrate reproducible workflows, but this should not be required for participants to progress. If you precompute all the measures for students, the scripts are simply add on that may or may not be used. We recommend that option.

Once you have confirmed that everything runs correctly, **zip the full course folder and copy it to a USB flash drive** for distribution. This allows students to begin immediately without dealing with data downloads, EEGLAB installation, or plugin setup. We also advise that you include EEGLAB and its plugin (either as a zip archive or uncompressed) on the flash drive so all students have the latest version of EEGLAB.

A few additional tips to improve the course experience: Clarify early that ICA may yield slightly different outcomes across computers and that this variability is normal. Finally, alternate between explanation and hands on exploration so participants stay engaged and do not fall behind. Have a teaching assistant present throughout the session so participants who get stuck can receive prompt one to one support without interrupting the flow of the course.

## Contributors

* Arnaud Delorme, creator of this course
* Other contributors include Scott Makeig, Romain Grandchamp, Johanna Wagner, Ramon Martinez-Cancino, Tim Mullen, John Iversen, and Cyril Pernet.
