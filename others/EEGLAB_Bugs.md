---
layout: default
title: EEGLAB Bugs
long_title: EEGLAB Bugs
parent: Support
---
EEGLAB bugs
===
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Dealing with EEGLAB bugs and suggestions
---

EEGLAB bugs are managed under [Github EEGLAB
Issues](https://github.com/sccn/eeglab/issues). The old [EEGLAB Bugzilla
interface](https://sccn.ucsd.edu/bugzilla/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=ON%20HOLD&bug_status=CHECKDEV&f0=OP&f1=OP&f3=CP&f4=CP&list_id=549&query_format=advanced)
has been deprecated, although it is still being used to track potential
improvements.

Since EEGLAB has been developed under MATLAB, there are little risks
that using EEGLAB will crash your machine or erase files
inadvertently, unless MATLAB itself crashes. This is one advantage
of using MATLAB.

About 1000 [test cases](https://sccn.ucsd.edu/wiki/EEGLAB_test_cases) run daily on EEGLAB code to test its integrity
    and that its functions are stable.

 EEGLAB is an open-source project. To understand in more detail how
    any signal processing is performed, you may study the
    function source file. To adjust its performance, you may edit
    it yourself. Note: If you do this successfully, please consider
    issuing a pull request on Github. See more information on
    [contributing to
    EEGLAB](https://sccn.ucsd.edu/wiki/A07:_Contributing_to_EEGLAB).

How do I report a Bug?
---
If you encounter a bug:
-  Please first read the MATLAB command-line and any error window text carefully to determine whether you may
    be able to avoid the problem directly.
-  Next, test whether the error
    occurs using the current release of EEGLAB. If so, check the [Github
    EEGLAB Issues](https://github.com/sccn/eeglab/issues) to see if your
    issue has already been reported:
    -   If your issue has been reported, you may comment on the bug.
    -   If your issue has not been reported, you may submit a new bug.
        Once you press the "New issue" button, you will be guided on how
        on the type of information needed to report your bug.

Mex files errors in EEGLAB
---

EEGLAB itself does not include any
precompiled functions (also called mex functions). If you get an error "could not locate mex file" or any related mex file
error, do not blame EEGLAB. However, some
external modules use mex files for reading binary data files or
performing source localization. Usually, an error indicates the
precompiled file is not available for your platform (it would thus need
to be recompiled, something you can sometimes do yourself - for more
information, see below). There are mainly four modules in EEGLAB that use mex
files.

-   Fieldtrip functions: If you get an error that some functions in the
    Fieldtrip folder cannot be found, refer to the [Fieldtrip
    documentation](https://www.fieldtriptoolbox.org/faq/matlab_complains_about_a_missing_or_invalid_mex_file_what_should_i_do/)
    for how to recompile such functions.

-   BIOSIG: Some release of BIOSIG contains some updated mex files so
    you might want to check if you have the latest version of BIOSIG.
    Sometimes BIOSIG does not preserve backward compatibility so you may
    experience problem when reading data after updating BIOSIG.

-   ANT plugin: The ANT plugin was made by the ANT company. Contact
    [ANT](mailto:info@ant-neuro.com) for an updated version of the
    compiled binaries.

-   ERPSS plugin: Simply recompile decompresserpss.c (type "mex
    decompresserpss.c")

Some known EEGLAB bugs and/or missing features:
---

-   *Epoch selection using pop_eegplot.m:* Epochs selected for
    rejection using *eegplot* data scrolling are not saved in EEGLAB
    history until the epochs are rejected. This means that they
    will not be reproduced automatically in a new EEGLAB session.
    However, the labeled epochs are identified in the field
    EEG.reject.manualrej that is saved along with the dataset. Also, and
    more importantly, when the labeled epochs are rejected,
    this operation is saved in EEGLAB history.

-   *Zooming using pop_eegplot.m*: When zooming and selecting
    epochs, only the data (no the background epoch markings) may be zoomed.

-   *Spectral analysis (with no MATLAB Signal Processing Toolbox):*
    The spec.m function emulates the function psd.m but not the function
    pwelch.m. As a result, the scaling of the spectrum (by the spectopo.m function
    only) may differ. Also, for unknown reasons, the spec.m function
    cannot handle frequencies that have been filtered out and may return
    inaccurately high power at these frequencies.

-   *MATLAB versions and OS:* MATLAB versions have different bugs
    under different OS and these bugs - usually graphical bugs - may
    affect EEGLAB. The latest one we know of is the fact that MATLAB
    version 2018a (all OS) requires a patch for EEGLAB to work.

