---
layout: default
title: Quick Tutorial on Rejection
parent: Reference Topics
grand_parent: Tutorials
nav_order: 12
---

Quick tutorial on rejecting data artifacts with EEGLAB
========================================================

Independent Component Analysis is a powerful tool for eliminating
several important types of non-brain artifacts from EEG data. 

EEGLAB allows the user to reject many such artifacts in an efficient and
user-friendly manner. 

This short tutorial is designed to guide  users who want to try using EEGLAB to remove artifacts from their data.

1. Start Matlab and EEGLAB, then import your data
-----------------------------------------------
Type \>\> eeglab to start EEGLAB under Matlab. 

Select menu item
<span style="color: brown">File → Import data</span> to import your data file
in any of a variety of file formats including EGI and Neuroscan binary.
See the [Import data](/tutorials/04_Import/Importing_Continuous_and_Epoched_Data) section for
more details.

Scroll and check data using menu item <span style="color: brown">Plot → Channel data (scroll)</span>.

2.Import a channel location file
----------------------------------
Importing a channel location file is critical for visualizing the
independent components of your data.

Select menu item <span style="color: brown">Edit → Channel locations</span>
and press the button *Read locations* in the bottom right corner of the
channel edit window.

The program recognizes channel location files in
most known formats (spherical BESA, polar Neuroscan, 3-D cartesian EGI,
3-D cartesian Polhemus, ...). P

ress *OK* after selecting the file and
then press *OK* to have EEGLAB recognize the file format automatically
from the file extension. 

*Note:* files with extension ".elp" are
considered Polhemus files by default and not BESA files. 

Press *OK* in
the channel edit window to import the channel locations into EEGLAB.

To check that your channel locations have been imported correctly, use
menu item <span style="color: brown">Plot → Channel locations → By name</span>

3.Reject artifact-laden data
-------------------------------

The quality of the data is critical for obtaining a good ICA
decomposition. ICA can separate out certain types of artifacts -- only
those associated with fixed scalp-amp projections. 

These include eye
movements and eye blinks, temporal muscle activity and line noise. ICA
may not be used to efficiently reject other types of artifacts -- those
associated with a series of one-of-a-kind scalp maps.

For example, if
the subject were to scratch their EEG cap for several seconds, the
result would be a long series of slightly different scalp maps
associated with the channel and wire movements, etc. Therefore, such
types of "non-stereotyped" or "paroxysmal" noise need to be removed by
the user before performing ICA decomposition.

To reject “noisy channels“ of either continuous or epoched data, select
menu item <span style="color: brown">Edit → select data</span>.

To reject noisy portions of “continuous data”, select menu item
<span style="color: brown">Tools → Reject continuuous data </span>.
 then mark noisy portions of continuous data for
reject by dragging the mouse horizontally with the left button held
down.

Press *Reject* when done. 

A new window pops up to ask for a name
for the new dataset.

To reject noisy “data epochs”, select menu item
<span style="color: brown">Tools → Reject data epochs → Reject by inspection</span>. 

Check the second checkbox to reject data at once
(instead of simply marking epochs for rejection) and press *OK*. 

Then,
in the scrolling window, click on data epochs you wish to reject. If you
change your mind about a data epoch marked for rejection, click it again
to un-select it. 

Press *Reject* when done. 

A new window pops up to ask
for a name for the new dataset.

EEGLAB also has facilities to automatically suggest data channels,
portions and/or epochs to reject. See menu item
<span style="color: brown">Tools → Reject data epochs → Reject data (all methods)</span>. See the [Data
rejection](/Chapter_01:_Rejecting_Artifacts "wikilink") tutorial for
more details.

4.Run ICA, select and reject artifactual components
------------------------------------------------------
Use menu <span style="color: brown">Tools → Run ICA</span> to run the ICA
algorithm. 

To accept the default options, press *OK*.

Use menu <span style="color: brown">Tools → Reject data using ICA → reject component by maps</span> to select artifactual components. See the [Data
analysis (running
ICA)](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink") tutorial for
more details.

Select menu item <span style="color: brown">Tools → Remove components</span>
to actually remove the selected component from the data.

See the [Data analysis (running
ICA)](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink") tutorial for
more details and some hints on how to select artifactual components.

5.Further processing of and/or exporting the cleaned data
-----------------------------------------------------------
Your data has now hopefully been pruned of its major artifactual
components. You may now proceed with further EEGLAB processing of the
remaining non-artifactual independent components (see [Data analysis
(working with ICA
components))](/Chapter_09:_Decomposing_Data_Using_ICA "wikilink").

You may also export your data by selecting menu item
<span style="color: brown"> File → Export → Data and ICA activity to text file </span>(EEGLAB v4.1). (Note: We believe Neuroscan versions 4.1 and
higher can import data files in text format.)

