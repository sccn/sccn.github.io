---
layout: default
title: EEGLAB revision history
parent: Other documents
---
EEGLAB revision history <font color=green>- DONE</font>
===
EEGLAB download in ZIP format is available on [this page](https://sccn.ucsd.edu/eeglab/download.php). This includes the
latest release as well as old versions of EEGLAB.

Starting in 2019, we are using the year of the release as the main
revision number. Minor revision are indicated using a second number
2019.0 is version 2019 and first release; 2019.1 is version 2019 and
second release. There are usually one or two releases per year. Prior major versions of EEGLAB (e.g., 13 or 14) did not follow a particular release schedule.

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
    clean\_rawdata plugin), run ICA, detect bad components (default is
    using ICLabel)
-   <b>Default plugins</b>. There are now 4 EEGLAB plugin installed with
    EEGLAB. Dipfit and firfilt - which were already installed by default
    in previous EEGLAB revision - and now clean\_rawdata and ICLabel.
    Clean\_rawdata is a powerful plugin based on ASR (Artifact Subspace
    Reconstruction) to automatically remove or correct artifacts.
    ICLabel is an algorithm to automate ICA component labeling (as brain
    or artifact).
-   We have also redesigned the plotting options at the study level to
    make them more user friendly, and now allow to plot ERPimage, and
    time-frequency decompositions in scalp arrays (previously this was
    only possible for ERP and spectrum).
-   There is a <b>new plug-in manager</b> (there was a new one in 2019.0
    but it yet a newer one) which automates plugin release for improved
    stability. This new manager also has a rating and feedback mecanism.
    The old plugin manager will be maintained for backward
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
-   <b>Mew plug-in manager</b>
-   <b>Full Octave compatibility</b> from the command line: The freely
    available open source app will now run EEGLAB command
    line scripts written in Matlab (note: the EEGLAB graphic interface
    and menu are not available in Octave).
-   <b>New license:</b> The open source license EEGLAB has been updated
    to BSD instead of GNU to allow commercial re-use of EEGLAB
    code (Note: each EEGLAB plug-in is released under its own license).
-   The EEGLAB code repository has migrated to Github from
    Bitbucket; code for all plug-ins handled by the plug-in manager have
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
