---
layout: default
title: EEGLAB preferences menu
long_title: The EEGLAB preferences menu
parent: Reference Topics
grand_parent: Tutorials
---
The EEGLAB preferences menu <span style="color: green"> - Done</span>
========================

This section is intended for users who wish to customize their EEGLAB settings. If there is a setting you think should be optional, please let us know. 

Call the EEGLAB preference menu item
---

To
modify the relevant EEGLAB options, select <span style="color: brown">File → Preferences</span>. 

By default, the EEGLAB option file (*eeg_options.m*) is saved in your home folder. In the rare case where EEGLAB cannot write in your home folder, the following window will pop up.

![](/assets/images/eeglaboptions_warning.png)

If this is the case, edit the *icadefs.m* file and specify another directory for the *eeg_options.m* file using the *EEGOPTION_PATH* parameter.

Now the following window will pop up.

![](/assets/images/eeglaboptions.png)

These options are for processing multiple datasets in EEGLAB STUDY.

- When the top option is set, EEGLAB can hold in memory more than one
dataset at a time. New datasets are created by most of the operations
called under the <span style="color: brown">Tools</span> menu. With this option set, users can undo dataset changes immediately by going back to
working with the parent (previous) dataset (unless they set the
"overwrite dataset" option when they saved the new dataset).

- The second option allows saving the raw EEG data in a separate file. This option is no longer the default (as of 2021) as there are no advantages to saving two files anymore.

### ICA options

- The option in this section allows pre-computing ICA component activities.
This may nearly double the main memory (RAM) required to work with the
dataset when you have ICA components. Otherwise, ICA activations will
be computed by EEGLAB only as needed, e.g., each time EEGLAB calls a
function that requires one or more activations. In this case, only the
activations needed will be computed, thus using less main memory.

### Current folder option

- The folder option is used to remember the last folder when reading datasets. This option is set by default but may be bothersome to expert Matlab users who expect GUIs to open files in the current Matlab folder.

### EEG connectivity and support options

- The first option in this list allows settings advanced options (see also below). For this change to take effect, you must close and reopen the current GUI.

- The next three options pertain to EEGLAB connectivity, checking for
new versions of EEGLAB, and allowing to see menu items from previous EEGLAB versions. 
  
- The last option, "size of cache", allows users to specify cache size limit in RAM when working with EEGLAB studies.

### Advanced option interface

If you select the option to show *advanced options*, you will be able to set additional options (not shown). These should be used with care as they could make EEGLAB unstable. Below is the list of additional advanced options.

- Files may be written using Matlab 6.5 file format, which is the most compatible format. Uncheck this option to write in Matlab 7.3 format, which allows saving individual data files larger than 2Gb.

- You may force EEGLAB to use double-precision numbers. Unless
you have a good reason to do so, you should leave that checkbox checked as EEGLAB will automatically convert the data to double-precision whenever this becomes necessary (filtering, running ICA, etc.).

- You may ask EEGLAB to process EEG datasets directly on disk (memory mapping), as this
is done for fMRI. This should remove any constraint on file size. This is a beta option that should only be used if you have memory limitations that prevent you from processing your data. Using this option may potentially create problems with EEGLAB plugins.

- You may use EEG objects instead of EEG structures.
From the user perspective, it will not change anything. However, it
allows EEGLAB to process objects that are not native to EEGLAB. For
example, another software could use EEGLAB function by passing on an
object as long as it behaves in a specific way. This option
should only be used by expert users, as it could trigger instabilities.

- Another option scales ICA component activities to RMS microvolt. 
  This
scaling does not change anything in terms of data processing. When
scaling ICA component activities, ICA scalp topographies are scaled as
well, so the product of the two remains constant. This scaling was not
performed in early versions of EEGLAB. There is no reason to uncheck that
option unless you want to preserve backward compatibility with early
versions of EEGLAB.

- Another option allow ignoring MATLAB toolboxes
even if they are present in the path. This may be useful when your
university has reached its quota in terms of toolbox users. In this
case, the extra toolbox functions exist in the path, but you may not use
them. Do not check that box unless you have a very good reason to do so, as it could make MATLAB unstable.

The icadefs.m file
-------------------
Using a text editor, you should edit file "icadefs.m" in the
distribution before beginning to use EEGLAB. This file contains EEGLAB
constants used by several functions. In this file, you may:

- Change the default folder for the EEGLAB option file

- Change y-axis direction for plotting ERPs

- Change font and color settings of the EEGLAB interface

-   Reference the binary version of the *runica.m* ICA function
    *ica* (see the [Binica repository](https://github.com/sccn/binica). For example, *ICABINARY = 'ica_linux2.4'*.

The dipfitdefs.m file
----------------------
The dipfitdefs.m contains other constants pertaining to dipole
localization, default models, and default electrode files.

