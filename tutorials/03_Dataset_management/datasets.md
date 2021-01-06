---
layout: default
title: 3. Dataset management
parent: Tutorials
nav_order: 3
---
Managing datasets in EEGLAB
=========================

This section deals with the basics of manipulating EEGLAB datasets. To illustrate the process, we will be loading the tutorial dataset and modifying it.

Load the sample EEGLAB dataset
------

Select menu item <span style="color: brown">File</span> and press sub-menu item
<span style="color: brown">Load existing dataset</span>. Select the tutorial file "eeglab_data.set", which is distributed with
the toolbox, located in the "sample_data" folder of EEGLAB. Then press *Open*.

![Image:Pop_loadset.png](/assets/images/Pop_loadset.png)

Modify and store the dataset
------

We need to modify the dataset for illustrative purposes, so we will only filter it. Select <span style="color: brown">Tools → Filter the data → Basic FIR filter (new, default)</span>, enter *1* as the *Lower edge* frequency in Hz (the first edit box), and press *OK*.

Upon modifying a dataset, EEGLAB asks users what to do with the modified dataset, as shown below. The default settings are to store the new datasets in memory while keeping the first dataset. Users may also decide to overwrite the original dataset in memory by clicking the appropriate checkbox below. At this point, it can be quite useful to edit the dataset
description -- to store the exact nature of the new dataset for future reference. Do this by pressing
*Description*. When done, press *Ok*.

![Image:pop_newset_new.png](/assets/images/pop_newset_new.png)

Upon storing a new dataset (not overwriting it), you may use the EEGLAB menu item <span style="color: brown">Dataset</span> to visualize and navigate between datasets available in memory as shown below. It is possible to select any dataset in this menu.

![Image:eeglab_dataset_menu.png](/assets/images/eeglab_dataset_menu.png)

Saving a dataset
------

Note that storing the new dataset in Matlab memory does not
automatically store it permanently on disk.  To do this, select
<span style="color: brown">File → Save current dataset(s)</span> to resave a modified dataset and overwrite the original file or <span style="color: brown">File → Save current dataset as</span> to save a new data file.

When saving a new data file, a file-browser window appears. Entering a name for the dataset
(which should end with the filename extension *.set*), and pressing
*SAVE* (below) will save the dataset, including
all its ancillary information re events, channel locations, processing
history, etc., plus any unique structure fields you may have added
yourself.

![Image:Saveepoch.png](/assets/images/Saveepoch.png)

Deleting a dataset
------

To delete from the Matlab memory the newly created second dataset, select
<span style="color: brown">File → Clear dataset(s)</span> or
<span style="color: brown">Edit → Delete dataset(s)</span> and enter the
dataset index, "2" as shown below, and press *OK*.

![Image:Delete.png](/assets/images/Delete.png)

The second dataset will now be removed from the EEGLAB/Matlab
workspace. (Note: It is not necessary to switch back to the first
dataset before deleting the second. It is also possible to delete
several datasets at once from this window by entering their indices
separated by spaces.) If the dataset has not been saved on disk, it will be lost.

To delete a dataset file, simply delete the file(s) from disk outside of Matlab.

Dataset and file preferences
------

Call menu item <span style="color: brown">File → Preferences</span>. Dataset and file preferences are the first three items shown below.

![Image:preferences.png](/assets/images/preferences.png)

The first option determines if more than one dataset may be stored in memory. We will be selecting this option when performing group analysis, as it is often not possible to hold all datasets in memory. When this option is selected, the drawback is that users must either save or overwrite the parent, as shown below (one of the checkboxes in the lower section must be selected).

![Image:pop_newset_overwrite.png](/assets/images/pop_newset_overwrite.png)

Going back to the list of options, by default, EEGLAB will save two files for each dataset. One file that contains metadata (with extension .set, and is a type of Matlab file), and one file containing raw data (float32 with .fdt extension). The second option makes it possible to save a single file.

The third option allows you to save Matlab files (the .set file) in different formats. It is best to write files in the Matlab 6.5 format because it is faster and Octave compatible. When dealing with individual data files larger than 2Gb, one may choose to save in the Matlab 7.3 format. Note that this last option is also relevant if you are concerned about files taking too much space on disk (as opposed to files in 6.5 format, files in 7.3 format are compressed).

