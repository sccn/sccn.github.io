---
layout: default
title: Tutorial data
long_title: Tutorial data and publicly available EEG data
parent: Tutorials
---
EEG data available for public download
===

Download data used in the workshops and in tutorials
-------------------------------------

You may download and uncompress the anonymized data
used in the [online workshop](/workshops/Online_EEGLAB_Workshop) and EEGLAB tutorial below.

- The [EEGLAB distribution](https://sccn.ucsd.edu/eeglab/download.php) contains EEGLAB tutorials datasets "eeglab_data.set" and "eeglab_data_epochs_ica.set". These files may be found in the "sample_data" folder.
<blockquote>
<details>
  <summary>Sample experiment description</summary>
In this experiment, there were two types of events "square" and "rt";
"square" events correspond to the appearance of a filled disk in a green
colored square in the display and "rt" to the subject's button press. 
<br><br>
The disk could be presented in any of the five squares on the screen, one
with a green outline and the others with a blue one, distributed along the horizontal
axis. Here we only considered presentation on the left, i.e. positions 1
and 2 as indicated by the *position* field (at about 5.5 degrees and 2.7
degrees of horizontal visual angle, respectively). 
<br><br>
In this experiment, the
subject covertly attended to a selected location on the computer screen
(the green square) and responded with a quick thumb button press only
when the disk was presented at this location. They were to ignore
circles presented at the unattended locations (the blue squares). 
<br><br>
To
reduce the amount of data required to download and process, this dataset
contains only targets (i.e., "square") stimuli presented at the two
left-visual-field attended locations for a single subject. For more
details about the experiment, see <a href="http://sccn.ucsd.edu/science2002.html">this paper</a>.
<br><br>
When using events in an EEGLAB dataset, there are two required event
fields: *type* and *latency*, plus any number of additional user-defined
information fields. It is important to understand here that the names of
the fields were defined by the user creating the dataset, and that it is
possible to create, save, and load as many event fields as desired.
<br><br>
Note also that *type* and *latency* (lowercase) are two keywords
explicitly recognized by EEGLAB and that these fields *must* be defined
by the user unless importing epoch event information (Note: If only
field *latency* is defined, then EEGLAB will create field *type* with a
constant default value of 1 for each event). Unless these two fields are
defined, EEGLAB cannot handle events appropriately to
extract epochs, plot reaction times, etc.
</details>
</blockquote>

- [Sternberg task with 13 subjects (0.9 Gb)](https://sccn.ucsd.edu/eeglab/download/STUDYstern_125hz.zip) in EEGLAB STUDY format. This is a large file. Make
sure you have a fast and reliable Internet connection before attempting
this download. A PDF contained in the ZIP file contains a description of this experiment.

- [Semantic task with 5 subjects (0.4 Gb)](https://sccn.ucsd.edu/eeglab/download/STUDY5subjects.zip) in EEGLAB STUDY format. Optional download for
more STUDY exploration. A description of this task is included in [this section](/tutorials/10_Group_analysis/study_creation.html#description-of-the-5-subject-experiment-tutorial-data) of the tutorial.

- [Go-nogo categorization task with 14 subjects (0.4 Gb)](https://sccn.ucsd.edu/eeglab/download/animal_study.zip) in EEGLAB STUDY format. A complete description of the task, the raw data (4Gb), and some MATLAB files to process it are all available on [openneuro.org](https://openneuro.org/datasets/ds002680) in BIDS format.

- [Face categorization task with 18 subjects](https://openneuro.org/datasets/ds002718) in BIDS format.

Other EEG data available online
-----------
There is an increasing amount of EEG data available on the internet. The list below is by no way exhaustive but may hopefully get you started on your search for the ideal dataset.

- A [web page](https://sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html) started in 2002 that contains a list of EEG datasets available online.

- The [OpenNeuro](https://openneuro.org/) database contains about 40 EEG studies in BIDS format.

- The [ERPcore](https://erpinfo.org/erp-core) resource is a freely available online resource consisting of optimized paradigms, experiment control scripts, example data from 40 participants.

- [Head-IT](https://headit.ucsd.edu/) is a legacy database containing ten experiments.