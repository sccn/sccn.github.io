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
Minor revisions are indicated using a second number: thus,
2019.0 is version 2019, first release; 2019.1 is version 2019, second release, etc..
There will usually be one or two releases per year. 
Previous major EEGLAB versions (e.g., versions 13, 14, etc.) did not use this naming scheme and did observe a regular release schedule.

## EEGLAB version 2023.1

- Issue date: August 23rd 2023; GIT tag: eeglab2023.1
- **Version statistics**: 50 files changed, 99 commits, 957 additions, and 395 deletions.
- **Major changes**: Update a variety of functions to process MEG datasets, including source localization (see [tutorial](https://eeglab.org/tutorials/misc/EEGLAB_and_MEG_data.html)). 
- **New feature**: EEGLAB redraw detects dataset changes. There is no more need to store the current dataset in the ALLEEG structure.
- **New feature**: New option "scatter" for control electrode size and color in topoplot.
- **New feature**: Computing custom features for STUDY and retreiving field content using std_readeegfield.
- **Interoperability**: Now support ERPLAB new menu status and new variables, and better support for -99 boundary event.
- **Interoperability**: Now support version of LIMO with updated GUI.
- **Bug fix**: Fixed MEG Neuromag automated coordinate transformation.
- **Bug fix**: Parfor option fix when processing multiple datasets from the EEGLAB menu. Fix parallel channel location assignment.
- **Bug fix**: Fixed issue with detecting removed channels when re-referencing the data.
- **Bug fix**: Fixed issue with saving large EEG files (>2Gb).
- **SIFT plugin**: Fixed some minor GUI issues and rewrote the tutorial, including new sections to compute statistics.
- **Clean_rawdata plugin**: New option to fuse channels rejected by clean_rawdata on multiple runs of the same subject.
- **DIPFIT plugin**: Fix handling non-EEG channels when computing Loreta 
- **bids-matlab-io plugin:** better import of MEG data, and many more small bug fixes and improvements.
  
## EEGLAB version 2023.0

- Issue date: March 3rd 2023; GIT tag: eeglab2023.0
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

## EEGLAB version 2022.1

- Issue date: Aug 2nd 2022; GIT tag: eeglab2022.1
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

- Issue date: Feb 11th 2022; GIT tag: eeglab2022.0
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
