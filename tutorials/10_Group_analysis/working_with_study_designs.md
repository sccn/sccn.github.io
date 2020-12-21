---
layout: default
title: c. STUDY designs
parent: 10. Group analysis
grand_parent: Tutorials 
---


Working with STUDY design
===========================

The STUDY.design structure is a concept introduced in EEGLAB v9.
It allows performing statistical comparisons of multiple trial and dataset
subsets of a STUDY without creating and storing the STUDY more than
once. All the statistical designs are contained in the STUDY structure
as (STUDY.design) sub-structures. 

For instance, a STUDY might contain
datasets for 5 conditions comprising a 2x2 set of conditions for each
subject plus a 'novel' condition. 
Data from all five conditions might be
used to find clusters of similar independent component sources across
subjects. 

However, statistical comparisons might be targeted to look at
the main effects and interactions among the 2x2 conditions only, at
differences between the 'novel' condition and each of the other four
conditions, etc. 

This can be handled, beginning in EEGLAB v9, by
defining a single STUDY structure with multiple STUDY.design
sub-structures.

The main advantages of using STUDY designs are detailed below:

-   No need to have one dataset per condition. 
An important restriction
of working with STUDY structures in EEGLAB 8.0 (prior to
STUDY.design) was that to compare multiple conditions users had to
generate one dataset per condition. However, to analyze the
influence of various contextual information about trials, it may be
relatively impractical to generate many datasets with specific sets
of trials. The new 'design' scheme in EEGLAB 9.0 is backward
compatible with EEGLAB 8 but allows for more flexibility, in
particular allowing the STUDY functions to dynamically extract
specified data trials from datasets. Each dataset may contain
several conditions or several datasets can be merged, using the
STUDY design facility, to form to one condition.

-   No restriction to studying "groups" and "conditions" only. Any
user-defined independent variable may now be used to contrast
different subsets of trials or datasets.

-   The ability to create and analyze different STUDY designs within the
same STUDY, each selecting only a subset of independent variable
values.

Simple STUDY design
-------------------

**Example:** In an oddball paradigm comprising trials time
locked to oddball, distractor, and standard stimuli, a user might want
to contrast oddball and distractor responses, considered together, with
responses to standard stimuli. One might also want to look for
differences between responses to oddball and distractor stimuli. 

If this STUDY has two subject groups, the user might want to look at the effect
of group on any of the response types, just focus an analysis on one
group, or look for Group by Condition interactions.
One might also want to temporarily exclude a subject from a data analysis. 

All of these
design concepts can be processed within a single **STUDY** using
multiple **STUDY.design** structures. 

Using multiple STUDY.design
structures may also be useful for testing different signal processing
options. For instance, one might create two identical STUDY designs, in
one computing the time/frequency measures using FFTs in one and using
wavelets in the other one. Once computed, you will be able to toggle
between design results so as to compare them.

Note that the tutorial STUDY for EEGLAB v9 is the same one that has been
available in the tutorial since 2006. A default design, implementing
EEGLAB processing of the whole STUDY (as per EEGLAB Version 8) is
automatically been created when the tutorial STUDY is first loaded. In
addition, all the precomputed measure files from v8 are preserved and
may be used. If you are importing an EEGLAB STUDY from a version prior
to v9 and not using the STUDY design menu, EEGLAB should behave exactly
as it did prior to version 9. 

### Editing the STUDY design

To edit the STUDY design, simply select
the second STUDY menu as shown below. Note that if you change the
default design (design(1)), your precomputed measure data files (STUDY
ERP, spectrum, ERSP and ITC) may be lost.




![Image:Studydesignmenu.jpg](/assets/images/Studydesignmenu.jpg)



This will pop up the following interface




![Image:Studydesign.jpg](/assets/images/StudyDesign.jpg)



