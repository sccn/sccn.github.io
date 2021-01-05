---
layout: default
title: EEGLAB Bugs
parent: Other documents
---
EEGLAB BUGS <span style="color: green">- DONE</span>
===

Dealing with EEGLAB bugs and suggestions
---

EEGLAB bugs are managed under [Github EEGLAB
Issues](https://github.com/sccn/eeglab/issues). The old [EEGLAB Bugzilla
interface](https://sccn.ucsd.edu/bugzilla/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=ON%20HOLD&bug_status=CHECKDEV&f0=OP&f1=OP&f3=CP&f4=CP&list_id=549&query_format=advanced)
has been deprecated, although it is still being used to track potential
improvements.

Since EEGLAB has been developed under Matlab, there are little risks
that using EEGLAB will crash your machine or erase files
inadvertently, unless Matlab itself crashes. This is one advantage
of using Matlab.

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
-  Please first read the Matlab command-line and any error window text carefully to determine whether you may
    be able to avoid the problem directly.
-  Next, test whether the error
    occurs using the current release of EEGLAB. If so, check the [Github
    EEGLAB Issues](https://github.com/sccn/eeglab/issues) to see if your
    issue has already been reported:
    -   If your issue has been reported, you may comment on the bug.
    -   If your issue has not been reported, you may submit a new bug.
        Once you press the "New issue" button, you will be guided on how
        on the type of information needed to report your bug.

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

-   *Spectral analysis (with no Matlab Signal Processing Toolbox):*
    The spec.m function emulates the function psd.m but not the function
    pwelch.m (psd.m was replaced by pwelch.m, beginning with EEGLAB 4.3,
    for [technical
    reasons](http://www.mathworks.com/support/solutions/data/24750.shtml)).
    As a result, the scaling of the spectrum (by the spectopo.m function
    only) may differ. Also, for unknown reasons, the spec.m function
    cannot handle frequencies that have been filtered out and may return
    inaccurately high power at these frequencies.

-   *Matlab versions and OS:* Matlab versions have different bugs
    under different OS and these bugs - usually graphical bugs - may
    affect EEGLAB. The latest one we know of is the fact that Matlab
    version 2018a (all OS) requires a patch for EEGLAB to work.

