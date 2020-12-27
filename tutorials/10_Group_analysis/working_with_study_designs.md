---
layout: default
title: c. STUDY designs
parent: 10. Group analysis
grand_parent: Tutorials 
---
Working with STUDY design
===========================
{: .no_toc }

STUDY designs allow performing statistical comparisons of multiple trial and dataset
subsets of a STUDY without creating and storing the STUDY more than
once. All the statistical designs are contained in the STUDY structure
as (STUDY.design) sub-structures. 

For instance, In an oddball paradigm comprising trials time
locked to oddball, distractor, and standard stimuli, a user might want
to contrast oddball and distractor responses, considered together, with
responses to standard stimuli. One might also want to look for
differences between responses to oddball and distractor stimuli. This can be handled by
defining a single STUDY structure with multiple STUDY designs.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

One-way STUDY design
-------------------

For this tutorial we will use the [STERN STUDY](http://sccn.ucsd.edu/eeglab/download/STUDYstern.zip) (2.3Gb). Please download the data on your computer.

### Description of STERN experiment tutorial data

The classic Sternberg working memory task involves presentation of a list of seven letters to memorize, presented one at a time. These letters, colored in green, are interspaced with letters to ignore, colored in red, and followed by a memory maintenance period during which the subject must maintain the list of items in memory. The maintenance period is terminated by the onset of a *probe* letter, to which the subject must respond whether the item was in their memorized list of items or not.

Trials contained varying numbers of ignore letters (either 1, 3 or 5), and the order of memorize and ignore letters in a given trial was randomized.

Event codes are the following:
- Memorize letters: “uppercase letter”, for example, ‘B’, ‘H’, ‘W’,’F’, etc...
- Ignore letters: “lowercase ‘g’, uppercase letter”, for example, ‘gB’, ‘gH’, ‘gW’,’gF’, etc... (‘g’ stands for ‘green’, see above explanation)
- Probe letters: “lowercase ‘r’, uppercase letter”, for example, ‘rB’, ‘rH’, ‘rW’,’rF’, etc... (‘r’ stands for ‘red’, see above explanation)

The PDF document within the zip archive contains additional details about the task.

### Looking at the STUDY information

Use menu item <span style="color: brown">File → Load existing study</span> and select the *stern.study* file. After the *STUDY* is loaded in EEGLAB,  select menu item <span style="color: brown">Study → Edit study info</span>. The following interface will pop up.

![Image:studydesign6.png](/assets/images/studydesign6.png)

This interface contains information about the *STUDY*, in particular the list of datasets and condition, session and run associated with them. It is described in detail in the [STUDY creation tutorial](/tutorials/10_Group_analysis/study_creation.html). In this case, it shows that for each subject, we have three epoched datasets, one containing letters to *memorize*, one containing letters to *ignore* letters data epochs, and one containing *probe* letters.

### Looking at current STUDY design

To edit the *STUDY* design, simply select
the second *STUDY* menu item <span style="color: brown">Study → Select/Edit study design(s)</span>. This will pop up the following interface.

![Image:Studydesign.jpg](/assets/images/studydesign7.png)

The three push buttons on the top pannel may be used to:
 - add a new design ("Add
design"), 
- rename a given design ("Rename design"),
- or delete a given
design ("Delete design"). 

Note that the first design cannot be deleted.
The reason the design does not have a name is that it was generated automatically when importing the data. You press the *Rename* button and name the design *Comparing memorize, ignore, and probe letters*.

The four push buttons on the bottom pannel may be used to:
- add a new independent variable to the current design. 
- edit an independent variable
- delete and independent variable
- list independent variables

Press the *Edit* button. The following GUI pops up. We can see that the *condition* independent variable is selected. We can also see that the two conditions are *ignore* (letters), *memorize* (letters), and  *probe* (letters).

![Image:Studydesign.jpg](/assets/images/studydesign8.png)

When using standard EEGLAB statistics, up to two categorical independent variables may be defined (two rows on lower pannel). When using the *LIMO* plugin to perform statistics, an arbitrary number of continuous and categorical variables may be used.
- Categorical variables are variable that takes discrete values, such as conditions (in this case *gnore* vs *memorize* vs *probe* letters)
- Continuous variables are variable that takes continuous values, such as reaction time.

Once an independent variable is selected, it is possible to
select only a subset of its values. All the datasets or trials not
selected will simply not be included when plotting measures for that design. For instance, in this specific example, the independent variable *condition*
may take the values *ignore* and *memorize* only to compare between the two types of letters. 

Press *Ok* to go back to the *STUDY* design interface. Now press the *List factor* button. These are the list of independent variable values (or beta parameters) in case you use a general linear model in the LIMO plugin hierarchical analysis. Refer to the [LIMO plugin documentation](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki) for more information.

![](/assets/images/studydesign30.png)

### Creating a new STUDY design

To illustrate how to manipulate *STUDY* designs, we are going to create an equivalent design using event types instead of dataset conditions. 
Press the *New* design button. Then, press the *Rename* button and rename the new design *Same as first design but using event types*. 

Then, select the *New* button in the independent variable pannel (lower pannel). The following window pops up. Select *type* for the independent variable. 
- Select all the letters not preceded by *g* or *r*. These are the *memorize* letters. Press the *combine* button to combine these letters.
- Select all letters preceded by *g*. These are the *ignore* letters. Press the *combine* button to combine these letters.
- Select all letters preceded by *r*. These are the *probe* (recall) letters. Press the *combine* button to combine these letters.
Go down to the bottom of the letter list and select the three sets of combined event types. 

![Image:Studydesign.jpg](/assets/images/studydesign9.png)

This selection is equivalent to selecting the three conditions in the previous design. However, it is conceptually quite different. In the first case, we are comparing between trials contained in different datasets (i.e., EEGLAB data files). In the second case, we are only selecting event types, which may be in one dataset, or in several datasets.

The list of independent variables is automatically generated
based on the STUDY definition information and also based on events from
each of the datasets. Every single event field (as visible in the <span style="color: brown">Edit → Event values</span>) is automatically made visible. Note that only information about the time-locking event is shown and other events within data epochs are ignored. However, EEGLAB populates empty fields within data epochs with information from other events within the same epochs. For example, events might have a field *correct* belonging to *reaction time* events (not the time-locking event) containing true or false. All events have the same fields so other events will also have a *correct* event field, which will be empty since it is not defined for these events. If this is the case, then the value (true or false) is automatically copied to all events within a given epoch, and may be selected as an independent variable in the GUI above. For details on what information from dataset is
being extracted, refer to the [STUDY design structure](/tutorials/multi-subject/EEGLAB-STUDY-data-structure.html)
tutorial. 

See also the [event scripting tutorial](/tutorials/11_Scripting/Event_Processing_command_line.html#adding-event-information-for-group-analysis) for defining new independent variable based on event context.

### Plotting ERPs for two designs

We describe in detail data plotting in the group analysis data [vizualisation tutorial](/tutorials/10_Group_analysis/study_data_visualization_tools.html). However, we will plot and compare the ERPs for these two designs. 

First, we need to precompute measurs. Select menu item <span style="color: brown">Study → Precompute channel measures</span>, click the *ERP* checkbox and press *Ok* (interface not shown). Then select menu item <span style="color: brown">Study → Plot channel measures</span>. The following interface pops up. Select electrode *Oz*.

![](/assets/images/studydesign13.png)

Press the *Params* button and select the central checkbox to plot the first independent variable on the same pannel as shown below. Press *Ok* to come back to the *STUDY* plotting GUI.

![](/assets/images/studydesign12.png)

Press the *Plot ERPs* pushbutton to plot the ERP for the first channel in the list. The following plot showing the grand-average ERP for each condition will pop up.. Then in the upper part of the *STUDY* plotting GUI, switch to the other design and again press the *Plot ERPs* button. The two plots are shown below side by side.

![](/assets/images/studydesign10.png)

The conditions are assigned different colors but the ERPs are identical in both conditions. 

Two-way STUDY design
--------------------------

Each letter is preceeded by other letters. Thus, when each letter is presented is presented, there is a memory load from 0 (no other letter to remember yet) to 7 (7 letters to remember).

Again select
the second *STUDY* menu item <span style="color: brown">Study → Select/Edit study design(s)</span>. Create a third design called *2-way design, letter type x load*.

![](/assets/images/studydesign21.png)

For this design, use two independent variables, one is the type of letter and we select *ignore* and *memorize* (since *load* is irrelevant for *probe* letters). We also select the memory load from 0 to 7 and change the type of variable to *categorical* instead of *continous* (it would also be possible to select *continuous* but this would require using the LIMO plugin to compute statistics and plot results).

![](/assets/images/studydesign22.png)

Since we have pre-computed measure in the previous section, there is no need to do that again - prior to EEGLAB 2019, one had to recompute measures for each design, but this is no longer necessary. Select menu item <span style="color: brown">Study → Plot channel measures</span>. Select electrode *Oz* and press the *Plot ERPs* button. The following plot pops up.

![](/assets/images/studydesign23.png)

Here we have one pannel per memory load. For memory load 7, there is no condition memorize (the load for the memorize letters goes from 0 to 6 which correspond to the number of letter already memorized). Note that the number of letters for the condition 6 is low (a total of 31 for the *ignore* condition) explaning the large amplitude artifacts. This comparison should be run only for load 0 to 5. To interpret this plot, we would need to select a shorter frequency range, overlay loads for both the *memorize* and *ignore* conditions.

This simple example shows that the range of possibilities for STUDY
designs is large. More details about STUDY.design structure is available
in the [STUDY structure](/tutorials/multi-subject/EEGLAB-STUDY-data-structure.html)
part of the tutorial.

For more complex designs, one must use the LIMO plugin. Refer to the [LIMO plugin documentation](https://github.com/LIMO-EEG-Toolbox/limo_meeg/wiki) for more information. 