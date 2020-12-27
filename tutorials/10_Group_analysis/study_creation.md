---
layout: default
title: b. STUDY Creation
parent: 10. Group analysis
grand_parent: Tutorials 
---

Creating a STUDY
====================
{: .no_toc }

This part of the tutorial will demonstrate how to create an EEGLAB
STUDY and perform simple plotting. 
An EEGLAB STUDY (or study) contains descriptions of and links to data
contained in one to many epoched datasets, for example a set of
datasets from a group of subjects in one or more conditions of the
same task, or performing different tasks in the same or different
sessions. 

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

Getting ready for group-level analysis
--------------------------

### Description of 5-subject experiment for tutorial data

In this tutorial, wew will use a [5-subject STUDY](http://sccn.ucsd.edu/eeglab/download/STUDY5subjects.zip) (450Mb). These data were acquired by Peter Ullsberger and colleagues from five subjects
performing an auditory task in which they were asked to distinguish
between synonymous and non-synonymous word pairs (the second word
presented 1 second after the first). 

Data epochs were extracted from 2
sec before the second-word onset to 2 sec after the second-word onset.

After decomposing each subject's data by ICA, two EEG datasets were
extracted, one (Synonyms) comprising trials in which the second word was
synonymous with the first one, and one (Non-synonyms) in which the
second-word was not a synonym of the first. 

Thus the study includes 10
datasets, two condition datasets for each of five subjects. Since both
datasets of each subject were recorded in a single session, the
decompositions and resulting independent component maps are the same
across both conditions for each subject.

After downloading the sample STUDY data, unzip it in a folder of your
choice (preferably in the 'sample_data' sub-folder of the EEGLAB release
you are currently using; under Linux use the 'unzip' command). This will
create a sub-folder '5subjects' containing several studies. Then open
a Matlab session and run *\>\> eeglab*.

Another *STUDY* sometimes used in EEGLAB tutorials is the [STERN STUDY](http://sccn.ucsd.edu/eeglab/download/STUDYstern.zip) (2.3Gb).

### Data organization

The term *STUDY* indicates that datasets
should originate from a single experimental STUDY and have comparable
structure and significance. 

The tutorial data is already optimally organized. However, when creating
a new STUDY, it is preferable to organize your data before running the
STUDY functions. 

We suggest creating one directory or folder per
subject, then storing the EEG dataset (".set") files for that subject in
this folder. The STUDY functions will then automatically add measure
files to the same subject directories.

### EEGLAB memory settings

We also advise modifying the default EEGLAB memory options. Call menu item <span style="color: brown">File → Preferences</span>. 
The first option determines if more than one dataset may be stored in memory. We will be selecting this option when performing group analysis, as it is often not possible to hold all datasets in memory.

![Image:preferences.png]({{ site.baseurl }}/assets/images/preferences.png)

When in use, *STUDY* datasets are
partially or totally loaded into EEGLAB. They thus may also be
accessed and modified individually, when desired, through the main
EEGLAB graphic interface or using EEGLAB command line functions or
custom dataset processing scripts. Dataset data arrays are then read from disk whenever
EEGLAB requires access to the data, but without cluttering memory. This
will allow Matlab to load and hold a large number of dataset structures
forming a large STUDY. 

Quick STUDY creation
---------------------------------------------
After uncompressing the [5-subject tutorial data](http://sccn.ucsd.edu/eeglab/download/STUDY5subjects.zip), to create a *STUDY*, select menu item
 <span style="color: brown">File → Create study → Simple ERP STUDY</span>. The interface belows pop up. Enter two for the number of conditions and five for the number of subjects, and press *Ok*.

![](/assets/images/simplestudy1.png)

Then enter the following information in the following interface. There are two columns of data files, one for the condition *synonym* (files *synXX-s253-clean.set) and one for the condition *non-synonym* (files *synXX-s254-clean.set*) with one row per subject. You may use the browse ("...") button to select the files. Name the *STUDY* "N400" and press *Ok*.

![](/assets/images/simplestudy3.png)

The following interfaces pop up. One is the grand average ERP across conditions for all electrodes. You may click on a trace to pop up a new figure. The other interface is the *STUDY* plotting graphic interface. This interface and how to use it is described in detail in the *STUDY* [vizualisation tutorial](/10_Group_analysis/study_data_visualization_tools.html).

![](/assets/images/simplestudy2.png)

This is it for creating a simple *STUDY*. In the rest of this tutorial page, we will describe an alternative method for creating a *STUDY*. This other method is more involved but allow setting additional parameters.

Creating a new STUDY
-----------------
To create a *STUDY*, select menu item
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
analysis and re-analysis. Note that here the fields *Subject* and *Condition* (above) have been filled
automatically. This is because the datasets already contained this
information. For instance, if you were to load this dataset into
EEGLAB by selecting menu item <span style="color: brown">Edit → Dataset info</span>, you would be able to edit the *Subject* and *Condition*
information for this dataset. You may also edit this information within the study itself. The dataset information and study dataset information may be different to ensure maximum flexibility, although we recommend to check the checkbox *Update dataset info...* to keep the dataset information consistent in case you modify it in the *STUDY*.

Click on the *Browse* button in the first blank location and select a dataset name. Do so for other datasets as well. 

The interface window should then look like the following:

![875px](/assets/images/studycreate.png)

Below, we detail what the *STUDY* terms *subjects*, *sessions*, *run*, *conditions*, and *groups* mean.

- The top of the window contains information about the STUDY, namely its
running name, the extended task name for the STUDY, and some notes.
- The next section contains information about the 10 datasets that are
part of the STUDY. For each dataset, we have specified a subject code
and condition name. 
- For each file, you may assign a session and run number. A run is when there are blocks in an experiment and the data from each block is stored in a separate file. Sessions are used when the data is collected on different days or when there is a break that involves removing the EEG cap. We chose to leave the session and run empty since there are irrelevant for this *STUDY* (there is only one session and one run).
- The *condition* column contains the condition associated with each file. Note that we have two files here per subject. However, it is also possible to have a single file per subject and to define conditions using EEGLAB event trial types. For more information on this topic, read the [STUDY design tutorial](/tutorials/10_Group_analysis/working_with_study_designs.html).
- The *group* column would indicate which group a subject belongs to. This is irrelevant for this STUDY since there
was only one subject group and data for both experimental conditions
were collected in a single session
- We will come back later to the *Select by r.v.* (select ICA component by residual variance) and the *Comp...* button when we perform ICA component clustering.
- Pressing the *Clear* button clears the information on a given row.

In general, we prefer the dataset information to be consistent with
the *STUDY* information -- thus we may check the first checkbox. The second checkbox removes all current cluster information and will be explained when we perform ICA component clustering.

After you have finished adding datasets to the study, press *OK* in the [pop_study.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m) GUI to import all the dataset information.

We strongly recommend that you also save the STUDY by selecting the EEGLAB
menu item <span style="color: brown">File → Save study as</span> after closing the [pop_study.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=pop_study.m) window.

Loading an existing STUDY
-------------------------------

Either use the studyset created in the previous section or load
another studyset. To load a studyset, select menu item
<span style="color: brown">File → Load existing study</span>. Select the file
*N400.study* in the folder *5subjects*. After loading or creating a
study, the main EEGLAB interface should look like this:

![Study Window](/assets/images/guistudy.png)

In the EEGLAB GUI (above): 
- *Epoch consistency* indicates whether or
not the data epochs in all the datasets have the same lengths and
limits 
- *Channels per frame* indicates the number of channels in each
of the datasets (*It is possible to process datasets with different
numbers of channels*)
- *Channel location* indicates whether or not
channel locations are present for all datasets. 
- *Clusters*  indicates the number of component clusters associated
with this STUDY. There is always at least one cluster associated with
a STUDY. This contains all the pre-selected ICA components from all
datasets
- *Status* indicates the current status of the
STUDY. In the case above, this line indicates that the STUDY is ready
for pre-clustering. 

To list the datasets in the STUDY, use menu item
<span style="color: brown">Study → Edit study info</span>. The interface described in the previous section will pop up.

### Editing STUDY datasets
Selecting an individual dataset from the
<span style="color: brown">Datasets</span> menu allows editing individual
datasets in a *STUDY*. 

Note, however, that creating new datasets or
removing datasets will also remove the *STUDY* from memory since the
study must remain consistent with datasets loaded in memory (here,
however, EEGLAB will prompt you to save the study before it is deleted).

### Reviewing the STUDY design

Another [section of the tutorial](/tutorials/10_Group_analysis/working_with_study_designs.html) describes *STUDY* designs in detail, but use different tutorial data. Our design is simple here, with only two conditions.

To edit the STUDY design, simply select
the second STUDY menu item <span style="color: brown">Study → Select/Edit study design(s)</span>.

![Image:Studydesignmenu.jpg](/assets/images/Studydesignmenu.jpg)

This will pop up the following interface.

![Image:Studydesign.jpg](/assets/images/studydesign1.png)

The top pannel contains the list of designs (in this case, a single design) and the bottom pannel contains the variables used in a specific design.

Let's rename the default design by pressing the *Rename* button to *Synonym vs non-synonym*. The following GUI pops up. Press *Ok*.

![Image:Studydesign.jpg](/assets/images/studydesign2.png)

Now, in the bottom pannel, click on the *Edit* button. The following GUI pops up. We can see that the *condition* independent variable is selected. We can also see that the two conditions are *non-synonym* and *synonym*.

![Image:Studydesign.jpg](/assets/images/studydesign3.png)

### What to do after creating your STUDY

We have already seen in this tutorial how to create a simple *STUDY* and plot the grand average ERP. This procedure bypass the standard *STUDY* pipeline which consists in first preprocessing the data and then plotting it, as we describe in the group analysis data [vizualisation tutorial](/tutorials/10_Group_analysis/study_data_visualization_tools.html).

If you are impatient, select menu item <span style="color: brown">Study → Precompute channel measures</span>, click the *ERP* checkbox and press *Ok*. Then select menu item <span style="color: brown">Study → Plot channel measures</span> and press the *Plot ERPs* pushbutton to plot the ERP for the first channel in the list. The following plot showing the grand-average ERP for each condition will pop up.

![875px](/assets/images/simplestudyplot.png)






