---
layout: default
title: EEGLAB revision history
parent: Download EEGLAB
---
EEGLAB revision history
===
EEGLAB downloads in ZIP format are available [here](https://sccn.ucsd.edu/eeglab/download.php). 
These include the latest release as well as older versions of EEGLAB.

As of 2019, we are using the year of the release as the main revision number. 
Minor revisions are indicated using a second number; thus,
2019.0 is version 2019, first release; 2019.1 is version 2019, second release, etc...
There will usually be one or two releases per year. 
Previous major EEGLAB versions (e.g., versions 13, 14, etc.) did not use this naming scheme and did observe a regular release schedule.

## EEGLAB version 2025.1.0

- Issue date: 9/17/2025 (TBD); GIT tag: 2025.1.0
- **Version statistics**: 39 files changed with 862 additions and 551 deletions.
- **Summary of changes:** EEGLAB 2025.1.0 introduces broad compatibility updates for MATLAB 2025, including fixes in eegplot rendering, font scaling, pophelp modernization, and automatic renderer adjustments to prevent darkened figures on Windows. It also corrects the representation of two-way ANOVA designs in STUDY functions, fixing factor ordering, labeling, and p-value mapping for more accurate visualization of 2×2 designs.
- **MATLAB compatibility:** MATLAB 2025 visual adjustments in many functions, including eegplot, to decrease font size and ensure visibility.  
- **STUDY and statistics:** std_limo adds a verbose noGUI mode for pipeline use and writes chanlocs under derivatives when appropriate. Contrast construction updated to handle one categorical factor with multiple conditions alongside continuous factors. FieldTrip stats on averaged channels fixed. Same color scale enforcement corrected. Corrects the representation of two-way ANOVA designs in STUDY functions, fixing factor ordering, labeling, and p-value mapping for more accurate visualization of 2×2 designs (labels were misleading).
- **Referencing and ICA:** New Huber average reference added to reref.m and exposed in pop_reref UI. Automatic recomputation of ICA activities now occurs on rereference unless backwardcomp is selected. AMICA path switched to runamica15 with guidance to install and use the AMICA plugin GUI.  
- **Interpolation and channel handling:** eeg_interp accepts bad channel lists as cell arrays and supports sphericalCRD. eeg_checkchanlocs removes stale urchan when urchanlocs is empty and avoids creating a new urchan field spuriously. pop_chanedit avoids showing urchan when urchanlocs are unset. pop_rmbase now operates strictly on the selected channel list.  
- **Event and epoching fixes:** biosig2eeglabevent and pop_biosig improve EDF+ decoding logic, including handling CodeDesc for extended event codes and importing EDF annotations into EEG.event when requested.  
- **Import/export and I/O:** pop_writeeeg now tolerates empty filename while letting users pick format and warns about known BDF header issues.  
- **GUI and UX:** pophelp substantially reworked for MATLAB 2025.  
- **EEGLAB integrity checks:** eeg_checkset large refactor and cleanups across warnings and edge cases.  
- **BIDS and pipeline:** EEG-BIDS submodule updated; lookups now search directly for derivatives folder. pop_exportbids and related scripts refreshed; bids_reexport streamlined. Fix issues with using samples when importing event latencies.  
- **Dipfit:** Update compatibility atlas mapping and LORETA source localization.  
- **Known behavior changes:** Re-referencing now recomputes ICA activities by default in 2025.1.0; use backwardcomp to preserve previous versions’ behavior.  
- Use this [Github link](https://github.com/sccn/eeglab/compare/2025.0.0..2025.1.0) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2025.0.0

- Issue date: 2/17/2025; GIT tag: 2025.0.0
- **Version statistics**: 45 files changed with 697 additions and 234 deletions.
- **Minor Code Adjustments:** Several functions have undergone minor tweaks. These include functions related to checking channel locations (eeg_checkchanlocs), dataset integrity (eeg_checkset), retrieving datasets (eeg_retrieve), updating EEGLAB (eeglab_update), adjusting event latencies (pop_adjustevents), editing channel information (pop_chanedit), selecting channels (pop_chansel), file I/O (pop_fileio), re-referencing data (pop_reref), running ICA (pop_runica), plotting data (eegplot), and statistical tests (ttest2_cell). These changes address specific edge cases, improve error handling, and enhance functionality.
- **UI bug**: input GUI (input UI) was fixed, and all functions that depend on it will now behave properly. This may include coregister.m, pop_editeventvals.m.
- **Plugin Updates:** Several plugins have been updated, including EEG-BIDS, ICLabel, clean_rawdata, and dipfit. EEG-BIDS is now one of the default plugins included in EEGLAB.
- Use this [Github link](https://github.com/sccn/eeglab/compare/2024.2.1..2025.0.0) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2024.2.1

- Issue date: 11/12/2024; GIT tag: 2024.2.1
- **Version statistics**: 3 files changed with 8 additions and 4 deletions.
- **Bug fix**: Fix crashes when EEGLAB is offline, WIFI is on and Biosig is installed.
- **Bug fix**: Minor fix crash to channel location field.
- Use this [Github link](https://github.com/sccn/eeglab/compare/2024.2..2024.2.1) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2024.2.0

- Issue date: 08/28/2024; GIT tag: 2024.2
- **Version statistics**: 7 files changed, 21 additions and 12 deletions.
- **Bug fix**: Fix the issue with the Edit Event Value menu item (which was not functional).
- Use this [Github link](https://github.com/sccn/eeglab/compare/2024.1..2024.2) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2024.1 

- Issue date: 08/06/2024; GIT tag: 2024.1
- **Version statistics**: 70 files changed, 1,480 additions, and 228 deletions.
- **New feature**: EEGLAB colormap changed. See this [post](https://sccn.ucsd.edu/pipermail/eeglablist/2024/017887.html) for more details.
- **New feature**: EEGLAB compiled version can now execute scripts given on the command line.
- **New feature**: Allowing plugins to have critical updates.
- **New feature**: New option to cluster components (thanks Yahya Shirazi).
- **New feature**: Allowing to better process ICA clusters when a subject is split into multiple EEG datasets (so study designs with multiple sessions can be considered)
- **bids-matlab-tools plugin:** Renamed EEG-BIDS. New options to export eye-tracking data.
- **Bug fix**: Fix the issue with not clearing the STUDY cache when editing a STUDY.
- **Bug fix**: Better detection of a dataset modified by users.
- **Bug fix**: Fix issue with STUDY [ICA component clustering](https://github.com/sccn/eeglab/issues/767). This is also related to the ICLabel bug below.
- <font color=red><b>ICLabel plugin:</b> The ICLabel version (1.5) released in the previous EEGLAB version had the same problem as described above. Make sure to use this EEGLAB distribution or update to ICLabel 1.6 if you are using EEGLAB 2024.0</font>
- Use this [Github link](https://github.com/sccn/eeglab/compare/2024.0..2024.1) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2024.0

- Issue date: 02/23/2024; GIT tag: 2024.0
- **Version statistics**: 199 files changed, 113 commits, 2,422 additions and 1,448 deletions.
- **New feature**: New custom measures for STUDY as illustrated [here](https://github.com/sccn/eegstats) and exporting results in table format.
- **New feature**: Code reformated to be more legible.
- **New feature**: New channel spherical interpolation method in eeg_interp.
- **New feature**: Now import Neuralinx data and associated events.
- **New feature**: Infomax Runica always returns the same result (backward compatible).
- **New feature**: Now selecting events for a group of datasets in STUDY.
- **Interoperability**: Improved Octave 8.4 compabitlity.
- **Bug fix**: Fix looking up channel locations in STUDY.
- **Bug fix**: Fix importing BIDS coordsystem file for MEG data when using File-IO.
- **DIPFIT plugin**: STUDY level leadfield matrix computation.
- **bids-matlab-tools plugin:** Version 8 has been released. Now handles behavioral data and many small improvements.
- **ROIconnect plugin:** Improved compatibility. This plugin has been released, although the documentation is not complete.
- <font color=red><b>ICLabel plugin:</b> The ICLabel version (1.5) released with this version has a bug. Make sure to upgrade to version 1.6 of the plugin</font>
- Use this [Github link](https://github.com/sccn/eeglab/compare/2023.1..2024.0) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2023.1

- Issue date: August 23rd 2023; GIT tag: 2023.1
- **Version statistics**: 50 files changed, 99 commits, 957 additions, and 395 deletions.
- **New feature**: EEGLAB redraw detects dataset changes. There is no more need to store the current dataset in the ALLEEG structure if you modify it on the command line.
- **New feature**: New option "scatter" for control electrode size and color in topoplot.
- **New feature**: Computing custom features for STUDY and retrieving field content using std_readeegfield.
- **Interoperability**: Now support ERPLAB new menu status and new variables, and better support for -99 boundary event.
- **Interoperability**: Now support the version of LIMO with updated GUI (LIMO version 4 not yet released).
- **Bug fix**: Update a variety of functions to process MEG datasets, including source localization function (see [tutorial](https://eeglab.org/tutorials/misc/EEGLAB_and_MEG_data.html)). 
- **Bug fix**: Parallel option fixed when processing multiple datasets from the EEGLAB menu.
- **Bug fix**: Fixed issue with detecting removed channels when re-referencing the data.
- **Bug fix**: Fixed issue with saving large EEG files when the option is not selected (>2Gb).
- **SIFT plugin**: Fixed some minor GUI issues and rewrote the tutorial, including new sections to compute [statistics](https://github.com/sccn/SIFT/wiki/Chapter-7.-Statistics-in-SIFT).
- **DIPFIT plugin**: Fix handling non-EEG channels when computing Loreta and Leadfield matrix.
- **bids-matlab-io plugin:** Better import of MEG data, and many more small bug fixes and improvements.
- **ROIconnect plugin:** Improved compatibility. This plugin is still in beta and will be released soon.
- Use this [Github link](https://github.com/sccn/eeglab/compare/2023.0..2023.1) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2023.0

- Issue date: March 3rd 2023; GIT tag: 2023.0
- **Version statistics**: 654 files changed, 230 commits, 11,585 additions and 3,248 deletions.
- **Major changes**: Update a variety of functions to process MEG datasets, including source localization (see [tutorial](https://eeglab.org/tutorials/misc/EEGLAB_and_MEG_data.html)). 
- **New feature**: Limit the number of displayed datasets to speed up display when processing more than 200 datasets.
- **New feature**: Change all function headers for better MATLAB interoperability (capitalize all function names, etc...).
- **Interoperability**: New function brainstorm2eeglab.m to import Brainstorm data epochs.
- **Interoperability**: Improved function fieldtrip2eeglab.m to convert Fieldtrip data structures. Update to pop_fileio to import MEG metadata.
- **Interoperability**: More command-line options to import files using BIOSIG.
- **Bug fix**: Better handling of boundary events (especially the ones at the beginning and end of the data).
- **Bug fix**: Better detection when a dataset is modified by the user in the global workspace.
- **Bug fix**: Better EEGLAB help menus and GUI formatting.
- **SIFT plugin**: Fix the issue with Picard ICA (SIFT was overloading the Picard function).
- **Clean_rawdata plugin**: New option to fuse channels rejected by clean_rawdata on multiple runs of the same subject.
- **DIPFIT plugin**: MEG source localization and custom MRI source localization (see [tutorial](https://eeglab.org/tutorials/09_source/Custom_head_model.html))
- **bids-matlab-io plugin:** support for behavioral information and motion capture. Better support to import iEEG and MEG data.
- Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2022.1..2023.0) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2022.1

- Issue date: Aug 2nd 2022; GIT tag: 2022.1
- **Version statistics**: 104 files changed, 4,411 insertions, 421 deletions.
- **Major interoperability change**: Allow using event type -99 for discontinuities and improve ERPLAB compatibility (20 functions modified). The default is still to use 'boundary' for event boundary, but the default can be changed in the EEGLAB preferences when processing numerical event types.
- **Interoperability**: Added 4 new parameters to import data with BIOSIG toolbox, in particular for EDF and BDF files.
- **Interoperability**: Increased compatibility for Fieldtrip dataset conversion back and forth, in particular for electrode coordinates.
- **Interoperability**: Fix processing data from multiple sessions for LIMO.
- **Group analysis**: Allow fusing channel rejection across datasets of the same subject and session.
- **Bug fix**: Fix concatenating datasets of the same size.
- **Bug fix**: Fix editing channel locations in groups of datasets (STUDY) - datasets were not resaved.
- **Bug fix**: Fix separating multiple sessions when precomputing data for STUDY - sessions were fused.
- **Minor bug fix**: Fix remembering the data was average referenced.
- **Plugins**: Minor updates to ICLabel, dipfit, and firfilt default plugins. Major update to clean_rawdata to fuse data channel rejections within subjects for group processing.
- **Testing**: New testing framework using Github [actions](https://github.com/sccn/eeglab_tests/actions). New binary test files are now included in the sample_data folder for quick testing of compiled EEGLAB versions.
- Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2022.0..eeglab2022.1) to see all changes from the previous EEGLAB version.

## EEGLAB version 2022.0

- Issue date: Feb 11th 2022; GIT tag: 2022.0
- **Version statistics**: 73 commits and 269 files changed, 988 insertions, 781 deletions.
- **Bug fix**: Fix study issue when parallel toolbox is absent (GCP error)
- **Bug fix**: Fix rare bug when writing two files for an EEGLAB dataset (old default; the new default since 2021 is to write a single .set file)
- **Bug fix**: Fix plotting ERPimage for ICA component clusters
- **Interoperability**: Improved Fieldtrip bidirectional conversion for data trials
- **Interoperability**: Improved LIMO compatibility issues when processing a study with multiple sessions
- **Speed increase**: Speed up IDing user profile and speed up eeg_checkset by 2 orders of magnitude
- **EDF files**: Exporting EDF files now use a common limit for all channels; fix importing channel labels with EEG prefix in EDF files
- **MEG**: Allow importing MEG gradiometers from FIF files
- **Artifact rejection using ASR**: Clean_rawdata plug-in now allows processing a subset of channels
- **Multiple dataset processing**: Now channel editor can process multiple datasets in a STUDY
- Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2021.1..eeglab2022.0) to see all changes from the previous EEGLAB version.

## EEGLAB version 2021.1

- Issue date: July 27th 2021; GIT tag: 2021.1
- **Version statistics**: 151 commits and 70 files changed, 3,592 additions and 1,029 deletions.
- **STUDY**: Allowing parallel execution of most STUDY functions. Allowing menu batch processing of studies of continuous data including BIDS-imported studies. Fix handling of multiple datasets within the same session. Fix error when computing statistics for averaged channels.
- **EEG file format**: Fix  reading newer .set files that have been moved or loading them from the command line. Allow saving in Matlab version 7.0 format.
- **EEG scrolling**: EEGPLOT function major speedup
- **Octave**: Improved GUI support
- **LIMO**: Improved LIMO compatibility and allowed the possibility to use multiple sessions per subject
- **Removed channels**: Fix interpolation when considering removed channels. Fix removed channeled list.
- **BIDS**: Fix issue when dealing with xml files containing unicode characters
- **DIPFIT**: Now computes Leadfield Matrices
- Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2021.0..eeglab2021.1) to see all changes from the previous EEGLAB version.

## EEGLAB version 2021.0

- Issue date: February 1st 2021; GIT tag: 2021.0
- **Statistics**: 159 commits, 80 files and 3,247 lines of code modified.
- **Multiple dataset processing**: Now allowing processing of multiple datasets with most menu items, including ICLabel and clean_rawdata plug-ins
- **File format**: Now saving all EEGLAB datasets in a single file instead of two (fully backward compatible)
- **Version checking**: Now EEGLAB version checking uses the same system as  for plug-ins
- **Example scripts**: New tutorial scripts are made available within EEGLAB
- **Custom group analysis**: Now allows custom processing of EEGLAB Studies.
- **Channel selection**: Now allows selecting channel subsets by label in all GUIs.
- **Channel location**: Now using the BEM-model channel scalp locations as the default for looking up channel locations by labels (instead of using the BESA spherical head model)
- **Plug-in support**: Now allowing plug-ins to be placed in the *plugins* subfolder of the current Matlab path
- **Interoperability**: Improved support for Matlab 2020 versions and for Octave, Fieldtrip, and LIMO
- **Menu structure**: Now hiding a rarely used menu item to compare datasets by default
- Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2020.0..eeglab2020.1) to see all changes compared to the previous EEGLAB version.

## EEGLAB version 2020.0

-   Issue date: July 31st, 2020; GIT tag: 2020.0
-   <b>EEGLAB Plug-in manager</b>: Fixed bugs, made plug-in detection
    case sensitive, added plug-in search capability.
-   <b>EEGLAB auto updater</b>: Allow installation of a new version of
    EEGLAB from within EEGLAB itself.
-   <b>Support for BIDS</b>: Now testing the EEGLAB BIDS-EEG plug-in
    (the beta version is available at
    <https://github.com/sccn/bids-matlab-tools>).
-   <b>HED</b> Hierarchical Event Descriptors (HED): Improved tools for
    annotating dataset events at the STUDY level in the HED-2 system,
    and for extracting HED-tagged epochs.
-   <b>IClabel</b>: Improved support and compatibility for the IClabel
    plug-in.
-   <b>LIMO</b>: Improved support and compatibility for the LIMO
    plug-in.
-   <b>EDF/EDF+</b>: Better conversion of EDF and EDF+ file events.
-   <b>Scrolling data viewer</b>: Fixed issue that dramatically slowed
    down scrolling EEG viewing when the dataset includes a large number
    of events.
-   <b>Channel rejection</b>: EEGLAB now remembers which channels were
    removed from a dataset.
-   <b>Test file output</b>: Fixed a resolution issue.
-   <b>LIMO STUDY statistics</b>: The STUDY interface now lists the
    first- and second-level variables in the STUDY design
-   <b>STUDY spectrum plots</b>: Fixed the ordinate (power) scale.
-   Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2019.1..eeglab2020.0) to see all changes compared to the previous EEGLAB version.

## EEGLAB Version 2019.1

-   Issue date: November 18th, 2019; GIT branch: 2019.1
-   <b>EEGLAB menus</b>. We have reorganized and simplified EEGLAB
    menus, in particular the tool menus. There is still an option to
    show all menus as in previous version by changing EEGLAB
    preferences. The standard processing pipeline is now to import data,
    filter, re-reference, apply artifact rejection (default is using the
    clean\_rawdata plug-in), run ICA, detect bad components (default is
    using ICLabel)
-   <b>Default plug-ins</b>. There are now 4 EEGLAB plug-in installed with
    EEGLAB. Dipfit and firfilt - which were already installed by default
    in previous EEGLAB revision - and now clean\_rawdata and ICLabel.
    Clean\_rawdata is a powerful plug-in based on ASR (Artifact Subspace
    Reconstruction) to automatically remove or correct artifacts.
    ICLabel is an algorithm to automate ICA component labeling (as brain
    or artifact).
-   We have also redesigned the plotting options at the study level to
    make them more user friendly, and now allow to plot ERPimage, and
    time-frequency decompositions in scalp arrays (previously this was
    only possible for ERP and spectrum).
-   There is a <b>new plug-                                                  in manager</b> (there was a new one in 2019.0
    but it yet a newer one) which automates plug-in release for improved
    stability. This new manager also has a rating and feedback mechanism.
    The old plug-in manager will be maintained for backward
    compatibility.
-   We have improved further the compatibility with the LIMO toolbox.
-   Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab2019..eeglab2019.1) to see all changes compared to the previous EEGLAB version.

## EEGLAB Version 2019.0

-   Issue date: May 17th, 2019; GIT tag: 2019.0
-   <b>Single-trial processing in STUDY processing functions</b>. This
    version includes a new STUDY framework compatible with LIMO (LInear
    MOdeling) applied to EEG data. We reworked
    STUDY-based computations (ERP, ERSP, ITC, mean spectra). You now
    only need to precompute these measures once, no matter how many
    statistical designs you want to run on the STUDY data. This is
    because all the single-trial level measures are now stored at the
    STUDY level. While all existing EEGLAB STUDY sets can be processed
    using STUDY functions in v2019.0, to perform additional statistical
    testing on an existing STUDY, the STUDY functions will need to
    recompute the pre-computed measure files.
-   New smart cache mechanism for STUDY processing.
-   <b>Mew plugin manager</b>
-   <b>Full Octave compatibility</b> from the command line: The freely
    available open source app will now run EEGLAB command
    line scripts written in MATLAB (note: the EEGLAB graphic interface
    and menu are not available in Octave).
-   <b>New license:</b> The open source license EEGLAB has been updated
    to BSD instead of GNU to allow commercial re-use of EEGLAB
    code (Note: each EEGLAB plugin is released under its own license).
-   The EEGLAB code repository has migrated to Github from
    Bitbucket; code for all plugins handled by the plugin manager have
    been placed in Github submodules
-   Support has been added for <b>data resampling and high/lowpass
    filtering at the STUDY level</b>.
-   Support for <b>channel selection when filtering</b> has been added -
    filters can now be applied only to selected channel subsets or
    types.
-   The <b>data import menu</b> has been cleaned up, adding direct links
    to some popular import plug-ins.
-   When performing source localization of independent components using
    DIPFIT, the brain area in which the equivalent dipole is located is
    now estimated based on direct look-up in the 40-region
    <b>Desikan-KIlliany cortical atlas</b>.
-   Use this [Github link](https://github.com/sccn/eeglab/compare/eeglab14..eeglab2019) to see all changes compared to the previous EEGLAB version.

Older versions of EEGLAB
---
- [EEGLAB version 14 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_14)
- [EEGLAB version 13 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_13)
- [EEGLAB version 12 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_12)
- [EEGLAB version 11 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_11)
- [EEGLAB version 10 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_10)
- [EEGLAB version 9 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_9)
- [EEGLAB version 8 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_8)
- [EEGLAB version 7 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_7)
- [EEGLAB version 6 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_6)
- [EEGLAB version 5 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_5)
- [EEGLAB version 4 revision history](https://sccn.ucsd.edu/wiki/EEGLAB_revision_history_version_4)
