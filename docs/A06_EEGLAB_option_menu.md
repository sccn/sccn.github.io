---
layout: default
title: A06 EEGLAB option menu
permalink: /docs/A06_EEGLAB_option_menu
parent: Docs
---

{ {Backward_Forward|A05:_Data_Structures|A05: Data
Structures|A07:_Contributing_to_EEGLAB|A07: Contributing to EEGLAB} }

### EEGLAB option menu

This section is intended for users who use large EEGLAB data-sets and
need to optimize their use of main memory (RAM) and disk space. To
modify the relevant EEGLAB options, select <font color = brown>File \>
Maximize memory</font>. If you cannot modify the file *eeg_options.m*
in the toolbox distribution, the window below will pop up.


<center>

![Image:option1.gif ](/assets/images/option1.gif)

</center>


Simply press *Yes*. A copy of *eeg_options.m* will be stored in the
local directory and modified when you change any of the EEGLAB options.
(Note: For EEGLAB to use this file, the current directory (.) must
appear BEFORE the EEGLAB toolbox directory in the Matlab path; see
*path()*). If the original *eeg_option.m* file is writable, EEGLAB will
modify it instead.


If the original distribution copy of the options file is modified, the
new options will affect all EEGLAB sessions using that file. If,
however, EEGLAB (or the user from the Matlab or shell commandline)
copies the options file to the current working directory, then only
EEGLAB sessions having this directory in their Matlab path (before the
EEGLAB distribution directory) will follow the modified options. It is
advised to have only one such option file to avoid confusion. Now the
following window will pop up.


<center>

[Image: Memory option gui2.png
](/assets/images/_Memory_option_gui2.png)

</center>

#### Group processing options


The top options are for processing multiple datasets in EEGLAB STUDY.
When the top option is set, EEGLAB can hold in memory more than one
data-set at a time. New data-sets are created by most of the operations
called under the <font color=brown>Tools</font> menu. With this option
set, users can undo data-set changes immediately by going back to
working with the parent (previous) data-set (unless they set the
"overwrite data-set" option when they saved the new data-set).
Processing multiple data-sets may be necessary when comparing data-sets
from separate subjects or experimental conditions.


The second option allow to save the raw data in a separate file. This
will be useful in future version of EEGLAB to read one channel at a time
from disk. This also allow faster reading of data-set when they are part
of a STUDY.


If the 3rd option is set, all the ICA activations (time courses of
activity) will be saved on disk to save computation time.

#### Memory options

The following options maximize memory usage.


The fist option forces EEGLAB to using single precision number. Unless
you have a good reason to do so, you should leave that checkbox checked.


The second option allow to process EEG dataset directly on disk, as this
is done for fMRI. This should remove any constraint on file size.
However, unlike SPM which is used to process fMRI data, EEGLAB was not
originally designed with this type of processing in mind. To be able to
use all of the EEGLAB functions that use passage of parameters by value,
we had to find a way to pass the data by reference, something that is
usually not possible in Matlab. This means that we had to implement some
hacks. We have a series of test (about 40) that check that the hack
functions are doing what they are supposed to do. However, it is hard to
guarantee that this implementation is bug free especially since it is
not the default implementation and not heavily used by users which would
help track potential bugs. Nevertheless this implementation passed the
about 5000 EEGLAB independent test cases. It is quite unlikely that
results of computation will be corrupted. Instead you can expect some
rare functions will return an error while they should not.


The third option allow to use EEG objects instead of EEG structures.
From the user perspective, it will not change anything. However, it
allows EEGLAB to process objects that are not native to EEGLAB. For
example, another software could use EEGLAB function by passing on an
object as long as this objects behaves a specific way. This option
should only be used by expert users.

#### ICA options


The first option allow to pre-computed the ICA component activities.
This may nearly double the main memory (RAM) required to work with the
data-set when you have ICA components. Otherwise, ICA activations will
be computed by EEGLAB only as needed, e.g. each time EEGLAB calls a
function that requires one or more activations. In this case, only the
activations needed will be computed, thus using less main memory.


The second option scales ICA component activities to RMS microvolt. This
scaling does not change anything in terms of data processing. When
scaling ICA component activities, ICA scalp topographies are scaled as
well so the product of the two remains constant. This scaling was not
performed in early version of EEGLAB. There is no reason to uncheck that
option unless you want to preserve backward compatibility with early
versions of EEGLAB.

#### Folder, Matlab toolboxes, and EEG connectivity and support options


The folder option is used to remember folder when reading data-sets. The
next option about using Matlab toolboxes allow to ignore such toolboxes
even if they are present in the path. This may be useful when your
university has reached its quota in terms of toolbox users. In this
case, the extra toolbox functions exist in the path but you may not use
them. The last 2 options pertain to EEGLAB connectivity, checking for
new version of EEGLAB and allowing to use the EEGLAB chat (currently
beta).

### The icadefs.m file

Using a text editor, you should edit file "icadefs.m" in the
distribution before beginning to use EEGLAB. This file contains EEGLAB
constants used by several functions. In this file, you may:

  - Specify the filename directory path of the EEGLAB tutorial. Using a
    local copy of this EEGLAB tutorial (available online at the [SCCN
    EEGLAB wiki](/EEGLAB "wikilink") requires a (recommended) [Tutorial
    Download
    (obsolete)](http://www.sccn.ucsd.edu/eeglab/download/eeglabtutorial.tar.gz).

> TUTORIAL_URL = '<http://sccn.ucsd.edu/wiki/EEGLAB>'; % online version

  - Reference the fast binary version of the *runica()* ICA function
    *ica* (see the [Binica
    Tutorial](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink")). This
    requires another (recommended) download from the SCCN
    [EEGLAB](http://sccn.ucsd.edu/eeglab/binica) site.

> ICABINARY = 'ica_linux2.4'; % \<=INSERT name of ica executable for
> binica.m

You can also change the colors of the EEGLAB interface using other
options located in the *icadefs* file.

### The dipfitdefs.m file

The dipfitdefs.m contains other constants pertaining to dipole
localization, default models, default electrode files.

[Category:IV. Appendix](/Category:IV._Appendix "wikilink") {
{Backward_Forward|A05:_Data_Structures|A05: Data
Structures|A07:_Contributing_to_EEGLAB|A07: Contributing to EEGLAB} }