The three push buttons at the top may be used to:
 - add a new design ("Add
design"), 
- rename a given design ("Rename design"),
- or delete a given
design ("Delete design"). 

Note that the default design (design(1))
cannot be deleted. Adding a design copies the current design and creates
a new design names "Design x" (x being the index of the new design).

- The "Independent variable 1" list helps define independent variables.
Currently, up to two independent variables may be defined (the two left
columns). The list of independent variables is automatically generated
based on the STUDY definition information and also based on events from
each of the datasets. 

For details on what information from dataset is
being extracted, refer to the [STUDY design structure]( /tutorials/multi-subject/EEGLAB-STUDY-data-structure.html)
tutorial. 

Once an independent variable is selected, it is possible to
select only a subset of its values. All the datasets or trials not
selected will simply not be included in the STUDY.design processing. 

For instance, in this specific example, the independent variable 'condition'
may take the values 'non-synonyms' and 'synonyms'. These values may be
combined by pressing the "Combine selected value" push button. In this
case, since there are only two values of the independent variable
"condition", this is irrelevant. 

The detailed example at the end of this
section shows an example of combining two values. Each independent
variable also has a pairing status ("paired statistics" for paired data
and "unpaired statistics" for unpaired data).

- The "Subject" list contains the subjects to include in a specific
design. Some subjects may be excluded or included. 

Note that it is
better to select all subjects before pre-computing all STUDY measures,
and then to exclude some subjects if necessary. When two groups of
subjects are included (patients versus controls, for instance), some
STUDY.design instances may include only one category of subjects.

### Selecting/excluding specific dataset or trials from design

Use the "Select only specific dataset/trials" push button to define a list
of independent variables and values to include in the design. 
Clicking
on the push button, "Select only specific dataset/trials," pops up the
following interface:




![Image:Studydesignselect.jpg](/assets/images/Studydesignselect.jpg)



In this interface, you may select specific independent variables with
specific values to include in the STUDY. 

This option is only relevant
for complex STUDY designs in which some sets of trials and/or datasets
are excluded.
 
 ressing the "Add" button will add the selection to the
edit box on the right of the "Select only specific dataset/trials" push
button in the STUDY design interface.

2-way design STUDY design
--------------------------

Below we show a more complex STUDY design scheme including 6 designs.
 
 In
this experiment, there were two groups of subjects, "control" and
"nondual" ( a type of meditation practice). There were also four types
of stimuli ("blank", "audio", "light" and "both" (audio and light)), two
sessions for each subject, and two presentation modes ("evoked" and
"spontanous"). 

Here, the stimulus type "audio - light" is not a real
stimulus type; it was obtained by selecting stimuli "audio" and "light"
and pressing the "Combine selected values" push button - see design
number 3 below for more details. These screen captures are courtesy of
the [Institute of Noetic Science](http://www.noetic.org).

In the first design, we contrast the two groups of subjects for the
"audio" and "visual" stimuli. There are two independent variables for
this design (a 3x2 design).



![Image:Studydesign_n0.jpg](/assets/images/Studydesign_n0.jpg)



In the second design, we only consider the "nondual" group subjects and
three types of stimuli ("audio", "light" and "blank"). There is only one
independent variable in this design (1x3 design).



![Image:Studydesign_n1.jpg](/assets/images/Studydesign_n1.jpg)




### Excluding specific subjects

In the third design, we only consider "nondual" subjects and compare two
types of stimuli ("blank" versus "audio - light"). The "audio - light"
condition groups together both "audio" and "light" trials - i.e. the
stimulus may have been of either type "audio" or "light". 

This design
helps contrast brain activity following stimulation compared to when no
stimulus was presented ("blank" condition). This is a simple 1x2
design.



![Image:Studydesign_n2.jpg](/assets/images/Studydesign_n2.jpg)




### Design with custom-defined event

In the fourth design, we were interested in analysing audio stimuli that
had been preceded by various types of stimuli. The independent variable
"prevevent" had to be defined using a script. 

A field was added to the
event structure using a custom script - it contained the previous
stimulus type for each time-locking event. For more information on how
to create and modify events in EEGLAB datasets, see [this section](/tutorials/advanced-topics/event-processing.html).

Once events are modified, they will be automatically detected at the
STUDY level - note that you have to modify events in all datasets
included in the design. In case, you already have an existing STUDY, you
might have to recreate a new one.

Note that in the design below, the edit box on the right of the "Select
only specific datasets/trials" GUI contains the string "'StimulusType',
{ 'audio' }". It indicates to EEGLAB that it should only consider this
type of stimulus in this design and ignore all trials of type "light",
"blank" and "both". This is a 1x3 design.



![Image:Studydesign_n3.jpg](/assets/images/Studydesign_n3.jpg)




### Other examples of STUDY design

In the fifth design, we compared brain responses to "light" and "audio"
stimuli in sessions 1 and 2. This is a 2x2 design.



![Image:Studydesign_n4.jpg](/assets/images/Studydesign_n4.jpg)



Finally, in the sixth design, we compared brain responses to "light" and
"audio" stimuli in "evoked" and "spontaneous" conditions. This is again
a 2x2 design.



![Image:Studydesign_n5.jpg](/assets/images/Studydesign_n5.jpg)



This simple example shows that the range of possibilities for STUDY
designs is large. More details about STUDY.design structure is available
in the [STUDY
structure](/tutorials/multi-subject/EEGLAB-STUDY-data-structure.html)
part of the tutorial.

<b>Note:</b> As of EEGLAB 12, a new row in the STUDY design graphic
interface allows selecting a specific folder to store STUDY design
files. This prevents encountering conflicts when several studies are
pointing to the same datasets. This also allow users to better organize
their data.
