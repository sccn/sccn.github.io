---
layout: default
title: EEGLAB and Python
parent: Other documents
---

EEGLAB and Python <span style="color: green"> - Done</span>
===================

EEGLAB does not work natively in Python because EEGLAB runs on
MATLAB (and, to a considerable extent, on the open source Octave
platform). Nevertheless, there are possible links with Python, which we
are detailing here.

Should I use MATLAB-based tools or Python-based tools
-----------------------------------------------------

One of the most important feature when using a software package is usage and community.
If the community is large and the software is popular, it is a safer
choice as this ensures many problems people encounter have
been solved - it also means that the code is probably more stable and
has fewer bugs. 

As of 2020, 56% of the citations of the
papers below go to EEGLAB, then 25% go to Fieldtrip, and 19% go to
Brainstorm and various versions of MNE. Note that EEGLAB and Fieldtrip
are intertwined where Fieldtrip users can write [EEGLAB
plugins](/others/EEGLAB_and_Fieldtrip.html)
by adding simple wrappers on their Fieldtrip code. So the pair
EEGLAB+Fieldtrip comprises 81% of the citations, and it is continuing to
grow, with the MATLAB-based tools (which include Brainstorm) gathering
about 90% of all citations. This is a strong argument for using MATLAB
based tools - and in particular EEGLAB - instead of Python-based tools
(i.e., MNE).

Below is an analysis of papers referencing EEGLAB, FieldTrip, MNE,
MNE-Python, and Brainstorm since 2004. Data were obtained from [Web of Science](http://webofknowledge.com).
The number of citation per year corresponds to the following five papers:

-   **EEGLAB**: Delorme, A. and Makeig, S., 2004. EEGLAB: an open source
    toolbox for analysis of single-trial EEG dynamics including
    independent component analysis. Journal of neuroscience methods,
    134(1), pp.9-21
-   **Fieldtrip**: Oostenveld, R., Fries, P., Maris, E., Schoffelen, JM
    (2011). FieldTrip: Open Source Software for Advanced Analysis of
    MEG, EEG, and Invasive Electrophysiological Data. Computational
    Intelligence and Neuroscience, Volume 2011 (2011)
-   **MNE 1**: A. Gramfort, M. Luessi, E. Larson, D. Engemann, D.
    Strohmeier, C. Brodbeck, L. Parkkonen, M. Hämäläinen, MNE software
    for processing MEG and EEG data, NeuroImage, Volume 86, 1 February
    2014, Pages 446-460, ISSN 1053-8119,
-   **MNE Python**: A. Gramfort, M. Luessi, E. Larson, D. Engemann, D.
    Strohmeier, C. Brodbeck, R. Goj, M. Jas, T. Brooks, L. Parkkonen, M.
    Hämäläinen, MEG and EEG data analysis with MNE-Python, Frontiers in
    Neuroscience, Volume 7, 2013, ISSN 1662-453X
-   **Brainstorm**: Tadel, F., Baillet, S., Mosher, J.C., Pantazis, D.
    and Leahy, R.M., 2011. Brainstorm: a user-friendly application for
    MEG/EEG analysis. Computational intelligence and neuroscience, 2011,
    p.8.


![](/assets/images/EEGLAB_usage.jpg)


Major differences between MATLAB and Python
-------------------------------------------

There is a trend in imaging tool development to migrate brain imaging
tools to Python. Of course, Python (and the numpy/scipy math packages
built on Python) would be an interesting (and free) alternative to using
MATLAB. However, irrespective of what Python enthusiasts might claim,
Python might not be ideal because it remains a programming language
designed for programmers. For example,

-   It is hard to understand for novices why an n-size vector should be
    indexed, beginning at 0 and ending at n-1 (in MATLAB and R, vectors
    begin at position 1 and end at n).
-   Code indentation is a nice feature of Python. However, this style
    does not come naturally to the novice programmer. It also makes
    copying and pasting code between file sources and the command line
    interface problematic (since a snippet of code will most likely have
    unwanted indentation when copied to the Python command line).
-   Python is much more object-oriented than MATLAB, sometimes requiring
    users to understand object-oriented concepts when calling functions.
-   Python usually requires the user to install multiple external
    libraries; this can be tedious and does not come naturally to
    novices. Even experienced users sometimes spend hours getting their
    library settings right. There are also other technical problems
    related to the operating system and library compatibility that can take
    hours or days to solve (we speak from experience).
-   Matrix manipulation in Python is not as intuitive as MATLAB. For
    example, the already non-intuitive Python code to concatenate arrays
    <i>np.concatenate((np.array(\[\[/1,_2\],_\[5,_6\|1, 2\], \[5,
    6\]\]), np.array(\[1, 2\])))</i> will fail because, unlike MATLAB,
    1-D vectors are not compatible with 2-D matrices by default - and
    need explicit conversion. Compare to MATLAB simpler notation <i>\[
    \[1 2; 5 6\]; \[1 2\] \]</i> or <i>\[ \[1 2; 5 6\] \[1 2\]' \]</i>
    depending on the dimension to concatenate. The MATLAB code is
    readable for someone with math training.
-   And of course, version problems: Python versions 2 and 3 are not
    fully compatible -- and Python 2.7, although no longer supported
    since January 1, 2020, is still widely used because a large number
    of Python libraries are not available in Python 3 -- leading to all
    kinds of unexpected problems that can slow down a novice
    programmer.
-   Python is free. Why should I have to pay for MATLAB? Good conduct in
    (open) science should transcend discussions on finances. We pay for
    Microsoft or Adobe licenses because the free alternative, even
    if it exists, does not fulfill our needs. The compiled version of
    EEGLAB does not require users to purchase MATLAB, and EEGLAB code
    also runs on Octave.
-   MEEG software packages on MATLAB are mainly EEGLAB, Fieldtrip, and
    Brainstorm. MEEG software on Python is MNE which is more tailored to MEG users than EEG users.
    The MATLAB suite of available software is currently more mature than
    the Python one, which is a good reason to stick to MATLAB.

- If you wish to use Python, the [Spyder IDE](https://www.spyder-ide.org/) is a good equivalent of the MATLAB interface and should feel familiar.

How to call EEGLAB functions from Python
----------------------------------------

If you want or need to call EEGLAB functions from Python, the best
solution is to use the Python package Oct2py (pip install Oct2py). You
will need to install Octave as well. See [this
page](/others/Running_EEGLAB_on_Octave.html) for more information on how
to run EEGLAB on Octave. The way this Python library works is that it
converts Python data structures to MATLAB/Octave data structures and
vice versa. Based on our research, it is the simplest and most stable way
to run MATLAB functions in Python, and most EEGLAB functions may be
called from within Python using this method.

``` Python
# import dataset from EEGLAB
from oct2py import octave
octave.addpath('/data/matlab/eeglab/functions/guifunc');
octave.addpath('/data/matlab/eeglab/functions/popfunc');
octave.addpath('/data/matlab/eeglab/functions/adminfunc');
octave.addpath('/data/matlab/eeglab/functions/sigprocfunc');
octave.addpath('/data/matlab/eeglab/functions/miscfunc');
EEG = octave.pop_loadset('/data/matlab/eeglab/sample_data/eeglab_data_epochs_ica.set');

# plot first trial of channel 1
import matplotlib.pyplot as plt
plt.plot(EEG.data[0][0]);
plt.show()
```

The SCIPY Python library can import EEGLAB files, when the raw data is embeded in the *.set* file.

``` Python
import scipy.io as sio
EEG = sio.loadmat('eeglabfile.set')
```

If the raw data is stored in a separate *.fdt* file, the *read_epochs_eeglab* MNE function can also import EEGLAB data files.

``` Python
import mne
EEG = mne.io.read_epochs_eeglab('eeglabfile.set')
```

Will EEGLAB ever run natively on Python?
----------------------------------------

For the foreseeable future, MATLAB will remain the platform on, which
EEGLAB is developed and supported. MATLAB has a breadth of useful tools
that are not yet matched by open source environments (e.g., no complex
system to install libraries, good graphical support for different
platforms, 3-D interactive graphics with transparency, powerful
debugging tools, capacity to run native Java code), plus a wealth of
available MATLAB toolboxes are handy, well known and well tested (e.g.,
image processing toolbox, for correcting for multiple comparisons;
signal processing toolbox, for spectral decompositions; optimization
toolbox, for optimizing code; bioinformatics toolbox, useful for EEG
classification; virtual reality toolbox, for the real-time 3-D rendering of
EEG activity). Finally, the MATLAB compiler allows us to create a
compiled version of EEGLAB that does not require the user to have MATLAB
-- MATLAB scripts can be run by [compiled
EEGLAB](/others/Compiled_EEGLAB.html), although interactive sessions
are not supported. Given that MATLAB is accessible to nearly everyone
working in scientific institutions, our incentive to find a MATLAB
alternative remains relatively low.

Rather than re-implementing EEGLAB on Python, we will be more likely to focus on increasing cross-compatibility between EEGLAB and Python, making it easier for users to go back and forth between the two.