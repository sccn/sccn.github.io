---
layout: default
title: EEGLAB v12 and earlier plugins
parent: Other documents
---
EEGLAB plugins and extensions
=====

This page describe popular EEGLAB plugins. The
most current plugin/extension page is available
[here](http://sccn.ucsd.edu/eeglab/plugin_uploader/plugin_list_all.php).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


### Data import extensions for EEGLAB

These extensions allow to import various type of data. Although EEGLAB
contains native function to import some data formats, these functions
support other formats.

-   **BIOSIG data import:** Import/export data in a wide variety of data
    formats, developed by [Alois
    Schloegl](mailto:alois.schloegl@ist.ac.at), the creator of the EDF+
    data format. For more information about BIOSIG toolbox from [this
    page](http://biosig.sourceforge.net/).

<!-- -->

-   **FileIO:**: toolbox allowing data import in multiple data formats.

<!-- -->

-   **CTF data import:** Import CTF MEG data. Available from Darren
    Weber's [EEG sourceforge](http://eeg.sourceforge.net) project, this
    extension imports MEG data (plus concurrent EEG, if any) plus sensor
    locations and data events from data in the CTF (Vancouver, CA) data
    format.

<!-- -->

-   **ANT data import (v1.03):** Import data files in the EEP format.
    Contributed by [ANT Software](http://www.ant-software.nl)
    (Netherlands) to import data in their format. Email contact:
    <info@ant-software.nl>.

<!-- -->

-   **BVA data import/export:** Import/export files from/to the Brain
    Vision Software Analyser suite. Contributed by Andreas Widmann of
    the University of Leipzig (Germany) with Arnaud Delorme.

<!-- -->

-   **Neuroimaging 4D:** Christian Wienbruch of the University of
    Konstanz (Germany) has an extension available for loading
    Neuroimaging 4-D data into EEGLAB.

<!-- -->

-   **TDT data import:** Adam Wilson at the NITRO Lab at the University
    of Wisconsin Madison (USA) offers an extension available for loading
    Tucker-Davis Technology format data into EEGLAB.

<!-- -->

-   **NeurOne data import:** EEGLAB extension for reading the file
    format of NeurOne system.

### Data processing extensions for EEGLAB

Many other EEGLAB extensions are available for EEGLAB. The list below is
not complete, and the methods they make available may have not been
assessed by the EEGLAB developers. (We recommend that EEG researchers
thoroughly study and consider the basis of any methods they apply to
experimental data). To allow us to add new extensions or information to
the list below, send us an email at <eeglab@sccn.ucsd.edu>:

-   **DIPFIT2:** Dipole modeling of independent data components using a
    spherical or boundary element head model. Uses functions from the
    FIELDTRIP toolbox of [Robert
    Oostenveld](http://www.miba.auc.dk/%7Eroberto/) at the Donders
    Center, University of Nijmegen. A [DIPFIT2
    tutorial]() is available.

<!-- -->

-   **IIRfilt:** Infinite impulse response filtering: Apply short
    non-linear filters to EEGLAB data. Contributed by [Maksyn
    Pozdin](http://www.nrc-iol.org/personnel).

<!-- -->

-   **FMRIB:** Remove FMRI-environment artifacts from EEGLAB data. This
    extension, by [Rami
    Niazy](http://www.fmrib.ox.ac.uk/%7Erami/fmribplugin) of Cardiff
    University (Wales, UK), allows removal of scanner-related artifacts
    from EEG data collected during fMRI scanning. These tools provide a
    gui for removing FMRI gradient artifacts, detecting QRS complexes
    from an ECG channel, and removing pulse-related
    ballistocardiographic (BCG) artifacts from the EEG data. All of the
    tools can also be used from the Matlab command line, allowing expert
    users to use them in custom scripts.

<!-- -->

-   **LORETA:** Import/export command line bridge function between
    EEGLAB and this well-known 'low-resolution' EEG source imaging
    approach by [R.D.
    Pascual-Marqui](http://www.unizh.ch/keyinst/NewLORETA/LORETA01.htm).
    Contributed by [Arnaud Delorme](http://www.nrc-iol.org/personnel).

<!-- -->

-   **CLUSTSET:** Cluster ICs of a single dataset by their residual
    mutual information. See tutorial [here](/A10:_MI-clust "wikilink").
    Contributed by Nima Bigdely Shamlo of SCCN (UCSD, La Jolla)

<!-- -->

-   **AAR (Automatic Artifact Removal toolbox):** This toolbox ([web
    page here](http://kasku.org/aar/)), implemented as an EEGLAB extension, aims to integrate several state-of-the-art methods for automatic removal of ocular and muscular artifacts in the electroencephalogram (EEG). Contact is [German Gomez Herrero](mailto:german.gomezherrero@tut.fi) (Tampere, Finland) for details.

<!-- -->

-   **ADJUST:** A completely automatic algorithm that identifies artifact-related Independent Components by combining stereotyped artifact-specific spatial and temporal features. Features are optimized to capture blinks, eye movements and generic discontinuities. Once artifacte-related ICs are identified, they can be simply removed from the data while leaving the activity due to neural sources almost unaffected. Download the extension and tutorial [here](http://www.unicog.org/pm/pmwiki.php/MEG/RemovingArtifactsWithADJUST).
    Contact mail: [ADJUST staff](mailto:adjust.staff@gmail.com).
    Contributed by [Andrea Mognon](https://www.portale.unitn.it/cimec/portalpage.do?channelId=-52074&channel2Id=-50286&content_OID=267997&page=/jsp/editorial/editorial.jsp&programId=267999)
    and [Marco Buiatti](http://www.unicog.org/pm/pmwiki.php/Main/MarcoBuiatti).

<!-- -->

-   **batch_context:** The batch_context extension provides an interface
    for generating data processing pipelines and executing them on
    multiple EEGLAB data files either locally or on remote compute
    clusters. The main development source is located at
    [1](https://git.sharcnet.ca/bucanl_eeglab_extensions/batch_context).
    Email James [here](mailto:jdesjard@sharcnet.ca).

<!-- -->

-   **BCILAB**: An extensive toolbox by [Christian
    Kothe](http://scholar.google.com/citations?user=3hAFHB4AAAAJ&hl=en)
    for building and running online brain-computer interface (BCI)
    models for a wide variety of purposes (volitional control, cognitive
    monitoring, neurofeedback, etc.). Extensive documentation and code
    are available [here](http://sccn.ucsd.edu/wiki/BCILAB), and a series
    of over 60 short video lectures
    [here](http://sccn.ucsd.edu/wiki/Introduction_To_Modern_Brain-Computer_Interface_Design).

<!-- -->

-   **BERGEN:** Removal of fMRI-related gradient artifacts from
    simultaneous EEG-fMRI data. The BERGEN extension for EEGLAB provides
    a GUI with different methods for gradient artifact correction.
    Contributed by [Matthias Moosmann](mailto:moosmann@gmail.com) and
    [Emanuel Neto](mailto:netoemanuel@gmail.com).

<!-- -->

-   **CIAC (cochlear implant artifact correction):** is a semi-automatic
    ICA-based tool for the correction of electrical artifacts
    originating from cochlear implants. A [validation
    paper](http://www.sciencedirect.com/science/article/pii/S0378595511003030)
    describing CIAC in detail has been published in Hearing Research.
    [More info and
    download](http://www.debener.de/CIAC_tutorial/ciacplugin.html).

<!-- -->

-   **CORRMAP:** Semi-automatic identification of common EEG artifacts
    based in a template. The CORRMAP extension consists of a set of
    Matlab functions allowing the identification and clustering of
    independent components representing common EEG artifacts (eye
    blinks, other ocular artifacts and heartbeat artifacts) in a large
    number of datasets (requires STUDY structure). Contributed by
    [Filipa Campos Viola](mailto:filipa.viola@uni-oldenburg.de).
    Download extension and tutorial available
    [here](http://www.debener.de/).

<!-- -->

-   **ERPLAB**: The [ERPLAB
    Toolbox](http://www.erpinfo.org/erplab/erplab-home/) is a set of
    open source Matlab routines for analyzing ERP data that operate as a
    set of extensions to EEGLAB. The development of ERPLAB Toolbox is
    being coordinated by Steve Luck and Javier Lopez-Calderon at UC
    Davis.

<!-- -->

-   **EYE-EEG**: The [EYE-EEG Toolbox](http://www2.hu-berlin.de/eyelab/)
    is an extension for EEGLAB developed by Olaf Dimigen & Ulrich
    Reinacher in Werner Sommer's Biological Psychology lab at Humboldt
    University Berlin with the goal of facilitating integrated analyses
    of electrophysiological and oculomotor data. The extension parses,
    imports, and synchronizes simultaneously recorded eye tracking data
    and adds it as extra channels to the EEG. Saccades and fixations can
    be imported from the eye tracking raw data or detected with a
    velocity-based algorithm. Eye movements are added as new
    time-locking events to the existing EEGLAB event structure, allowing
    easy saccade- and fixation-related EEG analyses in the time and
    frequency domains (e.g., fixation-related potentials, FRPs).
    Alternatively, EEG data can be aligned to stimulus onsets and
    analyzed according to oculomotor behavior (e.g. pupil size,
    microsaccades) in a given trial. Saccade-related ICA components can
    be objectively identified based on their covariance with the
    electrically independent eye tracker.

<!-- -->

-   **FASTER:** implements a fully automated, unsupervised method for
    processing of high density EEG data. FASTER can be used to process
    EEGLAB datasets, .set and .bdf files. Includes common features such
    as data importing, epoching, re-referencing, and grand average
    creation, as well as automated channel, epoch and artifact rejection
    based on ICA. FASTER has been peer-reviewed, it is free and the
    software is open source. If you use FASTER, please reference: Nolan,
    H., Whelan, R., & Reilly, R.B. *Journal of Neuroscience Methods,
    192*, 152-162, which can be obtained
    [here](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6T04-50KC6J3-5&_user=10&_coverDate=09%2F30%2F2010&_rdoc=21&_fmt=high&_orig=browse&_origin=browse&_zone=rslt_list_item&_srch=doc-info%28%23toc%234852%232010%23998079998%232330742%23FLA%23display%23Volume%29&_cdi=4852&_sort=d&_docanchor=&_ct=23&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=ae1dfffa89b5bcd673c56eed2c3251dd&searchtype=a).
    Download FASTER [here](https://sourceforge.net/projects/faster/).
    Contributed by [Hugh
    Nolan](http://www.mee.tcd.ie/neuraleng/People/Hugh) and [Robert
    Whelan](http://www.mee.tcd.ie/neuraleng/People/Robert).

<!-- -->

-   **FIRfilt:** Apply a variety of linear filters to EEGLAB data.
    Contributed by [Andreas
    Widmann](http://www.uni-leipzig.de/%7Epsycho/biopsych/widmann/index.html)
    (Leipzig, Germany). Latest version updates are available
    [here](http://www.uni-leipzig.de/%7Ebiocog/widmann/eeglab-plugins.shtml).
    For more information about this extension, check [firfilt
    FAQ](/firfilt_FAQ "wikilink").

<!-- -->

-   **Grandaverage:** Perform grand averaging across specified EEGLAB
    datasets. Contributed by [Andreas
    Widmann](http://www.uni-leipzig.de/%7Epsycho/biopsych/widmann/index.html)
    of the University of Leipzig (Germany). Download
    [here](http://www.uni-leipzig.de/%7Ebiocog/widmann/eeglab-plugins.shtml).

<!-- -->

-   **LIINC extensions:** Cogniscan data import, Linear Discrimination,
    Generalized Eigenvalue decomposition, Common Spatial Patterns, Peak
    Fitting, Eye Movement Removal: Paul Sajda and colleagues at the
    LIINC Lab at Columbia University (New York City) distribute several
    extensions for use in single-trial response detection. A reference
    article has been published
    [here](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WNP-4GSTS3N-1&_user=4429&_handle=V-WA-A-W-WW-MsSAYVA-UUW-U-AABZZEYUAZ-AABVWDYYAZ-CWEWWYWBU-WWU&_fmt=summary&_coverDate=11%2F01%2F2005&_rdoc=5&_orig=browse&_srch=%23toc%236968%232005%23999719997%23608050%21&_cdi=6968&view=c&_acct=C000059602&_version=1&_urlVersion=0&_userid=4429&md5=4080fbde8b83f9d280394d162b70c580).
    The download link is
    [here](http://liinc.bme.columbia.edu/downloads/).

<!-- -->

-   **MARA:** Automatic identification of artifactual independent
    components contributed by Irene Winkler and colleagues. MARA is a
    linear classifier that learns from expert ratings by extracting six
    features from the spatial, the spectral and the temporal domain.
    Features were optimized to solve the binary classification problem
    "reject vs. accept", and should be able to handle eye artifacts,
    muscular artifacts and loose electrodes equally well. Download the
    extension and tutorial
    [here](http://www.user.tu-berlin.de/irene.winkler/artifacts/).

<!-- -->

-   **Mass Univariate ERP Toolbox:** is a freely available set of MATLAB
    functions by David Groppe and colleagues for performing mass
    univariate analyses of event-related brain potentials (ERPs), a
    noninvasive measure of neural activity popular in cognitive
    neuroscience. A mass univariate analysis is the analysis of a
    massive number of simultaneously measured dependent variables via
    the performance of univariate hypothesis tests (e.g., t-tests).
    Savvy corrections for multiple comparisons are applied to make
    spurious findings unlikely while still retaining a useful degree of
    statistical power. This approach is popular in the fMRI community
    but has not been commonly used by ERP researchers. Compatible with
    EEGLAB and ERPLAB. Documentation and downloads
    [here](http://openwetware.org/wiki/Mass_Univariate_ERP_Toolbox). See
    also [David's lecture on multiple
    comparisons](http://www.cogsci.ucsd.edu/~dgroppe/EEGLAB12_statistics.html)
    in the [Online EEGLAB
    Workshop](https://sccn.github.io/workshops/Online_EEGLAB_Workshop.html).

<!-- -->

-   **MPT**: A toolbox for Measure Projection Analysis developed by Nima
    Bigdely-Shamlo at SCCN/UCSD for projecting EEG measures tagged by
    source location into a common template brain space, testing local
    spatial measure consistency, and parsing measure-consistent brain
    areas into measure-separable domains. Attractive 3-D graphics and
    some support for condition and group statistics are provided. A
    [paper](http://dx.doi.org/10.1016/j.neuroimage.2013.01.040) is
    available.

<!-- -->

-   **NFT**: The Neuroelectromagnetic Forward Head Modeling Toolbox, an
    elaborate extension by Zeynep Akalin Acar, builds custom Boundary
    Element Method (BEM) and Finite Element Model (FEM) forward head
    models from subject MR head images and/or from an MNI template brain
    model warps to measured electrode positions. Web documentation and a
    reference paper are available [here](http://sccn.ucsd.edu/wiki/NFT).

<!-- -->

-   **PACT:** is an EEGLAB extension for computing cross-frequency
    phase-amplitude coupling developed by [Makoto
    Miyakoshi](http://scholar.google.com/citations?user=9VGJVCQAAAAJ&hl=en)
    at SCCN/UCSD, with with documentation
    [here](http://sccn.ucsd.edu/wiki/PACT)

<!-- -->

-   **REGICA:** An extension by Manousos A. Klados of Aristotle
    University of Thessaloniki, Greece to remove EOG artifacts by
    regression performed on ICA components. A semi-simulated dataset
    that might be used in any artifact rejection study is also
    available. A paper on the method is
    [here](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B7XMN-52D4JVY-1&_user=10&_coverDate=03%2F16%2F2011&_rdoc=1&_fmt=high&_orig=gateway&_origin=gateway&_sort=d&_docanchor=&view=c&_searchStrId=1704452099&_rerunOrigin=scholar.google&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=047e95f03c74abe6814a87f1d519898c&searchtype=a).
    Email Manousos Klados [here](mailto:mklados@med.auth.gr).

<!-- -->

-   **SIFT**: The Source Information Flow Toolbox by [Tim
    Mullen](http://www.antillipsi.net/) computes a wide variety of
    multivariate effective causal models of source-resolved EEG data.
    Interactive visualizations and animations of event-related
    'information flow' networks are included. Extensive documentation is
    available [here](http://sccn.ucsd.edu/wiki/SIFT).

<!-- -->

-   **bioelectromag**: The
    [bioelectromagnetism](http://eeg.sourceforge.net/bioelectromagnetism.html)
    Matlab toolbox is interfaced in this extension to plot average ERPs
    and to find their minima and maxima. Only a few files from this
    toolbox are included in this extension.

<!-- -->

-   **Fieldtrip**: The [Fieldtrip](http://fieldtrip.fcdonders.nl/)
    toolbox may be used an extension to EEGLAB. Some Fieldtrip functions
    are used within EEGLAB for source localization (DIPFIT) and for
    computing STUDY statistics.

### Other Matlab EEG tools working well with EEGLAB

The tools below may not create new EEGLAB menus. Nevertheless they may
be used with EEGLAB.

-   **Svarog data format:** This web site allows importing Svarog data
    format. Though this is not an EEGLAB extension, once data and its
    parameters have been imported into Matlab, they can be imported into
    EEGLAB [link](http://karolaugustin.pl/svarog2matlab-2/).

<!-- -->

-   **LOC:** Performs approximate localization of electrocorticographic
    electrode positions from x-ray images, as documented by Kai Miller
    (University of Washington, Seattle) in this [J. Neurosci. Methods
    paper](http://sccn.ucsd.edu/%7Escott/pdf/kjm_jneurometh_2007.pdf).
    The download link is
    [here](http://sccn.ucsd.edu/eeglab/plugins/loc.zip) (27.8 MB)\].

<!-- -->

-   **LIINC extensions:** Bilinear Discriminant Component Analysis
    (BDCA) by Paul Sajda and colleagues at the LIINC Lab at Columbia
    University (New York City). The download link is
    [here](http://code.google.com/p/bdca/).

<!-- -->

-   **BESAfit:** dipole modeling using BESA3: Computes equivalent dipole
    locations for independent data components using [BESA (old) version
    3.0](http://www.besa.de/) (Megis Software, Germany) run external to
    Matlab. Download extension version 1.0
    [here](ftp://sccn.ucsd.edu/pub/besa1.0_plugin.tar.gz).

<!-- -->

-   **Micromed data import:** Micromed (Italy) has an extension
    available for loading their data format into EEGLAB. Contact
    [Cristiano Rizzo](mailto:cristiano.rizzo@micromed-it.com) for
    details.

Many other EEGLAB plug-ins may be available from authors' or
maintainers' web sites. The (alphabetically sorted) list below is not
complete, and the methods they make available may have not been assessed
by the EEGLAB developers. (We recommend that EEG researchers thoroughly
study and consider the basis of any methods they apply to experimental
data). To allow us to add new plug-ins or information to the list below,
send an email to us at <eeglab@sccn.ucsd.edu>: