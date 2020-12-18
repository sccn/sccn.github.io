---
layout: default
title: EEGLAB and python
parent: Other documents
---

EEGLAB of course does not work natively in python because EEGLAB runs on
Matlab (and, to a considerable extent, on the open source Octave
platform). Nevertheless, there are possible links with Python which we
are detailing here.

Should I use Matlab-based tools or Python-based tools
-----------------------------------------------------

One of the most important when using a software is usage and community.
If the community is large and the software is popular, it is a safer
choice as you can be certain a lot of problems people encounter have
been solved - it also means that the code is probably more stable and
has less bugs. As of late 2019/early 2020, 56% of the citations of the
papers below go to EEGLAB, then 25% go to Fieldtrip and 19% got to
Brainstorm, and various versions of MNE. Note that EEGLAB and Fieldtrip
are intertwined where Fieldtrip users can write [EEGLAB
plugins](/EEGLAB_and_Fieldtrip#Wrap_up_your_Fieldtrip_scripts_into_EEGLAB_plugin_menu_items "wikilink")
by adding simple wrappers on their Fieldtrip code. So the pair
EEGLAB+Fieldtrip comprises 81% of the citations and it is continuing to
grow, with the Matlab-based tools (which include Brainstorm) gathering
about 90% of all citations. This is a strong argument for using Matlab
based tools - and in particular EEGLAB - instead of Python based tools
at this stage (i.e. MNE). Note that MNE was given an unfair advantage in
this analysis since 2 papers (instead of 1 for the other tools) were
included (and it is reasonable to assume that a portion of papers cited
both articles thus artificially inflating MNE numbers).

Below is an analysis of papers referencing EEGLAB, FieldTrip, MNE,
MNE-Python, and Brainstorm since 2004. Data was obtained Web of Science.
The citation per year correspond to the following 5 papers:

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


![600px](/assets/images/Eeglab_usage.jpg)


Major differences between Matlab and Python
-------------------------------------------

There is a trend in imaging tool development to migrate brain imaging
tools to Python. Of course, Python (and the numpy/scipy math packages
built on Python) would be an interesting (and free) alternative to using
Matlab. However, irrespective of what Python enthusiasts might claim,
Python might not be ideal because it remains a programming language
designed for programmers. For example,

-   It is hard to understand for novices why an n-size vector should be
    indexed beginning at 0 and ending at n-1 (in Matlab and R, vectors
    begin at position 1 and end at n).
-   Code indentation is a nice feature of Python. However, this style
    does not come naturally to the novice programmer. It also makes
    copying and pasting code between file sources and the command line
    interface problematic (since a snippet of code will most likely have
    unwanted indentation when copied to the Python command line).
-   The closest alternative to the Matlab interactive interface is the
    Jupyter notebook environment that runs in your browser. Yet the
    graphical capabilities of Jupyter notebook are very limited (it is
    sometimes hard to manipulate figures, impossible to zoom, etc...).
    Also, all your code needs to be on one (very very long) page and it
    is hard to create subscripts or make your code modular. Executing
    blocks of code not in the order set in the notebook can be
    confusing. Most people we know who have used Matlab and tried
    Jupyter notebook hate Jupyter notebook - then learn to live with the
    limitations if they absolutely need it for their work.
-   Python is much more object-oriented than Matlab, sometimes requiring
    users to understand object-oriented concepts when calling functions.
-   Python usually requires the user to install multiple external
    libraries; this can be tedious and does not come naturally to
    novices. Even experienced users sometimes spend hours getting their
    library settings right. There are also other technical problems
    related to operating system and library compatibility that can take
    hours or days to solve (we speak from experience).
-   Matrix manipulation in Python is not as intuitive as Matlab. For
    example, the already non-intuitive Python code to concatenate arrays
    <i>np.concatenate((np.array(\[\[/1,_2\],_\[5,_6\|1, 2\], \[5,
    6\]\]), np.array(\[1, 2\])))</i> will fail because, unlike Matlab,
    1-D vectors are not compatible with 2-D matrices by default - and
    need explicit conversion. Compare to Matlab simpler notation <i>\[
    \[1 2; 5 6\]; \[1 2\] \]</i> or <i>\[ \[1 2; 5 6\] \[1 2\]' \]</i>
    depending on the dimension to concatenate. The Matlab code is
    readable for someone with math training.
-   And of course, version problems: Python versions 2.7 and 3.3 are not
    fully compatible -- and Python 2.7 although no longer supported
    since January 1, 2020, is still widely used because a large number
    of Python libraries are not available in Python 3 -- leading to all
    kinds of unexpected problems that can terribly slow down a novice
    programmer.
-   Python is free. Why should I have to pay for Matlab? Good conduct in
    (open) science should transcend discussions on finances. We pay for
    Microsoft or Adobe licenses, because of the free alternative, even
    if it exists, does not fulfill our needs. The compiled version of
    EEGLAB does not require users to purchase Matlab and EEGLAB code
    also runs on Octave.
-   MEEG software packages on Matlab are mainly EEGLAB, Fieldtrip, and
    Brainstorm. MEEG software on Python is MNE geared towards MEG users.
    The Matlab suite of available software is currently more mature than
    the Python one, which is a good reason to stick to Matlab for now.

How to call EEGLAB functions from python
----------------------------------------

If you want or need to call EEGLAB functions from python, the best
solution is to use the python package Oct2py (pip install Oct2py). You
will need to install Octave as well. See [this
page](/Running_EEGLAB_on_Octave "wikilink") for more information on how
to run EEGLAB on Octave. The way this Python library works is that it
converts Python data structures to Matlab/Octave data structures and
vice versa. Based on our research it is the simplest and most stable way
to run Matlab functions on Python and most EEGLAB functions may be
called from within python using this method.

``` python
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

An MNE function can also import EEGLAB data files

``` python
EEG = mne.io.read_epochs_eeglab(fname)
```

Will EEGLAB ever run natively on python?
----------------------------------------

For the foreseeable future, Matlab will remain the platform on which
EEGLAB is developed and supported. Matlab has a breadth of useful tools
that are not yet matched by open source environments (e.g., no complex
system to install libraries, good graphical support for different
platforms, 3-D interactive graphics with transparency, powerful
debugging tools, capacity to run native Java code), plus a wealth of
available Matlab toolboxes are handy, well known and well tested (e.g.,
image processing toolbox, for correcting for multiple comparisons;
signal processing toolbox, for spectral decompositions; optimization
toolbox, for optimizing code; bioinformatics toolbox, useful for EEG
classification; virtual reality toolbox, for real time 3-D rendering of
EEG activity). Finally, the Matlab compiler allows us to create a
compiled version of EEGLAB that does not require the user to have Matlab
-- Matlab scripts can be run by [compiled
EEGLAB](/A13:_Compiled_EEGLAB "wikilink"), although interactive sessions
are not supported. Given that Matlab is accessible to nearly everyone
working in scientific institutions, our incentive to find a Matlab
alternative remains relatively low, except possibly for high performance
and cloud computing applications because of license issues. However,
EEGLAB functions are fully compatible with Octave (an open source
version compatible with Matlab) from the command line - see also the new
[Open EEGLAB Portal](/EEGLAB_on_NSG "wikilink") to the NSF supercomputer
system.