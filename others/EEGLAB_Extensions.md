---
layout: default
title: EEGLAB Extensions
parent: Other documents
---
EEGLAB extensions and plugins <span style="color: green"> - Done</span>
====
{: .no_toc }

EEGLAB extensions or plugins allow users to build and publish new data
processing and/or visualization functions using EEGLAB data structures
and conventions. Plug-in functions can be easily used and tested by
selecting the new menu items they introduce into the EEGLAB menus. EEGLAB can download and install E*plugins* directly from the <span style="color: brown">File → Manage EEGLAB extensions</span> menu
item.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Lists of plugins for different EEGLAB versions
-----------------------------
The way plugins are handled has changed through EEGLAB history, leading
to more automation in more recent versions and different systems for
storing and managing plugins (the plugins themselves are often the
same across the different plugin management systems). The list of
plugins provided below is the same as the list of plugins available
through the EEGLAB plugin manager of the corresponding EEGLAB version.

-   [See the current list of plugins for EEGLAB 2019.1 and later
    versions](https://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php)
-   [See the list of plugins for EEGLAB
    2019.0](https://sccn.ucsd.edu/wiki/Plugin_list_all) (plugins on this page are no
    longer updated)
-   See the [import](https://sccn.ucsd.edu/wiki/Plugin_list_import) and [data processing](https://sccn.ucsd.edu/wiki/Plugin_list_process) extensions for EEGLAB
    13.x and 14.x (plugins and page no longer updated)

To install or update a plugin
------------------------------

Plug-ins may be installed using the EEGLAB plugin manager, using menu
item <span style="color: brown">File → Manage EEGLAB extensions</span>.

Although no longer recommended, plugins can still be installed
manually. After downloading the zip file for a plugin, uncompress the
downloaded plugin file in the main EEGLAB "plugins"
sub-directory. Remove the old version of the plugin if it is
present in the directory. Then restart EEGLAB. During start-up,
EEGLAB should print the following on the MATLAB command line:

``` matlab
> eeglab: adding plugin "eegplugin_myplugin" % (see >> help eegplugin_myplugin)
```

The plugin will typically have added one or more new items to the
EEGLAB menus (often under the *Import data* or *Tools* headings).

To uninstall a plugin
----------------------

Plug-ins can just as easily be removed from the EEGLAB extension
manager. Alternatively, you may move or remove its folder from
the EEGLAB plugins folder and restart EEGLAB.

To contribute a new plugin
--------------------------------------

See the simple instructions under [How to contribute to
EEGLAB](/tutorials/misc/Contributing_to_EEGLAB.html) to create EEGLAB compatible code.

Then, you may add your extension to the list above so that EEGLAB users can
download it automatically from within EEGLAB. To do this, use [this
form](http://sccn.ucsd.edu/eeglab/plugin_uploader/upload_form.php). If
you want to upload a new version of your plugin, you can use 
[this simplified form](http://sccn.ucsd.edu/eeglab/plugin_uploader/version_update.php).

Administrators, these are the maintenance pages to accept [Pending
plugin
requests](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/pending_requests.php)
and [Edit plugin
information](https://sccn.ucsd.edu/eeglab/plugin_uploader/protected/edit_plugin.php).

To access old versions of a plugin / extension
------------------------------------------------------

In case you need them, old versions of plugins are available for direct
download at
[http://sccn.ucsd.edu/eeglab/plugins/](http://sccn.ucsd.edu/eeglab/plugins/).
These cannot be installed through the EEGLAB extension manager. Simply
download the zip file and uncompress it in the *eeglab/plugins/* folder
(and make sure you remove any other version of the plugin you might
have installed).

Popular EEGLAB plugins
---------

We list below popular plugins available in EEGLAB. We have not assessed the methods they make available, so we recommend that EEG researchers thoroughly
study and consider the basis of any methods they apply to experimental
data. The list below is not complete, as there are currently 120 plugins available in EEGLAB. If your plugin has reached 500 downloads and it is not in the list below, please let us know.

### EEGLAB default plugins

These plugins are distributed along with the EEGLAB code.

-   **[FIRfilt](https://github.com/widmann/firfilt):** Apply a variety of linear filters to EEGLAB data.

-   **[CleanRawData](https://github.com/sccn/clean_rawdata):** Cleans raw EEG data using a variety of method, including Artifact Subspace Reconstruction.

-   **[DIPFIT](https://github.com/sccn/dipfit):** Dipole modeling of independent data components using a
    spherical or boundary element head model. Uses functions from the
    FIELDTRIP toolbox.

-   **[ICLabel](https://github.com/sccn/IClabel):** An automated EEG independent component classifier plugin for EEGLAB.

### Data collection

- **[App-MATLABViewer](https://github.com/labstreaminglayer/App-MATLABViewer/)**: Record EEG LSL streams as EEGLAB .set files.

### Data import

These extensions allow importing various types of data. Although EEGLAB
contains native functions to import some data formats, the plugins below
support other formats. There are many data import extension plugins.
We only include the most popular ones below.

- **[bids-matlab-tools](https://github.com/sccn/bids-matlab-tools)**: The bids-matlab-tool repository contains a collection of functions to import and export BIDS (Brain Imaging Data Structure)-formated experiments.

- **[BIOSIG](http://biosig.sourceforge.net/):** Import/export data in a wide variety of data
    formats.

- **[FileIO](https://github.com/fieldtrip/fileio):** Toolbox allowing data import in multiple data formats. It contains functions redundant with EEGLAB but also contains unique functions.

- **[ANTeepimport](https://www.ant-neuro.com/support/supporting-documentation-and-downloads)**: Import data files in the EEP format of the ANT EEG company.

- **[bva-io](https://github.com/arnodelorme/bva-io)**:  Import/export files from/to the Brain
    Vision Software Analyser suite.

- **[neuroscanio](https://github.com/sccn/neuroscanio)**: Import/export files from/to the Neuroscan software.

- **[MFFMATLABIO](https://github.com/arnodelorme/MFFMATLABIO)**: Import/export files from/to the EGI company in MFF format.

- **[xdfimport](https://github.com/xdf-modules/xdf-EEGLAB)**: Import files in XDF (LSL) format (EEG stream and EEG marker stream only).

- **[Mobilab](https://github.com/sccn/mobilab)**: Import files in XDF (LSL) format and allow fusing streams at different sampling rates for joint processing in EEGLAB.

### Preprocessing

-   **[IIRfilt](https://github.com/sccn/IIRfilt):** Apply short
    non-linear infinite impulse response filters to EEGLAB data.

- **[REST](https://github.com/sccn/REST):** A method to standardize a reference of scalp EEG recordings to a point at infinity.

-   **[AAR](http://kasku.org/aar/):** The Automatic Artifact Removal toolbox aims to integrate several state-of-the-art methods for the automatic removal of ocular and muscular artifacts in the electroencephalogram (EEG).

-   **[VisEd](https://github.com/BUCANL/Vised-Marks):** The Vised Marks extension for EEGLAB adds editing functions to the native *eegplot* data scrolling figure. Specifically, it allows adding/editing event markers, flagging channels/components, flagging time periods, and displaying the properties of the marks structure.

-   **[get_chanlocs](https://github.com/sccn/get_chanlocs/wiki):** The get_chanlocs EEGLAB plugin locates 3-D electrode positions from a 3-D scanned head image. A tutorial on how to acquire these images with off-the-shelf equipment is included.

### EEG/fMRI artifact removal

-   **[FMRIB](http://www.fmrib.ox.ac.uk/%7Erami/fmribplugin):** Remove fMRI-environment artifacts from EEGLAB data. This
    extension allows the removal of scanner-related artifacts
    from EEG data collected during fMRI scanning. See also the [GitHub repository](https://github.com/sccn/fmrib).

-   **[BERGEN](https://www.uib.no/en/rg/fmri/):** Removal of fMRI-related gradient artifacts from
    simultaneous EEG-fMRI data. The BERGEN extension for EEGLAB provides
    a GUI with different methods for gradient artifact correction.

### ICA-based artifact rejection and component classification

-   **[MARA](http:in.de/irene.winkler/artifacts//www.user.tu-berl/):** Automatic identification of artifactual independent
    components. MARA is a
    linear classifier that learns from expert ratings by extracting six
    features from the spatial, spectral, and temporal domains.
    
-   **[FASTER](https://sourceforge.net/projects/faster/):** implements a fully automated, unsupervised method for
    processing of high-density EEG data. FASTER includes common features such as data importing, epoching, re-referencing, grand average creation, automated channel, epoch, and artifact rejection based on ICA.

-   **[ADJUST](http://www.unicog.org/pm/pmwiki.php/MEG/RemovingArtifactsWithADJUST):** A completely automatic algorithm that identifies artifact-related Independent Components by combining stereotyped artifact-specific spatial and temporal features.

-   **[CORRMAP](https://github.com/sccn/corrmap):** Semi-automatic identification of common EEG artifacts
    based on a template. The CORRMAP extension consists of a set of
    MATLAB functions allowing the identification and clustering of
    independent components representing common EEG artifacts.

-   **[CIAC](http://www.debener.de/CIAC_tutorial/ciacplugin.html):** The cochlear implant artifact correction is a semi-automatic
    ICA-based tool for the correction of electrical artifacts
    originating from cochlear implants.

-   **[RELICA](https://github.com/sccn/relica)**: The goal of RELICA is to identify IC processes that are most stably separated from the decomposition data across many random bootstrap selections of its data frames or epochs.

-   **[MP_clustering](https://github.com/sccn/mp_clustering)**: A toolbox for Measure Projection Analysis for projecting EEG measures tagged by
    source location into a common template brain space, testing local
    spatial measure consistency, and parsing measure-consistent brain
    areas into measure-separable domains.

-   **[REGICA](https://doi.org/10.1016/j.bspc.2011.02.001):** An extension to remove EOG artifacts by
    regression performed on ICA components. A semi-simulated dataset
    that might be used in any artifact rejection study is also
    available. 

- **[SASICA](https://github.com/dnacombo/SASICA):** SASICA is an EEGLAB plugin to help you reject/select independent components based on various properties of these components.

- **[Automagic](https://github.com/methlabUZH/automagic):** Automagic is a MATLAB-based toolbox for preprocessing of EEG-datasets. It has been developed with the intention to offer a user-friendly pre-processing software for big (and small) EEG datasets.

- **[AMICA](https://github.com/japalmer29/amica):** Adaptive Mixture Independent Component Analysis (AMICA) is a binary program and EEGLAB plugin that performs an independent component analysis (ICA) decomposition on input data, potentially with multiple ICA models. Also, consider downloading the postAmicaUtility plugin. 

### Statistics and signal processing

-   **[Fieldtrip-lite](https://github.com/fieldtrip/fieldtrip):** Fieldtrip is a stand-alone toolbox but may also act as an EEGLAB extension providing source localization methods and additional statistical methods.

-   **[LIMO](https://github.com/LIMO-EEG-Toolbox/limo_tools):** The LInear MOdelling of MEEG data (LIMO MEEG) toolbox is an EEGLAB plugin dedicated to the statistical analysis of MEEG data.

-   **[ERPLAB](http://www.erpinfo.org/erplab/erplab-home/)**: The ERPLAB
    Toolbox is a set of
    open-source MATLAB routines for analyzing ERP data that operate as a
    set of extensions to EEGLAB.

-   **[EYE-EEG](http://www2.hu-berlin.de/eyelab/)**: The EYE-EEG Toolbox
    is an extension of EEGLAB developed with the goal of facilitating integrated analyses
    of electrophysiological and oculomotor data. 

-   **[mass_univ](http://openwetware.org/wiki/Mass_Univariate_ERP_Toolbox):** The Mass Univariate ERP Toolbox is a freely available set of MATLAB
    functions for performing mass
    univariate analyses of event-related brain potentials (ERPs), a
    noninvasive measure of neural activity popular in cognitive
    neuroscience.

-   **[bioelectromag](http://eeg.sourceforge.net/bioelectromagnetism.html)**: The
    bioelectromagnetism
    MATLAB toolbox is interfaced in this extension to plot average ERPs
    and to find their minima and maxima (peak finding). Only a few files from this toolbox are included in this extension.

### Source and connectivity analysis

-   **[SIFT](https://sccn.ucsd.edu/wiki/SIFT)**: The Source Information Flow Toolbox and EEGLAB plugin computes a wide variety of
    multivariate effective causal models of source-resolved EEG data.
    Interactive visualizations and animations of event-related
    'information flow' networks are included.

-   **[NFT](https://github.com/sccn/NFT/wiki)**: The Neuroelectromagnetic Forward Head Modeling Toolbox builds custom Boundary
    Element Method (BEM) and Finite Element Model (FEM) forward head
    models from subject MR head images and/or from an MNI template brain
    model warps to measured electrode positions.

- **[PACTools](https://github.com/sccn/PACTools)**: The Event-Related PACTools is an EEGLAB plugin to compute phase-amplitude coupling in single-subject data. In addition to traditional methods to compute PAC, the plugin includes the Instantaneous and Event-Related implementation of the Mutual Information Phase-Amplitude Coupling Method (MIPAC).

-   **[PACT](http://sccn.ucsd.edu/wiki/PACT):** PACT is an EEGLAB extension for computing cross-frequency
    phase-amplitude coupling.

- **[erpsource](https://github.com/sccn/erpsource)**: Source localization of ERPs using eLoreta.

### High performance computing

-   **[nsgportal](https://github.com/sccn/nsgportal)**: The NSG EEGLAB portal  to High-Performance Computing may be used to run EEGLAB scripts on high-performance computing resources via the freely available Neuroscience Gateway Portal (NSG) to the NSF-sponsored Expanse supercomputer of the San Diego Supercomputer Center. 
