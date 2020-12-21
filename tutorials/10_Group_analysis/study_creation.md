---
layout: default
title: b. STUDY Creation
parent: 10. Group analysis
grand_parent: Tutorials 
---

Creating a STUDY
====================

This part of the tutorial will demonstrate how to create an EEGLAB
STUDY. 

Loading the STUDY example
--------------------------
For this tutorial, the measures needed for data visualization,
clustering and cluster visualization have already been computed, as
described below in the following section, and are stored with the
datasets - [download the full studyset here](ftp://sccn.ucsd.edu/pub/5subjects_full.zip) (\~450Mb). 

Another dataset often used in EEGLAB tutorial is the STERN dataset [download the
full studyset here](ftp://sccn.ucsd.edu/pub/STUDYstern.zip) (2.3Gb).

Both datasets are downloadable using the FTP protocol - which is outdated
so let us know if you experience problems (we will soon migrate all
downloads to HTTPS).

#### Description of 5-subject experiment for tutorial data: 

These data were acquired by Peter Ullsberger and colleagues from five subjects
performing an auditory task in which they were asked to distinguish
between synonymous and non-synonymous word pairs (the second word
presented 1 second after the first). 

Data epochs were extracted from 2
sec before the second word onset to 2 sec after the second word onset.

After decomposing each subject's data by ICA, two EEG datasets were
extracted, one (Synonyms) comprising trials in which the second word was
synonymous with the first one, and one (Non-synonyms) in which the
second word was not a synonym of the first. 

Thus the study includes 10
datasets, two condition datasets for each of five subjects. Since both
datasets of each subject were recorded in a single session, the
decompositions and resulting independent component maps are the same
across both conditions for each subject.

After downloading the sample STUDY data, unzip it in a folder of your
choice (preferably in the 'sample_data' sub-folder of the EEGLAB release
you are currently using; under Linux use the 'unzip' command). This will
create a sub-folder '5subjects' containing several studysets. Then open
a Matlab session and run *\>\> eeglab*.

### Data organization

The tutorial data is already optimally organized. However, when creating
a new STUDY, it is preferable to organize your data before running the
STUDY functions. 

We suggest creating one directory or folder per
subject, then storing the EEG dataset (".set") files for that subject in
this folder. The STUDY functions will then automatically add measure
files to the same subject directories.

We also advise modifying the default EEGLAB memory options. Selecting
menu item <span style="color: brown"> File → Memory and other options</span> will
pop-up the following window:


![Image:Pop_editoptions.jpg](/assets/images/Pop_editoptions.jpg)




Set the first option so that no more than one dataset is stored in
memory at a time. Dataset data arrays are then read from disk whenever
EEGLAB requires access to the data, but without cluttering memory. This
will allow Matlab to load and hold a large number of dataset structures
forming a large STUDY. 

Also, unset the third option so ICA component
activations do not get recomputed automatically. This saves time as
datasets are re-saved automatically during computation of measures and
clustering of ICA components.

Creating a new STUDY structure and studyset
---------------------------------------------

To create a studyset: select menu item
 <span style="color: brown">File → Create study → Browse for datasets</span>.

Another option is to load into
EEGLAB all the datasets you want to include in the study and select
menu item 
<span style="color: brown">File → Create study → Using all loaded datasets</span>. 
A blank interface similar to the one described above
will appear. In this window, first enter a name for the studyset
('N400STUDY'), a short description of the study ('Auditory task:
Synonyms Vs. Non-synonyms, N400'). 

Here, we do not add notes about the
study, but we recommend that you do so for your own studies. The
accumulated notes will always be loaded with the study, easing later
analysis and re-analysis. 

Click on the *Browse* button in the first
blank location and select a dataset name. 

The interface window should
then look like the following:


![975px](/assets/images/Pop_study_empty.gif)


<u>Warning:</u> Users of  Matlab 7.x under a Linux distribution: do not copy and paste
information into the edit boxes. Though it *appears* that this works,
Matlab 7 does not correctly register such inputs. Enter all
information manually (except the 'browsed' dataset names). This
problem does not seem to arise under Windows.


Note that here the fields *Subject* and *Condition* (below) have been filled
automatically. This is because the datasets already contained this
information. 

For instance, if you were to load this dataset into
EEGLAB by selecting menu item <span style="color: brown">Edit → Dataset info</span>, you would be able to edit the *Subject* and *Condition*
information for this dataset (as shown below). 

You may also edit it within the study itself, since dataset information and study dataset
information may be different to ensure maximum flexibility. For
instance, if you want one dataset to belong to several studies, but
play different roles in each.

Note: Use the checkbox *Update dataset information...* to maintain
consistency between dataset and studyset fields. However, if you check
this option, datasets may be modified on disk by clustering functions.


![Image:Pop_editset.gif](/assets/images/Pop_editset.gif)


Enter all datasets for all subjects in the STUDY, so that the STUDY
creation gui looks like this:


![875px](/assets/images/Pop_study.gif)


After you have finished adding datasets to the study, press *OK* in
the { {File\|pop_study.m} } gui to import all the dataset information.
We strongly recommend that you also save the STUDY as a studyset by
filling in the bottom edit box in the gui, or by selecting the EEGLAB
menu item <span style="color: brown">File → Save study as</span> after closing
the { {File\|pop_study.m} } window.

*Important note for ICA component clustering*:
 
 Continuous data collected in one task or
experiment session are often separated into epochs defining different
task conditions (for example, separate sets of epochs time locked to
targets and non-targets respectively). Datasets from different
conditions collected in the same *session* are assumed by the clustering
functions to have the same ICA component weights (i.e., the same ICA
decomposition is assumed to have been applied to the data from all
session conditions at once). If this was not the case, then datasets
from the different conditions must be assigned to different
*sessions*.

Loading an existing studyset
-------------------------------

Either use the studyset created in the previous section or load
another studyset. To load a studyset, select menu item
<span style="color: brown">File → Load existing study</span>. Select the file
*N400.study* in the folder *5subjects*. After loading or creating a
study, the main EEGLAB interface should look like this:

![Study Window](/assets/images/Eeglab_study_window.gif)

An EEGLAB STUDY (or study) contains descriptions of and links to data
contained in one to many epoched datasets, for example a set of
datasets from a group of subjects in one or more conditions of the
same task, or performing different tasks in the same or different
sessions. 

Other designs are possible, for instance a number of
different task conditions from the same subject collected during one
or more sessions. 

The term *STUDY* indicates that these datasets
should originate from a single experimental STUDY and have comparable
structure and significance. When in use, studyset datasets are
partially or totally loaded into EEGLAB. They thus may also be
accessed and modified individually, when desired, through the main
EEGLAB graphic interface or using EEGLAB command line functions or
custom dataset processing scripts.


In the EEGLAB gui (above): 
- *Epoch consistency* indicates whether or
not the data epochs in all the datasets have the same lengths and
limits 
- *Channels per frame* indicates the number of channels in each
of the datasets (*It is possible to process datasets with different
numbers of channels*)
- *Channel location* indicates whether or not
channel locations are present for all datasets. 

Note that channel
locations may be edited for all datasets at the same time (simply call
menu item <span style="color: brown">Edit → Channel locations</span>). 

- *Clusters*  indicates the number of component clusters associated
with this STUDY. There is always at least one cluster associated with
a STUDY. This contains all the pre-selected ICA components from all
datasets
- *Status* indicates the current status of the
STUDY. In the case above, this line indicates that the STUDY is ready
for pre-clustering. 

Below, we detail what the *STUDY* terms
"subjects", "conditions", "sessions", and "groups" mean.


To list the datasets in the STUDY, use menu item
<span style="color: brown">Study → Edit study info</span>. 

The following
window will pop up:

![875px](/assets/images/Pop_study.gif)


- The top of the window contains information about the STUDY, namely its
running name, the extended task name for the STUDY, and some notes.

- The next section contains information about the 10 datasets that are
part of the STUDY. For each dataset, we have specified a subject code
and condition name. 

We chose to leave the session and group labels
empty, as they were irrelevant for this STUDY. This is because for this STUDY, there
was only one subject group and data for both experimental conditions
were collected in a single session, so the same ICA decomposition was
used for both conditions. Uniform default values will be used by
EEGLAB for those fields. 

- The *Components* column contains the
components for each dataset that will be clustered. 

Note that if you
change the component selection (by pressing the relevant push button),
all datasets with the same subject name and the same session number
will also be updated (as these datasets are assumed to have the same
ICA components).


Each of the datasets EEG structures may also contain subject, group,
session, and condition fields. They do not necessarily have to be the
same as those present in the STUDY. For example, the same dataset may
represent one condition in one STUDY and a different condition in
another STUDY.

In general, we prefer the dataset information to be consistent with
the studyset information -- thus we check the first checkbox above.
 The second checkbox removes all current cluster information. When
cluster information is present, it is not possible to add or remove
datasets and to edit certain fields (because this would not be
consistent with the already computed clusters). Re-clustering the
altered STUDY does not take much time, once the pre-clustering
information for the new datasets (if any) has been computed and
stored.

-   The third checkbox allows the STUDY to be saved (or re-saved) as a
studyset (for example, *MyName.std*).

Both raw data and ICA component data may be processed in STUDY. 

### Optional: Pre-selecting components for clustering.

If you wish to process ICA component data with the STUDY you need to complete the step below.

Simply press the *Select by r.v.* (r.v. = residual variance) push
button in the gui above. 

The entry box below will appear. This allows
you to set a threshold for residual variance of the dipole model
associated with each component.


*Note*: Using this option requires that dipole model information is
present in each dataset. Use EEGLAB plug-in { {File\|dipfit.m} }
options and save the resulting dipole models into each dataset
*before* calling the study guis. Otherwise, options related to dipole
localization will not be available.


![Pop study rv gui](/assets/images/Pop_study_rv.gif)


This interface allows specifying that components used in clustering
will only be those whose equivalent dipole models have residual dipole
variance of their component map, compared to the best-fitting
equivalent dipole model projection to the scalp electrodes, less than
a specified threshold (0% to 100%). The default r.v. value is 15%,
meaning that only components with dipole model residual variance of
less than 15% will be included in clusters. This is useful because of
the modeled association between components with near 'dipolar' (or
sometimes dual-dipolar) scalp maps with physiologically plausible
components, those that may represent the activation in one (or two
coupled) brain area(s). For instance, in the interface above, the
default residual variance threshold is set to 15%. This means that
only component that have an equivalent dipole model with less than 15%
residual variance will be selected for clustering. Pressing *OK* will
cause the component column to be updated in the main study-editing
window. Then press *OK* to save your changes.

Editing STUDY datasets
-----------------------
Selecting an individual dataset from the
<span style="color: brown">Datasets</span> menu allows editing individual
datasets in a *STUDY*. 

Note, however, that creating new datasets or
removing datasets will also remove the *STUDY* from memory since the
study must remain consistent with datasets loaded in memory (here,
however, EEGLAB will prompt you to save the study before it is deleted).


EEGLAB also allows limited parallel processing of datasets of a
*STUDY* in addition to computing clustering measures during
pre-clustering. You may, for instance, filter all datasets of a *STUDY*.
To do so, simply select menu item <span style="color: brown">Tools → Filter data</span>. You may also perform ICA decomposition of all datasets by
running ICA individually on each of the datasets.


You may also select specific datasets using the
<span style="color: brown">Datasets → Select multiple datasets</span> menu item
and run ICA on all the datasets concatenated together (the ICA graphic
interface contains a self-explanatory checkbox to perform that
operation). 

This is useful, for example, when you have two datasets for
two conditions from a subject that were collected in the same session,
and want to perform ICA decomposition on their combined data. Using this
option, you do not have to concatenate the datasets yourself; EEGLAB
will do it for you.


